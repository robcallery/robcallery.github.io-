from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1920,"height":1080}); errs=[]
    pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto("file:///home/claude/starting-soon.html?time=2026-10-19T21:00:00Z"); 
    pg.wait_for_timeout(2500); pg.screenshot(path=out+"ss_a.png")
    pg.wait_for_timeout(2600); pg.screenshot(path=out+"ss_mid.png",clip={"x":500,"y":620,"width":920,"height":200})
    pg.wait_for_timeout(3000); pg.screenshot(path=out+"ss_b.png")
    print(errs)
    b.close()
