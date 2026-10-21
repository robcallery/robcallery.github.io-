from snaplib import *
import random

S = {}
def add(city, title, note, sky, body, defs=''):
    slug = ''.join(ch for ch in city.lower() if ch.isalnum())
    S[city] = (title, note, scene(slug, sky, body, defs))
WIN = '#4a5878'

def lighthouse(x, base, h, body='#f4f1ea', band='#d22630', s=1.0):
    w = 14 * s
    g = P(f'M{x-w} {base} L{x-w*.7} {base-h} L{x+w*.7} {base-h} L{x+w} {base} Z', body)
    for k in range(3):
        y = base - h * (.2 + k * .28)
        g += P(f'M{x-w*.92+k*1.2} {y} L{x+w*.92-k*1.2} {y} L{x+w*.9-k*1.2} {y-h*.1} L{x-w*.9+k*1.2} {y-h*.1} Z', band)
    g += R(x - w * .8, base - h - 12 * s, w * 1.6, 12 * s, '#ffe27a') + P(f'M{x-w} {base-h-12*s} L{x} {base-h-24*s} L{x+w} {base-h-12*s} Z', band) + R(x - w * 1.1, base - h - 2 * s, w * 2.2, 3 * s, '#2a2a2a')
    return g

# Newcastle - Tyne Bridge
def newcastle():
    b = sun(330, 60, 13) + cloud(90, 50, .8) + cloud(250, 30, .5)
    rnd = random.Random(701)
    for i in range(12):
        x = i * 36 - 10; h = rnd.randint(40, 90)
        b += R(x, 200 - h, 34, h, rnd.choice(['#c4a27a', '#b98b6a', '#d8c8a8', '#a8826a'])) + windows(x + 5, 200 - h + 8, 3, int(h / 18), 6, 8, 4, 8, WIN)
    g = '#2f6b4a'
    b += PL('M40 200 Q200 40 360 200', g, 9) + PL('M40 200 Q200 56 360 200', g, 3)
    for k in range(1, 16):
        t = k / 16; px = (1 - t) ** 2 * 40 + 2 * (1 - t) * t * 200 + t * t * 360; py = (1 - t) ** 2 * 200 + 2 * (1 - t) * t * 40 + t * t * 200
        b += L(px, py, px, 150, g, 1.6) if py < 150 else ''
    b += R(0, 146, W, 8, g)
    for x in (30, 350):
        b += R(x - 14, 110, 28, 110, '#c9bca0') + R(x - 16, 104, 32, 8, '#b3a58c') + windows(x - 8, 120, 2, 3, 6, 12, 4, 12, WIN, arch=True)
    b += water(220, '#4f6f7a', 702, 16)
    b += P('M120 262 L220 262 L210 274 L130 274 Z', '#2b3a55') + R(150, 250, 40, 12, '#f4f1ea')
    return b
add('Newcastle upon Tyne', 'The Tyne Bridge', 'Opened in 1928 - built by Dorman Long, the same firm as Sydney Harbour Bridge.', 'day', newcastle())

# Sunderland - Roker Pier
def sunderland():
    b = sun(70, 60, 13) + cloud(260, 50, .8)
    b += water(150, '#3f86b5', 711, 22)
    b += P('M-10 210 L250 186 L262 190 L262 198 L-10 222 Z', '#d9c7b0') + P('M-10 222 L262 198 L262 204 L-10 230 Z', '#b9a690')
    b += ''.join(R(x, 214 - x * .093, 3, 8, '#b9a690') for x in range(0, 250, 16))
    b += lighthouse(262, 190, 70, '#e9dcc8', '#c0392b', 1.2)
    b += P('M-10 250 Q200 236 410 248 L410 320 L-10 320 Z', '#ecd9a8')
    b += crowd(10, 30, 380, 262, 712, 1.05, 40)
    return b
add('Sunderland', 'Roker Pier', 'Opened 1903 - there\'s a tunnel running all the way along inside it to the lighthouse.', 'day', sunderland())

# Middlesbrough - Transporter Bridge
def middlesbrough():
    b = sun(320, 210, 20, '#ffd27a', '#ff9e5a') + cloud(90, 60, .8, '#ffe1c7')
    b += R(0, 200, W, 30, '#5a5a66')
    for x in (60, 340):
        b += P(f'M{x-22} 240 L{x-8} 40 L{x+8} 40 L{x+22} 240', 'none', 'stroke="#3a4a6a" stroke-width="3"')
        for k in range(1, 10): b += L(x - 22 + k * 1.5, 240 - k * 20, x + 22 - k * 1.5, 240 - k * 20, '#3a4a6a', 1.6) + L(x - 22 + k * 1.5, 240 - k * 20, x + 22 - (k + 1) * 1.5, 240 - (k + 1) * 20, '#3a4a6a', .8)
    b += R(20, 34, 360, 10, '#3a4a6a') + ''.join(L(30 + k * 12, 34, 36 + k * 12, 44, '#5a6a8a', 1) for k in range(30))
    b += L(196, 44, 186, 190, '#3a4a6a', 1.2) + L(204, 44, 214, 190, '#3a4a6a', 1.2) + R(170, 190, 60, 10, '#3a4a6a') + R(184, 182, 20, 8, '#d22630', 2)
    b += water(230, '#5a6f7f', 721, 14)
    return b
