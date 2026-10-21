from snaplib import *
from snaps8 import townhall
import random

S = {}
def add(city, title, note, sky, body, defs=''):
    slug = ''.join(ch for ch in city.lower() if ch.isalnum())
    S[city] = (title, note, scene(slug, sky, body, defs))
WIN = '#4a5878'

def stone_castle(st, keep=True, seed=1):
    dk = shade(st, -.2)
    b = R(40, 150, 320, 90, st) + battlements(40, 150, 320, st, 4, 7)
    for x in (40, 330): b += R(x - 6, 120, 36, 120, st) + R(x + 20, 120, 10, 120, dk) + battlements(x - 6, 120, 36, st, 3, 6)
    if keep: b += R(160, 80, 80, 160, st) + R(220, 80, 20, 160, dk) + battlements(160, 80, 80, st, 4, 7) + windows(174, 100, 3, 3, 10, 16, 12, 14, WIN, arch=True)
    b += arch_win(186, 196, 28, 44, '#3b2a1a')
    return b

def stadium(name, main, seed, cols, sub='#e6e9ef'):
    b = P('M20 230 L40 130 L360 130 L380 230 Z', main) + R(30, 122, 340, 10, sub) + ''.join(L(40 + i * 20, 122, 50 + i * 20, 110, '#c9ced8', 2) for i in range(17)) + L(40, 110, 360, 110, '#c9ced8', 2)
    b += T(200, 170, name, 22, '#ffffff', f'textLength="{min(300, len(name)*16)}" lengthAdjust="spacingAndGlyphs"')
    b += windows(60, 186, 12, 1, 18, 24, 5, 0, sub) + road(230, '#3a3f4a') + crowd(36, 10, 390, 238, seed, 1.05, 30, cols)
    return b

def cathedral(st, spire_h=0, twin=False, seed=1):
    dk = shade(st, -.18)
    b = R(40, 150, 320, 100, st) + P('M40 150 L200 126 L360 150 Z', '#5a6a6a') + windows(54, 166, 10, 1, 12, 40, 18, 0, WIN, arch=True)
    if twin:
        for x in (60, 290): b += R(x, 70, 50, 180, st) + R(x + 38, 70, 12, 180, dk) + battlements(x, 70, 50, st, 4, 7) + windows(x + 10, 90, 2, 3, 10, 24, 10, 12, WIN, arch=True)
    b += R(170, 70, 60, 180, st) + R(216, 70, 14, 180, dk) + battlements(170, 70, 60, st, 4, 7) + windows(182, 90, 2, 3, 12, 26, 12, 12, WIN, arch=True)
    if spire_h: b += spire(200, 70, 40, spire_h, '#7a8a8a')
    return b

# Birmingham - Selfridges discs
def birmingham():
    b = sun(70, 50, 12) + cloud(280, 40, .8)
    b += R(0, 150, 120, 110, '#c9ced8') + windows(8, 160, 6, 5, 12, 12, 6, 8, '#7fa8c8') + R(330, 130, 80, 130, '#b9c0cc')
    b += P('M140 260 Q120 160 170 110 Q230 70 290 110 Q330 160 320 260 Z', '#2b5fb8')
    rnd = random.Random(1001)
    for i in range(260):
        x = rnd.uniform(130, 330); y = rnd.uniform(90, 258)
        if (x - 228) ** 2 / 100 ** 2 + (y - 180) ** 2 / 95 ** 2 < 1: b += C(x, y, 3.2, '#d9e2f0') + C(x - .8, y - .8, 1.2, '#ffffff')
    b += R(0, 260, W, 60, '#9e978a')
    b += E(80, 268, 22, 12, '#5a4a3a') + C(98, 260, 8, '#5a4a3a') + P('M96 252 l-6 -8 l4 0 z M102 252 l6 -8 l-4 0 z', '#d8d2c4') + R(64, 276, 4, 12, '#5a4a3a') + R(92, 276, 4, 12, '#5a4a3a')
    b += crowd(12, 140, 390, 272, 1002, 1.05, 30)
    return b
