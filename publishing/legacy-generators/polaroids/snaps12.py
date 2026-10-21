from snaplib import *
from snaps10 import cathedral, stadium, stone_castle
from snaps11 import pier, seaside, terrace
from snaps7 import lighthouse
import random

S = {}
def add(city, title, note, sky, body, defs=''):
    slug = ''.join(ch for ch in city.lower() if ch.isalnum())
    S[city] = (title, note, scene(slug, sky, body, defs))
WIN = '#4a5878'

def onion(x, base, w, h, f):
    return P(f'M{x-w/2} {base} Q{x-w/2-4} {base-h*.5} {x} {base-h} Q{x+w/2+4} {base-h*.5} {x+w/2} {base} Z', f) + R(x - 1, base - h - 10, 2, 10, '#c9a227')

# Brighton - Royal Pavilion
def brighton():
    st = '#f2e6cc'
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(40, 150, 320, 90, st) + windows(52, 170, 13, 1, 12, 40, 11.6, 0, WIN, arch=True)
    b += onion(200, 150, 90, 100, '#f4ead4') + onion(90, 150, 40, 50, '#f4ead4') + onion(310, 150, 40, 50, '#f4ead4')
    for x in (60, 130, 270, 340): b += R(x - 3, 110, 6, 40, st) + onion(x, 112, 10, 16, st)
    b += ground(240, '#5f9a50', '#7ab36a') + palm(20, 250, 1, 4) + tree(380, 250, 1.6) + crowd(10, 40, 360, 262, 1501, 1.05, 30)
    return b
add('Brighton and Hove', 'The Royal Pavilion', 'Built for the Prince Regent (George IV) as an Indian-style seaside palace.', 'day', brighton())

# Milton Keynes - concrete cows
def mk():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += hills(190, '#8fb07a', 1511, 8) + ground(210, '#6fa85a', '#86b86f')
    for x, y, s in ((90, 250, 1.3), (200, 270, 1.6), (310, 246, 1.2)):
        g = E(0, 0, 26, 14, '#b9b5ac') + R(-20, 8, 5, 18, '#a9a59c') + R(14, 8, 5, 18, '#a9a59c') + P('M22 -6 L40 -14 L44 2 L30 8 Z', '#b9b5ac') + E(-6, -2, 7, 5, '#5a5a5a') + E(10, 4, 6, 4, '#5a5a5a')
        b += f'<g transform="translate({x} {y}) scale({s})">{g}</g>'
    b += tree(30, 214, 1.8) + tree(380, 214, 1.8)
    return b
add('Milton Keynes', 'The concrete cows', 'Made in 1978 by artist Liz Leyh - Milton Keynes\' unofficial mascots.', 'day', mk())

# Southampton - Bargate
def southampton():
    st = '#b9a68a'; dk = shade(st, -.2)
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(100, 80, 200, 170, st) + battlements(100, 80, 200, st, 4, 7)
    for x in (100, 270): b += R(x - 10, 70, 40, 180, st) + R(x + 22, 70, 8, 180, dk) + battlements(x - 10, 70, 40, st, 3, 6)
    b += arch_win(170, 170, 60, 80, '#3b2a1a') + windows(150, 100, 4, 1, 12, 24, 22, 0, WIN, arch=True)
    b += R(0, 250, W, 70, '#aaa294') + crowd(10, 20, 380, 262, 1521, 1.05, 30)
    return b
add('Southampton', 'The Bargate', 'The medieval gateway into the old town - Titanic sailed from Southampton in 1912.', 'day', southampton())

