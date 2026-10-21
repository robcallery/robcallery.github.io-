from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
def walk(pg):
    seen=[pg.inner_text("#count")]
    for i in range(8):
        if pg.is_disabled("#next"): break
        pg.click("#next"); pg.wait_for_timeout(1150); seen.append(pg.inner_text("#count"))
    return seen
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={"width":1280,"height":800}); errs=[]
    pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto("http://localhost:8765/travel-guides/?demo"); pg.wait_for_timeout(200); pg.screenshot(path=out+"tg_closed.png")
    pg.wait_for_timeout(1700); pg.screenshot(path=out+"tg_open.png")
    pg.click("#next"); pg.wait_for_timeout(1200); pg.screenshot(path=out+"tg_s2.png")
    print(walk(pg)); pg.screenshot(path=out+"tg_end.png"); print(errs)
    m=b.new_page(viewport={"width":390,"height":844}); m.goto("http://localhost:8765/travel-guides/?demo"); m.wait_for_timeout(1700); m.click("#next"); m.wait_for_timeout(1200); m.screenshot(path=out+"tg_m.png"); print(walk(m))
    r=b.new_page(viewport={"width":1280,"height":800}); r.goto("http://localhost:8765/travel-guides/"); r.wait_for_timeout(1700); r.screenshot(path=out+"tg_real.png"); print(walk(r))
    h=b.new_page(viewport={"width":1280,"height":800}); h.goto("http://localhost:8765/explore/"); h.wait_for_timeout(800); h.click(".item-travel-guides"); h.wait_for_timeout(750); h.screenshot(path=out+"tg_flick.png",clip={"x":330,"y":230,"width":320,"height":360}); h.wait_for_timeout(1000); print("hub ->",h.url)
    b.close()