add('Birmingham', 'Selfridges & the Bull', 'Selfridges is covered in 15,000 aluminium discs - and the bronze Bull is everyone\'s meeting point.', 'day', birmingham())

# Coventry - cathedral ruins
def coventry():
    st = '#b9806a'; dk = shade(st, -.2)
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(40, 60, 50, 190, st) + R(78, 60, 12, 190, dk) + battlements(40, 60, 50, st, 4, 7) + spire(65, 60, 40, 50, st)
    for i in range(6):
        x = 110 + i * 42
        b += R(x, 150 - (i % 2) * 20, 10, 100 + (i % 2) * 20, st) + arch_win(x + 12, 160, 24, 60, '#7fb0d9')
    b += R(110, 236, 260, 14, st)
    b += R(300, 140, 4, 60, '#3b3b3b') + R(290, 150, 24, 4, '#3b3b3b')
    b += ground(250, '#5f8f55', '#79a86b') + R(0, 270, W, 50, '#aaa294') + crowd(10, 30, 370, 280, 1011, 1.05, 30)
    return b
add('Coventry', 'The old cathedral', 'The ruins of the cathedral bombed in 1940 stand right next to the new one.', 'day', coventry())

# Nottingham - Trip to Jerusalem under the castle
def nottingham():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += P('M-10 320 L-10 120 Q60 90 140 100 L220 96 L240 320 Z', '#b99a6a') + P('M40 100 L200 96 L200 70 L60 70 Z', '#d8c8a8') + battlements(60, 70, 140, '#d8c8a8', 4, 6)
    b += R(160, 180, 220, 80, '#efe6d2') + P('M156 180 L270 150 L384 180 Z', '#6b4a3a') + windows(176, 196, 7, 1, 14, 18, 15, 0, WIN)
    b += T(270, 236, 'YE OLDE TRIP TO JERUSALEM', 9, '#1b1b1b', 'textLength="190" lengthAdjust="spacingAndGlyphs"') + T(270, 250, 'A.D. 1189', 9, '#1b1b1b', 'letter-spacing="2"')
    b += R(0, 260, W, 60, '#aaa294') + crowd(10, 160, 390, 270, 1021, 1.05, 30)
    return b
add('Nottingham', 'Ye Olde Trip to Jerusalem', 'Built into the castle rock - it claims to be the oldest inn in England, from 1189.', 'day', nottingham())

# Derby - cathedral tower & falcons
def derby():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += cathedral('#c9b48f', 0, False, 1031)
    for px in (172, 226): b += spire(px, 72, 8, 24, '#c9b48f')
    b += P('M120 50 l14 -6 l-4 6 l4 6 z', '#3b3b4a') + P('M280 36 l14 -6 l-4 6 l4 6 z', '#3b3b4a')
    b += R(0, 250, W, 70, '#aaa294') + crowd(10, 30, 370, 262, 1032, 1.05, 30)
    return b
add('Derby', 'Derby Cathedral', 'Peregrine falcons nest on the tower - there\'s a live webcam.', 'day', derby())

# Stoke - bottle kilns
def stoke():
    br = '#a8503a'
    b = cloud(90, 40, .9, '#eef2f6') + cloud(300, 60, .7, '#eef2f6')
    b += R(0, 200, W, 60, '#b98b6a') + windows(8, 210, 14, 2, 14, 12, 14, 8, WIN)
    for x, h in ((80, 140), (180, 160), (280, 130)):
        b += P(f'M{x-40} 220 Q{x-50} {220-h*.5} {x-12} {220-h} L{x+12} {220-h} Q{x+50} {220-h*.5} {x+40} 220 Z', br) + P(f'M{x} 220 L{x} {220-h} L{x+12} {220-h} Q{x+50} {220-h*.5} {x+40} 220 Z', shade(br, -.2))
        b += C(x + 6, 200 - h, 10, '#e8e8f0', 'opacity=".5"')
    b += R(0, 260, W, 60, '#8a8475')
    return b
