from snaplib import *
from snaps4 import castle
import random

S = {}
def add(city, title, note, sky, body, defs=''):
    slug = ''.join(ch for ch in city.lower() if ch.isalnum())
    S[city] = (title, note, scene(slug, sky, body, defs))
WIN = '#4a5878'

def townhall(st, sky_extra='', tower='clock', dome='#6f8f7f', crowd_seed=1):
    dk = shade(st, -.18)
    b = sky_extra
    b += R(20, 140, 360, 100, st) + R(20, 134, 360, 8, dk) + windows(32, 152, 16, 2, 10, 24, 11.8, 14, WIN, arch=True)
    for i in range(6): b += R(150 + i * 18, 150, 8, 90, shade(st, .2)) + R(155 + i * 18, 150, 3, 90, dk)
    b += P('M140 134 L200 112 L260 134 Z', st)
    x = 176
    b += R(x, 48, 48, 86, st) + R(x + 36, 48, 12, 86, dk) + clockface(x + 24, 74, 11)
    if tower == 'dome':
        b += P(f'M{x-2} 48 Q{x+24} 10 {x+50} 48 Z', dome) + R(x + 23, 4, 2, 10, '#c9a227')
    else:
        b += R(x + 4, 30, 40, 18, st) + windows(x + 8, 33, 4, 1, 6, 12, 3.4, 0, WIN, arch=True) + P(f'M{x+2} 30 L{x+24} 4 L{x+46} 30 Z', dome)
    b += R(0, 240, W, 80, '#aaa294') + R(0, 240, W, 3, '#c3bba9')
    b += crowd(12, 30, 370, 256, crowd_seed, 1.05, 40)
    return b

# Bolton - Town Hall with lions
def bolton():
    b = townhall('#d6c39f', sun(330, 50, 12) + cloud(90, 50, .8), 'dome', '#6f8f7f', 801)
    for x in (150, 240): b += R(x - 4, 236, 18, 6, '#9a9284') + E(x + 5, 228, 9, 6, '#c9c0ad') + C(x + 12, 222, 5, '#c9c0ad')
    return b
add('Bolton', 'Bolton Town Hall', 'Opened in 1873 - a pair of stone lions guard the steps.', 'day', bolton())

# Warrington - Golden Gates
def warrington():
    b = sun(330, 50, 12) + cloud(90, 50, .8)
    b += R(80, 100, 240, 120, '#b58a6a') + windows(96, 116, 9, 3, 14, 18, 10.5, 12, WIN) + P('M76 100 L200 70 L324 100 Z', '#8a5a44')
    b += ground(220, '#5f8f55', '#79a86b')
    gold = '#d9b23a'
    b += R(40, 150, 320, 6, gold) + R(40, 240, 320, 6, gold)
    for i in range(33): b += R(42 + i * 9.8, 150, 2, 92, gold)
    for x in (40, 120, 280, 352): b += R(x - 4, 140, 12, 106, gold) + C(x + 2, 136, 6, gold)
    b += PL('M120 150 Q200 110 280 150', gold, 4) + C(200, 128, 10, 'none', f'stroke="{gold}" stroke-width="3"')
    for k in range(6): b += PL(f'M{150+k*20} 160 q10 -10 0 -20', gold, 1.5)
    b += R(0, 246, W, 74, '#aaa294')
    b += crowd(8, 20, 380, 262, 811, 1.05, 30)
    return b
add('Warrington', 'The Golden Gates', 'Made for the 1862 International Exhibition in London, then given to the town.', 'day', warrington())

# Stockport - viaduct
def stockport():
    br = '#a8503a'; dk = shade(br, -.2)
    b = sun(70, 50, 12) + cloud(260, 40, .8)
    b += R(0, 80, W, 16, br) + R(0, 76, W, 5, dk)
    for i in range(9):
        x = -10 + i * 48
        b += R(x, 96, 14, 170, br) + R(x + 10, 96, 4, 170, dk) + P(f'M{x+14} 96 L{x+14} 112 A17 17 0 0 1 {x+48} 112 L{x+48} 96 Z', br)
    b += R(0, 160, W, 6, br, ex='opacity=".0"')
    b += ''.join(R(x, 180 + (i % 3) * 8, 40, 80, c) + windows(x + 6, 190 + (i % 3) * 8, 3, 3, 6, 8, 6, 8, WIN) for i, (x, c) in enumerate(((20, '#c4a27a'), (90, '#d8c8a8'), (230, '#b98b6a'), (310, '#e3d6be'))))
    b += R(0, 262, W, 58, '#8a8475')
    b += R(80, 60, 200, 16, '#5a2a6a', 3) + windows(86, 63, 12, 1, 10, 6, 6, 0, '#cfe3f2')
    return b
