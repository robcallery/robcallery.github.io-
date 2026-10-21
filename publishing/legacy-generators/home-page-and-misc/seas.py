from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
cases=[("oct","2026-10-25T21:00:00"),("bonfire","2026-11-05T21:00:00"),("tree1","2026-11-10T21:00:00"),("tree2","2026-12-22T21:00:00"),("nye","2026-12-31T22:00:00"),("june","2026-06-10T13:00:00")]
with sync_playwright() as p:
    b=p.chromium.launch()
    for n,t in cases:
        pg=b.new_page(viewport={"width":1280,"height":800}); errs=[]
        pg.on("pageerror",lambda e:errs.append(str(e)))
        pg.goto(f"file:///home/claude/index.html?time={t}&weather=clear"); pg.wait_for_timeout(4500)
        pg.screenshot(path=out+f"s_{n}.png",clip={"x":0,"y":380,"width":560,"height":420})
        if n in("bonfire","nye"): pg.screenshot(path=out+f"sfull_{n}.png")
        print(n,errs)
    b.close()
