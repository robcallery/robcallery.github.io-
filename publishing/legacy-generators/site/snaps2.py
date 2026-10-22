from snaplib import *

S = {}
def add(city, title, note, sky, body, defs=''):
    slug = ''.join(ch for ch in city.lower() if ch.isalnum())
    S[city] = (title, note, scene(slug, sky, body, defs))

STONE = '#c9b48f'; GRIT = '#9c8a6c'; WIN = '#4a5878'

def gable_house(x, y, w, h, wall, roof='#5b4a44', win=WIN, door=None):
    g = R(x, y, w, h, wall) + P(f'M{x-3} {y} L{x+w/2} {y-h*.45} L{x+w+3} {y} Z', roof)
    g += windows(x + w * .15, y + h * .2, 2, 2, w * .22, h * .2, w * .26, h * .12, win)
    if door: g += R(x + w / 2 - 4, y + h - 13, 8, 13, door)
    return g

# Batley - Oakwell Hall
def batley():
    st = '#b8a07c'; dk = shade(st, -.18)
    b = sun(330, 60, 13) + cloud(90, 50, .8) + cloud(240, 70, .6)
    b += hills(200, '#8fb49a', 31, 12)
    b += R(70, 140, 260, 106, st)
    for x in (70, 160, 250):
        b += P(f'M{x} 140 L{x+40} 104 L{x+80} 140 Z', st) + P(f'M{x+40} 104 L{x+80} 140 L{x+40} 140 Z', dk)
        b += R(x + 30, 116, 20, 14, '#5a6680') + ''.join(L(x + 30 + i * 5, 116, x + 30 + i * 5, 130, st, 1) for i in range(1, 4))
    b += windows(84, 156, 6, 2, 30, 22, 11, 16, '#5a6680')
    for x in range(84, 330, 41):
        for y in (156, 194):
            b += L(x + 15, y, x + 15, y + 22, st, 1.2) + L(x, y + 11, x + 30, y + 11, st, 1)
    b += R(186, 214, 26, 32, '#5a3a22') + R(60, 132, 280, 4, dk)
    b += ground(246, '#5f8f55', '#79a86b') + R(150, 246, 100, 74, '#c9bc9c')
    b += tree(30, 250, 1.6) + tree(370, 252, 1.4) + flowers(0, 140, 252, 2, 26) + flowers(260, 400, 252, 3, 26)
    b += crowd(6, 150, 250, 270, 4, 1.05, 30)
    return b
add('Batley', 'Oakwell Hall', 'Elizabethan manor from 1583 - Charlotte Brontë wrote it into Shirley.', 'day', batley())

# Dewsbury - Minster
def dewsbury():
    st = '#a8937a'; dk = shade(st, -.2)
    b = cloud(100, 60, .9, '#eef2f6') + cloud(290, 40, .7, '#eef2f6')
    b += R(0, 200, W, 60, '#7d7468')
    for i, x in enumerate(range(0, 400, 50)):
        b += gable_house(x + 4, 170 + (i % 2) * 8, 42, 40, ['#b8826a', '#a26f58', '#c09378'][i % 3], '#4b3d3a')
    b += R(60, 160, 200, 92, st) + P('M60 160 L160 132 L260 160 Z', dk) + windows(76, 178, 7, 1, 14, 34, 12.5, 0, WIN, arch=True)
    x = 260
    b += R(x, 92, 64, 160, st) + R(x + 48, 92, 16, 160, dk) + battlements(x, 92, 64, st, 5, 8)
    b += arch_win(x + 22, 112, 20, 44, WIN) + clockface(x + 32, 180, 10)
    for px in (x - 2, x + 60): b += R(px, 76, 6, 18, st) + spire(px + 3, 78, 8, 12, st)
    b += R(0, 252, W, 68, '#9e978a') + R(0, 252, W, 3, '#bab3a6')
    b += crowd(8, 40, 360, 268, 7, 1.05, 30)
    return b
