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
      'cache-control': status === 200 ? `public, max-age=${maxAge}` : 'no-store',
      'x-content-type-options': 'nosniff',
    },
  });
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
  const lands = [...byName].map(([name, rides]) => ({ name, rides }));
  return { park: PARKS[id], parkId: Number(id), source: 'Queue-Times.com', sourceUrl: 'https://queue-times.com/', fetched: new Date().toISOString(), lands };
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
      if (url.pathname.startsWith('/api/')) return json({ error: 'Not found' }, 404);
    } catch (e) {
      return json({ error: 'Something went wrong fetching wait times.' }, 500);
    }
    return env.ASSETS.fetch(request);
  },
};
