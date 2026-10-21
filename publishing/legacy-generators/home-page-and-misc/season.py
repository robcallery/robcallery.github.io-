import random, sys
random.seed(4)
def build():
    G=[]; a=G.append
    # planters either side of the pub door (pub-local coords)
    def planter(x): return f'<rect x="{x}" y="706" width="30" height="14" rx="2" fill="#5a3a22"/><rect x="{x-2}" y="704" width="34" height="4" rx="1" fill="#6e4a2c"/>'
    a('<g id="planters">'+planter(98)+planter(172)+'</g>')
    # default: flowers
    fl=''
    for x0 in (98,172):
        for k in range(5):
            cx=x0+4+k*5.5; cy=700-(k%2)*3
            fl+=f'<line x1="{cx}" y1="704" x2="{cx}" y2="{cy}" stroke="#2f7d3a" stroke-width="1.5"/><circle cx="{cx}" cy="{cy}" r="2.6" fill="{["#e84a7f","#ffcd00","#ffffff","#b45ce0","#ff8a3a"][k]}"/>'
    a(f'<g id="s-flowers">{fl}</g>')
    # October: pumpkins, one carved, glowing at night
    def pumpkin(cx,r,face=False):
        g=f'<ellipse cx="{cx}" cy="{704-r*.8:.1f}" rx="{r*1.25:.1f}" ry="{r:.1f}" fill="#f07a14"/>'
        g+=f'<path d="M{cx} {704-r*1.8:.1f} q-{r*.35:.1f} {r*.9:.1f} 0 {r*1.8:.1f} M{cx-r*.7:.1f} {704-r*1.7:.1f} q-{r*.5:.1f} {r*.9:.1f} 0 {r*1.75:.1f} M{cx+r*.7:.1f} {704-r*1.7:.1f} q{r*.5:.1f} {r*.9:.1f} 0 {r*1.75:.1f}" stroke="#c65a08" stroke-width="1" fill="none"/>'
        g+=f'<rect x="{cx-1:.1f}" y="{704-r*2.05:.1f}" width="2.2" height="{r*.5:.1f}" rx="1" fill="#3e6b2a"/>'
        if face:
            y=704-r*.85
            g+=f'<g fill="#ffd34d" style="opacity:calc(.35 + .65*var(--night,0));filter:drop-shadow(0 0 3px #ffb000)"><path d="M{cx-r*.55:.1f} {y-r*.15:.1f} l{r*.25:.1f} -{r*.35:.1f} l{r*.25:.1f} {r*.35:.1f} z"/><path d="M{cx+r*.05:.1f} {y-r*.15:.1f} l{r*.25:.1f} -{r*.35:.1f} l{r*.25:.1f} {r*.35:.1f} z"/><path d="M{cx-r*.65:.1f} {y+r*.2:.1f} q{r*.65:.1f} {r*.55:.1f} {r*1.3:.1f} 0 l-{r*.25:.1f} {r*.12:.1f} l-{r*.2:.1f} -{r*.1:.1f} l-{r*.2:.1f} {r*.12:.1f} l-{r*.2:.1f} -{r*.1:.1f} z"/></g>'
        return g
    a('<g id="s-pumpkins">'+pumpkin(106,6)+pumpkin(120,8,True)+pumpkin(181,8,True)+pumpkin(195,5.5)+'</g>')
    # Christmas: holly + berries in planters
    ho=''
    for x0 in (98,172):
        for k in range(4):
            cx=x0+5+k*7
            ho+=f'<path d="M{cx} 704 q-6 -6 -2 -11 q2 4 5 2 q-1 5 -3 9z" fill="#1f6b33"/><path d="M{cx+2} 704 q6 -6 3 -11 q-2 4 -5 2 q1 5 2 9z" fill="#2a8040"/><circle cx="{cx+1}" cy="695" r="1.8" fill="#d22630"/>'
    a(f'<g id="s-holly">{ho}</g>')
    # Bonfire (Nov 1-6) in front of the bench
    fl='<g id="s-bonfire">'
    fl+='<ellipse cx="70" cy="782" rx="60" ry="14" fill="#ff9a3a" opacity=".25" class="glowpulse"/>'
    fl+='<g fill="#5a3a22" stroke="#3b2414" stroke-width="1"><path d="M40 784 L100 770 L102 776 L42 790 Z"/><path d="M42 770 L100 786 L98 792 L40 776 Z"/><path d="M58 786 L76 744 L82 746 L64 788 Z"/><path d="M82 786 L66 746 L72 744 L88 784 Z"/></g>'
    fl+='<g class="flames">'
    for i,(cx,h,w,c) in enumerate([(70,58,30,"#ff5a1f"),(60,40,20,"#ff8a1f"),(82,44,20,"#ff8a1f"),(70,38,18,"#ffc23a"),(70,22,10,"#fff1a8")]):
        fl+=f'<path class="flame f{i}" d="M{cx-w/2} 778 Q{cx-w/2} {778-h*.5} {cx} {778-h} Q{cx+w/2} {778-h*.5} {cx+w/2} 778 Z" fill="{c}"/>'
    fl+='</g>'
    fl+=''.join(f'<circle class="ember e{i}" cx="{70+random.uniform(-14,14):.0f}" cy="740" r="1.4" fill="#ffcf6a"/>' for i in range(6))
    fl+='</g>'
    a(fl)
    # Christmas tree (Nov 7 - Dec 30), grows toward the 25th
    tr='<g id="s-tree" transform="translate(232 762)"><g id="treeScale">'
    tr+='<rect x="-5" y="-14" width="10" height="14" fill="#5a3a22"/><rect x="-12" y="-6" width="24" height="10" rx="2" fill="#a3262e"/><rect x="-12" y="-4" width="24" height="2" fill="#ffcd00"/>'
    for (w,y0,h) in [(64,-14,40),(50,-44,38),(36,-72,34),(22,-96,28)]:
        tr+=f'<path d="M{-w/2} {y0} L0 {y0-h} L{w/2} {y0} Z" fill="#1d6b35"/><path d="M{-w/2} {y0} L0 {y0-h} L0 {y0} Z" fill="#185c2d"/>'
    bulbs=[(-20,-20),(14,-24),(-6,-34),(22,-18),(-14,-50),(10,-56),(0,-64),(-8,-80),(8,-82),(0,-100),(-24,-16),(18,-48)]
    cols=["#ffcd00","#ff4d4d","#4dd2ff","#ffffff","#ff8ad8","#7dff7a"]
    tr+='<g class="treelights">'+''.join(f'<circle class="twinkle" cx="{x}" cy="{y}" r="2.2" fill="{cols[i%6]}" style="animation-delay:{i*.27:.2f}s"/>' for i,(x,y) in enumerate(bulbs))+'</g>'
    tr+='<path d="M0 -133 l3.5 7.5 l8 .8 l-6 5.4 l1.8 8 l-7.3 -4.2 l-7.3 4.2 l1.8 -8 l-6 -5.4 l8 -.8 z" fill="#ffcd00" style="filter:drop-shadow(0 0 4px #ffd84d)"/>'
    tr+='</g></g>'
    a(tr)
    # NYE party
    ny='<g id="s-nye">'
    ny+='<g class="partylights"><rect class="pl0" x="45" y="662" width="60" height="34"/><rect class="pl1" x="195" y="662" width="60" height="34"/></g>'
    bt=''; cols=["#ffcd00","#1d4ed8","#ffffff","#e84a7f","#4dd2ff"]
    for i,x in enumerate(range(32,268,12)):
        sag=4*((x-150)/118)**2
        bt+=f'<path d="M{x} {648-sag+4:.1f} L{x+10} {648-sag+4:.1f} L{x+5} {658-sag+4:.1f} Z" fill="{cols[i%5]}"/>'
    ny+='<path d="M30 652 Q150 660 270 652" stroke="#222" stroke-width="1" fill="none"/>'+bt
    for (x,y,c) in [(104,672,"#ffcd00"),(112,666,"#1d4ed8"),(186,670,"#e84a7f"),(194,664,"#ffffff")]:
        ny+=f'<line x1="{x}" y1="{y+8}" x2="{x+4 if x<150 else x-4}" y2="704" stroke="#ddd" stroke-width=".8"/><ellipse class="bal" cx="{x}" cy="{y}" rx="5" ry="6.5" fill="{c}"/>'
    ny+='<g transform="translate(232 724)"><path d="M-14 0 L-10 -30 L10 -30 L14 0" fill="none" stroke="#5a3a22" stroke-width="2"/><rect x="-11" y="-30" width="22" height="22" fill="#1b1b1b" stroke="#5a3a22" stroke-width="2"/><g fill="#fff" font-family="Bebas Neue, Impact, sans-serif" font-size="6.5" text-anchor="middle"><text y="-22">NYE</text><text y="-16">PARTY</text><text y="-10" fill="#ffcd00" id="nyeYear">2027</text></g></g>'
    ny+='</g>'
    a(ny)
    return '\n    <!-- seasonal decorations at The Farke & Firkin -->\n    <g transform="translate(-5 36) scale(0.95)" id="season">'+''.join(G)+'</g>\n'

