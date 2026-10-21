from snaplib import *
import random

S = {}
def add(city, title, note, sky, body, defs=''):
    slug = ''.join(ch for ch in city.lower() if ch.isalnum())
    S[city] = (title, note, scene(slug, sky, body, defs))

WIN = '#4a5878'

def castle(cx, base, s, wall, roof, accent=None):
    g = ''
    def tower(x, w, h, rh):
        return R(x - w / 2, base - h, w, h, wall) + R(x + w / 2 - w * .25, base - h, w * .25, h, shade(wall, -.12)) + P(f'M{x-w/2-2} {base-h} L{x} {base-h-rh} L{x+w/2+2} {base-h} Z', roof) + L(x, base - h - rh, x, base - h - rh - 8 * s, '#c9a227', 1) + P(f'M{x} {base-h-rh-8*s} l6 2 l-6 2 z', accent or '#d22630')
    for dx, w, h, rh in ((-70, 18, 70, 30), (70, 18, 70, 30), (-44, 22, 104, 40), (44, 22, 104, 40), (-22, 20, 128, 44), (22, 20, 128, 44), (0, 30, 160, 58)):
        g += tower(cx + dx * s, w * s, h * s, rh * s)
    g += R(cx - 80 * s, base - 60 * s, 160 * s, 60 * s, wall) + battlements(cx - 80 * s, base - 60 * s, 160 * s, wall, 3, 5)
    g += arch_win(cx - 14 * s, base - 40 * s, 28 * s, 40 * s, '#3b2a1a')
    g += windows(cx - 64 * s, base - 48 * s, 3, 1, 6 * s, 12 * s, 8 * s, 0, WIN, arch=True) + windows(cx + 26 * s, base - 48 * s, 3, 1, 6 * s, 12 * s, 8 * s, 0, WIN, arch=True)
    return g

# Malaga - Cathedral "La Manquita"
def malaga():
    st = '#d9c49e'; dk = shade(st, -.18)
    b = sun(330, 50, 14) + cloud(110, 50, .6)
    b += R(70, 130, 240, 120, st) + R(70, 124, 240, 8, dk) + windows(86, 146, 6, 2, 16, 30, 22, 20, WIN, arch=True)
    b += R(70, 60, 60, 190, st) + R(118, 60, 12, 190, dk) + windows(84, 80, 2, 3, 10, 22, 12, 16, WIN, arch=True)
    b += R(64, 54, 72, 8, dk) + R(80, 34, 40, 20, st) + P('M80 34 Q100 10 120 34 Z', '#a8b3a0') + R(99, 4, 2, 10, '#c9a227')
    b += R(250, 100, 60, 150, st) + R(298, 100, 12, 150, dk) + R(244, 94, 72, 8, dk) + windows(262, 116, 2, 2, 10, 22, 16, 16, WIN, arch=True)
    b += P('M180 124 Q220 70 260 124 Z', '#3f6f8f') + P('M220 124 Q220 74 260 124 Z', '#2f5f7f')
    b += arch_win(176, 196, 28, 54, '#3b2a1a')
    b += palm(30, 262, 1.3, 6) + palm(360, 262, 1.4, -8) + palm(340, 266, 1, 6)
    b += R(0, 250, W, 70, '#e9dcc0') + R(0, 250, W, 3, '#f6ecd6')
    b += crowd(14, 40, 360, 262, 301, 1.05, 34)
    return b
add('Málaga', 'Málaga Cathedral', '"La Manquita" - the one-armed lady. The money for the second tower ran out.', 'bright', malaga())

