from snaplib import *
from snaps10 import cathedral, stadium, stone_castle
import random

S = {}
def add(city, title, note, sky, body, defs=''):
    slug = ''.join(ch for ch in city.lower() if ch.isalnum())
    S[city] = (title, note, scene(slug, sky, body, defs))
WIN = '#4a5878'

def pier(y, length_to, col='#6b4a3a', seed=1):
    b = P(f'M0 {y} L{length_to} {y-60} L{length_to} {y-54} L0 {y+8} Z', col)
    for k in range(int(length_to / 20)):
        x = k * 20; b += L(x, y + 4 - x * 60 / length_to, x, y + 30 - x * 60 / length_to, shade(col, -.2), 2)
    return b

def seaside(seed, sky_sun=True):
    b = (sun(320, 60, 14) if sky_sun else '') + cloud(90, 50, .8)
    b += water(150, '#3f86b5', seed, 18) + P('M-10 220 Q200 204 410 214 L410 320 L-10 320 Z', '#ecd9a8')
    return b

def terrace(y, seed, n=7, w=58, hmin=70, hmax=110):
    rnd = random.Random(seed); b = ''
    cols = ['#c4a27a', '#e3d6be', '#b98b6a', '#d8c8a8', '#efe6d2', '#a8826a']
    for i in range(n):
        x = -10 + i * w; h = rnd.randint(hmin, hmax); c = rnd.choice(cols)
        b += R(x, y - h, w - 2, h, c) + windows(x + 8, y - h + 10, 3, max(1, int(h / 26)), 10, 12, 6, 12, WIN) + P(f'M{x-2} {y-h} L{x+w/2-1} {y-h-14} L{x+w} {y-h} Z', '#5b4a44')
    return b

# Luton - hat & Kenilworth Road
def luton():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += terrace(220, 1301, 8, 52)
    b += R(0, 220, W, 100, '#3a3f4a') + crowd(24, 10, 390, 230, 1302, 1.05, 30, ['#f07a14', '#f07a14', '#ffffff', '#1b3a8f'])
    b += f'<g transform="translate(200 80)">' + E(0, 30, 70, 14, '#1b3a8f') + P('M-40 30 Q-42 -20 0 -22 Q42 -20 40 30 Z', '#1b3a8f') + R(-40, 16, 80, 10, '#f07a14') + '</g>'
    return b
add('Luton', 'The Hatters', 'Luton made straw hats for the world - which is why the football club are the Hatters.', 'day', luton())

# Norwich - cathedral spire
def norwich():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += cathedral('#e1d3b4', 150, False, 1311)
    b += ground(250, '#5f9a50', '#7ab36a') + tree(30, 254, 1.8) + tree(380, 254, 1.8)
    return b
add('Norwich', 'Norwich Cathedral', 'Its spire is the second tallest in England, after Salisbury.', 'day', norwich())

# Peterborough - west front
def peterborough():
    st = '#d8c49c'; dk = shade(st, -.18)
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(30, 80, 340, 170, st) + battlements(30, 80, 340, st, 4, 6)
    for x in (40, 150, 260):
        b += P(f'M{x} 250 L{x} 120 Q{x+50} 70 {x+100} 120 L{x+100} 250 Z', dk) + P(f'M{x+10} 250 L{x+10} 126 Q{x+50} 86 {x+90} 126 L{x+90} 250 Z', st)
        b += arch_win(x + 38, 150, 24, 50, WIN)
    for x in (30, 360): b += spire(x + 5, 82, 14, 40, st)
    b += R(0, 250, W, 70, '#aaa294') + crowd(10, 30, 370, 262, 1321, 1.05, 30)
    return b
add('Peterborough', 'Peterborough Cathedral', 'Catherine of Aragon, Henry VIII\'s first wife, is buried here.', 'day', peterborough())

# Southend - pier
def southend():
    b = seaside(1331)
    b += pier(214, 400)
    b += R(150, 168, 40, 12, '#1d4ed8', 3) + windows(154, 171, 4, 1, 6, 5, 3, 0, '#cfe3f2') + R(190, 166, 30, 12, '#1d4ed8', 3)
    b += crowd(12, 20, 380, 240, 1332, 1.05, 50)
    return b
add('Southend-on-Sea', 'Southend Pier', 'At 1.33 miles, the longest pleasure pier in the world - with its own railway.', 'day', southend())

