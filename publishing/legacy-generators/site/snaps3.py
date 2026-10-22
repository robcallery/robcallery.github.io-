from snaplib import *

S = {}
def add(city, title, note, sky, body, defs=''):
    slug = ''.join(ch for ch in city.lower() if ch.isalnum())
    S[city] = (title, note, scene(slug, sky, body, defs))

WIN = '#4a5878'

def train(x, y, n=4, body='#7a1f2b', s=1.0):
    g = ''
    for i in range(n):
        cx = x + i * 46 * s
        g += R(cx, y - 18 * s, 44 * s, 16 * s, body, 3) + windows(cx + 4 * s, y - 15 * s, 5, 1, 5 * s, 5 * s, 3 * s, 0, '#cfe3f2') + C(cx + 8 * s, y - 1 * s, 2.4 * s, '#222') + C(cx + 36 * s, y - 1 * s, 2.4 * s, '#222')
    return g

# Settle - Ribblehead Viaduct
def settle():
    st = '#8f8475'; dk = shade(st, -.2)
    b = cloud(90, 50, .9, '#eef2f6') + cloud(300, 70, .8, '#eef2f6')
    b += hills(120, '#7f9a6f', 101, 26, 3) + hills(170, '#a3b07f', 102, 10)
    b += R(0, 120, W, 12, st)
    for i in range(9):
        x = -10 + i * 48
        b += R(x, 132, 12, 140, st) + R(x + 9, 132, 3, 140, dk) + P(f'M{x+12} 132 L{x+12} 140 A18 18 0 0 1 {x+48} 140 L{x+48} 132 Z', st)
    b += train(40, 120, 5, '#7a1f2b', .9)
    b += ground(262, '#8a9a5c', '#a3b07f') + flowers(0, 400, 264, 5, 12, ('#ffffff',))
    for x, y in ((80, 292), (300, 286)):
        b += E(x, y, 10, 7, '#f2efe6') + C(x + 11, y - 3, 3.5, '#2a2a2a')
    return b
add('Settle', 'Ribblehead Viaduct', '24 arches carrying the Settle-Carlisle line across the moor.', 'grey', settle())

# Bentham - Ingleborough
def bentham():
    b = sun(80, 60, 14) + cloud(260, 50, .7) + cloud(350, 90, .5)
    b += P('M-20 230 L90 150 Q140 92 190 96 L270 96 Q300 100 330 150 L420 230 Z', '#7d8a6c') + P('M190 96 L270 96 Q300 100 330 150 L300 150 Q280 110 250 104 Z', '#6a7759')
    b += P('M180 110 L190 96 L270 96 L280 110 Z', '#8f9a7f')
    b += hills(200, '#8fb07a', 111, 12) + hills(230, '#6f9a5c', 112, 8)
    for y in (240, 262, 286):
        b += PL(f'M0 {y} Q100 {y-8} 200 {y} T400 {y}', '#9c9384', 2.4)
    for x, y in ((120, 274), (260, 296)):
        b += E(x, y, 10, 7, '#f2efe6') + C(x + 11, y - 3, 3.5, '#2a2a2a')
    b += gable_house_simple(320, 236, 50, 30)
    return b
def gable_house_simple(x, y, w, h):
    return R(x, y, w, h, '#cdbb98') + P(f'M{x-3} {y} L{x+w/2} {y-14} L{x+w+3} {y} Z', '#5b5450') + R(x + 8, y + 8, 8, 9, WIN) + R(x + w - 16, y + 8, 8, 9, WIN)
add('Bentham', 'Ingleborough', 'The flat-topped giant of the Three Peaks - 723 metres, best seen from Bentham.', 'day', bentham())

# Whitby - Abbey
def whitby():
    st = '#a59a8a'; dk = shade(st, -.25)
    b = moon(320, 60, 13) + stars(121, 30, 110) + cloud(100, 70, .8, '#6a6f95', .6)
    b += P('M-10 210 Q120 180 410 190 L410 320 L-10 320 Z', '#5f7a5a')
    b += R(60, 110, 240, 100, st)
    for i in range(6): b += arch_win(76 + i * 30, 126, 16, 60, '#3a3f66')
    b += P('M60 110 L60 60 L80 40 L100 60 L100 110 Z', st) + arch_win(70, 70, 20, 40, '#3a3f66') + R(60, 108, 240, 4, dk)
    b += R(300, 70, 50, 140, st) + arch_win(312, 84, 26, 70, '#3a3f66') + P('M300 70 L325 40 L350 70 Z', st)
    b += P('M140 110 L150 96 L160 110 Z M220 110 L232 92 L244 110 Z', '#3a3f66')
    for x in range(20, 400, 40): b += R(x, 228 + (x % 3) * 4, 6, 12, '#7a7f85') + R(x - 2, 230 + (x % 3) * 4, 10, 3, '#7a7f85')
    b += P('M-10 270 L410 250 L410 320 L-10 320 Z', '#2b4a6a')
    b += ''.join(R(30 + i * 10, 258 + i * 2.4, 8, 2, '#d8d2c4') for i in range(10))
    return b
