import re, os
fav = open('/home/claude/favicon.svg').read()
globe = re.search(r'<path fill="#f7f7f2" fill-rule="evenodd" d="([^"]+)"', fav).group(1)

BEERS_JS = r'''// ===== Rob's Beer Passport =====
// Add a new beer by copying one block below and filling it in.
// rating: 1-5 pints.  ink: "red", "blue", "green", "purple" or "black".
// date: "YYYY-MM-DD".  notes: a sentence or two in your own words.
window.BEERS = [
  // {
  //   name: "Beer name",
  //   brewery: "Brewery",
  //   style: "Pale Ale",
  //   abv: 4.5,
  //   where: "Pub or bar name",
  //   city: "Leeds",
  //   country: "England",
  //   date: "2026-10-20",
  //   rating: 4,
  //   ink: "red",
  //   notes: "What it was like."
  // },
];
'''

PAGE = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Beer Passport - Rob Callery</title>
<meta name="description" content="Rob Callery's beer passport: every beer stamped with where it was drunk and how it rated.">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Caveat:wght@500;700&family=DM+Serif+Display:ital@0;1&family=Inter:wght@400;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
  :root{--navy:#0a1838;--yellow:#ffcd00;--cream:#f7f2e4;--muted:#b8c3dc;--burg:#1b2b4d;--burg2:#0b1630;--paper:#f6efdc;--ink:#2a2a35;--line:#cdbf9c;--gold:#d9b45a}
  *{box-sizing:border-box;margin:0;padding:0}
  html,body{height:100%}
  body{min-height:100vh;background:radial-gradient(ellipse 90% 60% at 50% 0,#2b417e 0,#13285a 45%,#0a1838 100%);color:var(--cream);font-family:Inter,system-ui,sans-serif;display:flex;flex-direction:column;overflow-x:hidden}
  a{color:inherit}
  header{display:flex;align-items:center;justify-content:space-between;gap:16px;max-width:1160px;width:100%;margin:0 auto;padding:18px 16px}
  .brand{display:flex;align-items:center;gap:10px;text-decoration:none;font-family:"Bebas Neue",Impact,sans-serif;font-size:1.6rem;letter-spacing:.06em;white-space:nowrap}
  .brand svg{width:38px;height:38px}
  .back{font-size:.92rem;font-weight:600;text-decoration:none;opacity:.85;padding:.45em .9em;border:1.5px solid rgba(247,242,228,.4);border-radius:999px;white-space:nowrap}
  .back:hover,.back:focus-visible{opacity:1;border-color:var(--yellow)}
  main{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:4px 16px 24px}
  h1.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}

  /* ---------- the book ---------- */
  .stage{--pw:min(390px,44vw,calc((100vh - 210px)*.7));--ph:calc(var(--pw)/.7);perspective:2400px;width:calc(var(--pw)*2);height:var(--ph);position:relative;transition:transform .9s cubic-bezier(.3,.7,.2,1)}
  .stage.closed{transform:translateX(calc(var(--pw)*-.5))}
  .under{position:absolute;top:calc(var(--pw)*-.025);bottom:calc(var(--pw)*-.025);width:calc(var(--pw)*1.025);background:linear-gradient(135deg,var(--burg),var(--burg2));box-shadow:0 30px 60px rgba(0,0,0,.5);transition:opacity .5s}
  .under.l{left:calc(var(--pw)*-.025);border-radius:14px 0 0 14px}
  .under.r{right:calc(var(--pw)*-.025);border-radius:0 14px 14px 0}
  .under.l{transition:opacity .25s .85s}
  .stage.closed .under.l{opacity:0;transition-delay:0s}
  .page.inside{background:linear-gradient(135deg,var(--burg2),var(--burg));padding:calc(var(--pw)*.04)}
  .page.inside .ep{position:relative;flex:1;border-radius:4px;background:var(--paper);display:grid;place-items:center;text-align:center;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08)}
  .page.inside .own{position:relative;display:flex;flex-direction:column;gap:.5em;align-items:center;color:#6f6450}
  .page.inside .own span{font-size:.7em;letter-spacing:.12em;text-transform:uppercase}
  .page.inside .own b{font-family:"Caveat",cursive;font-weight:700;font-size:2.4em;color:#1d3a8a;letter-spacing:0}
  .spine{position:absolute;left:calc(50% - 3px);top:0;bottom:0;width:6px;background:linear-gradient(90deg,rgba(0,0,0,.25),rgba(0,0,0,0));z-index:400;pointer-events:none}
  .stage.closed .spine{opacity:0}
  .leaf{position:absolute;top:0;left:50%;width:var(--pw);height:100%;transform-origin:0 50%;transform-style:preserve-3d;transition:transform 1s cubic-bezier(.45,.05,.25,1);cursor:pointer}
  .leaf.flipped{transform:rotateY(-180deg)}
  .face{position:absolute;inset:0;backface-visibility:hidden;-webkit-backface-visibility:hidden;overflow:hidden}
  .face.b{transform:rotateY(180deg)}
  .face::after{content:"";position:absolute;inset:0;pointer-events:none}
  .face.f::after{background:linear-gradient(90deg,rgba(0,0,0,.14),rgba(0,0,0,0) 9%)}
  .face.b::after{background:linear-gradient(270deg,rgba(0,0,0,.14),rgba(0,0,0,0) 9%)}
  .face.f{border-radius:0 8px 8px 0}.face.b{border-radius:8px 0 0 8px}

  /* single page on phones */
  .stage.single{--pw:min(92vw,calc((100vh - 200px)*.7),420px);width:var(--pw)}
  .stage.single.closed{transform:none}
  .stage.single .under.l,.stage.single .spine{display:none}
  .stage.single .under.r{left:calc(var(--pw)*-.02);right:calc(var(--pw)*-.02);border-radius:14px}
  .stage.single .leaf{left:0}
  .stage.single .leaf.flipped{transform:rotateY(-165deg);opacity:0;transition:transform .9s cubic-bezier(.45,.05,.25,1),opacity .25s .6s}

  /* ---------- pages ---------- */
  .page{position:absolute;inset:0;font-size:calc(var(--pw)/25);color:var(--ink);background-color:var(--paper);background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='40'%3E%3Cpath d='M0 20 Q15 8 30 20 T60 20 T90 20 T120 20' fill='none' stroke='%23d9cfb4' stroke-width='.7'/%3E%3Cpath d='M0 30 Q15 18 30 30 T60 30 T90 30 T120 30' fill='none' stroke='%23e3d9c0' stroke-width='.6'/%3E%3Cpath d='M0 10 Q15 -2 30 10 T60 10 T90 10 T120 10' fill='none' stroke='%23e3d9c0' stroke-width='.6'/%3E%3C/svg%3E"),radial-gradient(ellipse at 50% 45%,rgba(255,255,255,.55),rgba(255,255,255,0) 70%);padding:1.4em 1.5em 1.2em;display:flex;flex-direction:column}
  .page .top{display:flex;justify-content:space-between;align-items:baseline;font-family:"Bebas Neue",Impact,sans-serif;letter-spacing:.14em;font-size:.8em;color:#8a7a58;border-bottom:1px solid var(--line);padding-bottom:.35em}
  .page .pno{font-family:"Space Mono",monospace;letter-spacing:0;font-size:.95em}
  .page .wm{position:absolute;inset:0;display:grid;place-items:center;pointer-events:none;opacity:.07}
  .page .wm svg{width:70%;height:auto}
  .mrz{margin-top:auto;font-family:"Space Mono",monospace;font-size:.62em;letter-spacing:.12em;color:#6f6450;line-height:1.5;white-space:nowrap;overflow:hidden;border-top:1px solid var(--line);padding-top:.45em}

  /* cover */
  .cover{background:#0e1a33;color:var(--gold);align-items:center;text-align:center;justify-content:flex-end;padding:0 1em .55em;overflow:hidden}
  .cover .coverimg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
  .cover .hint{position:relative}
  .cover .t1{font-family:"Bebas Neue",Impact,sans-serif;font-size:1.25em;letter-spacing:.22em;line-height:1.25}
  .cover svg.crest{width:58%;height:auto}
  .cover .t2{font-family:"Bebas Neue",Impact,sans-serif;font-size:2.6em;letter-spacing:.08em;line-height:1}
  .cover .t3{font-size:.62em;letter-spacing:.3em;opacity:.85}
  .cover .chip{width:2.4em;height:1.6em;border:1.5px solid var(--gold);border-radius:3px;position:relative}
  .cover .chip::after{content:"";position:absolute;inset:.3em .85em;border:1.5px solid var(--gold);border-radius:50%}
  .cover .hint{font-family:"Caveat",cursive;color:#f2dca0;font-size:1.05em;opacity:.9}

  /* ID page */
  .idgrid{display:grid;grid-template-columns:38% 1fr;gap:.9em;margin-top:1em}
  .photo{aspect-ratio:3/4;background:linear-gradient(#e6dcc2,#d6c9a8);border:1px solid var(--line);display:grid;place-items:end center;overflow:hidden}
  .photo svg{width:88%;height:auto}
  .fld{margin-bottom:.5em}
  .fld .k{font-size:.56em;letter-spacing:.14em;text-transform:uppercase;color:#8a7a58}
  .fld .v{font-family:"Space Mono",monospace;font-weight:700;font-size:.82em;line-height:1.2}
  .sig{font-family:"Caveat",cursive;font-size:1.9em;color:#1d3a8a;line-height:1;margin-top:.2em}
  .idnote{font-size:.68em;color:#6f6450;margin-top:1em;line-height:1.45}

  /* beer page */
  .stampbox{position:relative;height:42%;display:grid;place-items:center;margin:.5em 0 .3em}
  .stamp{width:72%;height:auto;mix-blend-mode:multiply;opacity:.88}
  .fields{display:grid;grid-template-columns:1fr 1fr;gap:.25em .9em}
  .fields .full{grid-column:1/-1}
  .fields .v{border-bottom:1px solid var(--line);padding-bottom:.08em;min-height:1.3em}
  .pints{display:flex;gap:.18em;align-items:end}
  .pints svg{width:.95em;height:auto}
  .notes{font-family:"Caveat",cursive;font-size:1.22em;line-height:1.15;color:#1d3a8a;margin-top:.45em}
  .sample{position:absolute;top:44%;left:50%;transform:translate(-50%,-50%) rotate(-24deg);font-family:"Bebas Neue",Impact,sans-serif;font-size:3.4em;letter-spacing:.2em;color:rgba(196,48,43,.16);border:.08em solid rgba(196,48,43,.16);padding:0 .3em;pointer-events:none;white-space:nowrap}
  .await .stamp{opacity:.35}
  .await .fields .v{color:transparent}
  .says .v{font-family:Inter,system-ui,sans-serif;font-weight:400;font-style:italic;font-size:.72em;line-height:1.4;border-bottom:0}
  .unk{color:#a39675;font-style:normal;font-weight:400}
  .stampbox{height:50%}
  .await-msg{text-align:center;font-family:"Caveat",cursive;font-size:1.35em;color:#8a7a58;margin-top:.6em}
  .backin{background:linear-gradient(135deg,var(--burg2),var(--burg));}

  /* controls */
  .controls{display:flex;align-items:center;gap:14px;margin-top:22px;user-select:none}
  .controls button{font:inherit;font-weight:700;border:0;border-radius:999px;padding:.6em 1.2em;background:var(--cream);color:var(--navy);cursor:pointer;transition:background .2s,opacity .2s}
  .controls button:hover:not(:disabled),.controls button:focus-visible{background:var(--yellow)}
  .controls button:focus-visible{outline:3px solid #fff;outline-offset:2px}
  .controls button:disabled{opacity:.35;cursor:default}
  .count{font-family:"Space Mono",monospace;font-size:.9rem;color:var(--muted);min-width:9em;text-align:center}
  .tip{font-size:.8rem;color:var(--muted);margin-top:8px;opacity:.8}
  footer{text-align:center;padding:18px 16px;color:var(--muted);font-size:.85rem}
  @media (max-width:480px){.brand{font-size:1.3rem}.brand svg{width:30px;height:30px}.back{font-size:.8rem}}
  @media (prefers-reduced-motion:reduce){.leaf,.stage{transition:none!important}}
</style>
</head>
<body>
<header>
  <a class="brand" href="/"><svg viewBox="190 157 700 700" aria-hidden="true"><circle cx="540" cy="507" r="345" fill="#f7f2e4"/><path fill="#0a1838" fill-rule="evenodd" d="__GLOBE__"/></svg>Rob Callery</a>
  <a class="back" href="/explore/">← Back to the bar</a>
</header>
<main>
  <h1 class="sr">Rob Callery's Beer Passport</h1>
  <div class="stage closed" id="stage" aria-live="polite">
    <div class="under l"></div><div class="under r"></div><div class="spine"></div>
  </div>
  <div class="controls">
    <button id="prev" aria-label="Previous page">‹ Prev</button>
    <span class="count" id="count">Closed</span>
    <button id="next" aria-label="Next page">Next ›</button>
  </div>
  <p class="tip">Tap a page, swipe, or use the arrow keys to flick through.</p>
</main>
<footer>© <span id="yr">2026</span> Rob Callery · callery.co.uk · Drink responsibly</footer>
<script src="beers.js"></script>
<script>
(function(){
  var GLOBE='__GLOBE__';
  var demo=/[?&]demo\b/.test(location.search);
  var beers=(window.BEERS||[]).slice();
  if(demo&&!beers.length){beers=[
    {name:"Kirkstall Pale",brewery:"Kirkstall Brewery",style:"Pale Ale",abv:4.4,where:"Kirkstall Bridge Inn",city:"Leeds",country:"England",date:"2026-08-16",rating:4,ink:"blue",notes:"Proper session pale before the match. Could've had five."},
    {name:"Victoria Málaga",brewery:"Cervezas Victoria",style:"Lager",abv:4.8,where:"Chiringuito on Malagueta beach",city:"Málaga",country:"Spain",date:"2026-06-02",rating:4,ink:"red",notes:"Ice cold, sun out, espetos on the go. Hard to beat."},
    {name:"Guinness",brewery:"St James's Gate",style:"Stout",abv:4.2,where:"The Gravity Bar",city:"Dublin",country:"Ireland",date:"2025-03-15",rating:5,ink:"green",notes:"Tastes better there. Everyone says it, and everyone's right."}
  ];}
  var INK={red:"#b3262b",blue:"#1d4fb3",green:"#1f7a43",purple:"#6b2fa3",black:"#2b2b33"};
  var inks=["red","blue","green","purple"];
  function esc(t){return String(t==null?'':t).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
  function fmtDate(d){if(!d)return'';var x=new Date(d+'T12:00:00');if(isNaN(x))return esc(d);return x.toLocaleDateString('en-GB',{day:'2-digit',month:'short',year:'numeric'}).toUpperCase()}
  function wm(){return '<div class="wm"><svg viewBox="190 157 700 700"><path fill="#1b2b4d" fill-rule="evenodd" d="'+GLOBE+'"/></svg></div>'}
  function top(label,n){return '<div class="top"><span>'+label+'</span><span class="pno">'+(n<10?'0':'')+n+'</span></div>'}
  function mrz(a,b){var pad=function(s){s=s.toUpperCase().replace(/[^A-Z0-9]+/g,'<');return (s+Array(45).join('<')).slice(0,44).replace(/</g,'&lt;')};return '<div class="mrz">'+pad(a)+'<br>'+pad(b)+'</div>'}
  function pint(full){return '<svg viewBox="0 0 20 28"><path d="M3 4 L17 4 L15 26 L5 26 Z" fill="'+(full?'#e8a317':'none')+'" stroke="#6f6450" stroke-width="1.6" stroke-linejoin="round"/>'+(full?'<path d="M2.5 5 Q4 0 8 2 Q10 -1 13 2 Q17 0 17.5 5 Z" fill="#fff" stroke="#6f6450" stroke-width="1.2"/>':'')+'</svg>'}
  var CINK={England:'blue',Scotland:'blue',Wales:'blue','United Kingdom':'blue',Spain:'red',USA:'purple','United States':'purple',Ireland:'green',Italy:'green',Netherlands:'orange',France:'blue',Japan:'red',Belgium:'black',Germany:'black'};
  INK.orange='#c75a12';
  function hash(t){var h=7;for(var k=0;k<t.length;k++)h=(h*31+t.charCodeAt(k))>>>0;return h}
  function wrap(t){t=t.toUpperCase();if(t.length<=12||t.indexOf(' ')<0)return [t];var w=t.split(' '),best=null;
    for(var k=1;k<w.length;k++){var l1=w.slice(0,k).join(' '),l2=w.slice(k).join(' '),m=Math.max(l1.length,l2.length);if(!best||m<best.m)best={m:m,l:[l1,l2]}}return best.l}
  function stamp(b,i,blank){
    var known=!!b.brewery;
    var c=blank?'#8a7a58':INK[b.ink]||INK[CINK[b.brewedCountry]]||(known?INK[inks[i%4]]:INK.black);
    var h=hash((b.name||'')+i), rot=blank?0:((h%25)-12), id='s'+i, shape=blank?'circle':['circle','rect','oval'][h%3];
    var top=blank?'AWAITING STAMP':esc((b.brewery||'BREWERY UNKNOWN').toUpperCase());
    var bot=blank?'UNITED KINGDOM OF ALES':esc((known&&(b.brewedIn||b.brewedCountry)?[b.brewedIn,b.brewedCountry].filter(Boolean).join(' · '):'UNITED KINGDOM OF ALES').toUpperCase());
    var lines=blank?['?']:wrap(b.name||'').map(esc), ml=Math.max.apply(null,lines.map(function(l){return l.length}));
    var fs=blank?44:ml<=7?30:ml<=10?24:ml<=13?20:17;
    var foot=blank?'':((b.date||b.added)?fmtDate(b.date||b.added):'ADMITTED');
    var fit=function(t,max,per){return t.length*per>max?' textLength="'+max+'" lengthAdjust="spacingAndGlyphs"':''};
    var g='<g fill="'+c+'" stroke="none" font-family="Bebas Neue, Impact, sans-serif">', body='';
    function nameAt(cy,maxW){var lh=fs*1.02,y0=cy-(lines.length-1)*lh/2+fs*.36;return lines.map(function(l,k){return '<text x="110" y="'+(y0+k*lh).toFixed(1)+'" text-anchor="middle" font-size="'+fs+'"'+fit(l,maxW,fs*.5)+'>'+l+'</text>'}).join('')}
    if(shape==='circle'){
      body='<defs><path id="a'+id+'" d="M30 110 A80 80 0 0 1 190 110"/><path id="b'+id+'" d="M22 110 A88 88 0 0 0 198 110"/></defs>'+
        '<circle cx="110" cy="110" r="104" stroke-width="5"/><circle cx="110" cy="110" r="92" stroke-width="2"/><circle cx="110" cy="110" r="60" stroke-width="2"/>'+g+
        '<text font-size="17" letter-spacing="2"><textPath href="#a'+id+'" startOffset="50%" text-anchor="middle"'+fit(top,236,11)+'>'+top+'</textPath></text>'+
        '<text font-size="13" letter-spacing="1.5"><textPath href="#b'+id+'" startOffset="50%" text-anchor="middle" dominant-baseline="hanging"'+fit(bot,250,8.5)+'>'+bot+'</textPath></text>'+
        nameAt(blank?110:100,104)+(foot?'<text x="110" y="148" text-anchor="middle" font-size="12" letter-spacing="2.5">'+foot+'</text>':'')+
        '<text x="20" y="116" font-size="16">★</text><text x="188" y="116" font-size="16">★</text></g>';
    } else if(shape==='rect'){
      body='<rect x="8" y="42" width="204" height="136" rx="10" stroke-width="5"/><rect x="18" y="52" width="184" height="116" rx="5" stroke-width="2"/>'+
        '<line x1="18" y1="76" x2="202" y2="76" stroke-width="2"/><line x1="18" y1="146" x2="202" y2="146" stroke-width="2"/>'+g+
        '<text x="110" y="70" text-anchor="middle" font-size="16" letter-spacing="2"'+fit(top,170,10)+'>'+top+'</text>'+
        nameAt(111,170)+
        '<text x="110" y="163" text-anchor="middle" font-size="12.5" letter-spacing="1.5"'+fit(bot,172,8)+'>'+bot+'</text>'+
        (foot?'<text x="110" y="34" text-anchor="middle" font-size="12" letter-spacing="3">✦ '+foot+' ✦</text>':'')+'</g>';
    } else {
      body='<defs><path id="a'+id+'" d="M20 110 A90 66 0 0 1 200 110"/><path id="b'+id+'" d="M20 110 A90 66 0 0 0 200 110"/></defs>'+
        '<ellipse cx="110" cy="110" rx="106" ry="82" stroke-width="5"/><ellipse cx="110" cy="110" rx="78" ry="56" stroke-width="2"/>'+g+
        '<text font-size="15" letter-spacing="2"><textPath href="#a'+id+'" startOffset="50%" text-anchor="middle"'+fit(top,210,10)+'>'+top+'</textPath></text>'+
        '<text font-size="12" letter-spacing="1.5"><textPath href="#b'+id+'" startOffset="50%" text-anchor="middle" dominant-baseline="hanging"'+fit(bot,230,8)+'>'+bot+'</textPath></text>'+
        nameAt(lines.length>1?97:104,124)+(foot?'<text x="110" y="'+(lines.length>1?146:137)+'" text-anchor="middle" font-size="11.5" letter-spacing="2.5">'+foot+'</text>':'')+'</g>';
    }
    return '<svg class="stamp" viewBox="0 0 220 220" style="transform:rotate('+rot+'deg)">'+
      '<defs><filter id="r'+id+'"><feTurbulence type="fractalNoise" baseFrequency="1.1" numOctaves="2" seed="'+(i+3)+'"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.5 1.4"/><feComposite in="SourceGraphic" operator="in"/></filter></defs>'+
      '<g filter="url(#r'+id+')" fill="none" stroke="'+c+'"'+(blank?' stroke-dasharray="6 5"':'')+'>'+body+'</g></svg>';
  }
  var INSIDE='<div class="ep">'+wm()+'<div class="own"><span>This passport is the property of</span><b>ROB CALLERY</b><span>If found, please return to the nearest pub.</span></div></div>';
  var pages=[];
  pages.push({cls:'cover',html:'<img class="coverimg" src="/beer-passport/cover.webp" alt="Beer Passport cover: a gold coat of arms with two lions holding a pint and a bottle, a crowned pint above a shield of hops, barley, a barrel and waves, and the mottos Good Beer, Good People, Great Places" decoding="async"><div class="hint">tap to open</div>'});
  pages.push({html:wm()+top('PASSPORT · HOLDER',1)+'<div class="idgrid"><div class="photo"><svg viewBox="0 0 100 120"><rect x="38" y="96" width="9" height="24" fill="#0a1838"/><rect x="53" y="96" width="9" height="24" fill="#0a1838"/><rect x="26" y="58" width="48" height="44" rx="14" fill="#ffcd00"/><circle cx="50" cy="36" r="17" fill="#f2b8a6"/></svg></div><div>'+
    '<div class="fld"><div class="k">Surname</div><div class="v">CALLERY</div></div><div class="fld"><div class="k">Given names</div><div class="v">ROB</div></div>'+
    '<div class="fld"><div class="k">Nationality</div><div class="v">LEEDS</div></div><div class="fld"><div class="k">Home ground</div><div class="v">ELLAND ROAD</div></div>'+
    '<div class="fld"><div class="k">Beers stamped</div><div class="v">'+(beers.length<10?'0':'')+beers.length+'</div></div></div></div>'+
    '<p class="idnote">This passport entitles the bearer to try one beer at a time, in every bar, in every city, and to report back honestly.</p>'+mrz('P<LDS CALLERY ROB','ELLAND ROAD MOT 1919')});
  beers.forEach(function(b,i){
    var r=Math.max(0,Math.min(5,Math.round(b.rating||0))),p='';for(var k=0;k<5;k++)p+=pint(k<r);
    var fld=function(k,v,full){return '<div class="fld'+(full?' full':'')+'"><div class="k">'+k+'</div><div class="v'+(k==='Verdict'?' pints':'')+'">'+v+'</div></div>'};
    var loc=[b.brewedIn,b.brewedCountry].filter(Boolean).join(', ');
    var f=fld('Beer',esc(b.name),true)+fld('Brewery',b.brewery?esc(b.brewery):'<i class="unk">Unknown</i>')+fld('Brewed in',loc?esc(loc):'<i class="unk">Unknown</i>');
    if(b.brewerSays) f+='<div class="fld full says"><div class="k">The brewer says</div><div class="v">'+esc(b.brewerSays)+'</div></div>';
    if(b.style||b.abv) f+=fld('Style · ABV',esc(b.style||'')+(b.abv?(b.style?' · ':'')+esc(b.abv)+'%':''),true);
    if(b.where||b.city) f+=fld('Where I had it',esc(b.where||'')+(b.where&&b.city?', ':'')+esc(b.city||''),true);
    if(b.date) f+=fld('Date',fmtDate(b.date));
    else if(b.added) f+=fld('Stamped',fmtDate(b.added));
    if(r) f+=fld('Verdict',p);
    pages.push({html:wm()+top('ENTRY · '+esc((b.brewedCountry||'UNKNOWN').toUpperCase()),i+2)+'<div class="stampbox">'+stamp(b,i,false)+'</div>'+
      '<div class="fields">'+f+'</div>'+(b.notes?'<div class="notes">“'+esc(b.notes)+'”</div>':'')+
      (demo&&!(window.BEERS||[]).length?'<div class="sample">SAMPLE</div>':'')+mrz('V<'+(b.name||''),(b.brewery||'')+' '+(b.brewedIn||''))});
  });
  pages.push({cls:'await',html:wm()+top('ENTRY · PENDING',beers.length+2)+'<div class="stampbox">'+stamp({},beers.length,true)+'</div>'+
    '<div class="fields"><div class="fld full"><div class="k">Beer</div><div class="v">-</div></div><div class="fld"><div class="k">Brewery</div><div class="v">-</div></div><div class="fld"><div class="k">Style · ABV</div><div class="v">-</div></div><div class="fld full"><div class="k">Where</div><div class="v">-</div></div></div>'+
    '<div class="await-msg">'+(beers.length?'Next stamp coming soon…':'The first stamps are being collected.<br>Check back soon!')+'</div>'+mrz('V<PENDING','')});

  var stage=document.getElementById('stage'), leaves=[], cur=0, single=false, lastBack=false;
  function maxCur(){return single?leaves.length-1:(lastBack?leaves.length:leaves.length-1)}
  function face(p,side){return '<div class="face '+side+'"><div class="page '+(p&&p.cls||'')+'">'+(p?p.html:wm())+'</div></div>'}
  function build(){
    single=matchMedia('(max-width:760px)').matches;
    stage.classList.toggle('single',single);
    leaves.forEach(function(l){l.remove()}); leaves=[];
    var list=pages.slice();
    if(!single) list.splice(1,0,{cls:'inside',html:INSIDE});
    lastBack=false; if(!single){ if(list.length%2) list.push({cls:'',html:wm()}); else lastBack=true; }
    var step=single?1:2;
    for(var i=0;i<list.length;i+=step){
      var l=document.createElement('div'); l.className='leaf';
      l.innerHTML=face(list[i],'f')+face(single?null:list[i+1],'b');
      (function(idx){l.addEventListener('click',function(){ if(idx<cur) go(cur-1); else go(cur+1); });})(leaves.length);
      stage.appendChild(l); leaves.push(l);
    }
    cur=Math.min(cur,maxCur()); layout(-1);
  }
  function layout(moving){
    var N=leaves.length;
    leaves.forEach(function(l,i){
      l.classList.toggle('flipped',i<cur);
      l.style.zIndex=(i===moving)?3*N:(i<cur?i+1:2*N-i);
    });
    stage.classList.toggle('closed',cur===0);
    var maxC=maxCur();
    document.getElementById('prev').disabled=cur===0;
    document.getElementById('next').disabled=cur>=maxC;
    var label;
    if(cur===0) label='Closed';
    else if(single){ label=cur===1?'Holder page':(cur-1<=beers.length?'Beer '+(cur-1)+' of '+beers.length:'Next stamp'); if(cur>=N-1&&cur-1>beers.length) label='Next stamp'; }
    else { var a=2*cur-2; label=cur===1?'Holder page':(cur===N?'Page '+a:'Pages '+a+'–'+(a+1)); }
    document.getElementById('count').textContent=label;
    if(moving>=0) setTimeout(function(){layout(-1)},1000);
  }
  function go(n){
    n=Math.max(0,Math.min(maxCur(),n)); if(n===cur) return;
    var moving=n>cur?cur:n; cur=n; layout(moving);
  }
  document.getElementById('prev').onclick=function(){go(cur-1)};
  document.getElementById('next').onclick=function(){go(cur+1)};
  addEventListener('keydown',function(e){if(e.key==='ArrowRight')go(cur+1);else if(e.key==='ArrowLeft')go(cur-1)});
  var sx=null; stage.addEventListener('touchstart',function(e){sx=e.touches[0].clientX},{passive:true});
  stage.addEventListener('touchend',function(e){if(sx==null)return;var dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>40){go(cur+(dx<0?1:-1));e.preventDefault()}sx=null});
  var mq=matchMedia('(max-width:760px)'); (mq.addEventListener?mq.addEventListener('change',build):mq.addListener(build));
  build();
  var startAt=parseInt((location.search.match(/[?&]page=(\d+)/)||[])[1]||'1',10);
  setTimeout(function(){go(startAt)},450);
  document.getElementById('yr').textContent=new Date().getFullYear();
})();
</script>
</body>
</html>
'''
os.makedirs('/home/claude/site/beer-passport', exist_ok=True)
open('/home/claude/site/beer-passport/index.html', 'w').write(PAGE.replace('__GLOBE__', globe))
bj = '/home/claude/site/beer-passport/beers.js'
if not os.path.exists(bj):
    open(bj, 'w').write(BEERS_JS)
print('passport built')
