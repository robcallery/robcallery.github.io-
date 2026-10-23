# F1 Pit Wall: /var-and-grill/f1/
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f1_scene import scene

OUT = '/home/claude/site/var-and-grill/f1/index.html'

CSS = r'''
  :root { --bg:#070b16; --panel:rgba(10,14,26,.86); --panel2:rgba(255,255,255,.04); --line:rgba(255,255,255,.85); --text:#fff; --muted:#a3acbf; --red:#e10600; --live:#ff2a2a; --ok:#27f4d2; }
  * { box-sizing:border-box; margin:0; padding:0; }
  html, body { height:100%; background:var(--bg); color:var(--text); font-family:'Titillium Web','Arial Narrow',Arial,sans-serif; overflow:hidden; }
  .sr { position:absolute; width:1px; height:1px; overflow:hidden; clip:rect(0 0 0 0); white-space:nowrap; }
  .scene { position:fixed; inset:0; z-index:0; }
  .scene svg { width:100%; height:100%; display:block; }
  .scene::after { content:""; position:absolute; inset:0; background:radial-gradient(ellipse at 50% 45%, rgba(5,8,18,.25), rgba(5,8,18,.7) 78%); }
  #car { animation: zoom 9s linear infinite; }
  @keyframes zoom { 0% { transform: translate(-260px, 640px) } 18% { transform: translate(1700px, 595px) } 100% { transform: translate(1700px, 595px) } }
  .fit { position:fixed; inset:0; z-index:1; overflow:hidden; }
  .stage { position:absolute; left:50%; top:50%; width:1920px; height:1080px; transform-origin:center; transform:translate(-50%,-50%);
           display:grid; grid-template-rows:96px minmax(0,1fr) 62px; padding:0 40px; }
  /* top bar */
  .top { display:flex; align-items:center; justify-content:space-between; border-bottom:3px solid var(--line); }
  .brand { display:flex; align-items:center; gap:18px; }
  .brand .tag { background:var(--red); color:#fff; font-weight:700; font-size:28px; letter-spacing:3px; padding:2px 18px; text-transform:uppercase; transform:skewX(-12deg); }
  .brand .tag span { display:inline-block; transform:skewX(12deg); }
  .brand .comp { font-size:34px; font-weight:700; letter-spacing:2px; text-transform:uppercase; }
  .right-bits { display:flex; align-items:center; gap:22px; }
  .meta { font-size:24px; font-weight:600; color:var(--muted); letter-spacing:2px; text-transform:uppercase; }
  a.back { font-size:22px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; color:#fff; text-decoration:none; border:2px solid rgba(255,255,255,.7); border-radius:30px; padding:2px 18px; background:rgba(6,10,22,.6); white-space:nowrap; }
  a.back:hover, a.back:focus-visible { border-color:var(--red); color:#ff6b63; }
  /* columns */
  .cols { display:grid; grid-template-columns:450px minmax(0,1fr) 450px; gap:34px; padding:26px 0 22px; min-height:0; }
  .card { background:var(--panel); border:2px solid var(--line); backdrop-filter:blur(3px); display:flex; flex-direction:column; min-height:0; }
  .head { background:#fff; color:#0b1020; display:flex; justify-content:space-between; align-items:center; gap:10px; padding:6px 16px; font-weight:700; font-size:22px; letter-spacing:2px; text-transform:uppercase; white-space:nowrap; }
  .head small { font-size:16px; letter-spacing:1px; color:#4a5168; overflow:hidden; text-overflow:ellipsis; }
  .head.live { background:var(--live); color:#fff; } .head.live small { color:#ffe1e1; }
  /* timing tower */
  .tower { flex:1; }
  #tower { flex:1; display:grid; grid-auto-rows:minmax(0,1fr); min-height:0; }
  .tr { display:grid; grid-template-columns:44px 7px 74px minmax(0,1fr) 118px; align-items:center; gap:10px; padding:0 14px 0 6px; font-size:22px; font-weight:600; border-bottom:1px solid rgba(255,255,255,.06); min-height:0; overflow:hidden; }
  .tr:nth-child(odd) { background:var(--panel2); }
  .tr .p { text-align:center; font-weight:700; }
  .tr .bar { height:70%; border-radius:2px; }
  .tr .code { font-weight:700; letter-spacing:1px; }
  .tr .team { color:var(--muted); font-size:17px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
  .tr .v { text-align:right; font-variant-numeric:tabular-nums; white-space:nowrap; }
  .tr .v.dnf { color:#ff8f8a; }
  .tr.lead .p { color:#ffd23f; }
  .tr .chg { font-size:13px; margin-left:4px; } .tr .up { color:#2bd46b; } .tr .down { color:#ff5a52; }
  .empty { padding:22px; color:var(--muted); font-size:22px; text-align:center; }
  /* centre */
  .mid { display:flex; flex-direction:column; gap:22px; min-height:0; }
  .race { padding:0 0 18px; }
  .race .body { padding:16px 26px 0; }
  .round { font-size:22px; letter-spacing:3px; color:var(--muted); text-transform:uppercase; font-weight:600; }
  .gp { font-size:64px; line-height:1.02; font-weight:700; text-transform:uppercase; letter-spacing:1px; margin:4px 0 4px; }
  .circuit { font-size:24px; color:#dfe4ee; }
  .cd { margin:18px 26px 0; border:2px solid var(--line); display:flex; flex-direction:column; }
  .cd .head { justify-content:center; }
  .cd .num { font-size:66px; font-weight:700; text-align:center; letter-spacing:3px; font-variant-numeric:tabular-nums; padding:4px 10px 6px; }
  .cd.live .head { background:var(--live); color:#fff; }
  .cd.live .num { color:#fff; }
  .dot { display:inline-block; width:16px; height:16px; border-radius:50%; background:var(--live); margin-right:14px; vertical-align:middle; animation:pulse 1.2s infinite; }
  @keyframes pulse { 50% { opacity:.25 } }
  .sched { margin:16px 26px 0; display:grid; grid-template-columns:repeat(var(--n,5), minmax(0,1fr)); gap:10px; }
  .ses { border:1px solid rgba(255,255,255,.35); padding:8px 10px; text-align:center; background:rgba(255,255,255,.03); }
  .ses b { display:block; font-size:18px; letter-spacing:1.5px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
  .ses span { display:block; font-size:18px; color:var(--muted); white-space:nowrap; }
  .ses.done { opacity:.5; } .ses.done b::after { content:" ✓"; color:var(--ok); }
  .ses.next { border-color:#fff; background:rgba(255,255,255,.12); }
  .ses.live { border-color:var(--live); background:rgba(255,42,42,.22); }
  .podium { flex:1; min-height:0; }
  .ses[data-k] { cursor:pointer; font:inherit; color:inherit; }
  .ses[data-k]:hover, .ses[data-k]:focus-visible { border-color:#fff; outline:none; background:rgba(255,255,255,.16); opacity:1; }
  .ses.on { border-color:#ffd23f !important; box-shadow:inset 0 -4px 0 #ffd23f; opacity:1; }
  .board { display:none; flex:1; min-height:0; }
  .mid.boardmode .race, .mid.boardmode .podium { display:none; }
  .mid.boardmode .board { display:flex; }
  .board .head.live { background:var(--live); color:#fff; } .board .head.live small { color:#fff; font-size:20px; }
  .bln { display:grid; grid-template-columns:56px 8px minmax(0,1.7fr) minmax(0,1fr) 130px 110px 64px; align-items:center; gap:12px; padding:0 18px 0 8px; }
  .bhd { font-size:16px; letter-spacing:2px; color:var(--muted); font-weight:700; height:34px; border-bottom:1px solid rgba(255,255,255,.2); }
  .bhd .t, .brow .t { text-align:right; font-variant-numeric:tabular-nums; }
  #boardRows { flex:1; display:grid; grid-auto-rows:minmax(0,1fr); min-height:0; }
  .brow { font-size:22px; font-weight:600; border-bottom:1px solid rgba(255,255,255,.06); min-height:0; overflow:hidden; transition:background .6s; }
  .brow:nth-child(odd) { background:var(--panel2); }
  .brow .p { text-align:center; font-weight:700; }
  .brow.lead .p { color:#ffd23f; }
  .brow .bar { height:68%; border-radius:2px; }
  .brow .dn { white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
  .brow .dn b { letter-spacing:1px; margin-right:10px; }
  .brow .dn span { color:#dfe4ee; font-weight:400; }
  .brow .tm { color:var(--muted); font-size:18px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
  .brow .mv { font-size:15px; margin-left:8px; font-weight:700; } .brow .up { color:#2bd46b; } .brow .down { color:#ff5a52; }
  .brow.moved { background:rgba(43,212,107,.18) !important; } .brow.dropped { background:rgba(255,90,82,.16) !important; }
  .brow .dnf { color:#ff8f8a; }
  .bnote { font-size:15px; color:var(--muted); padding:6px 18px; border-top:1px solid rgba(255,255,255,.12); white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
  .bfoot { display:flex; gap:10px; align-items:stretch; padding:0 18px 14px; }
  .bfoot .sched { margin:0; flex:1; }
  .bfoot #boardBack { font:inherit; font-size:17px; font-weight:700; letter-spacing:1px; text-transform:uppercase; color:#0b1020; background:#fff; border:0; padding:0 16px; cursor:pointer; white-space:nowrap; }
  .bfoot #boardBack:hover, .bfoot #boardBack:focus-visible { background:#ffd23f; }
  #podium { flex:1; display:grid; grid-template-columns:1fr 1fr 1fr; grid-template-rows:minmax(0,1fr); gap:16px; padding:14px 20px 0; align-items:stretch; min-height:0; overflow:hidden; }
  .pd { display:flex; flex-direction:column; align-items:center; justify-content:flex-end; text-align:center; gap:4px; min-width:0; min-height:0; height:100%; }
  .pd .nm { font-size:26px; font-weight:700; line-height:1.05; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:100%; }
  .pd .tm { font-size:18px; color:var(--muted); white-space:nowrap; }
  .pd .step { width:100%; display:flex; align-items:flex-start; justify-content:center; font-size:46px; font-weight:700; color:#0b1020; padding-top:4px; border-top:6px solid var(--c,#fff); background:#e9ecf3; }
  .pd .step { flex:0 1 auto; min-height:44px; } .pd.p1 .step { height:58%; } .pd.p2 .step { height:42%; } .pd.p3 .step { height:28%; }
  /* right */
  .right { display:flex; flex-direction:column; gap:22px; min-height:0; }
  .cons { flex:1; }
  #cons { flex:1; display:grid; grid-auto-rows:minmax(0,1fr); min-height:0; }
  #cons .tr { grid-template-columns:40px 7px minmax(0,1fr) 70px; }
  .beer .body { padding:14px 18px 16px; }
  .beer .bn { font-size:30px; font-weight:700; line-height:1.1; }
  .beer .bl { font-size:19px; color:#dfe4ee; margin-top:6px; line-height:1.3; }
  .beer .bg { display:inline-block; margin-top:10px; font-size:17px; font-weight:700; letter-spacing:1px; text-transform:uppercase; color:#ffd23f; text-decoration:none; border-bottom:2px solid; }
  /* ticker */
  .ticker { display:flex; align-items:center; border-top:3px solid var(--line); overflow:hidden; background:rgba(6,9,18,.75); }
  .ticker .lab { background:var(--red); color:#fff; font-weight:700; font-size:22px; letter-spacing:2px; padding:0 22px; align-self:stretch; display:flex; align-items:center; white-space:nowrap; }
  .ticker .run { flex:1; overflow:hidden; white-space:nowrap; }
  .ticker .track { display:inline-block; padding-left:100%; font-size:24px; font-weight:600; letter-spacing:1px; animation:tick var(--d,60s) linear infinite; }
  .ticker .track i { font-style:normal; color:#ffd23f; margin:0 18px; }
  @keyframes tick { to { transform:translateX(-100%) } }
  .msg { position:fixed; left:50%; top:50%; transform:translate(-50%,-50%); z-index:5; background:rgba(8,12,24,.92); border:2px solid #fff; padding:18px 26px; font-size:22px; display:none; max-width:90vw; text-align:center; }
  /* phones and tall screens: reflow */
  @media (max-width:1000px), (max-aspect-ratio:1/1) {
    html, body { overflow:auto; height:auto; }
    .fit { position:relative; overflow:visible; }
    .stage { position:relative; left:auto; top:auto; width:100%; height:auto; transform:none !important; display:flex; flex-direction:column; padding:0 14px; gap:14px; }
    .top { flex-wrap:wrap; gap:8px; padding:12px 0; }
    .brand { flex-wrap:wrap; row-gap:6px; } .brand .tag { font-size:18px; } .brand .comp { font-size:20px; }
    .right-bits { width:100%; flex-wrap:wrap; gap:8px; } .meta { font-size:15px; width:100%; order:3; }
    a.back { font-size:14px; padding:3px 10px; }
    .cols { display:flex; flex-direction:column; gap:14px; padding:0 0 14px; }
    .mid { order:-1; gap:14px; } .right { gap:14px; }
    .gp { font-size:clamp(26px, 8vw, 44px); } .round { font-size:14px; } .circuit { font-size:16px; }
    .race .body { padding:12px 14px 0; } .cd { margin:12px 14px 0; } .cd .num { font-size:clamp(30px, 10vw, 48px); }
    .sched { margin:12px 14px 0; grid-template-columns:repeat(auto-fit, minmax(92px, 1fr)); gap:6px; }
    .ses b, .ses span { font-size:13px; }
    .head { font-size:15px; padding:5px 12px; } .head small { font-size:12px; }
    #tower, #cons { display:block; } .tr { height:36px; font-size:16px; grid-template-columns:30px 5px 50px minmax(0,1fr) 84px; gap:7px; }
    #cons .tr { grid-template-columns:30px 5px minmax(0,1fr) 54px; }
    .tr .team { font-size:13px; }
    #podium { padding:12px; gap:8px; } .pd .nm { font-size:16px; } .pd .tm { font-size:12px; } .pd .step { font-size:28px; }
    #podium { height:190px; flex:none; } .pd.p1 .step { height:52%; } .pd.p2 .step { height:38%; } .pd.p3 .step { height:26%; }
    .beer .bn { font-size:22px; } .beer .bl { font-size:15px; }
    #boardRows { display:block; } .bln { grid-template-columns:30px 5px minmax(0,1fr) 0 86px 62px 0; gap:7px; padding:0 10px 0 4px; }
    .bln > :nth-child(4), .bln > :nth-child(7) { visibility:hidden; overflow:hidden; }
    .brow { height:36px; font-size:15px; } .brow .dn b { margin-right:6px; } .brow .dn span { font-size:13px; }
    .board .head { flex-wrap:wrap; white-space:normal; row-gap:2px; } .board .head.live small { font-size:14px; } .bhd { font-size:12px; height:28px; }
    .bfoot { flex-direction:column; padding:0 12px 12px; } .bfoot #boardBack { padding:10px; font-size:14px; } .bnote { font-size:12px; padding:6px 12px; white-space:normal; }
    .ticker { height:46px; } .ticker .lab, .ticker .track { font-size:15px; }
  }
  @media (prefers-reduced-motion:reduce) { #car, .ticker .track, .dot { animation:none; } }
'''

