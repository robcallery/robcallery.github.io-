from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1280,"height":800},device_scale_factor=2)
    pg.goto("http://localhost:8765/football-tales/"); pg.wait_for_timeout(800)
    pg.screenshot(path="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/packz.png",clip={"x":160,"y":90,"width":330,"height":430})
    b.close()
