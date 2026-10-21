# Drawing helpers for the travel-guide polaroids (flat style, matches the home page scene)
import random, math

W, H = 400, 320
GY = 262  # default ground line

def shade(hexc, k):
    """k<0 darker, k>0 lighter"""
    hexc = hexc.lstrip('#')
    r, g, b = int(hexc[0:2], 16), int(hexc[2:4], 16), int(hexc[4:6], 16)
    if k < 0:
        r, g, b = [int(c * (1 + k)) for c in (r, g, b)]
    else:
        r, g, b = [int(c + (255 - c) * k) for c in (r, g, b)]
    return '#%02x%02x%02x' % (r, g, b)

def R(x, y, w, h, f, rx=0, ex=''):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}"{f" rx=%s" % rx if rx else ""} fill="{f}" {ex}/>'

def P(d, f, ex=''):
    return f'<path d="{d}" fill="{f}" {ex}/>'

def C(cx, cy, r, f, ex=''):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{f}" {ex}/>'

def E(cx, cy, rx, ry, f, ex=''):
    return f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{f}" {ex}/>'

def L(x1, y1, x2, y2, s, w=1, ex=''):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{s}" stroke-width="{w}" {ex}/>'

def PL(d, s, w=1, ex=''):
    return f'<path d="{d}" fill="none" stroke="{s}" stroke-width="{w}" {ex}/>'

def T(x, y, txt, size, f, ex='', anchor='middle', font='Bebas Neue, Impact, sans-serif'):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-family="{font}" font-size="{size}" fill="{f}" text-anchor="{anchor}" {ex}>{txt}</text>'

SKIES = {
    'day':    ('#5fb4e8', '#cdeefc'),
    'bright': ('#3d9be0', '#bfe6fb'),
    'warm':   ('#5aa9e0', '#fbe3b8'),
    'dusk':   ('#2e3f86', '#f59f6a'),
    'sunset': ('#5a3d8a', '#ffb36b'),
    'night':  ('#0b1838', '#2b4280'),
    'grey':   ('#8fa7bb', '#dfe7ee'),
    'tropic': ('#2aa3e6', '#bff0ff'),
}

def defs_sky(sid, kind):
    a, b = SKIES[kind]
    return f'<linearGradient id="{sid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient>'

def stars(seed, n=40, ymax=180):
    rnd = random.Random(seed)
    return ''.join(C(rnd.uniform(5, W - 5), rnd.uniform(5, ymax), rnd.choice([.6, .8, 1.1]), '#fff', f'opacity="{rnd.uniform(.4, 1):.2f}"') for _ in range(n))

def cloud(cx, cy, s=1.0, f='#fff', op=.92):
    parts = [(-30, 4, 14, 11), (-12, -2, 20, 16), (10, 0, 19, 15), (28, 5, 13, 10)]
    g = ''.join(E(cx + dx * s, cy + dy * s, rx * s, ry * s, f) for dx, dy, rx, ry in parts)
    g += R(cx - 40 * s, cy + 2 * s, 80 * s, 12 * s, f, rx=6 * s)
    return f'<g opacity="{op}">{g}</g>'

def sun(cx, cy, r=18, f='#fff3b0', glow='#ffe27a'):
    return C(cx, cy, r * 2.2, glow, 'opacity=".25"') + C(cx, cy, r, f)

def moon(cx, cy, r=14):
    return f'<path d="M{cx} {cy-r} A{r} {r} 0 1 0 {cx} {cy+r} A{r*.72:.1f} {r} 0 1 1 {cx} {cy-r} Z" fill="#f4f1e0" transform="rotate(-25 {cx} {cy})"/>'

def hills(y, color, seed, amp=18, n=5, x0=-20, x1=W + 20, base=H):
    rnd = random.Random(seed)
    pts = [(x0, y + rnd.uniform(-amp, amp * .3))]
    step = (x1 - x0) / n
    d = f'M{x0} {base} L{pts[0][0]:.1f} {pts[0][1]:.1f}'
    for i in range(1, n + 1):
        x = x0 + i * step
        yy = y + rnd.uniform(-amp, amp * .4)
        cx = x - step / 2
        cy = min(yy, pts[-1][1]) - rnd.uniform(4, amp)
        d += f' Q{cx:.1f} {cy:.1f} {x:.1f} {yy:.1f}'
        pts.append((x, yy))
    d += f' L{x1} {base} Z'
    return P(d, color)

