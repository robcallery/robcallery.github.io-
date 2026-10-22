# Elland Road poster (bar page), the stadium scene, and the scoreboard art.
import random, math

def _crowd_dots(x0, x1, y0, y1, n, seed, cols=('#ffffff', '#ffcd00', '#1d4ed8', '#ffffff', '#e8e8e8')):
    rnd = random.Random(seed)
    return ''.join(f'<circle cx="{rnd.uniform(x0, x1):.1f}" cy="{rnd.uniform(y0, y1):.1f}" r="{rnd.uniform(1.3, 2.1):.1f}" fill="{rnd.choice(cols)}"/>' for _ in range(n))

# ---------------------------------------------------------------- poster
def poster():
    stand = ''
    # roof truss
    stand += '<rect x="22" y="112" width="186" height="5" fill="#c9d2e3"/>' + ''.join(
        f'<path d="M{22+i*9.3:.1f} 112 L{26.6+i*9.3:.1f} 104 L{31.2+i*9.3:.1f} 112" fill="none" stroke="#c9d2e3" stroke-width="1.2"/>' for i in range(20))
    stand += '<rect x="22" y="117" width="186" height="64" fill="#1e3f9a"/>' + ''.join(f'<rect x="{22+i*6.2:.1f}" y="117" width=".8" height="40" fill="#2a4fb0"/>' for i in range(30))
    stand += '<text x="115" y="143" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="24" fill="#fff" textLength="128" lengthAdjust="spacingAndGlyphs">ELLAND ROAD</text>'
    stand += '<rect x="64" y="148" width="102" height="2" fill="#ffcd00"/>'
    stand += '<rect x="22" y="157" width="186" height="3" fill="#f7f2e4"/>' + ''.join(f'<rect x="{27+i*11:.1f}" y="162" width="7" height="6" fill="#e8d6a8"/>' for i in range(17))
    stand += '<rect x="22" y="170" width="186" height="11" fill="#16307a"/>'
    for x in (62, 108, 154):
        stand += f'<rect x="{x}" y="172" width="13" height="9" fill="#f0c35a"/><rect x="{x-1}" y="169" width="15" height="3" fill="#ffcd00"/>'
    for x, words in ((24, ['SIDE', 'BEFORE', 'SELF']), (196, ['ALL', 'LEEDS', "AREN'T", 'WE'])):
        stand += f'<rect x="{x}" y="118" width="11" height="38" fill="#ffcd00"/><rect x="{x+1.2}" y="120" width="8.6" height="34" fill="#1e3f9a"/>'
        stand += ''.join(f'<text x="{x+5.5}" y="{127+i*7.5}" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="4.6" fill="#fff" textLength="7.4" lengthAdjust="spacingAndGlyphs">{w}</text>' for i, w in enumerate(words))
    crowd = _crowd_dots(26, 204, 184, 202, 70, 77)
    lights = ''.join(f'<g><rect x="{x-1}" y="70" width="2" height="44" fill="#4a5470"/><rect x="{x-9}" y="64" width="18" height="8" rx="1.5" fill="#dfe6ff"/><circle cx="{x}" cy="68" r="22" fill="#fff6c8" opacity=".18"/></g>' for x in (34, 196))
    stars = ''.join(f'<circle cx="{x}" cy="{y}" r=".8" fill="#fff" opacity=".8"/>' for x, y in ((50, 40), (80, 58), (120, 36), (150, 52), (176, 34), (100, 70), (60, 86), (168, 84)))
    return f'''<svg viewBox="0 0 230 300" role="img" aria-label="Elland Road poster">
  <defs>
    <linearGradient id="pSky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b1838"/><stop offset=".75" stop-color="#2b4180"/><stop offset="1" stop-color="#4a5f9a"/></linearGradient>
  </defs>
  <rect x="6" y="8" width="218" height="286" rx="2" fill="#f7f2e4"/>
  <rect x="6" y="8" width="218" height="286" rx="2" fill="none" stroke="#e3d9bf" stroke-width="1"/>
  <g transform="translate(0 2)">
    <rect x="16" y="20" width="198" height="200" fill="url(#pSky)"/>
    {stars}
    <path d="M190 48 A10 10 0 1 0 190 68 A7 10 0 1 1 190 48 Z" fill="#f4f1e0" transform="rotate(-25 190 58)"/>
    {lights}
    <rect x="16" y="100" width="20" height="104" fill="#24335a"/><rect x="194" y="100" width="20" height="104" fill="#24335a"/>
    {stand}
    <rect x="16" y="182" width="198" height="38" fill="#30364a"/>
    {crowd}
    <rect x="16" y="20" width="198" height="200" fill="none" stroke="#0a1838" stroke-width="1.5"/>
  </g>
  <text x="115" y="248" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="27" fill="#0a1838" letter-spacing="2">ELLAND ROAD</text>
  <rect x="58" y="254" width="114" height="2.5" fill="#ffcd00"/>
  <text x="115" y="270" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="10" fill="#1e3f9a" letter-spacing="3">MARCHING ON TOGETHER</text>
  <text x="115" y="284" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="7.5" fill="#8a7a58" letter-spacing="2.5">LEEDS · LS11 · EST. 1919</text>
  <rect x="2" y="0" width="34" height="13" fill="rgba(250,240,200,.78)" transform="rotate(-28 19 6)"/>
  <rect x="194" y="0" width="34" height="13" fill="rgba(250,240,200,.78)" transform="rotate(26 211 6)"/>
  <clipPath id="posterSheenClip"><rect x="8" y="8" width="214" height="286"/></clipPath>
  <g clip-path="url(#posterSheenClip)"><rect class="sheen" x="-120" y="8" width="60" height="286" fill="#fff" opacity=".18" transform="skewX(-20)"/></g>
</svg>'''

