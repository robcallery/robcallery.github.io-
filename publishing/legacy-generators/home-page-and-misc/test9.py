from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1280,"height":800})
    pg.goto("file:///home/claude/index.html?time=2026-10-19T12:00:00Z"); pg.wait_for_timeout(1500)
    for t in [12600,14000,15400,24000]:
        pg.evaluate(f"document.getAnimations().forEach(a=>{{if(['ballx','bally'].includes(a.animationName)){{a.pause();a.currentTime={t}}}}})")
        pg.wait_for_timeout(80); pg.screenshot(path=out+f"ball{t}.png",clip={"x":300,"y":280,"width":680,"height":200})
    b.close()
