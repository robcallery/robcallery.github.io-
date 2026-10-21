import sys
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1024,'height':640})
    pg.goto('http://localhost:8765/travel-guides/'); pg.wait_for_timeout(1500)
    for i,t in enumerate(sys.argv[1:]):
        h=pg.evaluate_handle("""(t)=>{const all=[...document.querySelectorAll('.page')].filter(e=>e.textContent.includes(t));const el=all[all.length-1];
          const c=el.cloneNode(true);const w=document.createElement('div');w.style.cssText='position:fixed;left:0;top:0;z-index:99999;width:'+el.offsetWidth+'px;height:'+el.offsetHeight+'px;overflow:visible';
          c.style.cssText+=';transform:none;position:relative;left:0;top:0;visibility:visible;opacity:1;backface-visibility:visible';w.appendChild(c);document.querySelectorAll('.shotw').forEach(x=>x.remove());w.className='shotw';document.body.appendChild(w);return w}""",t)
        pg.wait_for_timeout(200); h.as_element().screenshot(path=f'/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/g{i}.png')
    b.close()
