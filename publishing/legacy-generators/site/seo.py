import json, re
SITE="https://callery.co.uk"
SOCIAL=["https://www.youtube.com/@calz88","https://www.twitch.tv/robcallery","https://www.instagram.com/calz88","https://x.com/calz88","https://www.tiktok.com/@calz88","https://www.facebook.com/calz88","https://www.linkedin.com/in/rob-callery-98465216b"]
PAGES={
 "index.html":("/","Rob Callery – Travelling the world one beer at a time","Rob Callery: travelling the world one beer at a time and always heading home to Elland Road. Beer passport, pint-first travel guides and Leeds United tales."),
 "site/explore/index.html":("/explore/","Explore - Rob Callery","Pick a read from Rob Callery's bar: the beer passport, travel guides, Elland Road, and the telly for Twitch and YouTube."),
 "site/beer-passport/index.html":("/beer-passport/","Beer Passport - Rob Callery","Rob Callery's beer passport: every beer stamped with its brewery and where it's brewed."),
 "site/travel-guides/index.html":("/travel-guides/","Travel Guides - Rob Callery","Rob Callery's pint-first travel guides: the local Spoons, the best pubs, food and football in every town and city."),
 "site/football-tales/index.html":("/football-tales/","Football Tales - Rob Callery","Football: Tales of a Leeds Fan by Rob Callery - away days, home days and the pubs either side."),
 "site/stadium/index.html":("/stadium/","Elland Road - Rob Callery","Step inside Elland Road: football tales from a lifetime following Leeds United, and the match hub."),
 "site/match-hub/index.html":("/match-hub/","Match Hub - Rob Callery","Rob Callery's Leeds United match hub: scores, fixtures and matchday, coming soon."),
}
person={"@context":"https://schema.org","@graph":[
 {"@type":"Person","@id":SITE+"/#rob","name":"Rob Callery","alternateName":"calz88","url":SITE+"/","image":SITE+"/og-image.png","description":"Travelling the world one beer at a time. Leeds United fan.","sameAs":SOCIAL},
 {"@type":"WebSite","@id":SITE+"/#site","url":SITE+"/","name":"Rob Callery","publisher":{"@id":SITE+"/#rob"}}]}
for f,(path,title,desc) in PAGES.items():
    s=open(f).read()
    s=re.sub(r'\n<!-- seo -->.*?<!-- /seo -->','',s,flags=re.S)
    s=re.sub(r'<meta name="description" content="[^"]*">\n?','',s)
    tags=f'''
<!-- seo -->
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Rob Callery">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@calz88">
<meta name="twitter:image" content="{SITE}/og-image.png">
'''+(f'<script type="application/ld+json">{json.dumps(person)}</script>\n' if path=="/" else '')+'<!-- /seo -->'
    s=s.replace('<meta name="viewport" content="width=device-width, initial-scale=1">','<meta name="viewport" content="width=device-width, initial-scale=1">'+tags,1)
    open(f,'w').write(s)
open('site/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{SITE}{p}</loc><lastmod>2026-10-21</lastmod></url>\n' for p,_,_ in PAGES.values())+'</urlset>\n')
open('site/robots.txt','w').write(f"User-agent: *\nAllow: /\nDisallow: /starting-soon.html\n\nSitemap: {SITE}/sitemap.xml\n")
print("ok")
