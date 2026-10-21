import sys
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch()
    for w,h,pg_ in [(1280,800,2),(1280,800,3),(1280,800,30)]:
        pg=b.new_page(viewport={'width':w,'height':h}); pg.goto(f'http://localhost:8765/travel-guides/?page={pg_}'); pg.wait_for_timeout(2500)
        pg.screenshot(path=f'{sys.argv[1]}/m{w}_{pg_}.png')
    b.close()