# Portsmouth - Spinnaker Tower
def portsmouth():
    b = sun(70, 50, 12) + cloud(280, 40, .8)
    x = 220
    b += P(f'M{x-50} 250 Q{x-60} 120 {x+10} 20 Q{x-30} 120 {x-20} 250 Z', '#f4f4f4') + P(f'M{x+40} 250 Q{x+40} 140 {x+10} 20 Q{x+20} 140 {x+20} 250 Z', '#e6e9ef')
    b += P(f'M{x-30} 80 L{x+30} 80 L{x+26} 100 L{x-26} 100 Z', '#7fa8c8') + R(x - 20, 60, 34, 20, '#a3c4dc')
    b += water(230, '#3f6f8a', 1531, 16) + R(0, 226, W, 6, '#8a8475')
    b += P('M20 268 L150 268 L140 286 L30 286 Z', '#5a6670') + R(40, 254, 60, 14, '#8a96a0') + R(70, 236, 6, 18, '#5a6670')
    return b
add('Portsmouth', 'The Spinnaker Tower', '170 metres tall, shaped like a sail - stand on the glass floor if you dare.', 'day', portsmouth())

# Reading - Forbury lion
def reading():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(260, 120, 120, 120, '#9a8a7a') + ''.join(arch_win(270 + k * 34, 140, 20, 50, '#7a9a7a') for k in range(3))
    b += ground(230, '#5f9a50', '#7ab36a') + tree(40, 234, 2) + tree(380, 236, 1.6)
    b += R(110, 190, 120, 50, '#9a9a94')
    b += P('M120 190 L120 150 Q140 130 170 140 L210 140 Q226 144 226 160 L226 190 Z', '#5a5a52') + C(132, 142, 18, '#4a4a42') + P('M210 140 Q236 120 230 100', 'none', 'stroke="#5a5a52" stroke-width="4"')
    return b
add('Reading', 'The Maiwand Lion', 'One of the biggest cast-iron lions in the world, in the Forbury Gardens since 1886.', 'day', reading())

# Slough - Herschel's telescope & Windsor
def slough():
    b = moon(80, 50, 12) + stars(1551, 50, 140)
    b += R(260, 150, 120, 80, '#8a8478') + battlements(260, 150, 120, '#8a8478', 4, 6) + R(300, 110, 40, 120, '#8a8478') + battlements(300, 110, 40, '#8a8478', 3, 6)
    b += ground(230, '#2f4a3a') + P('M80 230 L180 90 L190 96 L96 236 Z', '#c9a27a') + L(120, 230, 150, 140, '#5a3a22', 2) + L(160, 230, 150, 140, '#5a3a22', 2)
    b += C(185, 92, 8, '#3a3a40')
    return b
add('Slough', 'Herschel\'s telescope', 'William Herschel built his giant 40ft telescope in Slough - and found new moons of Saturn.', 'night', slough())

# Oxford - Radcliffe Camera
def oxford():
    st = '#e3d2a8'; dk = shade(st, -.16)
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(0, 120, 80, 130, st) + R(320, 110, 80, 140, st) + windows(10, 140, 3, 3, 12, 18, 10, 14, WIN, arch=True) + windows(330, 130, 3, 3, 12, 18, 10, 14, WIN, arch=True)
    b += R(110, 160, 180, 90, st) + R(120, 150, 160, 12, dk)
    for i in range(8): b += R(118 + i * 22, 162, 6, 88, '#f0e2c0')
    b += R(140, 110, 120, 42, st) + windows(150, 118, 6, 1, 8, 24, 10, 0, WIN, arch=True)
    b += P('M136 112 Q200 30 264 112 Z', '#8a9a8a') + P('M200 112 Q200 36 264 112 Z', '#7a8a7a') + R(192, 26, 16, 18, st) + C(200, 22, 6, '#8a9a8a')
    b += R(0, 250, W, 70, '#bdb39f') + crowd(10, 20, 380, 262, 1561, 1.05, 30)
    return b
add('Oxford', 'The Radcliffe Camera', 'Tolkien and C.S. Lewis\'s Inklings met over pints at Oxford pubs.', 'day', oxford())