add('Dewsbury', 'Dewsbury Minster', 'Black Tom tolls the Devil\'s Knell every Christmas Eve - once for every year since Christ was born.', 'grey', dewsbury())

# Huddersfield - railway station
def huddersfield():
    st = '#c7b089'; dk = shade(st, -.2)
    b = cloud(80, 50, .8) + cloud(320, 60, .9) + sun(200, 40, 11)
    b += R(10, 120, 380, 132, st) + R(10, 112, 380, 10, dk)
    b += windows(22, 136, 4, 2, 12, 22, 12, 22, WIN) + windows(306, 136, 4, 2, 12, 22, 7, 22, WIN)
    b += P('M120 98 L200 64 L280 98 Z', st) + P('M128 96 L200 70 L272 96 Z', dk) + R(116, 98, 168, 10, st)
    for i in range(8):
        x = 126 + i * 21
        b += R(x, 108, 10, 144, '#e3d3b0') + R(x + 7, 108, 3, 144, dk) + R(x - 2, 106, 14, 4, st) + R(x - 2, 248, 14, 4, st)
    b += R(140, 200, 120, 52, '#3e3a36') + windows(146, 206, 5, 1, 18, 40, 4.5, 0, '#e8c46a')
    b += T(200, 92, 'HUDDERSFIELD', 8, '#5a4a2c', 'letter-spacing="1"')
    b += R(0, 252, W, 68, '#a69d8c') + R(0, 252, W, 3, '#c3bba9')
    # statue on plinth (generic figure)
    b += R(60, 236, 18, 18, '#8a8a8a') + person(69, 236, '#5f7a6a', '#5f7a6a', 1.4)
    b += crowd(14, 100, 380, 266, 6, 1.05, 34)
    return b
add('Huddersfield', 'Huddersfield station', 'John Betjeman called it the most splendid station façade in England.', 'day', huddersfield())

# Sheffield - Town Hall
def sheffield():
    st = '#d6c19a'; dk = shade(st, -.18)
    b = cloud(90, 60, .8) + cloud(320, 70, .7) + sun(330, 40, 12)
    b += R(10, 140, 380, 112, st) + R(10, 132, 380, 10, dk)
    b += windows(22, 154, 9, 2, 12, 26, 11, 18, WIN, arch=True) + windows(232, 154, 7, 2, 12, 26, 11, 18, WIN, arch=True)
    x = 170
    b += R(x, 66, 60, 186, st) + R(x + 46, 66, 14, 186, dk) + windows(x + 12, 150, 2, 2, 14, 30, 8, 14, WIN, arch=True)
    b += clockface(x + 30, 100, 13) + R(x - 4, 58, 68, 10, dk)
    b += P(f'M{x+4} 58 L{x+30} 30 L{x+56} 58 Z', '#4f7f6f') + R(x + 26, 16, 8, 16, '#4f7f6f')
    b += person(x + 30, 16, '#3f6f5f', '#3f6f5f', 1.2) + L(x + 34, 2, x + 34, 12, '#3f6f5f', 1.5)  # Vulcan
    b += R(0, 252, W, 68, '#b4ac9c') + R(0, 252, W, 3, '#cfc8b8')
    b += E(80, 290, 46, 10, '#7fb0d9') + E(80, 290, 30, 5, '#bfe0f5')  # Peace Gardens fountains
    b += crowd(14, 120, 390, 266, 12, 1.05, 34)
    return b
add('Sheffield', 'Sheffield Town Hall', 'Vulcan, Roman god of fire and metalwork, stands on top of the tower - steel city.', 'day', sheffield())

