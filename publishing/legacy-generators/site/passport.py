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
  .stage{--pw:min(420px,31vw,calc((100vh - 215px)*.7));--ph:calc(var(--pw)/.7);perspective:2400px;width:calc(var(--pw)*2);height:var(--ph);position:relative;transition:transform .9s cubic-bezier(.3,.7,.2,1)}
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
  .leaf.off{display:none}
  .face{position:absolute;inset:0;backface-visibility:hidden;-webkit-backface-visibility:hidden;overflow:hidden}
  .face.b{transform:rotateY(180deg)}
  .face::after{content:"";position:absolute;inset:0;pointer-events:none}
  .face.f::after{background:linear-gradient(90deg,rgba(0,0,0,.14),rgba(0,0,0,0) 9%)}
  .face.b::after{background:linear-gradient(270deg,rgba(0,0,0,.14),rgba(0,0,0,0) 9%)}
  .face.f{border-radius:0 8px 8px 0}.face.b{border-radius:8px 0 0 8px}

  /* single page on phones */
  .stage.single{--pw:min(88vw,calc((100vh - 330px)*.7),420px);width:var(--pw)}
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

  body.table{background:#2a170b;position:relative}
  body.table::before{content:"";position:fixed;inset:0;z-index:-2;
    background:
      radial-gradient(ellipse 55% 50% at 50% 48%,rgba(255,196,110,.20),transparent 70%),
      repeating-linear-gradient(90deg,rgba(0,0,0,.0) 0 196px,rgba(20,8,2,.75) 196px 199px,rgba(255,220,170,.08) 199px 200px),
      repeating-linear-gradient(90deg,rgba(0,0,0,.06) 0 2px,transparent 2px 7px,rgba(255,255,255,.025) 7px 9px,transparent 9px 23px),
      repeating-linear-gradient(92deg,transparent 0 40px,rgba(0,0,0,.05) 40px 44px,transparent 44px 97px),
      linear-gradient(90deg,#6b4022,#5a341a 30%,#6e4426 55%,#55311a 80%,#664026)}
  body.table::after{content:"";position:fixed;inset:0;z-index:-1;pointer-events:none;
    background:radial-gradient(ellipse 80% 75% at 50% 50%,transparent 45%,rgba(10,4,0,.6) 100%),linear-gradient(rgba(10,4,0,.55),transparent 120px)}
  body.table main{position:relative;padding:0 16px 10px;overflow-x:clip}
  .tablewrap{display:grid;grid-template-columns:1fr auto 1fr;grid-template-rows:1fr 1fr auto auto;grid-template-areas:"prev stage pint" "prev stage next" ". slip ." ". tip .";align-items:center;justify-items:center;column-gap:clamp(16px,3vw,56px);width:100%}
  .tablewrap>.stage{grid-area:stage}
  #prev{grid-area:prev;--r:-9deg;align-self:center}
  #next{grid-area:next;--r:8deg;align-self:start}
  .pint{grid-area:pint;align-self:end;margin-bottom:10px}
  .slip{grid-area:slip}
  .tablewrap>.tip{grid-area:tip}
  .pack{appearance:none;border:0;background:none;padding:0;cursor:pointer;width:clamp(110px,11vw,165px);display:block;transform:rotate(var(--r));transition:transform .25s ease,opacity .3s}
  .pack svg{width:100%;height:auto;display:block}
  .pack:hover:not(:disabled),.pack:focus-visible{transform:rotate(0) translateY(-6px) scale(1.05)}
  .pack:focus-visible{outline:3px solid #fff;outline-offset:6px;border-radius:8px}
  .pack:disabled{cursor:default;opacity:.4}
  .pint{width:clamp(130px,14vw,210px);transform:rotate(-12deg);pointer-events:none}
  .pint svg{width:100%;height:auto;display:block}
  .ring{position:absolute;border-radius:50%;border:3px solid rgba(30,12,2,.35);box-shadow:0 0 0 1px rgba(255,220,170,.06);pointer-events:none}
  .slip{display:inline-block;margin-top:clamp(10px,2vh,18px);background:#fbf7ec;color:#2a2a35;font-family:"Space Mono",monospace;font-size:.82rem;padding:.45em 1.1em .5em;transform:rotate(-1.5deg);box-shadow:0 6px 10px rgba(0,0,0,.45);clip-path:polygon(0 0,100% 0,100% 100%,96% 88%,92% 100%,88% 88%,84% 100%,80% 88%,76% 100%,72% 88%,68% 100%,64% 88%,60% 100%,56% 88%,52% 100%,48% 88%,44% 100%,40% 88%,36% 100%,32% 88%,28% 100%,24% 88%,20% 100%,16% 88%,12% 100%,8% 88%,4% 100%,0 88%)}
  .slip .count{color:#2a2a35;min-width:9em;display:inline-block;font-size:inherit}
  body.table .tip{color:#e9d9bd;opacity:.75}
  body.table footer{color:#d8c7a8;background:rgba(15,6,0,.55)}
  @media (max-width:1000px){
    .tablewrap{grid-template-columns:1fr auto 1fr;grid-template-rows:auto auto auto;grid-template-areas:"stage stage stage" "prev slip next" "tip tip tip";row-gap:10px;position:relative}
    #prev,#next{align-self:center;width:clamp(84px,24vw,124px)}
    #prev{justify-self:end}#next{justify-self:start}
    .slip{align-self:center;margin-top:0}
    .pint{position:absolute;right:-46px;top:-26px;width:150px;margin:0;z-index:0}
    .tablewrap>.stage{z-index:1}
    .stage:not(.single){--pw:min(40vw,calc((100vh - 370px)*.7))}
  }
  @media (prefers-reduced-motion:reduce){.leaf,.stage,.pack{transition:none!important}}
</style>
</head>
<body class="table">
<header>
  <a class="brand" href="/"><svg viewBox="190 157 700 700" aria-hidden="true"><circle cx="540" cy="507" r="345" fill="#f7f2e4"/><path fill="#0a1838" fill-rule="evenodd" d="__GLOBE__"/></svg>Rob Callery</a>
  <a class="back" href="/explore/">← Back to the bar</a>
</header>
<main>
  <h1 class="sr">Rob Callery's Beer Passport</h1>
  <div class="tablewrap">
  <div class="stage closed" id="stage" aria-live="polite">
    <div class="under l"></div><div class="under r"></div><div class="spine"></div>
  </div>
  <button class="pack" id="prev" aria-label="Previous page"><svg viewBox="-6 0 172 228" aria-hidden="true" focusable="false"><path d="M10 26 Q6 117 10 210 L166 210 Q170 117 166 26 Z" fill="#000" opacity=".35"/><defs><linearGradient id="pkprev" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8c2f1c"/><stop offset="1" stop-color="#5e1b10"/></linearGradient><linearGradient id="pkprevs" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".28"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs><path d="M6 14 Q2 107 6 200 L154 200 Q158 107 154 14 Z" fill="url(#pkprev)"/><path d="M0 6 L0.0,0.0 L10.0,6.0 L20.0,0.0 L30.0,6.0 L40.0,0.0 L50.0,6.0 L60.0,0.0 L70.0,6.0 L80.0,0.0 L90.0,6.0 L100.0,0.0 L110.0,6.0 L120.0,0.0 L130.0,6.0 L140.0,0.0 L150.0,6.0 L160.0,0.0 L160 18 L0 18 Z" fill="#5e1b10"/><g stroke="#000" stroke-opacity=".18" stroke-width="1"><line x1="5" y1="6" x2="5" y2="18"/><line x1="10" y1="6" x2="10" y2="18"/><line x1="15" y1="6" x2="15" y2="18"/><line x1="20" y1="6" x2="20" y2="18"/><line x1="25" y1="6" x2="25" y2="18"/><line x1="30" y1="6" x2="30" y2="18"/><line x1="35" y1="6" x2="35" y2="18"/><line x1="40" y1="6" x2="40" y2="18"/><line x1="45" y1="6" x2="45" y2="18"/><line x1="50" y1="6" x2="50" y2="18"/><line x1="55" y1="6" x2="55" y2="18"/><line x1="60" y1="6" x2="60" y2="18"/><line x1="65" y1="6" x2="65" y2="18"/><line x1="70" y1="6" x2="70" y2="18"/><line x1="75" y1="6" x2="75" y2="18"/><line x1="80" y1="6" x2="80" y2="18"/><line x1="85" y1="6" x2="85" y2="18"/><line x1="90" y1="6" x2="90" y2="18"/><line x1="95" y1="6" x2="95" y2="18"/><line x1="100" y1="6" x2="100" y2="18"/><line x1="105" y1="6" x2="105" y2="18"/><line x1="110" y1="6" x2="110" y2="18"/><line x1="115" y1="6" x2="115" y2="18"/><line x1="120" y1="6" x2="120" y2="18"/><line x1="125" y1="6" x2="125" y2="18"/><line x1="130" y1="6" x2="130" y2="18"/><line x1="135" y1="6" x2="135" y2="18"/><line x1="140" y1="6" x2="140" y2="18"/><line x1="145" y1="6" x2="145" y2="18"/><line x1="150" y1="6" x2="150" y2="18"/><line x1="155" y1="6" x2="155" y2="18"/></g><path d="M0 196 L160 196 L160 208 L0.0,208.0 L10.0,214.0 L20.0,208.0 L30.0,214.0 L40.0,208.0 L50.0,214.0 L60.0,208.0 L70.0,214.0 L80.0,208.0 L90.0,214.0 L100.0,208.0 L110.0,214.0 L120.0,208.0 L130.0,214.0 L140.0,208.0 L150.0,214.0 L160.0,208.0 Z" fill="#5e1b10"/><g stroke="#000" stroke-opacity=".18" stroke-width="1"><line x1="5" y1="196" x2="5" y2="208"/><line x1="10" y1="196" x2="10" y2="208"/><line x1="15" y1="196" x2="15" y2="208"/><line x1="20" y1="196" x2="20" y2="208"/><line x1="25" y1="196" x2="25" y2="208"/><line x1="30" y1="196" x2="30" y2="208"/><line x1="35" y1="196" x2="35" y2="208"/><line x1="40" y1="196" x2="40" y2="208"/><line x1="45" y1="196" x2="45" y2="208"/><line x1="50" y1="196" x2="50" y2="208"/><line x1="55" y1="196" x2="55" y2="208"/><line x1="60" y1="196" x2="60" y2="208"/><line x1="65" y1="196" x2="65" y2="208"/><line x1="70" y1="196" x2="70" y2="208"/><line x1="75" y1="196" x2="75" y2="208"/><line x1="80" y1="196" x2="80" y2="208"/><line x1="85" y1="196" x2="85" y2="208"/><line x1="90" y1="196" x2="90" y2="208"/><line x1="95" y1="196" x2="95" y2="208"/><line x1="100" y1="196" x2="100" y2="208"/><line x1="105" y1="196" x2="105" y2="208"/><line x1="110" y1="196" x2="110" y2="208"/><line x1="115" y1="196" x2="115" y2="208"/><line x1="120" y1="196" x2="120" y2="208"/><line x1="125" y1="196" x2="125" y2="208"/><line x1="130" y1="196" x2="130" y2="208"/><line x1="135" y1="196" x2="135" y2="208"/><line x1="140" y1="196" x2="140" y2="208"/><line x1="145" y1="196" x2="145" y2="208"/><line x1="150" y1="196" x2="150" y2="208"/><line x1="155" y1="196" x2="155" y2="208"/></g><text x="80" y="38" text-anchor="middle" font-family="Caveat, cursive" font-weight="700" font-size="19" fill="#ffcd00">Callery's</text><text x="80" y="62" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="22" fill="#fff3d6" letter-spacing="1" textLength="60" lengthAdjust="spacingAndGlyphs">PORK</text><text x="80" y="84" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="22" fill="#fff3d6" letter-spacing="1" textLength="120" lengthAdjust="spacingAndGlyphs">SCRATCHINGS</text><ellipse cx="80" cy="122" rx="52" ry="26" fill="#f7e7c2" opacity=".95"/><polygon points="48.8,111.0 47.9,113.9 42.9,115.0 37.8,113.9 37.0,111.0 36.7,108.0 42.9,105.4 49.5,107.1" fill="#b57430" stroke="#7a4518" stroke-width=".8"/><polygon points="56.2,112.4 55.6,116.2 50.3,118.0 46.2,116.2 44.2,112.4 44.6,108.7 50.3,107.3 55.5,108.3" fill="#b57430" stroke="#7a4518" stroke-width=".8"/><polygon points="70.1,117.1 66.5,120.4 62.5,122.6 57.3,119.9 54.3,117.1 58.1,113.4 62.5,112.5 66.0,113.5" fill="#d9a35a" stroke="#7a4518" stroke-width=".8"/><polygon points="78.7,125.5 76.3,128.7 71.4,131.2 66.8,129.1 66.4,125.5 66.4,121.4 71.4,121.4 75.8,122.0" fill="#c98a3e" stroke="#7a4518" stroke-width=".8"/><polygon points="90.1,115.1 87.3,119.3 82.6,121.5 77.4,118.1 75.6,115.1 78.4,111.6 82.6,109.3 89.3,111.1" fill="#b57430" stroke="#7a4518" stroke-width=".8"/><polygon points="97.1,111.0 96.1,114.2 91.7,114.2 87.5,113.9 85.3,111.0 86.9,107.9 91.7,106.3 95.1,107.3" fill="#d9a35a" stroke="#7a4518" stroke-width=".8"/><polygon points="105.2,115.8 103.5,118.5 99.8,119.8 95.4,118.4 94.7,115.8 96.0,112.7 99.8,110.1 104.9,113.1" fill="#b57430" stroke="#7a4518" stroke-width=".8"/><polygon points="115.4,120.0 116.0,123.5 109.7,124.1 104.1,124.0 102.8,120.0 104.7,117.1 109.7,115.5 115.2,115.8" fill="#d9a35a" stroke="#7a4518" stroke-width=".8"/><polygon points="121.8,120.9 119.9,123.6 114.8,125.1 110.6,124.0 108.5,120.9 110.0,118.4 114.8,116.9 119.7,118.4" fill="#b57430" stroke="#7a4518" stroke-width=".8"/><g transform="rotate(-4 80 168)"><rect x="18" y="152" width="124" height="32" rx="5" fill="#ffcd00"/><text x="80" y="177" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="27" fill="#14213f" letter-spacing="1">‹ BACK</text></g><text x="80" y="193" text-anchor="middle" font-family="Inter, sans-serif" font-size="7" fill="#fff3d6" opacity=".75" letter-spacing="1">PROPER PUB SNACK · 30g</text><path d="M30 18 L22 196 L44 196 L50 18 Z" fill="url(#pkprevs)" opacity=".8"/><path d="M118 18 L112 196 L122 196 L128 18 Z" fill="url(#pkprevs)" opacity=".5"/></svg></button>
  <div class="pint"><svg viewBox="0 0 260 260" aria-hidden="true" focusable="false"><defs><radialGradient id="foam" cx=".45" cy=".42" r=".6"><stop offset="0" stop-color="#fffaf0"/><stop offset=".7" stop-color="#f3e3c3"/><stop offset="1" stop-color="#d9b77e"/></radialGradient><radialGradient id="glassRim" cx=".5" cy=".5" r=".5"><stop offset=".82" stop-color="#fff" stop-opacity="0"/><stop offset=".92" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#fff" stop-opacity=".12"/></radialGradient><radialGradient id="ale" cx=".5" cy=".5" r=".5"><stop offset=".7" stop-color="#c77a12"/><stop offset="1" stop-color="#8a4a08"/></radialGradient></defs><circle cx="130" cy="134" r="124" fill="#000" opacity=".28"/><circle cx="128" cy="128" r="122" fill="#f4ead2"/><circle cx="128" cy="128" r="112" fill="none" stroke="#b3262b" stroke-width="7"/><path id="matArc" d="M40 128 A88 88 0 0 1 216 128" fill="none"/><text font-family="Bebas Neue, Impact, sans-serif" font-size="17" fill="#b3262b" letter-spacing="3"><textPath href="#matArc" startOffset="50%" text-anchor="middle">ONE BEER AT A TIME</textPath></text><path id="matArc2" d="M24 128 A104 104 0 0 0 232 128" fill="none"/><text font-family="Bebas Neue, Impact, sans-serif" font-size="14" fill="#0a1838" letter-spacing="4"><textPath href="#matArc2" startOffset="50%" text-anchor="middle">CALLERY.CO.UK</textPath></text><circle cx="136" cy="136" r="66" fill="#000" opacity=".22"/><circle cx="128" cy="128" r="66" fill="url(#ale)"/><circle cx="128" cy="128" r="59" fill="url(#foam)"/><circle cx="130.2" cy="157.3" r="1.9" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="101.2" cy="107.5" r="1.2" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="173.1" cy="131.7" r="1.6" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="133.3" cy="181.5" r="2.1" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="141.3" cy="106.0" r="2.5" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="148.0" cy="155.8" r="3.1" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="88.4" cy="122.2" r="2.6" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="165.7" cy="144.0" r="2.4" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="127.5" cy="129.6" r="3.1" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="89.8" cy="134.6" r="3.1" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="116.9" cy="79.5" r="1.9" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="135.5" cy="105.2" r="3.2" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="131.8" cy="124.4" r="1.3" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="138.7" cy="179.0" r="2.0" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="116.6" cy="116.4" r="2.2" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="113.7" cy="140.5" r="2.4" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="85.9" cy="103.3" r="2.6" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="169.7" cy="108.0" r="3.4" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="123.8" cy="120.2" r="3.1" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="175.7" cy="117.2" r="2.4" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="125.4" cy="116.9" r="3.0" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="114.2" cy="121.1" r="1.2" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="160.5" cy="85.5" r="1.2" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="134.9" cy="106.9" r="1.4" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="116.7" cy="167.9" r="3.1" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="159.9" cy="137.1" r="1.1" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="124.5" cy="110.5" r="3.1" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="155.1" cy="124.7" r="3.4" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="126.5" cy="131.9" r="2.4" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="138.5" cy="130.1" r="2.0" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="121.5" cy="122.6" r="1.1" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="139.4" cy="115.5" r="3.3" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="144.2" cy="115.7" r="2.1" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="93.5" cy="123.6" r="2.4" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="96.8" cy="115.8" r="3.3" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="104.7" cy="127.0" r="2.7" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="129.3" cy="144.2" r="3.3" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="98.6" cy="124.1" r="1.0" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="101.0" cy="143.9" r="1.0" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="102.5" cy="105.3" r="1.1" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="110.5" cy="109.9" r="2.6" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="105.1" cy="158.5" r="2.8" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="131.2" cy="128.5" r="2.6" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="141.2" cy="124.9" r="2.1" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="113.6" cy="118.5" r="1.9" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="120.4" cy="146.4" r="2.4" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="121.7" cy="147.4" r="2.9" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="158.3" cy="133.2" r="2.8" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="123.6" cy="139.2" r="2.9" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="128.7" cy="138.1" r="2.0" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="126.2" cy="122.8" r="1.8" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="105.4" cy="166.9" r="2.1" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="133.6" cy="120.8" r="1.8" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="100.0" cy="89.3" r="2.1" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="129.0" cy="134.4" r="2.3" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="143.8" cy="168.6" r="3.0" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="134.1" cy="141.8" r="2.9" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="100.7" cy="94.1" r="1.8" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="138.8" cy="139.5" r="2.9" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="125.5" cy="146.5" r="2.0" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/><circle cx="128" cy="128" r="68" fill="url(#glassRim)"/><circle cx="128" cy="128" r="68" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="2"/><path d="M80 98 A57 57 0 0 1 114 72" fill="none" stroke="#fff" stroke-opacity=".8" stroke-width="4" stroke-linecap="round"/><ellipse cx="62.1" cy="164.4" rx="3.3" ry="1.7" fill="#fff" opacity=".35"/><ellipse cx="207.5" cy="130.3" rx="3.3" ry="3.0" fill="#fff" opacity=".35"/><ellipse cx="55.1" cy="159.9" rx="3.4" ry="1.8" fill="#fff" opacity=".35"/><ellipse cx="125.8" cy="49.3" rx="2.8" ry="2.3" fill="#fff" opacity=".35"/><ellipse cx="109.9" cy="200.5" rx="2.0" ry="1.6" fill="#fff" opacity=".35"/><ellipse cx="64.9" cy="88.7" rx="3.1" ry="1.6" fill="#fff" opacity=".35"/><ellipse cx="191.8" cy="83.9" rx="3.3" ry="2.8" fill="#fff" opacity=".35"/><ellipse cx="189.9" cy="82.8" rx="1.5" ry="2.6" fill="#fff" opacity=".35"/><ellipse cx="163.1" cy="193.6" rx="2.8" ry="2.3" fill="#fff" opacity=".35"/><ellipse cx="59.9" cy="169.0" rx="2.7" ry="2.0" fill="#fff" opacity=".35"/></svg></div>
  <button class="pack" id="next" aria-label="Next page"><svg viewBox="-6 0 172 228" aria-hidden="true" focusable="false"><path d="M10 26 Q6 117 10 210 L166 210 Q170 117 166 26 Z" fill="#000" opacity=".35"/><defs><linearGradient id="pknext" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1f4fb8"/><stop offset="1" stop-color="#12306f"/></linearGradient><linearGradient id="pknexts" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".28"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs><path d="M6 14 Q2 107 6 200 L154 200 Q158 107 154 14 Z" fill="url(#pknext)"/><path d="M0 6 L0.0,0.0 L10.0,6.0 L20.0,0.0 L30.0,6.0 L40.0,0.0 L50.0,6.0 L60.0,0.0 L70.0,6.0 L80.0,0.0 L90.0,6.0 L100.0,0.0 L110.0,6.0 L120.0,0.0 L130.0,6.0 L140.0,0.0 L150.0,6.0 L160.0,0.0 L160 18 L0 18 Z" fill="#12306f"/><g stroke="#000" stroke-opacity=".18" stroke-width="1"><line x1="5" y1="6" x2="5" y2="18"/><line x1="10" y1="6" x2="10" y2="18"/><line x1="15" y1="6" x2="15" y2="18"/><line x1="20" y1="6" x2="20" y2="18"/><line x1="25" y1="6" x2="25" y2="18"/><line x1="30" y1="6" x2="30" y2="18"/><line x1="35" y1="6" x2="35" y2="18"/><line x1="40" y1="6" x2="40" y2="18"/><line x1="45" y1="6" x2="45" y2="18"/><line x1="50" y1="6" x2="50" y2="18"/><line x1="55" y1="6" x2="55" y2="18"/><line x1="60" y1="6" x2="60" y2="18"/><line x1="65" y1="6" x2="65" y2="18"/><line x1="70" y1="6" x2="70" y2="18"/><line x1="75" y1="6" x2="75" y2="18"/><line x1="80" y1="6" x2="80" y2="18"/><line x1="85" y1="6" x2="85" y2="18"/><line x1="90" y1="6" x2="90" y2="18"/><line x1="95" y1="6" x2="95" y2="18"/><line x1="100" y1="6" x2="100" y2="18"/><line x1="105" y1="6" x2="105" y2="18"/><line x1="110" y1="6" x2="110" y2="18"/><line x1="115" y1="6" x2="115" y2="18"/><line x1="120" y1="6" x2="120" y2="18"/><line x1="125" y1="6" x2="125" y2="18"/><line x1="130" y1="6" x2="130" y2="18"/><line x1="135" y1="6" x2="135" y2="18"/><line x1="140" y1="6" x2="140" y2="18"/><line x1="145" y1="6" x2="145" y2="18"/><line x1="150" y1="6" x2="150" y2="18"/><line x1="155" y1="6" x2="155" y2="18"/></g><path d="M0 196 L160 196 L160 208 L0.0,208.0 L10.0,214.0 L20.0,208.0 L30.0,214.0 L40.0,208.0 L50.0,214.0 L60.0,208.0 L70.0,214.0 L80.0,208.0 L90.0,214.0 L100.0,208.0 L110.0,214.0 L120.0,208.0 L130.0,214.0 L140.0,208.0 L150.0,214.0 L160.0,208.0 Z" fill="#12306f"/><g stroke="#000" stroke-opacity=".18" stroke-width="1"><line x1="5" y1="196" x2="5" y2="208"/><line x1="10" y1="196" x2="10" y2="208"/><line x1="15" y1="196" x2="15" y2="208"/><line x1="20" y1="196" x2="20" y2="208"/><line x1="25" y1="196" x2="25" y2="208"/><line x1="30" y1="196" x2="30" y2="208"/><line x1="35" y1="196" x2="35" y2="208"/><line x1="40" y1="196" x2="40" y2="208"/><line x1="45" y1="196" x2="45" y2="208"/><line x1="50" y1="196" x2="50" y2="208"/><line x1="55" y1="196" x2="55" y2="208"/><line x1="60" y1="196" x2="60" y2="208"/><line x1="65" y1="196" x2="65" y2="208"/><line x1="70" y1="196" x2="70" y2="208"/><line x1="75" y1="196" x2="75" y2="208"/><line x1="80" y1="196" x2="80" y2="208"/><line x1="85" y1="196" x2="85" y2="208"/><line x1="90" y1="196" x2="90" y2="208"/><line x1="95" y1="196" x2="95" y2="208"/><line x1="100" y1="196" x2="100" y2="208"/><line x1="105" y1="196" x2="105" y2="208"/><line x1="110" y1="196" x2="110" y2="208"/><line x1="115" y1="196" x2="115" y2="208"/><line x1="120" y1="196" x2="120" y2="208"/><line x1="125" y1="196" x2="125" y2="208"/><line x1="130" y1="196" x2="130" y2="208"/><line x1="135" y1="196" x2="135" y2="208"/><line x1="140" y1="196" x2="140" y2="208"/><line x1="145" y1="196" x2="145" y2="208"/><line x1="150" y1="196" x2="150" y2="208"/><line x1="155" y1="196" x2="155" y2="208"/></g><text x="80" y="38" text-anchor="middle" font-family="Caveat, cursive" font-weight="700" font-size="19" fill="#ffcd00">Callery's</text><text x="80" y="62" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="17" fill="#ffffff" letter-spacing="1" textLength="112" lengthAdjust="spacingAndGlyphs">CHEESE &amp; ONION</text><text x="80" y="84" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="22" fill="#ffffff" letter-spacing="1" textLength="72" lengthAdjust="spacingAndGlyphs">CRISPS</text><ellipse cx="80" cy="122" rx="52" ry="26" fill="#f7e7c2" opacity=".95"/><ellipse cx="41.8" cy="121.1" rx="11" ry="7" transform="rotate(34 41.8 121.1)" fill="#f5d76e" stroke="#c99a26" stroke-width=".8"/><ellipse cx="52.3" cy="126.4" rx="11" ry="7" transform="rotate(-25 52.3 126.4)" fill="#e8b93a" stroke="#c99a26" stroke-width=".8"/><ellipse cx="62.9" cy="122.1" rx="11" ry="7" transform="rotate(-25 62.9 122.1)" fill="#f5d76e" stroke="#c99a26" stroke-width=".8"/><ellipse cx="72.7" cy="112.6" rx="11" ry="7" transform="rotate(25 72.7 112.6)" fill="#e8b93a" stroke="#c99a26" stroke-width=".8"/><ellipse cx="84.5" cy="121.7" rx="11" ry="7" transform="rotate(-8 84.5 121.7)" fill="#f5d76e" stroke="#c99a26" stroke-width=".8"/><ellipse cx="95.1" cy="122.1" rx="11" ry="7" transform="rotate(-27 95.1 122.1)" fill="#f2c94c" stroke="#c99a26" stroke-width=".8"/><ellipse cx="106.3" cy="112.1" rx="11" ry="7" transform="rotate(-37 106.3 112.1)" fill="#f2c94c" stroke="#c99a26" stroke-width=".8"/><ellipse cx="115.9" cy="125.0" rx="11" ry="7" transform="rotate(-14 115.9 125.0)" fill="#e8b93a" stroke="#c99a26" stroke-width=".8"/><g transform="rotate(-4 80 168)"><rect x="18" y="152" width="124" height="32" rx="5" fill="#ffcd00"/><text x="80" y="177" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="27" fill="#14213f" letter-spacing="1">NEXT ›</text></g><text x="80" y="193" text-anchor="middle" font-family="Inter, sans-serif" font-size="7" fill="#ffffff" opacity=".75" letter-spacing="1">READY TO TURN · 25g</text><path d="M30 18 L22 196 L44 196 L50 18 Z" fill="url(#pknexts)" opacity=".8"/><path d="M118 18 L112 196 L122 196 L128 18 Z" fill="url(#pknexts)" opacity=".5"/></svg></button>
  <div class="slip"><span class="count" id="count">Closed</span></div>
  <p class="tip">Tap a page, swipe, use the arrow keys, or grab a packet.</p>
  </div>
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
      var l=document.createElement('div'); l.className='leaf off';
      l._f=list[i]; l._b=single?null:list[i+1]; l._built=false;
      (function(idx){l.addEventListener('click',function(){ if(idx<cur) go(cur-1); else go(cur+1); });})(leaves.length);
      stage.appendChild(l); leaves.push(l);
    }
    cur=Math.min(cur,maxCur()); layout(-1);
  }
  // only the few leaves around the open page exist and render; the rest stay empty and hidden
  function fill(l,on){
    if(on&&!l._built){l.innerHTML=face(l._f,'f')+face(l._b,'b');l._built=true}
    else if(!on&&l._built){l.innerHTML='';l._built=false}
  }
  function layout(moving){
    var N=leaves.length;
    leaves.forEach(function(l,i){
      var near=(i>=cur-2&&i<=cur+1)||i===moving;
      fill(l,(i>=cur-4&&i<=cur+3)||i===moving);
      l.classList.toggle('off',!near);
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