# Benalmadena - Buddhist Stupa
def benalmadena():
    b = sun(80, 60, 14) + cloud(300, 50, .6)
    b += water(220, '#2f86c5', 311, 14)
    b += P('M-10 230 Q150 150 260 120 Q340 110 410 150 L410 320 L-10 320 Z', '#b9a77e') + P('M-10 250 Q150 190 410 190 L410 320 L-10 320 Z', '#8fa070')
    x = 270
    b += R(x - 60, 160, 120, 20, '#f4f1ea') + R(x - 46, 140, 92, 22, '#ffffff')
    b += P(f'M{x-40} 142 Q{x-40} 90 {x} 88 Q{x+40} 90 {x+40} 142 Z', '#ffffff') + P(f'M{x} 88 Q{x+40} 90 {x+40} 142 L{x+10} 142 Z', '#ebe7de')
    b += R(x - 12, 74, 24, 16, '#ffffff') + P(f'M{x-8} 74 L{x} 20 L{x+8} 74 Z', '#e6c25a') + ''.join(L(x - 8 + k * .8, 70 - k * 6, x + 8 - k * .8, 70 - k * 6, '#c9a227', 1) for k in range(8))
    b += R(x - 10, 150, 20, 30, '#c9a227')
    b += ''.join(R(x - 60 + i * 16, 180 + i * 0, 10, 4, '#d8d2c4') for i in range(0))
    for i, hx in enumerate(range(20, 180, 32)):
        b += R(hx, 230 - i * 6, 28, 22, '#ffffff') + R(hx, 226 - i * 6, 28, 5, '#c0613a') + R(hx + 10, 236 - i * 6, 8, 8, '#4a7fa8')
    b += palm(170, 250, 1, 4)
    return b
add('Benalmádena', 'The Buddhist Stupa', 'The biggest stupa in Europe, high above the Costa del Sol.', 'tropic', benalmadena())

# Marne-la-Vallee - fairytale castle by day
def marne():
    b = sun(330, 50, 13) + cloud(80, 50, .8) + cloud(250, 40, .5)
    b += tree(30, 262, 2, '#3f8f4a') + tree(370, 262, 2.2, '#3f8f4a')
    b += castle(200, 236, 1.05, '#f3d6dc', '#3f6fb0', '#ffcd00')
    b += P('M120 236 Q200 226 280 236 L280 240 L120 240 Z', '#7fa8c8')
    b += ground(240, '#5f9a50', '#7ab36a') + R(170, 240, 60, 80, '#e3d6be')
    b += flowers(0, 160, 244, 321, 30) + flowers(240, 400, 244, 322, 30)
    b += crowd(16, 130, 270, 268, 323, 1.05, 40)
    return b
add('Marne-la-Vallée', 'Disneyland Paris', 'Opened in 1992 - and it\'s straight off the TGV from Charles de Gaulle.', 'day', marne())

# Amsterdam - canal houses
def amsterdam():
    b = sun(340, 50, 12) + cloud(90, 40, .7)
    cols = ['#5a3a2a', '#8a4a32', '#2f3a4a', '#a8623e', '#e8dcc4', '#3e5a4a', '#7a2f2a', '#c4a27a']
    x = -6; i = 0
    rnd = random.Random(331)
    while x < 410:
        w = rnd.choice([38, 42, 46]); h = rnd.randint(110, 150); c = cols[i % len(cols)]
        top = 210 - h
        b += R(x, top, w, h, c)
        gt = rnd.choice(['step', 'bell', 'neck'])
        if gt == 'step':
            b += R(x + 4, top - 8, w - 8, 8, c) + R(x + 10, top - 16, w - 20, 8, c) + R(x + 16, top - 22, w - 32, 6, c)
        elif gt == 'bell':
            b += P(f'M{x+2} {top} Q{x+2} {top-18} {x+w/2} {top-26} Q{x+w-2} {top-18} {x+w-2} {top} Z', c) + P(f'M{x+w/2-5} {top-24} Q{x+w/2} {top-32} {x+w/2+5} {top-24} Z', '#f7f2e4')
        else:
            b += R(x + 8, top - 20, w - 16, 20, c) + P(f'M{x+6} {top-20} L{x+w/2} {top-30} L{x+w-6} {top-20} Z', c)
        wc = '#f7f2e4' if c != '#e8dcc4' else '#4a5878'
        b += windows(x + 6, top + 10, 3, 4, (w - 20) / 3, 14, 4, 10, wc)
        b += R(x + w / 2 - 1, top - 4, 2, 6, '#2a2a2a')
        x += w; i += 1
    b += R(0, 210, W, 12, '#7a6a5a') + water(222, '#4a6f6a', 332, 16)
    b += P('M120 226 Q200 200 280 226 L280 234 Q200 210 120 234 Z', '#8a5a3a') + R(120, 222, 160, 4, '#6a4a2a')
    for k in range(5): b += bike(30 + k * 16, 208, '#1b1b1b', .9)
    for k in range(4): b += bike(300 + k * 16, 208, ['#1b1b1b', '#d22630', '#1d4ed8', '#1b1b1b'][k], .9)
    b += P('M40 290 L180 290 L172 302 L48 302 Z', '#2b3a55') + R(60, 278, 100, 12, '#e8f0f6', 4) + windows(66, 281, 8, 1, 8, 6, 3.6, 0, '#7fb0d9')
    return b
