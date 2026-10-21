from snaplib import *
import random

S = {}
def add(city, title, note, sky, body, defs=''):
    slug = ''.join(ch for ch in city.lower() if ch.isalnum())
    S[city] = (title, note, scene(slug, sky, body, defs))
WIN = '#4a5878'

# Glasgow - Wellington statue with cone
def glasgow():
    st = '#d8c8a8'; dk = shade(st, -.16)
    b = cloud(90, 50, .9, '#eef2f6') + cloud(300, 40, .7, '#eef2f6')
    b += R(20, 90, 360, 160, st) + R(20, 84, 360, 8, dk) + P('M100 84 L200 56 L300 84 Z', st)
    for i in range(8): b += R(96 + i * 28, 92, 12, 158, '#ece2cc') + R(104 + i * 28, 92, 4, 158, dk)
    b += windows(30, 110, 2, 4, 14, 20, 12, 14, WIN) + windows(334, 110, 2, 4, 14, 20, 12, 14, WIN)
    x = 200
    b += R(x - 40, 210, 80, 50, '#7a7a7a') + R(x - 46, 204, 92, 8, '#8a8a8a')
    b += E(x, 186, 30, 14, '#3f4a4a') + P(f'M{x+24} 180 L{x+40} 156 L{x+46} 160 L{x+34} 186 Z', '#3f4a4a') + C(x + 44, 152, 6, '#3f4a4a')
    b += L(x - 20, 196, x - 26, 206, '#3f4a4a', 4) + L(x + 20, 196, x + 26, 206, '#3f4a4a', 4)
    b += R(x - 6, 150, 14, 30, '#3f4a4a') + C(x + 1, 142, 7, '#3f4a4a')
    b += P(f'M{x-6} 136 L{x+1} 112 L{x+8} 136 Z', '#f07a14') + R(x - 3, 122, 8, 3, '#ffffff') + R(x - 8, 134, 18, 3, '#f07a14')
    b += R(0, 260, W, 60, '#9e978a') + crowd(12, 20, 380, 270, 901, 1.05, 30)
    return b
add('Glasgow', 'The Duke with the cone', 'The Duke of Wellington statue has worn a traffic cone on and off since the 1980s.', 'grey', glasgow())

# Edinburgh - castle on the rock
def edinburgh():
    st = '#8a8478'; dk = shade(st, -.2)
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += P('M-10 260 L40 180 L120 150 L170 120 L300 118 L360 150 L410 200 L410 260 Z', '#6a6458') + P('M170 120 L300 118 L330 140 L200 150 Z', '#5a5448')
    b += R(150, 80, 200, 44, st) + battlements(150, 80, 200, st, 4, 6) + windows(162, 92, 12, 1, 8, 14, 7.6, 0, '#3a3a4a')
    b += R(170, 50, 50, 34, st) + battlements(170, 50, 50, st, 3, 6) + R(270, 60, 40, 24, '#b9a68a') + P('M266 60 L290 40 L314 60 Z', '#4b5a5a')
    b += R(194, 20, 2, 30, '#5a5a5a') + P('M196 20 L216 24 L196 28 Z', '#1d4ed8') + L(196, 21, 214, 27, '#fff', 1.2) + L(214, 21, 196, 27, '#fff', 1.2)
    b += tree(30, 266, 2, '#3f7f45') + tree(90, 270, 1.6, '#4f8f50') + tree(330, 268, 1.8, '#3f7f45')
    b += ground(262, '#5f9a50', '#7ab36a') + C(240, 76, 6, '#e8e8f0', 'opacity=".7"')
    return b
add('Edinburgh', 'Edinburgh Castle', 'The One O\'Clock Gun has been fired from the castle every day except Sunday since 1861.', 'day', edinburgh())

# Aberdeen - Marischal College
def aberdeen():
    g = '#c9ccd2'; dk = shade(g, -.18)
    b = cloud(90, 50, .9, '#eef2f6') + cloud(300, 40, .7, '#eef2f6')
    b += R(20, 110, 360, 140, g)
    for i in range(24):
        x = 24 + i * 15
        b += R(x, 96 - (i % 4 == 0) * 16, 6, 154 + (i % 4 == 0) * 16, dk) + spire(x + 3, 98 - (i % 4 == 0) * 16, 8, 16, dk)
    b += R(170, 40, 60, 210, g) + R(214, 40, 16, 210, dk) + windows(182, 60, 2, 6, 12, 20, 12, 8, WIN, arch=True)
    for px in (170, 230): b += spire(px, 42, 10, 30, dk)
    b += spire(200, 42, 22, 34, dk)
    b += R(0, 250, W, 70, '#9e9a92') + crowd(10, 20, 380, 262, 911, 1.05, 30)
    return b
add('Aberdeen', 'Marischal College', 'The second-biggest granite building in the world - Aberdeen is the Granite City.', 'grey', aberdeen())

