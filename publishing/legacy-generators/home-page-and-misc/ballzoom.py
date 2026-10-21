from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1280,"height":800},device_scale_factor=4)
    pg.goto("file:///home/claude/index.html?time=2026-10-19T12:00:00Z"); pg.wait_for_timeout(1500)
    pg.evaluate("document.getAnimations().forEach(a=>{if(['ballx','bally','spinball'].includes(a.animationName)){a.pause();a.currentTime=a.animationName=='spinball'?0:14000}})")
    pg.wait_for_timeout(100)
    r=pg.evaluate("(()=>{const b=document.querySelector('.ballspin').getBoundingClientRect();return [b.x,b.y,b.width,b.height]})()")
    pg.screenshot(path=out+"ballzoom.png",clip={"x":r[0]-6,"y":r[1]-6,"width":r[2]+12,"height":r[3]+12})
    b.close()
