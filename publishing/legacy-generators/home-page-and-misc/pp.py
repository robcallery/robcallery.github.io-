from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={"width":1280,"height":800}); errs=[]
    pg.on("pageerror",lambda e:errs.append(str(e))); pg.on("console",lambda m: m.type=="error" and errs.append(m.text))
    pg.goto("http://localhost:8765/beer-passport/?demo"); pg.wait_for_timeout(200); pg.screenshot(path=out+"pp_closed.png")
    pg.wait_for_timeout(1700); pg.screenshot(path=out+"pp_open.png"); print(pg.inner_text("#count"))
    pg.click("#next"); pg.wait_for_timeout(450); pg.screenshot(path=out+"pp_turning.png")
    pg.wait_for_timeout(900); pg.screenshot(path=out+"pp_spread2.png"); print(pg.inner_text("#count"))
    pg.keyboard.press("ArrowRight"); pg.wait_for_timeout(1300); pg.screenshot(path=out+"pp_spread3.png"); print(pg.inner_text("#count"), pg.is_disabled("#next"))
    print("errs",errs)
    m=b.new_page(viewport={"width":390,"height":844}); m.goto("http://localhost:8765/beer-passport/?demo"); m.wait_for_timeout(1800); m.screenshot(path=out+"pp_m1.png")
    m.click("#next"); m.wait_for_timeout(1300); m.screenshot(path=out+"pp_m2.png"); print(m.inner_text("#count"))
    e=b.new_page(viewport={"width":1280,"height":800}); e.goto("http://localhost:8765/beer-passport/"); e.wait_for_timeout(1700); e.click("#next"); e.wait_for_timeout(1300); e.screenshot(path=out+"pp_empty.png"); print(e.inner_text("#count"))
    h=b.new_page(viewport={"width":1280,"height":800}); h.goto("http://localhost:8765/explore/"); h.wait_for_timeout(800)
    h.click(".item-beer-passport"); 
    for t in (300,700,1000): h.wait_for_timeout(t- (0 if t==300 else (300 if t==700 else 700))); h.screenshot(path=out+f"flick{t}.png",clip={"x":40,"y":230,"width":320,"height":360})
    h.wait_for_timeout(800); print("hub ->",h.url)
    b.close()
