from snaplib import *
import random

S = {}
def add(city, title, note, sky, body, defs=''):
    slug = ''.join(ch for ch in city.lower() if ch.isalnum())
    S[city] = (title, note, scene(slug, sky, body, defs))

WIN = '#4a5878'

# Bradford - City Hall & Mirror Pool
def bradford():
    st = '#c9b48f'; dk = shade(st, -.2)
    b = sun(330, 50, 12) + cloud(90, 50, .8) + cloud(240, 40, .5)
    b += R(20, 140, 360, 96, st) + R(20, 134, 360, 8, dk) + windows(32, 150, 16, 2, 10, 22, 11.8, 14, WIN, arch=True)
    b += battlements(20, 134, 360, st, 4, 5)
    x = 180
    b += R(x, 50, 40, 90, st) + R(x + 30, 50, 10, 90, dk) + clockface(x + 20, 76, 11) + R(x - 6, 40, 52, 10, st) + battlements(x - 6, 40, 52, st, 3, 6)
    b += R(x + 8, 18, 24, 22, st) + P(f'M{x+6} 18 L{x+20} 0 L{x+34} 18 Z', '#5a6a6a')
    b += R(0, 236, W, 84, '#bdb6a8') + E(200, 278, 170, 26, '#8fc0e0') + E(200, 278, 170, 26, 'none', 'stroke="#d8d2c4" stroke-width="3"')
    for k in range(9): b += PL(f'M{60+k*35} 280 q0 -18 2 -26', '#e6f6ff', 2, 'opacity=".8"')
    b += crowd(10, 30, 370, 300, 601, 1.05, 14)
    return b
add('Bradford', 'City Hall & the Mirror Pool', 'City Park\'s Mirror Pool is the biggest urban water feature in the UK.', 'day', bradford())

# Hull - Humber Bridge
def hull():
    b = sun(320, 200, 20, '#ffd27a', '#ff9e5a') + cloud(90, 60, .8, '#ffe1c7')
    b += water(200, '#4f6f8a', 611, 18)
    b += hills(196, '#5f7f55', 612, 6, 6, base=206)
    for x in (70, 330):
        b += R(x - 6, 50, 4, 170, '#cfd5de') + R(x + 2, 50, 4, 170, '#cfd5de') + R(x - 6, 70, 12, 3, '#cfd5de') + R(x - 6, 130, 12, 3, '#cfd5de') + R(x - 6, 190, 12, 3, '#cfd5de')
    b += PL('M70 52 Q200 176 330 52', '#cfd5de', 2.4) + PL('M-20 150 Q20 120 70 52', '#cfd5de', 2) + PL('M330 52 Q380 120 420 150', '#cfd5de', 2)
    for k in range(1, 26):
        t = k / 26; px = 70 + 260 * t; py = (1 - t) ** 2 * 52 + 2 * (1 - t) * t * 176 + t * t * 52
        b += L(px, py, px, 178, '#cfd5de', .6)
    b += R(-10, 178, 420, 6, '#e6e9ef')
    b += boat(140, 260, 1.6, '#c0392b', '#f4f1ea')
    return b
add('Hull', 'The Humber Bridge', 'The longest single-span suspension bridge in the world when it opened in 1981.', 'sunset', hull())

# Rotherham - Chapel on the Bridge
def rotherham():
    st = '#b9a07a'; dk = shade(st, -.2)
    b = sun(70, 60, 13) + cloud(260, 50, .8)
    b += R(0, 150, W, 70, '#a39b8c')
    b += P('M0 200 L400 200 L400 214 L0 214 Z', st)
    for i in range(4):
        x = 10 + i * 100
        b += P(f'M{x} 250 L{x} 222 A40 26 0 0 1 {x+80} 222 L{x+80} 250 Z', '#3b5a5a')
    b += P('M0 214 L400 214 L400 250 L0 250 Z', st, 'fill-opacity="0"')
    d = 'M0 214 L0 250 L10 250 L10 222 A40 26 0 0 1 90 222 L90 250 L110 250 L110 222 A40 26 0 0 1 190 222 L190 250 L210 250 L210 222 A40 26 0 0 1 290 222 L290 250 L310 250 L310 222 A40 26 0 0 1 390 222 L390 250 L400 250 L400 214 Z'
    b += P(d, st)
    b += R(150, 130, 100, 70, st) + R(230, 130, 20, 70, dk) + battlements(150, 130, 100, st, 4, 6)
    b += arch_win(166, 146, 22, 38, WIN) + arch_win(212, 146, 22, 38, WIN) + arch_win(190, 150, 20, 34, WIN)
    for px in (152, 246): b += R(px - 2, 116, 4, 16, st)
    b += water(250, '#4f7a7a', 621, 14)
    return b
add('Rotherham', 'The Chapel on the Bridge', 'One of only four medieval bridge chapels left in England.', 'day', rotherham())

