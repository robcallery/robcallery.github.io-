from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
with sync_playwright() as p:
    b=p.chromium.launch()
    for n,w,h in [("b1",1280,800),("b2",1920,1080),("b3",1366,650),("b4",390,844)]:
        pg=b.new_page(viewport={"width":w,"height":h}); pg.route("**/api.open-meteo.com/**",lambda r:r.abort())
        pg.goto("file:///home/claude/index.html?time=2026-10-20T13:00:00&weather=partly"); pg.wait_for_timeout(2500); pg.screenshot(path=out+n+".png")
    b.close()
