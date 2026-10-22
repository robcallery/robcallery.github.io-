import json, sys
from playwright.sync_api import sync_playwright
D='/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/'
LIVE = len(sys.argv)>1
def ev(i,date,opp,home,us=None,them=None,state='pre',clock=''):
    us_c={"id":"357","homeAway":"home" if home else "away","team":{"id":"357","displayName":"Leeds United"}}
    th_c={"id":"9"+str(i),"homeAway":"away" if home else "home","team":{"id":"9"+str(i),"displayName":opp}}
    if us is not None: us_c["score"]={"value":us,"displayValue":str(us)}; th_c["score"]={"value":them,"displayValue":str(them)}
    return {"id":str(1000+i),"date":date,"competitions":[{"competitors":[us_c,th_c],"venue":{"fullName":"Elland Road" if home else opp+" Stadium","address":{"city":"Leeds" if home else "Sunderland"}},
      "status":{"displayClock":clock,"type":{"state":state,"completed":state=='post',"shortDetail":"FT" if state=='post' else ''}}}]}
past=[ev(1,"2026-09-14T19:00Z","Newcastle United",True,2,1,'post'),ev(2,"2026-09-20T13:00Z","Crystal Palace",True,1,1,'post'),ev(3,"2026-10-10T11:30Z","Arsenal",False,0,2,'post'),ev(4,"2026-10-18T13:00Z","Manchester United",True,3,1,'post')]
nxt=ev(5,"2026-10-25T16:30Z","Sunderland",False) if not LIVE else ev(5,"2026-10-22T19:30Z","Sunderland",False,1,0,'in',"63'")
fut=[ev(6,"2026-11-01T15:00Z","Coventry City",True),ev(7,"2026-11-08T15:00Z","Everton",False),ev(8,"2026-11-22T15:00Z","Brentford",True)]
teams=["Arsenal","Liverpool","Manchester City","Chelsea","Leeds United","Aston Villa","Newcastle United","Brighton & Hove Albion","Tottenham Hotspur","Fulham"]
ent=[{"team":{"id":"357" if t=="Leeds United" else str(50+k),"displayName":t},"stats":[{"name":"rank","value":k+1},{"name":"gamesPlayed","value":8},{"name":"pointDifferential","value":10-k*2},{"name":"points","value":20-k}]} for k,t in enumerate(teams)]
def h(route):
    u=route.request.url
    if '/standings' in u: body={"children":[{"name":"English Premier League","standings":{"entries":ent}}]} if 'eng.1' in u else {}
    elif 'eng.1/teams/357/schedule?fixture' in u: body={"leagues":[{"name":"Premier League"}],"events":[nxt]+fut}
    elif 'eng.1/teams/357/schedule' in u: body={"leagues":[{"name":"Premier League"}],"events":past}
    elif 'eng.1/scoreboard' in u: body={"leagues":[{"name":"Premier League"}],"events":[nxt] if LIVE else []}
    else: body={"events":[]}
    route.fulfill(status=200,content_type='application/json',body=json.dumps(body),headers={'Access-Control-Allow-Origin':'*'})
with sync_playwright() as p:
    b=p.chromium.launch(); errs=[]
    for w,hh in [(1440,900),(1280,800),(1366,650),(390,844)]:
        pg=b.new_page(viewport={'width':w,'height':hh}); pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.route('https://site.api.espn.com/**',h)
        pg.goto('http://localhost:8765/match-hub/leeds/'); pg.wait_for_timeout(2500)
        pg.screenshot(path=D+f'lh_{w}{"_live" if LIVE else ""}.png', full_page=(w==390))
        print(w, pg.evaluate('[document.documentElement.scrollWidth,document.documentElement.scrollHeight]'), pg.evaluate("document.getElementById('bsMain').textContent"))
        pg.close()
    print(errs); b.close()
