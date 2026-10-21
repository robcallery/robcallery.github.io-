from playwright.sync_api import sync_playwright
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
def walk(pg,shots=None):
    seen=[pg.inner_text("#count")]
    for i in range(30):
        if pg.is_disabled("#next"): break
        pg.click("#next"); pg.wait_for_timeout(1100); seen.append(pg.inner_text("#count"))
        if shots and i in shots: pg.screenshot(path=out+shots[i])
    return seen
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={"width":1280,"height":800}); pg.goto("http://localhost:8765/travel-guides/"); pg.wait_for_timeout(1800); pg.screenshot(path=out+"j_toc.png")
    print(walk(pg,{6:"j_jp.png",8:"j_us1.png",9:"j_us2.png"}))
    m=b.new_page(viewport={"width":390,"height":844}); m.goto("http://localhost:8765/travel-guides/"); m.wait_for_timeout(1800); print(walk(m))
    b.close()
