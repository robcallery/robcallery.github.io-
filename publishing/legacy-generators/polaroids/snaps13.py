from snaplib import *
from snaps10 import cathedral, stadium
from snaps11 import pier, seaside, terrace
from snaps7 import lighthouse
import random

S = {}
def add(city, title, note, sky, body, defs=''):
    slug = ''.join(ch for ch in city.lower() if ch.isalnum())
    S[city] = (title, note, scene(slug, sky, body, defs))
WIN = '#4a5878'

# Bristol - Clifton Suspension Bridge
def bristol():
    b = sun(320, 200, 20, '#ffd27a', '#ff9e5a') + cloud(90, 60, .8, '#ffe1c7')
    b += P('M-10 320 L-10 110 L60 100 L80 320 Z', '#8a7a6a') + P('M410 320 L410 120 L340 110 L320 320 Z', '#7a6a5a')
    b += tree(20, 104, 1.4, '#4f7f45') + tree(380, 114, 1.4, '#4f7f45')
    for x in (70, 330):
        b += R(x - 12, 40, 24, 70, '#c9b48f') + arch_win(x - 6, 70, 12, 40, '#7a6a5a') + R(x - 14, 36, 28, 6, '#b3a07a')
    b += PL('M70 44 Q200 150 330 44', '#3a3a40', 2.5) + PL('M70 48 Q200 154 330 48', '#3a3a40', 1.5)
    for k in range(1, 26):
        x = 70 + k * 10; y = 44 + 106 * (1 - ((x - 200) / 130) ** 2)
        b += L(x, y, x, 112, '#3a3a40', .7)
    b += R(56, 110, 288, 5, '#3a3a40')
    b += water(270, '#5a6a6a', 2101, 8) + P('M80 320 L80 270 L320 270 L320 320 Z', '#6a7a5a', 'opacity=".0"')
    return b
add('Bristol', 'Clifton Suspension Bridge', 'Designed by Brunel, opened in 1864 - 75 metres above the Avon Gorge.', 'sunset', bristol())

# Plymouth - Smeaton's Tower
def plymouth():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += water(160, '#3f86b5', 2111, 18)
    b += P('M-10 210 Q200 196 410 210 L410 320 L-10 320 Z', '#6fa85a') + R(0, 250, W, 70, '#bdb39f')
    b += lighthouse(200, 214, 110, '#f4f1ea', '#d22630', 2)
    b += crowd(10, 20, 380, 262, 2112, 1.05, 40)
    return b
add('Plymouth', 'Smeaton\'s Tower', 'This lighthouse once stood on the Eddystone rocks - it was moved to the Hoe in the 1880s.', 'day', plymouth())

# Bournemouth - pier & beach huts
def bournemouth():
    b = seaside(2121) + pier(214, 300, '#e6e9ef')
    b += R(260, 150, 60, 24, '#f4f1ea') + E(290, 150, 30, 8, '#9ac4dc')
    for i, c in enumerate(('#d22630', '#1d4ed8', '#ffcd00', '#2a8a46', '#e84a7f', '#7c3aed', '#f07a14', '#4dd2ff')):
        x = 10 + i * 48; b += R(x, 260, 40, 34, c) + P(f'M{x-2} 260 L{x+20} 248 L{x+42} 260 Z', shade(c, -.25)) + R(x + 14, 274, 12, 20, '#f4f1ea')
    b += crowd(10, 20, 380, 232, 2122, 1.05, 18)
    return b
add('Bournemouth', 'The pier & beach huts', 'Seven miles of sandy beach from Sandbanks to Hengistbury Head.', 'day', bournemouth())