add('Stoke-on-Trent', 'The bottle kilns', 'At their peak there were around 2,000 bottle ovens across the Potteries.', 'grey', stoke())

# Wolverhampton - Molineux
def wolverhampton():
    b = sun(70, 50, 12) + cloud(280, 40, .8)
    b += stadium('MOLINEUX', '#f2a900', 1041, ['#f2a900', '#f2a900', '#1b1b1b', '#ffffff'], '#1b1b1b')
    return b
add('Wolverhampton', 'Molineux', 'Wolves\' floodlit friendlies in the 1950s helped inspire the European Cup.', 'day', wolverhampton())

# Northampton - Holy Sepulchre round church
def northampton():
    st = '#b9a07a'; dk = shade(st, -.2)
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(70, 150, 120, 100, st) + R(70, 140, 120, 12, dk) + P('M66 142 Q130 100 194 142 Z', '#6b5a50') + windows(82, 170, 5, 1, 10, 30, 13, 0, WIN, arch=True)
    b += R(190, 150, 120, 100, st) + P('M186 150 L250 126 L314 150 Z', '#6b5a50') + windows(204, 170, 4, 1, 12, 34, 14, 0, WIN, arch=True)
    b += R(300, 70, 50, 180, st) + R(338, 70, 12, 180, dk) + battlements(300, 70, 50, st, 4, 6) + spire(325, 70, 40, 60, '#8a8478')
    b += ground(250, '#5f8f55', '#79a86b') + tree(30, 254, 1.6)
    return b
add('Northampton', 'The Round Church', 'The Church of the Holy Sepulchre, built around 1100 - one of only a few round churches in England.', 'day', northampton())

# Telford - Iron Bridge
def telford():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += hills(130, '#5f8f55', 1061, 20) + hills(160, '#4f7f45', 1062, 16)
    for i, x in enumerate(range(20, 160, 34)): b += R(x, 150 + i * 6, 30, 40, ['#c9a27e', '#e3d6be', '#b88a68', '#d8c8a8', '#c4b08e'][i]) + P(f'M{x-2} {150+i*6} L{x+15} {140+i*6} L{x+32} {150+i*6} Z', '#5b4a44')
    b += water(220, '#5a7a6a', 1063, 14)
    b += R(40, 196, 320, 8, '#3a3a40') + PL('M70 230 Q200 120 330 230', '#3a3a40', 6)
    for k in range(4): b += PL(f'M{70+k*8} 230 Q200 {130+k*10} {330-k*8} 230', '#3a3a40', 2.5)
    for k in range(1, 12):
        x = 70 + k * 21.6
        b += L(x, 204, x, 204 + abs(x - 200) * .2, '#3a3a40', 1.4)
    b += R(20, 196, 50, 40, '#9a8a7a') + R(330, 196, 50, 40, '#9a8a7a')
    return b
add('Telford', 'The Iron Bridge', 'Opened in 1781 - the world\'s first major bridge made of cast iron.', 'day', telford())

# Newcastle-under-Lyme - Guildhall
def nul():
    br = '#a8503a'
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(110, 120, 180, 120, br) + R(110, 112, 180, 10, '#d8c8a8') + windows(126, 132, 6, 2, 16, 24, 11.6, 14, '#e8f0f6', arch=True)
    b += R(110, 196, 180, 44, '#d8c8a8') + windows(122, 202, 7, 1, 14, 34, 9, 0, '#3a3a4a', arch=True)
    b += R(186, 70, 28, 44, '#d8c8a8') + clockface(200, 90, 9) + P('M182 70 Q200 46 218 70 Z', '#4f8f7f')
    b += R(0, 240, W, 80, '#aaa294')
    for x in (40, 330): b += R(x - 26, 252, 52, 4, '#d22630') + R(x - 26, 244, 52, 9, '#f7f2e4') + R(x - 24, 256, 2, 20, '#555') + R(x + 22, 256, 2, 20, '#555')
    b += crowd(12, 20, 380, 266, 1071, 1.05, 30)
    return b