# Woking - tripod
def woking():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += terrace(240, 1571, 8, 52, 60, 90)
    x = 200
    b += L(x, 90, x - 60, 250, '#a3aab5', 5) + L(x, 90, x + 60, 250, '#a3aab5', 5) + L(x, 90, x + 6, 250, '#a3aab5', 5)
    b += E(x, 84, 38, 18, '#c9ced8') + E(x, 90, 30, 6, '#8a929e') + C(x + 20, 82, 5, '#ff4d4d')
    b += PL(f'M{x-30} 90 Q{x-60} 110 {x-70} 140', '#a3aab5', 2) + PL(f'M{x+30} 90 Q{x+60} 110 {x+64} 140', '#a3aab5', 2)
    b += R(0, 240, W, 80, '#aaa294') + crowd(10, 20, 380, 254, 1572, 1.05, 30)
    return b
add('Woking', 'The Martian', 'H.G. Wells had the Martians land on Horsell Common in The War of the Worlds.', 'day', woking())

# Guildford - High Street clock
def guildford():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += P('M0 320 L120 120 L280 120 L400 320 Z', '#b9b1a1') + ''.join(PL(f'M{120-k*10} {120+k*20} L{280+k*10} {120+k*20}', '#a39b8b', 1) for k in range(10))
    for side, xs in (('l', (0, 40, 80)), ('r', (280, 320, 360))):
        for i, x in enumerate(xs):
            b += R(x, 60 + i * 10, 40, 200, ['#e3d6be', '#c9a27e', '#efe6d2'][i]) + windows(x + 6, 74 + i * 10, 2, 5, 10, 14, 8, 12, WIN)
    b += R(150, 50, 100, 60, '#efe6d2') + R(146, 44, 108, 8, '#5b4a44') + windows(160, 64, 4, 1, 14, 30, 10, 0, WIN, arch=True)
    b += R(240, 70, 50, 6, '#2a2a2a') + C(292, 74, 16, '#2a2a2a') + clockface(292, 74, 12, '#f4f1ea', '#c9a227')
    b += crowd(12, 120, 280, 230, 1581, 1.05, 50)
    return b
add('Guildford', 'The Guildhall clock', 'The clock has hung out over the cobbled High Street since 1683.', 'day', guildford())

# Crawley - Gatwick
def crawley():
    b = sun(70, 50, 12) + cloud(280, 40, .8)
    b += R(0, 190, W, 40, '#dfe3ea') + windows(10, 198, 14, 1, 16, 18, 11, 0, '#7fb0d9')
    b += R(0, 230, W, 90, '#4b505c') + ''.join(R(10 + i * 50, 274, 26, 3, '#f7f2e4') for i in range(8))
    b += plane(220, 120, 1.6, '#ffffff', '#f07a14') + plane(100, 250, 1.1, '#ffffff', '#1d4ed8')
    return b
add('Crawley', 'Gatwick on the doorstep', 'Gatwick is the UK\'s second busiest airport - and it\'s in Crawley.', 'day', crawley())

# Worthing - pier
def worthing():
    b = seaside(1601)
    b += pier(214, 320, '#e6e9ef')
    b += R(250, 150, 80, 30, '#f4f1ea') + E(290, 150, 40, 8, '#9ac4dc') + R(200, 156, 40, 22, '#f4f1ea')
    b += crowd(12, 20, 380, 240, 1602, 1.05, 50)
    return b
add('Worthing', 'Worthing Pier', 'Its art deco pavilions helped it win Pier of the Year.', 'day', worthing())

# Eastbourne - Beachy Head
def eastbourne():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += water(160, '#3f86b5', 1611, 18)
    b += P('M-10 120 L240 110 L260 260 L-10 260 Z', '#f4f4ec') + P('M-10 120 L240 110 L240 118 L-10 130 Z', '#6fa85a')
    for k in range(6): b += L(40 + k * 36, 130, 46 + k * 38, 250, '#e3e3da', 2)
    b += lighthouse(320, 260, 90, '#f4f1ea', '#d22630', 1.3)
    b += R(240, 258, 170, 62, '#8a8a7a') + water(270, '#3f86b5', 1612, 10)
    return b
