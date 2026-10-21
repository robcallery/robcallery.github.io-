from playwright.sync_api import sync_playwright
from PIL import Image
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1280,"height":800})
    pg.goto("http://localhost:8765/explore/"); pg.wait_for_timeout(800)
    pg.evaluate("document.querySelector('.item-beer-passport').addEventListener('click',e=>e.stopImmediatePropagation(),true)")
    pg.evaluate("document.querySelector('.item-beer-passport').classList.add('flick')")
    fr=[]
    for t in range(0,1400,175):
        pg.screenshot(path=out+f"fl{t}.png",clip={"x":20,"y":230,"width":330,"height":360}); fr.append(out+f"fl{t}.png"); pg.wait_for_timeout(175)
    ims=[Image.open(f) for f in fr]; o=Image.new('RGB',(330*len(ims),360)); [o.paste(im,(i*330,0)) for i,im in enumerate(ims)]; o.save(out+"flick_strip.png")
    pg=b.new_page(viewport={"width":1280,"height":800}); pg.goto("http://localhost:8765/beer-passport/")
    fr=[]
    for t in range(0,1800,200):
        pg.screenshot(path=out+f"op{t}.png",clip={"x":200,"y":60,"width":880,"height":600}); fr.append(out+f"op{t}.png"); pg.wait_for_timeout(200)
    ims=[Image.open(f).resize((440,300)) for f in fr]; o=Image.new('RGB',(440*3,300*3)); [o.paste(im,((i%3)*440,(i//3)*300)) for i,im in enumerate(ims)]; o.save(out+"open_strip.png")
    b.close()
