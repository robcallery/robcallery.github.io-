from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch()
    for w,h in [(1280,800),(1024,640),(390,844),(1366,650)]:
        pg=b.new_page(viewport={'width':w,'height':h}); errs=[]
        pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.goto('http://localhost:8765/travel-guides/'); pg.wait_for_timeout(1500)
        r=pg.evaluate("""()=>{let bad=[];document.querySelectorAll('.page').forEach(pp=>{const q=pp.getBoundingClientRect();if(!q.height)return;pp.querySelectorAll('*').forEach(el=>{const a=el.getBoundingClientRect();if(a.width&&a.height&&(a.bottom>q.bottom+1||a.right>q.right+1))bad.push((pp.textContent.slice(0,40))+' :: '+(el.className||el.tagName))})});return [document.querySelectorAll('.page').length,[...new Set(bad)].slice(0,10)]}""")
        print(w,h,r,errs)
    b.close()