add('Amsterdam', 'The canal ring', 'The houses lean forward on purpose, so furniture can be hoisted up past the windows.', 'day', amsterdam())

# Malia - Minoan palace by the sea
def malia():
    b = sun(320, 70, 16, '#fff3b0', '#ffe27a') + cloud(100, 50, .5)
    b += P('M-10 150 Q100 120 200 140 Q300 120 410 140 L410 170 L-10 170 Z', '#9a8a8a')
    b += water(160, '#1f86c5', 341, 16)
    b += P('M-10 220 Q200 200 410 214 L410 320 L-10 320 Z', '#dccaa0')
    for x, y, w, h in ((40, 236, 70, 16), (130, 230, 90, 20), (240, 238, 60, 14), (70, 262, 110, 18), (210, 262, 120, 16)):
        b += R(x, y, w, h, '#c9b48f') + R(x, y, w, 3, '#e0cfab')
    for i in range(5):
        x = 140 + i * 18
        b += P(f'M{x} 230 L{x-2} 182 L{x+10} 182 L{x+8} 230 Z', '#a8322e') + R(x - 5, 176, 18, 7, '#1b1b1b') + E(x + 4, 175, 9, 3, '#3b2a1a')
    b += R(130, 168, 100, 10, '#c9b48f')
    for x in (30, 360): b += P(f'M{x-6} 300 Q{x} 250 {x+6} 300 Z', '#5a7a3a')
    b += ''.join(E(330 + k * 8, 200, 4, 2.5, '#5a7a4a') for k in range(0))
    return b
add('Malia', 'Palace of Malia', 'Minoan palace ruins around 4,000 years old, just along from the strip.', 'tropic', malia())

# Tokyo - Tokyo Tower
def tokyo():
    b = stars(351, 40, 120) + moon(340, 40, 11)
    rnd = random.Random(352)
    for i in range(16):
        x = i * 26 - 8; h = rnd.randint(40, 120)
        b += R(x, 260 - h, 24, h, rnd.choice(['#1b2440', '#222c4a', '#2a3456']))
        for yy in range(int(260 - h + 6), 255, 9):
            for xx in range(int(x + 3), int(x + 22), 6):
                if rnd.random() < .5: b += R(xx, yy, 3, 4, '#ffe27a', 'opacity=".8"')
    x = 200; o = '#f0582a'; w = '#f4f1ea'
    b += P(f'M{x-60} 260 L{x-8} 90 L{x+8} 90 L{x+60} 260 L{x+44} 260 L{x+4} 110 L{x-4} 110 L{x-44} 260 Z', o)
    for k, y in enumerate(range(240, 100, -20)):
        hw = 60 - (260 - y) * .3
        b += L(x - hw, y, x + hw, y - 20 + 3, o, 1.6) + L(x + hw, y, x - hw, y - 20 + 3, o, 1.6)
    b += R(x - 36, 196, 72, 10, w) + R(x - 24, 130, 48, 12, w)
    b += P(f'M{x-8} 90 L{x-2} 20 L{x+2} 20 L{x+8} 90 Z', o) + R(x - 10, 70, 20, 6, w) + R(x - 9, 50, 18, 5, o) + R(x - 1, 8, 2, 14, w)
    b += C(x, 8, 2, '#ff4d4d')
    b += R(0, 260, W, 60, '#2a2f44') + ''.join(R(10 + i * 50, 290, 26, 3, '#f7f2e4') for i in range(8))
    return b