add('Whitby', 'Whitby Abbey', '199 steps up to the abbey that inspired Bram Stoker\'s Dracula.', 'night', whitby())

# Scarborough - Grand Hotel & South Bay
def scarborough():
    b = sun(330, 50, 13) + cloud(90, 50, .8) + cloud(220, 70, .6)
    b += P('M240 120 L280 92 L330 90 L380 110 L410 130 L410 200 L240 200 Z', '#6f9a5c')
    b += R(330, 70, 30, 24, '#a59a8a') + battlements(330, 70, 30, '#a59a8a', 4, 5) + R(300, 88, 60, 6, '#a59a8a')
    st = '#d9b48a'
    b += R(40, 100, 160, 110, st)
    for x in (40, 184):
        b += R(x - 4, 90, 24, 120, '#c9a27a') + P(f'M{x-6} 90 Q{x+8} 66 {x+22} 90 Z', '#5a6a7a')
    b += windows(60, 112, 9, 5, 8, 10, 7.5, 9, WIN)
    b += R(200, 160, 120, 50, '#e8dcc4') + windows(206, 168, 8, 2, 8, 10, 6.5, 8, WIN)
    b += R(0, 200, W, 14, '#c8b89a')
    b += P('M0 214 L410 214 L410 250 Q200 240 0 252 Z', '#ecd9a8')
    b += water(250, '#3f86b5', 122, 16)
    b += P('M0 250 Q200 238 410 248 L410 254 Q200 244 0 256 Z', '#e9f4f7', 'opacity=".8"')
    for i, c in enumerate(('#d22630', '#1d4ed8', '#ffcd00', '#2a8a46', '#e84a7f', '#f07a14')):
        x = 30 + i * 22; b += R(x, 222, 18, 14, c) + P(f'M{x-1} 222 L{x+9} 216 L{x+19} 222 Z', shade(c, -.2))
    b += crowd(12, 180, 390, 226, 123, .95, 16)
    return b
add('Scarborough', 'South Bay', 'The Grand Hotel was one of the biggest hotels in the world when it opened in 1867.', 'day', scarborough())

# Redcar - Redcar Beacon
def redcar():
    b = sun(70, 60, 13) + cloud(250, 50, .8) + cloud(340, 90, .6)
    b += P('M0 210 L410 210 L410 240 L0 248 Z', '#ecd9a8')
    b += water(150, '#3f86b5', 131, 12)
    b += R(0, 150, W, 2, '#8fc0e0')
    b += P('M0 210 Q200 200 410 206 L410 214 Q200 206 0 216 Z', '#e9f4f7', 'opacity=".9"')
    x = 200
    b += P(f'M{x-14} 230 L{x-8} 70 L{x+8} 70 L{x+14} 230 Z', '#d9dce2') + P(f'M{x} 230 L{x} 70 L{x+8} 70 L{x+14} 230 Z', '#b9bdc6')
    for k in range(6): b += L(x - 13 + k * .9, 210 - k * 26, x + 13 - k * .9, 210 - k * 26, '#8a8f99', 1.2)
    b += R(x - 22, 56, 44, 16, '#2b3a55') + R(x - 24, 52, 48, 4, '#d9dce2') + windows(x - 19, 59, 4, 1, 8, 10, 3, 0, '#7fb0d9')
    b += R(0, 248, W, 72, '#7d7a80') + R(0, 248, W, 3, '#a39f9a')
    b += crowd(10, 20, 390, 262, 132, 1.05, 30)
    return b
add('Redcar', 'Redcar Beacon', 'A "vertical pier" - climb to the top for views right along the coast.', 'day', redcar())

