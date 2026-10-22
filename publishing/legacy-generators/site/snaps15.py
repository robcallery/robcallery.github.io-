# Ireland / Scotland / Wales / Spain books - polaroids for the 71 new places
from snaplib import *
from snaps7 import lighthouse
import random, math, json

S = {}
INFO = json.load(open('/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/isws_snaps.json'))
def add(city, sky, body, title=None):
    t, n = INFO[city]
    slug = 'b4' + ''.join(ch for ch in city.lower() if ch.isalnum())
    S[city] = (title or t, n, scene(slug, sky, body))
WIN = '#4a5878'; STONE = '#b8ab95'; GREY = '#9a958c'; SAND = '#d9c08a'

def day(seed=1): return sun(330, 50, 13) + cloud(80, 46, .7) + cloud(240, 34, .5)
def lawn(y=GY, f='#4f8a45'): return ground(y, f, shade(f, .15))
def towerhouse(x, base, w, h, st=STONE, win=WIN):
    dk = shade(st, -.18)
    return R(x, base - h, w, h, st) + R(x + w * .78, base - h, w * .22, h, dk) + battlements(x, base - h, w, st, 3, 6) + windows(x + w * .2, base - h + 18, 2, max(1, int(h // 34)), 6, 10, w * .3, 22, win, True)
def roundtower(x, base, r, h, st=STONE, cone=None):
    g = R(x - r, base - h, r * 2, h, st) + R(x + r * .3, base - h, r * .7, h, shade(st, -.15)) + windows(x - 3, base - h + 16, 1, max(1, int(h // 30)), 6, 10, 0, 18, WIN, True)
    g += (P(f'M{x-r-2} {base-h} L{x} {base-h-r*1.6} L{x+r+2} {base-h} Z', cone) if cone else battlements(x - r, base - h, r * 2, st, 3, 5))
    return g
def ruin(x0=60, x1=340, base=GY, h=110, st='#a89f8c'):
    g = R(x0, base - h, x1 - x0, h, st)
    n = int((x1 - x0) // 46)
    for i in range(n):
        g += arch_win(x0 + 14 + i * 46, base - h + 22, 24, 64, '#9fc4e0')
    g += R(x0, base - h - 4, 30, h + 4, shade(st, -.1)) + P(f'M{x1-50} {base-h} L{x1-25} {base-h-60} L{x1} {base-h} Z', st) + arch_win(x1 - 38, base - h - 20, 26, 50, '#9fc4e0')
    for i in range(8): g += R(x0 + i * 35, base - h - random.Random(i).randint(0, 14), 18, 14, st)
    return g
def houses(y, seed, n=9, w=46, hmin=44, hmax=70, cols=('#e84a5f', '#ffcd00', '#2f8fd8', '#3fae6a', '#f07a14', '#b45ce0', '#ffffff', '#f4a6c8')):
    rnd = random.Random(seed); g = ''
    for i in range(n):
        x = -6 + i * w; h = rnd.randint(hmin, hmax); c = rnd.choice(cols)
        g += R(x, y - h, w - 2, h, c) + windows(x + 7, y - h + 10, 3, max(1, h // 24), 7, 9, 5, 12, '#3a4a6a') + R(x - 1, y - h - 5, w, 5, shade(c, -.3))
    return g
def boats(y, seed, n=3):
    rnd = random.Random(seed)
    return ''.join(boat(rnd.uniform(40, 360), y + rnd.uniform(0, 30), rnd.uniform(1, 1.5), rnd.choice(['#d22630', '#1d4ed8', '#2a8a46', '#ffcd00'])) for _ in range(n))
def mountain(px, py, w, col, base=GY, snow=False):
    g = P(f'M{px-w} {base} L{px} {py} L{px+w} {base} Z', col) + P(f'M{px} {py} L{px+w} {base} L{px+w*.25} {base} Z', shade(col, -.15))
    if snow: g += P(f'M{px} {py} L{px-w*.18} {py+(base-py)*.22} L{px-w*.05} {py+(base-py)*.18} L{px+w*.06} {py+(base-py)*.24} L{px+w*.2} {py+(base-py)*.2} Z', '#fff')
    return g
def river(y, f='#4f86b0'): return water(y, f, int(y), 10)

# ---------------- Ireland
def cork():
    b = R(0, 0, W, H, '#5a4a3a') + P('M0 120 Q200 30 400 120 L400 0 L0 0 Z', '#3a3028')
    for i in range(7): b += PL(f'M{20+i*60} 120 L{20+i*60} 40', '#7a6a5a', 3)
    b += P('M0 120 Q200 34 400 120', '#8a6a4a', 'opacity="0"') + PL('M0 122 Q200 36 400 122', '#c9a46a', 4)
    b += R(140, 150, 120, 60, '#e8e0d0') + clockface(200, 120, 14) + R(80, 210, 240, 60, '#3a2a1a')
    rnd = random.Random(31)
    for i in range(18): b += C(rnd.uniform(90, 310), rnd.uniform(214, 236), rnd.uniform(5, 9), rnd.choice(['#d22630', '#f07a14', '#ffcd00', '#2a8a46', '#c98a5a']))
    b += R(80, 240, 240, 6, '#6a4a2a') + crowd(10, 20, 380, 270, 32, 1.2, 30)
    return b
def galway():
    b = day() + river(220, '#3f7aa8')
    b += R(60, 110, 280, 116, '#a89f8c') + arch_win(110, 150, 60, 76, '#3f7aa8') + arch_win(230, 160, 40, 66, '#3f7aa8')
    b += battlements(60, 110, 280, '#a89f8c', 5, 8) + R(0, 226, 400, 10, '#8a8478') + boats(250, 33, 2)
    b += crowd(8, 20, 380, 236, 34, 1.0, 6)
    return b
def limerick():
    b = day() + river(220, '#4a7fa8')
    b += R(80, 120, 240, 100, STONE) + battlements(80, 120, 240, STONE, 5, 7)
    for x in (80, 320): b += roundtower(x, 220, 22, 130)
    b += roundtower(200, 220, 20, 120) + arch_win(184, 180, 32, 40, '#3b2a1a')
    return b
def waterford():
    b = day() + road(GY, '#8a8f99') + R(0, 210, 120, 52, '#d8cfbe') + R(300, 200, 100, 62, '#c9b08a') + windows(10, 220, 4, 2, 12, 12, 14, 10, WIN)
    b += roundtower(200, GY, 46, 170, '#9a8f7c', '#5a5a62') + windows(190, 120, 1, 3, 20, 14, 0, 26, '#3a4a6a', True)
    return b
def kilkenny():
    b = day() + lawn(GY, '#5a9a4a')
    b += R(80, 130, 240, 132, '#a89a84') + windows(100, 160, 8, 3, 14, 18, 14, 14, WIN)
    for x in (80, 320): b += roundtower(x, GY, 30, 168, '#a89a84', '#5a6a6a')
    b += flowers(40, 360, 270, 41, 40)
    return b
def derry():
    b = day() + houses(170, 51, 9, 46, 40, 70, ('#e8dcc4', '#c9b08a', '#a54a35', '#f3efe6'))
    b += R(0, 170, 400, 92, '#8a8478') + battlements(0, 170, 400, '#8a8478', 6, 8) + R(0, 200, 400, 3, '#6a645a')
    for x in (90, 230): b += R(x, 180, 46, 10, '#2a2a2a') + C(x + 46, 185, 6, '#2a2a2a') + C(x + 10, 192, 9, '#3a3a3a')
    b += lawn(GY) + crowd(6, 40, 360, 166, 52, .9, 4)
    return b
def killarney():
    b = day() + mountain(100, 110, 160, '#6a7f5a') + mountain(300, 90, 180, '#5a6f4a') + water(200, '#4a7fa8', 61, 14)
    b += towerhouse(170, 210, 60, 130, '#a89f8c') + R(150, 196, 110, 16, '#a89f8c') + lawn(250, '#4f8a45')
    b += boat(320, 230, 1.6, '#2a8a46')
    return b
def dingle():
    b = day() + hills(150, '#6a9a5a', 71, 14) + houses(196, 72, 9, 46, 36, 56)
    b += water(200, '#2f7fb0', 73, 16) + boats(214, 74, 4)
    b += P('M300 268 Q320 240 345 262 Q330 262 326 272 Z', '#7a8a9a') + P('M330 252 L338 244 L340 254 Z', '#7a8a9a')
    return b
def westport():
    b = day() + mountain(220, 70, 150, '#7a7a6a') + P('M206 92 L220 70 L232 90 Z', '#f3efe6')
    b += water(214, '#3f86b5', 81, 14)
    for x, w in ((60, 30), (120, 22), (300, 26), (350, 18)): b += E(x, 222, w, 6, '#6a9a5a')
    b += R(0, 250, 400, 70, '#6a9a5a')
    return b
def sligo():
    b = day() + lawn(GY, '#5a8a4a') + ruin(50, 350, GY, 120, '#9a9282') + R(180, 90, 40, 52, '#9a9282')
    return b
def donegal():
    b = day() + river(232, '#4a7fa8') + lawn(GY, '#5a8a4a') + towerhouse(140, 236, 120, 150, '#a49a88')
    b += P('M140 86 L170 64 L230 64 L260 86 Z', '#6a6a72') + R(160, 56, 10, 12, '#a49a88') + R(232, 56, 10, 12, '#a49a88') + tree(40, 236, 1.6) + tree(360, 236, 1.6)
    return b
def athlone():
    b = day() + river(226, '#4a7fa8')
    b += P('M120 226 L130 110 L270 110 L280 226 Z', '#a89f8c') + battlements(130, 110, 140, '#a89f8c', 5, 8) + windows(150, 140, 4, 2, 10, 16, 20, 20, WIN, True)
    b += R(0, 226, 400, 8, '#8a8478') + R(300, 160, 100, 66, '#e8dcc4') + windows(310, 172, 4, 2, 10, 12, 12, 12, WIN)
    return b
def wexford():
    b = day() + lawn(GY, '#5a9a4a') + water(240, '#4a7fa8', 91, 4)
    for x, s in ((90, 1), (210, 1.3), (320, .9)):
        b += R(x - 30 * s, GY - 40 * s, 60 * s, 40 * s, '#c9a46a') + P(f'M{x-38*s} {GY-40*s} L{x} {GY-90*s} L{x+38*s} {GY-40*s} Z', '#b08a4a') + R(x - 6 * s, GY - 24 * s, 12 * s, 24 * s, '#3b2a1a')
    for i in range(30): b += R(10 + i * 13, 214, 4, 30, '#8a6a4a')
    return b
def kinsale():
    b = day() + water(196, '#2f7fb0', 101, 18)
    b += P('M40 250 L120 200 L280 200 L360 250 L280 300 L120 300 Z', '#b8ab95') + P('M70 250 L130 214 L270 214 L330 250 L270 286 L130 286 Z', '#7aa85a')
    b += R(170, 228, 60, 30, '#a89f8c') + windows(178, 236, 4, 1, 8, 10, 6, 0, WIN) + boats(176, 102, 2)
    return b
def cobh():
    b = day() + water(240, '#2f7fb0', 111, 14)
    b += P('M-10 240 L-10 180 Q200 120 410 160 L410 240 Z', '#6a9a5a') + houses(240, 112, 10, 42, 30, 46)
    b += R(150, 96, 120, 90, '#9a9aa2') + spire(240, 100, 40, 90, '#7a7a82') + R(220, 100, 40, 86, '#9a9aa2') + P('M150 96 L200 70 L250 96 Z', '#6a6a72') + arch_win(172, 120, 24, 50, '#5a7aa8')
    return b
def doolin():
    b = day() + P('M240 320 L240 120 L420 100 L420 320 Z', '#5a5a4a') + P('M240 120 L420 100 L420 112 L240 132 Z', '#6a9a5a')
    b += water(200, '#2f7fb0', 121, 16) + R(-10, 250, 180, 70, '#8a8478') + R(150, 236, 30, 14, '#8a8478')
    b += P('M40 232 L130 232 L120 246 L50 246 Z', '#ffffff') + R(64, 220, 46, 12, '#ffffff') + R(66, 222, 42, 4, '#1d4ed8')
    return b
def ennis():
    b = day() + lawn(GY, '#5a8a4a') + ruin(40, 300, GY, 100, '#a49a88') + R(240, 70, 50, 100, '#a49a88') + battlements(240, 70, 50, '#a49a88', 4, 6)
    return b
def carlingford():
    b = day() + mountain(300, 70, 200, '#5a7a4a') + water(210, '#4a7fa8', 131, 12)
    b += P('M40 220 L50 120 L180 120 L190 220 Z', '#a89f8c') + battlements(50, 120, 130, '#a89f8c', 5, 7) + arch_win(90, 150, 20, 40, '#3a3a3a') + arch_win(140, 150, 20, 40, '#3a3a3a')
    b += lawn(250, '#4f8a45')
    return b

# ---------------- Scotland
def inverness():
    st = '#b05a3a'
    b = day() + river(240, '#4a7fa8') + P('M-10 240 Q140 150 320 170 L410 240 Z', '#5a8a4a')
    b += R(110, 110, 180, 80, st) + battlements(110, 110, 180, st, 5, 8) + windows(126, 130, 7, 2, 10, 14, 13, 16, WIN, True)
    for x in (110, 290): b += roundtower(x, 190, 16, 120, st)
    return b
def stirling():
    b = day() + P('M-10 320 L-10 210 L80 150 L330 140 L410 200 L410 320 Z', '#6a6a5a') + P('M80 150 L330 140 L330 150 L80 160 Z', '#4f8a45')
    b += R(90, 90, 220, 60, '#d8c8a0') + battlements(90, 90, 220, '#d8c8a0', 5, 7) + windows(104, 104, 9, 2, 10, 12, 12, 10, WIN, True) + R(130, 70, 50, 24, '#d8c8a0') + towerhouse(250, 150, 50, 100, '#c9b88f')
    return b
def scone():
    st = '#c08a6a'
    b = day() + lawn(GY, '#5a9a4a') + R(70, 140, 260, 122, st) + battlements(70, 140, 260, st, 5, 7) + windows(86, 160, 9, 3, 12, 16, 14, 14, WIN, True)
    for x in (70, 200, 330): b += roundtower(x, GY, 14, 150, st)
    b += P('M300 284 Q310 268 322 280 Z', '#1d6fb3') + C(318, 270, 3, '#1d6fb3') + ''.join(L(306, 282, 286 + k * 4, 266, '#2a8a46', 2) for k in range(6))
    return b
def standrews():
    st = '#b8ab8c'
    b = day() + water(170, '#3f86b5', 141, 10) + lawn(GY, '#5a9a4a')
    b += R(80, 80, 40, 182, st) + R(220, 80, 40, 182, st) + R(120, 200, 100, 62, st) + arch_win(140, 110, 60, 90, '#a9d0ea')
    for x in (80, 220): b += arch_win(x + 12, 100, 16, 40, '#a9d0ea') + battlements(x, 80, 40, st, 3, 6)
    for i in range(12): b += R(30 + i * 30, 238, 14, 24, '#9a958c')
    return b
def oban():
    b = day() + P('M-10 200 Q200 110 410 190 L410 220 L-10 220 Z', '#4f8a45')
    b += P('M140 140 A60 30 0 0 1 260 140 L260 160 A60 30 0 0 0 140 160 Z', '#c9b88f')
    for i in range(10): b += arch_win(146 + i * 11, 142, 6, 12, '#3a5a2a')
    b += houses(232, 151, 9, 46, 30, 46, ('#f3efe6', '#e8dcc4', '#ffffff', '#c9b08a')) + water(232, '#2f7fb0', 152, 14) + boats(250, 153, 2)
    return b
def fortwilliam():
    b = R(0, 0, W, H, '#cfe3ee', 'opacity=".0"') + mountain(220, 50, 230, '#6a6a72', 250, True) + mountain(80, 130, 140, '#5a7a4a', 250)
    b += water(240, '#3f6f8a', 161, 10) + pine(30, 250, 1.6) + pine(370, 252, 1.8) + R(0, 250, 400, 70, '#4f7a40')
    return b
def pitlochry():
    b = day() + hills(150, '#5a8a4a', 171, 12) + water(150, '#3f6f8a', 172, 6)
    b += R(40, 150, 320, 50, '#c9c4b8') + ''.join(R(60 + i * 60, 150, 20, 50, '#b0aa9c') for i in range(5))
    for i in range(8): b += R(320 - i * 4 + 60, 200 + i * 7, 30, 7, '#a8a294')
    b += water(200, '#4a7fa8', 173, 16)
    return b
def ayr():
    b = sun(300, 160, 22, '#ffd27a', '#ff9e5a') + P('M180 196 L250 160 L300 180 L350 150 L410 190 L410 200 L180 200 Z', '#8a7aa0')
    b += water(196, '#3f6fa0', 181, 14, '#ffd27a') + P('M-10 320 L-10 250 Q200 236 410 250 L410 320 Z', '#ecd9a8') + crowd(6, 40, 360, 266, 182, 1.0, 30)
    return b
def dunfermline():
    st = '#b8ab95'
    b = day() + lawn(GY) + R(60, 160, 200, 102, st) + windows(76, 180, 6, 1, 14, 40, 16, 0, WIN, True)
    b += R(240, 90, 80, 172, st) + battlements(240, 90, 80, st, 4, 6)
    b += T(280, 106, 'KING ROBERT', 11, '#5a5040', 'letter-spacing="1"') + T(280, 120, 'THE BRUCE', 11, '#5a5040', 'letter-spacing="1"')
    b += R(250, 64, 60, 8, st)
    return b
def kelpies():
    b = sun(70, 60, 13) + cloud(300, 44, .7) + water(250, '#4a7fa8', 191, 10) + lawn(272, '#4f8a45')
    st = '#b8bcc2'
    for x, flip in ((150, 1), (270, -1)):
        b += f'<g transform="translate({x} 250) scale({flip} 1)">' + P('M-30 0 L-24 -90 Q-20 -150 10 -170 L40 -150 L50 -130 L30 -120 L20 -100 L28 -60 L20 0 Z', st) + P('M10 -170 L4 -186 L18 -172 Z', st) + C(14, -150, 3, '#4a4f58') + ''.join(L(-26, -k * 14, 24, -k * 14 - 4, '#8a8f98', 1) for k in range(10)) + '</g>'
    return b
def dumfries():
    b = day() + road(GY, '#8a8f99') + R(110, 130, 180, 132, '#f3efe6') + P('M100 132 L200 96 L300 132 Z', '#5a5a62') + windows(130, 150, 4, 2, 18, 24, 24, 22, '#3a4a6a') + R(186, 214, 28, 48, '#2a3a5a')
    b += R(0, 160, 100, 102, '#c9b08a') + R(300, 160, 100, 102, '#d8c8a8')
    return b
def peebles():
    b = day() + hills(170, '#6a9a5a', 201, 18) + river(220, '#4a7fa8')
    for i in range(5): b += PL(f'M{40+i*70} 222 Q{75+i*70} 196 {110+i*70} 222', '#a89f8c', 8)
    b += R(30, 206, 360, 10, '#a89f8c') + lawn(262, '#4f8a45') + tree(30, 262, 1.6) + tree(370, 262, 1.6)
    return b
def melrose():
    st = '#b07a5a'
    b = day() + lawn(GY, '#5a9a4a') + R(60, 130, 260, 132, st) + arch_win(220, 120, 70, 120, '#9fc4e0') + P('M210 130 L255 70 L300 130 Z', st)
    for i in range(4): b += arch_win(76 + i * 34, 160, 18, 60, '#9fc4e0')
    b += R(320, 180, 40, 82, st) + flowers(30, 370, 270, 211, 20)
    return b
def storr():
    b = R(0, 0, W, H, '#ffffff', 'opacity="0"') + cloud(100, 40, .9, '#eef2f5') + P('M-10 320 L-10 180 L120 140 L220 160 L410 120 L410 320 Z', '#6a7a5a')
    b += P('M200 160 L206 70 L220 50 L232 80 L236 160 Z', '#4a4a50') + P('M250 150 L256 110 L268 104 L274 150 Z', '#55555c')
    b += water(270, '#5a7a9a', 221, 8) + crowd(3, 120, 180, 240, 222, .7, 10)
    return b
def kirkwall():
    st = '#a8503a'
    b = day() + road(GY, '#8a8f99') + R(80, 140, 240, 122, st) + windows(96, 170, 8, 1, 12, 40, 16, 0, WIN, True)
    b += R(170, 70, 60, 90, st) + P('M166 70 L200 30 L234 70 Z', '#5a6a6a') + arch_win(186, 200, 28, 62, '#3b2a1a') + R(80, 130, 240, 10, '#c9a08a')
    return b
def lerwick():
    b = day() + R(0, 140, 400, 60, '#8a9a8a') + water(200, '#3f6fa0', 231, 16)
    for x in (40, 150, 260):
        b += R(x, 140, 90, 70, '#b8ab95') + P(f'M{x-4} 140 L{x+45} 112 L{x+94} 140 Z', '#5a5a62') + windows(x + 12, 156, 3, 2, 12, 12, 16, 12, WIN)
    b += boat(320, 240, 1.6, '#d22630') + boat(110, 262, 1.2, '#1d4ed8')
    return b

# ---------------- Wales
def newport_w():
    b = day() + river(232, '#6a7a7a')
    for x in (70, 330): b += R(x - 8, 50, 16, 190, '#2f5a8a') + ''.join(L(x - 8, 60 + k * 22, x + 8, 82 + k * 22, '#1f4a7a', 1.5) for k in range(8))
    b += R(56, 50, 288, 12, '#2f5a8a') + ''.join(L(70 + k * 20, 50, 80 + k * 20, 62, '#1f4a7a', 1) for k in range(13))
    b += L(200, 62, 200, 190, '#333', 1) + L(210, 62, 210, 190, '#333', 1) + R(186, 190, 40, 12, '#c9c4b8') + R(0, 240, 60, 22, '#8a8478') + R(340, 240, 60, 22, '#8a8478')
    return b
def wrexham():
    b = day() + R(0, 240, 400, 80, '#3f8a45')
    b += P('M10 240 L30 140 L370 140 L390 240 Z', '#c8102e') + R(20, 132, 360, 10, '#ffffff') + ''.join(L(30 + i * 20, 132, 40 + i * 20, 120, '#c9ced8', 2) for i in range(18)) + L(30, 120, 370, 120, '#c9ced8', 2)
    b += windows(40, 180, 15, 1, 16, 22, 6, 0, '#ffffff') + crowd(30, 10, 390, 244, 241, 1.0, 30, ['#c8102e', '#ffffff', '#c8102e'])
    return b
def bangor():
    st = '#7a7a7a'
    b = day() + lawn(GY, '#4f8a45') + R(60, 150, 180, 112, st) + battlements(60, 150, 180, st, 5, 7) + windows(76, 170, 6, 2, 12, 18, 14, 18, WIN, True)
    b += R(230, 70, 90, 192, st) + R(300, 70, 20, 192, shade(st, -.2)) + battlements(230, 70, 90, st, 4, 8) + windows(246, 90, 3, 5, 10, 16, 14, 16, WIN, True)
    return b
def stdavids():
    st = '#a8887a'
    b = day() + P('M-10 150 Q200 120 410 150 L410 320 L-10 320 Z', '#5a8a4a') + R(70, 170, 260, 92, st) + P('M70 170 L200 150 L330 170 Z', '#6a6a72')
    b += R(170, 110, 60, 152, st) + battlements(170, 110, 60, st, 4, 6) + windows(84, 190, 8, 1, 12, 34, 18, 0, WIN, True) + arch_win(186, 130, 28, 40, WIN)
    return b
def caernarfon():
    st = '#9a9088'
    b = day() + water(250, '#3f7aa8', 251, 12) + R(40, 140, 320, 110, st)
    for i in range(4): b += R(i * 20 + 40, 140, 320 - i * 40, 3, shade(st, -.1), 'opacity="0"')
    for x, h in ((40, 150), (150, 130), (260, 140), (360, 170)):
        b += P(f'M{x-22} 250 L{x-22} {250-h} L{x-12} {256-h-12} L{x+12} {256-h-12} L{x+22} {250-h} L{x+22} 250 Z', st) + battlements(x - 22, 250 - h, 44, st, 3, 6)
    for i in range(3): b += R(30 + i * 128, 166 + (i % 2) * 6, 300 / 3, 5, '#7a7068')
    return b
def conwy():
    st = '#7a7068'
    b = day() + water(236, '#3f7aa8', 261, 12) + R(70, 140, 260, 96, st) + battlements(70, 140, 260, st, 5, 7)
    for x in (70, 157, 243, 330): b += roundtower(x, 236, 22, 140, st)
    b += P('M330 200 L410 200 L410 210 L330 210 Z', '#b8b0a4') + L(340, 200, 380, 170, '#555', 1.5) + L(400, 200, 380, 170, '#555', 1.5)
    return b
def llandudno():
    b = day() + P('M-10 250 L-10 110 Q100 70 220 100 Q300 130 340 250 Z', '#5a8a4a') + P('M-10 140 Q80 110 180 120', '#4f7a40', 'opacity="0"')
    b += water(230, '#3f86b5', 271, 14) + P('M-10 320 L-10 262 Q200 250 410 262 L410 320 Z', '#ecd9a8')
    b += PL('M60 250 L120 170 L180 120', '#555', 1.5) + R(110, 168, 18, 10, '#2a5a9a') + R(170, 120, 18, 10, '#2a5a9a')
    b += houses(250, 272, 3, 40, 30, 40, ('#f3efe6', '#e8dcc4')).replace('x="-6"', 'x="300"', 0) + crowd(6, 200, 380, 276, 273, 1.0, 20)
    return b
def tenby():
    b = day() + houses(200, 281, 9, 46, 60, 90, ('#f4a6c8', '#ffcd00', '#7ac8e8', '#ffffff', '#f07a14', '#a8e0a0')) + R(0, 200, 400, 14, '#b8ab95')
    b += P('M-10 320 L-10 236 Q200 222 410 236 L410 320 Z', '#ecd9a8') + water(214, '#3f86b5', 282, 8) + boats(226, 283, 3)
    return b
def aberystwyth():
    b = day() + P('M-10 220 L-10 100 Q60 80 120 120 L160 220 Z', '#5a8a4a') + PL('M40 220 L110 110', '#555', 2) + R(98, 108, 14, 10, '#c8102e')
    b += houses(200, 291, 8, 46, 50, 70, ('#f3efe6', '#e8dcc4', '#ffcd00', '#7ac8e8', '#f4a6c8'))
    b += R(0, 200, 400, 18, '#b8ab95') + water(218, '#3f86b5', 292, 14) + R(300, 210, 110, 8, '#6b4a3a') + crowd(5, 60, 280, 214, 293, .9, 4)
    return b
def brecon():
    st = '#a8988a'
    b = day() + mountain(330, 100, 120, '#6a8a5a') + lawn(GY, '#4f8a45') + R(60, 160, 220, 102, st) + P('M60 160 L170 140 L280 160 Z', '#6a6a72') + R(230, 100, 60, 162, st) + battlements(230, 100, 60, st, 4, 6) + windows(76, 180, 6, 1, 12, 34, 16, 0, WIN, True)
    return b
def hay():
    b = day() + R(220, 90, 150, 172, '#a89f8c') + battlements(220, 90, 150, '#a89f8c', 5, 7) + road(GY, '#8a8f99')
    for k in range(4):
        y = 150 + k * 28; b += R(30, y, 170, 4, '#6b4a3a')
        rnd = random.Random(300 + k); x = 34
        while x < 196: w = rnd.randint(5, 10); h = rnd.randint(16, 24); b += R(x, y - h, w, h, rnd.choice(['#c8102e', '#1d4ed8', '#2a8a46', '#ffcd00', '#7a3a2a', '#f3efe6'])); x += w + 1
    b += R(26, 120, 4, 142, '#6b4a3a') + R(198, 120, 4, 142, '#6b4a3a') + P('M20 122 L110 98 L210 122 Z', '#5a5a62') + crowd(4, 60, 200, 278, 301, 1.0, 10)
    return b
def chepstow():
    st = '#a89f8c'
    b = day() + river(250, '#6a7a6a') + P('M-10 250 L-10 170 L240 160 L270 250 Z', '#7a7068') + R(30, 110, 220, 60, st) + battlements(30, 110, 220, st, 5, 7) + R(110, 70, 70, 100, st) + battlements(110, 70, 70, st, 4, 7) + windows(46, 126, 6, 1, 10, 20, 24, 0, WIN, True)
    b += tree(320, 250, 1.8) + tree(370, 250, 1.4)
    return b
def monmouth():
    st = '#a8a094'
    b = day() + river(232, '#4a7fa8') + R(-10, 196, 420, 18, st)
    for i in range(3): b += arch_win(60 + i * 110, 206, 70, 40, '#4a7fa8')
    b += R(170, 100, 60, 100, st) + P('M166 102 L200 70 L234 102 Z', '#6a6a72') + arch_win(186, 160, 28, 40, '#3b2a1a') + windows(182, 116, 2, 1, 8, 12, 20, 0, WIN, True)
    return b
def porthmadog():
    b = day() + mountain(300, 90, 160, '#5a7a4a') + lawn(236, '#5a8a4a') + R(0, 236, 400, 6, '#6b4a3a')
    b += R(80, 180, 110, 40, '#2a6a3a') + R(170, 160, 30, 60, '#2a6a3a') + R(90, 160, 14, 22, '#2a6a3a') + E(84, 200, 10, 18, '#2a6a3a') + C(110, 230, 12, '#c8102e') + C(150, 230, 12, '#c8102e') + C(185, 230, 10, '#c8102e')
    b += R(210, 190, 70, 34, '#7a3a2a') + windows(218, 196, 4, 1, 10, 10, 6, 0, '#f3efe6') + C(220, 230, 7, '#333') + C(270, 230, 7, '#333')
    for k in range(4): b += C(96 + k * 6, 146 - k * 12, 8 + k * 3, '#f3efe6', f'opacity="{.8-k*.15:.2f}"')
    return b
def swallowfalls():
    b = R(0, 0, W, H, '#cfe3ee', 'opacity="0"') + P('M-10 320 L-10 60 L140 40 L150 320 Z', '#5a5a52') + P('M410 320 L410 50 L260 40 L250 320 Z', '#4a4a44')
    b += P('M140 40 L260 40 L250 320 L150 320 Z', '#9fd0ea') + ''.join(PL(f'M{150+k*10} 40 L{155+k*9} 320', '#ffffff', 2, 'opacity=".7"') for k in range(11))
    b += pine(40, 70, 1.6) + pine(360, 60, 1.6) + pine(80, 90, 1.2) + E(200, 300, 100, 20, '#ffffff', 'opacity=".6"')
    return b
def pontcysyllte():
    b = day() + P('M-10 320 L-10 150 Q200 230 410 150 L410 320 Z', '#5a8a4a') + river(290, '#4a7fa8')
    b += R(-10, 110, 420, 12, '#5a5a62') + R(-10, 106, 420, 4, '#8a8a92')
    for i in range(10): b += P(f'M{i*42-6} 122 L{i*42+6} 122 L{i*42+10} 300 L{i*42-10} 300 Z', '#a8988a')
    b += P('M260 98 L330 98 L326 106 L264 106 Z', '#c8102e')
    return b
def cardigan():
    b = day() + river(240, '#4a7fa8') + P('M80 240 L90 140 L310 140 L320 240 Z', '#a89f8c') + battlements(90, 140, 220, '#a89f8c', 5, 7)
    b += R(150, 100, 100, 40, '#f3efe6') + P('M146 100 L200 76 L254 100 Z', '#5a5a62') + windows(160, 110, 4, 1, 12, 14, 10, 0, WIN) + tree(40, 240, 1.6) + tree(360, 240, 1.5)
    return b
def rhyl():
    b = day() + P('M-10 320 L-10 252 Q200 240 410 252 L410 320 Z', '#ecd9a8') + water(220, '#3f86b5', 311, 10)
    b += R(80, 150, 240, 70, '#e8e4dc') + E(200, 150, 70, 34, '#5a9ad0') + windows(96, 170, 10, 2, 14, 12, 8, 10, '#5a9ad0') + R(0, 214, 400, 10, '#b8ab95') + crowd(5, 40, 360, 270, 312, 1.0, 20)
    return b

# ---------------- Spain
def madrid():
    st = '#f0eadc'
    b = sun(330, 46, 14) + lawn(GY, '#c9b08a') + R(30, 120, 340, 142, st) + windows(46, 140, 16, 3, 10, 18, 10, 18, WIN)
    for i in range(10): b += R(110 + i * 18, 120, 6, 142, '#e2dccb')
    b += R(26, 112, 348, 10, '#e2dccb') + R(170, 96, 60, 18, st) + clockface(200, 104, 8)
    return b
def barcelona():
    st = '#c9a87a'
    b = sun(330, 46, 14) + cloud(80, 40, .7) + road(GY, '#8a8f99') + R(80, 170, 240, 92, st)
    for x, h in ((100, 150), (140, 190), (180, 170), (220, 200), (260, 180), (300, 140)):
        b += P(f'M{x-12} 172 L{x-8} {172-h} Q{x} {162-h-20} {x+8} {172-h} L{x+12} 172 Z', st) + C(x, 172 - h - 8, 5, '#d22630') + windows(x - 4, 190 - h, 1, int(h // 26), 6, 10, 0, 16, '#5a4a3a', True)
    b += P('M160 172 L200 120 L240 172 Z', shade(st, .1)) + R(170, 172, 60, 90, shade(st, -.1)) + L(330, 260, 330, 40, '#e0a020', 3) + L(330, 44, 250, 44, '#e0a020', 3)
    return b
def seville():
    b = sun(330, 46, 15) + R(0, 140, 400, 122, '#c96a4a') + windows(16, 156, 18, 2, 12, 18, 9, 16, '#f3e2b8', True)
    for x in (30, 370): b += R(x - 16, 60, 32, 202, '#c96a4a') + P(f'M{x-18} 62 L{x} 30 L{x+18} 62 Z', '#3a8a8a') + windows(x - 6, 80, 1, 5, 12, 14, 0, 18, '#f3e2b8', True)
    b += water(262, '#3f86b5', 401, 6) + R(0, 258, 400, 6, '#f3efe6') + ''.join(R(20 + i * 40, 252, 30, 12, ['#1d4ed8', '#ffcd00', '#f3efe6'][i % 3]) for i in range(10))
    return b
def valencia():
    b = sun(330, 46, 15) + water(240, '#5ab0d8', 411, 10) + R(0, 270, 400, 50, '#f3efe6')
    b += P('M40 240 Q130 130 260 150 Q200 180 160 240 Z', '#f8f8f8') + P('M70 240 L80 196 L200 186 L200 240 Z', '#dfe8ee') + ''.join(L(80 + k * 12, 194, 84 + k * 11, 240, '#c9d4dc', 1) for k in range(10))
    b += E(320, 210, 70, 34, '#f8f8f8') + E(320, 214, 40, 16, '#9fc8e0') + P('M250 214 Q320 150 390 214', '#ffffff', 'opacity="0"')
    return b
def granada():
    b = sun(330, 46, 14) + mountain(320, 60, 160, '#9aa8b8', 170, True) + P('M-10 320 L-10 180 L410 170 L410 320 Z', '#6a8a4a')
    b += R(40, 140, 320, 60, '#c46a4a') + battlements(40, 140, 320, '#c46a4a', 6, 8)
    for x in (60, 170, 260, 340): b += R(x - 14, 110, 28, 90, '#b55a3a') + battlements(x - 14, 110, 28, '#b55a3a', 3, 6)
    b += windows(80, 160, 10, 1, 10, 16, 18, 0, '#3a2a1a', True)
    for x in range(10, 400, 26): b += pine(x, 240 + (x % 3) * 6, 1.0, '#3f6a3a')
    return b
def cordoba():
    b = R(0, 0, W, H, '#3a2a1e')
    for i in range(6):
        x = 10 + i * 66
        b += R(x + 26, 120, 10, 200, '#e2d6bc') + P(f'M{x-6} 120 A36 34 0 0 1 {x+66} 120 L{x+60} 120 A30 28 0 0 0 {x} 120 Z', '#e2d6bc')
        for k in range(10):
            a1 = math.pi + k * math.pi / 10; a2 = math.pi + (k + 1) * math.pi / 10
            b += P(f'M{x+30+33*math.cos(a1):.1f} {120+31*math.sin(a1):.1f} L{x+30+33*math.cos(a2):.1f} {120+31*math.sin(a2):.1f} L{x+30+22*math.cos(a2):.1f} {120+20*math.sin(a2):.1f} L{x+30+22*math.cos(a1):.1f} {120+20*math.sin(a1):.1f} Z', '#b03a2a' if k % 2 else '#f3e6c8')
    b += R(0, 290, 400, 30, '#5a4030')
    return b
def bilbao():
    b = cloud(80, 40, .8) + sun(330, 46, 12) + river(240, '#5a8aa8')
    for x, y, w, h in ((80, 140, 90, 100), (150, 110, 80, 130), (210, 130, 100, 110), (290, 160, 70, 80)):
        b += P(f'M{x} {y+h} Q{x-10} {y+h/2} {x+10} {y} Q{x+w/2} {y-20} {x+w} {y+10} Q{x+w+10} {y+h/2} {x+w} {y+h} Z', '#c9cdd4') + PL(f'M{x+10} {y+20} Q{x+w/2} {y+h/2} {x+w-6} {y+h-10}', '#a8aeb8', 1.5)
    b += R(330, 180, 6, 60, '#b8a888') + R(40, 236, 360, 4, '#8a8478')
    return b
def sansebastian():
    b = sun(330, 46, 14) + cloud(90, 40, .7) + P('M-10 180 Q60 120 120 170 L120 200 L-10 200 Z', '#5a8a4a') + P('M300 190 Q350 120 410 160 L410 200 L300 200 Z', '#5a8a4a')
    b += E(210, 196, 26, 10, '#6a9a5a') + water(196, '#2a9ad0', 421, 14)
    b += P('M-10 320 L-10 240 Q200 200 410 240 L410 320 Z', '#ecd9a8') + R(-10, 236, 420, 6, '#f3efe6') + ''.join(R(10 + i * 30, 228, 2, 12, '#f3efe6') for i in range(14)) + crowd(8, 40, 360, 280, 422, 1.0, 20)
    return b
def zaragoza():
    st = '#c9a07a'
    b = sun(330, 46, 14) + river(250, '#5a8aa8') + R(30, 150, 340, 100, st) + windows(46, 170, 14, 1, 10, 30, 13, 0, '#5a4a3a', True)
    for x in (30, 370): b += R(x - 14, 60, 28, 190, st) + P(f'M{x-14} 60 L{x} 34 L{x+14} 60 Z', '#3a8a8a')
    for x in (120, 200, 280): b += R(x - 18, 128, 36, 22, st) + dome_tile(x, 128)
    return b
def dome_tile(x, y):
    g = P(f'M{x-20} {y} A20 22 0 0 1 {x+20} {y} Z', '#2a7a6a')
    for k in range(-2, 3): g += PL(f'M{x+k*8} {y} Q{x+k*4} {y-14} {x} {y-22}', '#f3d24a', 2)
    return g + R(x - 2, y - 30, 4, 8, '#2a7a6a')
def toledo():
    st = '#c9b48a'
    b = sun(330, 46, 14) + P('M-10 320 L-10 220 Q200 170 410 220 L410 320 Z', '#b8a07a') + river(290, '#5a8aa8')
    b += houses(220, 431, 9, 46, 20, 40, ('#d8c8a0', '#c9b08a', '#e8dcc4'))
    b += R(120, 90, 160, 110, st) + windows(136, 110, 7, 3, 10, 14, 10, 14, WIN)
    for x in (120, 280): b += R(x - 14, 60, 28, 140, st) + P(f'M{x-16} 62 L{x} 36 L{x+16} 62 Z', '#4a5a6a')
    return b
def salamanca():
    st = '#d8a868'
    b = sun(330, 46, 14) + R(0, 110, 400, 152, st) + R(0, 104, 400, 8, shade(st, -.1)) + windows(14, 124, 16, 2, 10, 16, 14, 14, '#5a4a3a')
    for i in range(14): b += arch_win(6 + i * 29, 200, 22, 62, '#4a3a2a')
    b += R(180, 70, 40, 40, st) + clockface(200, 88, 10) + ground(262, '#e2c79a') + crowd(10, 20, 380, 270, 441, 1.0, 30)
    return b
def santiago():
    st = '#a8a094'
    b = cloud(90, 40, .9, '#eef2f5') + cloud(300, 50, .8, '#eef2f5') + ground(262, '#a8a094')
    b += R(110, 140, 180, 122, st) + windows(130, 160, 6, 2, 12, 22, 14, 18, '#5a6a7a', True)
    for x in (110, 290): b += R(x - 26, 50, 52, 212, st) + P(f'M{x-20} 50 L{x} 20 L{x+20} 50 Z', st) + windows(x - 8, 70, 1, 5, 16, 22, 0, 12, '#5a6a7a', True)
    b += P('M150 140 L200 100 L250 140 Z', st) + crowd(10, 20, 380, 272, 451, 1.0, 30, ['#ffcd00', '#d22630', '#1d4ed8'])
    return b
def alicante():
    b = sun(330, 46, 14) + P('M80 230 L140 100 L220 80 L300 120 L340 230 Z', '#b8a07a') + R(150, 74, 90, 30, '#c9b48a') + battlements(150, 74, 90, '#c9b48a', 4, 6)
    b += water(230, '#2a9ad0', 461, 12) + P('M-10 320 L-10 262 Q200 250 410 262 L410 320 Z', '#ecd9a8') + palm(40, 270, 1.2) + palm(360, 270, 1.1, -6)
    return b
def murcia():
    st = '#d8c4a0'
    b = sun(330, 46, 14) + ground(262, '#d8c8a8') + R(60, 150, 200, 112, st) + P('M60 150 Q160 100 260 150 Z', st) + windows(80, 172, 5, 2, 18, 22, 18, 14, '#5a4a3a', True)
    b += R(270, 50, 60, 212, st) + windows(284, 70, 2, 5, 12, 16, 10, 18, '#5a4a3a', True) + R(276, 30, 48, 22, st) + dome_tile(300, 30)
    return b
def cadiz():
    b = sun(330, 46, 14) + water(230, '#2a8ad0', 471, 14) + R(0, 220, 400, 12, '#d8c8a8')
    b += R(110, 130, 180, 92, '#e8dcc4') + windows(126, 150, 7, 2, 12, 18, 12, 14, WIN, True) + R(170, 106, 60, 26, '#e8dcc4')
    b += P('M168 106 A32 34 0 0 1 232 106 Z', '#e0b030') + R(196, 64, 8, 10, '#e0b030')
    for x in (110, 290): b += R(x - 14, 90, 28, 132, '#e8dcc4') + P(f'M{x-14} 90 A14 14 0 0 1 {x+14} 90 Z', '#e0b030')
    b += houses(220, 472, 3, 40, 30, 50, ('#ffffff', '#ffcd00')).replace('x="-6"', 'x="-6"')
    return b
def ronda():
    b = sun(330, 46, 14) + P('M-10 320 L-10 110 L140 110 L150 320 Z', '#b8a07a') + P('M410 320 L410 100 L250 100 L240 320 Z', '#a8906a')
    b += houses(110, 481, 3, 46, 20, 30, ('#ffffff', '#f3efe6')) + R(260, 76, 140, 26, '#ffffff')
    b += R(130, 90, 130, 20, '#a8906a') + R(170, 110, 50, 210, '#a8906a') + arch_win(178, 130, 34, 70, '#5a8aa8') + R(140, 210, 30, 110, '#a8906a') + R(220, 210, 30, 110, '#a8906a')
    b += P('M150 320 L170 300 L220 300 L240 320 Z', '#5a8aa8')
    return b
def palma():
    st = '#d8b880'
    b = sun(330, 46, 14) + water(240, '#2a8ad0', 491, 14) + palm(40, 250, 1.2) + palm(370, 250, 1.1, -6)
    b += R(80, 120, 240, 120, st) + C(200, 160, 18, '#5a7aa8') + C(200, 160, 12, '#c9a46a') + windows(96, 140, 8, 1, 10, 50, 18, 0, '#5a4a3a', True)
    for x in range(80, 330, 40): b += R(x - 4, 90, 8, 30, st) + P(f'M{x-6} 92 L{x} 76 L{x+6} 92 Z', st)
    b += R(0, 236, 400, 8, '#d8c8a8')
    return b
def benidorm():
    b = sun(70, 46, 14) + cloud(300, 40, .7)
    rnd = random.Random(501)
    for x in range(0, 400, 32):
        h = rnd.randint(70, 200); b += R(x, 230 - h, 28, h, rnd.choice(['#f3efe6', '#e8dcc4', '#d8e4ee'])) + windows(x + 4, 238 - h, 3, h // 14, 5, 6, 3, 8, '#5a8ab0')
    b += P('M-10 320 L-10 236 Q200 226 410 236 L410 320 Z', '#ecd9a8') + water(262, '#2a9ad0', 502, 10)
    for x in range(30, 380, 40): b += L(x, 250, x, 232, '#555', 1.5) + P(f'M{x-12} 234 Q{x} 224 {x+12} 234 Z', ['#d22630', '#1d4ed8', '#ffcd00'][x // 40 % 3])
    return b
def tarragona():
    st = '#c9b48a'
    b = sun(330, 46, 14) + water(150, '#2a8ad0', 511, 14) + P('M-10 320 L-10 180 L410 170 L410 320 Z', '#b8a07a')
    b += E(200, 250, 170, 60, st) + E(200, 256, 120, 34, '#d8c49a')
    for k in range(4): b += PL(f'M{40+k*8} {250-k*10} Q200 {196-k*12} {360-k*8} {250-k*10}', shade(st, -.12), 2)
    b += windows(60, 200, 12, 1, 8, 12, 16, 0, '#7a6a4a', True)
    return b

PLAN = {
 'Cork': ('warm', cork), 'Galway': ('day', galway), 'Limerick': ('day', limerick), 'Waterford': ('day', waterford), 'Kilkenny': ('day', kilkenny),
 'Derry/Londonderry': ('day', derry), 'Killarney': ('day', killarney), 'Dingle': ('day', dingle), 'Westport': ('day', westport), 'Sligo': ('grey', sligo),
 'Donegal Town': ('day', donegal), 'Athlone': ('day', athlone), 'Wexford': ('day', wexford), 'Kinsale': ('bright', kinsale), 'Cobh': ('day', cobh),
 'Doolin': ('grey', doolin), 'Ennis': ('day', ennis), 'Carlingford': ('day', carlingford),
 'Inverness': ('day', inverness), 'Stirling': ('day', stirling), 'Perth': ('day', scone), 'St Andrews': ('day', standrews), 'Oban': ('day', oban),
 'Fort William': ('grey', fortwilliam), 'Pitlochry': ('day', pitlochry), 'Ayr': ('sunset', ayr), 'Dunfermline': ('day', dunfermline), 'Falkirk': ('day', kelpies),
 'Dumfries': ('day', dumfries), 'Peebles': ('day', peebles), 'Melrose': ('day', melrose), 'Portree': ('grey', storr), 'Kirkwall': ('grey', kirkwall), 'Lerwick': ('grey', lerwick),
 'Newport, Wales': ('day', newport_w), 'Wrexham': ('day', wrexham), 'Bangor': ('day', bangor), 'St Davids': ('day', stdavids), 'Caernarfon': ('day', caernarfon),
 'Conwy': ('day', conwy), 'Llandudno': ('bright', llandudno), 'Tenby': ('bright', tenby), 'Aberystwyth': ('day', aberystwyth), 'Brecon': ('day', brecon),
 'Hay-on-Wye': ('day', hay), 'Chepstow': ('day', chepstow), 'Monmouth': ('day', monmouth), 'Porthmadog': ('day', porthmadog), 'Betws-y-Coed': ('grey', swallowfalls),
 'Llangollen': ('day', pontcysyllte), 'Cardigan': ('day', cardigan), 'Rhyl': ('bright', rhyl),
 'Madrid': ('bright', madrid), 'Barcelona': ('bright', barcelona), 'Seville': ('bright', seville), 'Valencia': ('bright', valencia), 'Granada': ('bright', granada),
 'Córdoba': ('bright', cordoba), 'Bilbao': ('day', bilbao), 'San Sebastián': ('bright', sansebastian), 'Zaragoza': ('bright', zaragoza), 'Toledo': ('bright', toledo),
 'Salamanca': ('bright', salamanca), 'Santiago de Compostela': ('grey', santiago), 'Alicante': ('tropic', alicante), 'Murcia': ('bright', murcia), 'Cádiz': ('tropic', cadiz),
 'Ronda': ('bright', ronda), 'Palma de Mallorca': ('tropic', palma), 'Benidorm': ('tropic', benidorm), 'Tarragona': ('bright', tarragona),
}
TITLES = {'Wrexham': 'The Racecourse Ground', 'Perth': 'Scone Palace'}
for city, (sky, fn) in PLAN.items():
    add(city, sky, fn(), TITLES.get(city))
missing = [c for c in INFO if c not in S]
assert not missing, missing