add('Tokyo', 'Tokyo Tower', '333 metres, opened 1958 - painted orange and white to keep air-safety rules happy.', 'night', tokyo())

# Osaka - Osaka Castle
def osaka():
    wall = '#f4f1ea'; roof = '#3f7f73'
    b = sun(330, 50, 13) + cloud(90, 50, .8)
    b += P('M40 300 L60 230 L340 230 L360 300 Z', '#8a8475') + ''.join(L(60 + k * 20, 236, 50 + k * 22, 298, '#7a7466', 1) for k in range(15))
    x = 200
    tiers = [(230, 140, 30), (200, 118, 28), (172, 98, 26), (146, 80, 24), (122, 62, 22)]
    for y, w, h in tiers:
        b += R(x - w / 2 + 6, y - h, w - 12, h, wall) + windows(x - w / 2 + 14, y - h + 8, 4, 1, 8, 10, (w - 46) / 3, 0, '#2a3a3a')
        b += P(f'M{x-w/2-8} {y-h+2} L{x-w/2+4} {y-h-10} L{x+w/2-4} {y-h-10} L{x+w/2+8} {y-h+2} Z', roof)
        b += P(f'M{x-14} {y-h-10} Q{x} {y-h-22} {x+14} {y-h-10} Z', roof)
        b += C(x - w / 2 - 8, y - h + 1, 2, '#c9a227') + C(x + w / 2 + 8, y - h + 1, 2, '#c9a227')
    b += P(f'M{x-30} 100 L{x-24} 84 L{x+24} 84 L{x+30} 100 Z', roof) + P(f'M{x-24} 86 L{x-30} 76 L{x-20} 82 Z M{x+24} 86 L{x+30} 76 L{x+20} 82 Z', '#c9a227')
    b += tree(30, 300, 2.2, '#e88aa8') + tree(370, 300, 2.4, '#e88aa8') + tree(70, 306, 1.6, '#f2a6c0')
    b += water(300, '#3f7f8f', 361, 4)
    return b
add('Osaka', 'Osaka Castle', 'The main tower was rebuilt in 1931 - the museum inside is worth the climb.', 'day', osaka())

# Narita - Naritasan pagoda
def narita():
    b = sun(80, 60, 13) + cloud(300, 50, .7)
    b += tree(40, 280, 2.6, '#2f6b3c') + tree(360, 280, 2.8, '#2f6b3c') + tree(320, 284, 2, '#3f7f45')
    x = 200; red = '#c8322a'; roof = '#2a3a3a'
    for k, (y, w) in enumerate(((270, 120), (214, 100), (158, 82))):
        b += R(x - w / 2 + 16, y - 46, w - 32, 46, red) + R(x - w / 2 + 22, y - 40, w - 44, 30, '#2a6b8a', 'opacity=".6"')
        b += P(f'M{x-w/2-10} {y-44} Q{x} {y-56} {x+w/2+10} {y-44} L{x+w/2-6} {y-56} L{x-w/2+6} {y-56} Z', roof)
        b += R(x - w / 2 + 2, y - 50, w - 4, 4, '#c9a227')
    b += R(x - 2, 46, 4, 58, '#c9a227') + ''.join(E(x, 56 + i * 9, 6, 2, '#c9a227') for i in range(5)) + C(x, 44, 3, '#c9a227')
    b += R(0, 280, W, 40, '#bdb39f')
    b += crowd(8, 40, 360, 290, 371, 1.05, 20)
    return b
add('Narita', 'Naritasan Shinshoji', 'A temple founded in 940 - ten minutes from the airport, perfect for a long layover.', 'day', narita())

