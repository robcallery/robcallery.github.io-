import re, os
src = open('/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/passport.py').read()
PAGE = re.search(r"PAGE = r'''(.*?)'''\nos\.makedirs", src, re.S).group(1)
fav = open('/home/claude/favicon.svg').read()
globe = re.search(r'<path fill="#f7f7f2" fill-rule="evenodd" d="([^"]+)"', fav).group(1)

GUIDES_JS = r'''// ===== Rob's Travel Guides =====
// Add a city by copying one block below and filling it in. Leave out anything you don't need.
// visited: "YYYY-MM".  rating: 1-5 (would you go back?).
// colour: "teal", "red", "blue", "green", "orange" or "purple".
window.GUIDES = [
  // {
  //   city: "Málaga",
  //   country: "Spain",
  //   group: "Airports",   (optional: list it under its own heading instead of the country)
  //   visited: "2026-06",
  //   pint: "€3",
  //   localBeer: "Victoria",
  //   bestFor: "Beach bars and tapas",
  //   bars: [
  //     { name: "Bar name", note: "Why it's good" },
  //     { name: "Another bar", note: "What to order" }
  //   ],
  //   eat: "What to eat and where",
  //   dontMiss: "The one thing to do",
  //   football: "Local team / stadium / where to watch Leeds",
  //   gettingThere: "Flights, trains, tips",
  //   rating: 5,
  //   colour: "orange",
  //   notes: "A line or two in your own words."
  // },
];
'''