# Saltburn - pier & cliff lift
def saltburn():
    b = sun(340, 50, 13, '#ffe0a0', '#ffb36b') + cloud(90, 50, .8, '#ffe8d6')
    b += P('M-10 100 L140 70 L180 90 L180 320 L-10 320 Z', '#6f9a5c') + P('M-10 110 L140 80 L170 100 L170 320 L-10 320 Z', '#a0784a')
    b += L(60, 110, 140, 230, '#5a5a5a', 3) + L(74, 106, 154, 226, '#5a5a5a', 3)
    b += f'<g transform="translate(84 136) rotate(56)">' + R(0, 0, 22, 14, '#d22630', 2) + R(3, 3, 7, 5, '#cfe3f2') + R(12, 3, 7, 5, '#cfe3f2') + '</g>'
    b += f'<g transform="translate(130 200) rotate(56)">' + R(0, 0, 22, 14, '#1d4ed8', 2) + R(3, 3, 7, 5, '#cfe3f2') + R(12, 3, 7, 5, '#cfe3f2') + '</g>'
    b += water(200, '#3f7fb0', 141, 14)
    b += R(150, 196, 260, 6, '#6b4a3a')
    for i in range(10): b += R(160 + i * 26, 202, 4, 40, '#5a3a2a')
    b += R(380, 184, 20, 12, '#efe6d2') + P('M378 184 L390 176 L402 184 Z', '#2b4a6a')
    for x in range(160, 380, 20): b += C(x, 190, 1.8, '#ffe27a')
    b += P('M140 250 Q260 236 410 244 L410 320 L140 320 Z', '#ecd9a8')
    b += crowd(8, 200, 380, 262, 142, 1.05, 30)
    return b
add('Saltburn-by-the-Sea', 'Saltburn Pier & Cliff Lift', 'The cliff tramway has been running on water power since 1884.', 'sunset', saltburn())

# Keswick - Derwentwater
def keswick():
    b = sun(300, 60, 13) + cloud(90, 50, .7)
    b += P('M-20 200 L60 110 L110 150 L170 80 L240 160 L300 120 L420 200 Z', '#6f7f8f') + P('M170 80 L240 160 L200 160 Z M60 110 L110 150 L80 150 Z', '#5a6a7a')
    b += P('M162 92 L170 80 L178 92 Z', '#ffffff')
    b += hills(190, '#5f8f55', 151, 14)
    b += water(208, '#4f8aa8', 152, 16)
    b += P('M0 208 Q200 198 400 208 L400 212 L0 212 Z', '#4a7f4a')
    b += E(120, 228, 30, 6, '#3f6b3a') + tree(110, 226, .9, '#2f6b3c') + tree(126, 225, .8, '#2f6b3c')
    b += P('M-10 270 Q200 256 410 268 L410 320 L-10 320 Z', '#6b8f4e')
    b += R(250, 240, 46, 6, '#6b4a3a') + R(240, 246, 64, 4, '#6b4a3a')
    for i in range(3): b += boat(60 + i * 34, 262 + i * 3, .8, ['#d22630', '#1d4ed8', '#2a8a46'][i], '#f7f2e4')
    b += boat(330, 238, 1.6, '#1b4a3a', '#f7f2e4')
    return b
add('Keswick', 'Derwentwater', 'Get the launch across the lake and walk up Catbells for the view back.', 'day', keswick())

# Alnwick - castle
def alnwick():
    st = '#b9a68a'; dk = shade(st, -.2)
    b = sun(330, 50, 13) + cloud(90, 40, .8) + cloud(230, 60, .6)
    b += R(40, 120, 320, 130, st)
    for x, w, h in ((40, 50, 140), (120, 44, 120), (200, 60, 160), (290, 44, 124), (330, 50, 140)):
        b += R(x, 230 - h, w, h, st) + R(x + w - 10, 230 - h, 10, h, dk) + battlements(x, 230 - h, w, st, 4, 6)
        b += windows(x + 8, 250 - h, 2, 2, 8, 12, w - 32, 16, WIN)
    b += arch_win(214, 186, 32, 44, '#3b2a1a')
    for x in (52, 212, 342): b += person(x, 230 - 140 - 6 if x != 212 else 64, '#8a8072', '#8a8072', 1)
    b += hills(232, '#5f8f55', 161, 8) + ground(250, '#6b9a5a', '#86ad6f')
    b += tree(20, 256, 1.6) + tree(380, 258, 1.8)
    b += water(280, '#4f8aa8', 162, 8)
    return b