add('Stockport', 'Stockport Viaduct', 'Built in 1840 with around 11 million bricks - once the biggest brick structure in the world.', 'day', stockport())

# Oldham - old town hall
def oldham():
    st = '#d8c49c'; dk = shade(st, -.18)
    b = cloud(90, 50, .9, '#eef2f6') + cloud(300, 40, .7, '#eef2f6')
    b += R(60, 110, 280, 130, st) + R(60, 104, 280, 8, dk)
    b += P('M120 104 L200 70 L280 104 Z', st) + P('M130 102 L200 76 L270 102 Z', dk)
    for i in range(6): b += R(128 + i * 26, 112, 12, 128, '#ece0c4') + R(136 + i * 26, 112, 4, 128, dk)
    b += windows(70, 124, 2, 3, 12, 20, 10, 16, WIN) + windows(298, 124, 2, 3, 12, 20, 10, 16, WIN)
    b += R(130, 200, 140, 16, '#2b3a55') + T(200, 212, 'CINEMA', 12, '#ffcd00', 'letter-spacing="3"')
    b += R(0, 240, W, 80, '#a49b8a') + crowd(10, 30, 370, 254, 821, 1.05, 40)
    return b
add('Oldham', 'The Old Town Hall', 'The 1841 classical front survived - and now there\'s a cinema behind it.', 'grey', oldham())

# Rochdale - Gothic town hall
def rochdale():
    st = '#c9b48f'; dk = shade(st, -.2)
    b = sun(330, 50, 12) + cloud(90, 50, .8)
    b += R(20, 140, 360, 100, st) + P('M20 140 L200 110 L380 140 Z', '#5a6a6a') + windows(32, 156, 15, 2, 10, 26, 13, 14, WIN, arch=True)
    for x in range(30, 380, 40): b += spire(x, 142, 6, 16, st)
    x = 220
    b += R(x, 40, 40, 100, st) + R(x + 30, 40, 10, 100, dk) + clockface(x + 20, 70, 11) + spire(x + 20, 42, 44, 40, '#5a6a6a')
    for px in (x, x + 40): b += spire(px, 44, 6, 18, st)
    b += R(0, 240, W, 80, '#aaa294') + ground(240, '#5f8f55', '#79a86b') + R(0, 270, W, 50, '#aaa294')
    b += flowers(0, 400, 244, 831, 30)
    b += crowd(10, 30, 370, 274, 832, 1.05, 30)
    return b
add('Rochdale', 'Rochdale Town Hall', 'Gothic, from 1871 - legend says Hitler wanted to ship it to Germany.', 'day', rochdale())

# Wigan - Wigan Pier
def wigan():
    br = '#a8503a'
    b = sun(330, 50, 12) + cloud(90, 50, .8)
    b += R(200, 60, 180, 150, br) + windows(212, 72, 8, 6, 12, 14, 8.6, 8, WIN) + R(330, 20, 20, 50, br) + T(290, 66, 'TRENCHERFIELD MILL', 8, '#f4f1ea', 'textLength="150" lengthAdjust="spacingAndGlyphs"')
    b += R(0, 200, W, 12, '#8a8475')
    b += water(212, '#3f5f6a', 841, 12)
    b += P('M40 250 L180 250 L174 262 L46 262 Z', '#2a6b3a') + R(52, 240, 110, 10, '#d22630') + R(56, 242, 102, 6, '#ffcd00') + windows(60, 242, 8, 1, 6, 5, 6, 0, '#2a2a2a')
    b += R(0, 212, 30, 108, '#8a8475') + R(10, 170, 6, 40, '#2a2a2a') + R(6, 166, 30, 6, '#2a2a2a') + T(80, 192, 'WIGAN PIER', 12, '#1b1b1b', 'letter-spacing="2"')
    return b
add('Wigan', 'Wigan Pier', 'Made famous by George Orwell\'s The Road to Wigan Pier in 1937.', 'day', wigan())

