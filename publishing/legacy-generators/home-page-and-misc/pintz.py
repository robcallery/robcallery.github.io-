from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1280,"height":800},device_scale_factor=2)
    pg.goto("file:///home/claude/index.html?time=2026-10-19T12:00:00Z&weather=clear"); pg.wait_for_timeout(1500)
    pg.evaluate("document.getAnimations().forEach(a=>{if(a.animationName=='globeSpin'||a.animationName=='pintSpin'){a.pause();a.currentTime=8000}})")
    pg.wait_for_timeout(100); pg.screenshot(path="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/pintz.png",clip={"x":500,"y":30,"width":280,"height":250})
    b.close()