css='''  #season>g{display:none}
  #season #planters{display:inline}
  .flame{transform-box:fill-box;transform-origin:50% 100%;animation:flick .5s ease-in-out infinite alternate}
  .flame.f1{animation-duration:.37s}.flame.f2{animation-duration:.43s;animation-delay:-.2s}.flame.f3{animation-duration:.3s}.flame.f4{animation-duration:.27s}
  @keyframes flick{0%{transform:scale(1,1) skewX(0)}50%{transform:scale(.92,1.08) skewX(3deg)}100%{transform:scale(1.05,.9) skewX(-3deg)}}
  .glowpulse{animation:gp 1.2s ease-in-out infinite alternate}@keyframes gp{to{opacity:.12}}
  .ember{animation:ember 2.4s linear infinite}.e1{animation-delay:.4s}.e2{animation-delay:.8s}.e3{animation-delay:1.2s}.e4{animation-delay:1.6s}.e5{animation-delay:2s}
  @keyframes ember{0%{transform:translate(0,30px);opacity:0}15%{opacity:1}100%{transform:translate(8px,-40px);opacity:0}}
  .treelights{opacity:calc(.55 + .45*var(--night,0))}
  .partylights rect{mix-blend-mode:multiply;animation:party 1.6s steps(1) infinite}.partylights .pl1{animation-delay:-.8s}
  @keyframes party{0%{fill:#ff4dd2}25%{fill:#4dd2ff}50%{fill:#7dff7a}75%{fill:#ffcd00}}
  .bal{animation:bob2 2.5s ease-in-out infinite alternate}@keyframes bob2{to{transform:translateY(-2px)}}
  #fx{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
'''