# Salford - The Lowry & Quays
def salford():
    b = sun(70, 50, 12) + cloud(260, 40, .8)
    b += R(260, 90, 100, 120, '#c9ced8') + windows(268, 100, 6, 7, 10, 10, 5, 4, '#7fa8c8')
    b += P('M60 210 L80 120 L180 110 L220 140 L230 210 Z', '#c0c4cc') + P('M80 120 L180 110 L200 70 L110 80 Z', '#e6a23a') + R(120, 150, 70, 40, '#7fa8c8')
    b += T(150, 106, 'THE LOWRY', 10, '#1b1b1b', 'letter-spacing="2"')
    b += water(210, '#3f6f8f', 851, 16)
    b += PL('M40 230 Q200 190 360 230', '#f4f1ea', 3)
    b += crowd(8, 140, 260, 214, 852, .8, 6)
    return b
add('Salford', 'The Lowry at Salford Quays', 'Named after L.S. Lowry - the painter of the "matchstick men".', 'day', salford())

# Carlisle - castle
def carlisle():
    st = '#b8806a'; dk = shade(st, -.2)
    b = sun(330, 50, 12) + cloud(90, 50, .8)
    b += hills(200, '#7aa070', 861, 10) + R(30, 160, 340, 70, st) + battlements(30, 160, 340, st, 4, 7)
    b += R(150, 80, 100, 150, st) + R(230, 80, 20, 150, dk) + battlements(150, 80, 100, st, 4, 8) + windows(166, 100, 3, 3, 12, 16, 16, 14, WIN, arch=True)
    b += R(40, 140, 40, 90, st) + battlements(40, 140, 40, st, 3, 6) + R(320, 140, 40, 90, st) + battlements(320, 140, 40, st, 3, 6)
    b += arch_win(60, 196, 24, 34, '#3b2a1a')
    b += ground(230, '#5f8f55', '#79a86b') + tree(20, 236, 1.6) + tree(385, 238, 1.6)
    return b
add('Carlisle', 'Carlisle Castle', 'From 1916 to 1973, the government owned and ran almost every pub in Carlisle.', 'day', carlisle())

# Blackburn - cathedral
def blackburn():
    st = '#d8c8a8'; dk = shade(st, -.18)
    b = sun(330, 50, 12) + cloud(90, 50, .8)
    b += R(40, 150, 320, 90, st) + P('M40 150 L200 126 L360 150 Z', '#5a6a6a') + windows(54, 166, 10, 1, 12, 40, 18, 0, WIN, arch=True)
    b += R(160, 60, 80, 90, st) + R(222, 60, 18, 90, dk) + windows(172, 78, 4, 1, 8, 54, 7, 0, WIN, arch=True)
    b += P('M160 60 L200 40 L240 60 Z', st) + R(196, 10, 8, 32, '#c9a227') + C(200, 10, 4, '#c9a227')
    b += ground(240, '#5f8f55', '#79a86b') + R(0, 266, W, 54, '#aaa294')
    b += tree(30, 246, 1.5) + tree(370, 246, 1.5) + crowd(8, 60, 340, 278, 871, 1.05, 30)
    return b
add('Blackburn', 'Blackburn Cathedral', 'The Beatles sang about the 4,000 holes in Blackburn, Lancashire.', 'day', blackburn())

# Burnley - Weavers' Triangle
def burnley():
    br = '#9a4a34'
    b = cloud(90, 50, .9, '#eef2f6') + cloud(300, 40, .7, '#eef2f6')
    b += hills(130, '#7a9a6a', 881, 14)
    for x, w, h in ((20, 140, 110), (180, 110, 90), (300, 100, 120)):
        b += R(x, 220 - h, w, h, br) + windows(x + 8, 230 - h, int(w / 18), int(h / 22), 10, 12, 8, 10, WIN)
    b += R(150, 40, 16, 140, br) + R(146, 36, 24, 6, shade(br, -.2))
    b += R(0, 220, W, 10, '#8a8475') + water(230, '#3f5f6a', 882, 10)
    b += P('M200 268 L330 268 L324 280 L206 280 Z', '#1d4ed8') + R(214, 258, 100, 10, '#7a1f3d') + windows(220, 260, 8, 1, 6, 5, 6, 0, '#cfe3f2')
    return b
