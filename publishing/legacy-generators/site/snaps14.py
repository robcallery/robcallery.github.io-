# US state capitals book - polaroids
from snaplib import *
import random, math, openpyxl

S = {}
def add(city, title, note, sky, body, defs=''):
    slug = 'us' + ''.join(ch for ch in city.lower() if ch.isalnum())
    S[city] = (title, note, scene(slug, sky, body, defs))

WIN = '#5a6a8a'
def lawn(y=GY, f='#4f8a45'):
    return ground(y, f, shade(f, .15)) + R(0, y + 10, W, H - y - 10, shade(f, -.08))

def dome_shape(cx, y, rx, ry, f):
    g = P(f'M{cx-rx:.1f} {y:.1f} A{rx:.1f} {ry:.1f} 0 0 1 {cx+rx:.1f} {y:.1f} Z', f)
    g += P(f'M{cx:.1f} {y-ry:.1f} A{rx:.1f} {ry:.1f} 0 0 1 {cx+rx:.1f} {y:.1f} L{cx:.1f} {y:.1f} Z', shade(f, -.12))
    for k in (-.6, -.3, .3, .6):
        g += PL(f'M{cx+rx*k:.1f} {y:.1f} Q{cx+rx*k*.6:.1f} {y-ry*.7:.1f} {cx:.1f} {y-ry:.1f}', shade(f, -.25), .8)
    return g

