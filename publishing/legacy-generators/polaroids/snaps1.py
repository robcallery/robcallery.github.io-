from snaplib import *

S = {}  # city -> (title, note, svg)

def add(city, title, note, sky, body, defs=''):
    slug = ''.join(ch for ch in city.lower() if ch.isalnum())
    S[city] = (title, note, scene(slug, sky, body, defs))

# ---------------- Leeds: Elland Road ----------------
def leeds():
    b = sun(330, 60, 14) + cloud(90, 60, .9) + cloud(260, 40, .7)
    b += R(0, 150, W, 120, '#2a3a64')  # distant stands silhouette
    b += P('M0 150 L60 128 L60 270 L0 270 Z', '#24335a') + P('M400 150 L340 128 L340 270 L400 270 Z', '#24335a')
    # East Stand
    b += R(40, 112, 320, 8, '#c9d2e3') + ''.join(P(f'M{40+i*16} 112 L{48+i*16} 100 L{56+i*16} 112', 'none', 'stroke="#c9d2e3" stroke-width="1.5"') for i in range(20))
    b += R(40, 120, 320, 110, '#1e3f9a') + ''.join(R(40 + i * 8, 120, 1, 70, '#2a4fb0') for i in range(40))
    b += T(200, 166, 'ELLAND ROAD', 40, '#ffffff', 'textLength="236" lengthAdjust="spacingAndGlyphs"')
    b += R(110, 174, 180, 3, '#ffcd00')
    b += R(40, 190, 320, 4, '#f7f2e4') + ''.join(R(48 + i * 18, 196, 12, 10, '#e8d6a8') for i in range(18))
    b += R(40, 208, 320, 22, '#16307a')
    for x in (100, 190, 280):
        b += R(x, 212, 22, 18, '#f0c35a') + R(x + 10.5, 212, 1, 18, '#b38a2e') + R(x - 2, 206, 26, 5, '#ffcd00') + T(x + 11, 210, 'TURNSTILE', 4, '#1e3f9a')
    # banners
    for x, txt in ((44, ['SIDE', 'BEFORE', 'SELF']), (336, ['ALL', 'LEEDS', 'AREN\'T', 'WE'])):
        b += R(x, 122, 20, 64, '#ffcd00') + R(x + 2, 126, 16, 56, '#1e3f9a') + ''.join(T(x + 10, 138 + i * 12, t, 7, '#fff', 'textLength="14" lengthAdjust="spacingAndGlyphs"') for i, t in enumerate(txt))
    b += road(230, '#30364a')
    b += crowd(46, 10, 390, 238, 11, 1.05, 30, ['#ffffff', '#ffcd00', '#1d4ed8', '#ffffff'])
    return b
add('Leeds', 'Elland Road', 'Home since 1919. The East Stand was the world\'s biggest cantilever stand when it opened in 1993.', 'day', leeds())

# ---------------- Wakefield: Cathedral ----------------
def wakefield():
    st = '#b9a58a'; dk = shade(st, -.18)
    b = sun(70, 70, 15) + cloud(300, 70, .8) + cloud(150, 40, .6)
    b += hills(232, '#8fb49a', 3, 10)
    # nave
    b += R(40, 180, 200, 70, st) + P('M40 180 L140 150 L240 180 Z', dk)
    b += windows(56, 196, 8, 1, 10, 28, 12, 0, '#4a5878', arch=True)
    # tower
    tx = 250; b += R(tx, 120, 56, 130, st) + R(tx + 40, 120, 16, 130, dk)
    b += battlements(tx, 120, 56, st, 5, 6)
    b += arch_win(tx + 16, 150, 16, 34, '#4a5878') + clockface(tx + 24, 202, 8)
    for px in (tx + 2, tx + 51):
        b += spire(px + 1.5, 120, 6, 16, st)
    b += spire(tx + 28, 116, 34, 108, '#9a8a73')
    b += R(tx + 27, 4, 2, 6, '#c9a227') + L(tx + 23, 7, tx + 33, 7, '#c9a227', 1.5)
    b += ground(250, '#5f8f55', '#79a86b') + R(0, 268, W, 52, '#a69d8c')
    b += tree(20, 254, 1.2) + tree(370, 254, 1.4) + tree(340, 256, 1)
    b += crowd(10, 30, 360, 276, 2, 1.05, 30)
    return b