add('Burnley', 'The Weavers\' Triangle', 'Burnley was once the biggest producer of cotton cloth in the world.', 'grey', burnley())

# Preston - Harris Museum
def preston():
    st = '#e1d3b4'; dk = shade(st, -.16)
    b = sun(330, 50, 12) + cloud(90, 50, .8)
    b += R(60, 110, 280, 130, st) + R(60, 104, 280, 8, dk) + P('M110 104 L200 70 L290 104 Z', st) + P('M120 102 L200 76 L280 102 Z', dk)
    for i in range(6): b += R(118 + i * 30, 112, 12, 128, '#efe4cc') + R(126 + i * 30, 112, 4, 128, dk)
    b += R(170, 40, 60, 34, st) + windows(176, 46, 4, 1, 8, 20, 6, 0, WIN, arch=True) + P('M168 40 Q200 14 232 40 Z', dk)
    b += R(0, 240, W, 80, '#aaa294') + crowd(12, 30, 370, 254, 891, 1.05, 40)
    return b
add('Preston', 'The Harris Museum', 'Preston Guild is held only once every 20 years - hence "once every Preston Guild".', 'day', preston())

# Lancaster - Ashton Memorial
def lancaster():
    st = '#efe8da'; dk = shade(st, -.14)
    b = sun(70, 50, 12) + cloud(280, 50, .8)
    b += tree(30, 240, 2.4, '#3f7f45') + tree(370, 240, 2.6, '#3f7f45') + tree(80, 246, 1.8, '#4f8f50') + tree(320, 246, 1.8, '#4f8f50')
    b += R(110, 150, 180, 70, st) + R(100, 214, 200, 10, dk) + R(90, 224, 220, 10, st)
    for i in range(6): b += R(120 + i * 30, 150, 10, 64, '#f8f4ea') + R(127 + i * 30, 150, 3, 64, dk)
    b += R(150, 110, 100, 40, st) + windows(160, 118, 5, 1, 10, 24, 8, 0, WIN, arch=True)
    b += P('M150 112 Q200 40 250 112 Z', '#7aa89a') + P('M200 112 Q200 46 250 112 Z', '#6a988a') + R(194, 44, 12, 16, st) + C(200, 42, 5, '#7aa89a')
    for x in (110, 290): b += R(x - 10, 130, 20, 20, st) + P(f'M{x-12} 130 Q{x} 112 {x+12} 130 Z', '#7aa89a')
    b += ground(234, '#5f9a50', '#7ab36a') + flowers(0, 400, 238, 901, 30)
    return b
add('Lancaster', 'The Ashton Memorial', 'Built 1907-09 in Williamson Park - they call it the Taj Mahal of the North.', 'day', lancaster())

# Chester - Eastgate Clock
def chester():
    st = '#c9a87e'
    b = sun(330, 50, 12) + cloud(90, 50, .8)
    for i, x in enumerate(range(-10, 410, 70)):
        if 140 < x < 260: continue
        b += R(x, 100, 66, 140, '#f4f1ea') + ''.join(R(x + k * 14, 100, 3, 140, '#2a2a2a') for k in range(5)) + R(x, 140, 66, 3, '#2a2a2a') + R(x, 180, 66, 3, '#2a2a2a') + P(f'M{x-2} 100 L{x+33} 76 L{x+68} 100 Z', '#4b3d3a')
    b += R(130, 170, 140, 50, st) + arch_win(170, 176, 60, 44, '#3b4a5a') + R(126, 162, 148, 10, shade(st, -.2))
    b += R(196, 70, 8, 92, '#2a3a6a') + ''.join(PL(f'M{196-k*4} {150-k*20} L{204+k*4} {130-k*20}', '#2a3a6a', 1.2) for k in range(3))
    b += C(200, 74, 18, '#2a3a6a') + clockface(200, 74, 14, '#f4f1ea', '#1b1b1b', (11, 50)) + P('M190 56 Q200 30 210 56 Z', '#2a3a6a') + R(199, 26, 2, 8, '#c9a227')
    b += R(0, 240, W, 80, '#aaa294') + crowd(14, 20, 380, 252, 911, 1.05, 40)
    return b
add('Chester', 'The Eastgate Clock', 'Added for Queen Victoria\'s Diamond Jubilee in 1897 - reckoned the second most photographed clock in England.', 'day', chester())