# --- swap the passport look for a guidebook look
PAGE = PAGE.replace('<title>Beer Passport - Rob Callery</title>', '<title>Travel Guides - Rob Callery</title>')
PAGE = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Rob Callery\'s pint-first travel guides: where to drink, eat and watch the football in every city.">', PAGE, count=1)
PAGE = PAGE.replace("<h1 class=\"sr\">Rob Callery's Beer Passport</h1>", "<h1 class=\"sr\">Rob Callery's Travel Guides</h1>")
PAGE = PAGE.replace('<script src="beers.js"></script>', '<script src="/travel-guides/guides.js"></script><script src="/travel-guides/snaps.js"></script>')
PAGE = PAGE.replace('<a class="back" href="/explore/">← Back to the bar</a>', '<a class="back" href="/travel-guides/">← Back to the shelf</a>')
assert '--burg:#1b2b4d;--burg2:#0b1630;--paper:#f6efdc;' in PAGE
PAGE = PAGE.replace('--burg:#1b2b4d;--burg2:#0b1630;--paper:#f6efdc;', '--burg:#0f6f73;--burg2:#0a4a4d;--paper:#fbf7ec;')
PAGE = PAGE.replace("Tap a page, swipe, or use the arrow keys to flick through.", "Tap a page, swipe, or use the arrow keys to flick through the guide.")
CSS = r'''
  /* ---------- guidebook ---------- */
  .page{font-family:Inter,system-ui,sans-serif}
  .cover{background:linear-gradient(135deg,var(--burg),var(--burg2));justify-content:space-between;padding:2.4em 1.5em}
  .cover::before{content:"";position:absolute;inset:.8em;border:1.5px dashed rgba(255,205,0,.45);border-radius:6px}
  .cover .t1{color:#ffcd00}
  .cover .t2{font-family:"Bebas Neue",Impact,sans-serif;font-size:2.3em;letter-spacing:.06em;line-height:1;color:#ffcd00}
  .cover .gl{width:56%;height:auto}
  .cover .t2{color:#ffcd00}
  .cover .t3{font-family:"DM Serif Display",Georgia,serif;font-style:italic;font-size:1.05em;letter-spacing:0;color:#f7f2e4;opacity:1}
  .cover .by{font-family:"Bebas Neue",Impact,sans-serif;letter-spacing:.3em;color:#f7f2e4;font-size:.9em}
  .cover::before{border-color:rgba(255,205,0,.45)}
  .contents h2{font-family:"DM Serif Display",Georgia,serif;font-weight:400;font-size:1.7em;line-height:1;margin:.5em 0 .1em;color:#0a4a4d}
  .toc{list-style:none;margin-top:.4em}
  .contents h2.cont small{font-size:.5em;color:#8a7a58}
  .toc li{display:flex;align-items:baseline;gap:.4em;font-size:.78em;padding:.2em 0;border-bottom:1px dotted var(--line)}
  .toc li.grp{font-family:"Bebas Neue",Impact,sans-serif;letter-spacing:.2em;color:#0f6f73;font-size:.82em;border-bottom:1.5px solid #0f6f73;padding-top:.3em}
  .toc li b{font-family:"DM Serif Display",Georgia,serif;font-weight:400;font-size:1.15em}
  .toc li span.c{color:#8a7a58;font-size:.85em;flex:1}
  .toc li span.p{font-family:"Space Mono",monospace;font-size:.85em}
  .legend{margin-top:.6em;font-size:.6em;color:#6f6450;line-height:1.45}
  .hero{position:relative;margin:.55em -1.5em 0;padding:.5em 1.5em .3em;color:#fff;background:var(--c,#0f6f73);overflow:hidden;min-height:5.2em}
  .hero .sky{position:absolute;left:0;right:0;bottom:0;height:60%;opacity:.28}
  .hero .country{position:relative;font-family:"Bebas Neue",Impact,sans-serif;letter-spacing:.25em;font-size:.82em;opacity:.9}
  .hero h2{position:relative;font-family:"DM Serif Display",Georgia,serif;font-weight:400;font-size:2.3em;line-height:1.02;letter-spacing:-.01em}
  .hero .vis{position:relative;font-size:.62em;letter-spacing:.14em;text-transform:uppercase;opacity:.9;margin-top:.15em}
  .glance{display:grid;grid-template-columns:repeat(3,1fr);gap:.4em;margin:.6em 0 .3em}
  .glance>div{background:rgba(15,111,115,.07);border:1px solid var(--line);border-radius:4px;padding:.3em .4em;min-width:0}
  .glance .k,.sec .k{font-size:.52em;letter-spacing:.14em;text-transform:uppercase;color:#8a7a58}
  .glance .v{font-weight:700;font-size:.74em;line-height:1.2;overflow:hidden;text-overflow:ellipsis}
  .sec{margin-top:.38em}
  .sec .k{display:flex;align-items:center;gap:.4em;color:var(--c,#0f6f73);font-weight:700}
  .sec .k::after{content:"";flex:1;height:1px;background:var(--line)}
  .sec p,.sec li{font-size:.7em;line-height:1.38}
  .sec ul{list-style:none}
  .sec li b{font-weight:700}
  .badge{display:inline-block;font-family:"Bebas Neue",Impact,sans-serif;font-size:.95em;letter-spacing:.08em;line-height:1;background:#1b3a8f;color:#fff;border-radius:3px;padding:.15em .35em .1em;vertical-align:.08em}
  .badge.none{background:#8a7a58}
  .rate{display:flex;align-items:center;gap:.5em;margin-top:.4em;font-size:.6em;letter-spacing:.12em;text-transform:uppercase;color:#8a7a58}
  .rate .pints svg{width:1.6em}
  .page .notes{font-size:1.12em;margin-top:.3em}
  .page.city .mrz{display:none}
  .foot{margin-top:auto;display:flex;justify-content:space-between;font-family:"Bebas Neue",Impact,sans-serif;letter-spacing:.2em;font-size:.68em;color:#8a7a58;border-top:1px solid var(--line);padding-top:.4em}
  .tag{margin:2.2em auto .8em;width:62%;aspect-ratio:1.6;border:2px dashed #b9ab86;border-radius:.6em;display:grid;place-items:center;text-align:center;position:relative;color:#8a7a58;font-family:"Bebas Neue",Impact,sans-serif;letter-spacing:.15em;font-size:1.25em;line-height:1.2}
  .tag::before{content:"";position:absolute;left:-1.1em;top:50%;width:.7em;height:.7em;border:2px solid #b9ab86;border-radius:50%;transform:translateY(-50%)}
  .biro{position:relative;margin:.55em .2em 0 .4em;font-family:"Caveat",cursive;font-weight:500;font-size:1.25em;line-height:1.1;color:#1f3fa8;transform:rotate(-1.6deg);text-shadow:0 0 .4px #1f3fa8;opacity:.92}
  .biro .tt{font-weight:700;text-decoration:underline;text-decoration-thickness:1.5px;text-underline-offset:2px;text-decoration-style:wavy}

  .page.snap{display:flex;flex-direction:column}
  .pol{position:relative;margin:1.4em auto .2em;width:94%;background:#fffdf8;padding:.55em .55em 0;box-shadow:0 .25em .7em rgba(40,30,10,.28),0 .05em .15em rgba(40,30,10,.25);border-radius:2px}
  .pol .pic{aspect-ratio:5/4;background:#ddd;overflow:hidden}
  .pol .pic svg{width:100%;height:100%;display:block}
  .pol .nopic{height:100%;display:grid;place-items:center;font-family:"Caveat",cursive;font-size:1.4em;color:#8a7a58;background:#efe9da}
  .pol .cap{font-family:"Caveat",cursive;font-weight:600;font-size:1.45em;line-height:1;color:#22305c;text-align:center;padding:.38em .2em .5em}
  .pol .tape{position:absolute;width:26%;height:1.2em;background:rgba(250,240,200,.72);box-shadow:0 1px 2px rgba(0,0,0,.08);top:-.55em}
  .pol .tape.a{left:-5%;transform:rotate(-28deg)}
  .pol .tape.b{right:-5%;transform:rotate(26deg)}
  .dyk{margin:.9em .4em 0}
  .dyk .k{display:flex;align-items:center;gap:.4em;font-size:.52em;letter-spacing:.14em;text-transform:uppercase;color:var(--c,#0f6f73);font-weight:700}
  .dyk .k::after{content:"";flex:1;height:1px;background:var(--line)}
  .dyk p{font-size:.72em;line-height:1.4;margin-top:.2em}
  .page.snap .mrz,.page.blank .mrz{display:none}
  .backin{background:linear-gradient(135deg,var(--burg2),var(--burg))}
'''
PAGE = PAGE.replace('  /* controls */', CSS + '  /* controls */', 1)