# ---------------------------------------------------------------- scoreboard art (match hub page)
def scoreboard_art():
    return '''<svg viewBox="0 0 300 220" role="img" aria-label="Elland Road scoreboard">
  <rect x="146" y="150" width="8" height="70" fill="#3a3f4b"/><rect x="100" y="150" width="8" height="70" fill="#3a3f4b"/><rect x="192" y="150" width="8" height="70" fill="#3a3f4b"/>
  <rect x="10" y="10" width="280" height="150" rx="8" fill="#14161c"/><rect x="18" y="18" width="264" height="134" rx="4" fill="#06070a"/>
  <rect x="18" y="18" width="264" height="24" fill="#1e3f9a"/><text x="150" y="36" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="17" fill="#ffcd00" letter-spacing="3">MATCH HUB</text>
  <g font-family="'Courier New', monospace" font-weight="700" fill="#ffcd00" style="filter:drop-shadow(0 0 3px #ffb000)">
    <text x="78" y="78" text-anchor="middle" font-size="16">LEEDS</text><text x="222" y="78" text-anchor="middle" font-size="16">AWAY</text>
    <text x="150" y="118" text-anchor="middle" font-size="40" class="clock">0 - 0</text>
  </g>
  <text x="150" y="142" text-anchor="middle" font-family="'Courier New', monospace" font-weight="700" font-size="11" fill="#4dff88">KICK-OFF SOON</text>
</svg>'''

