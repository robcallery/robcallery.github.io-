import json, sys
from playwright.sync_api import sync_playwright
D='/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/'
LIVE='live' in sys.argv
def team(i,n,col): return {"id":i,"displayName":n,"shortDisplayName":n,"color":col,"logo":""}
def ev(eid,date,h,a,hs,as_,state,clock=0,period=0,name='STATUS_SCHEDULED',details=None):
    return {"id":eid,"date":date,"competitions":[{"competitors":[{"homeAway":"home","score":str(hs),"team":h},{"homeAway":"away","score":str(as_),"team":a}],
      "venue":{"fullName":"Stadium of Light","address":{"city":"Sunderland"}},"details":details or [],
      "status":{"clock":clock,"displayClock":"%d'"%(clock//60),"period":period,"type":{"state":state,"name":name,"shortDetail":"FT" if state=='post' else "","completed":state=='post'}}}]}
SUN=team("366","Sunderland","eb172b"); LEE=team("357","Leeds United","ffffff")
det=[{"team":{"id":"357"},"scoringPlay":True,"clock":{"displayValue":"23'"},"athletesInvolved":[{"id":"1","shortName":"Piroe","lastName":"Piroe"}]},
     {"team":{"id":"366"},"yellowCard":True,"clock":{"displayValue":"41'"},"athletesInvolved":[{"id":"2","shortName":"Ballard"}]}]
main=ev("777","2026-10-22T19:30Z",SUN,LEE,0,1,'in',3780,2,'STATUS_IN_PROGRESS',det) if LIVE else ev("777","2026-10-25T16:30Z",SUN,LEE,0,0,'pre')
others=[ev("701","2026-10-22T19:30Z",team("359","Arsenal","ff0000"),team("364","Liverpool","c8102e"),2,1,'in' if LIVE else 'pre',3600,2,'STATUS_IN_PROGRESS'),
        ev("702","2026-10-22T19:30Z",team("382","Manchester City","6cabdd"),team("363","Chelsea","034694"),1,1,'in' if LIVE else 'pre',3600,2,'STATUS_IN_PROGRESS'),
        ev("703","2026-10-22T17:30Z",team("362","Aston Villa","670e36"),team("361","Everton","003399"),0,0,'post',5400,2,'STATUS_FULL_TIME')]
names=["Arsenal","Liverpool","Manchester City","Chelsea","Leeds United","Aston Villa","Newcastle United","Brighton & Hove Albion","Tottenham Hotspur","Fulham","Brentford","Crystal Palace","Everton","Bournemouth","West Ham United","Nottingham Forest","Wolverhampton Wanderers","Sunderland","Burnley","Coventry City"]
ids={"Arsenal":"359","Liverpool":"364","Manchester City":"382","Chelsea":"363","Leeds United":"357","Aston Villa":"362","Everton":"361","Sunderland":"366"}
ent=[{"team":{"id":ids.get(n,str(900+k)),"displayName":n,"shortDisplayName":n},"stats":[{"name":"rank","value":k+1},{"name":"gamesPlayed","value":8},{"name":"pointsFor","value":14-k//2},{"name":"pointsAgainst","value":6+k//2},{"name":"pointDifferential","value":8-k},{"name":"points","value":20-k}]} for k,n in enumerate(names)]
xi=lambda side: [{"starter":True,"jersey":str(i+1),"athlete":{"id":str(100+i),"lastName":p}} for i,p in enumerate(side)]
summary={"boxscore":{"teams":[{"team":{"id":"366"},"statistics":[{"name":"possessionPct","displayValue":"44"},{"name":"totalShots","displayValue":"7"},{"name":"shotsOnTarget","displayValue":"2"},{"name":"wonCorners","displayValue":"3"},{"name":"yellowCards","displayValue":"1"},{"name":"accuratePasses","displayValue":"280"},{"name":"totalPasses","displayValue":"350"}]},
  {"team":{"id":"357"},"statistics":[{"name":"possessionPct","displayValue":"56"},{"name":"totalShots","displayValue":"11"},{"name":"shotsOnTarget","displayValue":"5"},{"name":"wonCorners","displayValue":"6"},{"name":"yellowCards","displayValue":"0"},{"name":"accuratePasses","displayValue":"390"},{"name":"totalPasses","displayValue":"450"}]}]},
  "rosters":[{"homeAway":"home","roster":xi(["Patterson","Hume","Ballard","Alderete","Reinildo","Xhaka","Sadiki","Le Fée","Talbi","Isidor","Mayenda"])},
             {"homeAway":"away","roster":xi(["Perri","Bogle","Rodon","Struijk","Gudmundsson","Ampadu","Stach","Aaronson","Okafor","Calvert-Lewin","Piroe"])}]} if LIVE else {}
def h(route):
    u=route.request.url
    if 'a.espncdn.com' in u: return route.fulfill(status=404,body='')
    if '/standings' in u: body={"children":[{"name":"Premier League","standings":{"entries":ent}}]}
    elif '/summary' in u: body=summary
    elif 'eng.1/scoreboard' in u: body={"leagues":[{"name":"Premier League"}],"events":[main]+others}
    elif 'eng.1/teams/357/schedule?fixture' in u: body={"leagues":[{"name":"Premier League"}],"events":[] if LIVE else [main]}
    else: body={"events":[]}
    route.fulfill(status=200,content_type='application/json',body=json.dumps(body),headers={'Access-Control-Allow-Origin':'*'})
with sync_playwright() as p:
    b=p.chromium.launch(); errs=[]
    for w,hh in [(1920,1080),(1366,768),(1280,800),(390,844)]:
        pg=b.new_page(viewport={'width':w,'height':hh}); pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.route('**/*',lambda r: h(r) if ('espn' in r.request.url) else r.continue_())
        pg.goto('http://localhost:8765/match-hub/leeds/'); pg.wait_for_timeout(3500)
        pg.screenshot(path=D+f'mc_{w}{"_live" if LIVE else ""}.png',full_page=(w==390))
        print(w, pg.evaluate('[document.documentElement.scrollWidth,document.documentElement.scrollHeight]'), pg.inner_text('#pill-text'), '|', pg.evaluate("document.getElementById('bsMain').textContent"))
        pg.close()
    print(errs); b.close()
