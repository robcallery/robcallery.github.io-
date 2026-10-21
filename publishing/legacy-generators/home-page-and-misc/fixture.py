import sys
sign='''
    <!-- next home game board, left of the stadium (live from ESPN fixtures) -->
    <g id="fixture" transform="translate(292 628)">
      <rect x="18" y="66" width="6" height="66" fill="#3a3f4b"/><rect x="122" y="66" width="6" height="66" fill="#3a3f4b"/>
      <rect x="0" y="0" width="146" height="72" rx="5" fill="#0b0d12" stroke="#ffcd00" stroke-width="2.5"/>
      <rect x="4" y="4" width="138" height="14" rx="2" fill="#ffcd00"/>
      <text x="73" y="14.6" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="11.5" letter-spacing="1.5" fill="#0a1838">NEXT HOME GAME</text>
      <g font-family="Bebas Neue, Impact, sans-serif" text-anchor="middle" class="led">
        <text id="fxTeams" x="73" y="38" font-size="17" fill="#ffffff">LEEDS UNITED</text>
        <text id="fxDate" x="73" y="53" font-size="11" fill="#ffcd00">ELLAND ROAD</text>
        <text id="fxCount" x="73" y="66" font-size="9" fill="#9fb3d9" letter-spacing=".5"></text>
      </g>
    </g>
'''
css='''  #fixture .led text{filter:drop-shadow(0 0 2px rgba(255,205,0,.35))}
  #fxCount.live{fill:#ff4d4d;animation:tw 1s steps(2) infinite}
'''
js=r'''<script>
// live "next home game" board (ESPN fixtures, TheSportsDB fallback)
(function(){
  var T=document.getElementById('fxTeams'),Dt=document.getElementById('fxDate'),C=document.getElementById('fxCount'); if(!T) return;
  function fit(el,max){el.removeAttribute('textLength');try{if(el.getComputedTextLength()>max){el.setAttribute('textLength',max);el.setAttribute('lengthAdjust','spacingAndGlyphs')}}catch(e){}}
  var game=null;
  function nowT(){var m=location.search.match(/[?&]time=([^&]+)/);return m?new Date(decodeURIComponent(m[1])):new Date()}
  function render(){
    if(!game){T.textContent='LEEDS UNITED';Dt.textContent='FIXTURES TBC';C.textContent='';return}
    T.textContent=('LEEDS v '+game.opp).toUpperCase(); fit(T,132);
    var tz={timeZone:'Europe/London'};
    var d=game.date.toLocaleDateString('en-GB',Object.assign({weekday:'short',day:'numeric',month:'short'},tz)).replace(',','');
    var t=game.date.toLocaleTimeString('en-GB',Object.assign({hour:'2-digit',minute:'2-digit'},tz));
    Dt.textContent=(d+' · '+(game.tbc?'TBC':t+' KO')).toUpperCase(); fit(Dt,132);
    var ms=game.date-nowT(), mins=Math.round(ms/60000);
    C.classList.remove('live');
    if(ms<=0&&ms>-2*3600e3){C.textContent='● MATCH ON NOW';C.classList.add('live')}
    else if(mins<60) C.textContent='KICK OFF IN '+Math.max(1,mins)+' MINS';
    else if(mins<24*60) C.textContent='KICK OFF IN '+Math.floor(mins/60)+'H '+(mins%60)+'M';
    else {var days=Math.round(ms/864e5);C.textContent='IN '+days+' DAY'+(days==1?'':'S')}
  }
  function pick(list){
    var n=nowT();
    list=list.filter(function(g){return g.date-n>-2*3600e3}).sort(function(a,b){return a.date-b.date});
    game=list[0]||null; render();
  }
  function espn(){
    return fetch('https://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/teams/357/schedule?fixture=true').then(function(r){return r.json()}).then(function(d){
      var out=[];(d.events||[]).forEach(function(e){var c=(e.competitions||[])[0];if(!c)return;
        var home=c.competitors.filter(function(x){return x.homeAway=='home'})[0], away=c.competitors.filter(function(x){return x.homeAway=='away'})[0];
        if(!home||!away||String(home.team.id)!=='357')return;
        var st=c.status&&c.status.type||{}; if(st.state==='post')return;
        out.push({date:new Date(c.date||e.date),opp:away.team.shortDisplayName||away.team.displayName,tbc:!!(e.timeValid===false)});});
      if(!out.length) throw 0; return out;});
  }
  function sportsdb(){
    return fetch('https://www.thesportsdb.com/api/v1/json/123/eventsnext.php?id=133635').then(function(r){return r.json()}).then(function(d){
      return (d.events||[]).filter(function(e){return /leeds/i.test(e.strHomeTeam)}).map(function(e){return {date:new Date((e.strTimestamp||e.dateEvent+'T'+(e.strTime||'15:00:00'))+'Z'),opp:e.strAwayTeam}});});
  }
  function load(){espn().catch(sportsdb).then(pick).catch(function(){game=null;render()})}
  load(); setInterval(load,30*60e3); setInterval(render,60e3);
})();
</script>'''
for f in sys.argv[1:]:
    s=open(f).read()
    if 'id="fixture"' in s: continue
    anchor="    <!-- every so often: a prop plane"
    s=s.replace(anchor,sign+"\n"+anchor,1)
    s=s.replace("  .blink{",css+"  .blink{",1)
    s=s.replace("<script>\n// spin the logo faster",js+"\n<script>\n// spin the logo faster",1)
    open(f,'w').write(s); print('ok',f)
