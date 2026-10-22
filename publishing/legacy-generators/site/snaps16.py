# Disney Parks book - polaroids (generic, no characters or logos)
from snaplib import *
import random, math, json
S = {}
INFO = json.load(open('/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/disney_snaps.json'))
def add(city, sky, body):
    t, n = INFO[city]
    slug = 'dp' + ''.join(ch for ch in city.lower() if ch.isalnum())
    S[city] = (t, n, scene(slug, sky, body))
WIN = '#4a5878'
def day(): return sun(330, 50, 13) + cloud(80, 46, .7) + cloud(240, 34, .5)
def lawn(y=GY, f='#4f8a45'): return ground(y, f, shade(f, .15))
def turret(x, base, w, h, wall, roof, gold=True):
    g = R(x - w / 2, base - h, w, h, wall) + R(x + w * .15, base - h, w * .35, h, shade(wall, -.1)) + P(f'M{x-w/2-3} {base-h} L{x} {base-h-w*2.2} L{x+w/2+3} {base-h} Z', roof)
    if gold: g += L(x, base - h - w * 2.2, x, base - h - w * 2.2 - 8, '#e0b030', 1.5) + C(x, base - h - w * 2.2 - 9, 1.6, '#e0b030')
    return g
def castle(wall, roof, base=GY, scale=1.0, centre_h=150):
    g = R(110, base - 70, 180, 70, wall) + arch_win(184, base - 46, 32, 46, '#5a4a6a') + battlements(110, base - 70, 180, wall, 5, 6)
    for x, w, h in ((120, 20, 100), (280, 20, 100), (150, 24, 120), (250, 24, 120), (175, 22, 140), (225, 22, 140), (200, 30, centre_h)):
        g += turret(x, base - 10, w * scale, h * scale, wall, roof)
    return g
def booths(y, n=4, cols=('#d22630', '#1d4ed8', '#2a8a46', '#f07a14')):
    g = ''
    for i in range(n):
        x = 30 + i * (340 / n); c = cols[i % len(cols)]
        g += R(x, y - 30, 60, 30, '#f3efe6') + P(f'M{x-6} {y-30} L{x+30} {y-46} L{x+66} {y-30} Z', c) + ''.join(R(x + k * 12, y - 30, 6, 6, '#ffffff') for k in range(5))
    return g
def fairy_lights(y0, seed):
    rnd = random.Random(seed); g = PL(f'M0 {y0} Q100 {y0+20} 200 {y0} T400 {y0}', '#333', 1)
    for k in range(26):
        x = k * 16; y = y0 + 10 * math.sin(k / 26 * math.pi * 4) + 6
        g += C(x, y, 2.4, rnd.choice(['#ffd84a', '#ff7a5a', '#7ad8ff', '#ffffff']))
    return g

def dlr_park(): return day() + lawn(GY, '#5a9a4a') + castle('#f2c6d2', '#4a7ac8') + R(0, 262, 400, 58, '#5a9a4a') + crowd(10, 30, 370, 270, 1, 1.0, 30)
def dca():
    b = day() + water(220, '#3f86b5', 2, 14)
    b += C(260, 140, 80, 'none', 'stroke="#f3efe6" stroke-width="6"') + C(260, 140, 10, '#f3efe6')
    for k in range(12):
        a = k * math.pi / 6; x = 260 + 80 * math.cos(a); y = 140 + 80 * math.sin(a)
        b += L(260, 140, x, y, '#f3efe6', 2) + R(x - 7, y - 4, 14, 12, ['#d22630', '#ffcd00', '#1d4ed8', '#2a8a46'][k % 4], 'rx="2"')
    b += P('M200 226 L260 140 L320 226 Z', 'none', 'stroke="#d8d4c8" stroke-width="5"')
    b += R(0, 214, 200, 10, '#c9a46a') + PL('M10 214 Q60 120 110 180 T190 150', '#d22630', 4) + R(0, 224, 400, 6, '#b8ab95')
    return b