def ground(y=GY, f='#3f6b3a', top=None):
    g = R(0, y, W, H - y, f)
    if top:
        g += R(0, y, W, 3, top)
    return g

def road(y=GY, f='#2f3340'):
    return R(0, y, W, H - y, f) + R(0, y, W, 2, shade(f, .2))

def water(y, f='#3a7fc1', seed=1, n=14, lines='#ffffff'):
    rnd = random.Random(seed)
    g = R(0, y, W, H - y, f)
    for _ in range(n):
        x = rnd.uniform(0, W); yy = rnd.uniform(y + 4, H - 4); w = rnd.uniform(10, 34)
        g += R(x, yy, w, 1.6, lines, ex=f'opacity="{rnd.uniform(.25, .55):.2f}"')
    return g

def tree(x, y, s=1.0, f='#3d8b45', trunk='#5a3a22'):
    return R(x - 2 * s, y - 10 * s, 4 * s, 10 * s, trunk) + C(x, y - 18 * s, 11 * s, f) + C(x - 6 * s, y - 13 * s, 7 * s, shade(f, -.12)) + C(x + 5 * s, y - 22 * s, 6 * s, shade(f, .12))

def pine(x, y, s=1.0, f='#2f6b3c'):
    return R(x - 1.5 * s, y - 6 * s, 3 * s, 6 * s, '#5a3a22') + P(f'M{x-10*s} {y-6*s} L{x} {y-34*s} L{x+10*s} {y-6*s} Z', f) + P(f'M{x} {y-6*s} L{x} {y-34*s} L{x+10*s} {y-6*s} Z', shade(f, -.15))

def palm(x, y, s=1.0, lean=6):
    g = PL(f'M{x} {y} Q{x+lean*s*.4} {y-30*s} {x+lean*s} {y-58*s}', '#7a5230', 4 * s, 'stroke-linecap="round"')
    tx, ty = x + lean * s, y - 58 * s
    for a, l in [(-160, 26), (-120, 24), (-60, 24), (-20, 26), (-95, 18)]:
        ra = math.radians(a)
        ex, ey = tx + math.cos(ra) * l * s, ty + math.sin(ra) * l * s + 10 * s
        mx, my = tx + math.cos(ra) * l * s * .5, ty + math.sin(ra) * l * s * .5 - 6 * s
        g += PL(f'M{tx:.1f} {ty:.1f} Q{mx:.1f} {my:.1f} {ex:.1f} {ey:.1f}', '#2f8a47', 4.5 * s, 'stroke-linecap="round"')
    return g

PEOPLE = ['#ffcd00', '#1d4ed8', '#ffffff', '#d22630', '#2a8a46', '#f07a14', '#7c3aed', '#e84a7f']
SKIN = ['#f1c9a5', '#d9a47a', '#a8714a', '#7a4b2c', '#f4d6bd']

def person(x, y, body='#ffcd00', skin='#f1c9a5', s=1.0):
    return R(x - 2.2 * s, y - 6 * s, 1.8 * s, 6 * s, '#2a2d3a') + R(x + .4 * s, y - 6 * s, 1.8 * s, 6 * s, '#2a2d3a') + R(x - 3 * s, y - 13 * s, 6 * s, 8 * s, body, rx=1.5 * s) + C(x, y - 15.5 * s, 2.6 * s, skin)

def crowd(n, x0, x1, y, seed, s=1.0, jitter=6, cols=PEOPLE):
    rnd = random.Random(seed)
    out = []
    for _ in range(n):
        yy = y + rnd.uniform(0, jitter)
        out.append((yy, person(rnd.uniform(x0, x1), yy, rnd.choice(cols), rnd.choice(SKIN), s * (0.85 + (yy - y) / 40))))
    return ''.join(p for _, p in sorted(out))

def windows(x, y, cols, rows, w, h, gx, gy, f, arch=False):
    g = ''
    for r in range(rows):
        for c in range(cols):
            wx, wy = x + c * (w + gx), y + r * (h + gy)
            if arch:
                g += P(f'M{wx:.1f} {wy+h:.1f} L{wx:.1f} {wy+w/2:.1f} A{w/2:.1f} {w/2:.1f} 0 0 1 {wx+w:.1f} {wy+w/2:.1f} L{wx+w:.1f} {wy+h:.1f} Z', f)
            else:
                g += R(wx, wy, w, h, f)
    return g

