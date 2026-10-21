from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
with sync_playwright() as p:
    b=p.chromium.launch()
    for url in ("beer-passport","travel-guides"):
        pg=b.new_page(viewport={"width":1280,"height":800}); errs=[]
        pg.on("pageerror",lambda e:errs.append(str(e)))
        pg.goto(f"http://localhost:8765/{url}/"); pg.wait_for_timeout(1700)
        if url=="travel-guides": pg.screenshot(path=out+"g_open.png")
        seen=[pg.inner_text("#count")]
        for i in range(4): pg.click("#next"); pg.wait_for_timeout(1050); seen.append(pg.inner_text("#count"))
        pg.evaluate("for(let i=0;i<80;i++)document.getElementById(\"next\").click()"); pg.wait_for_timeout(1500)
        seen.append(pg.inner_text("#count"))
        pg.click("#prev"); pg.wait_for_timeout(1000)
        for i in range(12):
            if pg.is_disabled("#prev"): break
            pg.click("#prev"); pg.wait_for_timeout(250)
        seen.append(pg.inner_text("#count"))
        print(url,seen,errs)
    b.close()