add('Eastbourne', 'Beachy Head', 'Britain\'s highest chalk sea cliff, with the red-and-white lighthouse below.', 'day', eastbourne())

# Hastings - net huts
def hastings():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += P('M-10 200 Q100 100 200 120 L200 200 Z', '#6fa85a') + L(120, 200, 170, 120, '#5a5a5a', 3) + R(140, 150, 14, 10, '#d22630')
    for i, x in enumerate(range(160, 400, 36)):
        h = 110 + (i % 3) * 20
        b += R(x, 250 - h, 30, h, '#1b1b1b') + P(f'M{x-2} {250-h} L{x+15} {250-h-14} L{x+32} {250-h} Z', '#1b1b1b') + R(x + 10, 230, 10, 20, '#3a3a3a')
    b += R(0, 250, W, 70, '#b9b1a1') + P('M20 280 L100 280 L94 296 L26 296 Z', '#1d4ed8') + R(46, 268, 20, 12, '#f4f1ea')
    return b
add('Hastings', 'The net huts', 'The tall black huts on the Stade were built to dry fishing nets - the fleet still launches off the beach.', 'day', hastings())

# Basingstoke - Jane Austen statue
def basingstoke():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += terrace(230, 1641, 8, 52, 80, 110)
    b += R(0, 230, W, 90, '#aaa294')
    x = 200
    b += R(x - 20, 230, 40, 30, '#8a8a8a') + P(f'M{x-18} 230 L{x-8} 168 L{x+8} 168 L{x+18} 230 Z', '#6a6a62') + C(x, 158, 9, '#6a6a62') + P(f'M{x-10} 154 Q{x} 140 {x+10} 154 Z', '#6a6a62')
    b += crowd(10, 20, 380, 270, 1642, 1.05, 30)
    return b
add('Basingstoke', 'Jane Austen', 'Austen grew up at Steventon, just outside town - her statue stands in Market Place.', 'day', basingstoke())

# Aldershot - Wellington statue
def aldershot():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += hills(200, '#6fa85a', 1651, 10) + ground(230, '#5f9a50', '#7ab36a')
    x = 200
    b += R(x - 40, 180, 80, 50, '#9a9a94')
    b += E(x, 150, 40, 18, '#4a4a42') + P(f'M{x+30} 146 L{x+50} 116 L{x+58} 120 L{x+44} 152 Z', '#4a4a42') + C(x + 56, 112, 7, '#4a4a42')
    for dx in (-26, -10, 14, 28): b += R(x + dx, 160, 6, 22, '#4a4a42')
    b += R(x - 6, 110, 14, 30, '#3a3a32') + C(x + 1, 104, 7, '#3a3a32') + P(f'M{x-8} 98 L{x+10} 98 L{x+1} 90 Z', '#3a3a32')
    return b
add('Aldershot', 'The Wellington Statue', 'It stood on Hyde Park Corner in London until 1883, then moved to the home of the British Army.', 'day', aldershot())

# Farnborough - jets
def farnborough():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    for i, (x, y, c) in enumerate(((120, 100, '#d22630'), (170, 80, '#ffffff'), (220, 100, '#1d4ed8'))):
        b += PL(f'M{x-120} {y+40} Q{x-60} {y+10} {x-12} {y}', c, 8, 'opacity=".75" stroke-linecap="round"')
        b += f'<g transform="translate({x} {y}) scale(.6)">' + P('M-30 0 L30 -3 L36 0 L30 3 Z', '#d22630') + P('M-6 0 L-20 -18 L-12 -18 L8 0 Z M-6 0 L-20 18 L-12 18 L8 0 Z', '#d22630') + '</g>'
    b += R(0, 220, W, 100, '#6fa85a') + R(0, 260, W, 20, '#4b505c')
    b += crowd(20, 10, 390, 240, 1661, 1.05, 20)
    return b