# Swindon - Magic Roundabout
def swindon():
    b = sun(330, 40, 10) + cloud(90, 30, .6)
    b += R(0, 0, W, H, '#6fa85a', 'opacity=".0"')
    b += R(0, 80, W, 240, '#6fa85a')
    b += R(170, 80, 60, 240, '#4b505c') + R(0, 170, W, 60, '#4b505c') + P('M60 80 L120 80 L240 320 L180 320 Z', '#4b505c')
    b += C(200, 200, 34, '#7aa86a') + C(200, 200, 34, 'none', 'stroke="#f4f1ea" stroke-width="3"')
    for a in range(5):
        ang = a * 2 * math.pi / 5 - 1.2; x = 200 + math.cos(ang) * 64; y = 200 + math.sin(ang) * 64
        b += C(x, y, 14, '#f4f1ea') + C(x, y, 9, '#7aa86a')
    for x, y, c in ((120, 196, '#d22630'), (270, 210, '#1d4ed8'), (190, 120, '#ffcd00'), (196, 280, '#2a8a46'), (310, 190, '#f4f1ea')):
        b += R(x - 9, y - 5, 18, 10, c, 2)
    return b
add('Swindon', 'The Magic Roundabout', 'Five mini-roundabouts around one big one, since 1972. Go both ways at once.', 'day', swindon())

# Poole - harbour
def poole():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += hills(150, '#4f7f45', 2141, 10) + water(160, '#3f86b5', 2142, 20)
    b += E(220, 168, 60, 10, '#4f7f45')
    for i, (x, y) in enumerate(((60, 230), (160, 260), (300, 220))):
        b += P(f'M{x-20} {y} L{x+20} {y} L{x+14} {y+8} L{x-14} {y+8} Z', '#f4f1ea') + L(x, y, x, y - 46, '#5a5a5a', 1.5) + P(f'M{x+1} {y-44} L{x+1} {y-4} L{x+24} {y-4} Z', ['#ffffff', '#d22630', '#ffcd00'][i])
    b += R(0, 290, W, 30, '#8a8475')
    return b
add('Poole', 'Poole Harbour', 'One of the biggest natural harbours in the world.', 'day', poole())

# Exeter - cathedral
def exeter():
    st = '#d6c39f'; dk = shade(st, -.18)
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(40, 140, 320, 110, st) + P('M40 140 L200 116 L360 140 Z', '#5a6a6a') + windows(54, 156, 10, 1, 12, 44, 18, 0, WIN, arch=True)
    for x in (90, 270): b += R(x, 70, 50, 180, st) + R(x + 38, 70, 12, 180, dk) + battlements(x, 70, 50, st, 4, 7) + windows(x + 10, 90, 2, 3, 10, 20, 10, 12, WIN, arch=True)
    b += ground(250, '#5f9a50', '#7ab36a') + crowd(10, 30, 370, 270, 2151, 1.05, 30)
    return b
add('Exeter', 'Exeter Cathedral', 'Inside is the longest unbroken medieval vaulted ceiling in the world.', 'day', exeter())

# Gloucester - cathedral cloisters
def gloucester():
    st = '#d8c8a0'; dk = shade(st, -.16)
    b = R(0, 0, W, H, '#c9b48f')
    for i in range(5):
        x = 20 + i * 76
        b += P(f'M{x} 320 L{x} 120 Q{x+36} 60 {x+72} 120 L{x+72} 320 Z', '#a8946c')
        for k in range(4): b += PL(f'M{x} 120 Q{x+36} {80+k*10} {x+72} 120', '#8a7a5a', 1)
        b += arch_win(x + 14, 140, 44, 110, '#9ac4dc') + ''.join(L(x + 22 + k * 10, 150, x + 22 + k * 10, 250, '#a8946c', 1.4) for k in range(3))
    b += R(0, 0, W, 60, '#b8a47c') + ''.join(PL(f'M{20+i*76} 60 Q{56+i*76} 20 {92+i*76} 60', '#8a7a5a', 1.4) for i in range(5))
    b += R(0, 290, W, 30, '#9a8a6a')
    return b
add('Gloucester', 'The cathedral cloisters', 'The fan-vaulted cloisters doubled as Hogwarts corridors in the Harry Potter films.', 'day', gloucester())

