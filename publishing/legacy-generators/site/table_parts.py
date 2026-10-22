import random, math

def _crimp(y0, h, w=160, n=16):
    pts = []
    for i in range(n + 1):
        x = i * w / n
        pts.append(f'{x:.1f},{y0 + (h if i % 2 else 0):.1f}')
    return pts

def packet(kind):
    """kind: 'prev' (pork scratchings) or 'next' (crisps). viewBox 0 0 160 214."""
    if kind == 'prev':
        c1, c2, band, ink, title1, title2, arrow = '#8c2f1c', '#5e1b10', '#ffcd00', '#fff3d6', 'PORK', 'SCRATCHINGS', '‹ BACK'
    else:
        c1, c2, band, ink, title1, title2, arrow = '#1f4fb8', '#12306f', '#ffcd00', '#ffffff', 'CHEESE &amp; ONION', 'CRISPS', 'NEXT ›'
    gid = 'pk' + kind
    rnd = random.Random(7 if kind == 'prev' else 11)
    g = [f'<svg viewBox="0 0 160 214" aria-hidden="true" focusable="false">',
         f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>',
         f'<linearGradient id="{gid}s" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".28"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>']
    # bag body with slightly bulging sides
    g.append(f'<path d="M6 14 Q2 107 6 200 L154 200 Q158 107 154 14 Z" fill="url(#{gid})"/>')
    # crimped seals
    top = ' '.join(_crimp(0, 6)) ; g.append(f'<path d="M0 6 L{top.replace(" ", " L")} L160 18 L0 18 Z" fill="{c2}"/>')
    g.append('<g stroke="#000" stroke-opacity=".18" stroke-width="1">' + ''.join(f'<line x1="{x}" y1="6" x2="{x}" y2="18"/>' for x in range(5, 160, 5)) + '</g>')
    bot = ' '.join(_crimp(208, 6)); g.append(f'<path d="M0 196 L160 196 L160 208 L{bot.replace(" ", " L")} Z" fill="{c2}"/>')
    g.append('<g stroke="#000" stroke-opacity=".18" stroke-width="1">' + ''.join(f'<line x1="{x}" y1="196" x2="{x}" y2="208"/>' for x in range(5, 160, 5)) + '</g>')
    # brand
    g.append(f'<text x="80" y="38" text-anchor="middle" font-family="Caveat, cursive" font-weight="700" font-size="19" fill="{band}">Callery\'s</text>')
    g.append(f'<text x="80" y="62" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="{22 if kind=="prev" else 17}" fill="{ink}" letter-spacing="1" textLength="{60 if kind=="prev" else 112}" lengthAdjust="spacingAndGlyphs">{title1}</text>')
    g.append(f'<text x="80" y="84" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="22" fill="{ink}" letter-spacing="1" textLength="{120 if kind=="prev" else 72}" lengthAdjust="spacingAndGlyphs">{title2}</text>')
    # food window
    g.append('<ellipse cx="80" cy="122" rx="52" ry="26" fill="#f7e7c2" opacity=".95"/>')
    if kind == 'prev':
        for i in range(9):
            x = 44 + i * 9 + rnd.uniform(-3, 3); y = 118 + rnd.uniform(-10, 10)
            r = rnd.uniform(6, 9)
            pts = ' '.join(f'{x + r*math.cos(a)*rnd.uniform(.7,1.2):.1f},{y + r*.7*math.sin(a)*rnd.uniform(.7,1.2):.1f}' for a in [k*math.pi/4 for k in range(8)])
            g.append(f'<polygon points="{pts}" fill="{rnd.choice(["#c98a3e","#b57430","#d9a35a"])}" stroke="#7a4518" stroke-width=".8"/>')
    else:
        for i in range(8):
            x = 42 + i * 10.5 + rnd.uniform(-2, 2); y = 120 + rnd.uniform(-9, 9); rot = rnd.uniform(-40, 40)
            g.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="11" ry="7" transform="rotate({rot:.0f} {x:.1f} {y:.1f})" fill="{rnd.choice(["#f2c94c","#f5d76e","#e8b93a"])}" stroke="#c99a26" stroke-width=".8"/>')
    # the "button" banner
    g.append(f'<g transform="rotate(-4 80 168)"><rect x="18" y="152" width="124" height="32" rx="5" fill="{band}"/><text x="80" y="177" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="27" fill="#14213f" letter-spacing="1">{arrow}</text></g>')
    g.append(f'<text x="80" y="193" text-anchor="middle" font-family="Inter, sans-serif" font-size="7" fill="{ink}" opacity=".75" letter-spacing="1">{"PROPER PUB SNACK · 30g" if kind=="prev" else "READY TO TURN · 25g"}</text>')
    # crinkle shine
    g.append(f'<path d="M30 18 L22 196 L44 196 L50 18 Z" fill="url(#{gid}s)" opacity=".8"/><path d="M118 18 L112 196 L122 196 L128 18 Z" fill="url(#{gid}s)" opacity=".5"/>')
    g.append('</svg>')
    return ''.join(g)

