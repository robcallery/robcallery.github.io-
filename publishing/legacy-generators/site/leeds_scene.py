# Elland Road from the corner of the South Stand, under the roof - drawn from Rob's photo
import numpy as np, random, math
W, H = 1600, 900

def homog(src, dst):
    A = []
    for (x, y), (u, v) in zip(src, dst):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y, -u]); A.append([0, 0, 0, x, y, 1, -v * x, -v * y, -v])
    _, _, vt = np.linalg.svd(np.array(A, float)); h = vt[-1].reshape(3, 3); return h / h[2, 2]
# pitch coords: u along the near touchline (0 = our corner, 105 = far end), v along the goal line (0 = corner, 68 = far touchline)
C, G, L, F = (300, 650), (1720, 525), (-760, 515), (760, 452)
Hm = homog([(0, 0), (0, 68), (105, 0), (105, 68)], [C, G, L, F])
def pt(u, v):
    p = Hm @ np.array([u, v, 1.0]); return p[0] / p[2], p[1] / p[2]
def poly(points, fill, extra=''):
    return f'<path d="M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in points) + f' Z" fill="{fill}" {extra}/>'
def line(pts, stroke='#f4f8f0', w=2.2):
    return f'<path d="M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + f'" fill="none" stroke="{stroke}" stroke-width="{w}" stroke-linejoin="round"/>'
def seg(u0, v0, u1, v1, n=24): return [pt(u0 + (u1 - u0) * k / n, v0 + (v1 - v0) * k / n) for k in range(n + 1)]
def arc(cu, cv, r, a0, a1, n=40): return [pt(cu + r * math.cos(a0 + (a1 - a0) * k / n), cv + r * math.sin(a0 + (a1 - a0) * k / n)) for k in range(n + 1)]

