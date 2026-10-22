import sys, re, json, subprocess, os
sys.path.insert(0, '/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad')
from leeds_scene import scene
from shelves import SHELF_OF_JS
fav = open('/home/claude/favicon.svg').read()
globe = re.search(r'<path fill="#f7f7f2" fill-rule="evenodd" d="([^"]+)"', fav).group(1)
svg, _ = scene()
GC = json.loads(subprocess.run(['node', '-e', "global.window={};require('/home/claude/site/travel-guides/guides.js');process.stdout.write(JSON.stringify(window.GUIDES.map(g=>g.city)))"], capture_output=True, text=True).stdout)

PAGE = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Leeds United Match Hub - Rob Callery</title>
<meta name="description" content="Rob Callery's Leeds United match hub: next match, live score, results, fixtures and the table, from a seat at Elland Road.">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
  :root{--navy:#0a1838;--blue:#1e3f9a;--yellow:#ffcd00;--cream:#f7f2e4;--ink:#16203a}
  *{box-sizing:border-box;margin:0;padding:0}
  html,body{height:100%}
  body{min-height:100vh;min-height:100dvh;background:#0b0f1a;color:var(--cream);font-family:Inter,system-ui,sans-serif;overflow-x:hidden}
  a{color:inherit}
  .scene{position:fixed;inset:0;z-index:0}
  .scene svg{width:100%;height:100%;display:block}
  header{position:relative;z-index:3;display:flex;align-items:center;justify-content:space-between;gap:16px;padding:14px clamp(16px,3vw,40px)}
  .brand{display:flex;align-items:center;gap:10px;text-decoration:none;font-family:"Bebas Neue",Impact,sans-serif;font-size:1.6rem;letter-spacing:.06em;white-space:nowrap;text-shadow:0 2px 6px rgba(0,0,0,.6)}
  .brand svg{width:38px;height:38px}
  .back{font-size:.92rem;font-weight:600;text-decoration:none;padding:.45em .9em;border:1.5px solid rgba(247,242,228,.55);border-radius:999px;white-space:nowrap;background:rgba(10,24,56,.55);backdrop-filter:blur(4px)}
  .back:hover,.back:focus-visible{border-color:var(--yellow)}
  .sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
  main{position:relative;z-index:2;min-height:calc(100vh - 70px);min-height:calc(100dvh - 70px);display:flex;flex-direction:column;justify-content:flex-end;padding:0 clamp(12px,2.5vw,36px) clamp(12px,2vh,24px)}
  .boards{display:grid;grid-template-columns:1.15fr 1fr 1fr 1.2fr;gap:clamp(10px,1.2vw,18px);align-items:end}
  .card{background:rgba(247,242,228,.96);color:var(--ink);border-radius:10px;overflow:hidden;box-shadow:0 14px 30px rgba(0,0,0,.45);max-height:min(36vh,330px);display:flex;flex-direction:column}
  .card h2{font-family:"Bebas Neue",Impact,sans-serif;font-weight:400;font-size:1.25rem;letter-spacing:.1em;background:var(--blue);color:#fff;padding:.35em .8em .25em;display:flex;justify-content:space-between;align-items:center;flex:none}
  .card h2 small{font-family:Inter,sans-serif;font-size:.62rem;letter-spacing:.08em;color:var(--yellow);font-weight:700}
  .card .in{padding:.6em .8em .7em;overflow:auto;font-size:.86rem}
  .next .vs{font-family:"Bebas Neue",Impact,sans-serif;font-size:clamp(1.5rem,2.2vw,2rem);line-height:1;color:var(--navy);margin:.1em 0 .2em}
  .next .vs i{font-style:normal;color:#8a7a58;font-size:.6em;vertical-align:.25em;margin:0 .25em}
  .next .meta{color:#4a5570;font-size:.82rem;line-height:1.45}
  .next .cd{display:flex;gap:6px;margin:.55em 0 .3em}
  .next .cd span{background:var(--navy);color:var(--yellow);font-family:"Space Mono",monospace;font-weight:700;font-size:1.05rem;border-radius:6px;padding:.2em .45em;min-width:2.6em;text-align:center;line-height:1.1}
  .next .cd span small{display:block;font-size:.55rem;color:#c9d2ec;font-weight:400;letter-spacing:.08em}
  .next .live{display:inline-block;background:#d22630;color:#fff;font-weight:700;font-size:.72rem;letter-spacing:.1em;padding:.15em .5em;border-radius:4px;animation:blink 1.2s steps(2) infinite}
  .next a.pub{display:inline-block;margin-top:.45em;font-weight:700;font-size:.8rem;color:var(--blue)}
  @keyframes blink{50%{opacity:.35}}
  ul.list{list-style:none}
  ul.list li{display:grid;grid-template-columns:auto 1fr auto;gap:.6em;align-items:center;padding:.32em 0;border-bottom:1px dashed #d8cfb8}
  ul.list li:last-child{border-bottom:0}
  .res{width:1.6em;height:1.6em;border-radius:50%;display:grid;place-items:center;font-weight:700;font-size:.72rem;color:#fff}
  .W{background:#1f8a43}.D{background:#8a8f99}.L{background:#c0392b}
  .when{font-family:"Space Mono",monospace;font-size:.72rem;color:#6a6250;white-space:nowrap}
  .sc{font-family:"Space Mono",monospace;font-weight:700;white-space:nowrap}
  .ha{font-size:.62rem;font-weight:700;color:#fff;background:var(--navy);border-radius:3px;padding:.1em .35em;margin-right:.3em}
  table{width:100%;border-collapse:collapse;font-size:.8rem}
  th{font-size:.62rem;letter-spacing:.08em;color:#8a7a58;text-align:right;font-weight:700;padding:0 .3em .3em}
  th:nth-child(2){text-align:left}
  td{padding:.26em .3em;text-align:right;border-bottom:1px solid #e6dcc4;font-variant-numeric:tabular-nums}
  td:nth-child(2){text-align:left;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:9em}
  tr.me td{background:var(--yellow);font-weight:700}
  .empty{color:#6a6250;font-style:italic}
  .note{font-size:.7rem;color:#c9d2ec;text-align:right;margin-top:6px;text-shadow:0 1px 3px #000}
  @media (max-width:1100px){.boards{grid-template-columns:1fr 1fr}.card{max-height:none}}
  @media (max-width:760px),(max-aspect-ratio:1/1){
    .scene{position:relative;height:62vh;min-height:300px}
    .scene svg{position:absolute;inset:0}
    header{position:absolute;top:0;left:0;right:0}
    main{min-height:0;padding-top:12px;background:#0b0f1a}
    .boards{grid-template-columns:1fr}
    .brand{font-size:1.3rem}.brand svg{width:30px;height:30px}.back{font-size:.8rem}
  }
  @media (prefers-reduced-motion:reduce){.next .live{animation:none}}
</style>
</head>
<body>
<div class="scene" aria-hidden="true"><svg viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice">__SVG__</svg></div>
<header>
  <a class="brand" href="/"><svg viewBox="190 157 700 700" aria-hidden="true"><circle cx="540" cy="507" r="345" fill="#f7f2e4"/><path fill="#0a1838" fill-rule="evenodd" d="__GLOBE__"/></svg>Rob Callery</a>
  <a class="back" href="/match-hub/">← Back to the pub</a>
</header>
<main>
  <h1 class="sr">Leeds United Match Hub</h1>
  <div class="boards">
    <section class="card next" aria-labelledby="hNext"><h2 id="hNext">Next match <small id="nextComp"></small></h2><div class="in" id="next"><p class="empty">Checking the fixture list…</p></div></section>
    <section class="card" aria-labelledby="hRes"><h2 id="hRes">Last results</h2><div class="in"><ul class="list" id="results"><li class="empty">Loading…</li></ul></div></section>
    <section class="card" aria-labelledby="hFix"><h2 id="hFix">Coming up</h2><div class="in"><ul class="list" id="fixtures"><li class="empty">Loading…</li></ul></div></section>
    <section class="card" aria-labelledby="hTab"><h2 id="hTab">The table <small id="tabName"></small></h2><div class="in"><table id="table" aria-describedby="hTab"><thead><tr><th>#</th><th>Team</th><th>P</th><th>GD</th><th>Pts</th></tr></thead><tbody><tr><td colspan="5" class="empty">Loading…</td></tr></tbody></table></div></section>
  </div>
  <p class="note">Scores from ESPN · times are UK time · refreshes every minute on matchday</p>
</main>
<script>
(function(){
  var TEAM='357', LEAGUES=['eng.1','eng.2','eng.fa','eng.league_cup'], TABLE_LEAGUES=['eng.1','eng.2'];
  var GUIDES=__GUIDES__;
  var API='https://site.api.espn.com/apis/site/v2/sports/soccer/';
  function $(id){return document.getElementById(id)}
  function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
  function get(u){return fetch(u).then(function(r){return r.ok?r.json():null}).catch(function(){return null})}
  function uk(d,o){try{return new Intl.DateTimeFormat('en-GB',Object.assign({timeZone:'Europe/London'},o)).format(d)}catch(e){return d.toDateString()}}
  function score(c){var s=c&&c.score;if(s==null)return null;if(typeof s==='object')s=s.displayValue!=null?s.displayValue:s.value;return s===''?null:s}
  function short(n){return (n||'').replace(' United',' Utd').replace('Manchester','Man').replace('Wolverhampton Wanderers','Wolves').replace('Brighton & Hove Albion','Brighton').replace('Tottenham Hotspur','Spurs').replace('Nottingham Forest',"Nott'm Forest")}
  function norm(e,lgName){
    var c=(e.competitions||[])[0]||{},cs=c.competitors||[],us=null,them=null;
    cs.forEach(function(t){var id=(t.team||{}).id||t.id;if(String(id)===TEAM)us=t;else them=t});
    if(!us||!them)return null;
    var st=(c.status||e.status||{}),ty=st.type||{},v=c.venue||{},ad=v.address||{};
    return {id:e.id,date:new Date(e.date),home:us.homeAway==='home',opp:(them.team||{}).displayName||(them.team||{}).name||'',
      us:score(us),them:score(them),state:ty.state||'pre',done:!!ty.completed,detail:ty.shortDetail||'',clock:st.displayClock||'',
      comp:lgName||((e.season||{}).displayName)||'',venue:v.fullName||'',city:ad.city||''};
  }
  var events={},tableData=null,timer=null;
  function add(list,lg){(list||[]).forEach(function(e){var n=norm(e,lg);if(n)events[n.id]=Object.assign(events[n.id]||{},n)})}
  function compName(d,lg){return ((d&&d.leagues&&d.leagues[0])||{}).name||({'eng.1':'Premier League','eng.2':'Championship','eng.fa':'FA Cup','eng.league_cup':'Carabao Cup'})[lg]||''}
  function loadAll(){
    var jobs=[];
    LEAGUES.forEach(function(lg){
      jobs.push(get(API+lg+'/teams/'+TEAM+'/schedule').then(function(d){if(d)add(d.events,compName(d,lg))}));
      jobs.push(get(API+lg+'/teams/'+TEAM+'/schedule?fixture=true').then(function(d){if(d)add(d.events,compName(d,lg))}));
      jobs.push(get(API+lg+'/scoreboard').then(function(d){if(d)add(d.events,compName(d,lg))}));
    });
    return Promise.all(jobs);
  }
  function loadTable(){
    var i=0;
    function next(){if(i>=TABLE_LEAGUES.length)return Promise.resolve(null);var lg=TABLE_LEAGUES[i++];
      return get('https://site.api.espn.com/apis/v2/sports/soccer/'+lg+'/standings').then(function(d){
        var ch=d&&d.children&&d.children[0],en=ch&&ch.standings&&ch.standings.entries;
        if(en&&en.some(function(x){return String((x.team||{}).id)===TEAM}))return {name:ch.name||d.name||'',entries:en};
        return next()})}
    return next();
  }
  function stat(x,n){var s=(x.stats||[]).filter(function(t){return t.name===n})[0];return s?(s.displayValue!=null?s.displayValue:s.value):''}
  function guideFor(city){var ps=(city||'').split(',').map(function(s){return s.trim()});for(var i=0;i<ps.length;i++)if(GUIDES.indexOf(ps[i])>=0)return ps[i];return null}
  function line(m){return (m.home?'Leeds':short(m.opp))+'  v  '+(m.home?short(m.opp):'Leeds')}
  function setScreen(head,main,sub,foot){$('bsHead').textContent=head;$('bsMain').textContent=main;$('bsSub').textContent=sub;$('bsFoot').textContent=foot||' '}
  var LED=['MARCHING ON TOGETHER','ALL LEEDS AREN\\'T WE','SIDE BEFORE SELF EVERY TIME','FOLLOW @CALZ88','ONE BEER AT A TIME'],ledI=0;
  function render(){
    var all=Object.keys(events).map(function(k){return events[k]}).sort(function(a,b){return a.date-b.date});
    var now=new Date();
    var live=all.filter(function(m){return m.state==='in'})[0];
    var past=all.filter(function(m){return m.state==='post'||m.done}).slice(-5).reverse();
    var up=all.filter(function(m){return m.state==='pre'&&m.date>new Date(now-3*36e5)});
    var nx=live||up[0];
    // next match card
    if(!all.length){$('next').innerHTML='<p class="empty">The feed is down - try again later.</p>';setScreen('ELLAND ROAD','LEEDS UNITED','MARCHING ON TOGETHER');}
    else if(nx){
      $('nextComp').textContent=(nx.comp||'').toUpperCase();
      var g=guideFor(nx.city),h='<div class="vs">'+esc(line(nx)).replace('  v  ','<i>v</i>')+'</div>';
      if(live){h+='<span class="live">LIVE</span> <b class="sc" style="font-size:1.3rem;margin-left:.3em">'+esc(nx.home?(nx.us||0)+' - '+(nx.them||0):(nx.them||0)+' - '+(nx.us||0))+'</b> <span class="when">'+esc(nx.clock||nx.detail)+'</span>'}
      else{h+='<div class="cd" id="cd"></div>'}
      h+='<p class="meta">'+esc(uk(nx.date,{weekday:'long',day:'numeric',month:'long'}))+' · '+esc(uk(nx.date,{hour:'2-digit',minute:'2-digit'}))+' UK<br>'+esc(nx.venue+(nx.city?', '+nx.city:''))+'</p>';
      if(!nx.home&&g)h+='<a class="pub" href="/travel-guides/?city='+encodeURIComponent(g)+'">Away day? Our pint guide to '+esc(g)+' →</a>';
      else if(nx.home)h+='<a class="pub" href="/travel-guides/?city=Leeds">Pre-match pints in Leeds →</a>';
      $('next').innerHTML=h;
      if(live)setScreen('LIVE · '+(nx.clock||nx.detail),(nx.home?'LEEDS '+(nx.us||0)+'-'+(nx.them||0)+' '+short(nx.opp):short(nx.opp)+' '+(nx.them||0)+'-'+(nx.us||0)+' LEEDS').toUpperCase(),'MARCHING ON TOGETHER',nx.comp);
      else setScreen('NEXT UP',line(nx).replace('  v  ',' v ').toUpperCase(),uk(nx.date,{weekday:'short',day:'numeric',month:'short'}).toUpperCase()+' · '+uk(nx.date,{hour:'2-digit',minute:'2-digit'}),nx.comp);
      tick();
    } else {$('next').innerHTML='<p class="empty">No fixtures announced yet.</p>';setScreen('ELLAND ROAD','LEEDS UNITED','MARCHING ON TOGETHER')}
    // results
    $('results').innerHTML=past.length?past.map(function(m){var u=+m.us,t=+m.them,r=u>t?'W':u<t?'L':'D';
      return '<li><span class="res '+r+'">'+r+'</span><span><span class="ha">'+(m.home?'H':'A')+'</span>'+esc(short(m.opp))+'</span><span class="sc">'+esc(m.us)+'-'+esc(m.them)+'</span></li>'}).join(''):'<li class="empty">No results yet this season.</li>';
    // fixtures
    var fx=up.filter(function(m){return m!==nx}).slice(0,5);
    $('fixtures').innerHTML=fx.length?fx.map(function(m){
      return '<li><span class="when">'+esc(uk(m.date,{day:'2-digit',month:'short'}))+'</span><span><span class="ha">'+(m.home?'H':'A')+'</span>'+esc(short(m.opp))+'</span><span class="when">'+esc(uk(m.date,{hour:'2-digit',minute:'2-digit'}))+'</span></li>'}).join(''):'<li class="empty">Nothing else announced yet.</li>';
    // led messages
    LED=['MARCHING ON TOGETHER','ALL LEEDS AREN\\'T WE','SIDE BEFORE SELF EVERY TIME','FOLLOW @CALZ88'];
    if(nx&&!live)LED.unshift('NEXT: '+line(nx).replace('  v  ',' V ').toUpperCase());
    if(past[0])LED.push('LAST TIME: '+(past[0].home?'LEEDS '+past[0].us+'-'+past[0].them+' '+short(past[0].opp):short(past[0].opp)+' '+past[0].them+'-'+past[0].us+' LEEDS').toUpperCase());
    clearTimeout(timer);if(live)timer=setTimeout(refresh,60000);
  }
  function renderTable(t){
    var tb=$('table').querySelector('tbody');
    if(!t){tb.innerHTML='<tr><td colspan="5" class="empty">Table unavailable right now.</td></tr>';return}
    $('tabName').textContent=(t.name||'').toUpperCase();
    var en=t.entries.slice().sort(function(a,b){return (+stat(a,'rank')||99)-(+stat(b,'rank')||99)});
    var me=en.findIndex(function(x){return String((x.team||{}).id)===TEAM}),from=Math.max(0,Math.min(me-3,en.length-7));
    tb.innerHTML=en.slice(from,from+7).map(function(x,i){var gd=stat(x,'pointDifferential');gd=(+gd>0?'+':'')+gd;
      return '<tr'+(from+i===me?' class="me"':'')+'><td>'+esc(stat(x,'rank')||from+i+1)+'</td><td>'+esc(short((x.team||{}).displayName||(x.team||{}).name))+'</td><td>'+esc(stat(x,'gamesPlayed'))+'</td><td>'+esc(gd)+'</td><td><b>'+esc(stat(x,'points'))+'</b></td></tr>'}).join('');
  }
  function tick(){var el=$('cd');if(!el)return;var all=Object.keys(events).map(function(k){return events[k]}).filter(function(m){return m.state==='pre'&&m.date>new Date()}).sort(function(a,b){return a.date-b.date});
    if(!all[0]){el.innerHTML='';return}var s=Math.max(0,Math.floor((all[0].date-new Date())/1000)),d=Math.floor(s/86400),h=Math.floor(s%86400/3600),m=Math.floor(s%3600/60),x=s%60;
    function p(n){return (n<10?'0':'')+n}
    el.innerHTML='<span>'+d+'<small>DAYS</small></span><span>'+p(h)+'<small>HRS</small></span><span>'+p(m)+'<small>MINS</small></span><span>'+p(x)+'<small>SECS</small></span>'}
  setInterval(tick,1000);
  var led=$('ledText');setInterval(function(){ledI=(ledI+1)%LED.length;led.style.opacity=0;setTimeout(function(){led.textContent=LED[ledI];led.style.opacity=1},350)},4500);
  led.style.transition='opacity .35s';
  function refresh(){loadAll().then(render)}
  refresh();loadTable().then(renderTable);
})();
</script>
</body>
</html>
'''
out = PAGE.replace('__SVG__', svg).replace('__GLOBE__', globe).replace('__GUIDES__', json.dumps(GC, ensure_ascii=False))
os.makedirs('/home/claude/site/match-hub/leeds', exist_ok=True)
open('/home/claude/site/match-hub/leeds/index.html', 'w').write(out)
print('leeds hub', len(out) // 1024, 'KB')
