import json,re,subprocess
D="2019-02-23"
L={ "Theakston":("T&R Theakston","Masham","England"), "Daleside":("Daleside Brewery","Harrogate","England"),
 "Leeds":("Leeds Brewery","Leeds","England"), "Ilkley":("Ilkley Brewery","Ilkley","England"), "Rudgate":("Rudgate Brewery","Tockwith, nr York","England"),
 "Monkey":("Beer Monkey Brew Co","Skipton","England"), "Hambleton":("Hambleton Ales","Melmerby, nr Ripon","England"),
 "Roosters":("Rooster's Brewing Co.","Harrogate","England"), "ColdBath":("Cold Bath Brewing","Harrogate","England"),
 "HopStudio":("The Hop Studio","Elvington, nr York","England"), "Anarchy":("Anarchy Brew Co","Newcastle upon Tyne","England"),
 "Blackjack":("Blackjack Brewing","Manchester","England"), "Siren":("Siren Craft Brew","Finchampstead, Berkshire","England"),
 "NorthernMonk":("Northern Monk","Leeds","England"), "Salopian":("Salopian Brewery","Hadnall, Shropshire","England"),
 "Thornbridge":("Thornbridge Brewery","Bakewell","England"), "ThreeBrothers":("Three Brothers Brewing Co.","Stockton-on-Tees","England"),
 "HarrogateBC":("Harrogate Brewing Co","Harrogate","England"), "Harbour":("Harbour Brewing Co","Bodmin, Cornwall","England") }