add('Wakefield', 'Wakefield Cathedral', 'Its spire is the tallest in Yorkshire - 75 metres.', 'day', wakefield())

# ---------------- York: Minster ----------------
def york():
    st = '#d8c7a0'; dk = shade(st, -.16); win = '#5a6a8c'
    b = cloud(80, 50, .8) + cloud(320, 80, .9) + sun(350, 40, 12)
    # central tower
    b += R(160, 70, 80, 120, st) + R(220, 70, 20, 120, dk) + battlements(160, 70, 80, st, 4, 7)
    b += windows(170, 90, 3, 1, 12, 44, 13, 0, win, arch=True)
    # west towers
    for x in (40, 310):
        b += R(x, 92, 50, 160, st) + R(x + 36, 92, 14, 160, dk) + battlements(x, 92, 50, st, 4, 7)
        b += windows(x + 9, 110, 2, 2, 12, 34, 9, 16, win, arch=True)
        for px in (x, x + 46):
            b += R(px, 80, 4, 14, st)
    # west front between towers
    b += R(90, 140, 220, 112, st) + P('M90 140 L200 104 L310 140 Z', dk)
    b += arch_win(170, 150, 60, 74, win) + ''.join(L(178 + i * 11, 160, 178 + i * 11, 224, st, 1.4) for i in range(5)) + C(200, 166, 14, 'none', f'stroke="{st}" stroke-width="2"')
    b += arch_win(186, 226, 28, 26, '#3b2a1a')
    b += windows(104, 160, 2, 1, 14, 56, 18, 0, win, arch=True) + windows(264, 160, 2, 1, 14, 56, 4, 0, win, arch=True)
    b += R(0, 252, W, 68, '#b9b1a1') + R(0, 252, W, 3, '#d2cbbb')
    b += crowd(22, 10, 390, 264, 5, 1.05, 40)
    return b
add('York', 'York Minster', 'Took 250 years to build. The Great East Window is the size of a tennis court.', 'day', york())

# ---------------- Knaresborough: viaduct ----------------
def knaresborough():
    st = '#b9a07a'; dk = shade(st, -.2)
    b = cloud(90, 50, .8) + cloud(300, 40, .7) + sun(340, 70, 13)
    b += hills(150, '#7da57a', 7, 14) + hills(175, '#5f8f55', 9, 12)
    # houses on the cliff (right)
    for i, (x, y, c) in enumerate([(300, 120, '#e8dcc4'), (330, 110, '#d9c7a4'), (360, 118, '#efe4cf'), (280, 135, '#d6c09a')]):
        b += R(x, y, 26, 26, c) + P(f'M{x-2} {y} L{x+13} {y-10} L{x+28} {y} Z', '#6b4a3a') + R(x + 8, y + 8, 6, 7, '#4a5878')
    # viaduct
    b += R(0, 132, W, 14, st) + battlements(0, 132, W, st, 4, 5)
    for i in range(5):
        x = 10 + i * 80
        b += R(x, 146, 22, 110, st) + R(x + 16, 146, 6, 110, dk)
        b += P(f'M{x+22} 146 L{x+22} 160 A29 29 0 0 1 {x+80} 160 L{x+80} 146 Z', st)
    b += water(215, '#3f7f8f', 4, 18)
    b += P('M0 215 Q120 205 400 216 L400 220 L0 220 Z', '#5f8f55')
    b += boat(120, 245, 1.1, '#c0392b', '#e8d6a8') + boat(230, 262, 1, '#1d4ed8', '#fff') + boat(320, 240, .9, '#2a8a46', '#ffcd00')
    b += person(120, 244, '#ffcd00', SKIN[0], .9) + person(232, 261, '#d22630', SKIN[2], .9)
    return b
add('Knaresborough', 'The Nidd Viaduct', 'Rowing boats on the river under the viaduct - the classic Knaresborough shot.', 'day', knaresborough())

