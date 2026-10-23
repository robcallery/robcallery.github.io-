# CALFAX 303: the Leeds match centre as a Ceefax page.
# Rotates: Leeds game -> other games -> table top half -> table bottom half.
import os
OUT = '/home/claude/site/var-and-grill/leeds/ceefax/index.html'

PAGE = r'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CALFAX 303 - Rob Callery</title>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=VT323&display=swap" rel="stylesheet">
<style>
  :root{--bk:#000;--wh:#fff;--ye:#ff0;--cy:#0ff;--gr:#0f0;--re:#f00;--ma:#f0f;--bl:#00f}
  *{box-sizing:border-box;margin:0;padding:0}
  html,body{background:#000;color:var(--wh);min-height:100%}
  body{font-family:VT323,'Courier New',monospace;display:flex;justify-content:center;align-items:center;min-height:100vh;min-height:100dvh;padding:16px}
  .tv{width:min(100%,820px);font-size:clamp(13px,min(3.5vw,2.95vh),30px);line-height:1.12;position:relative;padding:.4em .6em .8em;border-radius:14px;
      background:#000;box-shadow:0 0 0 2px #111,0 0 60px rgba(0,255,255,.07) inset}
  .tv::after{content:"";position:absolute;inset:0;border-radius:14px;pointer-events:none;
      background:repeating-linear-gradient(180deg,rgba(255,255,255,.04) 0 1px,transparent 1px 3px)}
  .row{white-space:pre-wrap;min-height:1.12em}
  .hdr{display:flex;justify-content:space-between;gap:.5em}
  .w{color:var(--wh)}.y{color:var(--ye)}.c{color:var(--cy)}.g{color:var(--gr)}.r{color:var(--re)}.m{color:var(--ma)}
  .band{display:flex;gap:.18em;margin:.25em 0 .1em}
  .band i{display:block;flex:1;height:.55em;background:var(--cy)}
  .band i:nth-child(3n){height:.85em}.band i:nth-child(4n){opacity:.65}
  .strap{display:flex;justify-content:space-between;background:var(--bl);padding:0 .3em;margin:.2em 0 .1em}
  .title{font-size:2.15em;line-height:1;color:var(--ye);letter-spacing:.04em;margin:.12em 0 .2em;white-space:nowrap;overflow:hidden;text-overflow:clip}
  .screen{min-height:17em}
  .page{display:none}.page.on{display:block}
  .dh{font-size:1.5em;line-height:1.05}
  .score{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:0 .6em;margin:.15em 0}
  .score span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .ev{display:grid;grid-template-columns:1fr 1fr;gap:0 1em;margin:.25em 0}
  .ev div{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .ev .a{text-align:right}
  .list .ln{display:grid;grid-template-columns:minmax(0,1fr) 5ch minmax(0,1fr) 9ch;gap:0 .5ch;white-space:nowrap}
  .list .ln span{overflow:hidden;text-overflow:ellipsis}
  .list .ln .h{text-align:right}.list .ln .s{text-align:center}.list .ln .t{text-align:right}
  .tbl .ln{display:grid;grid-template-columns:3ch minmax(0,1fr) 3ch 4ch 4ch;gap:0 .6ch;white-space:nowrap}
  .tbl .ln span{overflow:hidden;text-overflow:ellipsis}
  .tbl .ln .n,.tbl .ln .p,.tbl .ln .d,.tbl .ln .pt{text-align:right}
  .tbl .ln.hd{color:var(--cy)}
  .tbl .ln.leeds{color:var(--ye)}
  .tbl .ln.zu{border-left:.25em solid var(--bl)}.tbl .ln.ze{border-left:.25em solid var(--ma)}.tbl .ln.zr{border-left:.25em solid var(--re)}
  .tbl .ln{border-left:.25em solid transparent;padding-left:.15em}
  .live{color:var(--gr)}
  .blink{animation:bl 1s steps(2) infinite}@keyframes bl{50%{opacity:0}}
  .bg-bl{background:var(--bl)}.bg-re{background:var(--re)}
  .fastext{display:grid;grid-template-columns:repeat(4,1fr);margin-top:.8em}
  .fastext a,.fastext button{display:block;text-align:center;padding:.18em .2em;text-decoration:none;color:#000;font:inherit;font-size:.95em;border:0;cursor:pointer}
  .fastext a:hover,.fastext a:focus-visible,.fastext button:hover,.fastext button:focus-visible{outline:3px solid #fff;outline-offset:-3px}
  .k-r{background:var(--re);color:#fff!important}.k-g{background:var(--gr)}.k-y{background:var(--ye)}.k-c{background:var(--cy)}
  .k-g[aria-pressed="true"]{background:#fff}
  .muted{opacity:.85}
  .small{font-size:.75em}
  @media (prefers-reduced-motion:reduce){.blink{animation:none}}
</style>
</head>
<body>
<main class="tv">
  <h1 style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)">Leeds United on CALFAX 303</h1>
  <div class="row hdr"><span><span class="w">P303</span> <span class="y">CALFAX 303</span></span><span><span class="w" id="date"></span> <span class="y" id="clock"></span></span></div>
  <div class="band" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
  <div class="strap"><span class="y">LEEDS UNITED</span><span class="w" id="sub">1/4</span></div>
  <div class="title" id="title">FOOTBALL</div>
  <div class="screen" aria-live="polite">
    <section class="page on" id="pg-msg"><div class="row c">SEARCHING FOR A SIGNAL<span class="blink">...</span></div></section>
    <section class="page" id="pg-leeds"></section>
    <section class="page" id="pg-other"></section>
    <section class="page" id="pg-top"></section>
    <section class="page" id="pg-bot"></section>
  </div>
  <div class="fastext">
    <a href="/var-and-grill/leeds/" class="k-r">MATCH CTR</a>
    <button type="button" class="k-g" id="hold" aria-pressed="false">HOLD</button>
    <button type="button" class="k-y" id="next">NEXT</button>
    <a href="/var-and-grill/" class="k-c">THE BAR</a>
  </div>
  <div class="row muted small" style="margin-top:.6em">Scores from ESPN's public feed. Not affiliated with Leeds United or any league. Drink responsibly.</div>
</main>
<script>
(function () {
  var TEAM = '357';
  var LEAGUES = [['eng.1', 'PREMIER LEAGUE'], ['eng.2', 'CHAMPIONSHIP'], ['eng.fa', 'FA CUP'], ['eng.league_cup', 'CARABAO CUP']];
  var API = 'https://site.api.espn.com/apis/';
  var SHORT = { 'Manchester United': 'Man Utd', 'Manchester City': 'Man City', 'Tottenham Hotspur': 'Spurs', 'Wolverhampton Wanderers': 'Wolves',
    'Brighton & Hove Albion': 'Brighton', 'Nottingham Forest': "Nott'm Forest", 'Newcastle United': 'Newcastle', 'West Ham United': 'West Ham',
    'Leeds United': 'Leeds', 'AFC Bournemouth': 'Bournemouth', 'Queens Park Rangers': 'QPR', 'West Bromwich Albion': 'West Brom',
    'Sheffield United': 'Sheff Utd', 'Sheffield Wednesday': 'Sheff Wed', 'Crystal Palace': 'C Palace', 'Preston North End': 'Preston' };
  var $ = function (id) { return document.getElementById(id); };
  var esc = function (s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); };
  var pad = function (n) { return (n < 10 ? '0' : '') + n; };
  var ymd = function (d) { return d.getFullYear() + pad(d.getMonth() + 1) + pad(d.getDate()); };
  var ukDay = function (d) { return d.toLocaleDateString('en-GB', { timeZone: 'Europe/London', year: 'numeric', month: '2-digit', day: '2-digit' }); };
  var day = function (d) { return d.toLocaleDateString('en-GB', { timeZone: 'Europe/London', weekday: 'short' }).toUpperCase(); };
  var dayDate = function (d) { return d.toLocaleDateString('en-GB', { timeZone: 'Europe/London', weekday: 'short', day: 'numeric', month: 'short' }).toUpperCase().replace(/,/g, ''); };
  var hm = function (d) { return d.toLocaleTimeString('en-GB', { timeZone: 'Europe/London', hour: '2-digit', minute: '2-digit' }); };
  function get(u) { return fetch(u, { cache: 'no-store' }).then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; }); }
  function nm(t) { t = t || {}; return SHORT[t.displayName] || t.shortDisplayName || t.displayName || t.name || ''; }
  function mapEvent(e) {
    var c = (e.competitions || [])[0] || {}, cs = c.competitors || [];
    var h = cs.filter(function (x) { return x.homeAway === 'home'; })[0] || cs[0] || {}, a = cs.filter(function (x) { return x.homeAway === 'away'; })[0] || cs[1] || {};
    var st = c.status || e.status || {}, ty = st.type || {};
    return { id: String(e.id), date: new Date(e.date), raw: c, state: ty.state || 'pre', name: ty.name || '', detail: ty.shortDetail || '',
      clock: st.displayClock || '', period: st.period || 0,
      home: { id: String((h.team || {}).id || h.id), name: nm(h.team), score: +h.score || 0 },
      away: { id: String((a.team || {}).id || a.id), name: nm(a.team), score: +a.score || 0 } };
  }
  function minute(g) {
    if (/HALFTIME/.test(g.name)) return 'HT';
    var m = (g.clock || '').replace(/'$/, '');
    return m ? m + "'" : 'LIVE';
  }

  var S = { main: null, league: 'eng.1', comp: 'PREMIER LEAGUE', list: [], listMode: 'none', listLabel: '', table: [], live: [] };

  /* ---------- 1. find Leeds' live, just-finished or next game ---------- */
  function findMain() {
    var found = [], jobs = [];
    function scan(d, lg, label) {
      ((d && d.events) || []).forEach(function (e) {
        var g = mapEvent(e);
        if (g.home.id !== TEAM && g.away.id !== TEAM) return;
        g.lg = lg; g.comp = (((d.leagues || [])[0] || {}).name || label).toUpperCase();
        found.push(g);
      });
    }
    LEAGUES.forEach(function (L) {
      var base = API + 'site/v2/sports/soccer/' + L[0];
      jobs.push(get(base + '/scoreboard').then(function (d) { scan(d, L[0], L[1]); }));
      jobs.push(get(base + '/teams/' + TEAM + '/schedule?fixture=true').then(function (d) { scan(d, L[0], L[1]); }));
      jobs.push(get(base + '/teams/' + TEAM + '/schedule').then(function (d) { scan(d, L[0], L[1]); }));
    });
    return Promise.all(jobs).then(function () {
      var now = Date.now(), by = function (k) { return function (a, b) { return k * (a.date - b.date); }; };
      var live = found.filter(function (f) { return f.state === 'in'; })[0];
      var recent = found.filter(function (f) { return f.state === 'post' && now - f.date < 4 * 36e5; }).sort(by(-1))[0];
      var next = found.filter(function (f) { return f.state === 'pre' && f.date > now - 3 * 36e5; }).sort(by(1))[0];
      return live || recent || next || found.filter(function (f) { return f.state === 'post'; }).sort(by(-1))[0] || null;
    });
  }

  /* ---------- 2. refresh the game, the other games and the table ---------- */
  function refresh() {
    var m = S.main;
    var base = API + 'site/v2/sports/soccer/' + S.league;
    var jobs = [];
    // the Leeds game on its own date (gives the live score and the goals)
    jobs.push(get(base + '/scoreboard?dates=' + ymd(m.date)).then(function (d) {
      var g = ((d && d.events) || []).map(mapEvent).filter(function (x) { return x.id === m.id; })[0];
      if (g) { g.lg = m.lg; g.comp = m.comp; S.main = g; }
    }));
    // today's games in this competition, otherwise the next round of fixtures
    var today = new Date(), until = new Date(Date.now() + 21 * 864e5);
    jobs.push(get(base + '/scoreboard?dates=' + ymd(today)).then(function (d) {
      var list = ((d && d.events) || []).map(mapEvent).filter(function (g) { return ukDay(g.date) === ukDay(today); });
      if (list.length) { S.list = list; S.listMode = 'today'; S.listLabel = ''; return; }
      return get(base + '/scoreboard?dates=' + ymd(today) + '-' + ymd(until) + '&limit=300').then(function (n) {
        var up = ((n && n.events) || []).map(mapEvent).filter(function (g) { return g.state === 'pre' && g.date > today; }).sort(function (a, b) { return a.date - b.date; });
        if (!up.length) { S.list = []; S.listMode = 'none'; return; }
        var first = up[0].date, round = up.filter(function (g) { return g.date - first < 4 * 864e5; }), last = round[round.length - 1].date;
        S.list = round; S.listMode = 'next';
        S.listLabel = ukDay(first) === ukDay(last) ? dayDate(first) : day(first) + '-' + dayDate(last);
      });
    }));
    // the league table (cups have no table, so fall back to Leeds' league)
    var tlg = /^eng\.[12]$/.test(S.league) ? S.league : 'eng.1';
    jobs.push(get(API + 'v2/sports/soccer/' + tlg + '/standings').then(function (d) {
      if (!d) return;
      var entries = (((d.children || [])[0] || {}).standings || d.standings || {}).entries || [];
      var stat = function (e, n) { var s = (e.stats || []).filter(function (x) { return x.name === n || x.type === n; })[0]; return +(s && s.value) || 0; };
      S.table = entries.map(function (e) {
        return { id: String(e.team.id), name: nm(e.team), p: stat(e, 'gamesPlayed'), gf: stat(e, 'pointsFor'), ga: stat(e, 'pointsAgainst'),
          gd: stat(e, 'pointDifferential'), pts: stat(e, 'points'), rank: stat(e, 'rank') };
      }).sort(function (a, b) { return a.rank - b.rank; });
      S.tableLeague = tlg;
    }));
    return Promise.all(jobs).then(render);
  }

  /* ---------- 3. draw the four pages ---------- */
  function countdown(d) {
    var s = Math.max(0, Math.floor((d - Date.now()) / 1000)), dd = Math.floor(s / 86400);
    s %= 86400;
    return (dd ? dd + (dd === 1 ? ' DAY ' : ' DAYS ') : '') + pad(Math.floor(s / 3600)) + ':' + pad(Math.floor(s % 3600 / 60)) + ':' + pad(s % 60);
  }
  function statusLine(g) {
    if (g.state === 'in') return '<span class="live">' + (minute(g) === 'HT' ? 'HALF TIME' : '<span class="blink">LIVE</span> ' + esc(minute(g))) + '</span>';
    if (g.state === 'post') return '<span class="c">' + (/PEN/.test(g.name + g.detail) ? 'FULL TIME (PENS)' : /AET|EXTRA/.test(g.name + g.detail) ? 'FULL TIME (AET)' : 'FULL TIME') + '</span>';
    if (/POSTPONED|CANCELED/.test(g.name)) return '<span class="r">POSTPONED</span>';
    return '<span class="g">KICK-OFF IN </span><span class="w" id="cd">' + countdown(g.date) + '</span>';
  }
  function renderLeeds() {
    var g = S.main, show = g.state !== 'pre';
    var row = function (t) {
      var cls = t.id === TEAM ? 'y' : 'w';
      return '<div class="score dh"><span class="' + cls + '">' + esc(t.name.toUpperCase()) + '</span><span class="' + cls + '">' + (show ? t.score : '') + '</span></div>';
    };
    var ev = { home: [], away: [] };
    (g.raw.details || []).forEach(function (d) {
      var side = String((d.team || {}).id) === g.home.id ? 'home' : String((d.team || {}).id) === g.away.id ? 'away' : '';
      if (!side || !(d.scoringPlay || d.redCard)) return;
      var who = (d.athletesInvolved || [])[0] || {}, n = who.shortName || who.lastName || who.displayName || '';
      var min = (d.clock || {}).displayValue || '';
      ev[side].push(d.scoringPlay ? esc(n) + ' ' + esc(min) + (d.ownGoal ? ' og' : d.penaltyKick ? ' pen' : '')
                                  : '<span class="r">' + esc(n) + ' ' + esc(min) + ' (s/o)</span>');
    });
    var v = (g.raw.venue || {}).fullName || '';
    var evs = '';
    for (var i = 0; i < Math.max(ev.home.length, ev.away.length); i++)
      evs += '<div class="ev"><div class="c">' + (ev.home[i] || '') + '</div><div class="c a">' + (ev.away[i] || '') + '</div></div>';
    $('pg-leeds').innerHTML =
      '<div class="row c">' + esc(g.comp) + '</div>' +
      '<div class="row w">' + dayDate(g.date) + '  KO ' + hm(g.date) + '</div>' +
      '<div class="row"> </div>' + row(g.home) + row(g.away) + evs +
      '<div class="row"> </div><div class="row">' + statusLine(g) + '</div>' +
      (v ? '<div class="row w muted">' + esc(v.toUpperCase()) + '</div>' : '');
  }
  function renderOther() {
    var games = S.list.filter(function (g) { return g.id !== S.main.id; }).slice(0, 10);
    var head = S.listMode === 'today' ? 'TODAY' : S.listMode === 'next' ? 'NEXT FIXTURES' : 'OTHER GAMES';
    var sub = S.listMode === 'next' ? S.listLabel : S.listMode === 'today' ? dayDate(new Date()) : '';
    var html = '<div class="row c">' + esc(S.comp) + (sub ? '  <span class="w">' + esc(sub) + '</span>' : '') + '</div><div class="row"> </div><div class="list">';
    if (!games.length) html += '<div class="row w">No other games scheduled.</div>';
    games.forEach(function (g) {
      var mid, tail;
      if (g.state === 'pre') { mid = '<span class="s c">v</span>'; tail = '<span class="t w">' + (S.listMode === 'next' ? day(g.date) + ' ' : '') + hm(g.date) + '</span>'; }
      else { mid = '<span class="s y">' + g.home.score + '-' + g.away.score + '</span>';
             tail = g.state === 'in' ? '<span class="t live">' + esc(minute(g)) + '</span>' : '<span class="t c">FT</span>'; }
      html += '<div class="ln"><span class="h w">' + esc(g.home.name) + '</span>' + mid + '<span class="w">' + esc(g.away.name) + '</span>' + tail + '</div>';
    });
    $('pg-other').innerHTML = html + '</div>';
    return head;
  }
  function liveTable() {
    var rows = S.table.map(function (r) { return Object.assign({}, r); }), by = {}, playing = {};
    rows.forEach(function (r) { by[r.id] = r; });
    if (S.tableLeague === S.league) {
      var games = S.list.filter(function (g) { return g.state === 'in'; });
      if (S.main.state === 'in' && !games.some(function (g) { return g.id === S.main.id; })) games.push(S.main);
      games.forEach(function (g) {
        var H = by[g.home.id], A = by[g.away.id], hs = g.home.score, as = g.away.score;
        if (!H || !A) return;
        playing[H.id] = playing[A.id] = 1;
        H.p++; A.p++; H.gf += hs; H.ga += as; A.gf += as; A.ga += hs; H.gd += hs - as; A.gd += as - hs;
        if (hs > as) H.pts += 3; else if (hs < as) A.pts += 3; else { H.pts++; A.pts++; }
      });
      rows.sort(function (a, b) { return b.pts - a.pts || b.gd - a.gd || b.gf - a.gf || a.name.localeCompare(b.name); });
    }
    return { rows: rows, playing: playing, live: Object.keys(playing).length > 0 };
  }
  function renderTable(el, from, to, T) {
    var n = T.rows.length, z = S.tableLeague === 'eng.2' ? { u: [1, 2], e: [3, 6], r: [n - 2, n] } : { u: [1, 4], e: [5, 5], r: [n - 2, n] };
    var zone = function (p) { return p >= z.u[0] && p <= z.u[1] ? ' zu' : p >= z.e[0] && p <= z.e[1] ? ' ze' : p >= z.r[0] && p <= z.r[1] ? ' zr' : ''; };
    var html = '<div class="row c">' + (S.tableLeague === 'eng.2' ? 'CHAMPIONSHIP' : 'PREMIER LEAGUE') + '</div><div class="tbl"><div class="ln hd"><span class="n"></span><span>' + (T.live ? 'LIVE TABLE' : 'TEAM') + '</span><span class="p">P</span><span class="d">GD</span><span class="pt">PTS</span></div>';
    T.rows.slice(from, to).forEach(function (r, i) {
      var pos = from + i + 1, lv = T.playing[r.id];
      html += '<div class="ln' + zone(pos) + (r.id === TEAM ? ' leeds' : '') + '"><span class="n">' + pos + '</span><span>' + esc(r.name) + (lv ? ' <span class="live">*</span>' : '') +
        '</span><span class="p">' + r.p + '</span><span class="d">' + (r.gd > 0 ? '+' : '') + r.gd + '</span><span class="pt">' + r.pts + '</span></div>';
    });
    html += '</div>';
    if (T.live) html += '<div class="row small live" style="margin-top:.3em">* playing now</div>';
    el.innerHTML = html;
  }

  var PAGES = [], cur = 0, hold = false, timer = null;
  function render() {
    renderLeeds();
    var otherHead = renderOther();
    var T = liveTable(), half = Math.ceil(T.rows.length / 2);
    PAGES = [{ id: 'pg-leeds', title: S.main.state === 'in' ? 'LIVE' : S.main.state === 'post' ? 'LEEDS RESULT' : 'NEXT LEEDS MATCH' },
             { id: 'pg-other', title: otherHead === 'TODAY' ? 'TODAY’S SCORES' : otherHead }];
    if (T.rows.length) {
      renderTable($('pg-top'), 0, half, T); renderTable($('pg-bot'), half, T.rows.length, T);
      PAGES.push({ id: 'pg-top', title: 'TOP ' + half }, { id: 'pg-bot', title: 'BOTTOM ' + (T.rows.length - half) });
    }
    show(cur % PAGES.length);
  }
  function show(i) {
    cur = i;
    document.querySelectorAll('.page').forEach(function (p) { p.classList.remove('on'); });
    var P = PAGES[i];
    $(P.id).classList.add('on');
    $('title').textContent = P.title;
    fitTitle();
    $('sub').textContent = (i + 1) + '/' + PAGES.length;
  }
  function fitTitle() {   // shrink the double-height title on narrow screens so it never gets cut off
    var t = $('title'), f = 2.15;
    t.style.fontSize = '';
    while (t.scrollWidth > t.clientWidth && f > 1.2) { f -= 0.05; t.style.fontSize = f + 'em'; }
  }
  addEventListener('resize', fitTitle);
  function step() { if (PAGES.length) show((cur + 1) % PAGES.length); }
  function schedule() {
    clearTimeout(timer);
    if (hold) return;
    // linger a little longer on the Leeds page when the game is on
    var secs = PAGES[cur] && PAGES[cur].id === 'pg-leeds' && S.main && S.main.state === 'in' ? 20 : 12;
    timer = setTimeout(function () { step(); schedule(); }, secs * 1000);
  }
  $('next').addEventListener('click', function () { step(); schedule(); });
  $('hold').addEventListener('click', function () { hold = !hold; this.setAttribute('aria-pressed', hold); this.textContent = hold ? 'HELD' : 'HOLD'; schedule(); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); step(); schedule(); }
    if (e.key === 'ArrowLeft') { show((cur - 1 + PAGES.length) % PAGES.length); schedule(); }
  });

  /* ---------- clock + countdown ---------- */
  function tick() {
    var n = new Date();
    $('date').textContent = n.toLocaleDateString('en-GB', { timeZone: 'Europe/London', weekday: 'short', day: '2-digit', month: 'short' }).replace(/,/g, '');
    $('clock').textContent = n.toLocaleTimeString('en-GB', { timeZone: 'Europe/London' });
    var cd = $('cd');
    if (cd && S.main) cd.textContent = countdown(S.main.date);
  }
  setInterval(tick, 1000); tick();

  /* ---------- go ---------- */
  findMain().then(function (g) {
    if (!g) { $('pg-msg').innerHTML = '<div class="row r">NO SIGNAL</div><div class="row w">The fixture feed is down - try again later.</div>'; return; }
    S.main = g; S.league = g.lg; S.comp = g.comp;
    return refresh().then(function () {
      schedule();
      (function loop() {
        var anyLive = S.main.state === 'in' || S.list.some(function (x) { return x.state === 'in'; });
        var soon = S.main.state === 'pre' && S.main.date - Date.now() < 15 * 6e4;
        setTimeout(function () {
          // after full time, look for the next game again
          var p = S.main.state === 'post' && Date.now() - S.main.date > 4 * 36e5 ? findMain().then(function (n) { if (n) { S.main = n; S.league = n.lg; S.comp = n.comp; } }) : Promise.resolve();
          p.then(refresh).then(loop, loop);
        }, (anyLive || soon ? 30 : 300) * 1000);
      })();
    });
  });
})();
</script>
</body>
</html>
'''
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w').write(PAGE)
print('ceefax', len(PAGE) // 1024, 'KB')
