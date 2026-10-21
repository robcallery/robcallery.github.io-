from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
with sync_playwright() as p:
    b=p.chromium.launch()
    for n,w,h in [("a",1280,800),("b",1920,1080),("c",1024,768),("d",920,700),("e",390,844)]:
        pg=b.new_page(viewport={"width":w,"height":h}); pg.goto("file:///home/claude/index.html"); pg.wait_for_timeout(300)
        pg.evaluate("document.getAnimations().forEach(a=>{ if(a.animationName&&a.animationName.startsWith('w')) a.currentTime=(a.effect.getTiming().delay||0)+5000 })")
        pg.wait_for_timeout(100); pg.screenshot(path=out+n+".png")
    b.close()