# ---------------- Paris: Eiffel Tower ----------------
def paris():
    ir = '#8b5e3c'; dk = shade(ir, -.2)
    b = sun(320, 210, 22, '#ffd27a', '#ff9e5a') + cloud(80, 70, .8, '#ffe1c7') + cloud(300, 60, .6, '#ffe1c7')
    cx = 200
    # legs
    b += P(f'M{cx-80} 262 Q{cx-40} 200 {cx-22} 120 L{cx-12} 120 Q{cx-26} 200 {cx-50} 262 Z', ir)
    b += P(f'M{cx+80} 262 Q{cx+40} 200 {cx+22} 120 L{cx+12} 120 Q{cx+26} 200 {cx+50} 262 Z', dk)
    b += P(f'M{cx-50} 262 Q{cx} 205 {cx+50} 262 L{cx+44} 262 Q{cx} 214 {cx-44} 262 Z', ir)
    b += R(cx - 62, 196, 124, 8, ir)
    b += P(f'M{cx-22} 120 L{cx+22} 120 L{cx+14} 60 L{cx-14} 60 Z', ir) + P(f'M{cx} 120 L{cx+22} 120 L{cx+14} 60 L{cx} 60 Z', dk)
    b += R(cx - 26, 116, 52, 6, ir)
    b += P(f'M{cx-14} 60 L{cx+14} 60 L{cx+3} 14 L{cx-3} 14 Z', ir) + R(cx - 1, 2, 2, 14, ir) + R(cx - 9, 56, 18, 5, ir)
    for y in range(130, 196, 10):
        b += L(cx - 30 - (y - 120) * .35, y, cx + 30 + (y - 120) * .35, y + 8, dk, .8, 'opacity=".6"') + L(cx + 30 + (y - 120) * .35, y, cx - 30 - (y - 120) * .35, y + 8, dk, .8, 'opacity=".6"')
    b += hills(250, '#4a6b45', 3, 6, 6) + ground(262, '#6b8f4e', '#86a865')
    b += tree(40, 266, 1.3, '#4f7f45') + tree(80, 268, 1.1, '#4f7f45') + tree(330, 266, 1.3, '#4f7f45') + tree(370, 268, 1.2, '#4f7f45')
    b += crowd(14, 110, 300, 282, 3, 1.3, 26)
    return b
add('Paris', 'Tour Eiffel', 'Built as a temporary entrance arch for the 1889 World\'s Fair. Never left.', 'sunset', paris())

# ---------------- Westminster: Big Ben ----------------
def westminster():
    st = '#c9b27e'; dk = shade(st, -.18); win = '#6a5a3c'
    b = cloud(90, 60, .8, '#eef2f6') + cloud(250, 40, .7, '#eef2f6')
    # parliament
    b += R(0, 170, 230, 70, st) + windows(8, 182, 14, 2, 8, 16, 7.6, 10, win)
    b += ''.join(spire(10 + i * 30, 172, 6, 14, st) for i in range(8))
    b += R(120, 140, 30, 34, st) + spire(135, 142, 30, 28, '#5a6b6e')
    # Elizabeth Tower
    x = 270
    b += R(x, 90, 50, 150, st) + R(x + 38, 90, 12, 150, dk)
    b += windows(x + 6, 150, 4, 5, 6, 12, 4.6, 5, win)
    b += R(x - 4, 50, 58, 42, st) + R(x + 40, 50, 14, 42, dk) + clockface(x + 25, 71, 15, '#f7f2e4', '#1b1b1b', (10, 10))
    b += R(x - 2, 38, 54, 12, st) + windows(x + 4, 40, 5, 1, 6, 8, 3.6, 0, win)
    b += P(f'M{x-2} 38 L{x+25} 4 L{x+52} 38 Z', '#3f4c4f') + P(f'M{x+25} 38 L{x+25} 4 L{x+52} 38 Z', '#2f3a3d') + R(x + 24, -6, 2, 12, '#c9a227')
    b += water(240, '#56708a', 6, 14)
    # bridge + red bus
    b += R(0, 236, W, 10, '#4f6b55') + ''.join(C(30 + i * 60, 236, 2.5, '#e6d27a') for i in range(7))
    b += R(150, 220, 46, 16, '#d22630', 3) + windows(154, 223, 5, 1, 6, 5, 2.4, 0, '#2b3a55') + windows(154, 230, 5, 1, 6, 4, 2.4, 0, '#2b3a55') + C(160, 236, 3, '#222') + C(188, 236, 3, '#222')
    b += boat(80, 270, 1.4, '#1b1b1b', '#e8e2d0')
    return b