# Cambridge - King's College Chapel & punts
def cambridge():
    st = '#e3d6b8'; dk = shade(st, -.16)
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(60, 100, 280, 110, st) + windows(80, 116, 9, 1, 14, 76, 15.5, 0, WIN, arch=True)
    for x in (56, 336): b += R(x - 6, 70, 20, 140, st) + spire(x + 4, 72, 14, 30, st)
    for x in range(90, 330, 30): b += spire(x, 102, 6, 16, st)
    b += ground(210, '#5f9a50', '#7ab36a') + water(240, '#4f7f8a', 1341, 12)
    for i, x in enumerate((80, 220)):
        b += R(x, 270 + i * 10, 90, 8, '#6b4a2a') + person(x + 80, 270 + i * 10, '#ffffff', SKIN[i], 1.2) + L(x + 86, 230 + i * 10, x + 70, 300 + i * 10, '#3b3b3b', 1.5) + crowd(2, x + 20, x + 50, 270 + i * 10, 1342 + i, 1, 1)
    return b
add('Cambridge', 'King\'s College Chapel', 'Punting past King\'s - and Watson and Crick told the Eagle they\'d found DNA in 1953.', 'day', cambridge())

# Ipswich - Ancient House
def ipswich():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(70, 110, 260, 140, '#f0e2c0') + P('M64 110 L200 70 L336 110 Z', '#6b4a3a')
    for x in (90, 170, 250): b += R(x, 130, 60, 40, '#a3c4dc') + ''.join(L(x + k * 12, 130, x + k * 12, 170, '#f0e2c0', 2) for k in range(1, 5))
    for k in range(10): b += PL(f'M{80+k*25} 190 q8 -10 16 0 t16 0', '#c9a27a', 2)
    b += R(120, 200, 160, 50, '#e8d6b0') + R(185, 208, 30, 42, '#5a3a22')
    b += R(0, 250, W, 70, '#aaa294') + crowd(10, 20, 380, 262, 1351, 1.05, 30)
    return b
add('Ipswich', 'The Ancient House', 'Covered in 1670 pargeting - decorative plasterwork showing the four known continents.', 'day', ipswich())

# Chelmsford - Marconi
def chelmsford():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(60, 150, 200, 100, '#b98b6a') + windows(72, 164, 8, 3, 14, 16, 9, 10, WIN) + T(160, 144, 'MARCONI', 14, '#1b1b1b', 'letter-spacing="4"')
    x = 310
    b += P(f'M{x-14} 250 L{x} 30 L{x+14} 250', 'none', 'stroke="#5a5a66" stroke-width="2"') + ''.join(L(x - 14 + k * 1.4, 250 - k * 22, x + 14 - k * 1.4, 250 - k * 22, '#5a5a66', 1) for k in range(1, 10))
    for i in range(4): b += PL(f'M{x+10+i*10} {40-i*4} q8 8 0 16', '#ffcd00', 1.6)
    b += R(0, 250, W, 70, '#aaa294')
    return b
add('Chelmsford', 'Birthplace of radio', 'Marconi opened the world\'s first wireless factory here in 1898.', 'day', chelmsford())

# Colchester - castle & Jumbo
def colchester():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(40, 130, 200, 120, '#b8806a') + battlements(40, 130, 200, '#b8806a', 4, 6) + windows(56, 150, 6, 2, 10, 16, 20, 20, WIN, arch=True)
    for x in (40, 220): b += R(x - 4, 116, 28, 134, '#b8806a')
    b += R(290, 70, 70, 50, '#a8503a') + battlements(290, 70, 70, '#a8503a', 3, 5)
    for x in (294, 316, 338): b += R(x, 120, 14, 130, '#a8503a') + arch_win(x + 2, 130, 10, 20, '#e8f0f6')
    b += ground(250, '#5f9a50', '#7ab36a') + tree(20, 254, 1.4)
    return b
add('Colchester', 'Colchester Castle & Jumbo', 'The biggest Norman castle keep in Europe - built on the ruins of a Roman temple.', 'day', colchester())

# Watford - Vicarage Road
def watford():
    b = sun(70, 50, 12) + cloud(280, 40, .8)
    b += stadium('VICARAGE ROAD', '#ffcd00', 1371, ['#ffcd00', '#d22630', '#1b1b1b', '#ffcd00'], '#d22630')
    return b