# Morley - Town Hall
def morley():
    st = '#c4ae86'; dk = shade(st, -.2)
    b = cloud(80, 60, .9, '#eef2f6') + cloud(300, 50, .7, '#eef2f6')
    b += R(20, 130, 360, 122, st) + R(20, 124, 360, 8, dk)
    b += windows(32, 146, 7, 2, 14, 30, 8.5, 18, WIN, arch=True) + windows(242, 146, 6, 2, 14, 30, 8.5, 18, WIN, arch=True)
    for i in range(6):
        b += R(152 + i * 18, 150, 8, 102, '#e0d0ab')
    b += P('M140 130 L200 104 L260 130 Z', st)
    x = 176
    b += R(x, 50, 48, 80, st) + R(x + 36, 50, 12, 80, dk) + clockface(x + 24, 78, 12)
    b += R(x + 4, 30, 40, 20, st) + windows(x + 8, 34, 4, 1, 6, 12, 3.4, 0, WIN, arch=True)
    b += P(f'M{x+2} 30 Q{x+24} 4 {x+46} 30 Z', '#6f8f7f') + R(x + 23, 0, 2, 10, '#c9a227')
    b += R(0, 252, W, 68, '#a49b8a') + R(0, 252, W, 3, '#c0b8a6')
    b += crowd(10, 30, 370, 266, 21, 1.05, 34)
    return b
add('Morley', 'Morley Town Hall', 'Opened in 1895 and Grade I-listed - a proper Victorian show-off.', 'grey', morley())

# Harrogate - Royal Pump Room
def harrogate():
    st = '#e1d3b4'; dk = shade(st, -.16)
    b = sun(320, 60, 13) + cloud(90, 50, .8) + cloud(230, 80, .6)
    b += tree(40, 250, 2.2, '#4f8f50') + tree(370, 250, 2.4, '#4f8f50')
    b += P('M90 170 L200 140 L310 170 L310 250 L90 250 Z', st) + P('M200 140 L310 170 L310 250 L250 250 L250 158 Z', dk)
    b += windows(104, 184, 3, 1, 16, 44, 14, 0, WIN, arch=True) + windows(262, 184, 2, 1, 14, 44, 10, 0, WIN, arch=True)
    b += R(176, 196, 48, 54, '#e9ddc2') + arch_win(186, 200, 28, 50, '#5a3a22')
    b += P('M150 150 Q200 70 250 150 Z', '#7a9a8a') + P('M200 150 Q200 76 250 150 Z', '#6a8a7a') + R(146, 148, 108, 6, st)
    b += C(200, 92, 7, '#7a9a8a') + R(199, 74, 2, 12, '#c9a227')
    b += ground(250, '#5f8f55', '#79a86b') + R(0, 268, W, 52, '#bdb39f')
    b += flowers(0, 400, 252, 7, 40)
    b += crowd(8, 60, 340, 278, 13, 1.05, 30)
    return b
add('Harrogate', 'The Royal Pump Room', 'Built in 1842 over the sulphur well - Europe\'s strongest, and it smells like it.', 'day', harrogate())

# Boroughbridge - Devil's Arrows
def boroughbridge():
    b = sun(80, 70, 16, '#ffe9b0', '#ffc46a') + cloud(260, 60, .8) + cloud(340, 100, .5)
    b += hills(200, '#9ab98a', 41, 10, 4) + hills(222, '#7fa56f', 42, 8, 4)
    b += ground(240, '#6f9a5c', '#86ad6f')
    for x, h, w, lean in ((110, 150, 26, -2), (210, 120, 22, 3), (300, 135, 24, -1)):
        b += P(f'M{x-w/2} 250 L{x-w/2+3+lean} {250-h} Q{x+lean} {250-h-10} {x+w/2-2+lean} {250-h+4} L{x+w/2} 250 Z', '#8c7f70')
        b += P(f'M{x+2} 250 L{x+lean+3} {250-h-4} Q{x+w/2-2+lean} {250-h+2} {x+w/2-2+lean} {250-h+4} L{x+w/2} 250 Z', '#6f6458')
        for k in range(3): b += PL(f'M{x+lean-6+k*5} {255-h} L{x+lean-4+k*5} {268-h}', '#5f564c', 1.6)
        b += E(x, 251, w * .8, 4, '#3f6b3a', 'opacity=".5"')
    b += crowd(3, 140, 180, 262, 3, 1.05, 10)
    for x in (40, 360): b += P(f'M{x-8} 262 Q{x} 252 {x+10} 260 Q{x+12} 266 {x} 268 Q{x-10} 268 {x-8} 262 Z', '#f2efe6') + C(x + 11, 258, 3, '#2a2a2a')
    return b