add('Middlesbrough', 'The Transporter Bridge', 'Opened in 1911 - a gondola slung under the frame carries cars across the Tees.', 'sunset', middlesbrough())

# Darlington - Locomotion
def darlington():
    b = sun(330, 50, 13) + cloud(90, 50, .8)
    b += hills(200, '#8fae7a', 731, 10) + ground(240, '#6f9a5c', '#86ad6f')
    b += R(0, 236, W, 6, '#6b4a3a') + ''.join(R(x, 242, 10, 4, '#5a3a2a') for x in range(0, 400, 18))
    x = 160
    b += R(x - 50, 176, 110, 46, '#2a5a3a', 6) + R(x - 56, 172, 6, 50, '#c9a227') + R(x + 60, 186, 8, 30, '#2a2a2a')
    b += R(x - 30, 120, 12, 56, '#2a2a2a') + R(x - 34, 116, 20, 6, '#2a2a2a')
    b += C(x - 20, 100, 12, '#e8e8f0', 'opacity=".8"') + C(x - 6, 82, 16, '#e8e8f0', 'opacity=".7"') + C(x + 16, 66, 20, '#e8e8f0', 'opacity=".6"')
    for cx in (x - 30, x + 30): b += C(cx, 226, 14, '#2a2a2a') + C(cx, 226, 4, '#c9a227')
    for k in range(3): b += L(x - 16 + k * 16, 168, x - 16 + k * 16, 140, '#c9a227', 2)
    b += R(x - 20, 140, 36, 4, '#c9a227')
    b += R(x + 80, 196, 60, 30, '#6b4a2a') + C(x + 92, 232, 8, '#2a2a2a') + C(x + 128, 232, 8, '#2a2a2a') + crowd(3, x + 86, x + 134, 198, 732, .9, 2)
    b += crowd(6, 20, 100, 270, 733, 1.05, 30)
    return b
add('Darlington', 'Locomotion No. 1', 'The Stockton & Darlington Railway opened in 1825 - the first public steam railway.', 'day', darlington())

# Hartlepool - HMS Trincomalee
def hartlepool():
    b = sun(330, 60, 13) + cloud(90, 50, .8) + cloud(230, 30, .5)
    b += R(0, 180, W, 30, '#c9b48f') + windows(10, 186, 16, 1, 14, 14, 10.5, 0, '#4a5878')
    b += water(210, '#3f6f8a', 741, 14)
    b += P('M50 212 L340 212 L320 250 L70 250 Z', '#1b1b1b') + R(60, 220, 270, 6, '#f4f1ea') + windows(76, 221, 14, 1, 6, 4, 12, 0, '#1b1b1b')
    b += P('M340 212 L372 200 L346 220 Z', '#1b1b1b')
    for x, h in ((120, 150), (200, 170), (280, 140)):
        b += R(x, 212 - h, 3, h, '#5a3a22')
        for k in range(3):
            y = 212 - h + 20 + k * 34; w = 30 - k * 3
            b += R(x - w, y, w * 2 + 3, 3, '#5a3a22') + R(x - w + 2, y + 3, w * 2 - 1, 22 - k * 3, '#f4f1ea', ex='opacity=".85"')
    b += L(372, 200, 280, 72, '#3b3b3b', .7) + L(50, 212, 120, 62, '#3b3b3b', .7)
    b += P('M200 40 l14 4 l-14 4 z', '#d22630')
    return b
add('Hartlepool', 'HMS Trincomalee', 'Launched in 1817 - the oldest British warship still afloat.', 'day', hartlepool())

# Stockton - Infinity Bridge
def stockton():
    b = moon(330, 50, 12) + stars(751, 30, 120)
    rnd = random.Random(752)
    for i in range(8):
        x = i * 52; h = rnd.randint(30, 70)
        b += R(x, 170 - h, 46, h, '#2a3456') + windows(x + 6, 170 - h + 6, 4, int(h / 14), 4, 5, 6, 8, '#ffe27a')
    b += R(0, 168, W, 8, '#3a4466')
    b += water(176, '#1f2f55', 753, 10, '#8fa8ff')
    for cx, w, h in ((150, 220, 70), (310, 120, 40)):
        b += PL(f'M{cx-w/2} 176 Q{cx} {176-h*2} {cx+w/2} 176', '#e6f0ff', 4) + PL(f'M{cx-w/2} 176 Q{cx} {176+h*2} {cx+w/2} 176', '#e6f0ff', 4, 'opacity=".45"')
        for k in range(1, 9):
            t = k / 9; px = cx - w / 2 + w * t; py = (1 - t) ** 2 * 176 + 2 * (1 - t) * t * (176 - h * 2) + t * t * 176
            b += L(px, py, px, 170, '#e6f0ff', .8)
    b += R(30, 168, 340, 4, '#e6f0ff')
    return b