# Dundee - RRS Discovery & V&A
def dundee():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += water(200, '#3f6f8a', 921, 16)
    b += P('M200 200 L230 120 L380 110 L400 200 Z', '#8a8478') + ''.join(L(200 + k * 6, 200, 232 + k * 6, 118 + (k % 3), '#a39d90', 2) for k in range(30))
    b += P('M20 210 L170 210 L156 236 L34 236 Z', '#1b1b1b') + R(26, 204, 140, 6, '#f4f1ea')
    for x, h in ((60, 130), (100, 150), (140, 120)):
        b += R(x, 206 - h, 3, h, '#5a3a22')
        for k in range(3): b += L(x - 20 + k * 2, 206 - h + 18 + k * 30, x + 23 - k * 2, 206 - h + 18 + k * 30, '#5a3a22', 1.4)
    b += R(98, 150, 8, 20, '#c9a227') + C(102, 146, 4, '#c9a227')
    b += L(170, 210, 140, 86, '#3b3b3b', .7) + P('M170 210 L190 200 L176 214 Z', '#1b1b1b')
    return b
add('Dundee', 'RRS Discovery & the V&A', 'Scott\'s Antarctic ship Discovery was built in Dundee in 1901 - and it\'s back home.', 'day', dundee())

# Belfast - Titanic Belfast & cranes
def belfast():
    b = sun(70, 60, 12) + cloud(280, 50, .8)
    for x in (260, 340):
        b += R(x - 10, 60, 8, 150, '#ffcd00') + R(x + 30, 60, 8, 150, '#ffcd00') + R(x - 16, 40, 60, 22, '#ffcd00') + T(x + 14, 56, 'H&W', 12, '#1b1b1b')
    b += P('M60 210 L80 110 L130 100 L150 140 L170 100 L220 110 L240 210 Z', '#c9ced8') + P('M80 110 L130 100 L150 140 L120 150 Z', '#a3aab5') + P('M170 100 L220 110 L240 210 L190 150 Z', '#e1e5eb')
    for k in range(6): b += L(70 + k * 6, 200 - k * 18, 230 - k * 6, 200 - k * 18, '#ffffff', .8, 'opacity=".5"')
    b += water(210, '#3f5f7f', 931, 14) + R(0, 206, W, 6, '#8a8475')
    return b
add('Belfast', 'Titanic Belfast', 'Titanic was built right here - under Harland & Wolff\'s yellow cranes, Samson and Goliath.', 'day', belfast())

# Cardiff - Principality Stadium
def cardiff():
    b = sun(70, 50, 12) + cloud(260, 40, .8)
    b += P('M30 230 L50 130 L350 130 L370 230 Z', '#e6e9ef') + R(40, 124, 320, 8, '#b9c0cc')
    for x in (50, 130, 270, 350):
        b += L(x, 40, x, 140, '#d22630', 4) + L(x, 40, x - 20, 130, '#c9ced8', 1.2) + L(x, 40, x + 20, 130, '#c9ced8', 1.2)
    b += windows(60, 146, 13, 2, 16, 16, 7, 10, '#7fa8c8') + T(200, 214, 'CAERDYDD', 12, '#d22630', 'letter-spacing="4"')
    b += water(232, '#4f6f8a', 941, 10) + R(0, 270, W, 50, '#9e978a')
    b += crowd(30, 10, 390, 276, 942, 1.05, 30, ['#d22630', '#d22630', '#ffffff', '#2a8a46'])
    return b
add('Cardiff', 'The Principality Stadium', 'Opened in 1999 - the first stadium in the UK with a retractable roof.', 'day', cardiff())

# Swansea - Mumbles pier & lighthouse
def swansea():
    b = sun(320, 70, 15, '#ffe0a0', '#ffb36b') + cloud(90, 50, .8, '#ffe8d6')
    b += water(150, '#3f86b5', 951, 18)
    b += P('M200 160 Q260 120 320 130 Q360 140 380 160 Z', '#6f7a5a') + R(330, 108, 12, 30, '#f4f1ea') + R(328, 102, 16, 8, '#ffe27a') + P('M328 102 L336 94 L344 102 Z', '#2a2a2a')
    b += P('M-10 180 Q100 150 180 168 L180 200 L-10 200 Z', '#7a8a5a')
    b += R(40, 170, 180, 6, '#6b4a3a') + ''.join(L(44 + k * 16, 176, 44 + k * 16, 200, '#5a3a2a', 2) for k in range(12)) + R(200, 160, 30, 12, '#e6e9ef') + P('M198 160 L215 152 L232 160 Z', '#2b4a6a')
    b += P('M-10 220 Q200 206 410 216 L410 320 L-10 320 Z', '#ecd9a8')
    b += crowd(10, 30, 380, 236, 952, 1.05, 50)
    return b
add('Swansea', 'Mumbles', 'The Swansea and Mumbles Railway carried the world\'s first fare-paying railway passengers in 1807.', 'warm', swansea())
