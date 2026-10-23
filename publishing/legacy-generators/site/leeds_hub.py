# Leeds United Match Centre - Rob's broadcast-style layout over the Elland Road scene
import sys, re, os
D = '/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/'
sys.path.insert(0, D)
from leeds_scene import scene
svg, _ = scene(screen=False)
STYLE = open(D + 'mc/style.css').read()
BODY = open(D + 'mc/body.html').read()
LOGO = open(D + 'mc/logo.html').read()
SCRIPT = open(D + 'mc/markers.js').read() + '\n' + open(D + 'mc/script.js').read()

# swap Rob's pitch theme for a stadium theme (keeps his layout and type)
THEME = r'''
  /* ===== Elland Road theme (replaces the pitch theme) ===== */
  :root { --panel: rgba(6, 14, 34, .80); --row: rgba(0,0,0,.28); --row-alt: rgba(255,255,255,.04); --muted: #b8c3dc; --accent: #ffcd00; --accent-fg: #0a1838; }
  html, body { width: 100%; height: 100%; background: #0b0f1a; }
  .scene { position: fixed; inset: 0; z-index: 0; }
  .scene svg { width: 100%; height: 100%; display: block; }
  .scene::after { content: ""; position: absolute; inset: 0;
    background: radial-gradient(ellipse at 40% 45%, rgba(5,10,24,.35), rgba(5,10,24,.72) 75%), linear-gradient(rgba(5,10,24,.25), rgba(5,10,24,.55)); }
  .fit { position: fixed; inset: 0; z-index: 1; overflow: hidden; }
  .stage { background: none !important; position: absolute; left: 50%; top: 50%; transform-origin: center center; transform: translate(-50%, -50%); }
  .card-head, .lp-head { background: #fff !important; color: #0a1838 !important; }
  .brand .tag { background: var(--accent); color: var(--accent-fg); }
  .top { border-bottom: 3px solid rgba(255,255,255,.85) !important; }
  .top .right-bits { display: flex; align-items: center; gap: 22px; }
  .top a.back { font-size: 22px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #fff; text-decoration: none;
    border: 2px solid rgba(255,255,255,.7); border-radius: 30px; padding: 4px 18px; background: rgba(6,14,34,.6); }
  .top a.back:hover, .top a.back:focus-visible { border-color: var(--accent); color: var(--accent); }
  .card-box { border: 2px solid rgba(255,255,255,.85); backdrop-filter: blur(3px); }
  .tr.hd { background: rgba(0,0,0,.45) !important; }
  /* the right column always fills the space between the top bar and the ticker; the table shares what's left across its rows */
  .right { display: flex; flex-direction: column; min-height: 0; overflow: hidden; }
  .right .card-box:first-child { flex: none; }
  .right .card-box:last-child { flex: 1 1 auto; min-height: 0; display: flex; flex-direction: column; }
  .card-head { flex: none; }
  .swap { flex: 1 1 auto; height: auto !important; min-height: 0; }
  #table { display: grid; grid-template-rows: 26px; grid-auto-rows: minmax(0, 1fr); height: 100%; }
  .tr { height: auto !important; min-height: 0; padding-top: 0; padding-bottom: 0; line-height: 1; overflow: hidden; } .g { padding-top: 6px; padding-bottom: 6px; }
  .g .s.pre { white-space: nowrap; }
  .card-head { white-space: nowrap; gap: 14px; } .card-head > span { flex: none; } .card-head small { overflow: hidden; text-overflow: ellipsis; min-width: 0; }
  #scores { overflow: hidden; }
  .right { padding: 16px 0 14px; gap: 14px; }
  .side .tname { font-size: 54px; text-shadow: 0 4px 14px rgba(0,0,0,.8); }
  .venue, .top .meta { text-shadow: 0 2px 8px rgba(0,0,0,.8); }
  .ticker { background: rgba(6,14,34,.92) !important; border-top: 3px solid #fff !important; }
  .tk-label, .tk-label::after { background: var(--accent) !important; color: var(--accent-fg) !important; }
  .tk-team { background: rgba(255,255,255,.08) !important; }
  .status-pill { display: block !important; padding: 0 !important; border-radius: 8px !important; min-width: 480px; text-align: center; overflow: hidden;
    background: var(--panel) !important; border: 2px solid rgba(255,255,255,.85) !important; box-shadow: 0 8px 24px rgba(0,0,0,.4); }
  .status-pill .card-head { justify-content: center; }
  .status-pill .pill-body { display: flex; align-items: center; justify-content: center; gap: 14px; padding: 10px 30px 8px; font-size: 46px; font-weight: 800; letter-spacing: 3px; }
  .status-pill.live .card-head { background: var(--live) !important; color: #fff !important; }
  .tr.focus, .tr.playing { background: rgba(255,205,0,.16) !important; }
  .tr.focus .nm span { color: var(--accent); }
  .crest { background: radial-gradient(circle, rgba(255,255,255,.14), rgba(255,255,255,0) 70%); }
  .msg { position: fixed; z-index: 2; inset: auto 0 40% 0; text-align: center; font-size: 28px; font-weight: 700; letter-spacing: 2px; color: #fff; text-shadow: 0 2px 8px #000; display: none; }
  .sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

  /* ===== phones and tall screens: reflow instead of shrinking the TV layout ===== */
  @media (max-width: 1000px), (max-aspect-ratio: 1/1) {
    html, body { overflow: auto; height: auto; }
    .scene { position: fixed; }
    .fit { position: relative; display: block; overflow: visible; }
    .stage { position: relative; left: auto; top: auto; width: 100% !important; height: auto !important; transform: none !important; display: flex; flex-direction: column; gap: 14px; padding: 0 14px 0; }
    .top { flex-wrap: wrap; gap: 8px; padding: 12px 0; }
    .brand .tag { font-size: 18px; } .brand .comp { font-size: 20px; }
    .top .meta { font-size: 15px; width: 100%; order: 3; }
    .top a.back { font-size: 15px; padding: 3px 12px; }
    .main { gap: 18px; padding: 6px 0 0; }
    .status-pill { min-width: 0; width: min(100%, 340px); align-self: center; } .status-pill .pill-body { font-size: 26px; padding: 6px 14px; }
    .fixture { gap: 8px; grid-template-columns: minmax(0,1fr) auto minmax(0,1fr); }
    .crest { width: 96px; height: 96px; } .crest img { width: 80px; height: 80px; }
    .side .tname { font-size: clamp(13px, 3.9vw, 26px) !important; letter-spacing: 0; white-space: nowrap; max-width: 100%; overflow: hidden; text-overflow: ellipsis; }
    .side { min-width: 0; width: 100%; }
    .tbar { width: 60px; height: 4px; }
    .score { font-size: 58px; gap: 6px; } .score .box { min-width: 50px; padding: 2px 10px 0; border-radius: 8px; }
    .score .dash, .score.pre .dash { font-size: 44px; }
    .events { gap: 16px; min-height: 0; } .ev-col { font-size: 17px; } .ev .note { font-size: 14px; }
    .venue { font-size: 16px; }
    .right { padding: 0; gap: 14px; }
    .g { font-size: 17px; padding: 6px 8px; grid-template-columns: 1fr auto 1fr 34px; } .g .st { font-size: 13px; } .g .s.pre { font-size: 15px; }
    .card-head { font-size: 18px; }
    .swap { height: auto !important; } .view { position: static; display: none; opacity: 1; } .view.on { display: block; }
    #table { display: block; height: auto; } .right .card-box:last-child { display: block; } .right { overflow: visible; }
    .tr { height: 28px !important; }
    .tr { font-size: 16px; height: 28px; grid-template-columns: 24px 22px 1fr 26px 36px 36px; }
    .fx-row { grid-template-columns: 80px 1fr 80px; font-size: 17px; height: 44px; padding: 0 10px; }
    .fx-teams { font-size: 17px; }
    .ticker { margin: 0 -14px; position: sticky; bottom: 0; }
    .tk-label { font-size: 16px; padding: 0 12px; } .tk-team, .tk-p { font-size: 17px; } .tk-team { height: 44px; } .tk-team img { width: 26px; height: 26px; }
    .logo-wrap { position: static; width: 110px; margin: 4px auto 10px; order: 20; }
    .ticker { order: 30; }
  }
'''

