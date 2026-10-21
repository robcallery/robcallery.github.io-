import json,re,subprocess
BREWER={
"Baby-Faced Assassin":"Citra-hopped IPA (6.1%) - mango, apricot and grapefruit, dangerously easy to drink for its strength.",
"Black Sheep":"A bold, grassy and peppery best bitter (3.8%) brewed with Dales water in Masham.",
"Blonde":"Golden, with a crisp, fresh palate of citrus fruit and floral notes.",
"Brooklyn Lager":"Brooklyn's flagship amber lager (5%) - once told it was 'too flavourful'.",
"Bud Light":"Light American lager - crisp, clean and easy-drinking.",
"Budweiser":"The 'King of Beers' - a crisp American lager, beechwood aged.",
"Cerveza Victoria":"'Malagueña y exquisita' - the authentic beer of Málaga, brewed since 1928.",
"Cold Bath Pale":"Easy-drinking session pale (3.8%) - tangerine, citrus and gooseberry with gentle bitterness.",
"Cold Beer":"'Crisp, cold, classic' - a light lager (3.4%) with subtle lemon notes. Serve ice cold.",
"Cruzcampo":"Andalusia's pilsner, brewed in Seville since 1904.",
"Cruzcampo Radler":"Cruzcampo mixed with natural lemon juice - low strength, made for the heat.",
"Disco King":"Their flagship American pale (5.1%) - Mosaic and Chinook, 'a real juicy little disco of a beer'.",
"Easy Going Assassin":"Gluten-free session IPA (4.3%) - the Assassin's punchy citrus and tropical fruit at lower strength.",
"Elvis Juice":"Grapefruit-infused IPA - big citrus, bitter finish.",
"Estrella Damm":"Barcelona's Mediterranean lager, brewed with barley malt, rice and hops since 1876.",
"Hazy Faced Assassin":"Soft, juicy hazy IPA (5.7%) - Citra, Galaxy and Mosaic with mango and peach.",
"Hazy Jane":"Juicy New England IPA - soft, hazy and full of tropical fruit.",
"Heineken":"Pure malt lager brewed with Heineken's own A-yeast.",
"Island Citrus Ale":"A simply brewed citrus ale (5%) made for hot days on the water - pairs with shellfish and spicy food.",
"Kronenbourg 1664":"French premium lager brewed with aromatic Strisselspalt hops from Alsace.",
"Lagunitas IPA":"West Coast IPA (6.2%) - 'electric citrus, unapologetic hops'.",
"Mahou":"Madrid's lager, brewed in the city since 1890.",
"Pennine IPA":"A crisp golden IPA (4.4%) - zesty fruit with mild liquorice and black pepper undertones.",
"Peroni Gran Riserva":"Full-bodied, easy-drinking Vienna-style lager (6.6%) made with 100% Italian malt.",
"Peroni Limone di Sicilia 0.0":"Alcohol-free Peroni blended with Sicilian lemon juice.",
"Peroni Nastro Azzurro":"Crisp, refreshing Italian lager brewed with Italian maize.",
"Peroni Red":"The original Peroni from 1846 (4.7%) - 100% Italian malt, a rounded bitter-sweet taste.",
"Punk IPA":"BrewDog's 'post-modern classic' - tropical fruit and grapefruit with a bitter finish.",
"Smithwick's Irish Pale Ale":"Amarillo-hopped pale ale with 100% pale malt - rich golden, creamy head, long finish.",
"Three Wishes IPA":"Hazy double IPA (8.5%) brewed with Galaxy hops.",
"Wingman":"Session IPA (4.3%) - 'citrus, biscuit, fruity', with tropical fruit and pine.",
"Yankee":"Light, easy-drinking pale ale (4.3%) - floral and citrus from Cascade hops.",
}
TIPS={
"Leeds":"Get to Whitelock's early on matchday - it's tiny and fills fast.",
"Wakefield":"Do Westgate as a crawl - Harry's, Black Rock and the Hop are all within a few minutes.",
"Batley":"The Union Rooms opens at 8am - breakfast and a pint in an old bank.",
"Dewsbury":"Start the Transpennine Ale Trail at the West Riding - it's on the platform.",
"Huddersfield":"Grab a pint at the King's Head before your train - it's in the station.",
"Sheffield":"Walk Kelham Island in a loop - Fat Cat, Kelham Island Tavern, then the Riverside.",
"Morley":"Nomad and Dyeworks are both closed early in the week - go Thursday to Sunday.",
"Harrogate":"The Winter Gardens staircase is worth the visit alone.",
"Knaresborough":"Have one by the river at the World's End, then walk up to the castle for the viaduct view.",
"Boroughbridge":"Ask for a look round Tap on the Tutt's 1930s rooms - they're barely changed.",
"Thirsk":"Go on a Monday or Saturday for the market, then the Three Tuns.",
"Northallerton":"Wednesday and Saturday are market days - the High Street pubs are buzzing.",
"York":"Walk the walls first - then you've earned the York Tap.",
"Wetherby":"Wetherby Brew Co's taproom is only open Thursday to Sunday.",
"Yeadon":"The airport Beer House opens at 5am for early flights.",
"Bingley":"Walk the Five Rise Locks, then the Brown Cow by the old bridge.",
"Halifax":"Go when there's something on in the Piece Hall - the Hop Yard is right inside.",
"Ripon":"Be in the Market Square at 9pm for the Hornblower, then straight to the pub.",
"Masham":"Book both brewery tours on the same day - they're five minutes apart.",
"Pateley Bridge":"Park at the bottom and walk the High Street - it's steep.",
"Malton":"Time it for the monthly food market, then Brass Castle's tap.",
"Settle":"Ride the Settle-Carlisle line out and back - the Talbot's by the station.",
"Bentham":"Ring the Coach House ahead for food - it's the main pub left in town.",
"Whitby":"Get fish and chips at the bottom of the 199 steps, after you've climbed them.",
"Scarborough":"South Bay for chips, North Bay for a quieter pint.",
"Redcar":"The Plimsoll Line's beer garden runs right through to Lord Street - grab a table outside.",
"Saltburn-by-the-Sea":"Take the cliff lift down to the Ship Inn - and back up after.",
"Keswick":"Book ahead for the Dog & Gun's goulash on a weekend.",
"Alnwick":"Barter Books first, then the Tanners Arms.",
"Bakewell":"Bakewell pudding, not tart - the locals will correct you.",
"Manchester":"Peveril of the Peak before anywhere else - it's an island of a pub.",
"Liverpool":"Visit the Philharmonic's gents - honestly, it's listed.",
"Leicester":"The Corn Exchange is right on the market - handy for a quick stop.",
"Daventry":"The Saracens Head is a proper old inn - worth the M1 detour.",
"Westminster":"Victoria station's Spoons has terraces - good for watching the world go by.",
"Southwark":"The Market Porter opens early on market days.",
"Tower Hamlets":"Prospect of Whitby has a terrace right on the Thames.",
"Newham":"Tap East is inside Westfield - easy pre-match on West Ham days.",
"Brent":"The Green Man goes one-in-one-out on matchdays - get there early.",
"Greenwich":"Get the Uber Boat in from central London - it's the best way to arrive.",
"Newport":"The Man in the Moon is in an old church - look up.",
"Llanrwst":"Tea at Tu Hwnt i'r Bont by the old bridge before the Pen-y-Bryn.",
"Dublin":"Skip Temple Bar's prices - Mulligan's and the Long Hall pour a better pint.",
"Málaga":"Antigua Casa de Guardia chalks your bill on the bar - don't wipe it off.",
"Benalmádena":"Get the cable car up Calamorro for the view, then the marina bars at sunset.",
"Paris":"A pint costs a fortune - drink wine or a demi instead.",
"Marne-la-Vallée":"Stay for the castle fireworks, then the Royal Pub in Disney Village.",
"Amsterdam":"Brouwerij 't IJ under the windmill - go early, it's packed by six.",
"Malia":"Old Town tavernas for dinner, Beach Road after midnight.",
"Tokyo":"Golden Gai bars are tiny and some charge a cover - check the sign on the door.",
"Osaka":"Beer Belly Tenma has no cover charge - a rarity in Osaka.",
"Narita":"The Barge Inn is a short taxi from the airport - perfect for a long layover.",
"Kyoto":"Fushimi Inari at sunrise, Kyoto Brewing Co at the weekend.",
"Orlando":"Redlight Redlight for the best beer list in town.",
"Tampa Bay":"Ybor City on 7th Avenue for brewery-hopping - Sky Puppy's in the old firehouse.",
"Kissimmee":"The Fox & Hounds does a proper British breakfast when you're homesick.",
"Chicago":"Order a 'cheezborger' at the Billy Goat - no fries, chips.",
"Philadelphia":"McGillin's has every bar's sign from Philly's history on its walls.",
"Lake Buena Vista":"Rose & Crown in Epcot - the closest thing to a proper pint in Florida.",
}
# beers.js
p='/home/claude/site/beer-passport/beers.js'; s=open(p).read()
for n,d in BREWER.items():
    s=re.sub(r'(\{ name: "'+re.escape(n)+r'", added: "[^"]+")', lambda m: m.group(1)+', brewerSays: '+json.dumps(d), s, count=1)
s=s.replace("//   rating: 1-5 pints","//   brewerSays: how the brewery describes the beer\n//   rating: 1-5 pints")
open(p,'w').write(s)
print('beers',s.count('brewerSays:')-1)
# guides.js
p='/home/claude/site/travel-guides/guides.js'; s=open(p).read()
pre=s[:s.index('window.GUIDES')]
out=subprocess.run(['node','-e',"global.window={};require('"+p+"');process.stdout.write(JSON.stringify(window.GUIDES))"],capture_output=True,text=True).stdout
G=json.loads(out)
for g in G:
    if g['city'] in TIPS: g['tip']=TIPS[g['city']]
print('tips',sum(1 for g in G if 'tip' in g),len(G))
if '// tip:' not in pre: pre=pre.replace("// rating: 1-5","// tip: a top tip, shown handwritten in biro.\n// rating: 1-5")
open(p,'w').write(pre+'window.GUIDES = '+json.dumps(G,indent=2,ensure_ascii=False)+';\n')
