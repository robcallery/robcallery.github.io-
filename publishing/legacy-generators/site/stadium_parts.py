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
  <rect class="sheen" x="-120" y="8" width="60" height="286" fill="#fff" opacity=".18" transform="skewX(-20)"/>
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
    # pitch with stripes
    a('<path d="M90 268 L1110 268 L1400 700 L-200 700 Z" fill="url(#stPitch)"/>')
    ys = [268 + (700 - 268) * ((i / 12) ** 1.35) for i in range(13)]
    for i in range(12):
        if i % 2: continue
        y0, y1 = ys[i], ys[i + 1]
        def xl(y): return 90 - (y - 268) / 432 * 290
        def xr(y): return 1110 + (y - 268) / 432 * 290
        a(f'<path d="M{xl(y0):.1f} {y0:.1f} L{xr(y0):.1f} {y0:.1f} L{xr(y1):.1f} {y1:.1f} L{xl(y1):.1f} {y1:.1f} Z" fill="#ffffff" opacity=".06"/>')
    line = 'fill="none" stroke="#f4f4ee" stroke-width="3" stroke-linejoin="round"'
    a(f'<path d="M120 282 L1080 282 L1300 640" {line}/><path d="M120 282 L-100 640" {line}/>')
    a(f'<path d="M600 282 L600 700" {line}/><ellipse cx="600" cy="420" rx="170" ry="52" {line}/><circle cx="600" cy="420" r="4" fill="#f4f4ee"/>')
    a(f'<path d="M150 300 L330 300 L250 420 L40 420" {line}/><path d="M1050 300 L870 300 L950 420 L1160 420" {line}/>')
    # goals
    for x, s in ((96, 1), (1104, -1)):
        a(f'<path d="M{x} 300 L{x} 274 L{x+s*44} 286 L{x+s*44} 316" fill="none" stroke="#ffffff" stroke-width="4"/><path d="M{x} 300 L{x+s*44} 316" stroke="#ffffff" stroke-width="1" opacity=".5"/>')
    # players warming up
    def player(x, y, s, kit='#ffffff'):
        return (f'<g transform="translate({x} {y}) scale({s})"><rect x="-3.5" y="-9" width="3" height="9" fill="#1e3f9a"/><rect x=".5" y="-9" width="3" height="9" fill="#1e3f9a"/>'
                f'<rect x="-5" y="-21" width="10" height="13" rx="2.5" fill="{kit}"/><circle cy="-25" r="4" fill="#e8c09a"/></g>')
    a(player(470, 360, 1.6) + player(700, 400, 1.9) + player(820, 330, 1.4) + player(380, 470, 2.3) + player(560, 330, 1.3, '#ffcd00'))
    a('<circle cx="640" cy="404" r="5" fill="#ffffff"/><path d="M637 401 l3 2 l3 -2" stroke="#222" stroke-width="1" fill="none"/>')
    # advertising boards along near side
    a('<path d="M-40 600 L1240 600 L1240 640 L-40 640 Z" fill="#0a1838"/>')
    for i, t in enumerate(['MARCHING ON TOGETHER', 'CALLERY.CO.UK', 'ONE BEER AT A TIME', 'LEEDS · LEEDS · LEEDS']):
        a(f'<text x="{150 + i*300}" y="628" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="24" fill="{["#ffcd00", "#ffffff"][i % 2]}" textLength="230" lengthAdjust="spacingAndGlyphs">{t}</text>')
    a('<rect x="-40" y="640" width="1280" height="60" fill="#30364a"/>')
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
    return ('<a href="/football-tales/" class="hot cards" aria-label="Football Tales: open the trading cards">'
            '<ellipse cx="1000" cy="652" rx="120" ry="14" fill="#000" opacity=".3"/>'
            + card(945, 578, -14, 'AWAY DAYS', '#1e3f9a') + card(1000, 568, 0, 'HOME DAYS', '#2f7d3a') + card(1058, 582, 13, 'THE PUBS', '#c0392b') + '</a>')
