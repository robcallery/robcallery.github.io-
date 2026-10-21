import json,subprocess
U={"US":"USA","E":"England"}
R=("Rooster's Brewing Co.","Harrogate","England"); BD=("BrewDog","Ellon, Aberdeenshire","Scotland"); SA=("Boston Beer Company","Boston, Massachusetts","USA")
BS=("Black Sheep Brewery","Masham","England"); BC=("Bad Co Brewing & Distilling","Dishforth, North Yorkshire","England")
TT=("Timothy Taylor","Keighley","England"); CT=("Camden Town Brewery","London","England"); NB=("North Brewing Co","Leeds","England"); BT=("Beavertown","London","England")
SC=("Schöfferhofer","Frankfurt","Germany")
NEW=[
("Stella Artois","2014-07-04",("AB InBev","Leuven","Belgium")),
("Coors Light","2014-07-25",("Molson Coors","Golden, Colorado","USA")),
("Cubanisto","2014-12-21",("Heineken","Amsterdam","Netherlands")),
("Desperados","2014-12-19",("Heineken","Schiltigheim, Alsace","France")),
("Samuel Adams Boston Lager","2015-03-20",SA),
("Samuel Adams Summer Ale","2015-05-01",SA),
("Samuel Adams Downtime Pilsner","2015-05-01",SA),
("Samuel Adams Rebel Rider IPA","2015-05-01",SA),
("Floridian Hefeweizen","2015-05-03",("Funky Buddha Brewery","Oakland Park, Florida","USA")),
("Category 3 IPA","2015-05-03",("Due South Brewing Co","Boynton Beach, Florida","USA")),
("Maple Bacon Stout","2015-05-03",(None,"Clearwater, Florida","USA")),
("Billy's Chilies","2015-05-03",("Twisted Pine Brewing Co","Boulder, Colorado","USA")),
("Blonde Ale","2015-05-06",("Orlando Brewing","Orlando, Florida","USA")),
("Channel Marker Red Ale","2015-05-06",(None,None,None)),
("Feast of Flowers Farmhouse","2015-05-06",(None,None,None)),
("Jai Alai","2015-05-06",("Cigar City Brewing","Tampa, Florida","USA")),
("Amstel","2015-12-24",("Heineken","Amsterdam","Netherlands")),
("Sierra Nevada Torpedo Extra IPA","2016-02-19",("Sierra Nevada Brewing Co","Chico, California","USA")),
("Singha","2016-02-20",("Boon Rawd Brewery","Bangkok","Thailand")),
("Guinness","2016-03-17",("Guinness","Dublin","Ireland")),
("Super Bock","2016-07-23",("Super Bock Group","Porto","Portugal")),
("Pilsner Urquell","2016-08-06",("Pilsner Urquell","Plzeň","Czechia")),
("Hop House 13","2017-08-03",("Guinness","Dublin","Ireland")),
("Boddingtons","2018-05-12",("Boddingtons","Manchester","England")),
("54° North Lager","2019-03-23",BS),
("Schöfferhofer Grapefruit","2019-11-02",SC),
("One Trick Pony","2020-04-09",R),
("Pilsner","2020-04-09",R),
("Golden Sheep","2020-05-24",BS),
("Ald IPA","2020-10-10",BD),
("Kick It Back","2020-10-25",BC),
("Kosmic Pale","2020-10-25",BC),
("Bad Co Lager","2020-10-25",BC),
("Love Over Gold","2020-10-25",BC),
("Two Hoots","2021-08-14",("Joseph Holt","Manchester","England")),
("Mythos","2021-10-08",("Mythos Brewery","Thessaloniki","Greece")),
("Marmite Ale","2021-10-09",CT),
("Hoppy Christmas","2021-11-18",BD),
("Santa's Progress","2021-12-02",("Daleside Brewery","Harrogate","England")),
("Lost Lager","2021-12-16",BD),
("Yellow Black Army IPA","2021-12-26",BS),
("Wainwright Golden Beer","2022-05-07",("Thwaites","Mellor Brook, Lancashire","England")),
("Madrí Excepcional","2022-07-31",("Molson Coors","Madrid","Spain")),
("Square Ball Californian Pale Ale","2022-10-08",NB),
("Springwell","2022-11-06",NB),
("Devil's Beer IPA","2023-01-27",(None,None,None)),
("Flying IPA","2023-01-27",(None,None,None)),
("Neck Oil","2023-03-17",BT),
("Gamma Ray","2023-03-17",BT),
("Jaipur","2023-02-19",("Thornbridge Brewery","Bakewell","England")),
("Ale to the King","2023-05-05",("St Austell Brewery","St Austell, Cornwall","England")),
("Estrella Galicia","2023-05-24",("Hijos de Rivera","A Coruña","Spain")),
("Pamplemousse","2023-06-09",R),
("Hopical Storm","2023-10-01",TT),
("Sapporo Premium","2023-10-14",("Sapporo Breweries","Sapporo","Japan")),
("Asahi Super Dry","2023-10-14",("Asahi Breweries","Tokyo","Japan")),
("Foster's Premium","2024-09-03",("Heineken UK","Manchester","England")),
("Leeds Pale","2024-09-29",("Leeds Brewery","Leeds","England")),
("Virtuous","2025-02-21",("Kirkstall Brewery","Leeds","England")),
("Level Head","2025-03-02",("Greene King","Bury St Edmunds","England")),
("Big Wave","2025-03-08",("Kona Brewing Co","Kailua-Kona, Hawaii","USA")),
("Pure Drop Session IPA","2025-03-15",TT),
("Schöfferhofer Watermelon Mint","2025-03-30",SC),
("Camden Hells","2025-06-01",CT),
("Terry's Chocolate Orange Stout","2025-12-14",R),
("Peculier Assassin","2026-09-04",("T&R Theakston x Rooster's","Masham & Harrogate","England")),
]
EXIST={"estrella damm":"2014-08-06","brooklyn lager":"2014-09-27","new england assassin":"2021-06-04","wingman":"2023-11-04",
       "kronenbourg 1664":"2025-03-12","cerveza victoria":"2025-04-18","mary jane":"2020-08-21"}
p='/home/claude/site/beer-passport/beers.js'; src=open(p).read(); pre=src[:src.index('window.BEERS')]
cur=json.loads(subprocess.run(['node','-e',"global.window={};require('"+p+"');process.stdout.write(JSON.stringify(window.BEERS))"],capture_output=True,text=True).stdout)
by={b['name'].lower():b for b in cur}
for k,d in EXIST.items():
    b=by[k]
    if not b.get('date') or d<b['date']: b['date']=d
    else: print('kept earlier',k,b['date'])
n=0
for name,d,(br,town,country) in NEW:
    if name.lower() in by: print('dup!',name); continue
    e={"name":name,"added":"2026-10-21","date":d}
    if br: e["brewery"]=br
    if town: e["brewedIn"]=town
    if country: e["brewedCountry"]=country
    cur.append(e); n+=1
cur.sort(key=lambda b:b['name'].lower())
open(p,'w').write(pre+'window.BEERS = [\n'+',\n'.join('  { '+', '.join(f'{k}: {json.dumps(v,ensure_ascii=False)}' for k,v in b.items())+' }' for b in cur)+'\n];\n')
print('added',n,'total',len(cur))