def scene(screen=True):
    rnd = random.Random(1919)
    g = ['<defs>',
         '<linearGradient id="erSky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9cc6e4"/><stop offset=".55" stop-color="#e6eef4"/><stop offset="1" stop-color="#f6f4ee"/></linearGradient>',
         '<linearGradient id="erRoof" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a3f47"/><stop offset="1" stop-color="#5a616b"/></linearGradient>',
         '<linearGradient id="erGrass" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3f9a3a"/><stop offset="1" stop-color="#5cbc45"/></linearGradient>',
         '<linearGradient id="erFront" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a2236"/><stop offset="1" stop-color="#0b0f1a"/></linearGradient>',
         '<radialGradient id="erGlow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>',
         '</defs>']
    a = g.append
    a(f'<rect width="{W}" height="{H}" fill="url(#erSky)"/>')
    # distant hills and a crane over the far end
    a('<path d="M0 395 Q200 372 420 386 T860 380 T1300 388 L1600 384 L1600 440 L0 440 Z" fill="#8a9a8a" opacity=".55"/>')
    a('<path d="M1020 400 L1046 250 L1052 250 L1030 400 Z" fill="#7a7f86"/>')
    # ---- far end stand (behind L-F) with the big screen at the corner
    ex = pt(105, -6); fx = pt(105, 70)
    top_l, top_r = (ex[0], ex[1] - 92), (fx[0] - 40, fx[1] - 70)
    a(poly([(ex[0], ex[1] + 6), (fx[0] - 40, fx[1] + 2), top_r, top_l], '#2b3a63'))
    for k in range(9):
        t = 0.12 + k * 0.095; y0 = ex[1] - 92 * t; y1 = fx[1] - 70 * t
        a(line([(ex[0], y0), (fx[0] - 40, y1)], '#1d2a4a', 1.2))
    for _ in range(900):
        t = rnd.random(); s = rnd.uniform(.12, .95)
        x = ex[0] + (fx[0] - 40 - ex[0]) * t; y = (ex[1] + (fx[1] - ex[1]) * t) - s * (92 + (70 - 92) * t)
        a(f'<rect x="{x:.0f}" y="{y:.0f}" width="2.4" height="2.4" fill="{rnd.choice(["#e9edf5","#1e3f9a","#ffcd00","#c9d2e6","#283a6a","#f2c9a5"])}"/>')
    a(poly([(ex[0], ex[1] - 92), (fx[0] - 40, fx[1] - 70), (fx[0] - 40, fx[1] - 84), (ex[0], ex[1] - 110)], '#e8ebef'))
    a(f'<text x="{(ex[0]+fx[0])/2-90:.0f}" y="{(ex[1]+fx[1])/2-92:.0f}" font-family="Bebas Neue, Impact, sans-serif" font-size="13" fill="#1e3f9a" letter-spacing="3" transform="rotate(-3 {(ex[0]+fx[0])/2:.0f} {(ex[1]+fx[1])/2-92:.0f})">NORMAN HUNTER NORTH STAND</text>')
    a(poly([(ex[0], ex[1] - 110), (fx[0] - 40, fx[1] - 84), (fx[0] - 40, fx[1] - 96), (ex[0], ex[1] - 124)], '#3b4150'))
    # ---- John Charles Stand (behind G-F), long, with the blue fascia
    jf, jg = pt(108, 72), pt(-8, 72)
    j_top_f, j_top_g = (jf[0], jf[1] - 86), (jg[0], jg[1] - 150)
    a(poly([(jf[0], jf[1] + 4), (jg[0], jg[1] + 4), j_top_g, j_top_f], '#26355c'))
    for k in range(12):
        t = 0.08 + k * 0.075
        a(line([(jf[0], jf[1] - 86 * t), (jg[0], jg[1] - 150 * t)], '#1b2747', 1.2))
    for _ in range(2200):
        t = rnd.random(); s = rnd.uniform(.08, .9)
        x = jf[0] + (jg[0] - jf[0]) * t; base = jf[1] + (jg[1] - jf[1]) * t; hh = 86 + (150 - 86) * t
        a(f'<rect x="{x:.0f}" y="{base - s*hh:.0f}" width="{2.2+2*t:.1f}" height="{2.2+2*t:.1f}" fill="{rnd.choice(["#e9edf5","#1e3f9a","#ffcd00","#d8dde8","#2a3c6c","#f2c9a5","#1e3f9a"])}"/>')
    # roof soffit & fascia
    a(poly([(jf[0], jf[1] - 86), (jg[0], jg[1] - 150), (jg[0], jg[1] - 168), (jf[0], jf[1] - 96)], '#1a1f2b'))
    a(poly([(jf[0], jf[1] - 96), (jg[0], jg[1] - 168), (jg[0], jg[1] - 206), (jf[0], jf[1] - 112)], '#2d4fb4'))
    a(poly([(jf[0], jf[1] - 112), (jg[0], jg[1] - 206), (jg[0], jg[1] - 214), (jf[0], jf[1] - 115)], '#d9dde4'))
    mx, my = jf[0] + (jg[0] - jf[0]) * .32, jf[1] - 104 + ((jg[1] - 187) - (jf[1] - 104)) * .32
    ang = math.degrees(math.atan2((jg[1] - 187) - (jf[1] - 104), jg[0] - jf[0]))
    a(f'<text x="{mx:.0f}" y="{my+5:.0f}" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="17" fill="#ffcd00" letter-spacing="2" transform="rotate({ang:.1f} {mx:.0f} {my:.0f})">JOHN CHARLES STAND</text>')
    for k, t in enumerate((.74,)):
        x = jf[0] + (jg[0] - jf[0]) * t; y = jf[1] - 104 + ((jg[1] - 187) - (jf[1] - 104)) * t
        a(f'<text x="{x:.0f}" y="{y+6:.0f}" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="{18+k*4}" fill="#ffffff" letter-spacing="2" transform="rotate({ang:.1f} {x:.0f} {y:.0f})">LEEDS UNITED</text>')
    # big screen (filled by script)
    sx, sy = fx[0] - 260, fx[1] - 178
    if screen:
        a(f'<g id="bigScreen"><rect x="{sx-6}" y="{sy-6}" width="176" height="104" rx="4" fill="#1a1d24"/><rect x="{sx}" y="{sy}" width="164" height="92" fill="#0a1838"/>'
          f'<rect x="{sx}" y="{sy}" width="164" height="18" fill="#ffcd00"/><text id="bsHead" x="{sx+82}" y="{sy+14}" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="14" fill="#0a1838" letter-spacing="2">NEXT UP</text>'
          f'<text id="bsMain" x="{sx+82}" y="{sy+46}" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="22" fill="#ffffff" textLength="150" lengthAdjust="spacingAndGlyphs">LEEDS UNITED</text>'
          f'<text id="bsSub" x="{sx+82}" y="{sy+68}" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="15" fill="#ffcd00" letter-spacing="1" textLength="150" lengthAdjust="spacingAndGlyphs">MARCHING ON TOGETHER</text>'
          f'<text id="bsFoot" x="{sx+82}" y="{sy+86}" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" fill="#9fb0d8"> </text>'
          f'<rect x="{sx+78}" y="{sy+98}" width="8" height="40" fill="#2a2d34"/></g>')
    sxy = (sx, sy)
    # ---- pitch
    a(poly([pt(-3, -3), pt(-3, 71), pt(108, 71), pt(108, -3)], '#2f8a34'))
    for k in range(14):
        u0 = k * 7.5
        a(poly([pt(u0, 0), pt(u0, 68), pt(u0 + 7.5, 68), pt(u0 + 7.5, 0)], '#4fb048' if k % 2 else '#43a23e'))
    a(poly([pt(-3, -3), pt(-3, 71), pt(108, 71), pt(108, -3)], 'url(#erGrass)', 'opacity=".25"'))
    lw = '#f6faf2'
    a(line(seg(0, 0, 0, 68) + seg(0, 68, 105, 68)[1:] + seg(105, 68, 105, 0)[1:] + seg(105, 0, 0, 0)[1:], lw, 2.4))
    a(line(seg(52.5, 0, 52.5, 68), lw, 1.8))
    a(line(arc(52.5, 34, 9.15, 0, 2 * math.pi, 60), lw, 1.8))
    for u in (0, 105):
        s = 1 if u == 0 else -1
        a(line([pt(u, 13.84), pt(u + s * 16.5, 13.84), pt(u + s * 16.5, 54.16), pt(u, 54.16)], lw, 2))
        a(line([pt(u, 24.84), pt(u + s * 5.5, 24.84), pt(u + s * 5.5, 43.16), pt(u, 43.16)], lw, 2))
        a(line(arc(u + s * 11, 34, 9.15, (-0.93 if s > 0 else math.pi - 0.93), (0.93 if s > 0 else math.pi + 0.93)), lw, 1.8))
    a(line(arc(0, 0, 1, 0, math.pi / 2, 8), lw, 1.6))
    # goals
    for u, near in ((0, True), (105, False)):
        p1, p2 = pt(u, 30.34), pt(u, 37.66); hgt = 34 if near else 9
        d = -2 if near else 2
        b1, b2 = pt(u + (-2.2 if near else 2.2), 30.34), pt(u + (-2.2 if near else 2.2), 37.66)
        a(poly([p1, b1, b2, p2, (p2[0], p2[1] - hgt), (p1[0], p1[1] - hgt)], '#ffffff', 'opacity=".22"'))
        for k in range(1, 8):
            t = k / 8
            a(line([(p1[0] + (p2[0] - p1[0]) * t, p1[1] + (p2[1] - p1[1]) * t - hgt), (b1[0] + (b2[0] - b1[0]) * t, b1[1] + (b2[1] - b1[1]) * t)], '#ffffff', .6))
        a(line([p1, (p1[0], p1[1] - hgt), (p2[0], p2[1] - hgt), p2], '#ffffff', 4 if near else 1.6))
        if near:
            a(line([p1, (p1[0], p1[1] - hgt)], '#1e3f9a', 4) + line([p2, (p2[0], p2[1] - hgt)], '#ffcd00', 3))
    cx, cy = C
    a(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-44}" stroke="#f2f2f2" stroke-width="2.5"/><path d="M{cx} {cy-44} L{cx+16} {cy-38} L{cx} {cy-30} Z" fill="#ffcd00"/>')
    # players warming up / groundstaff
    for u, v, c in ((40, 30, '#14182a'), (46, 36, '#14182a'), (60, 52, '#14182a'), (74, 20, '#14182a'), (88, 44, '#ffffff'), (95, 47, '#ffffff'), (12, 20, '#ff7a1a'), (3, -1.5, '#1e3f9a')):
        x, y = pt(u, v); s = 0.45 + 0.9 * (1 - u / 105) ** 2
        a(f'<g transform="translate({x:.0f} {y:.0f}) scale({s:.2f})"><rect x="-4" y="-26" width="8" height="15" rx="3" fill="{c}"/><rect x="-3.5" y="-12" width="3" height="12" fill="#222"/><rect x=".5" y="-12" width="3" height="12" fill="#222"/><circle cy="-30" r="4.5" fill="#e8c4a0"/></g>')
    # LED boards along the near touchline (behind which we stand)
    b0, b1 = pt(-1, -1.6), pt(106, -1.6)
    a(f'<g id="ledNear">' + poly([pt(-1, -1.6), pt(106, -1.6), (b1[0], b1[1] - 8), (b0[0], b0[1] - 22)], '#0a1838') + '</g>')
    a(f'<text id="ledText" x="{(b0[0]+b1[0])/2+40:.0f}" y="{(b0[1]+b1[1])/2-6:.0f}" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="16" fill="#ffcd00" letter-spacing="2" transform="rotate({math.degrees(math.atan2(b1[1]-b0[1], b1[0]-b0[0])):.1f} {(b0[0]+b1[0])/2+40:.0f} {(b0[1]+b1[1])/2-6:.0f})">MARCHING ON TOGETHER</text>')
    fl = pt(-1, 70.5); fr = pt(106, 70.5)
    a(poly([pt(-1, 70.5), pt(106, 70.5), (fr[0], fr[1] - 6), (fl[0], fl[1] - 12)], '#0a1838'))
    # ---- our stand: front wall, rows of fans, railings
    a(f'<path d="M0 {C[1]+40} L{C[0]-60} {C[1]+30} L1600 {C[1]-30} L1600 {H} L0 {H} Z" fill="url(#erFront)"/>')
    a(f'<path d="M0 {C[1]+40} L{C[0]-60} {C[1]+30} L1600 {C[1]-30} L1600 {C[1]-18} L{C[0]-60} {C[1]+42} L0 {C[1]+52} Z" fill="#e9edf2"/>')
    rows = []
    for r in range(9):
        yb = C[1] + 30 + r * 34; sc = 0.7 + r * 0.22
        n = int(26 - r * 1.6)
        for k in range(n):
            x = rnd.uniform(-40, 1640); y = yb - x * 0.04 + rnd.uniform(-6, 6)
            col = rnd.choice(['#1d2433', '#262d3d', '#14182a', '#2a3550', '#1e3f9a', '#3a2a2a', '#1e3f9a', '#4a4f5c', '#f2c200', '#22262e'] + (['#ff7a1a'] if rnd.random() < .06 else []))
            skin = rnd.choice(['#3a2a20', '#5a4030', '#2a2420', '#c9ccd2', '#8a6a4a', '#1e1e22', '#d9a77a', '#6a5a4a', '#1e3f9a'])
            rows.append((y, f'<g transform="translate({x:.0f} {y:.0f}) scale({sc:.2f})"><path d="M-16 40 Q-16 6 0 4 Q16 6 16 40 Z" fill="{col}"/><ellipse cx="0" cy="-6" rx="9" ry="11" fill="{skin}"/><path d="M-7 2 Q0 6 7 2 L6 6 Q0 9 -6 6 Z" fill="#d9a77a" opacity=".8"/>' + (f'<rect x="-6" y="18" width="12" height="4" fill="#ffcd00"/>' if rnd.random() < .15 else '') + '</g>'))
        rows.append((yb + 16, f'<path d="M-20 {yb+14 - (-20)*0.04:.0f} L1620 {yb+14 - 1620*0.04:.0f}" stroke="#c9ced8" stroke-width="{2+r*.5:.1f}" opacity=".85"/>'))
    for _, s in sorted(rows): a(s)
    # ---- roof overhead
    a('<path d="M0 0 L1600 0 L1600 248 L0 92 Z" fill="url(#erRoof)"/>')
    for k in range(18):
        x = k * 100; a(f'<path d="M{x} 0 L{x + 60} {92 + (156 * (x + 60) / 1600):.0f}" stroke="#2a2e36" stroke-width="2"/>')
    for t in (.25, .5, .75):
        a(f'<path d="M0 {92*t:.0f} L1600 {248*t:.0f}" stroke="#2a2e36" stroke-width="5"/>')
    a('<path d="M0 92 L1600 248" stroke="#7b5cff" stroke-width="5" opacity=".85"/><path d="M0 98 L1600 254" stroke="#cfc4ff" stroke-width="1.5" opacity=".6"/>')
    for x in (560, 1060, 1450):
        y = 92 + 156 * x / 1600
        a(f'<rect x="{x}" y="{y-6:.0f}" width="22" height="34" rx="4" fill="#20232a"/>')
    for x, y in ((900, 22), (960, 34), (1020, 46)):
        a(f'<ellipse cx="{x+30}" cy="{y+16}" rx="70" ry="30" fill="url(#erGlow)" opacity=".5"/><rect x="{x}" y="{y}" width="60" height="26" rx="3" fill="#f4f6ff" stroke="#9aa0ad" stroke-width="2"/>')
    return ''.join(g), sxy