add('Boroughbridge', 'The Devil\'s Arrows', 'Three Bronze Age standing stones - legend says the Devil threw them at Aldborough.', 'warm', boroughbridge())

# Thirsk - market place clock
def thirsk():
    b = sun(330, 55, 13) + cloud(90, 55, .8) + cloud(230, 40, .5)
    cols = ['#e7d8bc', '#c9a27e', '#f0e6d2', '#b88a68', '#ddd0b0', '#c4b08e']
    for i, x in enumerate(range(-10, 410, 60)):
        h = 70 + (i % 3) * 12
        b += R(x, 230 - h, 58, h, cols[i % 6]) + R(x - 2, 230 - h - 6, 62, 6, '#5b4a44')
        b += windows(x + 8, 230 - h + 12, 3, 2, 10, 14, 7, 10, '#4a5878') + R(x + 22, 212, 12, 18, '#6b3a2a')
    b += R(0, 230, W, 90, '#b9ae98') + ''.join(R(i * 40, 230, 2, 90, '#a99e88') for i in range(10))
    x = 200
    b += R(x - 14, 130, 28, 110, '#b59a72') + R(x + 6, 130, 8, 110, shade('#b59a72', -.2))
    b += R(x - 18, 110, 36, 22, '#c4a982') + clockface(x, 121, 8) + P(f'M{x-20} 110 L{x} 86 L{x+20} 110 Z', '#5b4a44')
    b += R(x - 1, 74, 2, 14, '#3b3b3b') + P(f'M{x+1} 76 L{x+12} 80 L{x+1} 84 Z', '#d22630')
    b += R(x - 20, 236, 40, 8, '#9a8466')
    for cx in (60, 320):
        b += R(cx - 30, 246, 60, 4, '#d22630') + R(cx - 28, 250, 2, 24, '#555') + R(cx + 26, 250, 2, 24, '#555') + R(cx - 30, 238, 60, 9, '#f7f2e4') + ''.join(R(cx - 30 + i * 12, 238, 6, 9, '#2a8a46') for i in range(5))
    b += crowd(14, 20, 380, 270, 33, 1.05, 34)
    return b
add('Thirsk', 'Thirsk Market Place', 'James Herriot\'s vet practice was just round the corner on Kirkgate.', 'day', thirsk())

# Northallerton - town hall & high street
def northallerton():
    b = cloud(100, 50, .9, '#eef2f6') + cloud(300, 70, .7, '#eef2f6')
    cols = ['#e3d6be', '#b98b6a', '#efe6d4', '#a77a5c', '#d8c8a8']
    for i, x in enumerate(list(range(-20, 120, 46)) + list(range(270, 420, 46))):
        h = 80 + (i % 3) * 10
        b += R(x, 230 - h, 44, h, cols[i % 5]) + P(f'M{x-2} {230-h} L{x+22} {230-h-16} L{x+46} {230-h} Z', '#4b3d3a') + windows(x + 7, 230 - h + 12, 2, 2, 12, 14, 6, 12, '#4a5878')
    st = '#c8b494'
    b += R(130, 120, 140, 110, st) + R(130, 112, 140, 10, shade(st, -.2)) + windows(144, 130, 5, 2, 16, 24, 9, 16, '#4a5878', arch=True)
    b += P('M150 112 L200 82 L250 112 Z', st) + clockface(200, 102, 8) + R(190, 196, 20, 34, '#5a3a22')
    b += R(0, 230, W, 90, '#9e978a') + R(0, 230, W, 2, '#bab3a6')
    for x in (40, 110, 290, 360):
        b += R(x - 22, 244, 44, 4, '#1d4ed8') + R(x - 22, 236, 44, 9, '#f7f2e4') + R(x - 20, 248, 2, 20, '#555') + R(x + 18, 248, 2, 20, '#555')
    b += crowd(16, 10, 390, 266, 44, 1.05, 34)
    return b