# Kyoto - Fushimi Inari torii
def kyoto():
    b = sun(200, 40, 10, '#fff3b0', '#ffe27a')
    b += R(0, 0, W, H, '#2f5a3a', 'opacity=".55"')
    b += tree(30, 260, 3, '#2a5a35') + tree(380, 260, 3.2, '#2a5a35')
    red = '#e2532a'
    for i in range(10):
        t = i / 9
        s = 1.6 - t * 1.2
        cx = 200 + math.sin(t * 2) * 40 * t; base = 300 - t * 150
        w = 150 * s; h = 170 * s
        x0 = cx - w / 2
        b += R(x0 + w * .12, base - h, 10 * s, h, red) + R(x0 + w * .88 - 10 * s, base - h, 10 * s, h, red)
        b += R(x0, base - h - 4 * s, w, 12 * s, '#1b1b1b') + R(x0 + w * .06, base - h + 14 * s, w * .88, 8 * s, red)
        b += R(x0 + w * .12, base - 12 * s, 10 * s, 12 * s, '#1b1b1b') + R(x0 + w * .88 - 10 * s, base - 12 * s, 10 * s, 12 * s, '#1b1b1b')
    b += P('M100 320 L170 150 L230 150 L300 320 Z', '#b9a98a', 'opacity=".5"')
    return b
add('Kyoto', 'Fushimi Inari', 'Around 10,000 torii gates winding up the mountain. Go at sunrise.', 'warm', kyoto())

# Orlando - Lake Eola fountain
def orlando():
    b = sun(330, 70, 14, '#ffd27a', '#ff9e5a') + cloud(90, 50, .7, '#ffe1c7')
    rnd = random.Random(381)
    for i in range(10):
        x = 10 + i * 40; h = rnd.randint(60, 150)
        b += R(x, 200 - h, 34, h, rnd.choice(['#5a6a8a', '#6a7a9a', '#4a5a7a'])) + windows(x + 4, 200 - h + 6, 4, int(h / 14), 4, 6, 3, 8, '#ffe27a')
    b += R(0, 196, W, 10, '#4f8f50') + water(206, '#3f6f9a', 382, 14)
    x = 200
    b += P(f'M{x-60} 250 L{x-40} 226 L{x+40} 226 L{x+60} 250 Z', '#f4f1ea')
    for k, c in enumerate(('#e84a7f', '#4dd2ff', '#ffcd00')):
        b += P(f'M{x-40+k*6} 226 L{x-26+k*8} {190-k*14} L{x+26-k*8} {190-k*14} L{x+40-k*6} 226 Z', 'none', f'stroke="{c}" stroke-width="2"')
    b += PL(f'M{x} 180 Q{x-30} 160 {x-50} 226 M{x} 180 Q{x+30} 160 {x+50} 226 M{x} 170 L{x} 226', '#e6f4fb', 2.5, 'opacity=".8"')
    for sx in (90, 300):
        b += E(sx, 280, 16, 8, '#ffffff') + P(f'M{sx+10} 280 Q{sx+20} 260 {sx+12} 254', 'none', 'stroke="#ffffff" stroke-width="4" stroke-linecap="round"') + P(f'M{sx+12} 254 l6 2 l-6 2 z', '#f07a14')
    b += palm(30, 210, .9, 4) + palm(370, 210, 1, -4)
    return b
add('Orlando', 'Lake Eola', 'Downtown Orlando\'s fountain - hire a swan boat and pedal round it.', 'sunset', orlando())

