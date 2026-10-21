from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1440,"height":900},device_scale_factor=2)
    pg.goto("http://localhost:8765/explore/"); pg.wait_for_timeout(1000)
    pg.screenshot(path="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/hub_1440.png")
    r=pg.evaluate("(()=>{const e=document.querySelector('.telly').getBoundingClientRect();return [e.x,e.y,e.width,e.height]})()")
    pg.screenshot(path="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/tvz.png",clip={"x":r[0]-10,"y":r[1]-10,"width":r[2]+20,"height":r[3]+20})
    b.close()
