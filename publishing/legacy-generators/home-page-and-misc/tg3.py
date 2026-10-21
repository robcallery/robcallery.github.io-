from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
CHK="""(()=>{const r=[];document.querySelectorAll('.leaf .page').forEach((p,i)=>{if(p.scrollHeight>p.clientHeight+1)r.push(i+':'+(p.querySelector('h2')||{}).textContent+' +'+(p.scrollHeight-p.clientHeight))});return r})()"""
with sync_playwright() as p:
    b=p.chromium.launch()
    for w,h,tag in [(1280,800,'d'),(1440,900,'L'),(390,844,'m'),(1024,640,'s')]:
        pg=b.new_page(viewport={"width":w,"height":h}); errs=[]
        pg.on("pageerror",lambda e:errs.append(str(e)))
        pg.goto("http://localhost:8765/travel-guides/"); pg.wait_for_timeout(1800)
        print(tag,"overflow:",pg.evaluate(CHK),errs)
        if tag=='d':
            pg.screenshot(path=out+"g_toc.png")
            for n in range(2,8): pg.evaluate(f"document.querySelector('#next').click()"); pg.wait_for_timeout(1150); pg.screenshot(path=out+f"g_{n}.png")
        if tag=='m':
            pg.click("#next"); pg.wait_for_timeout(1150); pg.screenshot(path=out+"g_m.png")
    b.close()
