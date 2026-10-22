from snaplib import *
from snaps4 import castle
import random

S = {}
def add(city, title, note, sky, body, defs=''):
    slug = ''.join(ch for ch in city.lower() if ch.isalnum())
    S[city] = (title, note, scene(slug, sky, body, defs))

WIN = '#4a5878'

def runway(y=250):
    return R(0, y, W, H - y, '#4b505c') + R(0, y, W, 2, '#6b7080') + ''.join(R(10 + i * 50, y + 34, 26, 3, '#f7f2e4') for i in range(8))

# Magic Kingdom
def mk():
    b = stars(501, 50, 120) + moon(60, 40, 10)
    b += fireworks(80, 90, 34, '#ffcd00') + fireworks(320, 70, 30, '#e84a7f') + fireworks(250, 40, 20, '#4dd2ff') + fireworks(130, 40, 18, '#7dff7a')
    b += castle(200, 236, 1.05, '#e9ecf4', '#2f5fb0', '#ffcd00')
    b += R(0, 236, W, 84, '#3a3f58') + R(170, 236, 60, 84, '#4a4f68')
    b += crowd(30, 10, 390, 254, 502, 1.05, 50)
    return b
add('Magic Kingdom', 'The castle at Magic Kingdom', '189 feet tall - just under the height that would need an aircraft warning light.', 'night', mk())

