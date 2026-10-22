import re, json, random, math, subprocess, sys
sys.path.insert(0, '/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad')
from shelves import SHELVES, SHELF_JSON, SHELF_OF_JS

fav = open('/home/claude/favicon.svg').read()
globe = re.search(r'<path fill="#f7f7f2" fill-rule="evenodd" d="([^"]+)"', fav).group(1)
counts = json.loads(subprocess.run(['node', '-e', "global.window={};require('/home/claude/site/travel-guides/guides.js');" + SHELF_OF_JS +
    ";const c={};window.GUIDES.forEach(g=>{const s=shelfOf(g);c[s]=(c[s]||0)+1});process.stdout.write(JSON.stringify(c))"], capture_output=True, text=True).stdout)

def view():
    rnd = random.Random(5)
    g = ['<svg class="view" viewBox="0 0 600 720" preserveAspectRatio="xMidYMid slice" role="img" aria-label="The view from the window: Muelle Uno in Málaga, with the harbour, the palm-lined promenade, the coloured glass cube, La Farola lighthouse and the castle on the hill">',
         '<defs><linearGradient id="vsky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5fb2e6"/><stop offset=".55" stop-color="#a9d9f2"/><stop offset="1" stop-color="#fbe6bf"/></linearGradient>',
         '<linearGradient id="vsea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2b7fb8"/><stop offset="1" stop-color="#1b5f93"/></linearGradient>',
         '<radialGradient id="vsun" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#fffbe6"/><stop offset=".45" stop-color="#fff1b8" stop-opacity=".9"/><stop offset="1" stop-color="#fff1b8" stop-opacity="0"/></radialGradient></defs>']
    a = g.append
    a('<rect width="600" height="720" fill="url(#vsky)"/>')
    a('<circle cx="470" cy="120" r="90" fill="url(#vsun)"/><circle cx="470" cy="120" r="30" fill="#fffbe9"/>')
    for x, y, s in ((90, 90, 1), (300, 60, .8), (560, 200, .7)):
        a(f'<g fill="#fff" opacity=".85" transform="translate({x} {y}) scale({s})"><ellipse cx="0" cy="0" rx="46" ry="14"/><ellipse cx="-20" cy="-8" rx="22" ry="14"/><ellipse cx="16" cy="-12" rx="26" ry="17"/></g>')
    # far mountains
    a('<path d="M0 330 L60 300 L130 318 L210 286 L300 312 L380 290 L460 316 L540 296 L600 310 L600 400 L0 400 Z" fill="#a7bccb"/>')
    # city: white blocks + cathedral tower
    x = 150
    while x < 600:
        w = rnd.randint(16, 34); h = rnd.randint(18, 46)
        a(f'<rect x="{x}" y="{392-h}" width="{w}" height="{h}" fill="{rnd.choice(["#f3ede1","#eadfc9","#f7f1e6","#e8d7b8"])}"/>')
        for wy in range(392 - h + 6, 388, 9):
            a(f'<rect x="{x+4}" y="{wy}" width="{w-8}" height="2" fill="#c9b99a" opacity=".6"/>')
        x += w + rnd.randint(0, 3)
    a('<rect x="318" y="318" width="34" height="74" fill="#e2cfa8"/><rect x="314" y="312" width="42" height="8" fill="#d4bf95"/><rect x="324" y="296" width="22" height="18" fill="#e2cfa8"/><path d="M322 296 Q335 276 348 296 Z" fill="#c7a26a"/>')
    a('<rect x="358" y="336" width="56" height="56" fill="#e7d6b2"/><path d="M356 336 L386 318 L416 336 Z" fill="#c98b5a"/>')
    # Gibralfaro hill with the castle walls
    a('<path d="M-10 400 L-10 268 Q40 236 110 246 Q170 256 210 300 Q240 336 300 392 L300 400 Z" fill="#7d8a4e"/>')
    a('<path d="M-10 400 L-10 300 Q60 290 130 320 Q190 350 230 400 Z" fill="#6a7742"/>')
    for i in range(26):
        tx = rnd.uniform(0, 230); ty = rnd.uniform(270, 395)
        a(f'<circle cx="{tx:.0f}" cy="{ty:.0f}" r="{rnd.uniform(3,6):.1f}" fill="#4f5d31" opacity=".8"/>')
    wall = 'M10 262 L40 250 L80 246 L120 250 L160 262 L190 286'
    a(f'<path d="{wall}" fill="none" stroke="#d9c49a" stroke-width="9" stroke-linejoin="round"/>')
    for tx, ty in ((14, 262), (58, 248), (102, 247), (146, 257), (184, 282)):
        a(f'<rect x="{tx-7}" y="{ty-22}" width="14" height="22" fill="#d9c49a"/><path d="M{tx-7} {ty-22} h3 v-3 h3 v3 h2 v-3 h3 v3 h3 v3 h-14 z" fill="#c9b282"/>')
    # sea
    a('<rect x="0" y="392" width="600" height="150" fill="url(#vsea)"/>')
    for i in range(40):
        sx = rnd.uniform(0, 600); sy = rnd.uniform(400, 530); w = rnd.uniform(6, 18)
        a(f'<rect x="{sx:.0f}" y="{sy:.0f}" width="{w:.0f}" height="1.6" fill="#fff" opacity="{rnd.uniform(.25,.6):.2f}"/>')
    # cruise ship far out, sailboats
    a('<g transform="translate(400 398)"><path d="M0 14 L150 14 L140 26 L8 26 Z" fill="#f7f7f7"/><rect x="18" y="4" width="110" height="10" fill="#fff"/><rect x="34" y="-4" width="74" height="8" fill="#fff"/><rect x="76" y="-12" width="12" height="9" fill="#1b5f93"/>' +
      ''.join(f'<rect x="{22+i*8}" y="7" width="5" height="3" fill="#2a5b8a"/>' for i in range(13)) + '<rect x="0" y="20" width="148" height="3" fill="#1b5f93"/></g>')
    for bx, by, s in ((200, 450, 1), (300, 476, .8)):
        a(f'<g transform="translate({bx} {by}) scale({s})"><path d="M0 0 L0 -46 L26 -6 Z" fill="#fff"/><path d="M-2 -40 L-2 -4 L-22 -4 Z" fill="#f3efe6"/><path d="M-26 0 L32 0 L24 9 L-20 9 Z" fill="#e9e4da"/></g>')
    # Muelle Uno quay + promenade
    a('<path d="M0 540 L600 520 L600 720 L0 720 Z" fill="#d8cbb0"/><path d="M0 540 L600 520 L600 528 L0 548 Z" fill="#b9aa8c"/>')
    a('<path d="M0 600 L600 586 L600 720 L0 720 Z" fill="#cbbd9f"/>')
    # the coloured glass cube on its glass base
    cx, cy, s = 130, 520, 78
    a(f'<rect x="{cx-50}" y="{cy}" width="100" height="18" fill="#bcd8e6" opacity=".9"/><rect x="{cx-50}" y="{cy+16}" width="100" height="4" fill="#9fb6c2"/>')
    cols = ['#e53935', '#fdd835', '#1e88e5', '#43a047', '#ffffff', '#fb8c00', '#8e24aa', '#00acc1']
    n = 4; step = s / n
    x0, y0 = cx - s / 2 - 10, cy - s
    for i in range(n):
        for j in range(n):
            a(f'<rect x="{x0+i*step:.1f}" y="{y0+j*step:.1f}" width="{step-1.5:.1f}" height="{step-1.5:.1f}" fill="{rnd.choice(cols)}" opacity=".92"/>')
    # side face (skewed)
    for i in range(2):
        for j in range(n):
            px = x0 + s + i * 11; py = y0 + j * step - i * 6
            a(f'<path d="M{px:.1f} {py:.1f} l11 -6 v{step-1.5:.1f} l-11 6 z" fill="{rnd.choice(cols)}" opacity=".75"/>')
    a(f'<path d="M{x0:.1f} {y0:.1f} l22 -12 h{s:.1f} l-22 12 z" fill="#f0f0f0" opacity=".9"/>')
    # pergola (the undulating white canopy) along the promenade
    pts = ' '.join(f'{x},{548 - 6*math.sin(x/38) - x*0.02:.1f}' for x in range(230, 601, 10))
    a(f'<polyline points="{pts}" fill="none" stroke="#ffffff" stroke-width="7" stroke-linecap="round"/>')
    for x in range(240, 600, 30):
        y = 548 - 6*math.sin(x/38) - x*0.02
        a(f'<rect x="{x-1.5}" y="{y:.1f}" width="3" height="{596-y-x*0.02:.1f}" fill="#f4f4f4"/>')
    # palm trees
    for px in (260, 350, 440, 560):
        base = 600 - px * .023
        a(f'<path d="M{px} {base:.0f} Q{px+6} {base-60:.0f} {px+2} {base-110:.0f}" fill="none" stroke="#8a6a44" stroke-width="6"/>')
        for ang in (-160, -125, -95, -60, -25, 10, 200):
            r = math.radians(ang); ex = px + 2 + 46 * math.cos(r); ey = base - 110 + 30 * math.sin(r) + 14
            a(f'<path d="M{px+2} {base-110:.0f} Q{(px+2+ex)/2:.0f} {base-128:.0f} {ex:.0f} {ey:.0f}" fill="none" stroke="#3f7a3a" stroke-width="7" stroke-linecap="round"/>')
    # La Farola lighthouse
    lx, ly = 520, 560
    a(f'<rect x="{lx-26}" y="{ly-30}" width="52" height="30" fill="#d9b27c"/><rect x="{lx-26}" y="{ly-34}" width="52" height="5" fill="#c49a62"/>')
    a(f'<path d="M{lx-13} {ly-34} L{lx-9} {ly-150} L{lx+9} {ly-150} L{lx+13} {ly-34} Z" fill="#f7f4ee"/>')
    a(f'<rect x="{lx-15}" y="{ly-156}" width="30" height="7" fill="#e8e2d6"/><rect x="{lx-8}" y="{ly-176}" width="16" height="20" fill="#cfe8f2" stroke="#7a7a7a" stroke-width="1.5"/><path d="M{lx-10} {ly-176} L{lx} {ly-190} L{lx+10} {ly-176} Z" fill="#b84a2e"/>')
    for k in range(3):
        a(f'<rect x="{lx-4}" y="{ly-130+k*30}" width="8" height="10" fill="#d4cbb8"/>')
    # people strolling
    for px in (300, 330, 410, 470):
        y = 596 - px * .02
        a(f'<g fill="{rnd.choice(["#1e3f9a","#b3262b","#2f6b3c","#333"])}"><circle cx="{px}" cy="{y-20:.0f}" r="3.4"/><rect x="{px-3}" y="{y-16:.0f}" width="6" height="12" rx="2"/></g><rect x="{px-2.5}" y="{y-5:.0f}" width="2" height="7" fill="#333"/><rect x="{px+.5}" y="{y-5:.0f}" width="2" height="7" fill="#333"/>')
    a('</svg>')
    return ''.join(g)

