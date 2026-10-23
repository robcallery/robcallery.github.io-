# Pit wall view at dusk: grandstand, start gantry, main straight, pit wall + monitors in the foreground.
import random, math

def scene():
    R = random.Random(26)
    g = []
    a = g.append
    a('''<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#070d1f"/><stop offset=".45" stop-color="#1b1d3c"/><stop offset=".72" stop-color="#5a2f4a"/><stop offset="1" stop-color="#d0703a"/>
  </linearGradient>
  <linearGradient id="asph" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a2d36"/><stop offset="1" stop-color="#16181e"/></linearGradient>
  <linearGradient id="wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2b2f3a"/><stop offset="1" stop-color="#101219"/></linearGradient>
  <radialGradient id="flood" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#fff8e0" stop-opacity=".95"/><stop offset=".25" stop-color="#ffe6a8" stop-opacity=".35"/><stop offset="1" stop-color="#ffe6a8" stop-opacity="0"/></radialGradient>
  <linearGradient id="beam" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff3c8" stop-opacity=".16"/><stop offset="1" stop-color="#fff3c8" stop-opacity="0"/></linearGradient>
  <pattern id="chq" width="16" height="16" patternUnits="userSpaceOnUse"><rect width="16" height="16" fill="#fff"/><rect width="8" height="8" fill="#111"/><rect x="8" y="8" width="8" height="8" fill="#111"/></pattern>
</defs>''')
    a('<rect width="1600" height="900" fill="url(#sky)"/>')
    # stars
    for _ in range(70):
        a(f'<circle cx="{R.uniform(0,1600):.0f}" cy="{R.uniform(0,250):.0f}" r="{R.uniform(.5,1.4):.1f}" fill="#fff" opacity="{R.uniform(.2,.8):.2f}"/>')
    # distant city skyline on the horizon
    x = 0
    while x < 1600:
        w = R.randint(30, 90); h = R.randint(20, 90)
        a(f'<rect x="{x}" y="{430-h}" width="{w}" height="{h}" fill="#241a33"/>')
        for _ in range(R.randint(0, 4)):
            a(f'<rect x="{x+R.randint(4,max(5,w-8))}" y="{430-h+R.randint(6,max(7,h-6))}" width="3" height="3" fill="#ffcf7a" opacity=".7"/>')
        x += w + R.randint(0, 10)
    # grandstand across the straight
    a('<path d="M0 300 L1600 270 L1600 470 L0 490 Z" fill="#1a1f2e"/>')
    a('<path d="M-20 286 L1620 254 L1620 270 L-20 302 Z" fill="#0d1018"/>')                     # roof edge
    for i in range(0, 1600, 80):
        a(f'<rect x="{i}" y="{297-i*0.019:.0f}" width="5" height="{180}" fill="#0f131d"/>')
    for row in range(16):
        y0 = 310 + row * 10.5
        for i in range(0, 1600, 7):
            if R.random() < .82:
                y = y0 - i * 0.0185 + R.uniform(-1, 1)
                c = R.choice(['#d8d8d8', '#ff8a3d', '#e8002d', '#3671c6', '#27f4d2', '#ffd23f', '#9aa4b2', '#5a6273', '#ffffff', '#ff87bc'])
                a(f'<rect x="{i+R.uniform(0,2):.0f}" y="{y:.0f}" width="3" height="4" fill="{c}" opacity="{R.uniform(.45,.9):.2f}"/>')
    # sponsor-free hoarding under the stand
    a('<path d="M0 478 L1600 458 L1600 478 L0 498 Z" fill="#e10600"/>')
    a('<text x="800" y="478" text-anchor="middle" font-family="Titillium Web, Arial Narrow, sans-serif" font-weight="700" font-size="17" fill="#fff" letter-spacing="10" transform="rotate(-0.7 800 478)">ONE BEER AT A TIME · PIT WALL · ONE BEER AT A TIME · PIT WALL</text>')
    # floodlight towers
    for fx, fy in ((140, 120), (560, 95), (1040, 90), (1460, 110)):
        a(f'<rect x="{fx-3}" y="{fy}" width="6" height="{300-fy+160}" fill="#0b0e16"/>')
        a(f'<rect x="{fx-34}" y="{fy-18}" width="68" height="22" rx="2" fill="#141824"/>')
        for k in range(5):
            a(f'<circle cx="{fx-26+k*13}" cy="{fy-7}" r="4.5" fill="#fff6d6"/>')
        a(f'<circle cx="{fx}" cy="{fy-7}" r="120" fill="url(#flood)"/>')
        a(f'<path d="M{fx-34} {fy} L{fx-260} 900 L{fx+260} 900 L{fx+34} {fy} Z" fill="url(#beam)"/>')
    # track: main straight running across
    a('<path d="M0 520 L1600 500 L1600 700 L0 760 Z" fill="url(#asph)"/>')
    a('<path d="M0 520 L1600 500 L1600 506 L0 527 Z" fill="#e6e6e6"/>')                         # far white line
    for i in range(0, 1600, 40):                                                                # far kerb
        a(f'<path d="M{i} {513-i*0.0125:.1f} L{i+40} {513-(i+40)*0.0125:.1f} L{i+40} {520-(i+40)*0.0125:.1f} L{i} {520-i*0.0125:.1f} Z" fill="{"#e10600" if (i//40)%2 else "#f2f2f2"}"/>')
    a('<path d="M0 748 L1600 690 L1600 698 L0 757 Z" fill="#e6e6e6"/>')                         # near white line
    # grid boxes
    for k in range(10):
        gx = 300 + k * 118; lane = k % 2
        yb = 560 + lane * 80 - gx * 0.03
        a(f'<path d="M{gx} {yb:.0f} l52 -2 M{gx} {yb:.0f} l0 22 M{gx+52} {yb-2:.0f} l0 22" stroke="#f2f2f2" stroke-width="3" fill="none" opacity=".75"/>')
    # start/finish line (chequered stripe across the straight)
    a('<path d="M1268 507 L1292 506 L1300 712 L1276 715 Z" fill="url(#chq)" opacity=".9"/>')
    # start gantry with the five red lights
    a('<rect x="1250" y="300" width="14" height="230" fill="#20242f"/><rect x="1500" y="290" width="14" height="235" fill="#20242f"/>')
    a('<rect x="1236" y="300" width="292" height="44" rx="3" fill="#121620"/>')
    for k in range(5):
        lx = 1268 + k * 56
        a(f'<rect x="{lx-18}" y="306" width="36" height="32" rx="4" fill="#05070c"/><circle class="gl" cx="{lx-8}" cy="322" r="7" fill="#3a0606"/><circle class="gl" cx="{lx+8}" cy="322" r="7" fill="#3a0606"/>')
    # a car flashing down the straight (simple silhouette)
    a('<g id="car" opacity=".95"><path d="M0 0 h120 l16 8 h40 l6 10 h-210 l8 -10 h20 z" fill="#e10600"/><circle cx="18" cy="20" r="10" fill="#0b0b0b"/><circle cx="150" cy="20" r="10" fill="#0b0b0b"/><rect x="60" y="-8" width="26" height="9" rx="3" fill="#111"/><rect x="-14" y="-6" width="10" height="20" fill="#111"/><rect x="176" y="6" width="14" height="12" fill="#111"/></g>')
    # pit wall + catch fence in the foreground
    a('<path d="M0 770 L1600 712 L1600 900 L0 900 Z" fill="url(#wall)"/>')
    a('<path d="M0 770 L1600 712 L1600 724 L0 784 Z" fill="#3a3f4c"/>')
    for i in range(0, 1600, 24):
        a(f'<rect x="{i}" y="{560+i*-0.036:.0f}" width="3" height="{215}" fill="#0c0f16" opacity=".75"/>')
    a('<path d="M0 560 L1600 502" stroke="#0c0f16" stroke-width="5"/>')
    fence = ''.join(f'M{i} {560-i*0.036:.1f} L{i+30} {780-(i+30)*0.036:.1f} ' for i in range(-200, 1600, 30)) + ''.join(f'M{i+30} {560-(i+30)*0.036:.1f} L{i} {780-i*0.036:.1f} ' for i in range(-200, 1600, 30))
    a(f'<path d="{fence}" stroke="#a9b1c2" stroke-width=".7" opacity=".22" fill="none"/>')
    # pit wall gantry monitors
    for mx in range(60, 1600, 210):
        my = 806 - mx * 0.036
        a(f'<rect x="{mx}" y="{my:.0f}" width="150" height="86" rx="4" fill="#0a0d14" stroke="#262b38" stroke-width="3"/>')
        for r in range(6):
            a(f'<rect x="{mx+10}" y="{my+10+r*12:.0f}" width="{R.randint(50,128)}" height="6" fill="{R.choice(["#27f4d2","#ffd23f","#ff8a3d","#e8e8e8","#9b59ff"])}" opacity=".55"/>')
    return ''.join(g)