JS_PAGES = r'''
  var GLOBE='__GLOBE__';
  var demo=/[?&]demo\b/.test(location.search);
  var SHELVES=__SHELVES__;
  __SHELFOF__
  var Q=location.search, shelfQ=(Q.match(/[?&]shelf=([^&]+)/)||[])[1], cityQ0=(Q.match(/[?&]city=([^&]+)/)||[])[1];
  try{cityQ0=cityQ0&&decodeURIComponent(cityQ0.replace(/\+/g,' '))}catch(e){}
  var ALL=(window.GUIDES||[]).slice();
  if(!shelfQ&&cityQ0){ALL.forEach(function(g){if(!shelfQ&&g.city.toLowerCase()===cityQ0.toLowerCase())shelfQ=shelfOf(g)})}
  var SH=null;SHELVES.forEach(function(s){if(s.id===shelfQ)SH=s});
  if(!SH&&!demo){location.replace('/travel-guides/');return}
  var beers=SH?ALL.filter(function(g){return shelfOf(g)===SH.id}):ALL;
  if(SH){var rs=document.documentElement.style;rs.setProperty('--burg',SH.c);rs.setProperty('--burg2','#'+SH.c.slice(1).match(/../g).map(function(h){return ('0'+Math.round(parseInt(h,16)*.68).toString(16)).slice(-2)}).join(''));document.title='Travelling '+SH.t+' One Beer at a Time - Rob Callery'}
  if(demo&&!beers.length){beers=[
    {city:"Leeds",country:"England",visited:"2026-10",pint:"£5",localBeer:"Kirkstall Pale",bestFor:"Matchdays & real ale",bars:[{name:"A canal-side brewery tap",note:"pre-match pints"},{name:"An old Victorian boozer",note:"cask on every pump"}],eat:"Something hot from the market before the walk to the ground.",dontMiss:"A night match under the lights at Elland Road.",football:"Elland Road, obviously. Get there early.",rating:5,colour:"blue",notes:"Home. No guide needed, but here's one anyway."},
    {city:"Málaga",country:"Spain",visited:"2026-06",pint:"€3",localBeer:"Victoria",bestFor:"Beach bars & tapas",bars:[{name:"A chiringuito on the beach",note:"cold lager, sardines on the fire"},{name:"Old town tapas bars",note:"hop between three or four"}],eat:"Espetos (grilled sardines) right on the sand.",dontMiss:"Sunset from the castle walls, then back down for one more.",football:"Málaga CF at La Rosaleda.",rating:5,colour:"orange",notes:"Firpo't of Call territory. Would move there tomorrow."},
    {city:"Dublin",country:"Ireland",visited:"2025-03",pint:"€7",localBeer:"Guinness",bestFor:"Pubs with live music",bars:[{name:"The Gravity Bar",note:"the pint with a view"},{name:"Any pub with a fiddle in the corner",note:"stay for the session"}],eat:"A proper stew to line the stomach.",dontMiss:"The brewery tour, then walk it off by the river.",football:"Catch a game in a sports bar with the locals.",rating:4,colour:"green",notes:"Pricey pints, but you're paying for the atmosphere."}
  ];}
  var COL={teal:"#0f6f73",red:"#b3262b",blue:"#1d4ed8",green:"#1f7a43",orange:"#d9711c",purple:"#6b2fa3"};
  var cols=["teal","orange","blue","green","red","purple"];
  function esc(t){return String(t==null?'':t).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
  function fmtMonth(d){if(!d)return'';var x=new Date((d.length<=7?d+'-15':d)+'T12:00:00');if(isNaN(x))return esc(d);return x.toLocaleDateString('en-GB',{month:'long',year:'numeric'})}
  function wm(){return '<div class="wm"><svg viewBox="190 157 700 700"><path fill="#0f6f73" fill-rule="evenodd" d="'+GLOBE+'"/></svg></div>'}
  function top(label,n){return '<div class="top"><span>'+label+'</span><span class="pno">'+(n<10?'0':'')+n+'</span></div>'}
  function mrz(){return ''}
  function pint(full){return '<svg viewBox="0 0 20 28"><path d="M3 4 L17 4 L15 26 L5 26 Z" fill="'+(full?'#e8a317':'none')+'" stroke="#6f6450" stroke-width="1.6" stroke-linejoin="round"/>'+(full?'<path d="M2.5 5 Q4 0 8 2 Q10 -1 13 2 Q17 0 17.5 5 Z" fill="#fff" stroke="#6f6450" stroke-width="1.2"/>':'')+'</svg>'}
  function skyline(seed){
    var x=0,d='M0 60',r=seed*9301+49297;
    function rnd(){r=(r*9301+49297)%233280;return r/233280}
    while(x<300){var w=8+rnd()*22,h=12+rnd()*40;if(rnd()<.15){d+=' L'+x+' '+(60-h)+' L'+(x+w/2)+' '+(60-h-14)+' L'+(x+w)+' '+(60-h);}else{d+=' L'+x+' '+(60-h)+' L'+(x+w)+' '+(60-h);}x+=w;}
    return '<svg class="sky" viewBox="0 0 300 60" preserveAspectRatio="none"><path d="'+d+' L300 60 Z" fill="#000"/></svg>';
  }
  var INSIDE='<div class="ep">'+wm()+'<div class="own"><span>This guide belongs to</span><b>ROB CALLERY</b><span>If found, return it to the nearest bar.</span></div></div>';
  var pages=[];
  pages.push({cls:'cover',html:'<div class="t1">'+(SH?'TRAVELLING':'TRAVEL GUIDES')+'</div>'+(SH?'<div class="t2">'+esc(SH.t.toUpperCase())+'</div>':'')+'<svg class="gl" viewBox="190 157 700 700"><circle cx="540" cy="507" r="345" fill="#0a1838"/><path fill="#f7f2e4" fill-rule="evenodd" d="'+GLOBE+'"/></svg><div><div class="t3">one beer at a time</div></div><div class="by">ROB CALLERY</div><div class="hint">tap to open</div>'});
  var rows=[],lastC=null;beers.forEach(function(g,i){var gk=g.group||g.country;if(gk!==lastC){rows.push({grp:gk||''});lastC=gk}rows.push({g:g,i:i})});
  var FIRST=13,MORE=19,chunks=[];if(!rows.length)chunks=[[]];else{var k=0;while(k<rows.length){var n=chunks.length?MORE:FIRST,ch=rows.slice(k,k+n);if(k+n<rows.length&&ch.length>1&&ch[ch.length-1].grp!=null)ch.pop();chunks.push(ch);k+=ch.length;}}
  var C=chunks.length, F=(C+1)%2;
  chunks.forEach(function(ch,ci){
    var toc=ch.map(function(r){if(r.grp!=null)return '<li class="grp">'+esc(r.grp)+'</li>';var n=C+1+F+2*r.i;return '<li><b>'+esc(r.g.city)+'</b><span class="c">'+esc(r.g.region||r.g.country)+'</span><span class="p">'+(n<10?'0':'')+n+'</span></li>'}).join('');
    pages.push({cls:'contents',html:wm()+top('TRAVEL GUIDES · CONTENTS',ci+1)+(ci===0?'<h2>Where I\'ve been</h2>':'<h2 class="cont">Where I\'ve been <small>(cont.)</small></h2>')+
      (beers.length?'<ul class="toc">'+toc+'</ul>':'<p class="legend" style="font-size:.8em">The first guides are being written. Check back soon!</p>')+
      (ci===0?'<p class="legend">Every guide is pint-first: what a pint costs, the local beer, the local Spoons where there is one, the bars worth the walk, where to eat, and where to watch the football. Rated on whether I\'d go back.</p>':'')+
      '<div class="foot"><span>ROB CALLERY</span><span>EDITION '+new Date().getFullYear()+'</span></div>'});
  });
  if(F) pages.push({cls:'blank',html:wm()+top('TRAVEL GUIDES · NOTES',pages.length)+'<div class="biro" style="margin-top:2em">Notes, beer mats and receipts go here…</div>'});
  var SN=window.SNAPS||{};
  beers.forEach(function(g,i){
    var c=COL[g.colour]||COL[cols[i%cols.length]], r=Math.max(0,Math.min(5,Math.round(g.rating||0))), p='';for(var k=0;k<5;k++)p+=pint(k<r);
    var bars=(g.bars||[]).slice(0,3).map(function(b){return '<li><b>'+esc(b.name)+'</b>'+(b.note?' – '+esc(b.note):'')+'</li>'}).join('');
    if(g.spoons) bars='<li class="spoons"><span class="badge'+(g.spoons.none?' none':'')+'">'+(g.spoons.none?'NO SPOONS':g.spoons.nearest?'NEAREST SPOONS':'SPOONS')+'</span> '+(g.spoons.name?'<b>'+esc(g.spoons.name)+'</b>'+(g.spoons.note?' – ':''):'')+esc(g.spoons.note||'')+'</li>'+bars;
    var sec=function(k,v){return v?'<div class="sec"><div class="k">'+k+'</div>'+v+'</div>':''};
    pages.push({cls:'city',gi:i,style:'--c:'+c,html:wm()+top('TRAVEL GUIDES · '+esc((g.region||g.country||'').toUpperCase()),pages.length)+
      '<div class="hero">'+skyline(i+3)+'<div class="country">'+esc(((g.region?g.region+' · ':'')+({'United Kingdom':'UK'}[g.country]||g.country||'')).toUpperCase())+'</div><h2>'+esc(g.city)+'</h2>'+(g.visited?'<div class="vis">Visited '+fmtMonth(g.visited)+'</div>':'')+'</div>'+
      '<div class="glance"><div><div class="k">A pint</div><div class="v">'+esc(g.pint||'–')+'</div></div><div><div class="k">Local beer</div><div class="v">'+esc(g.localBeer||'–')+'</div></div><div><div class="k">Best for</div><div class="v">'+esc(g.bestFor||'–')+'</div></div></div>'+
      sec('Where to drink',bars?'<ul>'+bars+'</ul>':'')+sec('Eat','<p>'+esc(g.eat||'')+'</p>'.replace('<p></p>',''))+sec('Don\'t miss',g.dontMiss?'<p>'+esc(g.dontMiss)+'</p>':'')+sec('Football',g.football?'<p>'+esc(g.football)+'</p>':'')+sec('Getting there',g.gettingThere?'<p>'+esc(g.gettingThere)+'</p>':'')+
      (r?'<div class="rate">Would I go back? <span class="pints">'+p+'</span></div>':'')+
      (g.notes?'<div class="notes">“'+esc(g.notes)+'”</div>':'')+
      (g.tip?'<div class="biro"><span class="tt">Top tip!</span> '+esc(g.tip)+'</div>':'')+
      (demo&&!(window.GUIDES||[]).length?'<div class="sample">SAMPLE</div>':'')});
    var sn=SN[g.city], rot=[-2.6,1.8,-1.4,2.4,-2][i%5];
    pages.push({cls:'snap',gi:i,style:'--c:'+c,html:wm()+top('TRAVEL GUIDES · SNAPSHOT',pages.length)+
      '<div class="pol" style="transform:rotate('+rot+'deg)"><i class="tape a"></i><i class="tape b"></i><div class="pic">'+(sn?sn.svg:'<div class="nopic">Photo coming soon</div>')+'</div><div class="cap">'+esc(sn?sn.t:g.city)+'</div></div>'+
      (sn&&sn.n?'<div class="dyk"><div class="k">Did you know?</div><p>'+esc(sn.n)+'</p></div>':'')+
      '<div class="foot"><span>'+esc(g.city.toUpperCase())+'</span><span>ONE BEER AT A TIME</span></div>'});
  });
  pages.push({cls:'await',html:wm()+top('TRAVEL GUIDES · NEXT STOP',pages.length)+'<div class="tag">NEXT DESTINATION<br>TBC</div><div class="await-msg">'+(beers.length?'Bags are packed. Next guide coming soon…':'The first guides are being written.<br>Check back soon!')+'</div><div class="foot"><span>ROB CALLERY</span><span>ONE BEER AT A TIME</span></div>'});
'''
import sys; sys.path.insert(0,'/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad')
from shelves import SHELF_JSON, SHELF_OF_JS
JS_PAGES = JS_PAGES.replace('__SHELVES__', SHELF_JSON).replace('__SHELFOF__', SHELF_OF_JS)
start = PAGE.index("  var GLOBE='__GLOBE__';")
end = PAGE.index("  var stage=document.getElementById('stage')")
PAGE = PAGE[:start] + JS_PAGES.lstrip('\n') + PAGE[end:]
# pages can carry a style (city colour)
PAGE = PAGE.replace("""function face(p,side){return '<div class="face '+side+'"><div class="page '+(p&&p.cls||'')+'">'""",
                    """function face(p,side){return '<div class="face '+side+'"><div class="page '+(p&&p.cls||'')+'"'+(p&&p.style?' style="'+p.style+'"':'')+'>'""")
