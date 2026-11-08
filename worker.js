// callery.co.uk Worker code. Only requests under /api/ come here (see run_worker_first in wrangler.jsonc);
// every other page is served straight from the static files, exactly as before.
//
// GET /api/waits/<park id>  ->  live ride waits for one park, from Queue-Times.com (free API, attribution
// "Powered by Queue-Times.com" required on any page that shows the data). Queue-Times updates every 5 minutes,
// so we cache for 2 minutes and never hit them more than that per Cloudflare location.

const PARKS = { 5: 'EPCOT', 6: 'Magic Kingdom', 7: 'Hollywood Studios', 8: 'Animal Kingdom' };
const TTL = 120; // seconds

function json(body, status = 200, maxAge = 60) {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      'content-type': 'application/json; charset=utf-8',
      'cache-control': status === 200 ? `private, max-age=${maxAge}` : 'no-store',
      'x-content-type-options': 'nosniff',
    },
  });
}

// ---------- what we leave out ----------
// Checked November 2026 against Disney Tourist Blog's refurbishment calendar and Pirates & Princesses' closures list.
// Party-only entries need a separate ticket, so they're not part of a normal day.
const PARTY = /very merry christmas party|not-so-scary halloween party|jollywood nights|after hours|early morning magic|extended evening/i;
// Closed for good (or replaced). Names are compared loosely: case, punctuation and quotes ignored.
const GONE = ['Splash Mountain', 'DINOSAUR', 'TriceraTop Spin', 'Primeval Whirl', 'Fossil Fun Games', 'The Boneyard', 'Liberty Square Riverboat',
  'Tom Sawyer Island', "Rock 'n' Roller Coaster Starring Aerosmith", 'Muppet*Vision 3D', 'MuppetVision 3D', "It's Tough to be a Bug!",
  'Voyage of the Little Mermaid', 'Let the Magic Begin'];
const GONE_LANDS = ['dinoland usa'];                        // Animal Kingdom's DinoLand U.S.A. closed 2 Feb 2026
// Long refurbishments: hidden until the reopening date, then they come back by themselves.
const REFURB = { "tianas bayou adventure": '2026-12-18', 'walt disneys carousel of progress': '2027-06-01', 'carousel of progress': '2027-06-01',
  'petes silly sideshow': '2027-06-01' };