# Hollywood Studios
def hs():
    st = '#d8b48a'; dk = shade(st, -.25)
    b = stars(511, 20, 100) + cloud(90, 60, 1.1, '#3a3f66', .9) + cloud(300, 40, 1, '#3a3f66', .9)
    b += P('M330 20 L310 60 L322 60 L300 110 L336 54 L322 54 L340 20 Z', '#fff7b0')
    x = 200
    b += R(x - 50, 40, 100, 220, st) + R(x + 30, 40, 20, 220, dk)
    b += windows(x - 40, 60, 5, 10, 10, 10, 6, 8, '#3a2a2a')
    for k in (2, 5, 11, 17, 26, 33, 41): b += R(x - 40 + (k % 5) * 16, 60 + (k // 5) * 18, 10, 10, '#ffe27a')
    b += R(x - 56, 34, 112, 8, dk) + P(f'M{x-40} 34 L{x-30} 14 L{x-20} 34 Z M{x+20} 34 L{x+30} 14 L{x+40} 34 Z', '#7a4a3a')
    b += R(x - 72, 110, 22, 150, st) + R(x + 50, 130, 26, 130, st)
    b += R(x - 30, 96, 60, 10, '#b03a2e') + T(x, 104, 'HOLLYWOOD TOWER HOTEL', 6, '#ffe27a', 'textLength="56" lengthAdjust="spacingAndGlyphs"')
    b += tree(40, 262, 2, '#2a4a3a') + palm(360, 262, 1.2, -6)
    b += R(0, 260, W, 60, '#3a3f58')
    b += crowd(16, 20, 380, 270, 512, 1.05, 40)
    return b
add('Hollywood Studios', 'Tower of Terror', 'Thirteen storeys of drop - and it does it more than once.', 'dusk', hs())

# Animal Kingdom - Tree of Life
def ak():
    b = sun(330, 50, 14) + cloud(90, 40, .7)
    b += hills(200, '#8fae6a', 521, 8)
    x = 200
    b += P(f'M{x-50} 250 Q{x-20} 200 {x-24} 140 Q{x-60} 110 {x-90} 120 L{x-20} 118 Q{x} 90 {x+20} 118 L{x+90} 120 Q{x+60} 110 {x+24} 140 Q{x+20} 200 {x+50} 250 Z', '#a88a6a')
    for k in range(10):
        b += PL(f'M{x-30+k*6} 240 Q{x-16+k*3} 190 {x-10+k*2} 140', '#8a6a4a', 1.4)
    rnd = random.Random(522)
    for i in range(40):
        a = rnd.uniform(math.pi, 2 * math.pi); r = rnd.uniform(20, 100)
        b += C(x + math.cos(a) * r * 1.3, 110 + math.sin(a) * r * .5, rnd.uniform(14, 22), rnd.choice(['#3f8f45', '#4f9f50', '#5fae55', '#2f7f3c', '#8fae4a']))
    b += ground(250, '#b9a06a', '#c9b07a')
    for gx, gy, s in ((60, 262, 1), (330, 270, .8)):
        b += P(f'M{gx} {gy} l0 -18 l-2 -22 l4 0 l2 22 l10 0 l0 18 Z', '#e6b450', f'transform="scale(1)"')
        b += R(gx - 2, gy - 18, 16, 10, '#e6b450') + R(gx - 2, gy - 8, 2, 12, '#c9963a') + R(gx + 12, gy - 8, 2, 12, '#c9963a') + R(gx - 2, gy - 44, 4, 26, '#e6b450') + E(gx - 2, gy - 44, 5, 3, '#e6b450')
        for k in range(5): b += C(gx + (k % 3) * 4, gy - 14 - (k // 3) * 12, 1.4, '#a8702a')
    b += crowd(10, 110, 290, 272, 523, 1.05, 30)
    return b
add('Animal Kingdom', 'The Tree of Life', 'Look closely - there are more than 300 animals carved into the trunk.', 'warm', ak())

# Islands of Adventure - lighthouse & coaster
def ioa():
    b = sun(70, 50, 13) + cloud(260, 40, .7)
    d = 'M120 250 Q130 120 200 110 Q280 100 280 170 Q280 230 220 220 Q160 210 180 150 Q200 90 300 90 Q380 90 390 250'
    b += PL(d, '#2a8a46', 6) + PL(d, '#5fd06a', 2)
    for xx in (140, 200, 260, 320, 380): b += L(xx, 250, xx, 120 + (xx % 60), '#c9ced8', 2)
    b += water(240, '#2f86c5', 531, 16)
    x = 70
    b += P(f'M{x-16} 250 L{x-10} 110 L{x+10} 110 L{x+16} 250 Z', '#f4f1ea') + ''.join(P(f'M{x-14+k*1.2} {230-k*34} L{x+14-k*1.2} {230-k*34} L{x+14-k*1.2-.6} {216-k*34} L{x-14+k*1.2+.6} {216-k*34} Z', '#d22630') for k in range(4))
    b += R(x - 14, 98, 28, 14, '#ffe27a') + P(f'M{x-16} 98 L{x} 82 L{x+16} 98 Z', '#d22630') + R(x - 18, 108, 36, 4, '#2a2a2a')
    b += P(f'M{x+14} 104 L{x+60} 92 L{x+60} 116 Z', '#fff7b0', 'opacity=".5"')
    b += boat(200, 276, 1.5, '#f4f1ea', '#1d4ed8')
    return b
add('Universal Islands of Adventure', 'Port of Entry', 'The Hulk coaster launches you up and out over the lagoon.', 'tropic', ioa())

# Universal Studios Florida - backlot street
def usf():
    b = sun(330, 50, 13) + cloud(90, 40, .7)
    cols = ['#a8623e', '#d8c8a8', '#7a2f2a', '#c4a27a', '#5a6a7a', '#e3d6be']
    for i, x in enumerate(range(-10, 410, 52)):
        h = 110 + (i % 3) * 30
        c = cols[i % 6]
        b += R(x, 250 - h, 50, h, c) + windows(x + 6, 250 - h + 10, 3, int(h / 26), 9, 12, 5, 12, '#2a3a4a')
        b += R(x + 4, 228, 42, 4, '#d22630' if i % 2 else '#1d4ed8') + R(x + 16, 232, 18, 18, '#2a2a2a')
    b += R(150, 120, 100, 34, '#1b1b1b', 3) + T(200, 143, 'NOW SHOWING', 14, '#ffe27a', 'textLength="84" lengthAdjust="spacingAndGlyphs"')
    for k in range(10): b += C(156 + k * 9.8, 124, 1.6, '#ffe27a') + C(156 + k * 9.8, 150, 1.6, '#ffe27a')
    b += f'<g transform="translate(330 250) rotate(-8)">' + R(-24, -30, 48, 30, '#1b1b1b') + ''.join(P(f'M{-24+k*12} -40 l8 0 l-4 10 l-8 0 z', '#f4f1ea') for k in range(4)) + R(-24, -40, 48, 10, 'none', ex='stroke="#1b1b1b" stroke-width="1.5"') + '</g>'
    b += P('M40 250 L60 120 L66 120', 'none', 'stroke="#fff7b0" stroke-width="10" opacity=".25"')
    b += road(250, '#4a4f5a')
    b += crowd(24, 10, 390, 260, 541, 1.05, 40)
    return b
add('Universal Studios Florida', 'The backlot', 'Opened in 1990 as a working film studio as well as a theme park.', 'day', usf())

# Manchester Airport - Concorde
def man():
    b = cloud(80, 50, .9, '#eef2f6') + cloud(300, 70, .8, '#eef2f6')
    b += hills(200, '#7aa070', 551, 8) + R(260, 170, 120, 50, '#c9ced8') + windows(268, 180, 8, 1, 10, 14, 4, 0, '#7fb0d9')
    b += runway(236)
    x, y = 200, 216
    b += P(f'M{x-150} {y} Q{x-150} {y-8} {x-120} {y-9} L{x+110} {y-6} Q{x+150} {y-3} {x+165} {y+4} Q{x+140} {y+6} {x+110} {y+4} L{x-120} {y+6} Q{x-150} {y+6} {x-150} {y} Z', '#f4f4f4')
    b += P(f'M{x-100} {y+4} L{x+40} {y+4} L{x-60} {y+12} L{x-120} {y+10} Z', '#dfe3ea')
    b += P(f'M{x-130} {y-8} L{x-150} {y-46} L{x-136} {y-46} L{x-112} {y-8} Z', '#f4f4f4') + P(f'M{x-146} {y-40} L{x-138} {y-40} L{x-132} {y-26} L{x-140} {y-26} Z', '#1b3a8f')
    b += windows(x - 100, y - 5, 30, 1, 2.4, 2.4, 4.2, 0, '#2b4a7a')
    b += R(x - 60, y + 10, 4, 14, '#555') + R(x + 120, y + 4, 3, 20, '#555') + C(x - 58, y + 26, 3, '#222') + C(x + 121, y + 26, 3, '#222')
    b += crowd(12, 20, 380, 262, 552, 1.05, 30)
    return b
add('Manchester Airport', 'Concorde at MAN', 'Concorde G-BOAC lives at the Runway Visitor Park - and you can go on board.', 'grey', man())

# Dublin Airport - old terminal
def dub():
    b = cloud(90, 50, .9, '#eef2f6') + cloud(290, 60, .8, '#eef2f6')
    b += R(60, 150, 280, 70, '#f4f1ea') + P('M60 150 Q200 120 340 150 Z', '#e6e2d6')
    for k in range(4):
        b += R(70 + k * 0, 160 + k * 14, 260, 8, '#a3c4dc')
    b += R(180, 110, 40, 40, '#f4f1ea') + R(176, 104, 48, 8, '#e6e2d6') + R(184, 116, 32, 14, '#a3c4dc')
    b += R(0, 220, W, 18, '#a8adb5') + runway(236)
    b += plane(220, 238, 1.7, '#ffffff', '#2a8a46')
    return b
add('Dublin Airport', 'Dublin Airport', 'The original 1940s terminal is a listed art deco building, still in use.', 'grey', dub())

# Schiphol - tulips & plane
def ams():
    b = sun(70, 60, 13) + cloud(260, 50, .8)
    b += plane(260, 90, 1.4, '#ffffff', '#1d6fd8', True)
    b += R(0, 180, W, 20, '#7aa070')
    x = 330
    b += P(f'M{x-12} 190 L{x-8} 140 L{x+8} 140 L{x+12} 190 Z', '#8a6a4a') + P(f'M{x-10} 140 L{x} 128 L{x+10} 140 Z', '#5a3a2a')
    for a in (20, 110, 200, 290):
        ra = math.radians(a); b += L(x, 134, x + math.cos(ra) * 36, 134 + math.sin(ra) * 36, '#f4f1ea', 4)
    for i, c in enumerate(('#d22630', '#ffcd00', '#e84a7f', '#f07a14', '#7c3aed', '#ffffff', '#d22630')):
        y = 200 + i * 18
        b += P(f'M-10 {y} L410 {y} L410 {y+18} L-10 {y+18} Z', c) + R(-10, y + 14, 420, 4, '#4f8f50')
    return b
add('Amsterdam Schiphol', 'Schiphol', 'Built on a drained lake bed - about 3 metres below sea level.', 'day', ams())

# CDG - Terminal 1 camembert
def cdg():
    b = cloud(90, 50, .8, '#eef2f6') + cloud(300, 40, .7, '#eef2f6')
    b += E(200, 200, 160, 40, '#9a9a94') + R(40, 120, 320, 80, '#b5b4ad') + E(200, 120, 160, 30, '#c9c8c1') + E(200, 120, 70, 14, '#7a9a6a')
    for k in range(13): b += R(52 + k * 24, 130, 12, 64, '#8a8a84')
    for k in range(4): b += P(f'M{140+k*18} 122 L{150+k*18} 176 L{156+k*18} 176 L{146+k*18} 122 Z', '#cfe3f2', 'opacity=".8"')
    b += runway(236) + plane(110, 232, 1.2, '#ffffff', '#1d3a8f')
    return b
add('Paris Charles de Gaulle', 'Terminal 1 - "le camembert"', 'Opened in 1974 - those glass tube escalators still look like the future.', 'grey', cdg())

# Malaga airport
def agp():
    b = sun(320, 200, 22, '#ffd27a', '#ff9e5a') + cloud(100, 60, .7, '#ffe1c7')
    b += P('M-10 220 L60 150 L120 190 L190 130 L260 180 L330 140 L410 210 L410 240 L-10 240 Z', '#8a6a7a')
    b += plane(170, 110, 1.6, '#ffffff', '#f07a14')
    b += R(0, 220, W, 20, '#d8c8a8')
    b += palm(40, 250, 1.2, 4) + palm(80, 252, 1, -4) + palm(360, 250, 1.3, -6)
    b += runway(250)
    return b
add('Málaga Costa del Sol', 'Málaga airport', 'Opened in 1919 - one of the oldest airports in Spain still going.', 'sunset', agp())

# MCO
def mco():
    b = sun(70, 60, 13) + cloud(260, 40, .7)
    b += R(320, 60, 16, 170, '#e6e9ef') + R(312, 46, 32, 16, '#3f6f9a') + R(308, 42, 40, 5, '#c9ced8')
    b += R(0, 200, 300, 34, '#dfe3ea') + windows(10, 208, 14, 1, 14, 16, 6.4, 0, '#7fb0d9')
    b += palm(30, 240, 1.2, 4) + palm(280, 240, 1.1, -4) + palm(380, 240, 1.3, -6)
    b += runway(240)
    b += plane(200, 140, 1.5, '#ffffff', '#1d4ed8', True)
    return b
add('Orlando International', 'MCO', 'The code comes from McCoy Air Force Base - which is what the airport used to be.', 'tropic', mco())

# Narita airport
def nrt():
    b = sun(330, 60, 13) + cloud(110, 50, .8)
    b += R(0, 190, 280, 40, '#dfe3ea') + windows(10, 200, 13, 1, 14, 18, 6.4, 0, '#7fb0d9') + R(0, 186, 280, 6, '#c9ced8')
    b += tree(320, 236, 2, '#f2a6c0') + tree(370, 238, 1.8, '#e88aa8')
    b += runway(236)
    b += plane(190, 234, 1.7, '#ffffff', '#d22630')
    return b
add('Tokyo Narita', 'Narita', 'Opened in 1978, an hour out of Tokyo - leave plenty of time.', 'day', nrt())
