from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1280,"height":800}); errs=[]
    pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto("http://localhost:8765/travel-guides/"); pg.wait_for_timeout(1800)
    pg.screenshot(path=out+"k_toc1.png"); pg.click("#next"); pg.wait_for_timeout(1150); pg.screenshot(path=out+"k_toc2.png")
    seen=[]
    for i in range(40):
        if pg.is_disabled("#next"): break
        pg.click("#next"); pg.wait_for_timeout(1050); seen.append(pg.inner_text("#count"))
        if i==9: pg.screenshot(path=out+"k_mid.png")
        if i==21: pg.screenshot(path=out+"k_abroad.png")
    print(seen[:3],seen[-3:],len(seen),errs)
    m=b.new_page(viewport={"width":390,"height":844}); m.goto("http://localhost:8765/travel-guides/"); m.wait_for_timeout(1800)
    s=[]
    for i in range(70):
        if m.is_disabled("#next"): break
        m.click("#next"); m.wait_for_timeout(950); s.append(m.inner_text("#count"))
    print(s[:5], s[-3:], len(s))
    b.close()
