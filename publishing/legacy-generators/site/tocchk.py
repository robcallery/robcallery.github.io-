import sys
from playwright.sync_api import sync_playwright
sys.path.insert(0,'/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad')
from shelves import SHELVES
JS="""()=>[...document.querySelectorAll('.page.contents')].filter(p=>p.getBoundingClientRect().height>0).map(p=>{const r=[];const b=p.getBoundingClientRect();
 const last=[...p.children].reduce((m,c)=>Math.max(m,c.getBoundingClientRect().bottom),0);
 const foot=p.querySelector('.foot');const ul=p.querySelector('.toc');
 return {over:p.scrollHeight-p.clientHeight, ulBottom: ul?Math.round(ul.getBoundingClientRect().bottom-(foot?foot.getBoundingClientRect().top:b.bottom)):0}})"""
bad=[];allw=[]
with sync_playwright() as p:
    b=p.chromium.launch()
    for w,h in [(1280,800),(1366,650),(1920,1080),(1024,640),(390,844),(375,667),(820,1180)]:
        pg=b.new_page(viewport={'width':w,'height':h})
        for sid,*_ in SHELVES:
            pg.goto(f'http://localhost:{sys.argv[1]}/travel-guides/guide/?shelf={sid}'); pg.wait_for_timeout(700)
            worst=-999
            for k in range(8):
                for r in pg.evaluate(JS):
                    worst=max(worst,r['ulBottom']+(1000 if r['over']>0 else 0))
                if 'Contents' not in pg.inner_text('#count') and k>0: break
                pg.keyboard.press('ArrowRight'); pg.wait_for_timeout(250)
            allw.append((w,h,sid,worst))
            if worst>-12: bad.append((w,h,sid,worst))
        pg.close()
    b.close()
print('problems:',bad)
print('closest gap px:',max(x[3] for x in allw))
