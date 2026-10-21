import json,subprocess
p='/home/claude/site/beer-passport/beers.js'; src=open(p).read(); pre=src[:src.index('window.BEERS')]
cur=json.loads(subprocess.run(['node','-e',"global.window={};require('"+p+"');process.stdout.write(JSON.stringify(window.BEERS))"],capture_output=True,text=True).stdout)
U={
"Channel Marker Red Ale":dict(style="American Red Ale",abv=5.9,brewery="3 Daughters Brewing",brewedIn="St. Petersburg, Florida",brewedCountry="USA",where="Florida Fresh, Epcot Flower & Garden Festival",city="Orlando"),
"Feast of Flowers Farmhouse":dict(style="Saison",abv=7.8,brewery="Florida Beer Company",brewedIn="Cape Canaveral, Florida",brewedCountry="USA",where="Florida Fresh, Epcot Flower & Garden Festival",city="Orlando"),
"Maple Bacon Stout":dict(style="Imperial Stout",abv=9.2,brewery="Shipyard Brewing Co.",brewedIn="Clearwater, Florida",brewedCountry="USA",where="The Smokehouse, Epcot Flower & Garden Festival",city="Orlando"),
"Blonde Ale":dict(where="Florida Fresh, Epcot Flower & Garden Festival",city="Orlando"),
"Jai Alai":dict(where="Florida Fresh, Epcot Flower & Garden Festival",city="Orlando"),
}
for b in cur:
    if b['name'] in U:
        keep={k:b[k] for k in ('name','added','date') if k in b}; rest={k:v for k,v in b.items() if k not in keep}
        rest.update(U[b['name']]); b.clear(); b.update(keep); b.update(rest); print(b)
open(p,'w').write(pre+'window.BEERS = [\n'+',\n'.join('  { '+', '.join(f'{k}: {json.dumps(v,ensure_ascii=False)}' for k,v in b.items())+' }' for b in cur)+'\n];\n')