# Crewe - railway
def crewe():
    b = sun(330, 50, 12) + cloud(90, 50, .8)
    b += R(0, 170, W, 60, '#b58a6a') + R(0, 160, W, 12, '#8a8f99') + ''.join(R(10 + k * 30, 180, 14, 20, WIN) for k in range(13))
    b += R(0, 230, W, 90, '#6b6f7a') + ''.join(L(0, 250 + k * 24, W, 250 + k * 24, '#c9ced8', 2) for k in range(3))
    b += R(40, 226, 240, 24, '#ffcd00', 4) + R(40, 226, 30, 24, '#1b1b1b', 4) + windows(80, 230, 9, 1, 14, 9, 8, 0, '#2b3a55') + R(40, 244, 240, 4, '#2b4a8a')
    b += R(300, 140, 4, 90, '#3b3b3b') + R(296, 140, 12, 24, '#1b1b1b') + C(302, 146, 3, '#2aff6a')
    b += T(200, 154, 'CREWE', 18, '#1b1b1b', 'letter-spacing="6"')
    return b
add('Crewe', 'Crewe station', 'Crewe grew up around the railway works, which opened in 1843.', 'day', crewe())

# Macclesfield - silk mill
def macclesfield():
    br = '#a8503a'
    b = sun(330, 50, 12) + cloud(90, 50, .8)
    b += hills(150, '#7a9a6a', 921, 14)
    b += R(60, 90, 280, 150, br) + windows(74, 102, 11, 6, 14, 14, 9.6, 8, '#cfe3f2') + P('M56 90 L200 66 L344 90 Z', '#5b4a44')
    b += R(300, 40, 16, 60, br)
    b += R(0, 240, W, 80, '#aaa294')
    for i, c in enumerate(('#d22630', '#7c3aed', '#ffcd00', '#2a8a46', '#1d4ed8', '#e84a7f')):
        b += P(f'M{40+i*56} 270 Q{60+i*56} 250 {80+i*56} 270 L{80+i*56} 300 L{40+i*56} 300 Z', c, 'opacity=".9"')
    return b
add('Macclesfield', 'The silk mills', 'Macclesfield was once the silk capital of the world - Paradise Mill still has its looms.', 'day', macclesfield())

# St Helens - glass cone
def sthelens():
    br = '#a8503a'
    b = sun(70, 50, 12) + cloud(280, 50, .8)
    b += P('M150 240 L176 80 Q200 64 224 80 L250 240 Z', br) + P('M200 240 L200 70 Q212 72 224 80 L250 240 Z', shade(br, -.2))
    b += arch_win(186, 196, 28, 44, '#ffb84a')
    b += R(250, 150, 120, 90, '#c9ced8') + R(250, 144, 120, 8, '#9aa3b0') + windows(260, 160, 6, 3, 12, 14, 7, 10, '#7fb0d9')
    b += R(20, 170, 110, 70, '#7fb0d9') + ''.join(L(20 + k * 22, 170, 20 + k * 22, 240, '#c9e3f2', 1.5) for k in range(6))
    b += water(240, '#3f6f8a', 931, 10) + R(0, 270, W, 50, '#aaa294')
    b += crowd(8, 30, 370, 278, 932, 1.05, 30)
    return b
add('St Helens', 'The World of Glass', 'Pilkington glass made St Helens famous - the museum has a Victorian glass cone.', 'day', sthelens())

# Widnes - Silver Jubilee Bridge
def widnes():
    b = sun(320, 210, 20, '#ffd27a', '#ff9e5a') + cloud(90, 60, .8, '#ffe1c7')
    b += water(200, '#4f6f8a', 941, 18)
    b += PL('M30 200 Q200 30 370 200', '#d9dce2', 9) + PL('M30 200 Q200 48 370 200', '#b9bdc6', 3)
    for k in range(1, 16):
        t = k / 16; px = (1 - t) ** 2 * 30 + 2 * (1 - t) * t * 200 + t * t * 370; py = (1 - t) ** 2 * 200 + 2 * (1 - t) * t * 30 + t * t * 200
        if py < 156: b += L(px, py, px, 156, '#d9dce2', 1.4)
    b += R(-10, 152, 420, 8, '#d9dce2')
    b += R(0, 196, 40, 20, '#8a8475') + R(360, 196, 40, 20, '#8a8475')
    return b