def tokyo_dl(): return day() + lawn(GY, '#5a9a4a') + castle('#f3f0e8', '#3a6ac8', centre_h=170) + crowd(10, 30, 370, 270, 3, 1.0, 30)
def tds():
    b = day() + P('M60 230 L170 70 L230 70 L340 230 Z', '#8a5a4a') + P('M170 70 L190 88 L210 76 L230 70 Z', '#5a3a2a') + C(190, 50, 12, '#c9c4bc', 'opacity=".8"') + C(205, 36, 9, '#c9c4bc', 'opacity=".6"')
    b += water(226, '#2f7fb0', 4, 14) + P('M0 226 L80 226 L80 200 L0 200 Z', '#d8c4a0') + windows(6, 206, 4, 1, 10, 12, 8, 0, WIN) + boat(260, 250, 1.6, '#f3efe6', '#c9a46a')
    return b
def paris_park(): return day() + lawn(GY, '#5a9a4a') + castle('#f2b8c6', '#3a5ab0', centre_h=160) + flowers(20, 380, 270, 5, 30)
def frozen():
    b = R(0, 0, W, H, '#ffffff', 'opacity="0"') + P('M-10 230 L60 90 L120 160 L200 50 L280 150 L340 80 L410 230 Z', '#cfe3f3') + P('M200 50 L220 90 L180 92 Z M60 90 L74 118 L46 118 Z', '#ffffff')
    b += water(230, '#4a7fa8', 6, 10)
    for x, c in ((40, '#c8102e'), (100, '#3a6a8a'), (160, '#e8b030'), (230, '#2a6a4a'), (300, '#c8102e'), (350, '#f3efe6')):
        b += R(x, 196, 44, 34, c) + P(f'M{x-4} 196 L{x+22} 174 L{x+48} 196 Z', '#4a3a3a') + windows(x + 8, 204, 2, 1, 10, 10, 8, 0, '#ffe9a8')
    return b
def hk():
    b = day() + mountain_bg('#6a8a5a') + lawn(GY, '#5a9a4a')
    cols = ['#e84a7f', '#7ad8ff', '#ffcd00', '#b45ce0', '#2a8a46', '#f07a14']
    b += R(110, GY - 70, 180, 70, '#f3efe6') + arch_win(184, GY - 46, 32, 46, '#5a4a6a')
    for i, (x, w, h) in enumerate(((120, 20, 100), (150, 24, 124), (175, 22, 144), (200, 30, 164), (225, 22, 144), (250, 24, 124), (280, 20, 100))):
        b += turret(x, GY - 10, w, h, '#f3efe6', cols[i % 6])
    return b
def mountain_bg(c): return P('M-10 262 L-10 230 L80 120 L160 180 L260 100 L410 200 L410 262 Z', c)
def shanghai():
    b = day() + water(250, '#4a7fa8', 7, 8) + lawn(GY + 10, '#5a9a4a')
    b += R(120, 170, 160, 80, '#f3efe6') + arch_win(184, 200, 32, 50, '#5a4a6a')
    for x, w, h in ((130, 22, 110), (270, 22, 110), (160, 26, 140), (240, 26, 140)): b += turret(x, 250, w, h, '#f3efe6', '#2a5ab0')
    b += R(186, 60, 28, 190, '#f3efe6') + P('M182 60 L200 -6 L218 60 Z', '#e0b030') + windows(194, 80, 1, 5, 12, 14, 0, 18, '#5a7aa8', True)
    return b
def typhoon():
    b = day() + P('M60 250 L170 90 L250 90 L360 250 Z', '#6a8a5a') + P('M150 112 L270 112 L262 128 L158 128 Z', '#8a5a3a') + R(196, 74, 4, 40, '#5a3a2a') + R(220, 84, 4, 30, '#5a3a2a')
    b += water(236, '#3fb0d8', 8, 16) + palm(40, 250, 1.3, 6) + palm(370, 250, 1.2, -6) + P('M-10 320 L-10 270 Q200 258 410 270 L410 320 Z', '#ecd9a8')
    return b