# Tampa Bay - Plant Hall minarets
def tampa():
    st = '#a84a32'; dk = shade(st, -.18)
    b = sun(70, 60, 13) + cloud(260, 50, .7)
    b += R(30, 150, 340, 100, st) + R(30, 144, 340, 8, dk) + windows(42, 164, 14, 2, 10, 20, 13.6, 18, '#f4f1ea', arch=True)
    for x in (60, 150, 250, 340):
        h = 70 if x in (150, 250) else 56
        b += R(x - 10, 144 - h, 20, h, st)
        b += P(f'M{x-14} {150-h} Q{x-16} {120-h} {x} {108-h} Q{x+16} {120-h} {x+14} {150-h} Z', '#c0c6cc') + P(f'M{x} {108-h} Q{x+16} {120-h} {x+14} {150-h} L{x} {150-h} Z', '#a3aab2')
        b += L(x, 108 - h, x, 96 - h, '#c9a227', 1.4) + P(f'M{x-3} {98-h} Q{x} {92-h} {x+3} {98-h}', 'none', 'stroke="#c9a227" stroke-width="1.4"')
        b += windows(x - 5, 156 - h, 1, 2, 10, 14, 0, 10, '#f4f1ea', arch=True)
    b += palm(20, 268, 1.2, 4) + palm(380, 268, 1.3, -6) + palm(200, 272, .9, 4)
    b += ground(250, '#5f9a50', '#7ab36a') + R(0, 268, W, 52, '#d8cdb8')
    b += crowd(10, 40, 360, 274, 391, 1.05, 30)
    return b
add('Tampa Bay', 'Plant Hall', 'Built as the Tampa Bay Hotel in 1891 - those silver minarets are now the university.', 'tropic', tampa())

# Kissimmee - airboat & gator
def kissimmee():
    b = sun(320, 70, 16, '#ffd27a', '#ff9e5a') + cloud(100, 50, .7, '#ffe1c7')
    b += hills(190, '#4f7f45', 401, 6, 7)
    for x in range(-10, 410, 36): b += P(f'M{x} 200 Q{x+6} 140 {x+12} 200 Z', '#3f6f3a') + tree(x + 20, 202, .9, '#5f8f50')
    b += water(200, '#5a7f6a', 402, 18)
    for x in range(0, 400, 14): b += PL(f'M{x} 206 l2 -12 M{x+4} 206 l-1 -9', '#7a9a5a', 1.4)
    b += P('M120 250 L260 250 L250 262 L130 262 Z', '#d8dce2') + R(150, 236, 40, 14, '#c9ced8') + C(170, 232, 4, '#f1c9a5')
    b += C(236, 228, 22, 'none', 'stroke="#555" stroke-width="2"') + ''.join(L(236, 228, 236 + math.cos(a) * 20, 228 + math.sin(a) * 20, '#777', 1) for a in (0, 1.57, 3.14, 4.71)) + R(234, 226, 4, 24, '#555')
    b += crowd(4, 140, 200, 248, 403, .9, 2)
    b += P('M40 290 Q70 282 100 288 Q120 292 130 290 L130 294 Q90 298 40 294 Z', '#3f5a2a') + C(48, 288, 2, '#ffe27a')
    for k in range(6): b += P(f'M{58+k*10} 286 l3 -4 l3 4 z', '#3f5a2a')
    return b
add('Kissimmee', 'Airboats on the lakes', 'Airboat out on Lake Toho and count the gators. There will be gators.', 'sunset', kissimmee())

# Chicago - Willis Tower
def chicago():
    b = sun(70, 50, 12) + cloud(290, 60, .8)
    rnd = random.Random(411)
    for i in range(14):
        x = i * 30 - 10; h = rnd.randint(50, 130)
        b += R(x, 230 - h, 28, h, rnd.choice(['#8a96a8', '#9aa6b8', '#7a869a'])) + windows(x + 3, 230 - h + 4, 4, int(h / 10), 4, 5, 2.5, 5, '#c9d8e8')
    x = 200; d = '#2a2d36'
    for dx, top in ((-30, 70), (-10, 30), (10, 30), (30, 90), (-30, 120)):
        b += R(x + dx - 10, top, 20, 230 - top, d)
    b += R(x - 40, 30, 80, 200, d, ex='opacity="0"')
    for yy in range(36, 228, 8): b += L(x - 40, yy, x + 40, yy, '#3a3e4a', 1)
    b += R(x - 16, 10, 3, 22, '#c9ced8') + R(x + 13, 6, 3, 26, '#c9ced8')
    b += water(230, '#3f7fa8', 412, 14)
    b += boat(100, 262, 2, '#f7f7f7', '#1d4ed8')
    return b
