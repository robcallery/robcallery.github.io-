from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1280,'height':800})
    pg.goto('http://localhost:8765/beer-passport/'); pg.wait_for_timeout(1500)
    h=pg.evaluate_handle("""()=>{const el=[...document.querySelectorAll('.page')].find(e=>e.textContent.includes("Foster's Premium"));
      const c=el.cloneNode(true);const r=el.getBoundingClientRect();
      const w=document.createElement('div');w.style.cssText='position:fixed;left:0;top:0;z-index:99999;width:'+(el.offsetWidth||500)+'px;height:'+(el.offsetHeight||640)+'px';
      c.style.cssText+=';transform:none;position:relative;left:0;top:0;visibility:visible;opacity:1;backface-visibility:visible';w.appendChild(c);document.body.appendChild(w);return w}""")
    pg.wait_for_timeout(300); h.as_element().screenshot(path='/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/fosters.png')
    b.close()