def blizzard():
    b = day() + P('M60 250 L170 70 L250 70 L360 250 Z', '#e8f2f8') + P('M170 70 L250 70 L230 100 L190 100 Z', '#ffffff') + PL('M200 80 L230 250', '#3a8ad0', 6) + PL('M190 80 Q120 160 150 250', '#d22630', 5)
    b += R(196, 66, 30, 8, '#8a5a3a') + water(250, '#3fb0d8', 9, 10) + palm(40, 260, 1.2, 6) + palm(370, 260, 1.2, -6)
    return b
def uk_gardens():
    b = day() + lawn(240, '#5a9a4a')
    b += R(40, 140, 120, 100, '#f3efe6') + ''.join(L(40 + k * 20, 140, 40 + k * 20, 240, '#3a2a1a', 3) for k in range(7)) + L(40, 190, 160, 190, '#3a2a1a', 3) + P('M34 142 L100 104 L166 142 Z', '#6a4a3a')
    b += R(240, 150, 120, 90, '#c9a07a') + windows(254, 166, 4, 2, 12, 16, 14, 14, WIN) + P('M234 152 L300 120 L366 152 Z', '#5a5a62')
    for x in (60, 130, 200, 270, 340):
        b += C(x, 236, 14, '#3f8a45') + C(x, 216, 10, '#4f9a55') + C(x, 200, 6, '#5aa45a')
    b += flowers(10, 390, 260, 10, 70)
    return b
def american():
    b = day() + lawn(GY, '#5a9a4a') + R(90, 120, 220, 120, '#b05a3a') + windows(104, 140, 9, 3, 12, 16, 10, 12, '#f3efe6')
    b += R(170, 90, 60, 30, '#f3efe6') + P('M168 90 A32 30 0 0 1 232 90 Z', '#f3efe6') + R(196, 50, 8, 14, '#f3efe6') + booths(GY + 4, 4)
    return b
def france_arts():
    b = day() + R(20, 120, 200, 140, '#e8dcc4') + windows(34, 140, 7, 3, 12, 18, 14, 14, WIN, True) + P('M14 122 L120 96 L226 122 Z', '#5a6a7a')
    b += P('M300 260 L320 60 L340 260 Z', 'none', 'stroke="#7a6a5a" stroke-width="4"') + L(306, 190, 334, 190, '#7a6a5a', 3) + L(312, 130, 328, 130, '#7a6a5a', 3) + ground(260, '#d8c8a8')
    for x, c in ((80, '#ffcd00'), (160, '#e84a7f'), (240, '#1d4ed8')):
        b += L(x - 14, 300, x, 240, '#6b4a3a', 2) + L(x + 14, 300, x, 240, '#6b4a3a', 2) + R(x - 18, 236, 36, 28, '#f3efe6') + C(x, 250, 8, c)
    return b
def norway_holidays():
    b = sun(330, 50, 12, '#fff3b0') + R(0, 0, 0, 0, '#000') + ground(GY, '#e8f2f8', '#ffffff')
    b += R(130, 150, 140, 112, '#7a3a2a') + P('M120 150 L200 100 L280 150 Z', '#3a2a2a') + R(176, 70, 48, 40, '#7a3a2a') + P('M170 72 L200 30 L230 72 Z', '#3a2a2a') + P('M186 34 L200 10 L214 34 Z', '#3a2a2a')
    b += windows(148, 170, 4, 2, 14, 18, 18, 16, '#ffd84a') + P('M330 262 L352 180 L374 262 Z', '#2a6a3a') + C(352, 176, 4, '#ffd84a')
    b += fairy_lights(120, 11) + stars(12, 20, 60)
    return b
