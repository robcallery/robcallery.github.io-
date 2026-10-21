from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
def walk(pg,label):
    seen=[pg.inner_text("#count")]
    for i in range(8):
        if pg.is_disabled("#next"): break
        pg.click("#next"); pg.wait_for_timeout(1150); seen.append(pg.inner_text("#count"))
    print(label,seen)
with sync_playwright() as p:
    b=p.chromium.launch()
    for q,w,h in [("?demo",1280,800),("",1280,800),("?demo",390,844),("",390,844)]:
        pg=b.new_page(viewport={"width":w,"height":h}); errs=[]
        pg.on("pageerror",lambda e:errs.append(str(e)))
        pg.goto("http://localhost:8765/beer-passport/"+q); pg.wait_for_timeout(1700)
        walk(pg,f"{w}{q or ' real'}"); pg.screenshot(path=out+f"end_{w}{q.strip('?') or 'real'}.png")
        if errs: print(errs)
    pg=b.new_page(viewport={"width":1280,"height":800}); pg.goto("http://localhost:8765/beer-passport/"); pg.wait_for_timeout(1700); pg.screenshot(path=out+"real_open.png",clip={"x":240,"y":560,"width":800,"height":90})
    b.close()