add('Alnwick', 'Alnwick Castle', 'Played Hogwarts in the first two Harry Potter films. Broomstick lessons on the lawn.', 'day', alnwick())

# Bakewell - bridge
def bakewell():
    st = '#a8957a'; dk = shade(st, -.2)
    b = sun(330, 50, 13) + cloud(90, 50, .8) + cloud(240, 30, .5)
    b += hills(140, '#7da57a', 171, 12)
    for i, x in enumerate(range(10, 400, 48)):
        b += R(x, 136 + (i % 2) * 6, 42, 40, ['#c4b08e', '#b9a37e', '#d0bd9a'][i % 3]) + P(f'M{x-2} {136+(i%2)*6} L{x+21} {124+(i%2)*6} L{x+44} {136+(i%2)*6} Z', '#5b5450') + R(x + 8, 146 + (i % 2) * 6, 8, 10, WIN)
    b += tree(30, 186, 1.6) + tree(370, 186, 1.8)
    b += R(0, 170, W, 16, st) + R(0, 166, W, 5, dk)
    d = 'M0 186'
    for i in range(5):
        x = i * 80
        d += f' L{x+8} 186 L{x+8} 200 A32 22 0 0 1 {x+72} 200 L{x+72} 186'
    d += ' L400 186 L400 214 L0 214 Z'
    b += P('M0 170 L400 170 L400 220 L0 220 Z', st) + P(d, 'none')
    for i in range(5):
        x = i * 80
        b += P(f'M{x+8} 222 L{x+8} 200 A32 22 0 0 1 {x+72} 200 L{x+72} 222 Z', '#3b5a5a')
        b += P(f'M{x-4} 222 L{x+8} 196 L{x+8} 222 Z', dk)
    b += water(222, '#4f8a9a', 172, 16)
    for x, y in ((100, 260), (140, 280), (300, 270)):
        b += E(x, y, 7, 3.5, '#6b4a2a') + C(x + 6, y - 3, 2.6, '#2a6b3a') + P(f'M{x+8} {y-3} l4 1 l-4 1 z', '#f0b020')
    return b
add('Bakewell', 'Bakewell Bridge', 'A five-arch bridge from the 1300s. Bakewell pudding, never "tart".', 'day', bakewell())

# Manchester - Central Library
def manchester():
    st = '#e3d8c4'; dk = shade(st, -.16)
    b = cloud(80, 60, .9, '#eef2f6') + cloud(300, 40, .8, '#eef2f6')
    b += R(0, 120, 70, 140, '#b98b6a') + windows(8, 130, 3, 5, 12, 14, 7, 10, WIN) + R(330, 110, 70, 150, '#a77a5c') + windows(338, 120, 3, 6, 12, 14, 7, 9, WIN)
    b += E(200, 150, 140, 22, dk) + R(60, 150, 280, 106, st)
    for i in range(9):
        x = 96 + i * 26
        b += R(x, 162, 10, 84, '#f2ebdd') + R(x + 7, 162, 3, 84, dk)
    b += R(60, 150, 280, 12, dk) + R(60, 242, 280, 6, dk)
    b += R(60, 162, 30, 84, st) + R(310, 162, 30, 84, st)
    b += windows(66, 172, 1, 3, 14, 18, 0, 8, WIN) + windows(318, 172, 1, 3, 14, 18, 0, 8, WIN)
    b += E(200, 150, 140, 16, '#5a6a6a') + E(200, 146, 120, 10, '#6a7a7a')
    b += R(0, 256, W, 64, '#8a8d95') + ''.join(R(20 + i * 40, 286, 22, 2, '#f7f2e4') for i in range(10))
    b += R(240, 266, 70, 16, '#ffcd00', 3) + windows(246, 269, 7, 1, 6, 6, 2.6, 0, '#2b3a55') + C(252, 282, 3, '#222') + C(298, 282, 3, '#222')
    b += crowd(10, 40, 230, 258, 181, 1.05, 10)
    return b
add('Manchester', 'Central Library', 'The 1934 rotunda in St Peter\'s Square - modelled on Rome\'s Pantheon.', 'grey', manchester())

