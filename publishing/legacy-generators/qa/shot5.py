from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
with sync_playwright() as p:
    b=p.chromium.launch()
    for n,w,h,t in [("bp1",1280,800,"2026-10-19T12:00:00Z"),("bp2",1280,800,"2026-10-19T21:00:00Z"),("bp3",390,844,"2026-10-19T12:00:00Z")]:
        pg=b.new_page(viewport={"width":w,"height":h}); pg.goto("file:///home/claude/index.html?time="+t); pg.wait_for_timeout(2500)
        pg.evaluate("document.getAnimations().forEach(a=>{if(a.animationName=='fly3')a.currentTime=9000+14000})")
        pg.wait_for_timeout(100); pg.screenshot(path=out+n+".png")
    b.close()
