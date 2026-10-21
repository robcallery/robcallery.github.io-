from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
with sync_playwright() as p:
    b=p.chromium.launch()
    for n,t in [("xn","2026-12-20T21:00:00"),("xd","2026-12-20T13:00:00"),("oct","2026-10-20T21:00:00")]:
        pg=b.new_page(viewport={"width":1280,"height":800},device_scale_factor=2); errs=[]
        pg.on("pageerror",lambda e:errs.append(str(e)))
        pg.goto(f"file:///home/claude/index.html?time={t}&weather=clear"); pg.wait_for_timeout(2500)
        pg.screenshot(path=out+f"{n}.png",clip={"x":0,"y":420,"width":1280,"height":380}); print(n,errs)
    b.close()