# Salisbury - spire
def salisbury():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += cathedral('#cfc6b0', 170, False, 2171)
    b += ground(250, '#5f9a50', '#7ab36a') + tree(30, 254, 1.8) + tree(380, 254, 1.8)
    return b
add('Salisbury', 'Salisbury Cathedral', 'The tallest spire in Britain, and the best-preserved copy of Magna Carta.', 'day', salisbury())

# Bath - Royal Crescent
def bath():
    st = '#e8d6a8'; dk = shade(st, -.14)
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += P('M-10 220 Q200 90 410 220 L410 240 Q200 116 -10 240 Z', st, 'opacity=".0"')
    for i in range(20):
        t = i / 19; x = -10 + t * 420; y = 100 + 80 * (2 * t - 1) ** 2
        b += R(x, y, 22, 110, st) + R(x + 2, y + 10, 4, 100, dk) + R(x + 14, y + 10, 4, 100, dk) + windows(x + 7, y + 20, 1, 3, 6, 14, 0, 14, WIN)
    b += ground(220, '#5f9a50', '#7ab36a') + crowd(8, 40, 360, 270, 2181, 1.05, 30)
    return b
add('Bath', 'The Royal Crescent', '30 Georgian houses in one sweeping curve, finished in 1774.', 'day', bath())

# Weston-super-Mare - Grand Pier & donkeys
def weston():
    b = seaside(2191) + pier(214, 340, '#e6e9ef')
    b += R(290, 120, 90, 40, '#f4f1ea') + ''.join(onion(300 + k * 22, 122, 10, 16, '#f4f1ea') for k in range(4))
    for x in (90, 150, 210):
        b += E(x, 262, 16, 9, '#8a7a6a') + C(x + 16, 254, 6, '#8a7a6a') + P(f'M{x+14} 248 l2 -8 l3 7 z', '#8a7a6a') + R(x - 10, 268, 3, 12, '#6a5a4a') + R(x + 8, 268, 3, 12, '#6a5a4a') + R(x - 6, 252, 14, 6, '#d22630')
    return b
def onion(x, base, w, h, f):
    return P(f'M{x-w/2} {base} Q{x-w/2-2} {base-h*.5} {x} {base-h} Q{x+w/2+2} {base-h*.5} {x+w/2} {base} Z', f)
add('Weston-super-Mare', 'The Grand Pier', 'The tide here has one of the biggest ranges in the world - the sea goes out for miles.', 'day', weston())

# Taunton - cricket & church tower
def taunton():
    st = '#d8b48a'; dk = shade(st, -.18)
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(260, 60, 50, 140, st) + R(298, 60, 12, 140, dk) + battlements(260, 60, 50, st, 4, 8)
    for px in (262, 284, 306): b += spire(px, 60, 6, 16, st)
    b += R(20, 150, 200, 50, '#e6e9ef') + windows(30, 160, 8, 1, 16, 20, 7, 0, '#7fa8c8')
    b += ground(200, '#6fb05a', '#86c06f') + E(200, 270, 160, 40, '#7ac06a') + R(180, 250, 40, 40, '#d9c79a')
    b += crowd(3, 170, 230, 268, 2201, 1, 6, ['#ffffff']) + L(196, 252, 196, 262, '#c9a27e', 1) + L(204, 284, 204, 294, '#c9a27e', 1)
    return b
add('Taunton', 'The County Ground', 'Somerset cricket under St James\'s church tower - with a cider in hand.', 'day', taunton())

# Yeovil - helicopter
def yeovil():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += hills(200, '#8fb07a', 2211, 10) + ground(230, '#6fa85a', '#86b86f')
    x, y = 200, 120
    b += E(x, y, 46, 18, '#3f5a4a') + P(f'M{x+40} {y-4} L{x+120} {y-10} L{x+120} {y-2} L{x+40} {y+6} Z', '#3f5a4a') + R(x + 112, y - 26, 8, 22, '#3f5a4a')
    b += E(x - 18, y - 2, 16, 10, '#a3c4dc') + R(x - 2, y - 26, 4, 10, '#2a2a2a') + L(x - 90, y - 26, x + 90, y - 26, '#2a2a2a', 3)
    b += L(x - 30, y + 18, x - 30, y + 26, '#2a2a2a', 2) + L(x + 20, y + 18, x + 20, y + 26, '#2a2a2a', 2) + L(x - 40, y + 26, x + 30, y + 26, '#2a2a2a', 2)
    return b
