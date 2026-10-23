# Travelling F1 in 2026 - polaroids (illustrations, no logos). Keys are "f1-2026|City" so they don't clash with other books.
from snaplib import *
import random, math, json
S = {}
INFO = json.load(open('/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/f1_snaps.json'))
def add(city, sky, body):
    t, n = INFO[city]
    slug = 'f1' + ''.join(ch for ch in city.lower() if ch.isalnum())
    S['f1-2026|' + city] = (t, n, scene(slug, sky, body))
WIN = '#4a5878'; LIT = '#ffd98a'
def day(): return sun(330, 50, 13) + cloud(80, 46, .7) + cloud(240, 34, .5)
def kerb(y, x0=0, x1=400, h=8, w=20):
    return ''.join(R(x, y, w, h, '#e10600' if (x // w) % 2 else '#f4f4f4') for x in range(x0, x1, w))
def tower(x, base, w, h, f, win=WIN, cols=None, rows=None, top=None):
    g = R(x, base - h, w, h, f) + R(x + w * .7, base - h, w * .3, h, shade(f, -.12))
    c = cols or max(1, int(w // 10)); r = rows or max(1, int(h // 14))
    g += windows(x + 4, base - h + 8, c, r, 4, 6, (w - 8) / c, (h - 12) / r, win)
    if top: g += top
    return g
def skyline(base, seed, x0=0, x1=400, hmin=40, hmax=120, cols=('#9aa8bd', '#7d8ca6', '#b6c1d1', '#6c7a93'), win=WIN):
    rnd = random.Random(seed); g = ''; x = x0
    while x < x1:
        w = rnd.randint(18, 36); h = rnd.randint(hmin, hmax)
        g += tower(x, base, w, h, rnd.choice(cols), win); x += w + rnd.randint(0, 6)
    return g

# 1 Melbourne - lake, skyline, kerb
def melbourne():
    b = day() + skyline(200, 11, 20, 380, 50, 140) + R(0, 198, 400, 6, '#5d8f4a') + water(204, '#3f86b5', 3, 12)
    b += R(0, 268, 400, 52, '#3a3d46') + kerb(262) + ''.join(tree(x, 204, .55, '#4f8a45') for x in (30, 360))
    return b
# 2 Shanghai - Bund at night with the pearl tower
def shanghai():
    b = stars(2, 50, 150) + skyline(220, 21, 0, 400, 60, 150, ('#2b3556', '#334068', '#26304d'), LIT)
    x = 250
    b += R(x - 3, 70, 6, 150, '#c9c9d6') + C(x, 175, 22, '#d23a6a') + C(x, 105, 15, '#d23a6a') + C(x, 70, 6, '#d23a6a') + L(x, 64, x, 30, '#c9c9d6', 3)
    b += L(x - 18, 220, x - 4, 180, '#c9c9d6', 4) + L(x + 18, 220, x + 4, 180, '#c9c9d6', 4)
    b += water(222, '#16244a', 4, 16, '#ffd98a') + R(0, 286, 400, 34, '#5b4a3b') + R(0, 282, 400, 5, '#cbb89a')
    return b
# 3 Suzuka - the Ferris wheel
def suzuka():
    b = day() + hills(220, '#6aa860', 31, 16) + ground(240, '#4f8a45')
    cx, cy, r = 220, 140, 92
    b += C(cx, cy, r, 'none', 'stroke="#e8e8ee" stroke-width="5"')
    for k in range(16):
        a = k * math.pi / 8; x = cx + r * math.cos(a); y = cy + r * math.sin(a)
        b += L(cx, cy, x, y, '#e8e8ee', 1.5) + R(x - 7, y - 4, 14, 12, ['#e84a7f', '#ffcd00', '#1d9bf0', '#2a8a46'][k % 4], 2)
    b += C(cx, cy, 9, '#e8e8ee') + L(cx, cy, cx - 50, 245, '#cfd2da', 6) + L(cx, cy, cx + 50, 245, '#cfd2da', 6)
    b += R(0, 262, 400, 58, '#3a3d46') + kerb(256)
    return b
# 4 Miami - Wynwood murals
def miami():
    b = day() + R(0, 110, 400, 160, '#f2e6d0')
    cols = ['#ff4d6d', '#ffbe0b', '#3a86ff', '#8338ec', '#06d6a0', '#fb5607']
    rnd = random.Random(4)
    for i in range(6):
        x = i * 68 + 4; c = cols[i]
        b += R(x, 120, 62, 140, c)
        b += C(x + 31, 170, 18, cols[(i + 2) % 6]) + P(f'M{x} 240 Q{x+31} {200+rnd.randint(-20,20)} {x+62} 240 L{x+62} 260 L{x} 260 Z', cols[(i + 3) % 6])
        b += R(x + 10, 140, 42, 6, '#ffffff', 3)
    b += R(0, 262, 400, 58, '#c9c2b4') + palm(30, 262, 1.1) + palm(372, 262, 1.0, -6)
    return b
# 5 Montreal - Old Port with the market dome
def montreal():
    b = day() + R(60, 130, 280, 90, '#c9b79a') + windows(76, 150, 12, 3, 8, 12, 22, 22, WIN)
    b += E(200, 130, 34, 30, '#8d9aa5') + R(166, 120, 68, 12, '#c9b79a') + R(196, 86, 8, 14, '#8d9aa5') + C(200, 84, 4, '#8d9aa5')
    b += R(330, 90, 26, 130, '#b8a789') + clockface(343, 110, 9) + P('M326 90 L343 64 L360 90 Z', '#7b8a96')
    b += water(220, '#3a6f98', 5, 14) + boat(110, 252, 1.0) + boat(270, 262, .8, '#1d4ed8')
    return b
# 6 Monaco - yachts in Port Hercule
def monaco():
    b = day() + hills(150, '#7aa36a', 61, 30)
    rnd = random.Random(6)
    for i in range(22):
        x = rnd.randint(0, 390); y = rnd.randint(120, 190); w = rnd.randint(16, 30)
        b += R(x, y, w, 210 - y, rnd.choice(['#f3ead8', '#f2d7b6', '#e9c9a6', '#ffffff'])) + windows(x + 3, y + 6, 2, 3, 3, 4, w / 2 - 2, 10, WIN)
    b += R(0, 205, 400, 4, '#d8d0c0') + water(209, '#2f7fb5', 6, 14)
    for x, s in ((40, 1.4), (150, 1.6), (270, 1.3), (350, 1.0)):
        b += P(f'M{x} {258} l{70*s} 0 l{-10*s} {12*s} l{-50*s} 0 Z', '#ffffff') + R(x + 14 * s, 248, 34 * s, 10, '#ffffff') + R(x + 20 * s, 241, 18 * s, 8, '#dfe6ee') + L(x + 30 * s, 241, x + 30 * s, 215, '#ffffff', 1.5)
    return b
# 7 Barcelona - Park Güell mosaics
def barcelona():
    b = day() + hills(210, '#7aa860', 71, 12)
    b += R(60, 150, 90, 90, '#d9b98a') + P('M54 152 Q105 110 156 152 Z', '#7a5a3a') + P('M90 120 Q105 70 120 120 Z', '#ffffff')
    for k in range(8): b += C(92 + k * 4, 116 - abs(k - 3.5) * 4, 2.4, ['#1d4ed8', '#d22630', '#2a8a46'][k % 3])
    b += R(250, 160, 80, 80, '#e9d3a8') + P('M244 162 Q290 120 336 162 Z', '#3f6aa8') + R(282, 100, 14, 62, '#e9d3a8') + P('M276 100 L289 76 L302 100 Z', '#e04a3a')
    rnd = random.Random(7)
    wave = ''.join(R(x, 240 + 10 * math.sin(x / 30), 12, 10, rnd.choice(['#2a8a46', '#1d4ed8', '#ffcd00', '#d22630', '#ffffff', '#f07a14'])) for x in range(0, 400, 12))
    b += wave + R(0, 262, 400, 58, '#d8c39a')
    return b
# 8 Spielberg - green hills and the grandstand
def spielberg():
    b = day() + hills(170, '#8fb38a', 81, 34) + hills(200, '#5e9a52', 82, 22) + ground(232, '#4f8a45')
    b += R(150, 180, 200, 50, '#3a4250') + P('M140 180 L360 180 L350 168 L150 168 Z', '#c9ccd4')
    rnd = random.Random(8)
    for i in range(90): b += R(156 + (i % 30) * 6.4, 186 + (i // 30) * 12, 4, 6, rnd.choice(PEOPLE))
    b += R(0, 250, 400, 40, '#3a3d46') + kerb(244) + R(0, 290, 400, 30, '#4f8a45')
    return b
# 9 Silverstone - the Wing
def silverstone():
    b = day() + ground(230, '#4f8a45') + R(30, 150, 340, 66, '#e8ecf2') + windows(40, 170, 16, 2, 14, 10, 20.5, 18, '#7aa0c8')
    b += P('M20 150 Q200 100 380 150 L380 158 Q200 112 20 158 Z', '#ffffff') + P('M20 150 Q200 100 380 150', 'none', 'stroke="#b7c0cc" stroke-width="2"')
    b += R(0, 236, 400, 30, '#3a3d46') + ''.join(R(x, 249, 14, 3, '#ffffff') for x in range(10, 400, 30)) + kerb(230, h=6) + R(0, 266, 400, 54, '#4f8a45')
    return b
# 10 Spa - Eau Rouge in the rain
def spa():
    b = cloud(80, 50, 1.2, '#c9d1da') + cloud(260, 36, 1.4, '#bcc5cf') + hills(150, '#2f5a36', 101, 30)
    b += ''.join(pine(x, 200 + (x % 3) * 6, .9) for x in range(0, 400, 26))
    b += P('M-10 300 Q90 300 150 250 Q220 190 410 140 L410 175 Q240 220 180 265 Q120 315 -10 320 Z', '#3a3d46')
    b += P('M-10 300 Q90 300 150 250 Q220 190 410 140', 'none', 'stroke="#e10600" stroke-width="5" stroke-dasharray="12 12"')
    b += P('M-10 320 Q120 315 180 265 Q240 220 410 175', 'none', 'stroke="#f4f4f4" stroke-width="3"')
    b += ''.join(L(x, 60, x - 8, 100, '#9fb3c8', 1) for x in range(20, 400, 23))
    return b
# 11 Budapest - Parliament on the Danube
def budapest():
    b = R(0, 0, 400, 320, 'none') + sun(80, 70, 16, '#ffd6a0') + R(30, 150, 340, 60, '#efe2c8') + windows(40, 162, 24, 3, 6, 10, 13.5, 14, '#7a6a55', True)
    for x in range(40, 370, 28): b += P(f'M{x} 150 L{x+4} 130 L{x+8} 150 Z', '#d8c6a6')
    b += E(200, 132, 34, 30, '#c4553f') + R(194, 70, 12, 40, '#efe2c8') + P('M190 72 L200 40 L210 72 Z', '#c4553f')
    b += R(120, 120, 10, 30, '#efe2c8') + P('M117 122 L125 96 L133 122 Z', '#c4553f') + R(270, 120, 10, 30, '#efe2c8') + P('M267 122 L275 96 L283 122 Z', '#c4553f')
    b += water(210, '#3b5f8a', 11, 14, '#ffd6a0')
    return b
# 12 Zandvoort - dunes and a banked corner
def zandvoort():
    b = day() + P('M-10 200 Q60 150 130 190 Q200 140 280 185 Q340 150 410 175 L410 320 L-10 320 Z', '#e3cf98')
    rnd = random.Random(12)
    b += ''.join(L(x, 200 - rnd.randint(0, 25), x + rnd.randint(-4, 4), 185 - rnd.randint(25, 40), '#7d9a52', 1.5) for x in range(0, 400, 9))
    b += P('M-10 300 Q200 200 410 260 L410 290 Q200 235 -10 320 Z', '#3a3d46') + P('M-10 300 Q200 200 410 260', 'none', 'stroke="#ff7a00" stroke-width="5" stroke-dasharray="14 10"')
    b += ''.join(R(x, 140, 3, 64, '#ffffff') + P(f'M{x+3} 140 l16 6 l-16 6 Z', '#ff7a00') for x in (60, 170, 300))
    return b
# 13 Monza - the old banking in the park
def monza():
    b = day() + hills(205, '#6aa060', 131, 10) + ground(208, '#5a9a4a') + ''.join(tree(x, 212, 1.0, '#3d7b40') for x in range(-10, 410, 36))
    b += P('M-10 300 L120 300 Q300 290 360 160 L410 140 L410 320 L-10 320 Z', '#b9b4aa') + P('M120 300 Q300 290 360 160', 'none', 'stroke="#8d877c" stroke-width="3"')
    b += ''.join(L(150 + k * 30, 296 - k * k * 3, 158 + k * 30, 270 - k * k * 3, '#8d877c', 2) for k in range(7))
    b += R(0, 300, 400, 20, '#4f8a45')
    return b
# 14 Madrid - Gran Vía and the domed corner building
def madrid():
    b = day() + R(0, 120, 120, 150, '#e8dcc6') + windows(10, 130, 5, 6, 8, 12, 21, 22, WIN) + R(290, 110, 110, 160, '#efe3cc') + windows(298, 120, 4, 6, 8, 12, 25, 22, WIN)
    b += R(140, 120, 120, 150, '#f4ecdc') + windows(150, 150, 5, 5, 8, 12, 22, 22, WIN) + E(200, 118, 46, 36, '#2a3a4a') + R(154, 112, 92, 10, '#f4ecdc')
    b += R(196, 66, 8, 20, '#d9b04a') + P('M186 70 L200 54 L214 70 Z', '#d9b04a') + ''.join(C(170 + k * 15, 100, 2, '#d9b04a') for k in range(5))
    b += road(270, '#3a3d46') + ''.join(R(x, 292, 20, 3, '#ffffff') for x in range(10, 400, 40))
    return b
# 15 Baku - the Flame Towers at night
def baku():
    b = stars(15, 40, 140)
    for x, h, c in ((110, 160, '#ff7a1a'), (200, 200, '#ffa41a'), (290, 150, '#ff5a1a')):
        b += P(f'M{x-34} 230 Q{x-40} {230-h*.6} {x} {230-h} Q{x+40} {230-h*.6} {x+34} 230 Z', c, 'opacity=".92"')
        b += ''.join(L(x - 30, y, x + 30, y, '#ffe1a8', .8, 'opacity=".5"') for y in range(int(230 - h * .8), 230, 10))
    b += R(0, 230, 400, 40, '#2b3045') + R(40, 196, 30, 34, '#b39a78') + P('M36 196 L55 182 L74 196 Z', '#8a7458')
    b += water(270, '#14223f', 15, 12, '#ffb35a')
    return b
# 16 Kuala Lumpur - the twin towers
def kualalumpur():
    b = day() + skyline(262, 16, 0, 400, 30, 90, ('#b6c1d1', '#9aa8bd', '#c9d2de'))
    for x in (155, 245):
        for k, (w, y) in enumerate(((40, 120), (34, 80), (26, 55), (16, 38))):
            b += R(x - w / 2, y, w, 262 - y if k == 0 else 40, '#c8ced8') + R(x, y, w / 2, 262 - y if k == 0 else 40, '#a9b1bd')
        b += L(x, 38, x, 8, '#c8ced8', 3)
    b += R(175, 150, 50, 8, '#a9b1bd') + L(185, 158, 175, 180, '#a9b1bd', 2) + L(215, 158, 225, 180, '#a9b1bd', 2)
    b += ground(262, '#4f8a45') + palm(40, 262, 1.0) + palm(360, 262, 1.1, -6)
    return b
# 17 Singapore - three towers and the ship on top
def singapore():
    b = stars(17, 30, 120) + skyline(230, 17, 0, 400, 50, 120, ('#2b3556', '#334068'), LIT)
    for x in (120, 200, 280):
        b += P(f'M{x-22} 230 L{x-16} 90 L{x+16} 90 L{x+22} 230 Z', '#d6dbe4') + windows(x - 14, 100, 3, 9, 4, 6, 10, 14, LIT)
    b += P('M80 90 L340 84 L346 76 L74 82 Z', '#bfc6d2') + E(330, 80, 18, 5, '#9fb0c4')
    b += water(232, '#101c3a', 17, 14, '#ffd98a')
    for x in (30, 60, 360): b += L(x, 290, x, 250, '#7a5ab0', 3) + P(f'M{x-14} 250 Q{x} 236 {x+14} 250 Z', '#b45ce0')
    return b
# 18 Austin - the State Capitol
def austin():
    b = day() + ground(240, '#5a9a4a') + R(70, 170, 260, 70, '#e7c3a8') + windows(80, 180, 18, 3, 6, 10, 14, 18, WIN)
    b += R(165, 120, 70, 50, '#e7c3a8') + windows(172, 128, 6, 2, 5, 9, 11, 18, WIN) + E(200, 118, 38, 34, '#e0b89c') + R(196, 76, 8, 14, '#e0b89c') + C(200, 72, 5, '#e0b89c')
    b += R(192, 64, 16, 4, '#d9b04a') + ''.join(R(80 + k * 30, 240, 10, 22, '#f2f0ea') for k in range(9))
    return b
# 19 Mexico City - Palacio de Bellas Artes
def mexicocity():
    b = day() + R(60, 150, 280, 100, '#f2efe8') + ''.join(R(80 + k * 30, 170, 10, 80, '#e0dbd0') for k in range(9))
    b += E(200, 148, 48, 44, '#f0a51a') + E(200, 148, 34, 32, '#e3c04a') + C(200, 104, 8, '#f0a51a') + E(110, 150, 18, 16, '#f0a51a') + E(290, 150, 18, 16, '#f0a51a')
    b += R(0, 250, 400, 70, '#d8d2c4') + ''.join(tree(x, 252, .7, '#4f8a45') for x in (20, 380))
    return b
# 20 São Paulo - the endless skyline
def saopaulo():
    b = day() + skyline(230, 20, 0, 400, 30, 100, ('#c4c9d2', '#a9b1bd', '#d6dbe4')) + skyline(250, 21, 0, 400, 40, 150)
    b += ground(250, '#4f8a45') + ''.join(tree(x, 252, .8, '#3d7b40') for x in range(0, 410, 40))
    return b
# 21 Las Vegas - the welcome sign
def lasvegas():
    b = stars(21, 50, 160) + R(0, 250, 400, 70, '#2b2b36')
    b += R(196, 200, 8, 60, '#c9c9d6') + P('M200 80 L320 140 L200 200 L80 140 Z', '#f7f2e4', 'stroke="#e10600" stroke-width="4"')
    b += ''.join(C(200 + 118 * math.cos(a) * (1 if abs(math.cos(a)) > .01 else 0), 140, 0, 'none') for a in (0,))
    for k in range(16):
        t = k / 16 * 2 * math.pi; x = 200 + 104 * math.cos(t); y = 140 + 52 * math.sin(t)
        b += C(x, y, 3, '#ffd84a')
    b += T(200, 122, 'WELCOME', 18, '#e10600') + T(200, 150, 'LAS VEGAS', 26, '#1d4ed8') + T(200, 170, 'NEVADA', 12, '#e10600')
    b += palm(40, 260, 1.0) + palm(360, 260, 1.0, -6)
    return b
# 22 Lusail - marina towers
def lusail():
    b = R(0, 0, 400, 320, 'none') + sun(300, 70, 15, '#fff0c2') + skyline(220, 22, 0, 400, 40, 110, ('#d9cdb4', '#c8bba0', '#e6dcc7'))
    b += P('M140 220 Q120 120 180 60 Q150 130 170 220 Z', '#c9d6de') + P('M260 220 Q280 120 220 60 Q250 130 230 220 Z', '#c9d6de')
    b += water(222, '#2f7fb5', 22, 14) + boat(120, 262, .8, '#ffffff', '#c9d6de') + boat(280, 270, .7, '#ffffff', '#c9d6de')
    return b
# 23 Abu Dhabi - the hotel over the track
def abudhabi():
    b = sun(70, 200, 22, '#ffb36b', '#ff8a4a') + water(230, '#2b4f7a', 23, 12, '#ffb36b')
    b += R(40, 160, 130, 60, '#e8eef4') + R(230, 160, 130, 60, '#e8eef4') + windows(48, 168, 10, 3, 6, 10, 12, 16, LIT) + windows(238, 168, 10, 3, 6, 10, 12, 16, LIT)
    b += P('M20 162 Q200 70 380 162 L380 170 Q200 82 20 170 Z', '#9fb8d0', 'opacity=".9"')
    b += ''.join(L(20 + k * 24, 165 - 70 * math.sin(math.pi * k / 15), 44 + k * 24, 165 - 70 * math.sin(math.pi * (k + 1) / 15) + 8, '#ffffff', .8) for k in range(15))
    b += R(170, 190, 60, 30, '#c5d3e0') + R(0, 220, 400, 10, '#3a3d46')
    return b

for city, sky, fn in (('Melbourne', 'day', melbourne), ('Shanghai', 'night', shanghai), ('Suzuka', 'bright', suzuka), ('Miami', 'tropic', miami),
                      ('Montréal', 'day', montreal), ('Monaco', 'bright', monaco), ('Barcelona', 'warm', barcelona), ('Spielberg', 'day', spielberg),
                      ('Silverstone', 'grey', silverstone), ('Spa-Francorchamps', 'grey', spa), ('Budapest', 'dusk', budapest), ('Zandvoort', 'day', zandvoort),
                      ('Monza', 'warm', monza), ('Madrid', 'bright', madrid), ('Baku', 'night', baku), ('Kuala Lumpur', 'tropic', kualalumpur),
                      ('Singapore', 'night', singapore), ('Austin', 'warm', austin), ('Mexico City', 'bright', mexicocity), ('São Paulo', 'day', saopaulo),
                      ('Las Vegas', 'night', lasvegas), ('Lusail', 'warm', lusail), ('Abu Dhabi', 'sunset', abudhabi)):
    add(city, sky, fn())
