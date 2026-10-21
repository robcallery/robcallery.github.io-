import sys, math
cols=["#ff4d4d","#ffcd00","#4dd2ff","#7dff7a","#ff8ad8","#ffffff"]
def bulbs(pts,r=2,start=0):
    return ''.join(f'<circle class="twinkle" cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{cols[(i+start)%6]}" style="animation-delay:{((i*0.37)%2):.2f}s"/>' for i,(x,y) in enumerate(pts))
def line(p0,p1,n,sag=0):
    out=[]
    for i in range(n+1):
        t=i/n; x=p0[0]+(p1[0]-p0[0])*t; y=p0[1]+(p1[1]-p0[1])*t+sag*4*t*(1-t); out.append((x,y))
    return out
def wreath(cx,cy,r):
    g=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#1d6b35" stroke-width="{r*.7:.1f}"/>'
    g+=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#2a8a46" stroke-width="{r*.3:.1f}" stroke-dasharray="2 2"/>'
    g+=''.join(f'<circle cx="{cx+r*math.cos(a):.1f}" cy="{cy+r*math.sin(a):.1f}" r="{r*.18:.1f}" fill="#d22630"/>' for a in [0.3,1.6,2.9,4.2,5.4])
    g+=f'<path d="M{cx} {cy+r} l-{r*.6:.1f} -{r*.35:.1f} l0 {r*.7:.1f} z M{cx} {cy+r} l{r*.6:.1f} -{r*.35:.1f} l0 {r*.7:.1f} z" fill="#d22630"/>'
    return g
def hat(x,y,s,rot):
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><path d="M-10 0 Q-2 -22 14 -16 Q4 -12 10 0 Z" fill="#d22630"/><rect x="-12" y="-2" width="24" height="6" rx="3" fill="#fff"/><circle cx="14" cy="-16" r="3.2" fill="#fff"/></g>'

# --- Farke & Firkin (pub-local coords)
pub='<g id="s-xmas-pub">'
pub+='<path d="M20 600 L150 548 L280 600" fill="none" stroke="#1b1b1b" stroke-width=".8"/>'
pub+='<g class="treelights">'+bulbs(line((22,600),(150,549),12)+line((150,549),(278,600),12)[1:])+'</g>'
# garland swags under the sign
sw='M22 643 '+' '.join(f'Q{22+32*i+16} 654 {22+32*(i+1)} 643' for i in range(8))
pub+=f'<path d="{sw}" fill="none" stroke="#1d6b35" stroke-width="4" stroke-linecap="round"/><path d="{sw}" fill="none" stroke="#2a8a46" stroke-width="1.5" stroke-dasharray="2 3"/>'
pub+=''.join(f'<path d="M{22+32*i} 643 l-3 -3 l0 6 z M{22+32*i} 643 l3 -3 l0 6 z" fill="#d22630"/>' for i in range(9))
pub+='<g class="treelights">'+bulbs([(22+32*i+16,650) for i in range(8)],1.8,2)+'</g>'
pub+=wreath(150,691,6)
pub+='</g>'

# --- Firpo't of Call (tapas-local coords)
tap='<g id="s-xmas-tapas" style="display:none">'
tap+='<g class="treelights">'+bulbs(line((974,662),(1150,662),16),1.8,1)+'</g>'
# lights spiralling up the palm trunk
pts=[]
for i in range(18):
    y=716-i*9.5; x=1180+3*math.sin(y/30)+(-4 if i%2 else 4)*0.9
    pts.append((x,y))
tap+='<g class="treelights">'+bulbs(pts,2.1,3)+'</g>'
tap+=hat(1003,640,1.0,-12)
tap+=wreath(1047,707,5)
tap+='<g>'+''.join(f'<g transform="translate({x} 703)">'+''.join(f'<ellipse rx="1.6" ry="3.6" transform="rotate({a}) translate(0 -3)" fill="#d22630"/>' for a in range(0,360,60))+'<circle r="1.2" fill="#ffcd00"/></g>' for x in (1121,1129,1137))+'</g>'
tap+='<g font-family="Bebas Neue, Impact, sans-serif" font-size="7" fill="#d22630" text-anchor="middle"><text x="1003" y="690" textLength="26" lengthAdjust="spacingAndGlyphs">FELIZ</text><text x="1091" y="690" textLength="30" lengthAdjust="spacingAndGlyphs">NAVIDAD</text></g>'
tap+='</g>'

for f in sys.argv[1:]:
    s=open(f).read()
    # pub decorations go inside the #season group
    s=s.replace('<g id="s-nye">',pub+'<g id="s-nye">',1)
    # tapas decorations inside a copy of the tapas transform, right after the season group
    a=s.index('<g transform="translate(-5 36) scale(0.95)" id="season">'); b=s.index('\n',a)
    s=s[:b]+'\n    <g transform="translate(-159.3 -108) scale(1.15)">'+tap+'</g>'+s[b:]
    s=s.replace("else if(xmas){show('s-tree');show('s-holly');","else if(xmas){show('s-tree');show('s-holly');show('s-xmas-pub');show('s-xmas-tapas');",1)
    open(f,'w').write(s); print('ok',f)