add('Westminster', 'Big Ben', 'Technically the bell\'s called Big Ben - the tower is the Elizabeth Tower.', 'grey', westminster())

# ---------------- EPCOT: geodesic sphere ----------------
def epcot():
    cx, cy, r = 200, 150, 95
    defs = f'<clipPath id="epc"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>'
    b = stars(8, 50) + moon(340, 50, 12)
    b += fireworks(80, 80, 30, '#ffcd00') + fireworks(330, 110, 24, '#e84a7f') + fireworks(110, 150, 18, '#4dd2ff')
    g = C(cx, cy, r, '#9aa7b8')
    tri = ''
    s = 19
    for row in range(-6, 7):
        for col in range(-6, 7):
            x0 = cx + col * s + (row % 2) * s / 2; y0 = cy + row * s * .87
            tone = 0.15 * math.sin(col * .7 + row * .5) - (x0 - cx) / r * .18
            f1 = shade('#a9b5c6', tone if tone > 0 else tone)
            tri += P(f'M{x0:.1f} {y0:.1f} l{s/2:.1f} {s*.87:.1f} l{-s:.1f} 0 Z', f1, 'stroke="#6c7a8f" stroke-width=".6"')
            tri += P(f'M{x0:.1f} {y0:.1f} l{s:.1f} 0 l{-s/2:.1f} {s*.87:.1f} Z', shade(f1, -.08), 'stroke="#6c7a8f" stroke-width=".6"')
    b += f'<g clip-path="url(#epc)">{g}{tri}</g>' + C(cx, cy, r, 'none', 'stroke="#56637a" stroke-width="2"')
    b += C(cx - 30, cy - 40, 30, '#fff', 'opacity=".12"')
    for lx in (-50, 0, 50):
        b += P(f'M{cx+lx-8} {cy+r-6} L{cx+lx-14} 262 L{cx+lx+14} 262 L{cx+lx+8} {cy+r-6} Z', '#56637a')
    b += ground(262, '#2a3048') + R(0, 262, W, 2, '#4a5070')
    b += crowd(30, 10, 390, 272, 9, 1.0, 36)
    return b
add('EPCOT', 'The big golf ball', 'Spaceship Earth - a geodesic sphere made of 11,324 triangles.', 'night', epcot(), '<clipPath id="epc"><circle cx="200" cy="150" r="95"/></clipPath>')

# ---------------- LBA ----------------
def lba():
    b = cloud(80, 50, .9, '#f2f4f7') + cloud(280, 70, .8, '#f2f4f7') + cloud(180, 30, .6, '#f2f4f7')
    b += hills(180, '#8fae86', 21, 16) + hills(200, '#7aa070', 22, 12)
    # dry stone walls
    for y in (205, 222):
        b += PL(f'M0 {y} Q100 {y-6} 200 {y} T400 {y}', '#a39a85', 2)
    # terminal
    b += R(220, 196, 170, 40, '#dfe3ea') + R(220, 196, 170, 6, '#1d4ed8') + windows(228, 208, 10, 1, 12, 16, 4.4, 0, '#7fb0d9')
    b += T(305, 202, 'LEEDS BRADFORD', 7, '#fff', 'letter-spacing="1"')
    b += R(370, 150, 10, 46, '#cfd5de') + R(362, 140, 26, 12, '#7fb0d9') + R(360, 136, 30, 4, '#56637a')
    b += R(0, 236, W, 84, '#4b505c') + ''.join(R(10 + i * 50, 276, 26, 3, '#f7f2e4') for i in range(8)) + R(0, 236, W, 2, '#6b7080')
    b += plane(150, 250, 1.6, '#ffffff', '#1d4ed8')
    b += plane(300, 70, .7, '#ffffff', '#d22630')
    return b
add('Leeds Bradford Airport', 'Up on the hill at Yeadon', 'England\'s highest airport, about 200 metres up - hence the fog.', 'grey', lba())