add('Newcastle-under-Lyme', 'The Guildhall', 'The town got its first charter in 1173 - one of the oldest market towns in Staffordshire.', 'day', nul())

# Solihull - Land Rover
def solihull():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += hills(180, '#8fae6a', 1081, 16) + ground(230, '#8a6a4a', '#9a7a5a')
    for k in range(6): b += E(40 + k * 70, 270 + (k % 2) * 16, 26, 6, '#6a4a2a')
    x, y = 200, 236
    b += R(x - 80, y - 60, 160, 44, '#3f6b4a', 6) + R(x - 50, y - 92, 110, 36, '#3f6b4a', 4) + windows(x - 44, y - 86, 3, 1, 26, 22, 8, 0, '#a3c4dc')
    b += R(x + 78, y - 50, 8, 26, '#2a2a2a') + R(x - 86, y - 40, 10, 14, '#2a2a2a') + R(x - 82, y - 30, 6, 4, '#ffe27a')
    b += C(x - 46, y - 12, 18, '#1b1b1b') + C(x - 46, y - 12, 7, '#9a9a9a') + C(x + 50, y - 12, 18, '#1b1b1b') + C(x + 50, y - 12, 7, '#9a9a9a')
    b += C(x - 120, y - 6, 14, '#8a6a4a', 'opacity=".5"') + C(x - 140, y - 16, 10, '#8a6a4a', 'opacity=".4"')
    return b
add('Solihull', 'Off-road at Solihull', 'The very first Land Rovers were built in Solihull in 1948.', 'day', solihull())

# West Bromwich - The Hawthorns
def westbrom():
    b = sun(70, 50, 12) + cloud(280, 40, .8)
    b += stadium('THE HAWTHORNS', '#1b3a8f', 1091, ['#1b3a8f', '#ffffff', '#1b3a8f', '#ffffff'])
    return b
add('West Bromwich', 'The Hawthorns', 'At about 168 metres above sea level, it\'s the highest league ground in England.', 'day', westbrom())

# Dudley - Black Country Living Museum
def dudley():
    b = cloud(90, 40, .9, '#eef2f6') + cloud(300, 60, .7, '#eef2f6')
    b += hills(110, '#5f8f55', 1101, 14) + R(280, 70, 70, 50, '#8a8478') + battlements(280, 70, 70, '#8a8478', 4, 6)
    for i, x in enumerate(range(10, 400, 56)):
        b += R(x, 170, 52, 70, ['#a8503a', '#b98b6a', '#8a4a32', '#c4a27a'][i % 4]) + windows(x + 6, 180, 2, 2, 14, 14, 12, 10, WIN) + P(f'M{x-2} 170 L{x+26} 156 L{x+54} 170 Z', '#4b3d3a')
    b += R(0, 240, W, 80, '#7a7466') + L(0, 270, W, 270, '#c9ced8', 2) + L(0, 278, W, 278, '#c9ced8', 2)
    b += R(140, 248, 70, 24, '#d8b23a', 4) + R(146, 252, 58, 8, '#cfe3f2') + C(156, 274, 5, '#1b1b1b') + C(196, 274, 5, '#1b1b1b')
    b += crowd(8, 220, 390, 262, 1102, 1.05, 30, ['#3b3b3b', '#5a4a3a', '#2a2a2a', '#7a1f2b'])
    return b
add('Dudley', 'The Black Country Living Museum', 'The old streets here have stood in for Birmingham in Peaky Blinders.', 'grey', dudley())

