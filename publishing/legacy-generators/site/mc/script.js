function startCentre(CONFIG) {
  const $ = id => document.getElementById(id);
  const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;' }[c]));
  const pad = n => String(n).padStart(2, '0');
  const norm = s => (s || '').toLowerCase().replace(/\b(fc|afc)\b/g, '').replace(/&/g, 'and').replace(/[^a-z0-9]/g, '');
  const API = 'https://site.api.espn.com/apis';
  const kickoff = new Date(CONFIG.kickoff);
  const fotmob = id => `https://images.fotmob.com/image_resources/logo/teamlogo/${id}.png`;
  const logoOf = t => t?.logo || t?.logos?.[0]?.href || '';
  const matches = (team, wanted) => {
    const w = norm(wanted);
    return [team.displayName, team.shortDisplayName, team.name, team.location]
      .map(norm).filter(Boolean).some(n => n === w || n.includes(w) || w.includes(n));
  };

  // ---------- state ----------
  let main = null, mainFetchedAt = 0, mainId = '', mainTeamIds = {};
  let others = [], allLive = [], baseTable = [];
  let lineups = {
    home: { xi: CONFIG.home.xi.map(n => ({ name: n })), subs: CONFIG.home.subs.map(n => ({ name: n })) },
    away: { xi: CONFIG.away.xi.map(n => ({ name: n })), subs: CONFIG.away.subs.map(n => ({ name: n })) }
  };
  let pendingLineups = null;
  let facts = null;
  let lastMainScore = null;
  const lastScores = {}, flashIds = new Set();

  // ---------- static ----------
  if (CONFIG.transparentBackground) document.body.classList.add('transparent');
  document.documentElement.style.setProperty('--home', CONFIG.home.color);
  document.documentElement.style.setProperty('--away', CONFIG.away.color);
  $('comp').textContent = CONFIG.competition;
  $('home-name').textContent = CONFIG.home.name;
  $('away-name').textContent = CONFIG.away.name;
  $('venue').textContent = CONFIG.venue;
  $('meta').textContent = kickoff.toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long' }) +
    ' · KO ' + pad(kickoff.getHours()) + ':' + pad(kickoff.getMinutes());
  setBadge($('home-badge'), CONFIG.home.logo);
  setBadge($('away-badge'), CONFIG.away.logo);

  function setBadge(img, url, alt) {
    if (alt) img.dataset.alt = alt;
    img.onerror = () => { if (img.dataset.alt && img.src !== img.dataset.alt) img.src = img.dataset.alt; else img.style.visibility = 'hidden'; };
    if (url && !img.getAttribute('src')) img.src = url;
    else if (alt && img.style.visibility === 'hidden') { img.style.visibility = ''; img.src = alt; }
  }

  // ---------- data ----------
  async function getJSON(url) {
    const r = await fetch(url, { cache: 'no-store' });
    if (!r.ok) throw new Error(r.status);
    return r.json();
  }
  const ymd = d => d.getFullYear() + pad(d.getMonth() + 1) + pad(d.getDate());

  async function fetchScoreboard() {
    const data = await getJSON(`${API}/site/v2/sports/soccer/${CONFIG.league}/scoreboard?dates=${ymd(kickoff)}`);
    const all = (data.events || []).map(e => {
      const c = e.competitions[0];
      const h = c.competitors.find(x => x.homeAway === 'home');
      const a = c.competitors.find(x => x.homeAway === 'away');
      const st = c.status || e.status;
      return {
        id: e.id, date: new Date(e.date), raw: c,
        state: st.type.state, name: st.type.name, detail: st.type.shortDetail,
        clock: Number(st.clock) || 0, displayClock: st.displayClock, period: st.period || 0,
        home: { id: h.team.id, name: h.team.shortDisplayName || h.team.displayName, logo: logoOf(h.team), score: +h.score || 0, raw: h.team },
        away: { id: a.team.id, name: a.team.shortDisplayName || a.team.displayName, logo: logoOf(a.team), score: +a.score || 0, raw: a.team }
      };
    });
    allLive = all.filter(g => g.state === 'in');
    const m = all.find(g => g.id === CONFIG.eventId) || all.find(g => g.home.id === CONFIG.home.id && g.away.id === CONFIG.away.id);
    if (m) {
      main = m; mainFetchedAt = Date.now(); mainId = m.id;
      mainTeamIds = { [m.home.id]: 'home', [m.away.id]: 'away' };
      setBadge($('home-badge'), null, m.home.logo);
      setBadge($('away-badge'), null, m.away.logo);
    }
    others = all.filter(g => g !== m);
    for (const g of others) {
      const k = g.home.score + '-' + g.away.score;
      if (lastScores[g.id] && lastScores[g.id] !== k) flashIds.add(g.id);
      lastScores[g.id] = k;
    }
  }

  async function fetchTable() {
    const data = await getJSON(`${API}/v2/sports/soccer/${CONFIG.league}/standings`);
    const entries = data.children?.[0]?.standings?.entries || data.standings?.entries || [];
    const stat = (e, n) => +(e.stats.find(s => s.name === n || s.type === n)?.value || 0);
    baseTable = entries.map(e => ({
      id: e.team.id, name: e.team.shortDisplayName || e.team.displayName, logo: logoOf(e.team),
      p: stat(e, 'gamesPlayed'), gf: stat(e, 'pointsFor'), ga: stat(e, 'pointsAgainst'),
      gd: stat(e, 'pointDifferential'), pts: stat(e, 'points'), rank: stat(e, 'rank')
    })).sort((a, b) => a.rank - b.rank);
  }

  async function fetchLineups() {
    if (!mainId) return;
    const data = await getJSON(`${API}/site/v2/sports/soccer/${CONFIG.league}/summary?event=${mainId}`);
    const fx = {};
    for (const t of data.boxscore?.teams || []) {
      const side = mainTeamIds[t.team?.id];
      if (!side) continue;
      fx[side] = Object.fromEntries((t.statistics || []).map(x => [x.name, +x.displayValue || 0]));
    }
    if (fx.home && fx.away) facts = fx;
    const out = {};
    for (const r of data.rosters || []) {
      if (!r.homeAway || !r.roster?.length) continue;
      const toP = p => ({
        name: (p.athlete?.lastName || p.athlete?.displayName || '') + (p.captain ? ' (C)' : ''),
        num: p.jersey, id: String(p.athlete?.id || ''),
        tag: p.subbedIn ? 'in' : p.subbedOut ? 'out' : '',
        subMin: (p.plays || []).find(pl => pl.substitution)?.clock?.displayValue || ''
      });
      out[r.homeAway] = { xi: r.roster.filter(p => p.starter).map(toP), subs: r.roster.filter(p => !p.starter).map(toP) };
    }
    if (out.home?.xi.length === 11 && out.away?.xi.length === 11 &&
        JSON.stringify(out) !== JSON.stringify(lineups)) pendingLineups = out;
  }

  // ---------- main fixture ----------
  function renderMain() {
    const now = Date.now();
    const pill = $('pill'), scoreEl = $('score');
    let text = '', isLive = false, added = '', showScore = false, hs = 0, as = 0;

    if (main && main.state !== 'pre') {
      showScore = true; hs = main.home.score; as = main.away.score;
      if (main.state === 'post') text = /PEN/.test(main.name) ? 'FULL TIME (PENS)' : /AET/.test(main.name) ? 'AFTER EXTRA TIME' : 'FULL TIME';
      else if (/HALFTIME/.test(main.name)) text = 'HALF TIME';
      else if (/POSTPONED|CANCEL|SUSPEND|DELAY/.test(main.name)) text = main.detail || 'POSTPONED';
      else {
        isLive = true;
        let secs = main.clock + Math.floor((now - mainFetchedAt) / 1000);
        const cap = { 1: 2700, 2: 5400, 3: 6300, 4: 7200 }[main.period];
        if (cap && secs > cap) { added = '+' + Math.ceil((secs - cap) / 60); secs = cap; }
        text = pad(Math.floor(secs / 60)) + ':' + pad(secs % 60);
      }
    } else {
      const diff = Math.floor((kickoff - now) / 1000);
      if (diff > 0) {
        const d = Math.floor(diff / 86400), h = Math.floor(diff % 86400 / 3600), m = Math.floor(diff % 3600 / 60), s = diff % 60;
        text = 'KICK-OFF IN ' + (d ? d + 'D ' : '') + pad(h) + ':' + pad(m) + ':' + pad(s);
      } else text = 'KICK-OFF';
    }

    scoreEl.classList.toggle('pre', !showScore);
    $('dash').textContent = showScore ? '-' : 'V';
    $('home-score').textContent = hs;
    $('away-score').textContent = as;
    $('pill-text').textContent = text;
    pill.classList.toggle('live', isLive);
    $('added').textContent = added;
    $('added').classList.toggle('show', !!added);

    const key = hs + '-' + as;
    if (showScore && lastMainScore !== null && key !== lastMainScore) {
      scoreEl.classList.remove('flash'); void scoreEl.offsetWidth; scoreEl.classList.add('flash');
    }
    if (showScore) lastMainScore = key;
    if (window.onCentre) window.onCentre({ text, hs, as, showScore, isLive });
  }

  function renderEvents() {
    const cols = { home: [], away: [] };
    for (const d of main?.raw?.details || []) {
      const side = mainTeamIds[d.team?.id];
      if (!side) continue;
      const who = d.athletesInvolved?.[0];
      const name = who?.shortName || who?.displayName || '';
      const min = d.clock?.displayValue || '';
      let icon = '', note = '';
      if (d.scoringPlay) { icon = '<span class="ball"></span>'; note = d.ownGoal ? 'OG' : d.penaltyKick ? 'PEN' : ''; }
      else if (d.redCard) icon = '<span class="card r"></span>';
      else if (d.yellowCard) icon = '<span class="card y"></span>';
      else continue;
      const inner = `${icon}<span>${esc(name)}</span>${note ? `<span class="note">(${note})</span>` : ''}<span class="min">${esc(min)}</span>`;
      cols[side].push(`<span class="ev">${inner}</span>`);
    }
    $('home-events').innerHTML = cols.home.join('');
    $('away-events').innerHTML = cols.away.join('');
  }

  // ---------- right column ----------
  let scorePage = 0;
  function renderScores() {
    if (!others.length) { $('scores').innerHTML = '<div class="empty">No other games today</div>'; $('scores-sub').textContent = ''; return; }
    const per = CONFIG.maxScoresShown, pages = Math.ceil(others.length / per);
    if (scorePage >= pages) scorePage = 0;
    const list = others.slice(scorePage * per, scorePage * per + per);
    $('scores-sub').textContent = pages > 1 ? `${scorePage + 1}/${pages}` : (allLive.length ? `${allLive.length} LIVE` : '');
    $('scores').innerHTML = list.map(g => {
      let s, st = '', live = false;
      if (g.state === 'pre') s = `<span class="s pre">${pad(g.date.getHours())}:${pad(g.date.getMinutes())}</span>`;
      else {
        s = `<span class="s">${g.home.score} - ${g.away.score}</span>`;
        if (g.state === 'post') st = 'FT';
        else if (/HALFTIME/.test(g.name)) st = 'HT';
        else if (/POSTPONED|CANCEL/.test(g.name)) { st = ''; s = '<span class="s pre">P-P</span>'; }
        else { st = g.displayClock || g.detail; live = true; }
      }
      return `<div class="g${flashIds.has(g.id) ? ' flash' : ''}">
        <div class="t h"><span>${esc(g.home.name)}</span><img src="${esc(g.home.logo)}" onerror="this.style.visibility='hidden'"></div>
        ${s}
        <div class="t"><img src="${esc(g.away.logo)}" onerror="this.style.visibility='hidden'"><span>${esc(g.away.name)}</span></div>
        <div class="st${live ? ' live' : ''}">${esc(st)}</div></div>`;
    }).join('');
    flashIds.clear();
  }

  function renderTable() {
    if (!baseTable.length) { $('table').innerHTML = '<div class="empty">Table loading…</div>'; return; }
    const rows = baseTable.map(r => ({ ...r }));
    const byId = Object.fromEntries(rows.map(r => [r.id, r]));
    const playing = new Set();
    for (const g of allLive) {
      const H = byId[g.home.id], A = byId[g.away.id];
      if (!H || !A) continue;
      playing.add(H.id); playing.add(A.id);
      const hs = g.home.score, as = g.away.score;
      H.p++; A.p++; H.gf += hs; H.ga += as; A.gf += as; A.ga += hs; H.gd += hs - as; A.gd += as - hs;
      if (hs > as) H.pts += 3; else if (hs < as) A.pts += 3; else { H.pts++; A.pts++; }
    }
    rows.sort((a, b) => b.pts - a.pts || b.gd - a.gd || b.gf - a.gf || a.name.localeCompare(b.name));
    if (!showingFacts) $('table-title').textContent = allLive.length ? 'Live Table' : 'Table';
    const z = CONFIG.zones;
    const zone = n => n >= z.ucl[0] && n <= z.ucl[1] ? 'ucl' : n >= z.uel[0] && n <= z.uel[1] ? 'uel' : n >= z.rel[0] && n <= z.rel[1] ? 'rel' : '';
    $('table').innerHTML = `<div class="tr hd"><span class="n">#</span><span></span><span>TEAM</span><span class="num">P</span><span class="num">GD</span><span class="pts">PTS</span></div>` +
      rows.map((r, i) => {
        const pos = i + 1;
        const mv = pos < r.rank ? '<span class="mv up">▲</span>' : pos > r.rank ? '<span class="mv down">▼</span>' : '';
        const focus = mainTeamIds[r.id] ? ' focus' : '';
        return `<div class="tr ${zone(pos)}${playing.has(r.id) ? ' playing' : ''}${focus}">
          <span class="n">${pos}</span><img src="${esc(r.logo)}" onerror="this.style.visibility='hidden'">
          <span class="nm"><span>${esc(r.name)}</span>${playing.has(r.id) ? '<i class="ld"></i>' : ''}${mv}</span>
          <span class="num">${r.p}</span><span class="num">${r.gd > 0 ? '+' : ''}${r.gd}</span><span class="pts">${r.pts}</span></div>`;
      }).join('');
  }

  // ---------- match facts ----------
  function renderFacts() {
    if (!facts) { $('facts').innerHTML = ''; return; }
    const H = facts.home, A = facts.away, M = CONFIG.manualStats;
    const pass = s => s.accuratePasses ? `${s.accuratePasses} <small>${Math.round(100 * s.accuratePasses / (s.totalPasses || s.accuratePasses))}%</small>` : '0';
    const rows = [
      ['Expected goals (xG)', M.xg[0], M.xg[1]],
      ['Total shots', H.totalShots, A.totalShots],
      ['Shots on target', H.shotsOnTarget, A.shotsOnTarget],
      ['Touches in opp. box', M.touchesOppBox[0], M.touchesOppBox[1]],
      ['Big chances', M.bigChances[0], M.bigChances[1]],
      ['Big chances missed', M.bigChancesMissed[0], M.bigChancesMissed[1]],
      ['Accurate passes', pass(H), pass(A), H.accuratePasses, A.accuratePasses],
      ['Yellow cards', H.yellowCards, A.yellowCards],
      ['Red cards', H.redCards, A.redCards],
      ['Corners', H.wonCorners, A.wonCorners]
    ].filter(r => r[1] !== '' && r[1] != null && r[2] !== '' && r[2] != null);
    const ph = Math.round(H.possessionPct || 50), pa = 100 - ph;
    const lead = (a, b, lowerBetter) => a === b ? ['', ''] : (a > b) !== !!lowerBetter ? [' lead', ''] : ['', ' lead'];
    $('facts').innerHTML = `
      <div class="fx-teams">
        <span><img src="${esc(CONFIG.home.logo)}" onerror="this.style.display='none'">${esc(CONFIG.home.name)}</span>
        <span>${esc(CONFIG.away.name)}<img src="${esc(CONFIG.away.logo)}" onerror="this.style.display='none'"></span>
      </div>
      <div class="fx-poss"><div class="lbl">BALL POSSESSION</div>
        <div class="bar"><div class="h" style="width:${ph}%">${ph}%</div><div class="a" style="width:${pa}%">${pa}%</div></div></div>` +
      rows.map(([label, hv, av, hn, an]) => {
        const h = +(hn ?? parseFloat(hv)) || 0, a = +(an ?? parseFloat(av)) || 0;
        const tot = h + a || 1;
        const [lh, la] = lead(h, a, /card/i.test(label));
        return `<div class="fx-row"><span class="v${lh}">${/<small>/.test(hv) ? hv : esc(hv)}</span>
          <div class="mid"><span class="lab">${esc(label)}</span>
            <div class="bars"><i><b style="width:${100 * h / tot}%"></b></i><i><b style="width:${100 * a / tot}%"></b></i></div></div>
          <span class="v a${la}">${/<small>/.test(av) ? av : esc(av)}</span></div>`;
      }).join('');
  }

  let showingFacts = false;
  function rotateRight() {
    showingFacts = facts ? !showingFacts : false;
    $('table').classList.toggle('on', !showingFacts);
    $('facts').classList.toggle('on', showingFacts);
    $('table-title').textContent = showingFacts ? 'Match Facts' : (allLive.length ? 'Live Table' : 'Table');
    $('table-sub').textContent = showingFacts ? `${CONFIG.home.name} v ${CONFIG.away.name}` : 'P · GD · PTS';
    setTimeout(rotateRight, (showingFacts ? CONFIG.factsSecs : CONFIG.tableSecs) * 1000);
  }

  // ---------- ticker ----------
  const track = $('tk-track');
  let anim = null;
  // goals & cards for a player, matched by ESPN id or surname
  const surname = s => norm(String(s || '').replace(/\(C\)/i, '').trim().split(/\s+/).pop());
  function playerBadges(p) {
    let h = '';
    for (const d of main?.raw?.details || []) {
      const who = d.athletesInvolved?.[0];
      if (!who) continue;
      const same = (p.id && who.id) ? String(who.id) === p.id
                 : surname(who.lastName || who.shortName || who.displayName) === surname(p.name);
      if (!same) continue;
      let icon = '', note = '';
      if (d.scoringPlay) { icon = '<i class="tk-ball"></i>'; note = d.ownGoal ? ' OG' : d.penaltyKick ? ' PEN' : ''; }
      else if (d.redCard) icon = '<i class="tk-card r"></i>';
      else if (d.yellowCard) icon = '<i class="tk-card y"></i>';
      else continue;
      h += `<span class="tk-ev">${icon}<b>${esc(d.clock?.displayValue || '')}${note}</b></span>`;
    }
    if (p.tag === 'in') h += `<span class="tk-tag tk-in">▲ ON${p.subMin ? ' ' + esc(p.subMin) : ''}</span>`;
    if (p.tag === 'out') h += `<span class="tk-tag tk-out">▼ OFF${p.subMin ? ' ' + esc(p.subMin) : ''}</span>`;
    return h;
  }
  function tickerBlock(team, side, which, label) {
    const list = lineups[side][which];
    if (!list.length) return '';
    let html = `<span class="tk-team" style="--c:${team.color}"><img src="${esc(team.logo)}" onerror="this.style.display='none'">${esc(team.name)} <small>${label}</small></span>`;
    for (const p of list) {
      html += `<span class="tk-p" style="--c:${team.color}">${p.num ? `<span class="tk-num">${esc(p.num)}</span>` : ''}${esc(p.name)}${playerBadges(p)}</span>`;
    }
    return html;
  }
  function runTicker() {
    if (pendingLineups) { lineups = pendingLineups; pendingLineups = null; }
    track.innerHTML =
      tickerBlock(CONFIG.home, 'home', 'xi', 'STARTING XI') + tickerBlock(CONFIG.home, 'home', 'subs', 'SUBS') +
      tickerBlock(CONFIG.away, 'away', 'xi', 'STARTING XI') + tickerBlock(CONFIG.away, 'away', 'subs', 'SUBS');
    if (!track.innerHTML.trim()) track.innerHTML =
      `<span class="tk-p" style="color:#9aa4b2">${esc(CONFIG.home.name)} v ${esc(CONFIG.away.name)} · LINE-UPS EXPECTED ABOUT AN HOUR BEFORE KICK-OFF</span>`;
    const start = track.parentElement.offsetWidth, w = track.scrollWidth;
    if (anim) anim.cancel();
    anim = track.animate([{ transform: `translateX(${start}px)` }, { transform: `translateX(${-w}px)` }],
      { duration: (start + w) / CONFIG.tickerSpeed * 1000, easing: 'linear' });
    anim.onfinish = runTicker;
  }

  // ---------- loops ----------
  async function poll() {
    await Promise.allSettled([fetchScoreboard(), fetchTable()]);
    await fetchLineups().catch(() => {});
    renderEvents(); renderScores(); renderTable(); renderFacts();
  }
  setInterval(renderMain, 1000);
  setTimeout(rotateRight, CONFIG.tableSecs * 1000);
  setInterval(() => { scorePage++; renderScores(); }, 10000);
  renderMain();
  poll();
  setInterval(poll, CONFIG.pollSeconds * 1000);
  (document.fonts ? document.fonts.ready : Promise.resolve()).then(runTicker);
}