PAGE = PAGE.replace("label=cur===1?'Holder page':(cur-1<=beers.length?'Beer '+(cur-1)+' of '+beers.length:'Next stamp'); if(cur>=N-1&&cur-1>beers.length) label='Next stamp';",
                    "label=cur<=C?'Contents':(pages[cur]&&pages[cur].gi!=null?beers[pages[cur].gi].city+' · '+(pages[cur].gi+1)+' of '+beers.length:'Next stop');")
PAGE = PAGE.replace("label=cur===1?'Holder page':(cur===N", "label=(cur===1||a<=C)?'Contents':(pages[a]&&pages[a].gi!=null)?beers[pages[a].gi].city+' · pages '+a+'–'+(a+1):(cur===N")
PAGE = PAGE.replace("This passport is the property of","This guide belongs to").replace("If found, please return to the nearest pub.","If found, return it to the nearest bar.")
_SA = "  var startAt=parseInt((location.search.match(/[?&]page=(\\d+)/)||[])[1]||'1',10);"
assert _SA in PAGE
PAGE = PAGE.replace(_SA, _SA + r"""
  var cityQ=(location.search.match(/[?&]city=([^&]+)/)||[])[1];
  if(cityQ){try{cityQ=decodeURIComponent(cityQ.replace(/\+/g,' '))}catch(e){}
    var gi=-1;beers.forEach(function(g,i){if(gi<0&&g.city.toLowerCase()===cityQ.toLowerCase())gi=i});
    if(gi>=0){var k=-1;pages.forEach(function(p,i){if(k<0&&p.gi===gi&&p.cls==='city')k=i});if(k>=0)startAt=single?k:(k+2)/2}}""",1)
assert "'Contents'" in PAGE and 'guides.js' in PAGE

os.makedirs('/home/claude/site/travel-guides', exist_ok=True)
os.makedirs('/home/claude/site/travel-guides/guide', exist_ok=True)
open('/home/claude/site/travel-guides/guide/index.html', 'w').write(PAGE.replace('__GLOBE__', globe))
gj = '/home/claude/site/travel-guides/guides.js'
if not os.path.exists(gj):
    open(gj, 'w').write(GUIDES_JS)
print('guide built')