BODY = '''
<div class="top">
  <div class="brand"><div class="tag"><span>Pit Wall</span></div><div class="comp" id="season">Formula 1</div></div>
  <div class="right-bits"><div class="meta" id="meta">Loading the calendar…</div><a class="back" href="/var-and-grill/">&larr; Back to the pub</a></div>
</div>
<div class="cols">
  <section class="card tower" aria-label="Timing tower">
    <div class="head" id="towerHead"><span id="towerTitle">Drivers' standings</span><small id="towerSub"></small></div>
    <div id="tower"><div class="empty">Waiting for the timing feed…</div></div>
  </section>
  <div class="mid">
    <section class="card race" aria-label="Next race">
      <div class="head" id="raceHead"><span>Next race</span><small id="raceSub"></small></div>
      <div class="body">
        <div class="round" id="round"></div>
        <h1 class="gp" id="gp">Formula 1</h1>
        <div class="circuit" id="circuit"></div>
      </div>
      <div class="cd" id="cd"><div class="head"><span id="cdHead">Lights out in</span></div><div class="num" id="cdNum">--:--:--</div></div>
      <div class="sched" id="sched"></div>
    </section>
    <section class="card board" id="board" aria-label="Session timing">
      <div class="head" id="boardHead"><span id="boardTitle">Timing</span><small id="boardSub"></small></div>
      <div class="bln bhd"><span style="text-align:center">POS</span><span></span><span>DRIVER</span><span>TEAM</span><span class="t" id="bhTime">BEST LAP</span><span class="t">GAP</span><span class="t" id="bhLaps">LAPS</span></div>
      <div id="boardRows"></div>
      <div class="bnote" id="boardNote"></div>
      <div class="bfoot"><div class="sched" id="sched2"></div><button type="button" id="boardBack">&larr; Race weekend</button></div>
    </section>
    <section class="card podium" aria-label="Last race podium">
      <div class="head"><span>Last time out</span><small id="podSub"></small></div>
      <div id="podium"><div class="empty">Loading…</div></div>
    </section>
  </div>
  <div class="right">
    <section class="card cons" aria-label="Constructors' championship">
      <div class="head"><span>Constructors</span><small>PTS</small></div>
      <div id="cons"><div class="empty">Loading…</div></div>
    </section>
    <section class="card beer" aria-label="Race weekend beer">
      <div class="head"><span>Race weekend beer</span><small id="beerWhere"></small></div>
      <div class="body"><div class="bn" id="beerName">—</div><div class="bl" id="beerLine"></div><a class="bg" id="beerGuide" href="/travel-guides/" hidden>Read the travel guide &rarr;</a></div>
    </section>
  </div>
</div>
<div class="ticker"><div class="lab">PIT WALL</div><div class="run"><span class="track" id="tick">Formula 1 from the pit wall · one beer at a time</span></div></div>
'''