# Walsall - leather
def walsall():
    br = '#a8503a'
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(60, 90, 280, 160, br) + windows(74, 104, 10, 5, 14, 16, 12.4, 12, '#e8f0f6') + T(200, 84, 'LEATHER MUSEUM', 14, '#5a3a22', 'letter-spacing="2"')
    b += R(0, 250, W, 70, '#aaa294')
    b += f'<g transform="translate(320 270)">' + P('M-30 0 Q-30 -26 0 -28 Q30 -26 30 0 L20 4 L-20 4 Z', '#8a5a2a') + P('M-8 -28 Q0 -40 8 -28', 'none', 'stroke="#5a3a1a" stroke-width="3"') + '</g>'
    b += crowd(8, 30, 280, 262, 1111, 1.05, 30)
    return b
add('Walsall', 'The Leather Museum', 'Walsall\'s been the heart of British saddle-making for centuries - hence "the Saddlers".', 'day', walsall())

# Burton - brewing
def burton():
    br = '#a8503a'
    b = sun(70, 50, 12) + cloud(280, 40, .8)
    b += R(40, 110, 220, 140, br) + windows(54, 124, 8, 4, 14, 16, 12, 12, '#e8f0f6') + R(200, 40, 24, 80, br) + T(150, 104, 'BREWERY', 14, '#f4f1ea', 'letter-spacing="3"')
    b += R(280, 90, 70, 60, '#7a7a7a') + R(290, 150, 6, 100, '#5a5a5a') + R(334, 150, 6, 100, '#5a5a5a')
    b += R(0, 250, W, 70, '#8a8475')
    for i in range(6): b += E(60 + i * 50, 262, 18, 22, '#8a5a32') + R(42 + i * 50, 250, 36, 3, '#3b3b3b') + R(42 + i * 50, 272, 36, 3, '#3b3b3b')
    return b
add('Burton upon Trent', 'The brewing capital', 'Burton\'s gypsum-rich water made it Britain\'s brewing capital - brewers elsewhere still "Burtonise" their water.', 'day', burton())

# Chesterfield - crooked spire
def chesterfield():
    st = '#b9a07a'; dk = shade(st, -.2)
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(60, 160, 280, 90, st) + P('M60 160 L200 136 L340 160 Z', '#6b5a50') + windows(74, 176, 9, 1, 12, 34, 18, 0, WIN, arch=True)
    b += R(170, 100, 60, 60, st) + R(218, 100, 12, 60, dk)
    b += P('M168 100 Q176 60 196 30 Q206 14 214 6 Q214 40 226 70 Q232 86 232 100 Z', '#6a5a50')
    for k in range(7): b += PL(f'M{172+k*8} 100 Q{186+k*4} 60 {212-k*0.5} 8', '#4f4238', 1)
    b += ground(250, '#5f8f55', '#79a86b') + R(0, 270, W, 50, '#aaa294') + crowd(10, 30, 370, 280, 1131, 1.05, 30)
    return b
add('Chesterfield', 'The Crooked Spire', 'It twists 45 degrees and leans about 9 feet off centre.', 'day', chesterfield())

# Mansfield - viaduct
def mansfield():
    st = '#c9b48f'; dk = shade(st, -.2)
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(0, 90, W, 16, st) + R(0, 86, W, 5, dk)
    for i in range(7):
        x = -20 + i * 64
        b += R(x, 106, 16, 150, st) + P(f'M{x+16} 106 L{x+16} 130 A24 24 0 0 1 {x+64} 130 L{x+64} 106 Z', st)
    for i, x in enumerate((20, 150, 280)): b += R(x, 180, 80, 70, ['#d8c8a8', '#b98b6a', '#e3d6be'][i]) + windows(x + 8, 190, 4, 2, 10, 12, 8, 12, WIN)
    b += R(0, 250, W, 70, '#aaa294') + crowd(10, 20, 380, 262, 1141, 1.05, 30)
    return b
