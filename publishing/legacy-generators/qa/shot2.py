from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={"width":1280,"height":800})
    pg.goto("file:///home/claude/index.html"); pg.wait_for_timeout(500)
    # jump animations so both planes are mid-flight
    pg.evaluate("""document.getAnimations().forEach(a=>{const n=a.animationName; if(n=='fly1')a.currentTime=3000+2800; if(n=='fly2')a.currentTime=14000+3500;})""")
    pg.wait_for_timeout(100); pg.screenshot(path=out+"desk2.png")
    m=b.new_page(viewport={"width":390,"height":844}); m.goto("file:///home/claude/index.html"); m.wait_for_timeout(500); m.screenshot(path=out+"mob2.png")
    b.close()