SCRIPT = r'''
(function () {
  var J = 'https://api.jolpi.ca/ergast/f1/';
  var ESPN = 'https://site.api.espn.com/apis/site/v2/sports/racing/f1/scoreboard';
  var $ = function (id) { return document.getElementById(id); };
  var esc = function (s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); };
  var pad = function (n) { return (n < 10 ? '0' : '') + n; };
  var norm = function (s) { return String(s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z]/g, ''); };
  var uk = function (d, o) { return d.toLocaleString('en-GB', Object.assign({ timeZone: 'Europe/London' }, o)); };
  var dayTime = function (d) { return uk(d, { weekday: 'short' }).toUpperCase() + ' ' + uk(d, { hour: '2-digit', minute: '2-digit' }); };
  function get(u) { return fetch(u, { cache: 'no-store' }).then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; }); }

  /* team colours by Jolpica constructorId, with name fallbacks */
  var TEAM = { mclaren: ['#FF8000', 'McLaren'], ferrari: ['#E8002D', 'Ferrari'], red_bull: ['#3671C6', 'Red Bull'], mercedes: ['#27F4D2', 'Mercedes'],
    aston_martin: ['#229971', 'Aston Martin'], alpine: ['#0093CC', 'Alpine'], williams: ['#64C4FF', 'Williams'], rb: ['#6692FF', 'Racing Bulls'],
    sauber: ['#52E252', 'Sauber'], audi: ['#BB0A30', 'Audi'], haas: ['#B6BABD', 'Haas'], cadillac: ['#C9B37E', 'Cadillac'] };
  function team(c) {
    c = c || {}; var id = c.constructorId || '', n = norm(c.name);
    var t = TEAM[id] || (/racingbulls|visacashapp|^rb/.test(n) ? TEAM.rb : /redbull/.test(n) ? TEAM.red_bull : null) ||
      Object.keys(TEAM).map(function (k) { return TEAM[k]; }).filter(function (t) { return n.indexOf(norm(t[1])) >= 0; })[0];
    return { colour: t ? t[0] : '#9aa4b2', name: t ? t[1] : (c.name || '') };
  }

  /* a local beer for every race weekend */
  var BEER = {
    Australia: ['Carlton Draught', 'Brewed in Melbourne since 1864 - the Albert Park pint.'],
    China: ['Tsingtao', "China's best-known lager; Shanghai's craft bars do the rest."],
    Japan: ['Kirin Ichiban', 'A crisp Japanese lager for the Suzuka figure of eight.'],
    Bahrain: ['an ice-cold imported lager', "Bahrain has no breweries of its own, but the circuit bars keep it cold."],
    'Saudi Arabia': ['a "Saudi Champagne"', 'Apple juice and sparkling water - alcohol is banned in Saudi Arabia.'],
    Miami: ['Funky Buddha Floridian Hefeweizen', 'Brewed up the road in Oakland Park, Florida.'],
    Canada: ['Unibroue La Fin du Monde', 'A Quebec tripel from Chambly, just outside Montreal.'],
    Monaco: ['Brasserie de Monaco Blonde', 'Brewed on the harbour - the only brewery in the principality.'],
    Barcelona: ['Estrella Damm', "Barcelona's own since 1876."],
    Madrid: ['Mahou Cinco Estrellas', "Madrid's lager, and a caña is the way to order it."],
    Austria: ['Gösser Märzen', 'Brewed in Leoben, Styria - half an hour from the Red Bull Ring.'],
    UK: ['Hook Norton Old Hooky', 'A proper Oxfordshire bitter, brewed down the road from Silverstone.'],
    Belgium: ['Jupiler', 'Brewed in Jupille, Liège - the Spa weekend pint.'],
    Hungary: ['Dreher Classic', 'Budapest-brewed lager since 1854.'],
    Netherlands: ['Heineken', 'The orange army\'s pint - Amsterdam is half an hour from Zandvoort.'],
    Italy: ['Birrificio Italiano Tipopils', 'A cult pilsner brewed near Como, a short hop from Monza.'],
    Azerbaijan: ['Xirdalan', "Azerbaijan's own lager, brewed just outside Baku."],
    Singapore: ['Tiger', 'Brewed in Singapore since 1932 - made for a humid night race.'],
    USA: ['Shiner Bock', 'A Texas classic from Shiner, an hour and a bit from COTA.'],
    Mexico: ['Victoria', 'Mexico City\'s favourite since 1865.'],
    Brazil: ['Brahma', 'The São Paulo lager - Interlagos runs on it.'],
    'Las Vegas': ['Tenaya Creek Hop Ride IPA', 'Brewed in Las Vegas, a few miles off the Strip.'],
    Qatar: ['a beer in a licensed hotel bar', 'Alcohol is tightly controlled in Qatar - hotel bars only.'],
    UAE: ['a cold lager at Yas Marina', 'Abu Dhabi licenses alcohol at the circuit and hotels.'],
    Portugal: ['Super Bock', 'The Portuguese favourite.'],
    'Emilia Romagna': ['Birra Moretti', 'The Italian classic for an Imola weekend.'],
    Malaysia: ['Tiger', 'Brewed in Selangor - Sepang is just down the road.']
  };
  // every race has a page in the "Travelling F1 in 2026" book
  var BOOK = { Melbourne: 'Melbourne', Shanghai: 'Shanghai', Suzuka: 'Suzuka', Miami: 'Miami', Montreal: 'Montréal', 'Monte Carlo': 'Monaco', Monaco: 'Monaco',
    Barcelona: 'Barcelona', Spielberg: 'Spielberg', Silverstone: 'Silverstone', Spa: 'Spa-Francorchamps', Budapest: 'Budapest', Zandvoort: 'Zandvoort', Monza: 'Monza',
    Madrid: 'Madrid', Baku: 'Baku', 'Kuala Lumpur': 'Kuala Lumpur', 'Marina Bay': 'Singapore', Singapore: 'Singapore', Austin: 'Austin', 'Mexico City': 'Mexico City',
    'São Paulo': 'São Paulo', 'Las Vegas': 'Las Vegas', Lusail: 'Lusail', 'Abu Dhabi': 'Abu Dhabi' };
  function beerFor(race) {
    var L = (race.Circuit || {}).Location || {}, c = L.country, loc = L.locality;
    var k = /Miami/.test(loc) ? 'Miami' : /Vegas/.test(loc) ? 'Las Vegas' : /Barcelona|Montmel/.test(loc) ? 'Barcelona' : /Madrid/.test(loc) ? 'Madrid' : /Imola/.test(loc) ? 'Emilia Romagna' : c;
    return { key: k, beer: BEER[k], where: [loc, c].filter(Boolean).join(', '), book: BOOK[loc] || BOOK[c] };
  }

  var SESS = [['FirstPractice', 'Practice 1', 'FP1'], ['SecondPractice', 'Practice 2', 'FP2'], ['ThirdPractice', 'Practice 3', 'FP3'],
              ['SprintShootout', 'Sprint Quali', 'SQ'], ['SprintQualifying', 'Sprint Quali', 'SQ'], ['Sprint', 'Sprint', 'SPR'], ['Qualifying', 'Qualifying', 'QUALI']];
  function when(o) { return o && o.date ? new Date(o.date + 'T' + (o.time || '12:00:00Z')) : null; }
  function sessions(r) {
    var out = [];
    SESS.forEach(function (s) { var d = when(r[s[0]]); if (d) out.push({ key: s[0], name: s[1], short: s[2], date: d }); });
    out.push({ key: 'Race', name: 'Race', short: 'RACE', date: when(r) });
    return out.sort(function (a, b) { return a.date - b.date; });
  }
  var LEN = { FirstPractice: 60, SecondPractice: 60, ThirdPractice: 60, SprintShootout: 45, SprintQualifying: 45, Sprint: 45, Qualifying: 60, Race: 120 };

  var S = { races: [], drivers: [], cons: [], last: null, espn: null, next: null, ses: [], view: 'auto', tcache: {}, prev: {}, mv: {} };
  var OF = 'https://api.openf1.org/v1/';

  function load() {
    return Promise.all([
      get(J + 'current.json?limit=40'), get(J + 'current/driverstandings.json'), get(J + 'current/constructorstandings.json'),
      get(J + 'current/last/results.json'), get(ESPN)
    ]).then(function (r) {
      if (r[0]) S.races = (((r[0].MRData || {}).RaceTable || {}).Races) || S.races;
      var ds = r[1] && ((((r[1].MRData || {}).StandingsTable || {}).StandingsLists || [])[0]);
      if (ds) { S.drivers = ds.DriverStandings || []; S.dRound = ds.round; S.season = ds.season; }
      var cs = r[2] && ((((r[2].MRData || {}).StandingsTable || {}).StandingsLists || [])[0]);
      if (cs) S.cons = cs.ConstructorStandings || [];
      var lr = r[3] && ((((r[3].MRData || {}).RaceTable || {}).Races || [])[0]);
      if (lr) S.last = lr;
      S.espn = r[4];
      render();
    });
  }

  /* who's who: ESPN names -> Jolpica driver + team */
  function driverIndex() {
    var idx = {};
    S.drivers.forEach(function (d) { var D = d.Driver || {}; var t = team((d.Constructors || [])[0]);
      var v = { code: D.code || (D.familyName || '').slice(0, 3).toUpperCase(), name: D.givenName + ' ' + D.familyName, team: t };
      idx[norm(D.familyName)] = v; idx[norm(D.givenName + D.familyName)] = v; });
    return idx;
  }
  function liveSession() {
    var evs = (S.espn && S.espn.events) || [], best = null;
    evs.forEach(function (e) { (e.competitions || []).forEach(function (c) {
      var st = ((c.status || {}).type || {}).state;
      if (st === 'in') best = { e: e, c: c, state: 'in' };
      else if (st === 'post' && (!best || best.state !== 'in')) { var ago = Date.now() - new Date(c.date || e.date); if (ago > 0 && ago < 6 * 36e5) best = { e: e, c: c, state: 'post' }; }
    }); });
    return best;
  }
  function espnRows(c) {
    var idx = driverIndex();
    return (c.competitors || []).slice().sort(function (a, b) { return (a.order || 99) - (b.order || 99); }).map(function (x, i) {
      var A = x.athlete || {}, full = A.displayName || A.fullName || A.shortName || '';
      var last = full.split(' ').slice(1).join(' ') || full;
      var d = idx[norm(full)] || idx[norm(last)] || idx[norm(full.split(' ').pop())] || { code: last.slice(0, 3).toUpperCase(), team: { colour: '#9aa4b2', name: '' } };
      return { pos: x.order || i + 1, code: d.code, name: d.name || full, team: d.team, v: '' };
    });
  }

  function towerRows(rows, valueHead) {
    if (!rows.length) return '<div class="empty">No timing yet.</div>';
    return rows.map(function (r) {
      return '<div class="tr' + (r.pos == 1 ? ' lead' : '') + '"><span class="p">' + esc(r.pos) + '</span><span class="bar" style="background:' + r.team.colour + '"></span>' +
        '<span class="code">' + esc(r.code) + '</span><span class="team">' + esc(r.team.name) + '</span><span class="v' + (r.dnf ? ' dnf' : '') + '">' + esc(r.v) + '</span></div>';
    }).join('');
  }
  function renderTower(now) {
    var L = liveSession(), head = $('towerHead');
    head.classList.remove('live');
    var abbr = function (c) { var t = c.type || {}; return (t.text || t.abbreviation || 'Session').replace(/^Qual$/, 'Qualifying').replace(/^SS$/, 'Sprint Quali').replace(/^SR$/, 'Sprint'); };
    S.lap = 0;
    if (L && L.state === 'in') {
      var isR = /^(Race|SR|Sprint)$/i.test(((L.c.type || {}).abbreviation) || '');
      S.lap = isR ? (+((L.c.status || {}).period) || 0) : 0;
    }
    if (L && L.state === 'in' && !boardShowing()) {
      head.classList.add('live');
      $('towerTitle').innerHTML = '<span class="dot"></span>Live';
      var isRace = /^(Race|SR|Sprint)$/i.test(((L.c.type || {}).abbreviation) || ''), lap = +((L.c.status || {}).period) || 0;
      $('towerSub').textContent = abbr(L.c) + (isRace && lap ? ' · Lap ' + lap : '');
      S.lap = isRace ? lap : 0;
      $('tower').innerHTML = towerRows(espnRows(L.c));
      return;
    }
    var lastDate = S.last ? when(S.last) : null;
    if (S.last && lastDate && now - lastDate < 3 * 864e5) {
      $('towerTitle').textContent = 'Race result';
      $('towerSub').textContent = (S.last.raceName || '').replace('Grand Prix', 'GP');
      $('tower').innerHTML = towerRows((S.last.Results || []).map(function (x) {
        var D = x.Driver || {}, fin = /^\+?\d|Finished|Lap/.test(x.status || '');
        var v = x.position === '1' ? ((x.Time || {}).time || 'WINNER') : (x.Time || {}).time || (/Lap/.test(x.status) ? x.status.replace(' Laps', ' laps').replace(' Lap', ' lap') : 'DNF');
        return { pos: x.positionText && /^\d+$/.test(x.positionText) ? x.positionText : x.position, code: D.code || (D.familyName || '').slice(0, 3).toUpperCase(), team: team(x.Constructor), v: v, dnf: !fin && !(x.Time || {}).time };
      }));
      return;
    }
    if (L && L.state === 'post' && !boardShowing()) {
      $('towerTitle').textContent = 'Classification';
      $('towerSub').textContent = abbr(L.c);
      $('tower').innerHTML = towerRows(espnRows(L.c));
      return;
    }
    $('towerTitle').textContent = "Drivers' standings";
    $('towerSub').textContent = S.dRound ? 'Rd ' + S.dRound : '';
    $('tower').innerHTML = towerRows(S.drivers.map(function (d) {
      var D = d.Driver || {};
      return { pos: d.position || d.positionText, code: D.code || (D.familyName || '').slice(0, 3).toUpperCase(), team: team((d.Constructors || [])[0]), v: d.points + ' PTS' };
    }));
  }

  function pickNext(now) {
    return S.races.filter(function (r) { var d = when(r); return d && now - d < 3 * 36e5; })[0] || null;
  }
  function renderRace(now) {
    var r = S.next;
    if (!r) {
      $('gp').textContent = 'Season over';
      $('round').textContent = S.season ? S.season + ' season' : '';
      $('circuit').textContent = 'See you on the grid in March.';
      $('cd').hidden = true; $('sched').innerHTML = ''; $('raceSub').textContent = '';
      $('meta').textContent = 'Off season';
      return;
    }
    var L = r.Circuit || {}, loc = L.Location || {};
    $('round').textContent = 'Round ' + r.round + ' of ' + Math.max.apply(null, S.races.map(function (x) { return +x.round || 0; }));
    $('gp').textContent = r.raceName;
    $('circuit').textContent = (L.circuitName || '') + ' · ' + [loc.locality, loc.country].filter(Boolean).join(', ');
    var ses = sessions(r), live = null, nxt = null;
    ses.forEach(function (s) {
      var end = +s.date + (LEN[s.key] || 60) * 6e4;
      s.state = now >= end ? 'done' : now >= s.date ? 'live' : 'pre';
      if (s.state === 'live') live = s;
      if (s.state === 'pre' && !nxt) nxt = s;
    });
    // trust the timing feed if it says a session is running
    var EL = liveSession();
    if (EL && EL.state === 'in' && !live) live = nxt;
    S.ses = ses; S.liveSes = live; S.nextSes = nxt;
    $('sched').style.setProperty('--n', ses.length);
    renderTiles();
    var raceDay = ses[ses.length - 1].date;
    $('raceSub').textContent = uk(raceDay, { day: 'numeric', month: 'short' }).toUpperCase() + ' · UK TIMES';
    $('meta').textContent = (r.raceName || '').replace('Grand Prix', 'GP') + ' · ' + uk(raceDay, { weekday: 'long', day: 'numeric', month: 'long' }) + ' · ' + uk(raceDay, { hour: '2-digit', minute: '2-digit' });
    $('cd').hidden = false;
    tickCountdown();
    // beer
    var b = beerFor(r);
    $('beerWhere').textContent = b.where;
    $('beerName').textContent = b.beer ? b.beer[0].replace(/^\w/, function (c) { return c.toUpperCase(); }) : 'Whatever the locals drink';
    $('beerLine').textContent = b.beer ? b.beer[1] : 'Ask at the bar for something brewed nearby.';
    var gl = $('beerGuide');
    if (b.book) { gl.hidden = false; gl.href = '/travel-guides/guide/?shelf=f1-2026&city=' + encodeURIComponent(b.book); gl.innerHTML = 'Read the ' + esc(b.book) + ' race guide &rarr;'; } else gl.hidden = true;
  }
  function renderTiles() {
    var live = S.liveSes, nxt = S.nextSes, cur = boardKey();
    var mk = function (short) { return S.ses.map(function (s) {
      var cls = s === live ? 'live' : s.state === 'done' ? 'done' : s === nxt && !live ? 'next' : '';
      var click = s === live || s.state === 'done';
      var tag = click ? 'button type="button" data-k="' + s.key + '" title="Show ' + esc(s.name) + ' timing"' : 'div';
      return '<' + tag + ' class="ses ' + cls + (cur === s.key ? ' on' : '') + '"><b>' + esc(short ? s.short : s.name) + '</b><span>' + (s === live ? 'LIVE' : dayTime(s.date)) + '</span></' + tag.split(' ')[0] + '>';
    }).join(''); };
    $('sched').style.setProperty('--n', S.ses.length); $('sched').innerHTML = mk(false);
    $('sched2').style.setProperty('--n', S.ses.length); $('sched2').innerHTML = mk(true);
  }
  /* ---------- the big timing board ---------- */
  var ABBR = { FirstPractice: 'FP1', SecondPractice: 'FP2', ThirdPractice: 'FP3', Qualifying: 'Qual', Race: 'Race', SprintQualifying: 'SS', SprintShootout: 'SS', Sprint: 'SR' };
  var OFNAME = { FirstPractice: ['Practice 1'], SecondPractice: ['Practice 2'], ThirdPractice: ['Practice 3'], Qualifying: ['Qualifying'], Race: ['Race'],
                 SprintQualifying: ['Sprint Qualifying', 'Sprint Shootout'], SprintShootout: ['Sprint Shootout', 'Sprint Qualifying'], Sprint: ['Sprint'] };
  function boardKey() {
    // which session the board shows, or null for the race weekend view
    if (S.view === 'race') return null;
    if (S.view !== 'auto') return S.view;
    if (S.liveSes) return S.liveSes.key;
    var now = Date.now(), recent = S.ses.filter(function (x) { var end = +x.date + (LEN[x.key] || 60) * 6e4; return x.state === 'done' && now - end < 90 * 6e4; }).pop();
    return recent ? recent.key : null;
  }
  function boardShowing() { return !!boardKey(); }
  function sesOf(k) { return S.ses.filter(function (x) { return x.key === k; })[0]; }
  function espnComp(k) {
    var out = null;
    ((S.espn && S.espn.events) || []).forEach(function (e) { (e.competitions || []).forEach(function (c) { if (((c.type || {}).abbreviation) === ABBR[k]) out = c; }); });
    return out;
  }
  function fmtT(sec) { if (sec == null || isNaN(sec)) return ''; var m = Math.floor(sec / 60), x = (sec - m * 60).toFixed(3); return (m ? m + ':' + (x < 10 ? '0' : '') : '') + x; }
  function secs(t) { if (!t) return null; var p = String(t).split(':'); return p.length > 1 ? +p[0] * 60 + +p[1] : +p[0]; }
  function lastOf(v) { if (!Array.isArray(v)) return v; for (var i = v.length - 1; i >= 0; i--) if (v[i] != null) return v[i]; return null; }
  function openf1(k) {
    return get(OF + 'sessions?meeting_key=latest').then(function (list) {
      if (!Array.isArray(list)) return null;
      var names = OFNAME[k] || [], ss = list.filter(function (x) { return names.indexOf(x.session_name) >= 0; })[0];
      if (!ss) return null;
      return Promise.all([get(OF + 'session_result?session_key=' + ss.session_key), get(OF + 'drivers?session_key=' + ss.session_key)]).then(function (r) {
        var res = r[0], drv = r[1];
        if (!Array.isArray(res) || !res.length) return null;
        var by = {}; (Array.isArray(drv) ? drv : []).forEach(function (d) { by[d.driver_number] = d; });
        var quali = /Qualifying|Shootout/.test(ss.session_name), race = /^(Race|Sprint)$/.test(ss.session_name);
        var rows = res.slice().sort(function (a, b) { return (a.position || 99) - (b.position || 99); }).map(function (x, i) {
          var d = by[x.driver_number] || {}, t = team({ name: d.team_name });
          var out = x.dnf ? 'DNF' : x.dns ? 'DNS' : x.dsq ? 'DSQ' : '';
          var dur = lastOf(x.duration), gap = lastOf(x.gap_to_leader);
          var seg = Array.isArray(x.duration) ? ['Q1', 'Q2', 'Q3'][x.duration.reduce(function (a, v, j) { return v != null ? j : a; }, 0)] : '';
          return { pos: x.position || i + 1, code: d.name_acronym || '', name: d.full_name ? d.full_name.split(' ').map(function (w) { return w.length > 1 && w === w.toUpperCase() ? w.charAt(0) + w.slice(1).toLowerCase() : w; }).join(' ') : '',
            team: { colour: d.team_colour ? '#' + d.team_colour : t.colour, name: t.name || d.team_name || '' },
            time: out || (race && i > 0 ? '' : fmtT(dur)), gap: out ? '' : (i === 0 ? '' : typeof gap === 'number' ? '+' + gap.toFixed(3) : (gap || '')),
            laps: quali ? seg : (x.number_of_laps != null ? x.number_of_laps : ''), dnf: !!out };
        });
        return { rows: rows, src: 'Timing from OpenF1', timeHead: race ? 'TIME' : quali ? 'BEST' : 'BEST LAP', lapsHead: quali ? 'OUT' : 'LAPS' };
      });
    });
  }
  function jolpica(k) {
    var r = S.next; if (!r || !/^(Qualifying|Sprint|Race)$/.test(k)) return Promise.resolve(null);
    var file = k === 'Qualifying' ? 'qualifying' : k === 'Sprint' ? 'sprint' : 'results';
    return get(J + r.season + '/' + r.round + '/' + file + '.json').then(function (d) {
      var R = d && (((d.MRData || {}).RaceTable || {}).Races || [])[0];
      var list = R && (R.QualifyingResults || R.SprintResults || R.Results);
      if (!list || !list.length) return null;
      var pole = k === 'Qualifying' ? secs(list[0].Q3 || list[0].Q2 || list[0].Q1) : null;
      return { src: 'Results from Jolpica', timeHead: k === 'Qualifying' ? 'BEST' : 'TIME', lapsHead: k === 'Qualifying' ? 'OUT' : 'LAPS', rows: list.map(function (x) {
        var D = x.Driver || {}, best = x.Q3 || x.Q2 || x.Q1, fin = (x.Time || {}).time;
        var g = k === 'Qualifying' && x.Q3 && pole && x.position !== '1' ? '+' + (secs(x.Q3) - pole).toFixed(3) : '';
        return { pos: x.position, code: D.code || (D.familyName || '').slice(0, 3).toUpperCase(), name: D.givenName + ' ' + D.familyName, team: team(x.Constructor),
          time: k === 'Qualifying' ? (best || '') : (x.position === '1' ? fin : ''), gap: k === 'Qualifying' ? g : (x.position === '1' ? '' : fin || x.status || ''),
          laps: k === 'Qualifying' ? (x.Q3 ? 'Q3' : x.Q2 ? 'Q2' : 'Q1') : x.laps, dnf: k !== 'Qualifying' && !fin && !/Lap/.test(x.status || '') };
      }) };
    });
  }
  function timing(k) {
    var c = S.tcache[k];
    if (c && (c.full || Date.now() - c.at < 5 * 6e4)) return Promise.resolve(c.data);
    return openf1(k).catch(function () { return null; }).then(function (d) { return d || jolpica(k).catch(function () { return null; }); }).then(function (d) {
      if (!d) { var ec = espnComp(k); if (ec && (ec.competitors || []).length) d = { rows: espnRows(ec).map(function (x) { return Object.assign(x, { time: '', gap: '', laps: '' }); }), src: 'Order from ESPN - lap times show here once OpenF1 has them (it locks while any session is live)', timeHead: 'BEST LAP', lapsHead: 'LAPS', partial: true }; }
      if (d) S.tcache[k] = { data: d, at: Date.now(), full: !d.partial && Date.now() - +((sesOf(k) || {}).date || 0) > 3 * 36e5 };
      return d;
    });
  }
  function boardRows(rows, live) {
    if (!rows || !rows.length) return '<div class="empty">No timing for this session yet.</div>';
    return rows.map(function (r) {
      var m = live && S.mv[r.code], mv = m ? (m.d > 0 ? '<span class="mv up">▲' + m.d + '</span>' : '<span class="mv down">▼' + (-m.d) + '</span>') : '';
      return '<div class="bln brow' + (r.pos == 1 ? ' lead' : '') + (m ? (m.d > 0 ? ' moved' : ' dropped') : '') + '"><span class="p">' + esc(r.pos) + '</span><span class="bar" style="background:' + r.team.colour + '"></span>' +
        '<span class="dn"><b>' + esc(r.code) + '</b><span>' + esc(r.name || '') + '</span>' + mv + '</span><span class="tm">' + esc(r.team.name) + '</span>' +
        '<span class="t' + (r.dnf ? ' dnf' : '') + '">' + esc(r.time || '') + '</span><span class="t">' + esc(r.gap || '') + '</span><span class="t">' + esc(r.laps == null ? '' : r.laps) + '</span></div>';
    }).join('');
  }
  var boardSeq = 0;
  function renderBoard() {
    var k = boardKey(), mid = document.querySelector('.mid');
    mid.classList.toggle('boardmode', !!k);
    renderTiles();
    if (!k) return;
    var s = sesOf(k) || { name: k }, live = S.liveSes && S.liveSes.key === k, head = $('boardHead');
    head.classList.toggle('live', !!live);
    $('boardTitle').innerHTML = live ? '<span class="dot"></span>Live timing · ' + esc(s.name) : esc(s.name) + ' · ' + (S.next ? esc(S.next.raceName.replace('Grand Prix', 'GP')) : '');
    $('boardBack').hidden = !!live && S.view === 'auto' ? false : false;
    if (live) {
      var ec = espnComp(k) || ((liveSession() || {}).c);
      var rows = ec ? espnRows(ec) : [], now = Date.now();
      // movers since the last update stay lit for a minute
      rows.forEach(function (r) { var was = S.prev[r.code]; if (was && was !== r.pos) S.mv[r.code] = { d: was - r.pos, until: now + 6e4 }; S.prev[r.code] = r.pos; });
      Object.keys(S.mv).forEach(function (c) { if (S.mv[c].until < now) delete S.mv[c]; });
      $('bhTime').textContent = 'BEST LAP'; $('bhLaps').textContent = 'LAPS';
      $('boardRows').innerHTML = boardRows(rows.map(function (r) { return Object.assign(r, { time: '', gap: '', laps: '' }); }), true);
      $('boardNote').textContent = 'Live running order from ESPN, updated every 15 seconds · lap times appear when the session ends';
      tickCountdown();
      return;
    }
    $('boardSub').textContent = 'Final';
    var seq = ++boardSeq;
    if (!S.tcache[k]) { $('boardRows').innerHTML = '<div class="empty">Loading the timing…</div>'; $('boardNote').textContent = ''; }
    timing(k).then(function (d) {
      if (seq !== boardSeq) return;
      $('bhTime').textContent = d ? d.timeHead : 'TIME'; $('bhLaps').textContent = d ? d.lapsHead : 'LAPS';
      $('boardRows').innerHTML = d ? boardRows(d.rows, false) : '<div class="empty">No timing for this session yet - try again in a few minutes.</div>';
      $('boardNote').textContent = d ? d.src : '';
    });
  }
  document.addEventListener('click', function (e) {
    var t = e.target.closest && e.target.closest('.ses[data-k]');
    if (t) { S.view = t.getAttribute('data-k'); renderBoard(); renderTower(Date.now()); return; }
    if (e.target.closest && e.target.closest('#boardBack')) { S.view = 'race'; renderBoard(); renderTower(Date.now()); }
  });
  function tickCountdown() {
    var cd = $('cd'), now = Date.now(), live = S.liveSes, nxt = S.nextSes;
    if (!S.next) return;
    if (live) {
      cd.classList.add('live');
      $('cdHead').innerHTML = '<span class="dot"></span>' + esc(live.name) + ' - live now';
      var left = Math.max(0, Math.floor((+live.date + (LEN[live.key] || 60) * 6e4 - now) / 1000));
      $('cdNum').textContent = live.key === 'Race' ? (S.lap ? 'LAP ' + S.lap : 'LIGHTS OUT') : pad(Math.floor(left / 60)) + ':' + pad(left % 60) + ' TO GO';
      if (boardKey() === live.key) $('boardSub').textContent = /^(Race|Sprint)$/.test(live.key) ? (S.lap ? 'LAP ' + S.lap : 'RACING') : pad(Math.floor(left / 60)) + ':' + pad(left % 60) + ' TO GO';
      return;
    }
    cd.classList.remove('live');
    if (!nxt) { $('cdHead').textContent = 'Chequered flag'; $('cdNum').textContent = 'FINISHED'; return; }
    $('cdHead').textContent = nxt.key === 'Race' ? 'Lights out in' : nxt.name + ' starts in';
    var s = Math.max(0, Math.floor((nxt.date - now) / 1000)), d = Math.floor(s / 86400); s %= 86400;
    $('cdNum').textContent = (d ? d + (d === 1 ? ' DAY ' : ' DAYS ') : '') + pad(Math.floor(s / 3600)) + ':' + pad(Math.floor(s % 3600 / 60)) + ':' + pad(s % 60);
  }
  function renderPodium() {
    var r = S.last;
    if (!r || !(r.Results || []).length) { $('podium').innerHTML = '<div class="empty">No races yet this season.</div>'; return; }
    $('podSub').textContent = (r.raceName || '').replace('Grand Prix', 'GP');
    var top = r.Results.slice(0, 3), order = [top[1], top[0], top[2]], cls = ['p2', 'p1', 'p3'];
    $('podium').innerHTML = order.map(function (x, i) {
      if (!x) return '<div></div>';
      var D = x.Driver || {}, t = team(x.Constructor);
      return '<div class="pd ' + cls[i] + '" style="--c:' + t.colour + '"><div class="nm">' + esc(D.familyName) + '</div><div class="tm">' + esc(t.name) +
        ' · ' + esc((x.Time || {}).time || x.status || '') + '</div><div class="step">' + esc(x.position) + '</div></div>';
    }).join('');
  }
  function renderCons() {
    if (!S.cons.length) { $('cons').innerHTML = '<div class="empty">Standings appear after round 1.</div>'; return; }
    $('cons').innerHTML = S.cons.map(function (c) {
      var t = team(c.Constructor);
      return '<div class="tr' + (c.position == 1 ? ' lead' : '') + '"><span class="p">' + esc(c.position || c.positionText) + '</span><span class="bar" style="background:' + t.colour + '"></span><span class="code" style="letter-spacing:0">' + esc(t.name) + '</span><span class="v">' + esc(c.points) + '</span></div>';
    }).join('');
  }
  function renderTicker() {
    var bits = [];
    if (S.last && S.last.Results && S.last.Results[0]) { var w = S.last.Results[0].Driver; bits.push('LAST TIME OUT: ' + (w.givenName + ' ' + w.familyName).toUpperCase() + ' WON THE ' + S.last.raceName.toUpperCase()); }
    if (S.drivers.length) bits.push('CHAMPIONSHIP: ' + S.drivers.slice(0, 5).map(function (d) { return d.position + '. ' + (d.Driver.code || d.Driver.familyName).toUpperCase() + ' ' + d.points; }).join('  '));
    if (S.cons.length) bits.push('CONSTRUCTORS: ' + S.cons.slice(0, 3).map(function (c) { return c.position + '. ' + team(c.Constructor).name.toUpperCase() + ' ' + c.points; }).join('  '));
    var n = S.races.filter(function (r) { return when(r) > Date.now(); });
    if (n[1]) bits.push('AFTER THAT: ' + n[1].raceName.toUpperCase() + ' · ' + uk(when(n[1]), { day: 'numeric', month: 'short' }).toUpperCase());
    bits.push('ONE BEER AT A TIME');
    var t = $('tick'); t.innerHTML = bits.map(esc).join('<i>◆</i>');
    t.style.setProperty('--d', Math.max(30, t.textContent.length / 5) + 's');
  }
  function render() {
    var now = Date.now();
    if (!S.races.length && !S.drivers.length) { var m = $('msg'); m.textContent = 'The F1 timing feed is having a pit stop - try again in a minute.'; m.style.display = 'block'; return; }
    $('msg').style.display = 'none';
    $('season').textContent = 'Formula 1 · ' + (S.season || (S.races[0] || {}).season || '');
    S.next = pickNext(now);
    var wasLive = S.liveKey;
    renderRace(now);
    S.liveKey = S.liveSes ? S.liveSes.key : null;
    if (S.liveKey && S.liveKey !== wasLive) { S.view = 'auto'; S.prev = {}; S.mv = {}; }   // a new session going live takes over the board
    renderTower(now); tickCountdown(); renderBoard(); renderPodium(); renderCons(); renderTicker();
  }

  setInterval(tickCountdown, 1000);
  /* fit the 1920x1080 layout to any screen */
  var st = $('stage'), mq = matchMedia('(max-width: 1000px), (max-aspect-ratio: 1/1)');
  function fit() { if (mq.matches) { st.style.transform = ''; return; } var s = Math.min(innerWidth / 1920, innerHeight / 1080); st.style.transform = 'translate(-50%, -50%) scale(' + s + ')'; }
  addEventListener('resize', fit); fit();
  /* start lights: five reds, then out */
  var gl = [].slice.call(document.querySelectorAll('.gl'));
  (function lights() { var i = 0;
    var t = setInterval(function () { if (i < 5) { gl[i * 2].setAttribute('fill', '#ff1a1a'); gl[i * 2 + 1].setAttribute('fill', '#ff1a1a'); i++; }
      else { clearInterval(t); setTimeout(function () { gl.forEach(function (g) { g.setAttribute('fill', '#3a0606'); }); setTimeout(lights, 6000); }, 900); } }, 900); })();

  (function loop() {
    load().then(function () {
      var live = S.liveSes || (liveSession() || {}).state === 'in';
      setTimeout(loop, (live ? 15 : 300) * 1000);
    }, function () { setTimeout(loop, 60000); });
  })();
})();
'''

PAGE = '''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>F1 Pit Wall - Rob Callery</title>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Titillium+Web:wght@400;600;700&display=swap" rel="stylesheet">
<style>__CSS__</style>
</head>
<body>
<div class="scene" aria-hidden="true"><svg viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice">__SVG__</svg></div>
<div class="fit"><div class="stage" id="stage">__BODY__</div></div>
<div class="msg" id="msg" role="status"></div>
<script>__SCRIPT__</script>
</body>
</html>
'''
out = PAGE.replace('__CSS__', CSS).replace('__SVG__', scene()).replace('__BODY__', BODY).replace('__SCRIPT__', SCRIPT)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w').write(out)
print('pit wall', len(out) // 1024, 'KB')
