from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
cases=[("partly","2026-10-19T12:00:00Z"),("rain","2026-10-19T12:00:00Z"),("snow","2026-10-19T21:00:00Z"),("fog","2026-10-19T09:00:00Z"),("storm","2026-10-19T16:50:00Z"),("cloudy","2026-10-19T21:00:00Z")]
with sync_playwright() as p:
    b=p.chromium.launch()
    for wx,t in cases:
        pg=b.new_page(viewport={"width":1280,"height":800}); errs=[]
        pg.on("pageerror",lambda e:errs.append(str(e)))
        pg.goto(f"file:///home/claude/index.html?time={t}&weather={wx}"); pg.wait_for_timeout(2500)
        pg.screenshot(path=out+f"wx_{wx}.png"); print(wx,errs)
    b.close()