add('Farnborough', 'Farnborough Airshow', 'Samuel Cody made the first powered flight in Britain here in 1908.', 'day', farnborough())

# Fareham - Portchester Castle
def fareham():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += stone_castle('#b3a58c')
    b += water(240, '#4f8ab5', 1671, 14)
    return b
add('Fareham', 'Portchester Castle', 'The castle sits inside a Roman fort - its walls are the most complete in northern Europe.', 'day', fareham())

# Gosport - submarine
def gosport():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(320, 60, 14, 170, '#f4f4f4') + P('M300 100 L360 100 L350 120 L310 120 Z', '#7fa8c8')
    b += water(200, '#3f6f8a', 1681, 16)
    b += P('M40 220 Q40 200 80 200 L280 200 Q300 200 300 220 Q300 236 280 236 L80 236 Q40 236 40 220 Z', '#2a2f3a') + R(140, 170, 50, 32, '#2a2f3a') + R(160, 150, 6, 22, '#2a2f3a')
    b += R(0, 260, W, 60, '#8a8475') + crowd(8, 20, 380, 270, 1682, 1.05, 30)
    return b
add('Gosport', 'HMS Alliance', 'The Submarine Museum lets you climb inside a real Cold War submarine.', 'day', gosport())

# Winchester - cathedral
def winchester():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    st = '#d6c39f'; dk = shade(st, -.18)
    b += R(10, 140, 380, 100, st) + P('M10 140 L200 118 L390 140 Z', '#5a6a6a') + windows(24, 156, 14, 1, 10, 40, 16, 0, WIN, arch=True)
    b += R(160, 90, 80, 50, st) + battlements(160, 90, 80, st, 4, 6)
    b += ground(240, '#5f9a50', '#7ab36a') + tree(20, 244, 1.6) + tree(380, 244, 1.6)
    return b
add('Winchester', 'Winchester Cathedral', 'The longest medieval cathedral in Europe - and Jane Austen is buried inside.', 'day', winchester())

# Canterbury - cathedral
def canterbury():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += cathedral('#d8c8a0', 0, True, 1701)
    for x in (60, 110, 290, 340): b += spire(x, 72, 8, 20, '#d8c8a0')
    b += R(0, 250, W, 70, '#aaa294') + crowd(10, 20, 380, 262, 1702, 1.05, 30)
    return b
add('Canterbury', 'Canterbury Cathedral', 'Thomas Becket was murdered here in 1170 - pilgrims have come ever since.', 'day', canterbury())

# Maidstone - Leeds Castle
def maidstone():
    st = '#d8c8a8'; dk = shade(st, -.18)
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += hills(150, '#6fa85a', 1711, 10) + tree(30, 170, 2) + tree(380, 170, 2.2)
    b += R(90, 110, 220, 80, st) + battlements(90, 110, 220, st, 4, 6) + windows(104, 126, 9, 2, 12, 18, 10, 14, WIN, arch=True)
    b += R(130, 80, 60, 40, st) + battlements(130, 80, 60, st, 3, 5) + R(250, 90, 40, 30, st) + P('M246 90 L270 70 L294 90 Z', '#6b5a50')
    b += water(190, '#4f7f9a', 1712, 16)
    b += P('M110 192 L290 192 L300 206 L100 206 Z', st, 'opacity=".35"')
    b += E(80, 260, 9, 4, '#1b1b1b') + C(87, 255, 3, '#1b1b1b') + P('M89 255 l5 1 l-5 1 z', '#d22630')
    return b
add('Maidstone', 'Leeds Castle', 'Not in Leeds at all - it\'s just outside Maidstone. Called "the loveliest castle in the world".', 'day', maidstone())

