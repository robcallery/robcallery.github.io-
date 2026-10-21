from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch()
    for w,h in [(1280,800),(1024,640),(390,844),(1366,650)]:
        pg=b.new_page(viewport={'width':w,'height':h}); pg.goto('http://localhost:8765/travel-guides/'); pg.wait_for_timeout(1200)
        r=pg.evaluate("""()=>[...document.querySelectorAll('.page')].filter(e=>e.scrollHeight>e.clientHeight+2||[...e.querySelectorAll('*')].some(c=>c.scrollHeight>c.clientHeight+2&&getComputedStyle(c).overflow!='visible')).map(e=>e.textContent.slice(0,30)+' '+e.clientHeight+'/'+e.scrollHeight)""")
        print(w,h,len(r),r[:12])
    b.close()