add('Watford', 'Vicarage Road', 'Elton John owned the club twice and is still its honorary life president.', 'day', watford())

# Bedford - Embankment
def bedford():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += tree(30, 200, 2.4) + tree(110, 196, 2) + tree(300, 198, 2.2) + tree(380, 200, 2.4)
    b += R(0, 200, W, 10, '#d8d2c4') + water(210, '#4f7f8a', 1381, 14)
    b += PL('M60 220 Q200 150 340 220', '#f4f4f4', 3) + PL('M60 150 L60 225 M340 150 L340 225', '#f4f4f4', 4)
    for k in range(1, 14):
        x = 60 + k * 20; y = 220 - 70 * (1 - ((x - 200) / 140) ** 2)
        b += L(x, y, x, 222, '#f4f4f4', 1)
    b += R(56, 220, 288, 5, '#f4f4f4')
    b += E(130, 270, 9, 4, '#f7f7f7') + C(137, 265, 3, '#f7f7f7')
    return b
add('Bedford', 'The Embankment', 'John Bunyan wrote much of The Pilgrim\'s Progress while locked up in Bedford jail.', 'day', bedford())

# Stevenage - clock tower
def stevenage():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(0, 160, 160, 90, '#e6e9ef') + R(240, 160, 160, 90, '#e6e9ef') + windows(8, 176, 7, 2, 16, 20, 6, 12, '#7fa8c8') + windows(248, 176, 7, 2, 16, 20, 6, 12, '#7fa8c8')
    b += R(190, 70, 20, 180, '#f4f1ea') + R(184, 70, 32, 32, '#1b3a8f') + clockface(200, 86, 11)
    b += R(0, 250, W, 70, '#c9c2b4') + E(200, 270, 50, 10, '#7fb0d9') + crowd(10, 20, 380, 266, 1391, 1.05, 40)
    return b
add('Stevenage', 'The Town Square', 'Stevenage was Britain\'s first post-war New Town, designated in 1946.', 'day', stevenage())

# Harlow - The Lawn tower
def harlow():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += tree(60, 240, 2.4, '#3f7f45') + tree(340, 240, 2.6, '#3f7f45')
    b += R(160, 60, 80, 180, '#e6e2d6') + windows(170, 70, 4, 9, 10, 12, 8, 6, '#7fa8c8') + ''.join(R(158, 64 + k * 18, 84, 3, '#c9c4b6') for k in range(10))
    b += ground(240, '#5f9a50', '#7ab36a')
    b += R(100, 230, 10, 20, '#8a8a8a') + C(105, 222, 8, '#5a6a6a') + R(290, 220, 30, 30, '#d22630', 15)
    return b
add('Harlow', 'The Lawn', 'Built in 1951 - Britain\'s first residential tower block.', 'day', harlow())

# Basildon - new town centre
def basildon():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(150, 50, 70, 200, '#d8d2c4') + windows(158, 60, 4, 12, 10, 10, 6, 5, '#7fa8c8') + R(150, 230, 70, 20, '#5a5a5a')
    b += R(0, 170, 140, 80, '#e6e9ef') + R(230, 170, 170, 80, '#e6e9ef') + windows(8, 184, 6, 2, 16, 18, 6, 12, '#7fa8c8') + windows(240, 184, 7, 2, 16, 18, 6, 12, '#7fa8c8')
    b += R(0, 250, W, 70, '#c9c2b4') + E(200, 278, 40, 10, '#7fb0d9') + crowd(12, 20, 380, 268, 1411, 1.05, 40)
    return b
add('Basildon', 'Town Square', 'One of the first wave of post-war New Towns, designated in 1949.', 'day', basildon())

# Brentwood - cathedral
def brentwood():
    st = '#efe6d2'; dk = shade(st, -.14)
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(80, 120, 240, 130, st) + R(80, 114, 240, 8, dk) + P('M150 114 L200 90 L250 114 Z', st)
    for i in range(5): b += R(150 + i * 22, 122, 10, 128, '#f8f2e4') + R(156 + i * 22, 122, 3, 128, dk)
    b += windows(92, 140, 2, 2, 14, 30, 14, 20, WIN, arch=True) + windows(270, 140, 2, 2, 14, 30, 14, 20, WIN, arch=True)
    b += R(186, 60, 28, 34, st) + P('M182 60 Q200 40 218 60 Z', '#7a9a8a') + R(199, 30, 2, 12, '#c9a227')
    b += ground(250, '#5f9a50', '#7ab36a') + tree(30, 254, 1.6) + tree(380, 254, 1.6)
    return b