add('Yeovil', 'The helicopter town', 'Helicopters have been built in Yeovil since the 1950s.', 'day', yeovil())

# Torquay - palms & harbour
def torquay():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += terrace(150, 2221, 8, 52, 50, 70) + P('M-10 150 Q200 120 410 150 L410 160 L-10 160 Z', '#6fa85a')
    b += water(160, '#2f86c5', 2222, 18)
    for i, x in enumerate((60, 150, 240, 330)): b += P(f'M{x-16} {220+i%2*20} L{x+16} {220+i%2*20} L{x+12} {228+i%2*20} L{x-12} {228+i%2*20} Z', '#f4f1ea') + L(x, 220 + i % 2 * 20, x, 180 + i % 2 * 20, '#5a5a5a', 1.4)
    b += R(0, 270, W, 50, '#bdb39f') + palm(40, 276, 1.2, 4) + palm(200, 278, 1.1, -4) + palm(360, 276, 1.2, -6)
    return b
add('Torquay', 'The English Riviera', 'Agatha Christie was born in Torquay in 1890.', 'tropic', torquay())

# Paignton - steam train & pier
def paignton():
    b = seaside(2231)
    b += pier(200, 200, '#e6e9ef')
    b += R(0, 238, W, 6, '#6b4a3a')
    x = 280
    b += R(x - 50, 206, 100, 30, '#2a6b3a', 4) + R(x + 40, 192, 24, 44, '#2a6b3a') + R(x - 36, 186, 10, 20, '#1b1b1b')
    b += C(x - 30, 170, 10, '#e8e8f0', 'opacity=".8"') + C(x - 18, 154, 14, '#e8e8f0', 'opacity=".6"')
    for cx in (x - 30, x, x + 30): b += C(cx, 238, 9, '#1b1b1b') + C(cx, 238, 3, '#c9a227')
    b += crowd(10, 20, 220, 262, 2232, 1.05, 40)
    return b
add('Paignton', 'Pier & steam railway', 'Steam trains run from here along the coast to Kingswear for the Dartmouth ferry.', 'day', paignton())

# Newton Abbot - Tuckers Maltings
def newtonabbot():
    br = '#b98b6a'
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += R(60, 110, 240, 140, br) + windows(74, 124, 9, 4, 14, 14, 11.6, 14, '#e8f0f6') + T(180, 104, 'TUCKERS MALTINGS', 14, '#5a3a22', 'letter-spacing="2"')
    for x in (300, 330): b += P(f'M{x} 110 L{x+14} 80 L{x+28} 110 Z', '#6b5a50') + R(x + 4, 110, 20, 140, br)
    b += R(0, 250, W, 70, '#aaa294') + crowd(8, 20, 380, 262, 2241, 1.05, 30)
    return b
add('Newton Abbot', 'Tuckers Maltings', 'A working Victorian malthouse - one of the last of its kind in England.', 'day', newtonabbot())

# Weymouth - Jubilee Clock
def weymouth():
    b = seaside(2251)
    x = 200
    b += R(x - 10, 120, 20, 110, '#1d4ed8') + R(x - 16, 100, 32, 26, '#d22630') + clockface(x, 113, 10) + P(f'M{x-18} 100 Q{x} 80 {x+18} 100 Z', '#2a8a46') + R(x - 1, 74, 2, 10, '#c9a227')
    b += R(x - 16, 226, 32, 10, '#f4f1ea')
    b += crowd(12, 20, 380, 240, 2252, 1.05, 50)
    return b