add('Chicago', 'Willis Tower', '442 metres - step out onto The Ledge, a glass box 103 floors up.', 'day', chicago())

# Philadelphia - Independence Hall
def philadelphia():
    br = '#a8503a'; dk = shade(br, -.2)
    b = sun(330, 50, 13) + cloud(90, 50, .8)
    b += R(40, 150, 320, 100, br) + R(40, 144, 320, 8, '#f4f1ea') + windows(56, 164, 8, 2, 16, 26, 22, 22, '#2a3a4a')
    b += P('M120 144 L200 132 L280 144 Z', dk)
    x = 200
    b += R(x - 26, 70, 52, 80, br) + R(x - 30, 66, 60, 6, '#f4f1ea') + arch_win(x - 10, 90, 20, 40, '#2a3a4a')
    b += R(x - 20, 40, 40, 26, '#f4f1ea') + clockface(x, 53, 9)
    b += R(x - 14, 22, 28, 18, '#f4f1ea') + ''.join(R(x - 12 + k * 7, 26, 3, 12, '#2a3a4a') for k in range(4))
    b += P(f'M{x-12} 22 Q{x} 6 {x+12} 22 Z', '#f4f1ea') + R(x - 1, 0, 2, 10, '#c9a227')
    b += R(x - 10, 210, 20, 40, '#f4f1ea') + arch_win(x - 6, 214, 12, 36, '#3b2a1a')
    b += ground(250, '#5f8f55', '#79a86b') + R(150, 250, 100, 70, '#cfc2a4')
    b += tree(20, 256, 1.8) + tree(380, 256, 1.8)
    b += crowd(10, 120, 300, 270, 421, 1.05, 40)
    return b
add('Philadelphia', 'Independence Hall', 'Where the Declaration of Independence was signed in 1776.', 'day', philadelphia())

# Lake Buena Vista - Disney Springs balloon
def lbv():
    b = sun(320, 220, 20, '#ffd27a', '#ff9e5a') + cloud(90, 60, .8, '#ffe1c7')
    x, y = 260, 90
    b += C(x, y, 40, '#ffcd00') + ''.join(P(f'M{x-40+k*16} {y} Q{x-40+k*16+8} {y-40} {x} {y-40} Q{x-40+k*16+8} {y+40} {x} {y+40}', 'none', 'stroke="#f07a14" stroke-width="2"') for k in range(0)) + P(f'M{x-40} {y} A40 40 0 0 1 {x+40} {y} Z', '#d22630', 'opacity=".25"')
    b += P(f'M{x-40} {y} Q{x-20} {y+40} {x-14} {y+46} L{x+14} {y+46} Q{x+20} {y+40} {x+40} {y} Z', '#ffcd00')
    b += R(x - 40, y - 2, 80, 6, '#1d4ed8')
    b += L(x - 12, y + 46, x - 10, y + 70, '#555', 1) + L(x + 12, y + 46, x + 10, y + 70, '#555', 1) + R(x - 14, y + 70, 28, 10, '#6b4a2a')
    b += L(x, y + 80, x, 230, '#777', .8)
    for i, c in enumerate(('#e8dcc4', '#c9a27e', '#a8623e', '#f0e6d2', '#7a9a8a', '#d8c8a8')):
        bx = 10 + i * 66; h = 50 + (i % 3) * 14
        b += R(bx, 230 - h, 60, h, c) + windows(bx + 8, 230 - h + 10, 3, 2, 10, 12, 8, 10, '#ffe27a') + P(f'M{bx-2} {230-h} L{bx+30} {218-h} L{bx+62} {230-h} Z', shade(c, -.3))
    b += water(230, '#3f6f9a', 431, 16)
    b += P('M60 270 L140 270 L134 280 L66 280 Z', '#f4f1ea') + R(80, 262, 40, 8, '#1d4ed8')
    return b
add('Lake Buena Vista', 'Disney Springs', 'The tethered balloon goes up to 400 feet for a view over the whole resort.', 'sunset', lbv())