PAGE = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Leeds United Match Centre - Rob Callery</title>
<meta name="description" content="Rob Callery's Leeds United match centre: live score, goals and cards, line-ups, today's scores, the live table and match facts, from a seat at Elland Road.">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700;800&family=Bebas+Neue&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>__STYLE__
__THEME__
</style>
</head>
<body>
<div class="scene" aria-hidden="true"><svg viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice">__SVG__</svg></div>
<div class="fit">
<div class="stage" id="stage">
  <h1 class="sr">Leeds United Match Centre</h1>
  __LOGO__
  __BODY__
</div>
</div>
<div class="msg" id="msg">Finding the next Leeds game…</div>
<script>
__SCRIPT__
</script>
<script>
/* ---------- fit the 1920x1080 broadcast layout to any screen ---------- */
(function () {
  var st = document.getElementById('stage'), mq = matchMedia('(max-width: 1000px), (max-aspect-ratio: 1/1)');
  function fit() { if (mq.matches) { st.style.transform = ''; return; }
    var s = Math.min(innerWidth / 1920, innerHeight / 1080); st.style.transform = 'translate(-50%, -50%) scale(' + s + ')'; }
  addEventListener('resize', fit); fit();
})();
/* ---------- the back link lives in the top bar ---------- */
(function () {
  var meta = document.getElementById('meta'), wrap = document.createElement('div'); wrap.className = 'right-bits';
  meta.parentNode.insertBefore(wrap, meta); wrap.appendChild(meta);
  var a = document.createElement('a'); a.className = 'back'; a.href = '/match-hub/'; a.textContent = '\\u2190 Back to the pub'; wrap.appendChild(a);
})();
/* ---------- pick Leeds' live, latest or next game automatically ---------- */
(function () {
  var TEAM = '357', LEEDS = { name: 'Leeds', color: '#FFFFFF' };
  var LEAGUES = [['eng.1', 'Premier League'], ['eng.2', 'Championship'], ['eng.fa', 'FA Cup'], ['eng.league_cup', 'Carabao Cup']];
  var API = 'https://site.api.espn.com/apis/site/v2/sports/soccer/';
  function get(u) { return fetch(u, { cache: 'no-store' }).then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; }); }
  var SHORT = { 'Manchester United': 'Man Utd', 'Manchester City': 'Man City', 'Tottenham Hotspur': 'Spurs', 'Wolverhampton Wanderers': 'Wolves',
    'Brighton & Hove Albion': 'Brighton', 'Nottingham Forest': "Nott'm Forest", 'Newcastle United': 'Newcastle', 'West Ham United': 'West Ham', 'Leeds United': 'Leeds' };
  function teamOf(c) { var t = c.team || {}; var col = (t.color && !/^(000000|ffffff)$/i.test(t.color)) ? '#' + t.color : (t.alternateColor ? '#' + t.alternateColor : '#c9d2e6');
    return { id: String(t.id || c.id), name: SHORT[t.displayName] || t.shortDisplayName || t.displayName || t.name || '', color: col, logo: t.logo || ((t.logos || [])[0] || {}).href || (t.id ? 'https://a.espncdn.com/i/teamlogos/soccer/500/' + t.id + '.png' : window.teamMarker(t)) }; }
  var found = [];
  function scan(d, lg, label) {
    ((d && d.events) || []).forEach(function (e) {
      var c = (e.competitions || [])[0] || {}, cs = c.competitors || [];
      if (!cs.some(function (x) { return String((x.team || {}).id || x.id) === TEAM; })) return;
      var st = (c.status || e.status || {}).type || {};
      found.push({ e: e, c: c, lg: lg, label: ((d.leagues || [])[0] || {}).name || label, state: st.state || 'pre', date: new Date(e.date) });
    });
  }
  var jobs = [];
  LEAGUES.forEach(function (L) {
    jobs.push(get(API + L[0] + '/scoreboard').then(function (d) { scan(d, L[0], L[1]); }));
    jobs.push(get(API + L[0] + '/teams/' + TEAM + '/schedule?fixture=true').then(function (d) { scan(d, L[0], L[1]); }));
    jobs.push(get(API + L[0] + '/teams/' + TEAM + '/schedule').then(function (d) { scan(d, L[0], L[1]); }));
  });
  Promise.all(jobs).then(function () {
    var now = Date.now();
    var live = found.filter(function (f) { return f.state === 'in'; })[0];
    var recent = found.filter(function (f) { return f.state === 'post' && now - f.date < 4 * 36e5; }).sort(function (a, b) { return b.date - a.date; })[0];
    var next = found.filter(function (f) { return f.state === 'pre' && f.date > now - 3 * 36e5; }).sort(function (a, b) { return a.date - b.date; })[0];
    var pick = live || recent || next || found.filter(function (f) { return f.state === 'post'; }).sort(function (a, b) { return b.date - a.date; })[0];
    if (!pick) { var m = document.getElementById('msg'); m.textContent = "The fixture feed is down - try again later."; m.style.display = 'block'; return; }
    var cs = pick.c.competitors, h = cs.filter(function (x) { return x.homeAway === 'home'; })[0] || cs[0], a = cs.filter(function (x) { return x.homeAway === 'away'; })[0] || cs[1];
    var home = teamOf(h), away = teamOf(a);
    [home, away].forEach(function (t) { if (t.id === TEAM) { t.name = LEEDS.name; t.color = LEEDS.color; } });
    var v = pick.c.venue || {};
    var cfg = { competition: pick.label, league: pick.lg, eventId: String(pick.e.id), kickoff: pick.e.date, venue: v.fullName || '', transparentBackground: false,
      home: Object.assign(home, { xi: [], subs: [] }), away: Object.assign(away, { xi: [], subs: [] }),
      tickerSpeed: 90, tableSecs: 20, factsSecs: 20,
      manualStats: { xg: ['', ''], touchesOppBox: ['', ''], bigChances: ['', ''], bigChancesMissed: ['', ''] },
      maxScoresShown: 4, zones: { ucl: [1, 4], uel: [5, 5], rel: [18, 20] }, pollSeconds: 20 };
    if (pick.lg !== 'eng.1') cfg.zones = { ucl: [1, 2], uel: [3, 6], rel: [22, 24] };
    // the big screen in the stadium follows the game
    var bh = document.getElementById('bsHead'), bm = document.getElementById('bsMain'), bs = document.getElementById('bsSub');
    window.onCentre = function (s) {
      if (!bh) return;
      bh.textContent = s.isLive ? 'LIVE' : s.showScore ? 'FULL TIME' : 'NEXT UP';
      bm.textContent = (home.name + (s.showScore ? ' ' + s.hs + '-' + s.as + ' ' : ' V ') + away.name).toUpperCase();
      bs.textContent = s.text.replace('KICK-OFF IN ', 'KO IN ');
    };
    startCentre(cfg);
  });
  // pitch-side LED board
  var led = document.getElementById('ledText'), msgs = ['MARCHING ON TOGETHER', "ALL LEEDS AREN'T WE", 'SIDE BEFORE SELF EVERY TIME', 'FOLLOW @CALZ88', 'ONE BEER AT A TIME'], i = 0;
  if (led) { led.style.transition = 'opacity .35s'; setInterval(function () { i = (i + 1) % msgs.length; led.style.opacity = 0; setTimeout(function () { led.textContent = msgs[i]; led.style.opacity = 1; }, 350); }, 4500); }
})();
</script>
</body>
</html>
'''
out = (PAGE.replace('__STYLE__', STYLE).replace('__THEME__', THEME).replace('__SVG__', svg).replace('__LOGO__', LOGO)
       .replace('__BODY__', BODY).replace('__SCRIPT__', SCRIPT))
os.makedirs('/home/claude/site/match-hub/leeds', exist_ok=True)
open('/home/claude/site/match-hub/leeds/index.html', 'w').write(out)
print('match centre', len(out) // 1024, 'KB')
