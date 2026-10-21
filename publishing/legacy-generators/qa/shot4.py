from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
times={"t1":"2026-10-19T09:00:00Z","t2":"2026-10-19T12:00:00Z","t3":"2026-10-19T16:50:00Z","t4":"2026-10-19T17:20:00Z","t5":"2026-10-19T21:00:00Z"}
with sync_playwright() as p:
    b=p.chromium.launch()
    for n,t in times.items():
        pg=b.new_page(viewport={"width":1280,"height":800}); pg.goto("file:///home/claude/index.html?time="+t); pg.wait_for_timeout(2500); pg.screenshot(path=out+n+".png")
    for n,w,h in [("big",1920,1080),("mob",390,844),("mid",920,700)]:
        pg=b.new_page(viewport={"width":w,"height":h}); pg.goto("file:///home/claude/index.html?time=2026-10-19T21:00:00Z"); pg.wait_for_timeout(2500); pg.screenshot(path=out+n+".png")
    b.close()