def grizzly():
    b = day() + P('M40 250 L120 110 Q160 70 200 100 L240 80 L280 120 L360 250 Z', '#b0684a') + P('M200 100 L240 80 L250 120 Z', '#8a4a3a')
    b += pine(30, 250, 1.6) + pine(370, 252, 1.8) + water(250, '#4a7fa8', 13, 6) + R(0, 262, 400, 58, '#5a8a4a')
    for x, c in ((80, '#d22630'), (200, '#ffcd00'), (320, '#2a8a46')): b += R(x - 2, 170, 4, 90, '#555') + R(x + 2, 172, 24, 40, c)
    return b
def paradise_holidays():
    b = stars(14, 30, 120) + moon(330, 50) + water(220, '#1a2a5a', 15, 10, '#ffd84a') + R(0, 214, 400, 10, '#c9a46a')
    b += palm(60, 214, 1.3, 6) + palm(340, 214, 1.2, -6) + fairy_lights(140, 16) + fairy_lights(180, 17)
    b += ground(262, '#3a3a44') + crowd(10, 20, 380, 270, 18, 1.0, 30)
    return b
def med_harbor():
    b = day() + houses_it(200) + water(200, '#2f7fb0', 19, 14) + booths(GY + 6, 3, ('#d22630', '#2a8a46', '#ffcd00'))
    b += P('M120 228 Q200 240 280 228 L272 236 Q200 246 128 236 Z', '#222') + R(250, 210, 3, 20, '#333')
    return b