def sill_svg():
    return '''<svg class="sillart" viewBox="0 0 300 90" aria-hidden="true">
  <g transform="translate(40 0)"><path d="M0 46 L56 46 L50 88 L6 88 Z" fill="#b5532f"/><rect x="-3" y="40" width="62" height="10" rx="2" fill="#c8633c"/>
  ''' + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>' for x, y, r, c in [(10,28,9,'#3f7a3a'),(28,22,11,'#2f6b3c'),(46,28,9,'#3f7a3a'),(20,12,7,'#e2363a'),(36,8,6,'#e2363a'),(46,18,5,'#f04d4d'),(12,20,5,'#f04d4d')]) + '''</g>
  <g transform="translate(220 22)"><path d="M0 0 L26 0 L22 66 L4 66 Z" fill="#f7f4ee" opacity=".45"/><path d="M2 14 L24 14 L22 66 L4 66 Z" fill="#e8a317"/><rect x="1" y="8" width="24" height="9" rx="3" fill="#fffaf0"/></g>
</svg>'''

def deco(kind):
    if kind == 'stack':
        return '<svg class="deco stack" viewBox="0 0 90 60" aria-hidden="true"><rect x="4" y="44" width="82" height="14" rx="2" fill="#8a2338"/><rect x="10" y="30" width="72" height="14" rx="2" fill="#d9b45a"/><rect x="2" y="16" width="78" height="14" rx="2" fill="#2f4d7a"/><rect x="8" y="34" width="60" height="2" fill="#fff" opacity=".4"/></svg>'
    if kind == 'globe':
        return '<svg class="deco globe" viewBox="0 0 80 100" aria-hidden="true"><path d="M20 94 L60 94 L54 86 L26 86 Z" fill="#5a361b"/><rect x="38" y="70" width="4" height="18" fill="#a07a3a"/><path d="M8 40 A32 32 0 0 0 72 40" fill="none" stroke="#a07a3a" stroke-width="3"/><circle cx="40" cy="40" r="28" fill="#2b7fb8"/><path d="M24 26 Q34 20 40 28 T56 30 L58 42 Q48 48 40 44 T22 48 Z M30 56 Q40 52 48 58 L44 64 Q36 62 32 64 Z" fill="#7cb342"/></svg>'
    if kind == 'plant':
        return '<svg class="deco plant" viewBox="0 0 70 100" aria-hidden="true"><path d="M16 66 L54 66 L50 98 L20 98 Z" fill="#b5532f"/>' + ''.join(f'<path d="M35 66 Q{35+dx*.4:.0f} {40:.0f} {35+dx} {h}" fill="none" stroke="#3f7a3a" stroke-width="5" stroke-linecap="round"/>' for dx, h in ((-26, 20), (-12, 6), (4, 2), (18, 10), (28, 28))) + '</svg>'
    if kind == 'ball':
        return '<svg class="deco ball" viewBox="0 0 60 60" aria-hidden="true"><circle cx="30" cy="30" r="27" fill="#fff" stroke="#222" stroke-width="2"/><path d="M30 18 l10 7 -4 12 h-12 l-4 -12 z" fill="#222"/><path d="M30 18 V5 M40 25 L54 20 M36 37 L44 50 M24 37 L16 50 M20 25 L6 20" stroke="#222" stroke-width="2"/></svg>'
    if kind == 'bottle':
        return '<svg class="deco bottle" viewBox="0 0 30 110" aria-hidden="true"><path d="M11 2 h8 v26 q9 8 9 20 v58 h-26 v-58 q0 -12 9 -20 z" fill="#5b3a14"/><rect x="4" y="58" width="22" height="26" fill="#f3e2b8"/><rect x="10" y="0" width="10" height="6" fill="#d9b45a"/><text x="15" y="75" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="8" fill="#6b1a1a">ALE</text></svg>'
    if kind == 'scarf':
        return '<svg class="deco scarf" viewBox="0 0 60 110" aria-hidden="true">' + ''.join(f'<rect x="14" y="{4+i*12}" width="30" height="12" fill="{["#1e3f9a","#ffcd00","#ffffff"][i%3]}"/>' for i in range(8)) + '<g stroke="#1e3f9a" stroke-width="2">' + ''.join(f'<line x1="{16+k*4}" y1="100" x2="{16+k*4}" y2="108"/>' for k in range(7)) + '</g></svg>'
    return ''

def book(sid):
    s = {x[0]: x for x in SHELVES}[sid]
    _, title, c, b, ink = s
    n = counts.get(sid, 0)
    rnd = random.Random(sid)
    h = rnd.choice([88, 91, 94, 97]); lean = 0
    return (f'<a class="book" href="/travel-guides/guide/?shelf={sid}" data-shelf="{sid}" style="--c:{c};--b:{b};--i:{ink};--h:{h}%">'
            f'<span class="band t"></span><span class="ti">{title}</span><span class="n" data-count="{sid}">{n}</span><span class="band u"></span>'
            f'<span class="sr"> – {n} guide{"s" if n != 1 else ""}</span></a>')

ROWS = [
    (['north-england', 'south-england', 'east-england', 'west-england', 'wales', 'scotland'], ['stack']),
    (['northern-ireland', 'ireland', 'spain', 'france', 'usa', 'rest-of-world'], ['globe']),
    (['airports'], ['scarf', 'plant', 'ball', 'bottle']),
]

def case():
    out = ['<div class="case"><div class="plaque"><h1>Travel Guides</h1><span>one beer at a time</span></div>']
    for ids, decos in ROWS:
        books = ''.join(book(i) for i in ids)
        d = ''.join(deco(k) for k in decos)
        out.append(f'<div class="shelf">{books}{d}</div>')
    out.append('</div>')
    return ''.join(out)

CSS = r'''
  :root{--navy:#0a1838;--yellow:#ffcd00;--cream:#f7f2e4}
  *{box-sizing:border-box;margin:0;padding:0}
  html,body{min-height:100%}
  body{min-height:100vh;min-height:100dvh;display:flex;flex-direction:column;font-family:Inter,system-ui,sans-serif;color:#2a2018;overflow-x:hidden;overflow-x:clip;
    background:
      radial-gradient(ellipse 45% 60% at 74% 40%,rgba(255,236,190,.55),transparent 70%),
      radial-gradient(ellipse 120% 80% at 50% 0,transparent 55%,rgba(90,60,30,.18)),
      url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='.8' numOctaves='2'/%3E%3CfeColorMatrix values='0 0 0 0 .5 0 0 0 0 .4 0 0 0 0 .3 0 0 0 .06 0'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23n)'/%3E%3C/svg%3E"),
      linear-gradient(#f1e7d3,#e8dbc2)}
  a{color:inherit}
  header{display:flex;align-items:center;justify-content:space-between;gap:16px;width:100%;padding:14px clamp(16px,3vw,40px);position:relative;z-index:3}
  .brand{display:flex;align-items:center;gap:10px;text-decoration:none;font-family:"Bebas Neue",Impact,sans-serif;font-size:1.6rem;letter-spacing:.06em;white-space:nowrap;color:#2a2018}
  .brand svg{width:38px;height:38px}
  .back{font-size:.92rem;font-weight:600;text-decoration:none;padding:.45em .9em;border:1.5px solid rgba(42,32,24,.35);border-radius:999px;white-space:nowrap;transition:border-color .15s,background .15s}
  .back:hover,.back:focus-visible{border-color:#2a2018;background:rgba(255,255,255,.4)}
  .sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
  main.room{flex:1;overflow-x:clip;display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);align-items:end;gap:clamp(20px,5vw,90px);padding:0 clamp(16px,5vw,90px);position:relative}
  .floor{height:clamp(40px,8vh,80px);background:
      repeating-linear-gradient(90deg,transparent 0 78px,rgba(80,30,10,.35) 78px 80px),
      linear-gradient(#b8643d,#9c4e2c);border-top:6px solid #7a3d22;position:relative}
  .floor::after{content:"";position:absolute;left:52%;right:4%;top:0;bottom:0;background:linear-gradient(90deg,transparent,rgba(255,230,170,.35),transparent);transform:skewX(-30deg);pointer-events:none}
  /* ---- bookcase ---- */
  .case{--sh:clamp(118px,calc((100vh - 300px)/3),220px);justify-self:end;width:min(100%,560px,calc(52vh + 120px));background:linear-gradient(90deg,#4a2a14,#5e3a1e 8%,#5e3a1e 92%,#4a2a14);padding:0 16px 16px;border-radius:6px 6px 0 0;box-shadow:0 20px 40px rgba(60,30,10,.35),inset 0 0 0 3px #3a200e;position:relative}
  .plaque{position:relative;margin:0 -24px 12px;background:linear-gradient(#6e4524,#4a2a14);padding:10px 16px 12px;border-radius:6px;text-align:center;box-shadow:0 6px 0 #3a200e}
  .plaque h1{display:inline-block;font-family:"Bebas Neue",Impact,sans-serif;font-weight:400;font-size:clamp(1.3rem,2.4vw,1.9rem);letter-spacing:.14em;color:#3a2a10;background:linear-gradient(#f3d985,#c9a23f);padding:.12em .9em 0;border-radius:4px;box-shadow:inset 0 0 0 2px #a8842f,0 2px 4px rgba(0,0,0,.4)}
  .plaque span{display:block;font-family:"Caveat",cursive;font-size:1.15rem;color:#f2dca0;margin-top:2px}
  .shelf{height:var(--sh);overflow:hidden;display:flex;align-items:flex-end;gap:5px;padding:0 10px;border-bottom:12px solid #7a4b27;box-shadow:inset 0 -14px 18px rgba(0,0,0,.35),0 4px 0 #3a200e;background:linear-gradient(#2c170a,#3b2010);margin-top:10px}
  .book{position:relative;height:var(--h);width:clamp(40px,4.4vw,62px);flex:none;display:flex;flex-direction:column;align-items:center;text-decoration:none;color:var(--i);
    background:linear-gradient(90deg,rgba(0,0,0,.28),rgba(255,255,255,.14) 18%,rgba(255,255,255,0) 40%,rgba(0,0,0,.22)),var(--c);
    border-radius:3px 3px 2px 2px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.25);transition:transform .25s ease;outline:none;overflow:hidden;flex:0 1 auto;min-width:30px}
  .book .band{display:block;width:100%;height:7px;background:var(--b);margin-top:9%}
  .book .band.u{margin-top:auto;margin-bottom:12%}
  .book .ti{writing-mode:vertical-rl;font-family:"Bebas Neue",Impact,sans-serif;font-size:clamp(.95rem,min(1.45vw,2.2vh),1.3rem);letter-spacing:.05em;line-height:1.02;margin-top:8px;white-space:normal;text-transform:uppercase;flex:1 1 auto;min-height:0;max-width:100%;padding:0 3px;overflow:hidden;text-align:start}
  .book .n{font-family:"Bebas Neue",Impact,sans-serif;font-size:.85rem;margin-top:4px;opacity:.85;flex:none}
  .book .n::after{content:"";}
  .book:hover,.book:focus-visible{transform:translateY(-14px)}
  .book:focus-visible{box-shadow:0 0 0 3px #fff,0 0 0 6px #1e3f9a}
  .shelf .deco{height:72%;width:auto;flex:0 1 auto;min-width:0;margin-left:auto}
  .shelf .deco~.deco{margin-left:6px}
  .shelf .deco.stack{height:32%}.shelf .deco.ball{height:36%}.shelf .deco.globe{height:78%}.shelf .deco.scarf{height:80%}.shelf .deco.bottle{height:66%}
  /* ---- window ---- */
  .win{justify-self:start;align-self:center;width:min(100%,640px);position:relative;margin-bottom:6vh}
  .frame{position:relative;width:74%;aspect-ratio:5/6;max-height:62vh;background:#fdfbf6;padding:16px;border-radius:120px 120px 6px 6px/90px 90px 6px 6px;box-shadow:0 18px 30px rgba(60,30,10,.25),inset 0 0 0 2px #d9cdb6;margin:0 auto}
  .glass{position:relative;height:100%;overflow:hidden;border-radius:106px 106px 2px 2px/78px 78px 2px 2px;box-shadow:inset 0 0 0 3px #e7dccb}
  .glass .view{position:absolute;inset:0;width:100%;height:100%}
  .glass::before{content:"";position:absolute;left:calc(50% - 5px);top:0;bottom:0;width:10px;background:#fdfbf6;box-shadow:0 0 0 1px #e2d7c4;z-index:2}
  .glass::after{content:"";position:absolute;left:0;right:0;top:44%;height:10px;background:#fdfbf6;box-shadow:0 0 0 1px #e2d7c4;z-index:2}
  .glare{position:absolute;inset:0;background:linear-gradient(120deg,rgba(255,255,255,.25),transparent 30%,transparent 60%,rgba(255,255,255,.12) 70%,transparent 80%);z-index:1;pointer-events:none}
  .shutter{position:absolute;top:2%;bottom:2%;width:19%;background:repeating-linear-gradient(#2f6b4f 0 9px,#255a42 9px 12px);border:5px solid #24533d;border-radius:6px;box-shadow:0 10px 20px rgba(0,0,0,.2)}
  .shutter.l{right:calc(100% + 6px);transform:perspective(600px) rotateY(28deg);transform-origin:100% 50%}
  .shutter.r{left:calc(100% + 6px);transform:perspective(600px) rotateY(-28deg);transform-origin:0 50%}
  .sill{position:relative;height:16px;width:84%;margin:0 auto;background:linear-gradient(#f7f2e8,#ddd2bf);border-radius:3px;box-shadow:0 8px 12px rgba(60,30,10,.25)}
  .sillart{position:absolute;bottom:14px;left:6%;width:58%;height:auto}
  .caption{position:absolute;right:0;bottom:-30px;font-family:"Caveat",cursive;font-size:1.15rem;color:#6b5236;transform:rotate(-2deg)}
  footer{text-align:center;padding:10px 16px;color:#f3dcc8;font-size:.85rem;background:#7a3d22}
  @media (max-width:860px),(max-aspect-ratio:4/5){
    main.room{grid-template-columns:1fr;align-items:start;gap:34px;padding:6px 16px 0}
    .win{order:-1;justify-self:center;margin-bottom:6px}
    .frame{aspect-ratio:auto;width:80%;height:min(40vh,380px);max-height:none}
    .win{width:min(96vw,520px)!important}
    .case{justify-self:center;width:100%;max-width:560px;--sh:min(26vh,190px)}
    .book{width:clamp(36px,11.5vw,58px)}
    .book .ti{font-size:clamp(.9rem,4vw,1.15rem)}
    .shutter{width:18%}
  }
  @media (max-width:420px){.shelf .deco.stack,.shelf .deco.globe,.shelf .deco.ball{display:none}.brand{font-size:1.3rem}.brand svg{width:30px;height:30px}.back{font-size:.8rem}}
  @media (prefers-reduced-motion:reduce){.book{transition:none}}
'''

PAGE = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Travel Guides - Rob Callery</title>
<meta name="description" content="Rob Callery's pint-first travel guides, shelved by region.">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Caveat:wght@500;700&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<script>(function(){{var q=location.search;if(/[?&](city|shelf)=/.test(q))location.replace('/travel-guides/guide/'+q)}})();</script>
<style>{CSS}</style>
</head>
<body>
<header>
  <a class="brand" href="/"><svg viewBox="190 157 700 700" aria-hidden="true"><circle cx="540" cy="507" r="345" fill="#0a1838"/><path fill="#f7f2e4" fill-rule="evenodd" d="{globe}"/></svg>Rob Callery</a>
  <a class="back" href="/explore/">← Back to the bar</a>
</header>
<main class="room">
  <nav aria-label="Guide books by region" style="min-width:0">{case()}</nav>
  <div class="win">
    <div class="frame"><div class="shutter l" aria-hidden="true"></div><div class="shutter r" aria-hidden="true"></div><div class="glass">{view()}<div class="glare"></div></div></div>
    <div class="sill">{sill_svg()}</div>
    <div class="caption">Muelle Uno, Málaga</div>
  </div>
</main>
<div class="floor" aria-hidden="true"></div>
<footer>© <span id="yr">2026</span> Rob Callery · callery.co.uk · Drink responsibly</footer>
<script src="/travel-guides/guides.js"></script>
<script>
(function(){{
  {SHELF_OF_JS}
  var c={{}};(window.GUIDES||[]).forEach(function(g){{var s=shelfOf(g);c[s]=(c[s]||0)+1}});
  [].forEach.call(document.querySelectorAll('[data-count]'),function(e){{var n=c[e.getAttribute('data-count')]||0;e.textContent=n;var sr=e.parentNode.querySelector('.sr');if(sr)sr.textContent=' – '+n+' guide'+(n===1?'':'s')}});
  document.getElementById('yr').textContent=new Date().getFullYear();
  // shrink any spine title that doesn't fit its book
  function fit(){{[].forEach.call(document.querySelectorAll('.book .ti'),function(t){{t.style.fontSize='';var fs=parseFloat(getComputedStyle(t).fontSize),n=0;
    while((t.scrollHeight>t.clientHeight+1||t.scrollWidth>t.clientWidth+1)&&fs>8&&n++<40){{fs-=.5;t.style.fontSize=fs+'px'}}}})}}
  fit();addEventListener('resize',fit);if(document.fonts&&document.fonts.ready)document.fonts.ready.then(fit);
}})();
</script>
</body>
</html>
'''
open('/home/claude/site/travel-guides/index.html', 'w').write(PAGE)
print('room built', counts)