# Doncaster - racecourse
def doncaster():
    b = sun(330, 50, 13) + cloud(90, 50, .8) + cloud(230, 40, .5)
    b += R(40, 110, 320, 90, '#e6e9ef') + P('M30 110 L370 110 L380 96 L20 96 Z', '#b9c0cc')
    b += windows(50, 120, 14, 2, 16, 18, 6.4, 10, '#7fa8c8') + R(40, 166, 320, 34, '#4f6f9a')
    b += crowd(30, 50, 350, 196, 631, .8, 4)
    b += R(0, 200, W, 12, '#f4f1ea') + ''.join(R(i * 20, 200, 2, 12, '#c9ced8') for i in range(21))
    b += ground(212, '#4f9a45', '#6ab35a')
    for i, (x, c) in enumerate(((90, '#d22630'), (160, '#ffcd00'), (230, '#1d4ed8'), (300, '#2a8a46'))):
        y = 250 + (i % 2) * 14
        b += E(x, y, 20, 9, '#6b3a1a') + P(f'M{x+14} {y-4} L{x+28} {y-18} L{x+32} {y-14} L{x+22} {y} Z', '#6b3a1a') + C(x + 30, y - 16, 4, '#6b3a1a')
        b += L(x - 14, y + 6, x - 22, y + 20, '#6b3a1a', 3) + L(x - 8, y + 6, x - 2, y + 20, '#6b3a1a', 3) + L(x + 12, y + 6, x + 22, y + 20, '#6b3a1a', 3) + L(x + 6, y + 6, x + 2, y + 20, '#6b3a1a', 3)
        b += R(x - 4, y - 18, 8, 9, c, 2) + C(x, y - 21, 3, c)
    return b
add('Doncaster', 'Doncaster Racecourse', 'Home of the St Leger - the oldest of the five classics, first run in 1776.', 'day', doncaster())

# Barnsley - Town Hall
def barnsley():
    st = '#ece6d6'; dk = shade(st, -.14)
    b = sun(330, 50, 13) + cloud(90, 50, .8)
    b += R(30, 130, 340, 110, st) + R(30, 124, 340, 8, dk) + windows(42, 142, 14, 3, 12, 18, 11.5, 12, WIN)
    for i in range(6): b += R(150 + i * 18, 150, 8, 90, '#f6f2e8') + R(155 + i * 18, 150, 3, 90, dk)
    x = 172
    b += R(x, 40, 56, 90, st) + R(x + 44, 40, 12, 90, dk) + clockface(x + 28, 66, 12) + windows(x + 12, 90, 2, 1, 10, 26, 12, 0, WIN, arch=True)
    b += R(x + 6, 24, 44, 16, st) + windows(x + 10, 27, 4, 1, 6, 10, 4, 0, WIN) + R(x + 12, 12, 32, 12, dk) + R(x + 26, 0, 4, 12, '#c9a227')
    b += R(0, 240, W, 80, '#a9a294') + R(0, 240, W, 3, '#c3bca9')
    b += tree(20, 244, 1.5) + tree(380, 244, 1.5)
    b += crowd(10, 50, 350, 258, 641, 1.05, 40)
    return b
add('Barnsley', 'Barnsley Town Hall', 'Opened in 1933 in white Portland stone - the Experience Barnsley museum is inside.', 'day', barnsley())

# Grimsby - Dock Tower
def grimsby():
    br = '#a8503a'; dk = shade(br, -.2)
    b = cloud(90, 60, .9, '#eef2f6') + cloud(300, 50, .7, '#eef2f6')
    x = 200
    b += R(x - 18, 70, 36, 170, br) + R(x + 8, 70, 10, 170, dk)
    for y in range(90, 230, 30): b += arch_win(x - 6, y, 10, 18, '#3a3a4a')
    b += R(x - 24, 56, 48, 16, br) + windows(x - 18, 58, 4, 1, 6, 12, 5, 0, '#3a3a4a') + battlements(x - 24, 56, 48, br, 3, 5)
    b += R(x - 14, 30, 28, 26, br) + P(f'M{x-14} 30 L{x} 6 L{x+14} 30 Z', '#5a5a5a')
    for px in (x - 24, x + 20): b += R(px, 36, 4, 22, br) + spire(px + 2, 38, 6, 10, '#5a5a5a')
    b += R(0, 230, W, 14, '#8a8475')
    b += water(244, '#4f6f8a', 651, 14)
    b += P('M40 272 L150 272 L140 288 L50 288 Z', '#2b3a55') + R(80, 256, 40, 16, '#f4f1ea') + R(96, 244, 4, 12, '#d22630') + R(60, 262, 8, 10, '#f4f1ea')
    b += P('M250 268 L360 268 L352 282 L258 282 Z', '#c0392b') + R(290, 254, 36, 14, '#f4f1ea')
    return b
add('Grimsby', 'Grimsby Dock Tower', 'Built in 1852 to power the dock gates with water pressure - modelled on a tower in Siena.', 'grey', grimsby())

# Scunthorpe - steelworks
def scunthorpe():
    b = sun(70, 220, 22, '#ffd27a', '#ff7a3a') + cloud(260, 60, .8, '#ffd8c0')
    b += R(0, 180, W, 140, '#3a3a44')
    for i, x in enumerate((70, 160, 250, 340)):
        b += R(x - 16, 80, 32, 140, '#4a4a56') + R(x - 22, 60, 44, 24, '#55556a') + R(x - 4, 20, 8, 44, '#4a4a56')
        b += PL(f'M{x+16} 120 L{x+40} 120 L{x+40} 200', '#55556a', 6)
        b += C(x + 20, 14, 10, '#d8d2e0', 'opacity=".5"') + C(x + 30, 2, 13, '#d8d2e0', 'opacity=".4"')
        b += R(x - 10, 200, 20, 20, '#ff8a3a', 'opacity=".8"')
        b += T(x, 74, ['ANNE', 'BESS', 'MARY', 'VICTORIA'][i], 9, '#ffcd00', 'textLength="34" lengthAdjust="spacingAndGlyphs"')
    b += R(0, 260, W, 60, '#2a2a33') + ''.join(R(i * 30, 274, 20, 4, '#6a6a7a') for i in range(14))
    return b
add('Scunthorpe', 'The Four Queens', 'Scunthorpe\'s blast furnaces are named Anne, Bess, Mary and Victoria.', 'sunset', scunthorpe())
