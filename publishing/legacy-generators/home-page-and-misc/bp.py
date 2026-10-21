from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
CHK="""(()=>{const r=[];document.querySelectorAll('.leaf .page').forEach((p,i)=>{if(p.scrollHeight>p.clientHeight+1)r.push(i)});return r})()"""
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={"width":1280,"height":800},device_scale_factor=1); errs=[]
    pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto("http://localhost:8765/beer-passport/"); pg.wait_for_timeout(1800)
    print("overflow",pg.evaluate(CHK),errs, pg.inner_text("#count"))
    shots=[]
    for n in range(1,19):
        pg.click("#next"); pg.wait_for_timeout(1100)
        if n in (1,6,10,14,16): pg.screenshot(path=out+f"bp_{n}.png"); shots.append(n)
    print(pg.inner_text("#count"), pg.is_disabled("#next"))
    m=b.new_page(viewport={"width":390,"height":844}); m.goto("http://localhost:8765/beer-passport/"); m.wait_for_timeout(1800)
    print("m overflow",m.evaluate(CHK))
    for n in range(28): m.click("#next"); m.wait_for_timeout(1000)
    m.screenshot(path=out+"bp_m.png"); print(m.inner_text("#count"))
    b.close()