B=[
("Barista Stout","Theakston","Stout",4.2,"Velvety, nitrogen-infused coffee stout - crème caramel and vanilla, dark berry fruit and a bold espresso aroma."),
("Peculier Pale Ale","Theakston","Pale",4.5,"Summit, El Dorado and Cascade hops - spicy citrus, sweet orange and stone fruit. The ultimate thirst quencher."),
("Theakston Best Bitter","Theakston","Bitter",3.8,"Classic English session cask ale - golden, sweet and zesty with subtle fruit and baked apple, mellow finish."),
("Lightfoot","Theakston","Pale",4.1,"Refreshing blonde with English malts and continental hops - subtle honey aroma and lemon fruit, medium-dry finish."),
("Old Peculier","Theakston","Dark",5.6,"Pale, crystal and roasted barley with Fuggle hops - banana and black cherry, a Christmas pudding of flavour. Rich, smooth and sweet."),
("Double Cross IPA","Theakston","IPA",4.2,"Classic IPA with English hops - rich tea biscuit base with dry lemon and grapefruit."),
("Ru(g)by Ale","Theakston","Ruby ale",4.0,"A scrummage of malts and New World hops - full-bodied ruby ale with Sussex hops for a citrus aroma."),
("Monkey Wrench","Daleside","Dark",5.3,"Dark and beautifully smooth."),
("Legover","Daleside","Bitter",4.1,"A well-balanced ale with a nutty, bitter-sweet taste."),
("Pride of England","Daleside","Pale",4.0,"A light-coloured beer with a floral aroma."),
("Blood Orange IPA","Daleside","IPA",4.5,"A well-hopped, blood-orange-infused IPA with citrus notes."),
("Crackshot","Daleside","Brown ale",5.5,"Medium brown ale unusually made with malted oats - a subtle hint of sweetness on the finish."),
("Daleside Lager","Daleside","Lager",4.2,"An authentic craft lager with a delicate floral aroma and refreshing finish."),
("Union","Leeds","Bitter",4.1,"A British classic best bitter, brewed to celebrate an England Six Nations victory charge (fingers crossed)."),
("Yorkshire Gold","Leeds","Golden",4.0,"Golden, fruity ale - Chinook hops give great grapefruit citrus and a long finish."),
("Mary Jane","Ilkley","Pale",3.5,"Intensely refreshing, with citrus aroma and balanced bitterness."),
("Joshua Jane","Ilkley","Bitter",3.7,"Everything great about traditional Yorkshire bitter, fused with Ilkley's own hop character."),
("Ruby Jane","Ilkley","Mild",4.0,"Seven malts give complex biscuit layers, a velvety palate and creamy head, with soft hop bitterness."),
("Ruby Mild","Rudgate","Mild",4.4,"Multi-award-winning - nutty, deeply rich and satisfying."),
("Battle Axe","Rudgate","Bitter",4.2,"Bitter-sweet, with complex fruit and a memorable aftertaste."),
("Chocolate Stout","Rudgate","Stout",5.0,"Deep, rich premium stout with complex balanced flavours and a warm, subtle chocolate finish."),
("Uncle Monks","Monkey","IPA",4.5,"Kilned malt, slightly sweet and growing bitterness - an American-style session IPA with a big hoppy end."),
("For Pete's Sake","Monkey","Pale",3.9,"Dry hopped to maximise flavour."),
("Cuddly Toy","Monkey","Golden",3.6,"A crisp, refreshing pale ale."),
("YPA","Roosters","Pale",3.7,"Yorkshire Pale Ale - a pale, aromatic summer ale with delicate peach and berry fruit."),
("First World Problems","Roosters","Stout",4.5,"A smooth and decadent salted caramel stout."),
("Stud Blonde","Hambleton","Pale",4.3,"Easy-drinking golden blonde. Gluten free."),
("Stallion Amber","Hambleton","Bitter",4.2,"Well-hopped, smooth-drinking best bitter."),
("Mosaic","HopStudio","APA",4.9,"Oats and Mosaic hops - berries and pine, herbal flavours and a huge chewy mouthfeel."),
("XS","HopStudio","IPA",5.5,"Spicy dark fruit, malty and bitter, with hints of floral and citrus aroma."),
("Exile","Anarchy","Pale (gluten free)",4.9,"Clean, slick gluten-free pale - big American hops and smooth bitterness."),
("Cashmere","Anarchy","Pale",5.0,"Cashmere hops and Marisota - smooth, easy pale ale with lemon, lime and melon."),
("New Deck","Blackjack","Bitter",4.4,"Quaffable traditional golden bitter hopped with Summit, Admiral and Goldings."),
("Royal Flush","Blackjack","IPA",5.0,"An excellent English pale ale with five tasty English hops."),
("Broken Dreams","Siren","Stout",6.0,"Smoke and coffee aromas with chocolate, milk and oats - thick, velvety and slick."),
("Striding Edge","NorthernMonk","Light IPA",3.0,"First in a series of light IPAs with mountain runner Ricky Lightfoot - Simcoe, Mosaic and Citra."),
("Lemon Dream","Salopian","Golden",4.5,"Zesty, pale, delicate, lemony, refreshing and clean."),
("Tiny Pai","Thornbridge","Pale",6.2,"New Zealand-hopped pale ale - passion fruit, gooseberry and mango, sweet then a lasting grapefruit bitterness."),
("ThalPA","ThreeBrothers","Session IPA",4.1,"Lemongrass-infused hoppy session IPA - full flavour at a lower ABV."),
("Harrogate Pale","HarrogateBC","Pale",4.2,"Tasty session ale, changing the hops every time."),
("Beeching Axe","HarrogateBC","IPA",5.2,"Hoppy IPA - fruity citrus, dry hopped for extra aroma."),
("Ellensberg Session PA","Harbour","Session pale",4.3,"Best Pale, Crystal and Munich malts with Mosaic, Perle and Amarillo - bright golden, perfumed citrus, juicy and dry."),
]
p='/home/claude/site/beer-passport/beers.js'; src=open(p).read()
pre=src[:src.index('window.BEERS')]
cur=json.loads(subprocess.run(['node','-e',"global.window={};require('"+p+"');process.stdout.write(JSON.stringify(window.BEERS))"],capture_output=True,text=True).stdout)
names={b['name'].lower():b for b in cur}
# existing beers that were on the menu: add the date and the menu description
upd={"baby-faced assassin":("IPA",6.1,"100% Citra hops - mango, apricot, grapefruit and mandarin, with a lasting juicy tropical bitterness."),
     "blonde":("Pale",3.9,"A full-flavoured golden ale with a hoppy aroma and a crisp finish."),
     "cold bath pale":("Pale",3.4,"Beautifully balanced low-gravity pale, twin-hopped with the classic West Coast pairing of Citra and Simcoe.")}
for k,(st,abv,say) in upd.items():
    b=names[k]; b['date']=D; b['style']=st; b['abv']=abv; b['brewerSays']=say
added=0
for n,br,st,abv,say in B:
    if n.lower() in names: print('dup',n); continue
    name,town,country=L[br]
    cur.append({"name":n,"added":"2026-10-21","date":D,"brewerSays":say,"style":st,"abv":abv,"brewery":name,"brewedIn":town,"brewedCountry":country}); added+=1
cur.sort(key=lambda b:b['name'].lower())
def fmt(b): return '  '+json.dumps(b,ensure_ascii=False).replace('","','", "').replace('{"','{ ').replace('"}',' "}').replace('": ',': ')
lines=[]
for b in cur:
    s='{ '+', '.join(f'{k}: {json.dumps(v,ensure_ascii=False)}' for k,v in b.items())+' }'
    lines.append('  '+s)
open(p,'w').write(pre+'window.BEERS = [\n'+',\n'.join(lines)+'\n];\n')
print('added',added,'total',len(cur))