# ---------------------------------------------------------------- stadium scene
def stadium_scene():
    W, H = 1200, 700
    g = []
    a = g.append
    a('<defs><linearGradient id="stSky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#070f26"/><stop offset="1" stop-color="#1b2c5e"/></linearGradient>'
      '<linearGradient id="stPitch" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2f7d3a"/><stop offset="1" stop-color="#3f9a48"/></linearGradient>'
      '<radialGradient id="stGlow"><stop offset="0" stop-color="#fffbe0" stop-opacity=".55"/><stop offset="1" stop-color="#fffbe0" stop-opacity="0"/></radialGradient></defs>')
    a(f'<rect width="{W}" height="{H}" fill="url(#stSky)"/>')
    rnd = random.Random(5)
    a(''.join(f'<circle cx="{rnd.uniform(0, W):.0f}" cy="{rnd.uniform(0, 70):.0f}" r="{rnd.choice([.8, 1.1, 1.4])}" fill="#fff" opacity="{rnd.uniform(.3, .9):.2f}"/>' for _ in range(40)))
    # floodlights
    for x in (70, 1130):
        a(f'<circle cx="{x}" cy="40" r="120" fill="url(#stGlow)"/><rect x="{x-4}" y="40" width="8" height="200" fill="#3a4466"/><rect x="{x-34}" y="22" width="68" height="34" rx="3" fill="#2a3456"/>')
        a(''.join(f'<rect x="{x-30+c*15}" y="{26+r*15}" width="11" height="11" rx="2" fill="#fffbe0"/>' for c in range(4) for r in range(2)))
    # far stand
    a('<path d="M120 150 L1080 150 L1110 268 L90 268 Z" fill="#16307a"/>')
    for r in range(8):
        y = 160 + r * 13
        a(f'<rect x="{110 - r*2.5:.1f}" y="{y}" width="{980 + r*5:.1f}" height="2" fill="#0f2462"/>')
    a(_crowd_dots(110, 1090, 156, 262, 650, 11))
    a('<rect x="100" y="138" width="1000" height="14" fill="#c9d2e3"/>' + ''.join(f'<path d="M{100+i*25} 138 L{112.5+i*25} 124 L{125+i*25} 138" fill="none" stroke="#c9d2e3" stroke-width="2"/>' for i in range(40)))
    # banners on the far stand
    for x, txt in ((210, 'SIDE BEFORE SELF'), (870, "ALL LEEDS AREN'T WE")):
        a(f'<rect x="{x}" y="232" width="150" height="22" fill="#ffcd00"/><rect x="{x+3}" y="235" width="144" height="16" fill="#1e3f9a"/><text x="{x+75}" y="248" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="14" fill="#fff" textLength="136" lengthAdjust="spacingAndGlyphs">{txt}</text>')
    # side stands
    a('<path d="M0 120 L90 150 L90 268 L-40 420 L0 420 Z" fill="#132a6c"/><path d="M1200 120 L1110 150 L1110 268 L1240 420 L1200 420 Z" fill="#132a6c"/>')
    a(_crowd_dots(4, 86, 150, 330, 160, 12) + _crowd_dots(1114, 1196, 150, 330, 160, 13))
    # ---- pitch drawn with a real perspective projection (metres -> screen)
    F, FH, YH, CX = 1408.0, 78565.0, -185.6, 600.0
    ZN = 100.0                      # near touchline distance from camera
    def P(X, Z, up=0.0):            # X along the pitch (-52.5..52.5), Z depth (ZN..ZN+68), up = height in m
        return (CX + F * X / Z, YH + FH / Z - F * up / Z)
    def pts(*xz): return ' '.join(f'{x:.1f},{y:.1f}' for x, y in (P(*q) for q in xz))
    def poly(xz, **kw):
        attrs = ' '.join(f'{k.replace("_", "-")}="{v}"' for k, v in kw.items())
        return f'<polygon points="{pts(*xz)}" {attrs}/>'
    def pline(xz, w=3):
        return f'<polyline points="{pts(*xz)}" fill="none" stroke="#f4f4ee" stroke-width="{w}" stroke-linejoin="round"/>'
    ZF, ZM = ZN + 68, ZN + 34
    a(poly([(-58, ZF + 4), (58, ZF + 4), (58, ZN - 30), (-58, ZN - 30)], fill='url(#stPitch)'))
    for i in range(12):            # mowing stripes
        if i % 2: continue
        z0, z1 = ZF - i * 68 / 12, ZF - (i + 1) * 68 / 12
        a(poly([(-58, z0), (58, z0), (58, z1), (-58, z1)], fill='#ffffff', opacity='.06'))
    # touchlines, goal lines, halfway line
    a(pline([(-52.5, ZN), (-52.5, ZF), (52.5, ZF), (52.5, ZN)]))
    a(pline([(0, ZF), (0, ZN - 30)]))
    circ = [(9.15 * math.cos(t), ZM + 9.15 * math.sin(t)) for t in [k * math.pi / 24 for k in range(49)]]
    a(pline(circ)); cx_, cy_ = P(0, ZM); a(f'<circle cx="{cx_:.1f}" cy="{cy_:.1f}" r="4" fill="#f4f4ee"/>')
    for s in (-1, 1):
        g0 = 52.5 * s
        # penalty area 16.5 m deep x 40.32 m wide, six-yard box 5.5 x 18.32
        a(pline([(g0, ZM - 20.16), (g0 - s * 16.5, ZM - 20.16), (g0 - s * 16.5, ZM + 20.16), (g0, ZM + 20.16)]))
        a(pline([(g0, ZM - 9.16), (g0 - s * 5.5, ZM - 9.16), (g0 - s * 5.5, ZM + 9.16), (g0, ZM + 9.16)], 2.4))
        sx, sy = P(g0 - s * 11, ZM); a(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="3" fill="#f4f4ee"/>')
        arc = [(g0 - s * 11 - s * 9.15 * math.cos(t), ZM + 9.15 * math.sin(t)) for t in [k * math.pi / 30 for k in range(-30, 31)]]
        arc = [q for q in arc if abs(q[0]) < abs(g0) - 16.5]
        if arc: a(pline(arc, 2.4))
        # the goal: posts 7.32 m apart, 2.44 m high, 2 m deep net behind the line
        za, zb = ZM - 3.66, ZM + 3.66
        back = g0 + s * 2.0
        a(poly([(back, za), (back, zb), (g0, zb), (g0, za)], fill='#ffffff', opacity='.12'))
        net = (f'<polygon points="{pts((g0, za, 2.44), (back, za, 2.0), (back, zb, 2.0), (g0, zb, 2.44))}" fill="#ffffff" opacity=".22"/>'
               f'<polygon points="{pts((back, za, 2.0), (back, zb, 2.0), (back, zb), (back, za))}" fill="#ffffff" opacity=".18"/>')
        a(net)
        a(f'<polyline points="{pts((g0, za), (g0, za, 2.44), (g0, zb, 2.44), (g0, zb))}" fill="none" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"/>')
        a(f'<polyline points="{pts((g0, za, 2.44), (back, za, 2.0), (back, za))}" fill="none" stroke="#dfe3ea" stroke-width="1.4"/>'
          f'<polyline points="{pts((g0, zb, 2.44), (back, zb, 2.0), (back, zb))}" fill="none" stroke="#dfe3ea" stroke-width="1.4"/>')
        # corner flags
        for zc in (ZF, ZN):
            fx, fy = P(g0, zc); tx, ty = P(g0, zc, 1.5)
            a(f'<line x1="{fx:.1f}" y1="{fy:.1f}" x2="{tx:.1f}" y2="{ty:.1f}" stroke="#ffffff" stroke-width="1.6"/><path d="M{tx:.1f} {ty:.1f} l{8*-s} 3 l{8*s} 3 z" fill="#ffcd00"/>')
    # players warming up, placed on the pitch in metres
    def player(i, X, Z, kit='#ffffff'):
        x, y = P(X, Z); s = 150.0 / Z
        return (f'<g class="pl" id="pl{i}" data-x="{X}" data-z="{Z}" transform="translate({x:.1f} {y:.1f}) scale({s:.2f})"><g class="body"><rect x="-3.5" y="-9" width="3" height="9" fill="#1e3f9a"/><rect x=".5" y="-9" width="3" height="9" fill="#1e3f9a"/>'
                f'<rect x="-5" y="-21" width="10" height="13" rx="2.5" fill="{kit}"/><circle cy="-25" r="4" fill="#e8c09a"/></g></g>')
    squad = [(-14, 150), (9, 128), (18, 158), (-22, 112), (-4, 160, '#ffcd00'), (-49, ZM, '#f07a14'), (30, 120), (49, ZM, '#7c3aed')]
    a('<g id="players">' + ''.join(player(i, *q) for i, q in enumerate(squad)) + '</g>')
    bx, by = P(-22, 112)
    a(f'<g id="ball"><ellipse id="ballShadow" cx="{bx:.1f}" cy="{by:.1f}" rx="5" ry="2" fill="#000" opacity=".3"/>'
      f'<g id="ballBody" transform="translate({bx:.1f} {by-4:.1f})"><circle r="5" fill="#ffffff"/><path d="M-3 -2 l3 2 l3 -2 M0 0 l0 3" stroke="#222" stroke-width="1" fill="none"/></g></g>')
    # rotating LED advertising hoardings along the near side
    a('<rect x="-40" y="600" width="1280" height="44" fill="#05070d"/>')
    for i in range(3):
        x0 = i * 400
        a(f'<a class="board" id="board{i}" href="/" aria-label="Advertising board">'
          f'<rect class="bbg" x="{x0+4}" y="603" width="392" height="38" rx="2" fill="#0a1838"/>'
          f'<g class="bmsg"><text x="{x0+200}" y="630" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="25" fill="#ffcd00" textLength="330" lengthAdjust="spacingAndGlyphs">MARCHING ON TOGETHER</text></g></a>')
    a('<rect x="-40" y="644" width="1280" height="56" fill="#30364a"/>')
    return '\n'.join(g)

def scoreboard_link():
    # sits on the far-stand roof, links to the match hub
    return '''<a href="/match-hub/" class="hot sb" aria-label="Scoreboard: open the Match Hub">
  <rect x="470" y="10" width="260" height="122" rx="6" fill="#14161c"/><rect x="478" y="18" width="244" height="106" rx="3" fill="#06070a"/>
  <rect x="478" y="18" width="244" height="22" fill="#1e3f9a"/><text x="600" y="35" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="17" fill="#ffcd00" letter-spacing="3">MATCH HUB</text>
  <g font-family="'Courier New', monospace" font-weight="700" fill="#ffcd00" style="filter:drop-shadow(0 0 3px #ffb000)">
    <text x="530" y="66" text-anchor="middle" font-size="15">LEEDS</text><text x="670" y="66" text-anchor="middle" font-size="15">AWAY</text>
    <text x="600" y="98" text-anchor="middle" font-size="30">0 - 0</text>
  </g>
  <text x="600" y="117" text-anchor="middle" font-family="'Courier New', monospace" font-weight="700" font-size="11" fill="#4dff88" id="sbTicker">KICK-OFF SOON</text>
  <text x="712" y="35" text-anchor="end" font-family="'Courier New', monospace" font-weight="700" font-size="11" fill="#ffffff" id="sbClock">15:00</text>
  <rect x="560" y="132" width="10" height="8" fill="#3a3f4b"/><rect x="630" y="132" width="10" height="8" fill="#3a3f4b"/>
</a>'''

def cards_link():
    # a fan of Football Tales trading cards dropped by the near touchline
    def card(x, y, rot, title, col):
        return (f'<g transform="translate({x} {y}) rotate({rot})">'
                f'<rect x="-48" y="-66" width="96" height="132" rx="6" fill="#ffffff" stroke="#0a1838" stroke-width="2"/>'
                f'<rect x="-42" y="-60" width="84" height="88" rx="3" fill="{col}"/>'
                f'<circle cy="-20" r="20" fill="#f7f2e4" opacity=".9"/><path d="M-10 -20 l7 -9 l12 0 l7 9 l-7 9 l-12 0 z" fill="#0a1838" opacity=".8"/>'
                f'<rect x="-42" y="32" width="84" height="16" fill="#ffcd00"/><text y="44" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="13" fill="#0a1838" textLength="70" lengthAdjust="spacingAndGlyphs">{title}</text>'
                f'<text y="60" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="9" fill="#1e3f9a" textLength="74" lengthAdjust="spacingAndGlyphs">FOOTBALL TALES</text></g>')
    return ('<a href="/football-tales/" class="hot cards" aria-label="Football Tales (coming soon): open the trading cards">'
            '<ellipse cx="860" cy="594" rx="120" ry="12" fill="#000" opacity=".25"/>'
            + card(805, 520, -14, 'AWAY DAYS', '#1e3f9a') + card(860, 510, 0, 'HOME DAYS', '#2f7d3a') + card(918, 524, 13, 'THE PUBS', '#c0392b')
            + '<g transform="rotate(-6 862 440)"><rect x="810" y="428" width="104" height="24" rx="4" fill="#d22630" stroke="#ffffff" stroke-width="2"/><text x="862" y="446" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="17" fill="#ffffff" letter-spacing="2" textLength="88" lengthAdjust="spacingAndGlyphs">COMING SOON</text></g></a>')