# Liverpool - Royal Liver Building
def liverpool():
    st = '#c9c3b6'; dk = shade(st, -.18)
    b = cloud(80, 60, .8) + cloud(230, 40, .6) + sun(340, 60, 12)
    b += R(40, 110, 220, 130, st) + R(214, 110, 46, 130, dk) + windows(52, 122, 10, 7, 10, 10, 7.5, 6, WIN)
    for x in (60, 196):
        b += R(x, 60, 40, 52, st) + R(x + 30, 60, 10, 52, dk) + clockface(x + 20, 82, 12)
        b += R(x + 4, 36, 32, 24, st) + windows(x + 8, 40, 4, 1, 4, 14, 3, 0, WIN)
        b += P(f'M{x+4} 36 Q{x+20} 18 {x+36} 36 Z', '#4f8f7f') + R(x + 19, 12, 2, 10, '#4f8f7f')
        b += P(f'M{x+20} 2 l-6 6 l4 0 l0 6 l4 0 l0 -6 l4 0 z', '#4f8f7f')
    b += R(260, 140, 100, 100, '#d8d2c4') + E(310, 140, 30, 18, '#7a8a8a') + windows(268, 152, 6, 4, 8, 10, 6, 8, WIN)
    b += water(240, '#56708a', 191, 16)
    b += P('M240 262 L340 262 L330 276 L250 276 Z', '#f7f7f7') + R(262, 250, 50, 12, '#ffcd00') + R(270, 242, 20, 8, '#1b1b1b')
    return b
add('Liverpool', 'The Royal Liver Building', 'Legend says if the two Liver Birds fly away, the city will cease to exist.', 'day', liverpool())

# Leicester - King Power Stadium
def leicester():
    b = sun(70, 50, 13) + cloud(250, 50, .8) + cloud(340, 90, .5)
    b += R(0, 200, W, 60, '#6f7f8f')
    b += P('M20 220 L40 120 L360 120 L380 220 Z', '#1d4ed8') + P('M20 220 L40 120 L80 120 L60 220 Z', '#163fb0') + P('M380 220 L360 120 L320 120 L340 220 Z', '#163fb0')
    b += R(30, 112, 340, 10, '#e6e9ef') + ''.join(L(40 + i * 20, 112, 50 + i * 20, 100, '#c9ced8', 2) for i in range(17)) + L(40, 100, 360, 100, '#c9ced8', 2)
    b += T(200, 166, 'KING POWER STADIUM', 26, '#ffffff', 'textLength="270" lengthAdjust="spacingAndGlyphs"')
    b += R(110, 176, 180, 3, '#ffcd00')
    b += windows(60, 190, 12, 1, 18, 24, 5, 0, '#e6e9ef')
    b += road(230, '#3a3f4a')
    b += crowd(40, 10, 390, 238, 201, 1.05, 30, ['#1d4ed8', '#1d4ed8', '#ffffff', '#ffcd00'])
    return b
add('Leicester', 'King Power Stadium', 'Where 5,000-1 outsiders were crowned champions of England in 2016.', 'day', leicester())

# Daventry - Borough Hill
def daventry():
    b = sun(320, 60, 14, '#ffe9b0', '#ffc46a') + cloud(100, 50, .8)
    b += P('M-20 260 Q60 200 140 150 Q220 120 300 150 Q370 190 420 260 Z', '#7fa56f') + P('M140 150 Q220 120 300 150 Q260 140 220 140 Z', '#9ab98a')
    x = 220
    b += P(f'M{x-12} 140 L{x} 20 L{x+12} 140 Z', 'none', 'stroke="#c9ced8" stroke-width="2"') + L(x, 20, x, 140, '#c9ced8', 2)
    for k in range(1, 10): b += L(x - k * 1.2, 140 - k * 12, x + k * 1.2, 140 - k * 12, '#c9ced8', 1.2)
    b += C(x, 20, 3, '#d22630')
    for i in range(3): b += PL(f'M{x+10+i*8} {30-i*2} q6 6 0 12', '#ffcd00', 1.4)
    b += hills(240, '#6f9a5c', 211, 10) + ground(270, '#5f8f55', '#79a86b')
    b += tree(40, 276, 1.5) + tree(370, 276, 1.6)
    for i, x in enumerate(range(90, 330, 50)):
        b += R(x, 262, 40, 28, ['#c9a27e', '#e3d6be', '#b88a68'][i % 3]) + P(f'M{x-2} 262 L{x+20} 250 L{x+42} 262 Z', '#4b3d3a') + R(x + 15, 272, 10, 18, '#5a3a22')
    return b
add('Daventry', 'Borough Hill', 'BBC long-wave masts stood here from 1925 - and radar was first proven near Daventry in 1935.', 'warm', daventry())