add('Mansfield', 'Mansfield Viaduct', 'The stone railway viaduct strides right across the town centre, built in 1875.', 'day', mansfield())

# Lincoln - cathedral
def lincoln():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += cathedral('#d8c8a0', 0, True, 1151)
    b += P('M-10 320 L-10 250 Q200 230 410 250 L410 320 Z', '#aaa294')
    for i in range(6): b += R(10 + i * 30, 250 + i * 8, 28, 40, ['#e3d6be', '#c9a27e', '#d8c8a8'][i % 3])
    return b
add('Lincoln', 'Lincoln Cathedral', 'With its old spire it was the tallest building in the world for over 200 years.', 'day', lincoln())

# Hereford - cathedral & cider apples
def hereford():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += cathedral('#b8806a', 0, False, 1161)
    for px in (172, 226): b += spire(px, 72, 8, 24, '#b8806a')
    b += ground(250, '#5f8f55', '#79a86b')
    for x in (40, 360):
        b += R(x - 3, 220, 6, 34, '#5a3a22') + C(x, 206, 26, '#4f8f45') + ''.join(C(x - 16 + k * 8, 200 + (k % 3) * 8, 3.4, '#d22630') for k in range(5))
    return b
add('Hereford', 'Hereford Cathedral', 'Home of the Mappa Mundi - a map of the world drawn around 1300.', 'day', hereford())

# Worcester - cathedral & cricket
def worcester():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += cathedral('#d6c39f', 0, False, 1171)
    for px in (172, 226): b += spire(px, 72, 8, 24, '#d6c39f')
    b += water(250, '#5a7f8a', 1172, 6)
    b += R(0, 262, W, 58, '#6fb05a') + R(180, 274, 40, 26, '#d9c79a')
    b += crowd(4, 150, 250, 290, 1173, .9, 10, ['#ffffff']) + L(196, 280, 196, 290, '#c9a27e', 1) + L(204, 280, 204, 290, '#c9a27e', 1)
    return b
add('Worcester', 'The cathedral & New Road', 'Lea & Perrins have made Worcestershire sauce in the city since 1837.', 'day', worcester())

# Redditch - needle mill
def redditch():
    br = '#a8503a'
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(60, 130, 200, 110, br) + P('M56 130 L160 100 L264 130 Z', '#5b4a44') + windows(76, 146, 6, 3, 14, 16, 16, 12, '#e8f0f6')
    b += C(290, 200, 40, 'none', 'stroke="#5a3a22" stroke-width="6"') + ''.join(L(290, 200, 290 + math.cos(a) * 40, 200 + math.sin(a) * 40, '#5a3a22', 3) for a in [k * 0.785 for k in range(8)])
    b += water(240, '#4f7f8a', 1181, 10) + ground(270, '#5f8f55', '#79a86b')
    b += L(40, 70, 140, 30, '#c9ced8', 3) + C(138, 31, 3, 'none', 'stroke="#c9ced8" stroke-width="1.5"')
    return b
add('Redditch', 'Forge Mill Needle Museum', 'Redditch once made around 90% of the world\'s needles.', 'day', redditch())

# Kidderminster - steam train
def kidderminster():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(200, 140, 200, 90, '#b98b6a') + P('M196 140 L300 112 L404 140 Z', '#5b4a44') + windows(214, 156, 6, 2, 14, 16, 14, 14, WIN)
    b += R(0, 230, W, 90, '#7a7466') + L(0, 262, W, 262, '#c9ced8', 2)
    x = 110
    b += R(x - 70, 196, 130, 44, '#2a6b3a', 6) + R(x + 50, 176, 30, 64, '#2a6b3a') + R(x - 50, 160, 14, 36, '#1b1b1b') + R(x - 54, 156, 22, 6, '#1b1b1b')
    b += C(x - 44, 136, 14, '#e8e8f0', 'opacity=".8"') + C(x - 30, 116, 18, '#e8e8f0', 'opacity=".6"')
    for cx in (x - 40, x, x + 40): b += C(cx, 248, 13, '#1b1b1b') + C(cx, 248, 4, '#c9a227')
    b += R(x - 72, 230, 156, 4, '#c9a227')
    return b