add('Northallerton', 'The High Street', 'Market days are Wednesdays and Saturdays, all the way down the high street.', 'grey', northallerton())

# Wetherby - bridge & weir
def wetherby():
    st = '#c2ab84'; dk = shade(st, -.2)
    b = sun(80, 60, 13) + cloud(260, 50, .8) + cloud(350, 80, .5)
    b += tree(30, 180, 2) + tree(80, 176, 1.6) + tree(330, 178, 2.2) + tree(380, 182, 1.8)
    for i, x in enumerate(range(120, 300, 44)):
        b += gable_house(x, 128 - (i % 2) * 6, 40, 34, ['#e3d6be', '#c9a27e', '#efe6d4', '#b88a68'][i % 4], '#4b3d3a')
    b += R(0, 160, W, 18, st) + R(0, 156, W, 5, dk)
    for i in range(4):
        x = 20 + i * 100
        b += P(f'M{x} 178 L{x} 190 A40 40 0 0 1 {x+80} 190 L{x+80} 178 Z', 'none') + R(x + 80, 178, 20, 40, st)
    b += R(0, 176, W, 44, '#4f8a9a') + R(0, 176, W, 8, '#6a8f5a')
    b += P('M0 178 L0 218 L20 218 L20 190 A40 40 0 0 1 100 190 L100 218 L120 218 L120 190 A40 40 0 0 1 200 190 L200 218 L220 218 L220 190 A40 40 0 0 1 300 190 L300 218 L320 218 L320 190 A40 40 0 0 1 400 190 L400 178 Z', st)
    b += water(218, '#4f8a9a', 8, 16)
    b += P('M0 248 Q200 236 400 248 L400 258 Q200 246 0 258 Z', '#e9f4f7') + ''.join(PL(f'M{x} 254 l3 10', '#ffffff', 1.4, 'opacity=".7"') for x in range(6, 400, 12))
    b += E(320, 284, 8, 4, '#f7f7f7') + C(326, 279, 3, '#f7f7f7') + P('M328 279 l5 1 l-5 1 z', '#f07a14')  # swan
    b += E(120, 296, 8, 4, '#f7f7f7') + C(126, 291, 3, '#f7f7f7') + P('M128 291 l5 1 l-5 1 z', '#f07a14')
    return b
add('Wetherby', 'Wetherby Bridge', 'Walk down to the riverside below the bridge for the weir and the swans.', 'day', wetherby())

# Bingley - Five Rise Locks
def bingley():
    st = '#9f8c6c'; dk = shade(st, -.22)
    b = sun(330, 50, 13) + cloud(90, 40, .8) + cloud(220, 70, .5)
    b += hills(150, '#7da57a', 51, 14) + tree(40, 150, 1.4, '#3f7f45') + tree(370, 152, 1.6, '#3f7f45')
    for i in range(5):
        x = 20 + i * 76; y = 120 + i * 30
        b += R(x, y, 80, 200, st) + R(x, y, 80, 4, dk)
        b += R(x + 6, y + 6, 66, 24, '#4f7f9a') + R(x + 6, y + 6, 66, 3, '#7fb0d9')
        b += R(x + 68, y - 4, 6, 36, '#2a2a2a') + R(x + 74, y - 4, 22, 4, '#f7f2e4') + R(x + 92, y - 4, 4, 4, '#2a2a2a')
    b += ground(290, '#5f8f55')
    b += P('M290 274 L370 274 L376 286 L284 286 Z', '#2a6b3a') + R(300, 266, 50, 9, '#d22630') + R(304, 268, 42, 5, '#ffcd00') + windows(306, 268, 5, 1, 5, 4, 3, 0, '#2a2a2a')
    b += crowd(4, 30, 200, 152, 51, 1.05, 70)
    return b