# Southwark - The Shard
def southwark():
    b = sun(70, 60, 13) + cloud(300, 60, .8) + cloud(140, 40, .5)
    b += R(0, 170, 60, 80, '#a3aab5') + R(60, 190, 50, 60, '#8f97a3') + R(300, 160, 50, 90, '#9aa3b0') + R(350, 186, 50, 64, '#b3bac4')
    x = 200
    b += P(f'M{x-50} 250 L{x-6} 14 L{x+2} 20 L{x+50} 250 Z', '#a9c8e0') + P(f'M{x+2} 20 L{x+50} 250 L{x+6} 250 Z', '#7ea6c6')
    for k in range(1, 12): b += L(x - 50 + k * 4, 250 - k * 20, x + 50 - k * 4, 250 - k * 20, '#ffffff', .8, 'opacity=".5"')
    b += R(130, 210, 140, 40, '#b8a7a0') + windows(136, 216, 10, 2, 9, 9, 4.4, 4, WIN)
    b += water(250, '#56708a', 221, 14)
    b += boat(100, 276, 1.8, '#d22630', '#f7f2e4')
    return b
add('Southwark', 'The Shard', '310 metres of glass - the tallest building in the UK. Borough Market is at its feet.', 'day', southwark())

# Tower Hamlets - Tower Bridge
def towerhamlets():
    st = '#d8cdb8'; dk = shade(st, -.18)
    b = sun(320, 220, 22, '#ffd27a', '#ff9e5a') + cloud(90, 60, .8, '#ffe1c7') + cloud(260, 50, .5, '#ffe1c7')
    for x in (100, 260):
        b += R(x, 80, 40, 150, st) + R(x + 30, 80, 10, 150, dk)
        b += windows(x + 8, 100, 2, 4, 8, 14, 8, 12, '#3a4a6a', arch=True)
        for px in (x - 2, x + 38): b += R(px, 70, 4, 14, st) + spire(px + 2, 72, 6, 12, '#4a5a6a')
        b += P(f'M{x-2} 80 L{x+20} 50 L{x+42} 80 Z', '#4a5a6a') + R(x + 19, 36, 2, 16, '#c9a227')
    b += R(140, 96, 120, 6, '#5a8ab0') + R(140, 106, 120, 6, '#5a8ab0')
    for k in range(12): b += L(144 + k * 10, 96, 150 + k * 10, 112, '#7aa8c8', 1)
    b += P('M0 150 Q50 120 100 104 L100 112 Q50 128 0 158 Z', '#5a8ab0') + P('M400 150 Q350 120 300 104 L300 112 Q350 128 400 158 Z', '#5a8ab0')
    b += R(140, 196, 120, 8, '#5a8ab0') + R(0, 196, 100, 8, '#5a8ab0') + R(300, 196, 100, 8, '#5a8ab0')
    b += R(160, 180, 40, 16, '#d22630', 3) + windows(164, 183, 5, 1, 5, 4, 2.4, 0, '#2b3a55') + windows(164, 189, 5, 1, 5, 4, 2.4, 0, '#2b3a55')
    b += water(230, '#3f5f7f', 231, 16)
    b += P('M90 230 L150 230 L140 250 L100 250 Z', st) + P('M250 230 L310 230 L300 250 L260 250 Z', st)
    return b
add('Tower Hamlets', 'Tower Bridge', 'Opened 1894 - the road still lifts for tall ships about 800 times a year.', 'sunset', towerhamlets())

# Newham - London Stadium & Orbit
def newham():
    b = cloud(80, 50, .8) + cloud(300, 40, .7) + sun(210, 50, 11)
    b += P('M120 240 L140 170 Q240 150 340 170 L360 240 Z', '#e9edf2') + P('M140 170 Q240 150 340 170 L336 180 Q240 162 144 180 Z', '#7a1f3d')
    b += ''.join(L(150 + i * 16, 172 - (abs(i - 6) * -.6), 148 + i * 16, 236, '#c9ced8', 1.4) for i in range(13))
    x = 80
    d = f'M{x-14} 250 Q{x-30} 180 {x} 150 Q{x+30} 120 {x+6} 80 Q{x-20} 50 {x+10} 30 M{x+14} 250 Q{x+26} 190 {x-4} 160 Q{x-30} 120 {x+4} 90 Q{x+26} 60 {x+2} 40'
    b += PL(d, '#c0392b', 7, 'stroke-linecap="round"')
    b += E(x + 6, 36, 20, 7, '#9a9da6') + R(x - 14, 36, 40, 6, '#bfc3cc')
    b += PL(f'M{x+20} 44 Q{x+50} 120 {x+20} 200 Q{x+10} 230 {x+30} 250', '#9a9da6', 4)
    b += water(250, '#4f7f9a', 241, 10) + R(0, 268, W, 52, '#6b8f4e')
    b += crowd(16, 140, 380, 272, 242, 1.05, 30, ['#7a1f3d', '#7a1f3d', '#7fb0d9', '#ffffff'])
    return b