add('Weymouth', 'The Jubilee Clock', 'Built in 1888 for Queen Victoria\'s Golden Jubilee - George III made the town fashionable.', 'day', weymouth())

# Dorchester - Thomas Hardy statue
def dorchester():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += terrace(220, 2261, 8, 52, 80, 110) + R(0, 220, W, 100, '#aaa294')
    x = 200
    b += R(x - 22, 210, 44, 40, '#8a8a8a') + P(f'M{x-12} 210 L{x-8} 150 L{x+8} 150 L{x+12} 210 Z', '#5a6a5a') + C(x, 140, 9, '#5a6a5a') + P(f'M{x-14} 136 L{x+14} 136 L{x+8} 128 L{x-8} 128 Z', '#5a6a5a')
    b += P(f'M{x+8} 180 L{x+22} 190 L{x+20} 196 Z', '#5a6a5a')
    b += crowd(8, 20, 380, 270, 2262, 1.05, 30)
    return b
add('Dorchester', 'Thomas Hardy', 'Dorchester is Hardy\'s "Casterbridge" - his statue stands at the top of High West Street.', 'day', dorchester())

# Cheltenham - racecourse
def cheltenham():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += hills(140, '#6f9a5c', 2271, 18) + R(40, 130, 320, 60, '#e6e9ef') + windows(50, 140, 14, 1, 16, 20, 6.4, 0, '#7fa8c8')
    b += crowd(30, 50, 350, 196, 2272, .8, 4) + R(0, 200, W, 10, '#f4f1ea') + ground(210, '#4f9a45', '#6ab35a')
    b += R(150, 220, 100, 10, '#4a3a2a') + R(150, 216, 100, 4, '#2a6b2a') + ''.join(L(150 + k * 10, 210, 150 + k * 10, 222, '#2a6b2a', 2) for k in range(11))
    for i, (x, c) in enumerate(((90, '#d22630'), (200, '#ffcd00'), (320, '#1d4ed8'))):
        y = 270 + (i % 2) * 14
        b += E(x, y, 20, 9, '#6b3a1a') + P(f'M{x+14} {y-4} L{x+28} {y-18} L{x+32} {y-14} L{x+22} {y} Z', '#6b3a1a') + C(x + 30, y - 16, 4, '#6b3a1a')
        b += L(x - 14, y + 6, x - 22, y + 20, '#6b3a1a', 3) + L(x + 12, y + 6, x + 22, y + 20, '#6b3a1a', 3) + R(x - 4, y - 18, 8, 9, c, 2) + C(x, y - 21, 3, c)
    return b
add('Cheltenham', 'Cheltenham Racecourse', 'Home of the Gold Cup - the Festival every March is the biggest week in jump racing.', 'day', cheltenham())

# Stroud - mills in the valley
def stroud():
    b = sun(330, 50, 12) + cloud(90, 40, .8)
    b += P('M-10 320 L-10 80 Q100 120 200 200 Q300 120 410 80 L410 320 Z', '#6fa85a') + P('M-10 320 L-10 150 Q100 170 200 230 Q300 170 410 150 L410 320 Z', '#5f9a50')
    b += R(120, 190, 160, 50, '#d8c8a8') + windows(130, 198, 10, 2, 10, 10, 5, 8, WIN) + R(260, 150, 12, 40, '#a8503a')
    b += water(240, '#4f7f6a', 2281, 8) + R(0, 260, W, 60, '#5f9a50')
    for i, x in enumerate(range(20, 400, 70)): b += R(x, 270, 50, 30, ['#d22630', '#2a8a46', '#ffcd00', '#1d4ed8', '#e84a7f', '#f07a14'][i % 6]) + R(x + 2, 300, 2, 14, '#555') + R(x + 46, 300, 2, 14, '#555')
    return b
add('Stroud', 'The five valleys', 'Stroud\'s mills made the scarlet cloth for British Army uniforms.', 'day', stroud())