def arch_win(x, y, w, h, f):
    return P(f'M{x:.1f} {y+h:.1f} L{x:.1f} {y+w/2:.1f} A{w/2:.1f} {w/2:.1f} 0 0 1 {x+w:.1f} {y+w/2:.1f} L{x+w:.1f} {y+h:.1f} Z', f)

def battlements(x, y, w, f, mw=6, mh=6):
    n = max(2, int(w // (mw * 2)))
    step = w / n
    return ''.join(R(x + i * step, y - mh, step * .55, mh, f) for i in range(n)) + R(x + w - step * .55, y - mh, step * .55, mh, f)

def clockface(cx, cy, r, face='#f7f2e4', rim='#3b3b3b', t=(10, 2)):
    h, m = t
    ah = math.radians(h * 30 - 90); am = math.radians(m * 6 - 90)
    return C(cx, cy, r + 1.2, rim) + C(cx, cy, r, face) + L(cx, cy, cx + math.cos(ah) * r * .5, cy + math.sin(ah) * r * .5, rim, max(.8, r * .14)) + L(cx, cy, cx + math.cos(am) * r * .78, cy + math.sin(am) * r * .78, rim, max(.6, r * .1))

def spire(x, base, w, h, f):
    return P(f'M{x-w/2:.1f} {base:.1f} L{x:.1f} {base-h:.1f} L{x+w/2:.1f} {base:.1f} Z', f) + P(f'M{x:.1f} {base:.1f} L{x:.1f} {base-h:.1f} L{x+w/2:.1f} {base:.1f} Z', shade(f, -.15))

def plane(x, y, s=1.0, f='#ffffff', tail='#1d4ed8', flip=False):
    g = (E(0, 0, 34, 6.5, f) + P('M-30 -3 L-38 -18 L-30 -18 L-20 -3 Z', tail) + P('M-4 0 L-16 16 L-8 16 L10 0 Z', shade(f, -.12)) + P('M-4 -1 L-12 -10 L-6 -10 L6 -1 Z', shade(f, -.06))
         + ''.join(C(-18 + i * 5.5, -1.5, 1.3, '#2b4a7a') for i in range(8)) + P('M28 -3 Q34 -2 34 0 L26 0 Z', '#2b4a7a'))
    sc = f'scale({-s if flip else s} {s})'
    return f'<g transform="translate({x} {y}) {sc}">{g}</g>'

def boat(x, y, s=1.0, hull='#c0392b', top='#fff'):
    return f'<g transform="translate({x} {y}) scale({s})">' + P('M-18 0 L18 0 L13 7 L-13 7 Z', hull) + R(-7, -6, 12, 6, top) + '</g>'

def bike(x, y, f='#222', s=1.0):
    return f'<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{f}" stroke-width="1.2">' + '<circle cx="-6" cy="0" r="4.5"/><circle cx="6" cy="0" r="4.5"/><path d="M-6 0 L-1 -7 L5 -7 L6 0 M-1 -7 L1 0 L-6 0 M5 -9 L5 -7 M-2 -9 L1 -9"/></g>'

def flowers(x0, x1, y, seed, n=30, cols=('#e84a7f', '#ffcd00', '#ffffff', '#d22630', '#b45ce0')):
    rnd = random.Random(seed)
    return ''.join(C(rnd.uniform(x0, x1), y + rnd.uniform(0, 14), rnd.uniform(1.4, 2.4), rnd.choice(cols)) for _ in range(n))

def fireworks(cx, cy, r, f, n=14):
    g = ''
    for i in range(n):
        a = 2 * math.pi * i / n
        g += L(cx + math.cos(a) * r * .3, cy + math.sin(a) * r * .3, cx + math.cos(a) * r, cy + math.sin(a) * r, f, 1.4, 'stroke-linecap="round"')
        g += C(cx + math.cos(a) * r * 1.08, cy + math.sin(a) * r * 1.08, 1.2, f)
    return g

def scene(slug, sky, body, extra_defs=''):
    sid = f'sk-{slug}'
    bg = R(0, 0, W, H, f'url(#{sid})')
    return (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">'
            f'<defs>{defs_sky(sid, sky)}{extra_defs}</defs>{bg}{body}</svg>')
