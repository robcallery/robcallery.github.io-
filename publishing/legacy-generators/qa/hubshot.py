from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
with sync_playwright() as p:
    b=p.chromium.launch()
    for n,url,w,h in [("hub_d","/explore/",1280,800),("hub_m","/explore/",390,844),("soon_d","/football-tales/",1280,800),("soon_m","/beer-passport/",390,844)]:
        pg=b.new_page(viewport={"width":w,"height":h}); errs=[]
        pg.on("pageerror",lambda e:errs.append(str(e)))
        pg.goto("http://localhost:8765"+url); pg.wait_for_timeout(1500)
        pg.screenshot(path=out+n+".png",full_page=True); print(n,errs)
    pg=b.new_page(viewport={"width":1280,"height":800}); pg.goto("http://localhost:8765/explore/"); pg.wait_for_timeout(800)
    pg.hover(".item:nth-child(2)"); pg.wait_for_timeout(500); pg.screenshot(path=out+"hub_hover.png")
    pg=b.new_page(viewport={"width":1280,"height":800}); pg.goto("http://localhost:8765/?weather=clear"); pg.wait_for_timeout(800)
    pg.click(".enter"); pg.wait_for_timeout(600); print("after click:",pg.url)
    b.close()