add('Widnes', 'The Silver Jubilee Bridge', 'Paul Simon is said to have written Homeward Bound on Widnes station.', 'sunset', widnes())

# Birkenhead - Mersey ferry
def birkenhead():
    b = sun(330, 50, 12) + cloud(90, 50, .8)
    st = '#c9c3b6'
    b += R(40, 120, 120, 90, st) + windows(48, 130, 8, 5, 8, 8, 6, 6, WIN)
    for x in (52, 128): b += R(x, 90, 20, 32, st) + clockface(x + 10, 102, 6) + P(f'M{x} 90 Q{x+10} 76 {x+20} 90 Z', '#4f8f7f')
    b += R(170, 150, 60, 60, '#d8d2c4') + R(240, 110, 40, 100, '#9aa3b0') + R(290, 140, 90, 70, '#b9bdc6')
    b += water(210, '#4f6f8a', 951, 16)
    b += P('M90 262 L290 262 L276 284 L104 284 Z', '#1b1b1b') + R(110, 246, 170, 16, '#f4f1ea') + windows(116, 249, 12, 1, 9, 6, 4.6, 0, '#2b3a55')
    b += R(170, 232, 40, 14, '#ffcd00') + R(180, 220, 12, 12, '#1b1b1b') + ''.join(R(110 + k * 34, 262, 18, 5, ['#d22630', '#ffcd00', '#1d4ed8', '#2a8a46', '#e84a7f'][k]) for k in range(5))
    return b
add('Birkenhead', 'Ferry across the Mersey', 'Birkenhead Park (1847) inspired the design of New York\'s Central Park.', 'day', birkenhead())

# Southport - pier
def southport():
    b = sun(320, 70, 15, '#ffe0a0', '#ffb36b') + cloud(90, 50, .8, '#ffe8d6')
    b += water(150, '#4f8ab5', 961, 14) + P('M-10 196 Q200 180 410 192 L410 320 L-10 320 Z', '#ecd9a8')
    b += P('M0 200 L400 120 L400 126 L0 208 Z', '#6b4a3a')
    for k in range(20): x = k * 20; b += L(x, 204 - x * .2, x, 230 - x * .2, '#5a3a2a', 2)
    b += P('M330 126 L398 112 L398 120 L330 134 Z', '#1d4ed8') + R(352, 104, 30, 12, '#f4f1ea')
    b += R(100, 166, 30, 10, '#d22630', 2) + windows(103, 168, 4, 1, 5, 4, 2, 0, '#cfe3f2')
    b += crowd(12, 40, 380, 250, 962, 1.05, 50)
    return b
add('Southport', 'Southport Pier', 'Opened in 1860 - the second-longest pier in Britain.', 'warm', southport())

# Blackpool - Tower
def blackpool():
    b = sun(320, 210, 20, '#ffd27a', '#ff9e5a') + cloud(90, 60, .8, '#ffe1c7')
    b += water(210, '#3f6f9a', 971, 14)
    x = 200; red = '#c0392b'
    b += P(f'M{x-40} 210 L{x-8} 30 L{x+8} 30 L{x+40} 210 L{x+28} 210 L{x+4} 50 L{x-4} 50 L{x-28} 210 Z', red)
    for y in range(60, 200, 18):
        hw = 6 + (y - 30) * .19
        b += L(x - hw, y, x + hw, y + 18, red, 1.4) + L(x + hw, y, x - hw, y + 18, red, 1.4)
    b += R(x - 12, 22, 24, 10, red) + R(x - 2, 4, 4, 18, red) + C(x, 4, 3, '#ffcd00')
    b += R(80, 180, 240, 50, '#d8b48a') + windows(92, 188, 12, 2, 12, 14, 6.6, 6, '#3a4a6a') + R(80, 174, 240, 6, '#b08a5a')
    b += R(0, 230, W, 14, '#8a8f99') + ''.join(C(10 + k * 24, 236, 3, ['#ffcd00', '#ff4d4d', '#4dd2ff', '#7dff7a'][k % 4]) for k in range(17))
    b += P('M-10 244 L410 244 L410 320 L-10 320 Z', '#ecd9a8') + crowd(14, 20, 380, 258, 972, 1.05, 40)
    return b
add('Blackpool', 'Blackpool Tower', 'Opened in 1894, inspired by the Eiffel Tower - 158 metres to the flagpole.', 'sunset', blackpool())