add('Kidderminster', 'The Severn Valley Railway', 'Kidderminster was the carpet capital of Britain - now it\'s the start of a great steam line.', 'day', kidderminster())

# Stourbridge - glass cone
def stourbridge():
    br = '#a8503a'
    b = sun(70, 50, 12) + cloud(280, 40, .8)
    b += P('M120 250 L156 70 Q200 50 244 70 L280 250 Z', br) + P('M200 250 L200 58 Q224 62 244 70 L280 250 Z', shade(br, -.2))
    b += arch_win(180, 206, 40, 44, '#ffb84a')
    b += water(250, '#4f6f7a', 1201, 8) + R(0, 270, W, 50, '#aaa294') + crowd(8, 30, 370, 280, 1202, 1.05, 30)
    return b
add('Stourbridge', 'The Red House Glass Cone', 'One of only four complete glass cones left in the UK.', 'day', stourbridge())

# Tamworth - castle
def tamworth():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += P('M-10 320 L-10 240 Q200 180 410 240 L410 320 Z', '#5f8f55')
    b += stone_castle('#c4a27a')
    b += water(270, '#4f7f8a', 1211, 8) + flowers(0, 400, 250, 1212, 30)
    return b
add('Tamworth', 'Tamworth Castle', 'Tamworth was the capital of Mercia, the Anglo-Saxon kingdom of King Offa.', 'day', tamworth())

# Nuneaton - George Eliot statue
def nuneaton():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    for i, x in enumerate(range(-10, 410, 60)):
        b += R(x, 130, 56, 120, ['#c4a27a', '#e3d6be', '#b98b6a', '#d8c8a8'][i % 4]) + windows(x + 8, 144, 3, 3, 10, 14, 7, 12, WIN) + R(x - 2, 124, 60, 6, '#5b4a44')
    b += R(0, 250, W, 70, '#aaa294')
    b += R(180, 220, 40, 40, '#8a8a8a') + P('M190 220 L196 170 L206 170 L212 220 Z', '#4a5a5a') + C(201, 162, 8, '#4a5a5a') + P('M188 200 L214 200 L218 222 L184 222 Z', '#4a5a5a')
    b += crowd(10, 20, 380, 270, 1221, 1.05, 30)
    return b
add('Nuneaton', 'George Eliot', 'The novelist was born just outside Nuneaton in 1819 - and wrote it into her books.', 'day', nuneaton())

# Rugby - Rugby School
def rugby():
    st = '#c9a87e'; dk = shade(st, -.2)
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(40, 110, 320, 110, st) + battlements(40, 110, 320, st, 4, 6) + windows(54, 126, 12, 2, 12, 22, 13, 16, WIN, arch=True)
    b += R(170, 60, 60, 160, st) + R(216, 60, 14, 160, dk) + battlements(170, 60, 60, st, 4, 7)
    b += ground(220, '#5f9a50', '#7ab36a')
    for x in (80, 320): b += R(x - 26, 160, 4, 110, '#ffffff') + R(x + 22, 160, 4, 110, '#ffffff') + R(x - 26, 230, 52, 4, '#ffffff')
    b += E(200, 262, 12, 7, '#8a5a2a') + L(192, 262, 208, 262, '#ffffff', 1)
    return b
add('Rugby', 'Rugby School', 'Where William Webb Ellis is said to have picked up the ball and run, in 1823.', 'day', rugby())

