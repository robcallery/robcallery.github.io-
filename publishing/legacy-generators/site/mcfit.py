from playwright.sync_api import sync_playwright
import sys
D='/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/'
for mode in ([],['live']):
    sys.argv=['x']+mode
    exec(open(D+'mcmock.py').read().split('with sync_playwright()')[0])
    with sync_playwright() as p:
        b=p.chromium.launch()
        for big in (False, True):
            for w,hh in [(1920,1080),(1536,730),(1366,768),(1280,800),(1440,900),(1024,640)]:
                pg=b.new_page(viewport={'width':w,'height':hh})
                pg.route('**/*',lambda r: h(r) if ('espn' in r.request.url) else r.continue_())
                pg.goto('http://localhost:8765/match-hub/leeds/'); pg.wait_for_timeout(2500)
                if big: pg.add_style_tag(content=".stage{font-family:'DejaVu Sans','Verdana',sans-serif!important;line-height:1.35!important} .stage *{line-height:inherit}")
                pg.wait_for_timeout(300)
                r=pg.evaluate("""(()=>{const c=[...document.querySelectorAll('.right .card-box')].pop().getBoundingClientRect();
                  const rs=[...document.querySelectorAll('#table .tr')];const last=rs[rs.length-1].getBoundingClientRect();
                  const tk=document.querySelector('.ticker').getBoundingClientRect();
                  const s=document.getElementById('scores').getBoundingClientRect();const g=[...document.querySelectorAll('#scores .g')].pop();
                  return {rows:rs.length-1, lastInside: last.bottom<=c.bottom+0.5, cardAboveTicker: c.bottom<=tk.top+0.5, lastText: rs[rs.length-1].innerText.replace(/\\s+/g,' ').slice(0,18),
                          scoresOk: !g || g.getBoundingClientRect().bottom<=s.bottom+0.5, rowH: Math.round(rs[5].getBoundingClientRect().height)}})()""")
                print(mode, 'BIGFONT' if big else 'normal', w, hh, r)
                if big and w==1536: pg.screenshot(path=D+f'mcfit_{"live" if mode else "pre"}.png')
                pg.close()
        b.close()
