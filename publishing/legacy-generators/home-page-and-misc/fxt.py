from playwright.sync_api import sync_playwright
import json
out="/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/"
espn={"events":[
 {"date":"2026-10-25T16:30Z","competitions":[{"date":"2026-10-25T16:30Z","status":{"type":{"state":"pre"}},"competitors":[{"homeAway":"home","team":{"id":"366","shortDisplayName":"Sunderland"}},{"homeAway":"away","team":{"id":"357","shortDisplayName":"Leeds"}}]}]},
 {"date":"2026-11-08T15:00Z","competitions":[{"date":"2026-11-08T15:00Z","status":{"type":{"state":"pre"}},"competitors":[{"homeAway":"home","team":{"id":"357","shortDisplayName":"Leeds"}},{"homeAway":"away","team":{"id":"371","shortDisplayName":"Nottm Forest"}}]}]}]}
with sync_playwright() as p:
    b=p.chromium.launch()
    for n,t in [("fx1","2026-10-20T19:00:00"),("fx2","2026-11-08T15:40:00")]:
        pg=b.new_page(viewport={"width":1280,"height":800},device_scale_factor=2)
        pg.route("**/site.api.espn.com/**",lambda r:r.fulfill(status=200,content_type="application/json",body=json.dumps(espn),headers={"access-control-allow-origin":"*"}))
        pg.route("**/api.open-meteo.com/**",lambda r:r.abort())
        pg.goto(f"file:///home/claude/index.html?time={t}&weather=clear"); pg.wait_for_timeout(2500)
        pg.screenshot(path=out+n+".png",clip={"x":0,"y":540,"width":640,"height":260})
    b.close()