add('Newham', 'London Stadium & the Orbit', 'The Orbit has the world\'s longest tunnel slide - 178 metres down.', 'day', newham())

# Brent - Wembley
def brent():
    b = sun(70, 70, 14) + cloud(300, 60, .8)
    b += P('M40 240 Q200 60 360 240', 'none', 'stroke="#ffffff" stroke-width="9"')
    b += P('M40 240 Q200 60 360 240', 'none', 'stroke="#c9ced8" stroke-width="3"')
    for k in range(1, 20):
        t = k / 20; px = (1 - t) ** 2 * 40 + 2 * (1 - t) * t * 200 + t * t * 360; py = (1 - t) ** 2 * 240 + 2 * (1 - t) * t * 60 + t * t * 240
        b += L(px, py, 120 + k * 8, 180, '#ffffff', .6, 'opacity=".7"')
    b += P('M30 250 L50 176 Q200 160 350 176 L370 250 Z', '#e6e9ef') + R(50, 176, 300, 8, '#b9c0cc')
    b += windows(60, 192, 14, 2, 14, 16, 6.4, 8, '#7fa8c8')
    b += T(200, 244, 'WEMBLEY', 14, '#1b3a8f', 'letter-spacing="4"')
    b += road(250, '#4a4f5a')
    b += crowd(40, 10, 390, 258, 251, 1.05, 30, ['#ffffff', '#ffcd00', '#1d4ed8', '#d22630'])
    return b
add('Brent', 'Wembley Stadium', 'The arch is 133 metres tall - you can see it from all over north London.', 'day', brent())

# Greenwich - Cutty Sark
def greenwich():
    b = sun(330, 60, 13) + cloud(90, 50, .8) + cloud(220, 30, .5)
    b += hills(160, '#6f9a5c', 261, 14) + R(300, 120, 30, 20, '#d8cdb8') + E(315, 120, 10, 8, '#6f7f8f')
    b += R(0, 200, W, 60, '#cfc6b4')
    b += P('M60 210 L330 210 L310 240 L90 240 Z', '#1b1b1b') + R(70, 204, 250, 6, '#c9a227')
    b += P('M330 210 L360 196 L340 216 Z', '#1b1b1b')
    for x, h in ((120, 160), (190, 180), (260, 150)):
        b += R(x, 204 - h, 3, h, '#5a3a22')
        for k in range(4):
            y = 204 - h + 18 + k * 28; w = 34 - k * 2
            b += L(x - w, y, x + w + 3, y, '#5a3a22', 1.6)
        b += L(x + 1.5, 204 - h, 60 if x == 120 else x - 60, 210, '#3b3b3b', .7) + L(x + 1.5, 204 - h, x + 70, 210, '#3b3b3b', .7)
    b += L(330, 210, 260, 54, '#3b3b3b', .7)
    b += R(0, 240, W, 80, '#a69d8c') + R(0, 240, W, 3, '#c3bba9')
    b += crowd(14, 20, 380, 252, 262, 1.05, 30)
    return b
add('Greenwich', 'The Cutty Sark', 'The fastest tea clipper of her day, launched 1869. Stand on the Prime Meridian up the hill.', 'day', greenwich())