def pint():
    """Top-down pint on a beer mat. viewBox 0 0 260 260."""
    rnd = random.Random(3)
    g = ['<svg viewBox="0 0 260 260" aria-hidden="true" focusable="false"><defs>',
         '<radialGradient id="foam" cx=".45" cy=".42" r=".6"><stop offset="0" stop-color="#fffaf0"/><stop offset=".7" stop-color="#f3e3c3"/><stop offset="1" stop-color="#d9b77e"/></radialGradient>',
         '<radialGradient id="glassRim" cx=".5" cy=".5" r=".5"><stop offset=".82" stop-color="#fff" stop-opacity="0"/><stop offset=".92" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#fff" stop-opacity=".12"/></radialGradient>',
         '<radialGradient id="ale" cx=".5" cy=".5" r=".5"><stop offset=".7" stop-color="#c77a12"/><stop offset="1" stop-color="#8a4a08"/></radialGradient>',
         '</defs>']
    # beer mat
    g.append('<circle cx="130" cy="134" r="124" fill="#000" opacity=".28"/>')
    g.append('<circle cx="128" cy="128" r="122" fill="#f4ead2"/><circle cx="128" cy="128" r="112" fill="none" stroke="#b3262b" stroke-width="7"/>')
    g.append('<path id="matArc" d="M40 128 A88 88 0 0 1 216 128" fill="none"/>')
    g.append('<text font-family="Bebas Neue, Impact, sans-serif" font-size="17" fill="#b3262b" letter-spacing="3"><textPath href="#matArc" startOffset="50%" text-anchor="middle">ONE BEER AT A TIME</textPath></text>')
    g.append('<path id="matArc2" d="M24 128 A104 104 0 0 0 232 128" fill="none"/>')
    g.append('<text font-family="Bebas Neue, Impact, sans-serif" font-size="14" fill="#0a1838" letter-spacing="4"><textPath href="#matArc2" startOffset="50%" text-anchor="middle">CALLERY.CO.UK</textPath></text>')
    # glass shadow, glass, beer edge, foam
    g.append('<circle cx="136" cy="136" r="66" fill="#000" opacity=".22"/>')
    g.append('<circle cx="128" cy="128" r="66" fill="url(#ale)"/>')
    g.append('<circle cx="128" cy="128" r="59" fill="url(#foam)"/>')
    for i in range(60):
        a = rnd.uniform(0, 2*math.pi); d = rnd.uniform(0, 54); r = rnd.uniform(1, 3.4)
        g.append(f'<circle cx="{128+d*math.cos(a):.1f}" cy="{128+d*math.sin(a):.1f}" r="{r:.1f}" fill="none" stroke="#e2c99a" stroke-width=".7" opacity=".8"/>')
    g.append('<circle cx="128" cy="128" r="68" fill="url(#glassRim)"/><circle cx="128" cy="128" r="68" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="2"/>')
    g.append('<path d="M80 98 A57 57 0 0 1 114 72" fill="none" stroke="#fff" stroke-opacity=".8" stroke-width="4" stroke-linecap="round"/>')
    # condensation drops on the mat
    for i in range(10):
        a = rnd.uniform(0, 2*math.pi); d = rnd.uniform(72, 80)
        g.append(f'<ellipse cx="{128+d*math.cos(a):.1f}" cy="{128+d*math.sin(a):.1f}" rx="{rnd.uniform(1.5,3.5):.1f}" ry="{rnd.uniform(1.5,3):.1f}" fill="#fff" opacity=".35"/>')
    g.append('</svg>')
    return ''.join(g)

TABLE_CSS = r'''
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
  .pack{appearance:none;border:0;background:none;padding:0;cursor:pointer;width:clamp(110px,11vw,165px);display:block;transform:rotate(var(--r));transition:transform .25s ease,filter .25s ease,opacity .3s;filter:drop-shadow(0 12px 10px rgba(0,0,0,.5))}
  .pack svg{width:100%;height:auto;display:block}
  .pack:hover:not(:disabled),.pack:focus-visible{transform:rotate(0) translateY(-6px) scale(1.05);filter:drop-shadow(0 18px 14px rgba(0,0,0,.55)) drop-shadow(0 0 14px rgba(255,205,0,.35))}
  .pack:focus-visible{outline:3px solid #fff;outline-offset:6px;border-radius:8px}
  .pack:disabled{cursor:default;opacity:.45;filter:grayscale(.5) drop-shadow(0 8px 8px rgba(0,0,0,.4))}
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
'''
