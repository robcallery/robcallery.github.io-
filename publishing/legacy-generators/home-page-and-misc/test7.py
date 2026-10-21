from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1280,"height":800})
    pg.goto("file:///home/claude/index.html?time=2026-10-19T12:00:00Z"); pg.wait_for_timeout(1500)
    rate=lambda: pg.evaluate("document.querySelector('.logo .globe').getAnimations()[0].playbackRate")
    print("idle rate",rate())
    found=None
    for t in range(0,6000,100):
        pg.evaluate(f"document.getAnimations().forEach(a=>{{if(a.animationName=='fly1'){{a.pause();a.currentTime=3000+{t}}}}})")
        pg.wait_for_timeout(60)
        if rate()==5: found=t; break
    print("fast when fly1 at",found, "rate",rate())
    pg.screenshot(path=out+"plane_hit.png",clip={"x":380,"y":0,"width":520,"height":320})
    pg.evaluate("document.getAnimations().forEach(a=>{if(a.animationName=='fly1'){a.currentTime=3000+15000}})"); pg.wait_for_timeout(150)
    print("after pass rate",rate())
    pg.screenshot(path=out+"pub.png",clip={"x":0,"y":440,"width":340,"height":300})
    b.close()
