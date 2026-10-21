from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1280,"height":800})
    pg.goto("file:///home/claude/index.html?time=2026-10-19T12:00:00Z"); pg.wait_for_timeout(1500)
    for t in [3500,20000,44000]:
        pg.evaluate(f"document.getAnimations().forEach(a=>{{if(/^ts\\d/.test(a.animationName)){{a.pause();a.currentTime={t}}}}})")
        pg.wait_for_timeout(100); pg.screenshot(path=out+f"ts{t}.png",clip={"x":0,"y":420,"width":1280,"height":380})
    b.close()