def houses_it(y):
    rnd = random.Random(20); g = ''
    for i in range(9):
        x = -6 + i * 46; h = rnd.randint(70, 120); c = rnd.choice(['#e8b878', '#d88a5a', '#f3dcb0', '#c96a4a', '#f0c890'])
        g += R(x, y - h, 44, h, c) + windows(x + 7, y - h + 10, 3, max(1, h // 24), 6, 10, 6, 12, '#3a6a6a') + R(x - 1, y - h - 5, 46, 5, '#a85a3a')
    return g
def chalets(winter=False):
    b = (stars(21, 30, 120) + moon(330, 50)) if winter else day()
    b += ground(GY, '#ffffff' if winter else '#d8c8a8')
    for i, x in enumerate((30, 150, 270)):
        b += R(x, 170, 100, 92, '#8a5a3a') + P(f'M{x-10} 172 L{x+50} 130 L{x+110} 172 Z', '#ffffff' if winter else '#5a3a2a') + R(x + 10, 196, 80, 30, '#ffd84a' if winter else '#f3e2b8') + R(x + 6, 226, 88, 6, '#5a3a2a')
    if winter: b += fairy_lights(150, 22) + ''.join(C(random.Random(k).uniform(0, 400), random.Random(k + 99).uniform(0, 250), 1.5, '#ffffff') for k in range(40))
    else: b += C(200, 120, 14, '#7ad8ff', 'opacity=".6"') + crowd(8, 20, 380, 274, 23, 1.0, 30)
    return b
def springs():
    b = day() + water(220, '#3f86b5', 24, 14) + houses_it(220).replace('#a85a3a', '#7a4a3a')
    b += L(260, 220, 260, 120, '#555', 1) + C(260, 90, 34, '#f3efe6') + R(250, 120, 20, 12, '#3a3a3a') + PL('M226 90 L294 90', '#1d4ed8', 6) + R(0, 236, 400, 84, '#c9b48a') + crowd(8, 20, 380, 262, 25, 1.0, 40)
    return b
def promenade():
    b = sun(330, 50, 13, '#ffd27a', '#ff9e5a') + R(0, 120, 120, 142, '#e8b878') + R(280, 110, 120, 152, '#d88a5a') + windows(10, 140, 4, 3, 16, 18, 12, 16, '#ffe9a8') + windows(290, 130, 4, 3, 16, 18, 12, 16, '#ffe9a8')
    b += ground(GY, '#c9b48a') + palm(150, 262, 1.4, 6) + palm(250, 262, 1.3, -6) + fairy_lights(100, 26) + crowd(12, 20, 380, 272, 27, 1.0, 30)
    return b
def village():
    b = stars(28, 30, 100) + moon(60, 40) + R(0, 140, 400, 122, '#3a2a4a')
    for x, t, c in ((20, 'BAR', '#ff4a7a'), (150, 'SALOON', '#ffd84a'), (290, 'DINER', '#4ad8ff')):
        b += R(x, 150, 100, 112, '#4a3a5a') + R(x + 10, 120, 80, 26, '#111', 'rx="4"') + T(x + 50, 140, t, 18, c, 'letter-spacing="2"') + windows(x + 12, 170, 3, 2, 18, 18, 10, 14, '#ffd27a')
    b += ground(GY, '#2a2a34') + fairy_lights(110, 29) + crowd(10, 20, 380, 272, 30, 1.0, 30)
    return b
def ikspiari():
    b = day() + houses_it(250) + ground(250, '#d8c8a8') + C(200, 270, 26, '#9aa8b8') + C(200, 270, 18, '#7ab8e0') + R(196, 236, 8, 30, '#9aa8b8') + crowd(10, 20, 380, 280, 31, 1.0, 30)
    return b
def insp_lake():
    b = day() + P('M-10 220 L70 110 L150 170 L240 80 L330 150 L410 120 L410 220 Z', '#5a7a4a') + water(210, '#4a8ab8', 32, 14) + lawn(270, '#5a9a4a')
    b += P('M120 240 L160 240 L156 248 L124 248 Z', '#ffcd00') + P('M260 230 L296 230 L292 238 L264 238 Z', '#d22630') + tree(30, 270, 1.4) + tree(370, 270, 1.6)
    return b
def disneytown():
    b = day() + water(200, '#4a8ab8', 33, 12)
    b += R(276, 150, 40, 50, '#c9d4e8', 'opacity=".7"') + P('M290 150 L296 110 L302 150 Z', '#c9a46a', 'opacity=".7"')
    b += houses_it(260).replace('#a85a3a', '#5a3a6a') + ground(260, '#c9b48a') + fairy_lights(140, 34) + crowd(8, 20, 380, 280, 35, 1.0, 30)
    return b

PLAN = {'Disneyland Park, California': ('day', dlr_park), 'Disney California Adventure': ('bright', dca), 'Tokyo Disneyland': ('day', tokyo_dl), 'Tokyo DisneySea': ('day', tds),
 'Disneyland Park, Paris': ('day', paris_park), 'Disney Adventure World': ('grey', frozen), 'Hong Kong Disneyland': ('day', hk), 'Shanghai Disneyland': ('day', shanghai),
 'Typhoon Lagoon': ('tropic', typhoon), 'Blizzard Beach': ('bright', blizzard), 'EPCOT Flower & Garden Festival': ('day', uk_gardens), 'EPCOT Food & Wine Festival': ('day', american),
 'EPCOT Festival of the Arts': ('bright', france_arts), 'EPCOT Festival of the Holidays': ('night', norway_holidays), 'California Adventure Food & Wine Festival': ('day', grizzly),
 'California Adventure Festival of Holidays': ('night', paradise_holidays), 'DisneySea Food & Wine Festival': ('day', med_harbor), 'Le Rendez-vous Gourmand': ('day', lambda: chalets(False)),
 "L'Hiver Gourmand": ('night', lambda: chalets(True)), 'Disney Springs': ('dusk', springs), 'Downtown Disney District': ('sunset', promenade), 'Disney Village': ('night', village),
 'Ikspiari': ('day', ikspiari), 'Inspiration Lake': ('day', insp_lake), 'Disneytown': ('dusk', disneytown)}
for c, (sky, fn) in PLAN.items(): add(c, sky, fn())
missing = [c for c in INFO if c not in S and c not in ('Magic Kingdom', 'EPCOT', 'Hollywood Studios', 'Animal Kingdom')]
assert not missing, missing