add('Bingley', 'Bingley Five Rise Locks', 'The steepest staircase locks in Britain - five chambers, 18 metres up, opened 1774.', 'day', bingley())

# Halifax - Piece Hall
def halifax():
    st = '#d6c39f'; dk = shade(st, -.2)
    b = sun(340, 40, 12) + cloud(80, 40, .7) + cloud(220, 30, .5)
    b += hills(90, '#7f9f7a', 61, 10)
    b += R(0, 100, W, 150, st)
    for r, (y, h) in enumerate(((104, 40), (150, 40), (196, 44))):
        b += R(0, y + h, W, 5, dk)
        for i in range(20):
            x = 4 + i * 20
            b += (arch_win(x, y + 4, 12, h - 6, '#4a5068') if r < 2 else R(x, y + 8, 12, h - 8, '#4a5068'))
            b += R(x + 14, y + 2, 4, h, '#e8d9b8')
    b += R(0, 240, W, 80, '#cfc2a4') + ''.join(L(0, 240 + k * 10, W, 240 + k * 10, '#bfb294', 1) for k in range(1, 8))
    b += crowd(30, 10, 390, 256, 61, 1.05, 50)
    return b
add('Halifax', 'The Piece Hall', 'A 1779 Georgian cloth hall with 315 rooms round one huge square.', 'day', halifax())

# Ripon - Cathedral
def ripon():
    st = '#d2c09c'; dk = shade(st, -.18)
    b = moon(330, 50, 11) + stars(71, 20, 90) + cloud(110, 60, .7, '#c9c0d8', .5)
    b += R(100, 120, 200, 140, st) + P('M100 120 L200 96 L300 120 Z', dk)
    b += arch_win(150, 140, 22, 70, '#e8c46a') + arch_win(189, 140, 22, 70, '#e8c46a') + arch_win(228, 140, 22, 70, '#e8c46a')
    b += arch_win(186, 220, 28, 40, '#3b2a1a')
    for x in (40, 300):
        b += R(x, 90, 60, 170, st) + R(x + 46, 90, 14, 170, dk) + battlements(x, 90, 60, st, 5, 8)
        b += windows(x + 12, 110, 2, 3, 12, 30, 12, 14, '#e8c46a', arch=True)
    b += R(0, 260, W, 60, '#7d776c') + R(0, 260, W, 2, '#99938a')
    # hornblower
    b += person(200, 292, '#1b1b1b', SKIN[0], 1.6) + P('M200 270 l10 -6 l2 2 l-10 6 z', '#c9a227') + P('M194 270 L206 270 L200 264 Z', '#1b1b1b')
    return b
add('Ripon', 'Ripon Cathedral', 'The Hornblower sets the watch at 9pm every night - a tradition going back over 1,100 years.', 'dusk', ripon())

# Masham - brewery town
def masham():
    b = sun(70, 60, 13) + cloud(240, 50, .8) + cloud(340, 80, .5)
    b += hills(170, '#9ab98a', 81, 12)
    st = '#c7b08a'
    b += R(150, 110, 150, 130, st) + P('M146 110 L225 82 L304 110 Z', '#4b3d3a') + windows(162, 126, 6, 3, 14, 18, 9.5, 14, '#4a5878')
    b += R(126, 50, 20, 190, '#9a5a3c') + R(122, 46, 28, 6, '#7a4a2c')
    b += R(170, 196, 40, 44, '#3b2a1a') + T(225, 104, 'BREWERY', 10, '#f7f2e4', 'letter-spacing="2"')
    for i in range(4): b += E(230 + i * 16, 230, 7, 9, '#8a5a32') + R(223 + i * 16, 222, 14, 2, '#3b3b3b') + R(223 + i * 16, 236, 14, 2, '#3b3b3b')
    b += gable_house(20, 170, 70, 70, '#e3d6be', '#4b3d3a', door='#2a6b3a') + gable_house(320, 176, 70, 64, '#d8c8a8', '#4b3d3a', door='#1d4ed8')
    b += ground(240, '#6f9a5c', '#86ad6f')
    for x, y in ((60, 270), (110, 284), (300, 276), (350, 290), (200, 296)):
        b += E(x, y, 12, 8, '#2a2a2a') + C(x + 13, y - 3, 4.5, '#1b1b1b') + R(x - 7, y + 5, 2, 6, '#1b1b1b') + R(x + 5, y + 5, 2, 6, '#1b1b1b')
    return b