js=r'''<script>
// seasonal decorations + fireworks (?time=2026-11-05T21:00 to preview)
(function(){
  var m=location.search.match(/[?&]time=([^&]+)/), now=m?new Date(decodeURIComponent(m[1])):new Date();
  var M=now.getMonth(), D=now.getDate(), H=now.getHours(), Y=now.getFullYear();
  var show=function(id){var e=document.getElementById(id); if(e) e.style.display='inline'};
  var nye=(M==11&&D==31)||(M==0&&D==1&&H<4);
  var bonfire=(M==10&&D<=6);
  var xmas=(M==10&&D>=7)||(M==11&&D<=30);
  if(M==9) show('s-pumpkins');
  else if(bonfire) show('s-bonfire');
  else if(xmas){show('s-tree');show('s-holly');
    var start=new Date(Y,10,7), xd=new Date(Y,11,25), t=Math.min(1,Math.max(0,(now-start)/(xd-start)));
    document.getElementById('treeScale').setAttribute('transform','scale('+(0.3+0.7*t).toFixed(3)+')');}
  else if(!nye) show('s-flowers');
  if(nye){show('s-nye'); var y=document.getElementById('nyeYear'); if(y) y.textContent=(M==11?Y+1:Y);}
  if(!(nye||bonfire)) return;
  // fireworks at night
  var hero=document.querySelector('.hero'), c=document.createElement('canvas'); c.id='fx'; hero.insertBefore(c,hero.firstChild);
  var ctx=c.getContext('2d'), P=[], R=[], w, h;
  function size(){var d=Math.min(2,devicePixelRatio||1);w=c.clientWidth;h=c.clientHeight;c.width=w*d;c.height=h*d;ctx.setTransform(d,0,0,d,0,0)}
  size(); addEventListener('resize',size);
  var cols=['#ffcd00','#ff4d4d','#4dd2ff','#ffffff','#7dff7a','#ff8ad8','#ffa53a'];
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  function night(){return parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--night'))||0}
  function frame(){
    ctx.globalCompositeOperation='source-over'; ctx.clearRect(0,0,w,h);
    var n=night(), rate=(nye?0.06:0.03)*n;
    if(!reduce && n>0.3 && Math.random()<rate){
      var side=Math.random()<.5, x=w*(side?0.05+Math.random()*.27:0.68+Math.random()*.27);
      R.push({x:x,y:h*.72,vy:-(6+Math.random()*3),ty:h*(0.12+Math.random()*.3),c:cols[Math.random()*cols.length|0]});
    }
    ctx.globalCompositeOperation='lighter';
    R=R.filter(function(r){r.y+=r.vy;r.vy*=.985;ctx.fillStyle='#ffe9b0';ctx.fillRect(r.x-1,r.y,2,6);
      if(r.y<=r.ty){var k=60+Math.random()*40,sp=2+Math.random()*2.5;for(var i=0;i<k;i++){var a=Math.random()*6.283,v=sp*(.4+Math.random()*.6);P.push({x:r.x,y:r.y,vx:Math.cos(a)*v,vy:Math.sin(a)*v,l:1,c:Math.random()<.2?'#ffffff':r.c})}return false}return true});
    P=P.filter(function(p){p.x+=p.vx;p.y+=p.vy;p.vy+=.035;p.vx*=.985;p.vy*=.985;p.l-=.012;
      if(p.l<=0)return false;ctx.globalAlpha=p.l;ctx.fillStyle=p.c;ctx.beginPath();ctx.arc(p.x,p.y,1.8,0,6.283);ctx.fill();return true});
    ctx.globalAlpha=1; requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
})();
</script>'''

for f in sys.argv[1:]:
    s=open(f).read()
    anchor="    </g>\n\n    <!-- every so often: a prop plane"
    assert anchor in s, f
    s=s.replace(anchor,build()+anchor,1)
    s=s.replace("  .blink{",css+"  .blink{",1)
    s=s.replace("<script>\n// spin the logo faster",js+"\n<script>\n// spin the logo faster",1)
    s=s.replace('.plane,.walker,.ballx{display:none}','.plane,.walker,.ballx{display:none}.flame,.ember,.partylights rect{animation:none}')
    open(f,'w').write(s)
    print("ok",f)