add('Brentwood', 'Brentwood Cathedral', 'Rebuilt in 1991 in classical Italianate style - it looks centuries older.', 'day', brentwood())

# King's Lynn - Custom House
def kingslynn():
    st = '#e3d6b8'
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(140, 130, 120, 110, st) + windows(152, 146, 4, 2, 16, 24, 10, 16, WIN, arch=True) + R(136, 122, 128, 10, '#c9b48f')
    b += R(170, 90, 60, 34, st) + windows(178, 96, 3, 1, 10, 20, 10, 0, WIN, arch=True) + R(194, 50, 12, 40, st) + P('M190 50 L200 34 L210 50 Z', '#6b5a50')
    b += C(200, 70, 6, '#c9a227')
    b += R(0, 240, W, 10, '#8a8475') + water(250, '#4f6f7a', 1431, 12)
    b += P('M20 268 L120 268 L112 282 L28 282 Z', '#2b3a55') + R(50, 252, 4, 16, '#5a3a22')
    return b
add('King\'s Lynn', 'The Custom House', 'Built in 1683, when Lynn was one of England\'s busiest ports.', 'day', kingslynn())

# Great Yarmouth - Nelson's Monument / Golden Mile
def yarmouth():
    b = seaside(1441)
    b += pier(214, 250, '#e6e9ef')
    b += R(260, 130, 120, 80, '#ffffff') + R(260, 124, 120, 8, '#d22630') + T(320, 150, 'BRITANNIA', 12, '#1b3a8f', 'letter-spacing="2"') + windows(270, 160, 6, 2, 12, 12, 6, 10, '#ffcd00')
    b += R(60, 60, 10, 150, '#e3d6be') + C(65, 54, 7, '#c9a227') + R(52, 200, 26, 12, '#d8c8a8')
    b += crowd(12, 20, 380, 240, 1442, 1.05, 50)
    return b
add('Great Yarmouth', 'The Golden Mile', 'Nelson\'s Monument here was finished in 1819 - decades before the one in London.', 'day', yarmouth())

# Lowestoft - Ness Point
def lowestoft():
    b = sun(330, 110, 18, '#ffd27a', '#ff9e5a') + cloud(120, 60, .8, '#ffe1c7')
    b += water(150, '#3f6f9a', 1451, 18)
    b += P('M-10 210 L260 200 L300 214 L-10 240 Z', '#8a8475')
    b += C(240, 196, 22, '#e6e9ef') + ''.join(L(240, 196, 240 + math.cos(k * .7) * 22, 196 + math.sin(k * .7) * 22, '#9aa3b0', 1) for k in range(9))
    b += T(240, 200, 'N', 8, '#1b1b1b') + R(0, 240, W, 80, '#ecd9a8')
    for x in (100, 340): b += L(x, 240, x, 120, '#e6e9ef', 4) + ''.join(L(x, 130, x + math.cos(a) * 40, 130 + math.sin(a) * 40, '#e6e9ef', 3) for a in (-1.6, .5, 2.6))
    b += crowd(6, 160, 300, 252, 1452, 1.05, 30)
    return b
add('Lowestoft', 'Ness Point', 'The most easterly point in the UK - first to see the sunrise.', 'sunset', lowestoft())

# Bury St Edmunds - The Nutshell
def bury():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(0, 110, 140, 140, '#d8c8a8') + windows(10, 124, 4, 3, 16, 18, 14, 14, WIN) + R(260, 110, 140, 140, '#e3d6be') + windows(270, 124, 4, 3, 16, 18, 14, 14, WIN)
    b += R(150, 150, 100, 100, '#efe6d2') + R(150, 140, 100, 12, '#2a6b3a') + T(200, 150, 'THE NUTSHELL', 10, '#ffffff', 'letter-spacing="1"')
    b += R(162, 166, 34, 40, '#a3c4dc') + R(208, 176, 26, 74, '#2a6b3a') + R(170, 210, 18, 6, '#5a3a22')
    b += R(0, 250, W, 70, '#aaa294') + crowd(8, 20, 380, 262, 1461, 1.05, 30)
    return b
add('Bury St Edmunds', 'The Nutshell', 'Britain\'s smallest pub - the bar room is about 15ft by 7ft.', 'day', bury())