# Newport (Isle of Wight) - Carisbrooke Castle
def newport():
    st = '#b3a58c'; dk = shade(st, -.2)
    b = sun(330, 50, 13) + cloud(90, 50, .8) + cloud(240, 30, .5)
    b += P('M-20 320 L-20 220 Q100 150 200 140 Q300 150 420 220 L420 320 Z', '#6f9a5c')
    b += R(60, 120, 280, 50, st) + battlements(60, 120, 280, st, 4, 7)
    for x in (60, 330): b += R(x - 6, 100, 22, 70, st) + battlements(x - 6, 100, 22, st, 3, 6)
    b += R(170, 84, 60, 86, st) + R(214, 84, 16, 86, dk) + battlements(170, 84, 60, st, 4, 7)
    for x in (172, 212): b += R(x, 70, 16, 20, st) + battlements(x, 70, 16, st, 3, 5)
    b += arch_win(188, 126, 24, 44, '#3b2a1a') + windows(90, 136, 3, 1, 8, 12, 14, 0, WIN, arch=True) + windows(260, 136, 3, 1, 8, 12, 14, 0, WIN, arch=True)
    b += P('M140 170 L260 170 L300 230 L100 230 Z', '#c9b48f')
    b += E(300, 268, 14, 9, '#8a8478') + C(314, 260, 5, '#8a8478') + P('M312 254 l2 -8 l3 7 z M318 254 l3 -8 l2 8 z', '#8a8478') + R(290, 274, 3, 10, '#6a6458') + R(306, 274, 3, 10, '#6a6458')
    b += tree(30, 250, 1.6) + tree(380, 250, 1.8)
    return b
add('Newport', 'Carisbrooke Castle', 'Charles I was held prisoner here - and donkeys still work the old well wheel.', 'day', newport())

# Llanrwst - Pont Fawr & Tu Hwnt i'r Bont
def llanrwst():
    st = '#8f8475'; dk = shade(st, -.2)
    b = sun(330, 50, 12) + cloud(90, 50, .8)
    b += hills(120, '#5f7f55', 281, 24, 4)
    b += P('M0 200 Q100 170 200 130 Q300 170 400 200 L400 214 L0 214 Z', st)
    for x, w, h in ((40, 70, 26), (150, 100, 48), (290, 70, 26)):
        b += P(f'M{x} 214 L{x} {214-h*.4} A{w/2} {h} 0 0 1 {x+w} {214-h*.4} L{x+w} 214 Z', '#3b5a5a')
    b += water(212, '#4f7f8a', 282, 14)
    hx = 320
    b += R(hx, 150, 70, 52, '#a39684') + P(f'M{hx-4} 150 L{hx+35} 124 L{hx+74} 150 Z', '#5b5450')
    for k in range(60):
        import random as _r
        rr = _r.Random(k)
        b += C(hx + rr.uniform(0, 70), 150 + rr.uniform(0, 50), rr.uniform(3, 6), ['#b8322e', '#c9433a', '#8f2a2a'][k % 3])
    b += R(hx + 28, 180, 12, 22, '#3b2a1a')
    b += tree(30, 214, 1.5, '#4f7f45') + tree(80, 212, 1.2, '#4f7f45')
    return b
add('Llanrwst', 'Pont Fawr', 'The 1636 bridge, with the ivy-covered Tu Hwnt i\'r Bont tearoom on the far bank.', 'day', llanrwst())

# Dublin - Ha'penny Bridge
def dublin():
    b = sun(330, 220, 18, '#ffd27a', '#ff9e5a') + cloud(90, 60, .8, '#ffe1c7')
    cols = ['#d8c8a8', '#b98b6a', '#e3d6be', '#7a9a8a', '#c4ae86', '#a26f58']
    for i, x in enumerate(range(-10, 410, 44)):
        h = 90 + (i % 3) * 14
        b += R(x, 200 - h, 42, h, cols[i % 6]) + windows(x + 6, 200 - h + 10, 3, 4, 7, 10, 5, 8, '#3a4a6a')
    b += R(0, 196, W, 8, '#7a7a7a')
    b += water(204, '#3f5f7f', 291, 16)
    b += P('M40 220 Q200 150 360 220 L360 228 Q200 160 40 228 Z', '#f2f2ee')
    for k in range(1, 16):
        t = k / 16; px = (1 - t) ** 2 * 40 + 2 * (1 - t) * t * 200 + t * t * 360; py = (1 - t) ** 2 * 224 + 2 * (1 - t) * t * 152 + t * t * 224
        b += L(px, py - 8, px, py, '#f2f2ee', 1.2)
    b += PL('M40 212 Q200 142 360 212', '#f2f2ee', 2)
    for x in (130, 270): b += R(x - 1, 168, 2, 16, '#2a2a2a') + C(x, 166, 4, '#ffe27a')
    b += crowd(8, 120, 280, 180, 292, .8, 8)
    b += R(0, 290, W, 30, '#7a7a7a')
    return b
add('Dublin', 'Ha\'penny Bridge', 'Built in 1816 - you used to pay a halfpenny toll to cross the Liffey.', 'sunset', dublin())