# Leamington - Royal Pump Rooms
def leamington():
    st = '#efe6d2'; dk = shade(st, -.14)
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(40, 130, 320, 110, st) + R(40, 124, 320, 8, dk)
    for i in range(14): b += R(50 + i * 22, 140, 8, 100, '#f8f2e4') + R(55 + i * 22, 140, 3, 100, dk)
    b += R(170, 90, 60, 40, st) + P('M166 90 L200 70 L234 90 Z', dk)
    b += ground(240, '#5f9a50', '#7ab36a') + flowers(0, 400, 244, 1241, 40) + tree(20, 246, 1.6) + tree(380, 246, 1.6)
    return b
add('Leamington Spa', 'The Royal Pump Rooms', 'Leamington got its "Royal" in 1838, after Queen Victoria visited.', 'day', leamington())

# Warwick - castle
def warwick():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += stone_castle('#b9a68a')
    b += R(250, 40, 50, 120, '#b9a68a') + battlements(250, 40, 50, '#b9a68a', 4, 6)
    b += water(240, '#4f7f8a', 1251, 12)
    b += tree(20, 244, 1.8) + tree(380, 244, 1.8)
    return b
add('Warwick', 'Warwick Castle', 'William the Conqueror built the first castle here in 1068.', 'day', warwick())

# Kettering - Wicksteed Park
def kettering():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += water(180, '#4f8ab5', 1261, 12) + ground(220, '#5f9a50', '#7ab36a')
    b += PL('M20 210 Q80 80 140 180 Q200 260 260 140 Q300 80 380 200', '#d22630', 5)
    for x in (40, 100, 160, 220, 280, 340): b += L(x, 220, x, 140 + (x % 80), '#c9ced8', 2)
    b += R(150, 200, 60, 10, '#1d4ed8', 2) + crowd(5, 154, 206, 200, 1262, .7, 1)
    b += R(40, 250, 6, 40, '#5a3a22') + L(43, 250, 70, 276, '#888', 1) + R(64, 276, 14, 4, '#ffcd00')
    b += crowd(8, 120, 380, 272, 1263, 1.05, 30)
    return b
add('Kettering', 'Wicksteed Park', 'Opened in 1921 - one of the oldest leisure parks in the country.', 'day', kettering())

# Corby - Little Scotland
def corby():
    b = cloud(90, 40, .9, '#eef2f6') + cloud(300, 60, .7, '#eef2f6')
    b += R(0, 120, W, 110, '#6a6a76') + R(60, 60, 30, 70, '#5a5a66') + R(300, 70, 24, 60, '#5a5a66')
    b += ground(230, '#5f9a50', '#7ab36a')
    x = 200
    b += R(x - 2, 80, 4, 160, '#c9ced8') + R(x + 2, 80, 70, 46, '#1d5fb8') + L(x + 2, 80, x + 72, 126, '#ffffff', 6) + L(x + 72, 80, x + 2, 126, '#ffffff', 6)
    for k, c in enumerate(('#2a6b3a', '#d22630', '#1d4ed8')):
        b += R(60 + k * 100, 240, 40, 30, c) + R(60 + k * 100, 246, 40, 3, '#ffcd00') + R(60 + k * 100, 256, 40, 3, '#1b1b1b')
    b += crowd(10, 20, 380, 280, 1271, 1.05, 30)
    return b
add('Corby', 'Little Scotland', 'Thousands moved down from Scotland for the steelworks in the 1930s - hence the nickname.', 'grey', corby())

# Wellingborough - church & market
def wellingborough():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += cathedral('#c9b48f', 70, False, 1281)
    b += R(0, 250, W, 70, '#aaa294')
    for x in (60, 330): b += R(x - 26, 262, 52, 4, '#2a8a46') + R(x - 26, 254, 52, 9, '#f7f2e4') + R(x - 24, 266, 2, 20, '#555') + R(x + 22, 266, 2, 20, '#555')
    b += crowd(10, 20, 380, 270, 1282, 1.05, 30)
    return b
add('Wellingborough', 'Market day', 'The town grew up around its springs and wells - the Red Well is one of them.', 'day', wellingborough())
