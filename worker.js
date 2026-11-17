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

// Rides the source files under the wrong land: [ride name pattern, the land it really belongs in]
const MOVE = [[/^toy story mania/i, 'Toy Story Land']];
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
  for (const [re, to] of MOVE) {
    const dest = [...byName.keys()].find(k => k.toLowerCase() === to.toLowerCase()) || to;
    for (const [land, rides] of byName) {
      if (land === dest) continue;
      const out = rides.filter(r => re.test(r.name));
      if (!out.length) continue;
      byName.set(land, rides.filter(r => !re.test(r.name)));
      if (!byName.has(dest)) byName.set(dest, []);
      byName.get(dest).push(...out);
    }
  }
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
// Team domains whose sign-ins we accept. The team was renamed from cold-snowflake-d804 to callery-login on 8 Nov 2026,
// and devices that signed in before the rename keep a pass from the old name until it runs out, so both are trusted.
const ACCESS_TEAMS = ['https://callery-login.cloudflareaccess.com', 'https://cold-snowflake-d804.cloudflareaccess.com'];
const ACCESS_TEAM = ACCESS_TEAMS[0];
const ACCESS_AUD = '76e02c10f55dff8b8102af18e0a130ead64f4371e6a1df59410303e49d23969b';
const certs = {};   // team domain -> {keys, at}
const b64u = s => Uint8Array.from(atob(s.replace(/-/g, '+').replace(/_/g, '/') + '==='.slice((s.length + 3) % 4)), c => c.charCodeAt(0));
async function keysFor(team, fresh) {
  const c = certs[team];
  if (!fresh && c && Date.now() - c.at < 3600e3) return c.keys;
  const r = await fetch(team + '/cdn-cgi/access/certs');
  const keys = r.ok ? ((await r.json()).keys || []) : [];
  certs[team] = { keys, at: Date.now() };
  return keys;
}
// Returns {email} or {why}: none | bad | iss | kid | sig | aud | exp | email
async function check(request) {
  const tok = request.headers.get('cf-access-jwt-assertion');
  if (!tok) return { why: 'none' };
  const [h, p, s] = tok.split('.');
  if (!s) return { why: 'bad' };
  let head, body;
  try { head = JSON.parse(new TextDecoder().decode(b64u(h))); body = JSON.parse(new TextDecoder().decode(b64u(p))); } catch (e) { return { why: 'bad' }; }
  const team = String(body.iss || '').replace(/\/$/, '');
  check.last = { iss: body.iss, kid: head.kid, alg: head.alg, aud: [].concat(body.aud || []).map(a => a.slice(0, 8)), exp: body.exp, type: body.type, hasEmail: !!body.email };
  if (!ACCESS_TEAMS.includes(team)) return { why: 'iss' };
  if (head.alg !== 'RS256') return { why: 'bad' };
  // The key can be listed by either team name after the rename, and keys rotate, so look everywhere (fresh) before giving up
  const find = async fresh => { for (const tm of [team, ...ACCESS_TEAMS.filter(x => x !== team)]) { const k = (await keysFor(tm, fresh)).find(k => k.kid === head.kid); if (k) return k; } return null; };
  const jwk = (await find(false)) || (await find(true));
  if (!jwk) {
    // Last resort for a pass from our own team whose key is no longer published: Cloudflare Access has already checked this
    // request at the edge (these paths are behind it), and it tells us who it let in. Accept only if that matches the pass.
    const edge = (request.headers.get('cf-access-authenticated-user-email') || '').toLowerCase();
    if (edge && body.email && edge === String(body.email).toLowerCase() && [].concat(body.aud || []).includes(ACCESS_AUD) && body.exp * 1000 > Date.now()) return { email: edge, via: 'edge' };
    return { why: 'kid' };
  }
  const key = await crypto.subtle.importKey('jwk', jwk, { name: 'RSASSA-PKCS1-v1_5', hash: 'SHA-256' }, false, ['verify']);
  if (!(await crypto.subtle.verify('RSASSA-PKCS1-v1_5', key, b64u(s), new TextEncoder().encode(h + '.' + p)))) return { why: 'sig' };
  if (![].concat(body.aud || []).includes(ACCESS_AUD)) return { why: 'aud' };
  if (body.exp * 1000 < Date.now()) return { why: 'exp' };
  if (!body.email) return { why: 'email' };
  return { email: String(body.email).toLowerCase() };
}
async function who(request) { return (await check(request)).email || null; }
// Temporary: remember the last refused sign-in (reason and token shape only, no email) so it can be checked in the dashboard
async function noteRefusal(request, env) {
  check.last = null; const c = await check(request);
  const hdrs = ['cf-access-jwt-assertion', 'cookie'].map(h => h + ':' + (request.headers.get(h) ? (h === 'cookie' ? request.headers.get(h).split(';').map(x => x.trim().split('=')[0]).join(',') : 'yes') : 'no'));
  try { await env.CHECKS.put('dbg:refused', JSON.stringify({ at: new Date().toISOString(), path: new URL(request.url).pathname, host: new URL(request.url).host, why: c.why, token: check.last, hdrs, ua: (request.headers.get('user-agent') || '').slice(0, 90) }), { expirationTtl: 7 * 86400 }); } catch (e) {}
}
const denied = async request => { const r = json({ error: 'Please sign in', why: (await check(request)).why }, 401); r.headers.set('cache-control', 'no-store'); return r; };
// GET /api/checklist -> {email, done:{"<park id>|<ride>": ms}}   PUT the same shape to save (whole list, last write wins)
async function checklist(request, env) {
  const email = await who(request);
  if (!email) { await noteRefusal(request, env); return denied(request); }
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

// ---- "What we did today": a shared diary for everyone signed in to the Disney pages ----
// KV keys: d:<YYYY-MM-DD> (Florida date) -> [{id, at, who, name, park, text}]   n:<email> -> display name
// GET /api/diary?day=YYYY-MM-DD -> {day, today, me:{name}, entries}   POST {text, park, time?, day?} adds one
// DELETE /api/diary?day=..&id=.. removes your own entry   PUT /api/diary/name {name} sets what we call you
const floridaDay = ms => new Date(ms).toLocaleDateString('en-CA', { timeZone: 'America/New_York' });
const clean = (s, n) => String(s || '').replace(/[\u0000-\u001f]/g, ' ').trim().slice(0, n);
async function diary(request, env, url) {
  const email = await who(request);
  if (!email) { await noteRefusal(request, env); return denied(request); }
  const noStore = r => { r.headers.set('cache-control', 'no-store, private'); return r; };
  const name = await env.CHECKS.get('n:' + email);
  if (url.pathname === '/api/diary/name' && request.method === 'PUT') {
    const n = clean((await request.json()).name, 30);
    if (!n) return json({ error: 'Name needed' }, 400);
    await env.CHECKS.put('n:' + email, n);
    return noStore(json({ ok: true, name: n }));
  }
  const today = floridaDay(Date.now());
  const day = /^\d{4}-\d\d-\d\d$/.test(url.searchParams.get('day') || '') ? url.searchParams.get('day') : today;
  const key = 'd:' + day, list = (await env.CHECKS.get(key, 'json')) || [];
  const out = l => l.slice().sort((a, b) => a.at - b.at).map(e => ({ id: e.id, at: e.at, name: e.name, park: e.park, text: e.text, mine: e.who === email }));
  if (request.method === 'GET') return noStore(json({ day, today, me: { name: name || '' }, entries: out(list) }));
  if (request.method === 'POST') {
    const b = await request.json(), text = clean(b.text, 500);
    if (!text) return json({ error: 'Write something first' }, 400);
    if (!name) return json({ error: 'Tell us your name first' }, 400);
    const d = /^\d{4}-\d\d-\d\d$/.test(b.day || '') ? b.day : today, k = 'd:' + d;
    const l = d === day ? list : ((await env.CHECKS.get(k, 'json')) || []);
    if (l.length >= 300) return json({ error: 'That day is full' }, 400);
    const at = Number.isFinite(b.at) ? b.at : Date.now();
    l.push({ id: crypto.randomUUID().slice(0, 8), at, who: email, name, park: clean(b.park, 40), text });
    await env.CHECKS.put(k, JSON.stringify(l));
    return noStore(json({ day: d, today, me: { name }, entries: out(l) }));
  }
  if (request.method === 'DELETE') {
    const id = url.searchParams.get('id'), l = list.filter(e => !(e.id === id && e.who === email));
    await env.CHECKS.put(key, JSON.stringify(l));
    return noStore(json({ day, today, me: { name: name || '' }, entries: out(l) }));
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
      if (url.pathname === '/api/diary' || url.pathname === '/api/diary/name') return await diary(request, env, url);
      if (url.pathname.startsWith('/api/')) return json({ error: 'Not found' }, 404);
    } catch (e) {
      return json({ error: 'Something went wrong.' }, 500);
    }
    return env.ASSETS.fetch(request);
  },
};