# Ashford - WWI tank
def ashford():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += terrace(220, 1721, 8, 52, 80, 110) + R(0, 220, W, 100, '#aaa294')
    x = 200
    b += P(f'M{x-90} 250 L{x-70} 190 L{x+70} 190 L{x+90} 250 Z', '#5a6a4a') + P(f'M{x-90} 250 Q{x-100} 220 {x-70} 190 L{x-60} 196 Q{x-84} 222 {x-76} 246 Z', '#4a5a3a')
    b += R(x - 30, 170, 60, 22, '#5a6a4a') + R(x + 30, 178, 30, 6, '#3a3a32')
    for k in range(8): b += C(x - 70 + k * 20, 242, 6, '#3a3a32')
    b += R(x - 100, 250, 200, 10, '#8a8a8a')
    return b
add('Ashford', 'The Ashford tank', 'A First World War tank given to the town in 1919 for its war savings.', 'day', ashford())

# Dover - white cliffs & castle
def dover():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += water(200, '#3f86b5', 1731, 18)
    b += P('M-10 120 L180 100 L280 120 L410 160 L410 220 L-10 220 Z', '#f4f4ec') + P('M-10 120 L180 100 L280 120 L410 160 L410 168 L280 128 L180 108 L-10 128 Z', '#6fa85a')
    for k in range(10): b += L(20 + k * 38, 126, 24 + k * 38, 216, '#e3e3da', 2)
    b += R(80, 70, 60, 34, '#b3a58c') + battlements(80, 70, 60, '#b3a58c', 3, 5)
    b += P('M200 262 L360 262 L348 282 L212 282 Z', '#f4f4f4') + R(230, 240, 100, 22, '#1d3a8f') + R(300, 226, 14, 14, '#d22630')
    return b
add('Dover', 'The White Cliffs', 'On a clear day you can see France - it\'s only 21 miles away.', 'day', dover())

# Folkestone - Harbour Arm
def folkestone():
    b = sun(320, 210, 20, '#ffd27a', '#ff9e5a') + cloud(90, 60, .8, '#ffe1c7')
    b += water(180, '#3f6f9a', 1741, 18)
    b += P('M-10 200 L300 170 L310 176 L-10 210 Z', '#8a8475') + lighthouse(306, 172, 40, '#f4f1ea', '#2a2a2a', 1)
    for k in range(6): b += R(30 + k * 40, 186 - k * 4, 26, 12, ['#d22630', '#ffcd00', '#1d4ed8', '#2a8a46', '#e84a7f', '#f07a14'][k])
    b += P('M-10 240 Q200 226 410 236 L410 320 L-10 320 Z', '#cdbb98') + crowd(10, 20, 380, 254, 1742, 1.05, 40)
    return b
add('Folkestone', 'The Harbour Arm', 'The old ferry pier is now food stalls and bars, with a lighthouse at the end.', 'sunset', folkestone())

# Margate - Dreamland
def margate():
    b = sun(320, 60, 14) + cloud(90, 50, .8)
    b += R(20, 90, 150, 60, '#f4f1ea') + T(95, 132, 'DREAMLAND', 22, '#d22630', 'textLength="130" lengthAdjust="spacingAndGlyphs"')
    b += R(80, 150, 30, 60, '#f4f1ea')
    b += PL('M180 210 Q220 120 260 190 Q300 250 340 150 Q370 100 400 200', '#c9a27a', 5)
    for x in (200, 240, 280, 320, 360): b += L(x, 210, x, 150 + (x % 60), '#a88a5a', 2)
    b += R(0, 210, W, 20, '#e6e9ef') + P('M-10 230 Q200 220 410 228 L410 320 L-10 320 Z', '#ecd9a8') + crowd(12, 20, 380, 246, 1751, 1.05, 50)
    return b
add('Margate', 'Dreamland', 'Its wooden Scenic Railway from 1920 is the oldest rollercoaster in the UK.', 'day', margate())