add('Masham', 'Masham', 'One small town, two famous breweries - Theakston since 1827 and Black Sheep since 1992.', 'day', masham())

# Pateley Bridge
def pateley():
    b = sun(330, 50, 12) + cloud(100, 40, .8)
    b += hills(110, '#8aa77a', 91, 20) + hills(140, '#6f9a5c', 92, 16)
    for i in range(6):
        b += L(0, 150 + i * 14, W, 140 + i * 16, '#9a9180', 1.5, 'opacity=".6"')
    cols = ['#cdbb98', '#b9a37e', '#d8c8a8', '#c4ac86']
    for i in range(8):
        x = 120 + i * 30; y = 120 + i * 14
        b += R(x, y, 34, 40, cols[i % 4]) + P(f'M{x-2} {y} L{x+17} {y-10} L{x+36} {y} Z', '#5b5450') + R(x + 6, y + 10, 8, 10, '#4a5878')
    b += R(100, 230, 120, 30, '#f0e6d2') + R(100, 230, 120, 8, '#e84a7f') + T(160, 237, 'SWEET SHOP', 7, '#fff', 'letter-spacing="1"')
    b += windows(108, 242, 4, 1, 22, 16, 6, 0, '#bfe0f5') + ''.join(C(116 + i * 28, 254, 3, c) for i, c in enumerate(('#e84a7f', '#ffcd00', '#7c3aed', '#2a8a46')))
    b += R(0, 260, W, 60, '#a69d8c')
    b += crowd(10, 20, 380, 272, 92, 1.05, 30)
    return b
add('Pateley Bridge', 'Pateley Bridge', 'Home to the oldest sweet shop in England, trading since 1827.', 'day', pateley())

# Malton - Castle Howard
def malton():
    st = '#d8c49c'; dk = shade(st, -.2)
    b = sun(340, 60, 13) + cloud(80, 50, .8) + cloud(250, 40, .6)
    b += tree(20, 210, 2) + tree(380, 210, 2.2)
    b += R(40, 140, 320, 90, st) + R(40, 132, 320, 10, dk) + windows(52, 150, 14, 2, 10, 24, 11.6, 14, '#4a5878', arch=True)
    for i in range(6): b += R(150 + i * 18, 140, 8, 90, '#ecdcb8')
    b += P('M140 132 L200 112 L260 132 Z', st)
    b += R(170, 70, 60, 50, st) + P('M170 72 Q200 18 230 72 Z', '#c9a24a') + P('M200 72 Q200 22 230 72 Z', '#b08a3a') + R(194, 16, 12, 18, st) + C(200, 14, 5, '#c9a24a')
    b += windows(176, 84, 3, 1, 10, 24, 9, 0, '#4a5878', arch=True)
    b += water(230, '#4f8aa8', 81, 10)
    b += R(150, 244, 100, 10, '#d8c49c') + E(200, 244, 14, 8, '#d8c49c') + C(200, 236, 4, '#e6f4fb')
    return b
add('Malton', 'Castle Howard', 'Six miles out of Malton - Brideshead Revisited was filmed here.', 'day', malton())
