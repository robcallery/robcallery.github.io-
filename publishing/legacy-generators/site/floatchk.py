import json, base64, io
from playwright.sync_api import sync_playwright
from PIL import Image
D='/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/'
items=json.load(open(D+'magenta.json'))
res=[]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':400,'height':320})
    for it in items:
        svg=it['svg'].replace('preserveAspectRatio="xMidYMid slice"','width="400" height="320"')
        pg.set_content('<html><body style="margin:0">'+svg+'</body></html>'); 
        img=Image.open(io.BytesIO(pg.screenshot())).convert('RGB'); px=img.load()
        def mag(x,y):
            r,g,bb=px[x,y]; return r>230 and g<40 and bb>230
        score=0; ys=[]; gaps=[]
        rowfull=[sum(1 for xx in range(0,400,4) if not mag(xx,yy))/100 for yy in range(320)]
        for x in range(0,400,2):
            col=[mag(x,y) for y in range(320)]
            y=0
            while y<320:
                if col[y] and y>0 and not col[y-1] and y>140:
                    y2=y
                    while y2<320 and col[y2]: y2+=1
                    if y2<318 and (y2-y)>=3 and not any(col[y2:]) and rowfull[y2]>=0.9:   # sky gap, then solid all the way down
                        score+=(y2-y); ys.append(y); gaps.append((x,y,y2))
                    y=y2
                else: y+=1
        res.append((score,it['c'],(min(ys),max(ys)) if ys else None))
        if score>40:
            pg.set_content('<html><body style="margin:0">'+it['svg'].replace('fill="#ff00ff"','fill="#bfe3f5"').replace('preserveAspectRatio="xMidYMid slice"','width="400" height="320"')+'</body></html>')
            im=Image.open(io.BytesIO(pg.screenshot())).convert('RGB'); q=im.load()
            for x,y1,y2 in gaps:
                for yy in range(y1,y2):
                    for dx in (0,1): q[x+dx,yy]=(255,0,0)
            im.save(D+'fl/'+''.join(ch for ch in it['c'] if ch.isalnum())+'.png')
    b.close()
res.sort(reverse=True)
json.dump(res,open(D+'float_res.json','w'))
for s,c,r in res:
    if s>0: print(s,c,r)