add('Stockton-on-Tees', 'The Infinity Bridge', 'Its arches and their reflection in the Tees make an infinity sign - best seen at night.', 'night', stockton())

# Gateshead - Millennium Bridge & Baltic
def gateshead():
    b = sun(70, 60, 13) + cloud(260, 50, .8)
    b += R(250, 60, 90, 150, '#a8623e') + windows(262, 70, 5, 8, 10, 10, 6, 6, '#3a3a4a') + R(250, 54, 90, 8, '#8a4a2e') + T(295, 100, 'BALTIC', 12, '#f4f1ea', 'letter-spacing="2"')
    b += P('M40 200 Q60 120 110 116 Q150 112 170 130 Q160 160 120 180 Z', '#c9ced8', 'opacity=".9"') + P('M44 196 Q64 130 110 126 Q144 124 162 136', 'none', 'stroke="#a3aab5" stroke-width="2"')
    b += P('M100 210 Q200 70 300 210', 'none', 'stroke="#f4f4f4" stroke-width="5"')
    for k in range(1, 12):
        t = k / 12; px = (1 - t) ** 2 * 100 + 2 * (1 - t) * t * 200 + t * t * 300; py = (1 - t) ** 2 * 210 + 2 * (1 - t) * t * 70 + t * t * 210
        b += L(px, py, px + (200 - px) * .1, 214, '#f4f4f4', .8)
    b += PL('M100 214 Q200 232 300 214', '#f4f4f4', 4)
    b += water(210, '#4f6f7a', 761, 14)
    b += R(0, 200, 100, 14, '#8a8475') + R(300, 200, 100, 14, '#8a8475')
    return b
add('Gateshead', 'The Millennium Bridge', 'The "blinking eye" - the whole bridge tilts up to let boats through.', 'day', gateshead())

# South Shields - Groyne lighthouse & beach
def southshields():
    b = sun(320, 60, 13) + cloud(90, 50, .8)
    b += water(150, '#3f86b5', 771, 20)
    b += P('M120 200 L330 170 L336 176 L130 210 Z', '#8a8475')
    b += lighthouse(330, 172, 50, '#d22630', '#f4f1ea', 1)
    b += P('M-10 220 Q200 200 410 216 L410 320 L-10 320 Z', '#ecd9a8')
    b += ''.join(R(30 + i * 22, 236, 16, 12, c) + P(f'M{29+i*22} 236 L{38+i*22} 230 L{47+i*22} 236 Z', shade(c, -.2)) for i, c in enumerate(('#d22630', '#1d4ed8', '#ffcd00', '#2a8a46')))
    b += crowd(12, 130, 390, 250, 772, 1.05, 50)
    return b
add('South Shields', 'Littlehaven & the Groyne', 'One of the oldest surviving lifeboats, the Tyne (1833), is on display on Ocean Road.', 'day', southshields())

# Washington - Old Hall
def washington():
    st = '#b8a07c'; dk = shade(st, -.18)
    b = sun(330, 50, 13) + cloud(90, 50, .8)
    b += R(80, 130, 240, 110, st) + P('M76 130 L200 90 L324 130 Z', '#6b5a50')
    for x in (100, 290): b += R(x, 76, 14, 40, dk)
    b += windows(96, 146, 5, 2, 30, 26, 12, 20, '#4a5878')
    for x in range(96, 320, 42):
        for y in (146, 192): b += L(x + 15, y, x + 15, y + 26, st, 1.2) + L(x, y + 13, x + 30, y + 13, st, 1)
    b += R(186, 200, 28, 40, '#5a3a22')
    b += R(250, 60, 2, 70, '#5a5a5a') + R(252, 60, 30, 18, '#f4f1ea') + ''.join(R(252, 62 + k * 3.4, 30, 1.7, '#d22630') for k in range(0, 5, 2)) + R(252, 60, 12, 9, '#1d3a8f')
    b += ground(240, '#5f8f55', '#79a86b') + flowers(0, 400, 244, 781, 40)
    b += tree(30, 246, 1.6) + tree(380, 246, 1.6)
    return b
add('Washington', 'Washington Old Hall', 'The family home of George Washington\'s ancestors - the name came from here.', 'day', washington())
