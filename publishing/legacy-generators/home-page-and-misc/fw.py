from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1280,"height":800})
    pg.goto("file:///home/claude/index.html?time=2026-11-05T21:00:00&weather=clear"); 
    best=0
    for i in range(14):
        pg.wait_for_timeout(700)
        n=pg.evaluate("(()=>{const c=document.getElementById('fx');const d=c.getContext('2d').getImageData(0,0,c.width,c.height).data;let k=0;for(let i=3;i<d.length;i+=4)if(d[i]>0)k++;return k})()")
        if n>best: best=n; pg.screenshot(path=out+"fw.png")
    print("max lit px",best)
    b.close()