// Seasonal makeovers listed alongside the original: show whichever one is running.
const PAIRS = [['jungle cruise', 'jingle cruise']];
const STALE_DAYS = 14;                                     // an entry the source hasn't updated for a fortnight isn't really there
const norm = s => String(s || '').toLowerCase().replace(/[’'`"“”*]/g, '').replace(/[^a-z0-9]+/g, ' ').trim();
const GONE_N = new Set(GONE.map(norm));

export function keep(name, land, ride, now, all) {
  const n = norm(name);
  if (PARTY.test(name)) return 'party';
  if (GONE_N.has(n) || GONE_LANDS.includes(norm(land))) return 'gone';
  for (const k in REFURB) if (n.includes(k) && now < Date.parse(REFURB[k])) return 'refurb';
  for (const [a, b] of PAIRS) {
    const other = n === a ? b : n === b ? a : null;
    if (other && !ride.open && all.some(r => norm(r.name) === other && r.open)) return 'seasonal';
  }
  if (ride.updated && now - Date.parse(ride.updated) > STALE_DAYS * 864e5) return 'stale';
  return null;
}

export function tidy(id, raw) {
  const byName = new Map();
  const add = (name, list) => {
    const rides = (list || []).map(r => ({ name: r.name, open: !!r.is_open, wait: Number(r.wait_time) || 0, updated: r.last_updated || null }));
    if (!rides.length) return;
    if (!byName.has(name)) byName.set(name, []);
    byName.get(name).push(...rides);
  };
  for (const land of raw.lands || []) add(land.name || 'Other', land.rides);
  add('Other', raw.rides);
  const now = Date.now(), everything = [...byName.values()].flat(), hidden = { party: 0, gone: 0, refurb: 0, seasonal: 0, stale: 0 };
  const lands = [...byName].map(([name, rides]) => ({ name, rides: rides.filter(r => { const why = keep(r.name, name, r, now, everything); if (why) hidden[why]++; return !why; }) }))
    .filter(l => l.rides.length);
  return { hidden, park: PARKS[id], parkId: Number(id), source: 'Queue-Times.com', sourceUrl: 'https://queue-times.com/', fetched: new Date().toISOString(), lands };
}

async function waits(id, ctx) {
  const cache = caches.default;
  const key = new Request(`https://callery.co.uk/api/waits/${id}`);
  const hit = await cache.match(key);
  if (hit && Date.now() - Number(hit.headers.get('x-fetched-at') || 0) < TTL * 1000) return hit;
  const up = await fetch(`https://queue-times.com/parks/${id}/queue_times.json`, {
    headers: { 'user-agent': 'callery.co.uk wait times page', accept: 'application/json' },
    cf: { cacheTtl: TTL, cacheEverything: true },
  });
  if (!up.ok) return json({ error: 'The wait times source is not responding right now.' }, 502);
  const res = json(tidy(id, await up.json()));
  res.headers.set('x-fetched-at', String(Date.now()));
  ctx.waitUntil(cache.put(key, res.clone()));
  return res;
}

// ---- Signed-in pages (Cloudflare Access) ----
// /travel-guides/disney/*, /api/waits/* and /api/checklist sit behind Cloudflare Access (one-time code by email).
// Access adds a signed token to every request; we check it here so the checklist knows whose ticks to load and save.
const ACCESS_TEAM = 'https://cold-snowflake-d804.cloudflareaccess.com';
const ACCESS_AUD = '76e02c10f55dff8b8102af18e0a130ead64f4371e6a1df59410303e49d23969b';
let certs = null, certsAt = 0;
const b64u = s => Uint8Array.from(atob(s.replace(/-/g, '+').replace(/_/g, '/') + '==='.slice((s.length + 3) % 4)), c => c.charCodeAt(0));
async function who(request) {
  const tok = request.headers.get('cf-access-jwt-assertion');
  if (!tok) return null;
  const [h, p, s] = tok.split('.');
  if (!s) return null;
  const head = JSON.parse(new TextDecoder().decode(b64u(h))), body = JSON.parse(new TextDecoder().decode(b64u(p)));
  if (!certs || Date.now() - certsAt > 3600e3) { certs = (await (await fetch(ACCESS_TEAM + '/cdn-cgi/access/certs')).json()).keys; certsAt = Date.now(); }
  const jwk = certs.find(k => k.kid === head.kid);
  if (!jwk || head.alg !== 'RS256') return null;
  const key = await crypto.subtle.importKey('jwk', jwk, { name: 'RSASSA-PKCS1-v1_5', hash: 'SHA-256' }, false, ['verify']);
  const ok = await crypto.subtle.verify('RSASSA-PKCS1-v1_5', key, b64u(s), new TextEncoder().encode(h + '.' + p));
  const aud = [].concat(body.aud || []);
  if (!ok || !aud.includes(ACCESS_AUD) || body.exp * 1000 < Date.now() || body.iss !== ACCESS_TEAM || !body.email) return null;
  return String(body.email).toLowerCase();
}
// GET /api/checklist -> {email, done:{"<park id>|<ride>": ms}}   PUT the same shape to save (whole list, last write wins)
async function checklist(request, env) {
  const email = await who(request);
  if (!email) return json({ error: 'Please sign in' }, 401);
  const k = 'u:' + email, noStore = r => { r.headers.set('cache-control', 'no-store, private'); return r; };
  if (request.method === 'GET') {
    const v = await env.CHECKS.get(k, 'json');
    return noStore(json({ email, done: (v && v.done) || {}, updated: (v && v.updated) || 0 }));
  }
  if (request.method === 'PUT') {
    const text = await request.text();
    if (text.length > 100000) return json({ error: 'Too big' }, 413);
    const b = JSON.parse(text), done = {};
    for (const [key, ms] of Object.entries(b.done || {})) if (/^\d+\|.{1,120}$/.test(key) && Number.isFinite(ms)) done[key] = ms;
    const updated = Date.now();
    await env.CHECKS.put(k, JSON.stringify({ done, updated }));
    return noStore(json({ ok: true, updated }));
  }
  return json({ error: 'Method not allowed' }, 405);
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    try {
      const m = url.pathname.match(/^\/api\/waits\/(\d+)\/?$/);
      if (m) {
        if (request.method !== 'GET' && request.method !== 'HEAD') return json({ error: 'Method not allowed' }, 405);
        if (!PARKS[m[1]]) return json({ error: 'Unknown park' }, 404);
        return await waits(m[1], ctx);
      }
      if (url.pathname === '/api/checklist') return await checklist(request, env);
      if (url.pathname.startsWith('/api/')) return json({ error: 'Not found' }, 404);
    } catch (e) {
      return json({ error: 'Something went wrong.' }, 500);
    }
    return env.ASSETS.fetch(request);
  },
};