def capitol(cx=200, base=GY, w=280, stone='#efe9dc', dome='#f2efe6', dh=1.0, rx=34, statue=None, cols=6, wings=True, small_domes=False, drum_h=26):
    g = ''
    bh = 46
    if wings:
        g += R(cx - w / 2, base - bh + 8, w, bh - 8, shade(stone, -.04)) + windows(cx - w / 2 + 8, base - bh + 16, int((w - 16) // 14), 2, 7, 10, 7, 6, WIN)
    cw = w * .5
    g += R(cx - cw / 2, base - bh - 8, cw, bh + 8, stone) + windows(cx - cw / 2 + 8, base - bh, int((cw - 16) // 14), 2, 7, 12, 7, 6, WIN)
    pw = w * .26
    g += R(cx - pw / 2, base - bh - 6, pw, bh + 6, shade(stone, .1))
    for i in range(cols):
        x = cx - pw / 2 + 5 + i * (pw - 10) / (cols - 1)
        g += R(x - 2, base - bh, 4, bh, shade(stone, .25)) + R(x - 2.6, base - bh, 1.2, bh, shade(stone, -.12))
    g += P(f'M{cx-pw/2-4:.1f} {base-bh-6:.1f} L{cx:.1f} {base-bh-26:.1f} L{cx+pw/2+4:.1f} {base-bh-6:.1f} Z', shade(stone, .05)) + PL(f'M{cx-pw/2-4:.1f} {base-bh-6:.1f} L{cx:.1f} {base-bh-26:.1f} L{cx+pw/2+4:.1f} {base-bh-6:.1f}', shade(stone, -.2), 1)
    g += R(cx - pw / 2 - 6, base - 6, pw + 12, 6, shade(stone, -.1))
    top = base - bh - 8
    if small_domes:
        for dx in (-cw / 2 + 12, cw / 2 - 12):
            g += R(cx + dx - 7, top - 14, 14, 14, stone) + dome_shape(cx + dx, top - 14, 9, 10, dome)
    dr = rx * .95
    g += R(cx - dr, top - drum_h, dr * 2, drum_h, stone)
    for i in range(9):
        x = cx - dr + 3 + i * (dr * 2 - 6) / 8
        g += R(x - 1.2, top - drum_h + 3, 2.4, drum_h - 5, shade(stone, .25))
    g += R(cx - dr - 3, top - drum_h - 4, dr * 2 + 6, 4, shade(stone, -.08))
    y = top - drum_h - 4
    ry = rx * dh
    g += dome_shape(cx, y, rx, ry, dome)
    ly = y - ry
    g += R(cx - 5, ly - 12, 10, 12, stone) + dome_shape(cx, ly - 12, 6, 6, dome)
    if statue:
        g += R(cx - 1.5, ly - 30, 3, 12, statue) + C(cx, ly - 31, 2.4, statue)
    else:
        g += L(cx, ly - 18, cx, ly - 26, shade(dome, -.3), 1.4)
    return g

GOLD = '#d9b04a'; WHITE = '#f3f0e8'; COPPER = '#6fa58f'; SILVER = '#c9ccd2'

def tower_capitol(cx, base, stone, cap, statue=None, tw=44, th=130):
    g = R(cx - 120, base - 40, 240, 40, shade(stone, -.04)) + windows(cx - 112, base - 32, 15, 2, 7, 9, 8, 5, WIN)
    g += R(cx - tw / 2, base - 40 - th, tw, th, stone) + windows(cx - tw / 2 + 6, base - th - 30, 4, 9, 4, 10, 4, 3, WIN)
    g += R(cx - tw / 2 - 4, base - 40 - th - 6, tw + 8, 6, shade(stone, -.1))
    g += R(cx - 14, base - 40 - th - 24, 28, 18, stone) + dome_shape(cx, base - 40 - th - 24, 15, 14, cap)
    if statue:
        g += R(cx - 1.5, base - 40 - th - 52, 3, 14, statue) + C(cx, base - 40 - th - 53, 2.4, statue)
    return g

def std(city, title, note, sky='day', extra='', back='', **kw):
    b = sun(330, 48, 14) + cloud(80, 50, .8) + cloud(250, 36, .6) + back
    b += hills(232, '#8fb07a', sum(map(ord,city)) % 999, 10)
    b += lawn(GY) + capitol(**kw) + extra
    b += tree(30, GY, 1.3) + tree(370, GY, 1.3) + R(186, GY, 28, H - GY, '#d9d2c2')
    b += crowd(6, 120, 280, GY + 22, sum(map(ord,city)) % 777, 1.0, 20)
    add(city, title, note, sky, b)

# ---------- bespoke scenes
def glacier():
    b = cloud(80, 40, .8) + P('M-10 200 L60 90 L120 150 L180 70 L260 160 L330 80 L410 170 L410 230 L-10 230 Z', '#7d8fa3')
    b += P('M60 90 L80 120 L50 118 Z M180 70 L200 110 L165 105 Z M330 80 L350 115 L318 112 Z', '#fff')
    b += P('M120 230 Q170 130 230 120 Q260 140 300 230 Z', '#dff3fb') + P('M150 230 Q190 160 230 140 Q250 170 270 230 Z', '#a9dcf0')
    b += water(226, '#5d8fa8', 1401, 10)
    for x, y, s in ((90, 250, 1), (300, 262, .8), (200, 280, 1.2)):
        b += P(f'M{x-10*s} {y} L{x-4*s} {y-9*s} L{x+8*s} {y-7*s} L{x+12*s} {y} Z', '#e8f7fd')
    b += P('M330 120 L345 120 L350 226 L325 226 Z', '#eaf6fb', 'opacity=".8"')
    b += pine(20, 240, 1.4) + pine(380, 236, 1.6) + pine(360, 244, 1.2)
    return b

def saguaro(x, y, s=1.0):
    f = '#3f7d4a'
    g = R(x - 6 * s, y - 90 * s, 12 * s, 90 * s, f, rx=6 * s)
    g += PL(f'M{x-6*s} {y-40*s} Q{x-26*s} {y-40*s} {x-24*s} {y-66*s}', f, 10 * s, 'stroke-linecap="round"')
    g += PL(f'M{x+6*s} {y-55*s} Q{x+24*s} {y-55*s} {x+22*s} {y-78*s}', f, 10 * s, 'stroke-linecap="round"')
    return g

def desert():
    b = sun(200, 210, 34, '#ffdf8a', '#ff9e5a')
    b += hills(214, '#8a4a6a', 1411, 18) + hills(236, '#b0604a', 1412, 12)
    b += ground(250, '#d9a066', '#e8b87a')
    b += saguaro(90, 262, 1.25) + saguaro(300, 258, 1.0) + saguaro(360, 270, .7)
    for x in (40, 160, 230, 390):
        b += E(x, 262, 12, 5, '#7a8a4a')
    return b

def big_dam():
    b = sun(320, 50, 13) + cloud(90, 50, .8) + hills(200, '#5f8a52', 1421, 12)
    b += water(212, '#4f7f9a', 1422, 14)
    b += R(-10, 168, 420, 8, '#e8e4dc')
    for i in range(7):
        x = -10 + i * 70
        b += PL(f'M{x} 210 Q{x+35} 172 {x+70} 210', '#d9d4c9', 6)
        b += R(x - 3, 176, 6, 40, '#cfc9bd')
    b += L(-10, 162, 410, 162, '#9aa0a8', 1.5)
    b += ''.join(person(x, 168, c, '#f1c9a5', .8) for x, c in ((120, '#d22630'), (150, '#1d4ed8'), (260, '#ffcd00')))
    b += bike(200, 165, '#222', .9)
    return b

def tower_bridge_sac():
    b = sun(70, 50, 14) + cloud(300, 44, .7)
    b += water(220, '#3f6f8a', 1431, 14)
    for x in (110, 290):
        b += R(x - 14, 70, 28, 156, '#d4a93a') + R(x - 10, 74, 20, 10, '#b8902c')
        for k in range(6):
            b += L(x - 14, 90 + k * 22, x + 14, 112 + k * 22, '#b8902c', 1.5) + L(x + 14, 90 + k * 22, x - 14, 112 + k * 22, '#b8902c', 1.5)
    b += R(96, 70, 208, 10, '#d4a93a') + R(60, 176, 280, 14, '#d4a93a') + R(-10, 186, 420, 8, '#b8902c')
    for k in range(10):
        b += L(124 + k * 16, 80, 124 + k * 16, 176, '#c99d34', 1)
    b += R(0, 190, 40, 36, '#9aa0a8') + R(360, 190, 40, 36, '#9aa0a8')
    return b

def union_station():
    b = P('M-10 150 L60 110 L120 140 L200 96 L280 130 L340 100 L410 140 L410 262 L-10 262 Z', '#9fb3c8') + P('M200 96 L215 110 L190 108 Z', '#fff')
    b += road(GY) + R(0, GY - 4, W, 4, '#9aa0a8')
    b += R(50, 140, 300, 122, '#d8c3a0') + R(50, 132, 300, 10, '#c4ad86')
    for i in range(3):
        b += arch_win(130 + i * 50, 170, 40, 70, '#3a4a6a')
    b += windows(62, 152, 3, 4, 10, 14, 8, 8, '#3a4a6a') + windows(286, 152, 3, 4, 10, 14, 8, 8, '#3a4a6a')
    b += R(120, 112, 160, 22, '#1d2a44') + T(200, 129, 'UNION STATION', 17, '#ff5a3c', 'letter-spacing="2"')
    b += R(150, 140, 100, 14, '#1d2a44') + T(200, 151, 'TRAVEL BY TRAIN', 10, '#6fd3ff', 'letter-spacing="1"')
    b += clockface(200, 98, 12)
    b += crowd(8, 40, 360, GY + 14, 1441, 1.0, 20)
    return b

def twain_house():
    b = sun(330, 50, 13) + cloud(80, 46, .7) + lawn(GY, '#5a8f4a')
    b += R(90, 150, 220, 112, '#8a3a2a') + windows(104, 176, 6, 2, 14, 20, 20, 16, '#f3ead6')
    for y in range(156, 262, 10):
        b += L(90, y, 310, y, '#6f2c20', .6)
    b += P('M80 152 L130 100 L170 152 Z', '#3a3a44') + P('M150 152 L230 92 L310 152 Z', '#4a3a44') + P('M240 152 L270 120 L320 152 Z', '#3a3a44')
    for i in range(10):
        b += R(160 + i * 14, 118 + abs(5 - i) * 3, 8, 4, '#d9a347')
    b += R(110, 96, 18, 56, '#8a3a2a') + P('M106 98 L119 70 L132 98 Z', '#3a3a44')
    b += R(150, 220, 120, 8, '#f3ead6') + ''.join(R(154 + i * 22, 226, 4, 36, '#f3ead6') for i in range(6))
    b += tree(40, GY, 1.6) + tree(368, GY, 1.4)
    return b

def georgian(cx, base, w, h, brick='#a54a35', trim='#f3efe6'):
    g = R(cx - w / 2, base - h, w, h, brick) + windows(cx - w / 2 + 12, base - h + 12, int((w - 24) // 22), 2, 12, 18, 10, 14, trim)
    for i in range(int((w - 24) // 22)):
        pass
    g += P(f'M{cx-w/2-6} {base-h} L{cx} {base-h-30} L{cx+w/2+6} {base-h} Z', '#4a4a52')
    g += R(cx - 10, base - h - 52, 20, 26, trim) + dome_shape(cx, base - h - 52, 11, 12, trim) + L(cx, base - h - 64, cx, base - h - 74, '#555', 1.2)
    g += R(cx - 12, base - 30, 24, 30, trim) + R(cx - 8, base - 26, 16, 26, '#4a3a2a')
    return g

def old_state_house_dover():
    b = sun(330, 50, 13) + cloud(80, 46, .7) + lawn(GY, '#5a8f4a') + georgian(200, GY, 190, 92)
    b += tree(40, GY, 1.6) + tree(366, GY, 1.6) + R(188, GY, 24, H - GY, '#cfc6b5')
    return b

def florida():
    b = sun(70, 50, 14) + cloud(300, 40, .7) + lawn(GY, '#4f9a55')
    b += R(150, 50, 100, 212, '#e8e3d8') + windows(158, 60, 6, 15, 8, 8, 6, 5, WIN) + R(146, 46, 108, 8, '#cfc8ba')
    b += R(70, 178, 260, 84, '#f4f1ea') + windows(84, 200, 10, 2, 10, 12, 14, 12, WIN)
    for i in range(10):
        b += R(84 + i * 24, 196, 10, 6, ['#d22630', '#ffffff'][i % 2])
    b += R(170, 150, 60, 28, '#f4f1ea') + dome_shape(200, 150, 30, 26, '#f4f1ea')
    b += R(160, 210, 80, 52, '#ffffff') + ''.join(R(164 + i * 18, 210, 5, 52, '#e2ddd2') for i in range(5)) + P('M156 210 L200 192 L244 210 Z', '#f8f6f0')
    b += palm(40, GY, 1.2, 6) + palm(360, GY, 1.1, -6)
    return b

def atlanta():
    b = sun(330, 54, 13, '#ffd27a', '#ff9e5a') + hills(230, '#5f7f4a', 1451, 8)
    rnd = random.Random(1452)
    x = 0
    while x < 400:
        w = rnd.randint(22, 40); h = rnd.randint(60, 140)
        b += R(x, GY - h, w, h, rnd.choice(['#6a7f9a', '#7d8fa8', '#5a6d88'])) + windows(x + 4, GY - h + 8, max(1, (w - 8) // 7), h // 14, 3, 6, 4, 8, '#ffe9a8')
        x += w + 4
    b += R(160, 40, 44, 222, '#9a8a6a') + P('M160 40 L182 6 L204 40 Z', '#c9a94a') + L(182, 6, 182, -10, '#c9a94a', 2) + windows(166, 50, 4, 16, 5, 6, 5, 6, '#ffe9a8')
    b += R(250, 80, 40, 182, '#9ab0c8', 'rx="20"') + windows(256, 90, 4, 14, 4, 6, 4, 6, '#e8f2ff')
    b += road(GY)
    return b

def diamond_head():
    b = sun(70, 50, 15) + cloud(280, 40, .8)
    b += P('M120 200 Q170 120 230 110 Q290 104 330 140 Q370 170 420 200 Z', '#7a8a52') + P('M230 110 Q260 140 250 200 L330 200 Q320 150 330 140 Q290 104 230 110 Z', '#5f6f40')
    b += water(198, '#1f8fc8', 1461, 16) + R(0, 198, W, 4, '#ffffff', 'opacity=".6"')
    b += P('M-10 320 L-10 262 Q200 248 410 262 L410 320 Z', '#f0dca8')
    b += palm(40, 270, 1.4, 8) + palm(80, 274, 1.1, -4) + palm(370, 270, 1.3, -8)
    b += P('M180 226 L210 226 L206 230 L184 230 Z', '#ffcd00') + person(195, 226, '#d22630', '#a8714a', .7)
    return b

def obelisk_monument():
    b = sun(330, 50, 13) + cloud(80, 46, .7) + road(GY, '#8a8f99')
    b += R(0, 200, 90, 62, '#b49a7a') + R(310, 200, 90, 62, '#b49a7a') + windows(10, 210, 4, 2, 12, 14, 8, 10, WIN) + windows(318, 210, 4, 2, 12, 14, 8, 10, WIN)
    b += R(150, 220, 100, 42, '#cfc6b5') + R(162, 196, 76, 24, '#d8cfbe')
    b += P('M184 196 L190 60 L210 60 L216 196 Z', '#e2dacb') + P('M200 60 L210 60 L216 196 L200 196 Z', '#cfc6b5')
    b += R(186, 50, 28, 10, '#cfc6b5') + R(196, 30, 8, 20, '#7a8a6a') + C(200, 27, 4, '#7a8a6a')
    b += water(240, '#5a9ad0', 1471, 4) if False else ''
    b += crowd(8, 40, 360, GY + 14, 1472, 1.0, 20)
    return b

def baton_rouge():
    b = sun(330, 50, 13) + cloud(80, 46, .7) + lawn(GY, '#5a8f4a')
    b += R(110, 130, 180, 132, '#f4f1ea')
    for x in (100, 270):
        b += R(x, 104, 30, 158, '#f4f1ea') + battlements(x, 104, 30, '#f4f1ea', 4, 6) + arch_win(x + 9, 130, 12, 30, '#6a7a9a')
    b += battlements(110, 130, 180, '#f4f1ea', 5, 7)
    b += arch_win(180, 180, 40, 82, '#4a5a7a') + windows(130, 150, 3, 2, 10, 22, 8, 22, '#6a7a9a', True) + windows(236, 150, 3, 2, 10, 22, 8, 22, '#6a7a9a', True)
    b += tree(40, GY, 1.6, '#3f7a3a') + tree(370, GY, 1.6, '#3f7a3a')
    return b

def annapolis():
    b = sun(320, 46, 13) + cloud(90, 40, .7)
    b += hills(170, '#6f9a5a', 1481, 8) + windows(20, 150, 0, 0, 0, 0, 0, 0, WIN)
    rnd = random.Random(1482)
    for x in range(0, 400, 26):
        h = rnd.randint(18, 34); b += R(x, 176 - h, 22, h, rnd.choice(['#a54a35', '#e8dcc4', '#c9b08a', '#f3efe6'])) + P(f'M{x-2} {176-h} L{x+11} {170-h-8} L{x+24} {176-h} Z', '#4a4a52')
    b += R(184, 104, 32, 50, '#f3efe6') + R(188, 84, 24, 20, '#f3efe6') + dome_shape(200, 84, 13, 14, '#f3efe6') + L(200, 70, 200, 56, '#555', 1.4)
    b += water(176, '#2f6f9a', 1483, 16)
    for x, y, s in ((80, 250, 1.4), (220, 230, 1.0), (330, 270, 1.6)):
        b += f'<g transform="translate({x} {y}) scale({s})">' + P('M-20 0 L20 0 L14 7 L-14 7 Z', '#fff') + L(0, 0, 0, -44, '#555', 1.2) + P('M1 -42 L1 -4 L22 -4 Z', '#fff') + P('M-1 -38 L-1 -4 L-16 -4 Z', '#f3e2b8') + '</g>'
    return b

def boston_common():
    b = sun(70, 46, 13) + cloud(300, 40, .7)
    b += R(120, 120, 160, 80, '#b0503a') + windows(132, 140, 8, 2, 10, 14, 8, 12, '#f3efe6') + R(176, 160, 48, 40, '#f3efe6') + ''.join(R(180 + i * 11, 160, 4, 40, '#e2ddd2') for i in range(4))
    b += R(178, 96, 44, 24, '#f3efe6') + dome_shape(200, 96, 26, 26, GOLD) + R(196, 62, 8, 10, '#f3efe6') + C(200, 60, 4, GOLD)
    b += ground(196, '#4f8a45', '#6aa45a')
    b += P('M200 320 Q190 260 120 200 L140 200 Q210 260 230 320 Z', '#d9cfb8')
    b += tree(40, 240, 2.0) + tree(100, 222, 1.4) + tree(320, 230, 1.8) + tree(370, 250, 2.1) + E(300, 286, 50, 12, '#5aa0d0')
    b += crowd(7, 140, 240, 270, 1491, 1.0, 30)
    return b

def cathedral_dome(dcol=COPPER, stone='#d8c9a8', twin=False):
    b = sun(330, 50, 13) + cloud(80, 46, .7) + road(GY, '#8a8f99')
    if twin:
        b += R(130, 120, 140, 142, stone) + arch_win(180, 170, 40, 92, '#6a5a8a') + C(200, 150, 14, '#8a6aa8')
        for x in (130, 240):
            b += R(x, 70, 30, 192, stone) + spire(x + 15, 72, 30, 80, '#6f8a8a') + arch_win(x + 9, 100, 12, 30, '#6a5a8a')
        b += P('M130 120 L200 84 L270 120 Z', '#6f8a8a')
    else:
        b += R(90, 170, 220, 92, stone) + windows(104, 190, 8, 2, 10, 20, 16, 14, '#6a5a8a', True)
        b += R(160, 130, 80, 40, stone) + dome_shape(200, 130, 62, 66, dcol) + R(192, 52, 16, 14, stone) + L(200, 52, 200, 34, '#c9a94a', 2) + L(193, 42, 207, 42, '#c9a94a', 2)
        b += P('M150 210 L200 186 L250 210 Z', shade(stone, .1)) + R(150, 210, 100, 52, shade(stone, .08)) + arch_win(184, 226, 32, 36, '#4a3a2a')
    b += crowd(6, 60, 340, GY + 14, 1501, 1.0, 20)
    return b

def santa_fe():
    b = sun(330, 50, 14, '#fff3b0', '#ffe27a') + cloud(80, 40, .7) + hills(196, '#8a9a6a', 1511, 10)
    adobe = '#c98a5a'
    b += R(0, 150, 400, 112, adobe) + R(0, 150, 400, 6, shade(adobe, -.1))
    for x in range(10, 400, 24):
        b += C(x, 156, 3, '#7a4a2a')
    b += R(0, 200, 400, 6, '#8a5a3a') + ''.join(R(x, 206, 6, 56, '#8a5a3a') for x in range(16, 400, 48))
    b += windows(30, 170, 8, 1, 14, 20, 34, 0, '#3a6a8a')
    for x in (60, 160, 260, 350):
        b += ''.join(E(x, 214 + k * 7, 4, 4, '#c8102e') for k in range(5))
    b += ground(GY, '#d9c49a') + R(194, 196, 12, 66, '#e8dcc4') + P('M194 196 L200 176 L206 196 Z', '#e8dcc4')
    b += crowd(6, 40, 360, GY + 14, 1512, 1.0, 20)
    return b

def albany():
    b = sun(330, 50, 13) + cloud(80, 46, .7) + lawn(GY, '#5a8f4a')
    st = '#d8cfbe'
    b += R(70, 140, 260, 122, st) + windows(84, 156, 11, 4, 10, 14, 12, 10, WIN)
    b += P('M64 142 L90 96 L310 96 L336 142 Z', '#a8432e')
    for x in (60, 310):
        b += R(x, 112, 30, 150, st) + P(f'M{x-4} 114 L{x+15} 70 L{x+34} 114 Z', '#a8432e')
    for x in range(110, 300, 40):
        b += R(x, 104, 14, 18, st) + P(f'M{x-2} 106 L{x+7} 94 L{x+16} 106 Z', '#a8432e')
    b += R(140, 230, 120, 32, shade(st, .1)) + R(150, 240, 100, 22, '#6a5a4a')
    return b

def ohio():
    b = sun(330, 50, 13) + cloud(80, 46, .7) + lawn(GY, '#5a8f4a')
    st = '#d8cfbe'
    b += R(50, 176, 300, 86, st) + windows(60, 196, 13, 2, 10, 14, 12, 14, WIN)
    b += R(140, 168, 120, 94, shade(st, .1)) + ''.join(R(146 + i * 15, 176, 5, 86, shade(st, .25)) for i in range(8))
    b += R(160, 110, 80, 58, st) + ''.join(R(164 + i * 9, 116, 3, 50, shade(st, .25)) for i in range(9)) + R(156, 106, 88, 6, shade(st, -.1))
    b += tree(30, GY, 1.4) + tree(372, GY, 1.4)
    return b

def virginia():
    b = sun(330, 50, 13) + cloud(80, 46, .7) + lawn(GY, '#5a8f4a')
    st = '#f3f0e8'
    b += R(70, 170, 260, 92, st) + windows(84, 194, 3, 2, 14, 18, 16, 12, WIN) + windows(256, 194, 3, 2, 14, 18, 16, 12, WIN)
    b += R(140, 160, 120, 102, st) + ''.join(R(146 + i * 18, 170, 7, 92, '#e2ddd2') for i in range(7)) + P('M64 172 L200 112 L336 172 Z', st) + PL('M64 172 L200 112 L336 172 Z', '#cfc8ba', 1.5)
    b += R(120, 248, 160, 14, '#cfc8ba') + tree(30, GY, 1.4) + tree(372, GY, 1.4)
    return b

def oregon():
    b = sun(330, 50, 13) + cloud(80, 46, .7) + lawn(GY, '#4f8a45')
    st = '#f3f0e8'
    b += R(50, 190, 300, 72, st) + windows(64, 206, 13, 2, 8, 14, 13, 12, WIN)
    b += R(150, 150, 100, 112, st) + R(166, 86, 68, 64, st) + ''.join(R(170 + i * 7.5, 92, 3, 56, '#dedad0') for i in range(9))
    b += R(162, 80, 76, 6, '#dedad0') + R(194, 52, 12, 28, GOLD) + C(200, 48, 5, GOLD) + pine(30, GY, 2) + pine(370, GY, 2.2)
    return b

def scissortail():
    b = sun(70, 50, 13) + cloud(300, 44, .7)
    rnd = random.Random(1521)
    for x in range(0, 400, 30):
        h = rnd.randint(30, 80); b += R(x, 200 - h, 26, h, '#7d8fa8') + windows(x + 4, 206 - h, 3, h // 14, 4, 6, 4, 8, '#e8f2ff')
    b += R(240, 40, 46, 160, '#5d7a9a', 'rx="4"') + P('M240 46 L286 40 L286 60 Z', '#4d6a8a')
    b += ground(200, '#5a9a4a', '#72b05e') + E(160, 250, 120, 22, '#5ab0d8') + R(200, 228, 4, 22, '#fff')
    b += PL('M300 230 L330 196 L360 230', '#f3f0e8', 3) + PL('M330 196 L330 180', '#f3f0e8', 2)
    b += tree(40, 236, 1.4) + tree(370, 246, 1.6) + crowd(6, 280, 390, 262, 1522, 1.0, 20)
    return b

def waterfire():
    b = stars(1531, 40, 120) + moon(330, 50)
    rnd = random.Random(1532)
    for x in range(0, 400, 34):
        h = rnd.randint(40, 90); b += R(x, 190 - h, 30, h, '#2a3350') + windows(x + 5, 198 - h, 3, h // 16, 4, 6, 4, 10, '#ffd27a')
    b += R(0, 190, 400, 14, '#3a3a44')
    b += water(204, '#13203f', 1533, 18, '#ff9e5a')
    for x, y, s in ((50, 228, .8), (130, 240, 1), (230, 236, .9), (330, 252, 1.2)):
        b += R(x - 1.5 * s, y, 3 * s, 14 * s, '#555') + E(x, y, 9 * s, 4 * s, '#222') + P(f'M{x-8*s} {y} Q{x-4*s} {y-22*s} {x} {y-30*s} Q{x+4*s} {y-20*s} {x+8*s} {y} Z', '#ff8a1c') + P(f'M{x-4*s} {y} Q{x} {y-16*s} {x+4*s} {y} Z', '#ffd84a')
        b += E(x, y + 26 * s, 10 * s, 3 * s, '#ff9e5a', 'opacity=".5"')
    b += P('M160 280 L240 280 L250 272 L150 272 Z', '#111') + person(200, 272, '#222', '#f1c9a5', .8)
    return b

def honky_tonk():
    b = stars(1541, 30, 80) + road(GY, '#2a2d3a')
    cols = ['#7a2a2a', '#2a3a6a', '#5a3a2a', '#2a5a4a']
    signs = [('BEER', '#ff4a7a'), ('LIVE MUSIC', '#4ad8ff'), ('HONKY TONK', '#ffd84a'), ('BAR', '#7aff8a')]
    for i in range(4):
        x = i * 100
        b += R(x, 90, 96, 172, cols[i]) + windows(x + 10, 110, 3, 3, 18, 22, 10, 16, '#ffd27a') + R(x + 30, 214, 36, 48, '#1a1a1a')
        t, c = signs[i]
        b += R(x + 8, 66 + (i % 2) * 10, 80, 22, '#111', 'rx="4"') + T(x + 48, 83 + (i % 2) * 10, t, 15, c, 'letter-spacing="1"')
    b += P('M330 40 Q350 30 360 50 L356 70 L350 66 Z', '#ffd84a') + L(360, 50, 372, 20, '#ffd84a', 2)
    b += crowd(12, 10, 390, GY + 10, 1542, 1.0, 30)
    return b

def bats():
    b = sun(300, 196, 26, '#ffb36b', '#ff7a5a') + hills(200, '#5a3d6a', 1551, 10)
    rnd = random.Random(1552)
    x = 0
    while x < 400:
        w = rnd.randint(22, 36); h = rnd.randint(40, 110)
        b += R(x, 210 - h, w, h, '#3a2f55') + windows(x + 4, 218 - h, max(1, (w - 8) // 7), h // 16, 3, 5, 4, 11, '#ffd27a')
        x += w + 3
    b += water(222, '#3a3f6a', 1553, 14, '#ffb36b')
    b += R(-10, 206, 420, 10, '#7a6a5a') + ''.join(PL(f'M{x} 216 Q{x+30} 196 {x+60} 216', '#6a5a4a', 4) for x in range(-10, 420, 60))
    for _ in range(80):
        bx = rnd.uniform(20, 380); by = rnd.uniform(20, 180) * (1 - abs(bx - 200) / 600)
        s = rnd.uniform(.6, 1.2)
        b += P(f'M{bx-4*s:.1f} {by:.1f} Q{bx-2*s:.1f} {by-3*s:.1f} {bx:.1f} {by:.1f} Q{bx+2*s:.1f} {by-3*s:.1f} {bx+4*s:.1f} {by:.1f} Q{bx:.1f} {by-1*s:.1f} {bx-4*s:.1f} {by:.1f} Z', '#1a1428')
    return b

def us_capitol():
    b = sun(330, 50, 13) + cloud(80, 46, .7) + lawn(GY, '#4f8a45')
    b += capitol(200, GY, 340, '#f3f0e8', '#f8f6f0', 1.15, 38, '#7a8a8a', 8, True, False, 34) + E(200, 296, 140, 14, '#7ab8e0') + tree(20, GY, 1.4) + tree(380, GY, 1.4)
    return b

# ---------- load the data and add every capital
wb = openpyxl.load_workbook('/mnt/user-data/attachments/9cac7207-2d1b-5bf4-969e-62974606aff5/89f63e01-us_50_state_capitals_plus_dc_two_bars_each.xlsx')
ROWS = {r[1]: r for r in wb['50 Capitals'].iter_rows(min_row=2, values_only=True) if r[1]}
RENAME = {'Dover': 'Dover, Delaware', 'Lincoln': 'Lincoln, Nebraska'}

def note(cap): return ROWS[cap][9].rstrip('.') + '.'
def title(cap): return ROWS[cap][8]
def go(cap, sky, body):
    add(RENAME.get(cap, cap), title(cap), note(cap), sky, body)
def cap_std(cap, **kw):
    std(RENAME.get(cap, cap), title(cap), note(cap), **kw)

go('Juneau', 'grey', glacier())
go('Phoenix', 'sunset', desert())
go('Little Rock', 'day', big_dam())
go('Sacramento', 'warm', tower_bridge_sac())
go('Denver', 'day', union_station())
go('Hartford', 'day', twain_house())
go('Dover', 'day', old_state_house_dover())
go('Tallahassee', 'bright', florida())
go('Atlanta', 'dusk', atlanta())
go('Honolulu', 'tropic', diamond_head())
go('Indianapolis', 'day', obelisk_monument())
go('Baton Rouge', 'warm', baton_rouge())
go('Annapolis', 'day', annapolis())
go('Boston', 'day', boston_common())
go('Saint Paul', 'day', cathedral_dome())
go('Helena', 'day', cathedral_dome(twin=True))
go('Santa Fe', 'bright', santa_fe())
go('Albany', 'day', albany())
go('Columbus', 'day', ohio())
go('Oklahoma City', 'day', scissortail())
go('Salem', 'day', oregon())
go('Providence', 'night', waterfire())
go('Nashville', 'night', honky_tonk())
go('Austin', 'dusk', bats())
go('Richmond', 'day', virginia())
add('Washington, D.C.', 'US Capitol', note('Washington, D.C.'), 'day', us_capitol())

def towered(cap, stone, capc, statue, th=130, sky='day'):
    b = sun(330, 50, 13) + cloud(80, 46, .7) + lawn(GY) + tower_capitol(200, GY, stone, capc, statue, th=th) + tree(30, GY, 1.4) + tree(372, GY, 1.4)
    go(cap, sky, b)
towered('Lincoln', '#d8cfbe', GOLD, GOLD)
towered('Bismarck', '#e8e3d8', '#e8e3d8', None, th=150)

cap_std('Montgomery', stone='#f3f0e8', dome=WHITE)
cap_std('Boise', stone='#e3d9c2', dome='#e9e2d0', statue=None)
cap_std('Springfield', stone='#d8cfbe', dome=SILVER, dh=1.35, rx=30, drum_h=36)
cap_std('Des Moines', stone='#d8cfbe', dome=GOLD, small_domes=True, dh=1.2)
cap_std('Topeka', stone='#d8cfbe', dome=COPPER, dh=1.2, statue=COPPER)
cap_std('Frankfort', stone='#e8e3d8', dome=WHITE, dh=1.05)
cap_std('Augusta', stone='#d8cfbe', dome=COPPER, dh=.9, statue=GOLD, wings=True)
cap_std('Lansing', stone='#efe9dc', dome=WHITE, dh=1.4, rx=28, drum_h=38)
cap_std('Jackson', stone='#efe9dc', dome=WHITE, dh=1.05, statue=GOLD)
cap_std('Jefferson City', stone='#e3dccb', dome=WHITE, dh=1.15)
cap_std('Carson City', stone='#cfc6b0', dome=SILVER, rx=18, drum_h=18, dh=1.2, w=200)
cap_std('Concord', stone='#cfcac0', dome=GOLD, rx=20, dh=1.1, statue=GOLD, w=220)
cap_std('Trenton', stone='#efe9dc', dome=GOLD, dh=1.1)
cap_std('Raleigh', stone='#cfc6b5', dome=COPPER, rx=26, dh=.7, w=220)
cap_std('Harrisburg', stone='#d8cfbe', dome='#5f9a7a', dh=1.2, statue=GOLD)
cap_std('Columbia', stone='#d8cfbe', dome=COPPER, dh=1.0)
cap_std('Pierre', stone='#d8cfbe', dome=COPPER, dh=1.05)
cap_std('Salt Lake City', stone='#e3dccb', dome=COPPER, dh=1.15, back=P('M-10 200 L40 130 L90 170 L140 110 L190 160 L250 100 L310 150 L360 112 L410 170 L410 262 L-10 262 Z', '#9aa8b8') + P('M140 110 L156 126 L128 128 Z M250 100 L266 118 L236 118 Z', '#fff'))
cap_std('Montpelier', stone='#cfcac0', dome=GOLD, dh=1.0, statue='#c9a46a', w=230)
cap_std('Olympia', stone='#efe9dc', dome='#e9e3d4', dh=1.35, rx=30, drum_h=36)
cap_std('Charleston', stone='#e8e3d8', dome=GOLD, dh=1.25)
cap_std('Madison', stone='#f3f0e8', dome='#f3f0e8', dh=1.25, statue=GOLD)
cap_std('Cheyenne', stone='#d8cfbe', dome=GOLD, dh=1.1)
missing = [c for c in ROWS if RENAME.get(c, c) not in S]
assert not missing, missing
