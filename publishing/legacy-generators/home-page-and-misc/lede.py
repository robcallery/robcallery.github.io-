from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
with sync_playwright() as p:
    b=p.chromium.launch()
    for n,t,w in [("l_day","2026-06-21T12:00:00","clear"),("l_dusk","2026-10-20T17:55:00","clear"),("l_night","2026-10-20T22:00:00","clear"),("l_fog","2026-10-20T12:00:00","fog"),("l_sunset","2026-10-20T17:15:00","clear")]:
        pg=b.new_page(viewport={"width":1280,"height":800}); errs=[]
        pg.on("pageerror",lambda e:errs.append(str(e)))
        pg.route("**/site.api.espn.com/**",lambda r:r.abort())
        pg.goto(f"file:///home/claude/index.html?time={t}&weather={w}"); pg.wait_for_timeout(3500)
        c=pg.evaluate("getComputedStyle(document.querySelector('.lede')).color")
        pg.screenshot(path=out+n+".png",clip={"x":0,"y":240,"width":1280,"height":120}); print(n,c,errs)
    b.close()
