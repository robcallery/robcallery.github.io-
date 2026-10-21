# Match Hub: the pub with two tellies, the Leeds TV art, and the CALFAX teletext page.
import json, random

LEEDS_SCREEN = '''
  <rect x="0" y="0" width="300" height="168" fill="#0b1f63"/>
  <rect x="0" y="0" width="300" height="168" fill="url(#lufcGlow)"/>
  <path d="M0 120 L300 70 L300 96 L0 146 Z" fill="#ffcd00" opacity=".95"/>
  <path d="M0 132 L300 82 L300 88 L0 138 Z" fill="#ffffff" opacity=".9"/>
  <text x="150" y="58" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="34" fill="#ffffff" letter-spacing="3" textLength="230" lengthAdjust="spacingAndGlyphs">LEEDS UNITED</text>
  <text x="150" y="80" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="15" fill="#ffcd00" letter-spacing="4">MATCH HUB</text>
  <rect x="96" y="146" width="108" height="16" rx="3" fill="#ffffff"/>
  <text x="150" y="158" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="11" fill="#0b1f63" letter-spacing="2">COMING SOON</text>
'''

TELETEXT_SCREEN = '''
  <rect x="0" y="0" width="220" height="160" fill="#000"/>
  <g font-family="'Courier New', monospace" font-weight="700" font-size="9">
    <text x="6" y="12" fill="#ffffff">P302 CALFAX 302</text><text x="214" y="12" text-anchor="end" fill="#ffff00" class="ttclock">22:11</text>
  </g>
  <g fill="#00ffff">''' + ''.join(f'<rect x="{6+i*13}" y="18" width="11" height="{8 + (i*5)%9}" opacity="{.6 + (i%3)*.2}"/>' for i in range(16)) + '''</g>
  <text x="110" y="52" text-anchor="middle" font-family="'Courier New', monospace" font-weight="700" font-size="20" fill="#ffff00">FOOTBALL</text>
  <g font-family="'Courier New', monospace" font-weight="700" font-size="10">
    <text x="10" y="76" fill="#ffffff">MADRID      2</text><text x="10" y="90" fill="#ffffff">SEVILLA     1</text>
    <text x="10" y="106" fill="#00ff00">67'  LIVE</text>
    <text x="10" y="124" fill="#00ffff">BEER: MAHOU</text>
  </g>
  <rect x="0" y="140" width="55" height="20" fill="#ff0000"/><rect x="55" y="140" width="55" height="20" fill="#00ff00"/><rect x="110" y="140" width="55" height="20" fill="#ffff00"/><rect x="165" y="140" width="55" height="20" fill="#00ffff"/>
'''

def modern_tv(x, y, w=330):
    s = w / 300
    return (f'<g transform="translate({x} {y}) scale({s:.3f})">'
            '<rect x="138" y="-60" width="24" height="64" fill="#2a2a30"/><rect x="110" y="-66" width="80" height="10" rx="3" fill="#3a3a42"/>'
            '<rect x="-10" y="-8" width="320" height="186" rx="8" fill="#111216"/><rect x="-10" y="-8" width="320" height="186" rx="8" fill="none" stroke="#2c2e36" stroke-width="2"/>'
            '<svg x="0" y="0" width="300" height="168" viewBox="0 0 300 168">' + LEEDS_SCREEN + '</svg>'
            '<rect x="0" y="0" width="300" height="168" fill="url(#screenSheen)"/>'
            '<circle cx="292" cy="172" r="2" fill="#3dff7a"/></g>')

def retro_tv(x, y, w=300):
    s = w / 300
    return (f'<g transform="translate({x} {y}) scale({s:.3f})">'
            '<path d="M118 -2 L80 -62 M182 -2 L220 -62" stroke="#9aa0aa" stroke-width="4" stroke-linecap="round"/><circle cx="80" cy="-62" r="5" fill="#c9ced8"/><circle cx="220" cy="-62" r="5" fill="#c9ced8"/>'
            '<rect x="0" y="0" width="300" height="210" rx="18" fill="#7a4b27"/><rect x="0" y="0" width="300" height="210" rx="18" fill="none" stroke="#4a2c16" stroke-width="4"/>'
            '<rect x="10" y="10" width="280" height="190" rx="14" fill="#8a5a32" opacity=".5"/>'
            '<rect x="18" y="20" width="210" height="170" rx="26" fill="#1b1b1b"/>'
            '<svg x="25" y="25" width="196" height="160" viewBox="0 0 220 160" preserveAspectRatio="none">' + TELETEXT_SCREEN + '</svg>'
            '<rect x="25" y="25" width="196" height="160" rx="22" fill="url(#crtSheen)"/>'
            '<rect x="238" y="22" width="48" height="166" rx="8" fill="#5a361b"/>'
            '<circle cx="262" cy="52" r="15" fill="#e8dcc4"/><rect x="260" y="38" width="4" height="14" fill="#5a361b"/>'
            '<circle cx="262" cy="96" r="11" fill="#e8dcc4"/><rect x="260" y="86" width="4" height="10" fill="#5a361b" transform="rotate(40 262 96)"/>'
            + ''.join(f'<rect x="246" y="{124+i*9}" width="32" height="4" rx="2" fill="#3b2312"/>' for i in range(6)) +
            '<rect x="30" y="210" width="16" height="22" fill="#4a2c16"/><rect x="254" y="210" width="16" height="22" fill="#4a2c16"/></g>')

def pub_scene():
    g = ['<defs>'
         '<linearGradient id="pubWall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1e3a2e"/><stop offset="1" stop-color="#16291f"/></linearGradient>'
         '<linearGradient id="screenSheen" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".16"/><stop offset=".45" stop-color="#fff" stop-opacity="0"/></linearGradient>'
         '<radialGradient id="crtSheen" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#fff" stop-opacity=".18"/><stop offset=".6" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".35"/></radialGradient>'
         '<radialGradient id="lufcGlow" cx=".5" cy=".3" r=".8"><stop offset="0" stop-color="#2a56c8"/><stop offset="1" stop-color="#0b1f63" stop-opacity="0"/></radialGradient>'
         '<radialGradient id="lamp" cx=".5" cy="0" r="1"><stop offset="0" stop-color="#ffd98a" stop-opacity=".5"/><stop offset="1" stop-color="#ffd98a" stop-opacity="0"/></radialGradient>'
         '</defs>']
    a = g.append
    a('<rect width="1200" height="640" fill="url(#pubWall)"/>')
    # wallpaper stripes and dado rail
    a(''.join(f'<rect x="{i*40}" y="0" width="18" height="430" fill="#ffffff" opacity=".025"/>' for i in range(30)))
    a('<rect y="430" width="1200" height="8" fill="#5a361b"/><rect y="438" width="1200" height="40" fill="#3b2312"/>')
    # warm lamps
    for x in (210, 600, 990):
        a(f'<ellipse cx="{x}" cy="40" rx="190" ry="210" fill="url(#lamp)"/><rect x="{x-1}" y="0" width="2" height="26" fill="#2a2a2a"/><path d="M{x-22} 40 L{x+22} 40 L{x+12} 24 L{x-12} 24 Z" fill="#c9a227"/>')
    # back-bar shelf with bottles between the tellies
    a('<rect x="490" y="250" width="220" height="10" fill="#5a361b"/><rect x="490" y="350" width="220" height="10" fill="#5a361b"/>')
    rnd = random.Random(9)
    for shelf in (250, 350):
        x = 500
        while x < 700:
            w = rnd.choice([12, 14, 16]); h = rnd.randint(38, 62); c = rnd.choice(['#2f6b3c', '#7a4b27', '#c9a227', '#3a5aa0', '#a8322e', '#d8d2c4'])
            a(f'<rect x="{x}" y="{shelf-h}" width="{w}" height="{h-14}" rx="3" fill="{c}" opacity=".9"/><rect x="{x+w/2-2}" y="{shelf-h-10}" width="4" height="12" fill="{c}"/>'
              f'<rect x="{x+2}" y="{shelf-h+14}" width="{w-4}" height="10" fill="#f7f2e4" opacity=".75"/>')
            x += w + 6
    a('<rect x="560" y="140" width="80" height="60" rx="4" fill="#0a1838"/><text x="600" y="168" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="16" fill="#ffcd00" letter-spacing="2">THE</text><text x="600" y="188" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="16" fill="#ffcd00" letter-spacing="1">LOCAL</text>')
    # the tellies (links)
    a('<a href="/match-hub/leeds/" class="hot tvlink" id="tvLeeds" aria-label="Leeds United match hub">' + modern_tv(95, 150, 340) + '</a>')
    a('<a href="/match-hub/world/" class="hot tvlink" id="tvWorld" aria-label="Around the world: a random live game and the local beer">' + retro_tv(790, 150, 320) + '</a>')
    # bar counter
    a('<rect y="470" width="1200" height="22" fill="#8a5a32"/><rect y="470" width="1200" height="5" fill="#b07a4a"/>')
    a('<rect y="492" width="1200" height="148" fill="#5a361b"/>' + ''.join(f'<rect x="{20+i*120}" y="510" width="100" height="110" rx="4" fill="none" stroke="#3b2312" stroke-width="4"/>' for i in range(10)))
    a('<rect y="626" width="1200" height="14" fill="#c9a227" opacity=".6"/>')
    # beer pumps and pints on the bar
    for i, x in enumerate((470, 520, 570, 630, 680, 730)):
        a(f'<rect x="{x-5}" y="420" width="10" height="52" rx="3" fill="#f2efe6"/><rect x="{x-9}" y="396" width="18" height="28" rx="4" fill="{["#1e3f9a", "#a8322e", "#2f6b3c", "#c9a227", "#1e3f9a", "#7a1f2b"][i]}"/>'
          f'<rect x="{x-7}" y="404" width="14" height="10" fill="#f7f2e4"/>')
    for x, full in ((300, 1), (350, .6), (880, 1), (930, .8), (1050, 1)):
        a(f'<path d="M{x-12} 470 L{x-15} 430 L{x+15} 430 L{x+12} 470 Z" fill="#f7f2e4" opacity=".35"/>'
          f'<path d="M{x-12} 470 L{x-14.5} {470-40*full:.0f} L{x+14.5} {470-40*full:.0f} L{x+12} 470 Z" fill="#e8a317"/>'
          f'<rect x="{x-15}" y="{466-40*full:.0f}" width="30" height="6" rx="3" fill="#ffffff"/>')
    return '\n'.join(g)

def leeds_tv_art():
    return ('<svg viewBox="-20 -80 340 270" role="img" aria-label="Leeds United match hub telly"><defs>'
            '<linearGradient id="screenSheen" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".16"/><stop offset=".45" stop-color="#fff" stop-opacity="0"/></linearGradient>'
            '<radialGradient id="lufcGlow" cx=".5" cy=".3" r=".8"><stop offset="0" stop-color="#2a56c8"/><stop offset="1" stop-color="#0b1f63" stop-opacity="0"/></radialGradient></defs>'
            + modern_tv(0, 0, 300) + '</svg>')

# ---------------------------------------------------------------- local beer lookup
CITY_BEER = {
 # UK & Ireland
 'London': "London Pride (Fuller's)", 'Manchester': 'Boddingtons', 'Salford': 'Boddingtons', 'Liverpool': 'a pint of local cask',
 'Leeds': 'Kirkstall Pale', 'Newcastle': 'Newcastle Brown Ale', 'Newcastle upon Tyne': 'Newcastle Brown Ale', 'Sunderland': 'Maxim Double Maxim',
 'Birmingham': "Banks's", 'Sheffield': 'Abbeydale Moonshine', 'Nottingham': 'Castle Rock', 'Bristol': 'Bristol Beer Factory', 'Derby': 'Marston\'s Pedigree',
 'Burton upon Trent': "Marston's Pedigree", 'Norwich': "Woodforde's Wherry", 'Ipswich': 'Adnams', 'Glasgow': "Tennent's Lager", 'Edinburgh': 'Belhaven Best',
 'Cardiff': 'Brains SA', 'Swansea': 'Brains SA', 'Dublin': 'Guinness', 'Belfast': 'Guinness', 'Wolverhampton': "Banks's", 'Stoke-on-Trent': 'Titanic Plum Porter',
 'Middlesbrough': 'a Teesside cask ale', 'Hull': 'a Hull cask ale', 'Bradford': 'Wallers', 'Blackburn': 'Thwaites', 'Preston': 'Thwaites',
 'Burnley': "Moorhouse's", 'Wigan': 'Wigan Brewhouse', 'Southampton': 'Ringwood', 'Portsmouth': 'Ringwood', 'Brighton': "Harvey's Sussex Best",
 'Falmer': "Harvey's Sussex Best", 'Leicester': "Everards Tiger", 'Coventry': 'a Warwickshire cask ale', 'Bournemouth': 'Ringwood', 'Plymouth': 'Plymouth Gin (or a Jail Ale)',
 'Reading': 'Loddon', 'Luton': 'a Bedfordshire cask ale', 'Watford': 'a Hertfordshire cask ale', 'Aberdeen': 'BrewDog Punk IPA', 'Dundee': 'a Scottish cask ale',
 # Spain & Portugal
 'Madrid': 'Mahou Cinco Estrellas', 'Barcelona': 'Estrella Damm', 'Seville': 'Cruzcampo', 'Sevilla': 'Cruzcampo', 'Valencia': 'Turia', 'Málaga': 'Victoria',
 'Malaga': 'Victoria', 'Vigo': 'Estrella Galicia', 'A Coruña': 'Estrella Galicia', 'Bilbao': 'a Basque craft ale', 'San Sebastián': 'a Basque craft ale',
 'Zaragoza': 'Ambar', 'Pamplona': 'Estrella Galicia', 'Lisbon': 'Sagres', 'Lisboa': 'Sagres', 'Porto': 'Super Bock', 'Braga': 'Super Bock',
 # Italy
 'Rome': 'Peroni', 'Roma': 'Peroni', 'Milan': 'Birra Moretti', 'Milano': 'Birra Moretti', 'Naples': 'Peroni', 'Napoli': 'Peroni', 'Turin': 'Menabrea', 'Torino': 'Menabrea',
 'Udine': 'Birra Moretti', 'Bergamo': 'Birra Moretti', 'Florence': 'Birra Moretti', 'Firenze': 'Birra Moretti', 'Genoa': 'Peroni', 'Genova': 'Peroni',
 # Germany & co
 'Munich': 'Augustiner Helles', 'München': 'Augustiner Helles', 'Dortmund': 'a Dortmunder Export', 'Cologne': 'Früh Kölsch', 'Köln': 'Früh Kölsch',
 'Düsseldorf': 'Uerige Altbier', 'Berlin': 'Berliner Kindl', 'Hamburg': 'Astra', 'Bremen': "Beck's", 'Frankfurt': 'Binding', 'Stuttgart': 'Stuttgarter Hofbräu',
 'Leipzig': 'Ur-Krostitzer', 'Gelsenkirchen': 'Veltins', 'Mönchengladbach': 'Bolten Alt', 'Leverkusen': 'Früh Kölsch', 'Bamberg': 'Schlenkerla Rauchbier',
 'Vienna': 'Ottakringer', 'Wien': 'Ottakringer', 'Salzburg': 'Stiegl', 'Prague': 'Pilsner Urquell', 'Praha': 'Pilsner Urquell',
 # France, Benelux
 'Paris': 'Kronenbourg 1664', 'Marseille': 'Kronenbourg 1664', 'Lyon': 'Kronenbourg 1664', 'Lille': 'a Ch\'ti bière de garde', 'Strasbourg': 'Kronenbourg 1664',
 'Amsterdam': 'Heineken', 'Rotterdam': 'Heineken', 'Eindhoven': 'Dommelsch', 'Brussels': 'Jupiler', 'Bruxelles': 'Jupiler', 'Brugge': 'Brugse Zot', 'Bruges': 'Brugse Zot', 'Liège': 'Jupiler',
 # elsewhere
 'Istanbul': 'Efes Pilsen', 'Athens': 'Mythos', 'Piraeus': 'Mythos', 'Thessaloniki': 'Mythos', 'Copenhagen': 'Carlsberg', 'København': 'Carlsberg',
 'Mexico City': 'Victoria (the Mexican one)', 'Ciudad de México': 'Victoria (the Mexican one)', 'Monterrey': 'Tecate', 'Guadalajara': 'Corona',
 'Rio de Janeiro': 'Brahma', 'São Paulo': 'Brahma', 'Porto Alegre': 'Polar', 'Belo Horizonte': 'Brahma', 'Buenos Aires': 'Quilmes', 'Rosario': 'Quilmes',
 'Montevideo': 'Pilsen', 'Santiago': 'Escudo', 'Bogotá': 'Club Colombia', 'Medellín': 'Club Colombia', 'Lima': 'Cusqueña',
 'Tokyo': 'Asahi Super Dry', 'Osaka': 'Asahi Super Dry', 'Yokohama': 'Kirin Ichiban', 'Sapporo': 'Sapporo Classic', 'Kobe': 'Kirin Ichiban',
 'Seoul': 'Cass', 'Sydney': 'Tooheys New', 'Melbourne': 'Victoria Bitter', 'Brisbane': 'XXXX Gold', 'Perth': 'Swan Lager', 'Adelaide': 'Coopers Pale Ale',
 'New York': 'Brooklyn Lager', 'Harrison': 'Brooklyn Lager', 'Chicago': 'Goose Island IPA', 'Philadelphia': 'Yuengling', 'Chester': 'Yuengling',
 'Atlanta': 'SweetWater 420', 'Miami': 'Funky Buddha Floridian', 'Fort Lauderdale': 'Funky Buddha Floridian', 'Orlando': 'Ivanhoe Park', 'Seattle': 'a Pacific Northwest IPA',
 'Portland': 'a Pacific Northwest IPA', 'Los Angeles': 'a West Coast IPA', 'Carson': 'a West Coast IPA', 'San Diego': 'a West Coast IPA', 'Denver': 'Coors Banquet',
 'Commerce City': 'Coors Banquet', 'Boston': 'Samuel Adams Boston Lager', 'Foxborough': 'Samuel Adams Boston Lager', 'Austin': 'a Texas craft lager',
 'Houston': 'Saint Arnold', 'Kansas City': 'Boulevard Wheat', 'Saint Louis': 'Budweiser', 'St. Louis': 'Budweiser', 'Toronto': 'Steam Whistle', 'Vancouver': 'Granville Island',
 'Montreal': 'Molson Export', 'Riyadh': 'nothing - it\'s a dry country, so a coffee', 'Jeddah': 'nothing - it\'s a dry country, so a coffee',
}
COUNTRY_BEER = {
 'England': 'a pint of local cask bitter', 'Scotland': "Tennent's Lager", 'Wales': 'Brains SA', 'Northern Ireland': 'Guinness', 'Ireland': 'Guinness',
 'Spain': 'Mahou Cinco Estrellas', 'Portugal': 'Super Bock', 'Italy': 'Peroni', 'Germany': 'the local Pils', 'France': 'Kronenbourg 1664',
 'Netherlands': 'Heineken', 'Belgium': 'Jupiler', 'Turkey': 'Efes Pilsen', 'Türkiye': 'Efes Pilsen', 'Greece': 'Mythos', 'Austria': 'Stiegl',
 'Switzerland': 'Feldschlösschen', 'Denmark': 'Carlsberg', 'Sweden': 'Mariestads', 'Norway': 'Ringnes', 'Czech Republic': 'Pilsner Urquell', 'Czechia': 'Pilsner Urquell',
 'Poland': 'Tyskie', 'Croatia': 'Ožujsko', 'Serbia': 'Jelen', 'Scotland ': "Tennent's Lager", 'USA': 'a local craft IPA', 'United States': 'a local craft IPA',
 'Canada': 'Molson Canadian', 'Mexico': 'Modelo Especial', 'Brazil': 'Brahma', 'Argentina': 'Quilmes', 'Uruguay': 'Pilsen', 'Chile': 'Escudo',
 'Colombia': 'Club Colombia', 'Peru': 'Cusqueña', 'Ecuador': 'Pilsener', 'Paraguay': 'Pilsen', 'Bolivia': 'Paceña', 'Japan': 'Asahi Super Dry',
 'South Korea': 'Cass', 'Korea Republic': 'Cass', 'China': 'Tsingtao', "China PR": 'Tsingtao', 'Australia': 'Victoria Bitter', 'Saudi Arabia': "nothing - it's a dry country, so a coffee",
 'Qatar': "something from the hotel bar - it's tightly licensed", 'United Arab Emirates': 'something from a licensed hotel bar', 'Egypt': 'Stella (the Egyptian one)',
 'South Africa': 'Castle Lager', 'Nigeria': 'Star Lager', 'Morocco': 'Casablanca', 'India': 'Kingfisher', 'Thailand': 'Singha', 'Ukraine': 'Obolon', 'Russia': 'Baltika',
}
GUIDE_ALIAS = {'Newcastle': 'Newcastle upon Tyne', 'Brighton': 'Brighton and Hove', 'Falmer': 'Brighton and Hove', 'Stoke': 'Stoke-on-Trent', 'Malaga': 'Málaga'}

LEAGUES = ['eng.1', 'eng.2', 'eng.3', 'eng.4', 'sco.1', 'esp.1', 'esp.2', 'ita.1', 'ger.1', 'fra.1', 'ned.1', 'por.1', 'bel.1', 'tur.1',
           'gre.1', 'den.1', 'aut.1', 'sui.1', 'usa.1', 'mex.1', 'bra.1', 'arg.1', 'col.1', 'chi.1', 'jpn.1', 'aus.1', 'ksa.1', 'irl.1',
           'uefa.champions', 'uefa.europa', 'uefa.europa.conf', 'conmebol.libertadores', 'conmebol.sudamericana', 'fifa.world', 'uefa.nations']

def teletext_page(guide_cities):
    data = json.dumps({'city': CITY_BEER, 'country': COUNTRY_BEER, 'alias': GUIDE_ALIAS, 'guides': guide_cities, 'leagues': LEAGUES}, ensure_ascii=False)
    return '''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CALFAX 302 - Rob Callery</title>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=VT323&display=swap" rel="stylesheet">
<style>
  :root{--bk:#000;--wh:#fff;--ye:#ff0;--cy:#0ff;--gr:#0f0;--re:#f00;--ma:#f0f;--bl:#00f}
  *{box-sizing:border-box;margin:0;padding:0}
  html,body{background:#000;color:var(--wh);min-height:100%}
  body{font-family:VT323,'Courier New',monospace;display:flex;justify-content:center;align-items:flex-start;padding:16px}
  .tv{width:min(100%,760px);aspect-ratio:auto;font-size:clamp(17px,3.6vw,28px);line-height:1.12;position:relative;padding:.4em .6em 1em;border-radius:14px;
      background:#000;box-shadow:0 0 0 2px #111,0 0 60px rgba(0,255,255,.07) inset}
  .tv::after{content:"";position:absolute;inset:0;border-radius:14px;pointer-events:none;
      background:repeating-linear-gradient(180deg,rgba(255,255,255,.04) 0 1px,transparent 1px 3px)}
  .row{white-space:pre-wrap;word-break:break-word;min-height:1.12em}
  .hdr{display:flex;justify-content:space-between;gap:.5em}
  .w{color:var(--wh)}.y{color:var(--ye)}.c{color:var(--cy)}.g{color:var(--gr)}.r{color:var(--re)}.m{color:var(--ma)}
  .band{display:flex;gap:.18em;margin:.25em 0 .1em}
  .band i{display:block;flex:1;height:.55em;background:var(--cy)}
  .band i:nth-child(3n){height:.85em}.band i:nth-child(4n){opacity:.65}
  .title{font-size:2.15em;line-height:1;color:var(--ye);letter-spacing:.06em;margin:.15em 0 .25em}
  .bg-bl{background:var(--bl)}.bg-re{background:var(--re)}.bg-ye{background:var(--ye);color:#000}
  .score{display:grid;grid-template-columns:1fr auto;gap:0 1em;font-size:1.45em;margin:.2em 0}
  .score b{font-weight:400}
  .dh{font-size:1.45em}
  .blink{animation:bl 1s steps(2) infinite}@keyframes bl{50%{opacity:0}}
  .fastext{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin-top:1em}
  .fastext a,.fastext span{display:block;text-align:center;padding:.18em .2em;text-decoration:none;color:#000;font-size:.95em}
  .fastext a:hover,.fastext a:focus-visible{outline:3px solid #fff;outline-offset:-3px}
  .k-r{background:var(--re);color:#fff!important}.k-g{background:var(--gr)}.k-y{background:var(--ye)}.k-c{background:var(--cy)}
  a{color:inherit}
  .muted{opacity:.85}
  @media (prefers-reduced-motion:reduce){.blink{animation:none}}
</style>
</head>
<body>
<main class="tv" aria-live="polite">
  <div class="row hdr"><span><span class="w">P302</span> <span class="y">CALFAX 302</span></span><span><span class="w" id="date"></span> <span class="y" id="clock"></span></span></div>
  <div class="band" aria-hidden="true">''' + '<i></i>' * 18 + '''</div>
  <div class="title">FOOTBALL</div>
  <div class="row c" id="league">SEARCHING FOR A SIGNAL<span class="blink">...</span></div>
  <div class="row"> </div>
  <div class="score" id="score"></div>
  <div class="row g" id="status"></div>
  <div class="row w" id="venue"></div>
  <div class="row"> </div>
  <div class="row bg-bl"><span class="y"> LOCAL BEER </span></div>
  <div class="row c dh" id="beer"></div>
  <div class="row w muted" id="beerline"></div>
  <div class="row"> </div>
  <div class="row y" id="also"></div>
  <div id="alsolist"></div>
  <div class="fastext">
    <a href="#" class="k-r" id="another">NEXT GAME</a>
    <a href="/travel-guides/" class="k-g" id="guide">GUIDES</a>
    <a href="/match-hub/" class="k-y">THE BAR</a>
    <a href="/stadium/" class="k-c">STADIUM</a>
  </div>
  <div class="row muted" style="margin-top:.6em;font-size:.75em">Scores from ESPN's public scoreboard feed. Not affiliated with any league or club. Drink responsibly.</div>
</main>
<script>
var DATA=''' + data + ''';
(function(){
  var $=function(id){return document.getElementById(id)};
  function tick(){var d=new Date();
    try{$('date').textContent=new Intl.DateTimeFormat('en-GB',{weekday:'short',day:'2-digit',month:'short',timeZone:'Europe/London'}).format(d).replace(',','');
        $('clock').textContent=new Intl.DateTimeFormat('en-GB',{hour:'2-digit',minute:'2-digit',second:'2-digit',timeZone:'Europe/London'}).format(d)}catch(e){}}
  tick();setInterval(tick,1000);
  var live=[],upcoming=[],current=null,refresh=null;
  function up(s){return (s||'').toUpperCase()}
  function pad(s,n){s=up(s);return s.length>n?s.slice(0,n):s}
  function beerFor(ev){
    var c=ev.city||'',k=ev.country||'';
    var parts=[c].concat(c.split(',').map(function(x){return x.trim()}));
    for(var i=0;i<parts.length;i++){if(DATA.city[parts[i]])return {beer:DATA.city[parts[i]],where:parts[i]}}
    if(DATA.country[k])return {beer:DATA.country[k],where:k};
    return {beer:'whatever the locals are drinking',where:c||k||'here'};
  }
  function guideFor(ev){var ps=(ev.city||'').split(',').map(function(x){x=x.trim();return DATA.alias[x]||x});
    for(var i=0;i<ps.length;i++){if(DATA.guides.indexOf(ps[i])>=0)return ps[i]}return null}
  function norm(e,lg,slug){
    var comp=(e.competitions||[])[0]||{},cs=comp.competitors||[],h=null,a=null;
    cs.forEach(function(t){if(t.homeAway==='home')h=t;else a=t});h=h||cs[0];a=a||cs[1];if(!h||!a)return null;
    var v=comp.venue||{},ad=v.address||{},st=(e.status||{}).type||{};
    return {id:e.id,slug:slug,league:lg,home:(h.team||{}).shortDisplayName||(h.team||{}).displayName,away:(a.team||{}).shortDisplayName||(a.team||{}).displayName,
      hs:h.score,as:a.score,state:st.state,detail:st.shortDetail||'',clock:(e.status||{}).displayClock||'',date:e.date,
      venue:v.fullName||'',city:ad.city||'',country:ad.country||''};
  }
  function load(){
    var urls=DATA.leagues.map(function(l){return 'https://site.api.espn.com/apis/site/v2/sports/soccer/'+l+'/scoreboard'});
    return Promise.all(urls.map(function(u){return fetch(u).then(function(r){return r.ok?r.json():null}).catch(function(){return null})})).then(function(res){
      live=[];upcoming=[];var any=false;
      res.forEach(function(d,ix){if(!d)return;any=true;var lg=((d.leagues||[])[0]||{}).name||'',slug=DATA.leagues[ix];
        (d.events||[]).forEach(function(e){var n=norm(e,lg,slug);if(!n)return;
          if(n.state==='in')live.push(n);else if(n.state==='pre'&&new Date(n.date)>new Date())upcoming.push(n)})});
      upcoming.sort(function(a,b){return new Date(a.date)-new Date(b.date)});
      return any;
    });
  }
  function rows(list){return list.map(function(g){
      return '<div class="row w">'+pad(g.home,12).padEnd(12)+' '+(g.hs||'0')+'-'+(g.as||'0')+' '+pad(g.away,12)+'</div>'}).join('')}
  function show(g,isLive){
    current=g;
    $('league').textContent=up(g.league);
    $('score').innerHTML='<b class="w">'+pad(g.home,16)+'</b><b class="y">'+(isLive?(g.hs||'0'):'')+'</b><b class="w">'+pad(g.away,16)+'</b><b class="y">'+(isLive?(g.as||'0'):'')+'</b>';
    if(isLive){$('status').innerHTML='<span class="blink">LIVE</span>  '+up(g.clock||g.detail)}
    else{var mins=Math.max(0,Math.round((new Date(g.date)-new Date())/60000)),h=Math.floor(mins/60),m=mins%60;
      var ko=new Intl.DateTimeFormat('en-GB',{hour:'2-digit',minute:'2-digit',timeZone:'Europe/London'}).format(new Date(g.date));
      $('status').textContent='NO GAMES IN PLAY - KICK-OFF '+ko+' UK (IN '+(h?h+'H ':'')+m+'M)'}
    $('venue').textContent=up([g.venue,g.city,g.country].filter(Boolean).join(', '));
    var b=beerFor(g);$('beer').textContent=up(b.beer);
    $('beerline').textContent='When in '+b.where+', do as the locals do.';
    var gc=guideFor(g),gl=$('guide');
    if(gc){gl.textContent='OUR GUIDE';gl.href='/travel-guides/?city='+encodeURIComponent(gc)}else{gl.textContent='GUIDES';gl.href='/travel-guides/'}
    var others=(isLive?live:upcoming).filter(function(x){return x!==g}).slice(0,4);
    $('also').textContent=others.length?(isLive?'ALSO IN PLAY':'COMING UP'):'';
    $('alsolist').innerHTML=isLive?rows(others):others.map(function(x){
      var t=new Intl.DateTimeFormat('en-GB',{hour:'2-digit',minute:'2-digit',timeZone:'Europe/London'}).format(new Date(x.date));
      return '<div class="row w">'+t+' '+pad(x.home,12)+' V '+pad(x.away,12)+'</div>'}).join('');
  }
  function pick(){
    if(live.length){var pool=live.length>1&&current?live.filter(function(x){return x.id!==current.id}):live;show(pool[Math.floor(Math.random()*pool.length)],true)}
    else if(upcoming.length){var p=upcoming.slice(0,8).filter(function(x){return !current||x.id!==current.id});show((p.length?p:upcoming)[Math.floor(Math.random()*Math.min(8,(p.length?p:upcoming).length))],false)}
    else{$('league').textContent='NO SIGNAL';$('score').innerHTML='';$('status').textContent='THE FEED IS DOWN - TRY AGAIN LATER';$('venue').textContent='';
      $('beer').textContent='A PINT OF WHATEVER IS ON';$('beerline').textContent='';$('also').textContent='';$('alsolist').innerHTML=''}
  }
  function start(){load().then(function(ok){if(!ok){current=null;live=[];upcoming=[]}pick()})}
  $('another').addEventListener('click',function(e){e.preventDefault();
    $('league').innerHTML='SEARCHING<span class="blink">...</span>';
    setTimeout(function(){if(live.length||upcoming.length)pick();else start()},350)});
  start();
  // keep the score fresh
  refresh=setInterval(function(){if(!current||current.state!=='in'||document.hidden)return;var cur=current;
    fetch('https://site.api.espn.com/apis/site/v2/sports/soccer/'+cur.slug+'/scoreboard').then(function(r){return r.json()}).then(function(d){
      var lg=((d.leagues||[])[0]||{}).name||cur.league;
      (d.events||[]).forEach(function(e){if(e.id!==cur.id)return;var n=norm(e,lg,cur.slug);if(n&&current&&current.id===n.id){show(n,n.state==='in')}})}).catch(function(){})},60000);
})();
</script>
</body>
</html>
'''


# ====================================================================== full-screen pub (v2)
def _defs(sfx):
    return ('<defs>'
            f'<linearGradient id="screenSheen{sfx}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".16"/><stop offset=".45" stop-color="#fff" stop-opacity="0"/></linearGradient>'
            f'<radialGradient id="crtSheen{sfx}" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#fff" stop-opacity=".18"/><stop offset=".6" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".35"/></radialGradient>'
            f'<radialGradient id="lufcGlow{sfx}" cx=".5" cy=".3" r=".8"><stop offset="0" stop-color="#2a56c8"/><stop offset="1" stop-color="#0b1f63" stop-opacity="0"/></radialGradient>'
            '</defs>')

def _sfx(svg, sfx):
    for k in ('screenSheen', 'crtSheen', 'lufcGlow'):
        svg = svg.replace(f'url(#{k})', f'url(#{k}{sfx})')
    return svg

def leeds_tv_svg():
    return ('<svg viewBox="-20 -72 340 258" role="img" aria-label="Leeds United match hub telly">' + _defs('L') + _sfx(modern_tv(0, 0, 300), 'L') + '</svg>')

def world_tv_svg():
    return ('<svg viewBox="-8 -72 316 312" role="img" aria-label="Retro telly showing teletext football">' + _defs('W') + _sfx(retro_tv(0, 0, 300), 'W') + '</svg>')

def hub_tv_svg():
    # the big middle telly: a sports-news style title screen
    return '''<svg viewBox="-14 -46 668 420" role="img" aria-label="The Match Hub">
  <defs>
    <linearGradient id="hubBg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0d1f5c"/><stop offset=".55" stop-color="#081236"/><stop offset="1" stop-color="#050816"/></linearGradient>
    <linearGradient id="hubRed" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e3001b"/><stop offset="1" stop-color="#a30016"/></linearGradient>
    <linearGradient id="hubSheen" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".12"/><stop offset=".4" stop-color="#fff" stop-opacity="0"/></linearGradient>
    <clipPath id="hubClip"><rect x="0" y="0" width="640" height="360"/></clipPath>
  </defs>
  <rect x="300" y="-46" width="40" height="40" fill="#2a2a30"/><rect x="250" y="-46" width="140" height="10" rx="3" fill="#3a3a42"/>
  <rect x="-14" y="-14" width="668" height="388" rx="10" fill="#111216"/><rect x="-14" y="-14" width="668" height="388" rx="10" fill="none" stroke="#2c2e36" stroke-width="2"/>
  <g clip-path="url(#hubClip)">
    <rect width="640" height="360" fill="url(#hubBg)"/>
    <path d="M380 0 L640 0 L640 360 L250 360 Z" fill="#ffffff" opacity=".04"/>
    <path d="M470 0 L640 0 L640 360 L380 360 Z" fill="#ffffff" opacity=".04"/>
    <g opacity=".22" stroke="#4d7cff" stroke-width="1">''' + ''.join(f'<line x1="{x}" y1="0" x2="{x-120}" y2="360"/>' for x in range(80, 760, 40)) + '''</g>
    <rect x="28" y="26" width="64" height="26" fill="url(#hubRed)"/><text x="60" y="45" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="20" fill="#fff" letter-spacing="2">LIVE</text>
    <rect x="92" y="26" width="76" height="26" fill="#ffffff"/><text x="130" y="45" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="20" fill="#0d1f5c" class="hubclock">22:00</text>
    <g transform="skewX(-8)">
      <text x="70" y="150" font-family="Bebas Neue, Impact, sans-serif" font-size="44" fill="#ffcd00" letter-spacing="4">THE</text>
      <text x="70" y="226" font-family="Bebas Neue, Impact, sans-serif" font-size="96" fill="#ffffff" letter-spacing="2" textLength="380" lengthAdjust="spacingAndGlyphs">MATCH HUB</text>
      <rect x="72" y="240" width="370" height="10" fill="url(#hubRed)"/>
    </g>
    <text x="48" y="282" font-family="Inter, system-ui, sans-serif" font-weight="600" font-size="17" fill="#c8d3f5">Leeds on the left. The rest of the world on the right.</text>
    <rect x="0" y="316" width="640" height="44" fill="#ffffff"/>
    <rect x="0" y="316" width="118" height="44" fill="url(#hubRed)"/><text x="59" y="345" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="22" fill="#fff" letter-spacing="2">LATEST</text>
    <svg x="118" y="316" width="522" height="44" viewBox="0 0 522 44"><g class="ticker"><text x="0" y="29" font-family="Bebas Neue, Impact, sans-serif" font-size="22" fill="#0d1f5c" letter-spacing="1">CALFAX 302 NOW SHOWING ON THE OLD SET  ·  LEEDS MATCH HUB COMING SOON  ·  MARCHING ON TOGETHER  ·  ONE BEER AT A TIME  ·  FOLLOW @CALZ88  ·  CALFAX 302 NOW SHOWING ON THE OLD SET  ·  LEEDS MATCH HUB COMING SOON  ·  MARCHING ON TOGETHER  ·  ONE BEER AT A TIME  ·  FOLLOW @CALZ88  ·</text></g></svg>
    <rect width="640" height="360" fill="url(#hubSheen)"/>
  </g>
  <circle cx="630" cy="368" r="2.5" fill="#3dff7a"/>
</svg>'''

def poster_leeds():
    return '''<svg viewBox="0 0 150 205" role="img" aria-label="Poster: Leeds United Match Hub, coming soon">
  <rect x="2" y="4" width="146" height="199" rx="2" fill="#f7f2e4"/>
  <rect x="10" y="12" width="130" height="140" fill="#1e3f9a"/>
  <path d="M10 112 L140 74 L140 92 L10 130 Z" fill="#ffcd00"/><path d="M10 121 L140 83 L140 87 L10 125 Z" fill="#ffffff"/>
  <circle cx="75" cy="56" r="22" fill="#ffffff"/><path d="M68 49 l7 -5 l7 5 l-3 8 h-8 z" fill="#1e3f9a"/>''' + ''.join(f'<path d="M75 56 L{75+22*__import__("math").cos(a):.1f} {56+22*__import__("math").sin(a):.1f}" stroke="#1e3f9a" stroke-width="1.2"/>' for a in (0.6, 2.2, 3.8, 5.4)) + '''
  <text x="75" y="172" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="22" fill="#0a1838" letter-spacing="1" textLength="118" lengthAdjust="spacingAndGlyphs">LEEDS UNITED</text>
  <text x="75" y="187" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="11" fill="#1e3f9a" letter-spacing="3">MATCH HUB</text>
  <g transform="rotate(-14 104 140)"><rect x="70" y="128" width="72" height="22" rx="3" fill="none" stroke="#d22630" stroke-width="2.4"/><text x="106" y="144" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="14" fill="#d22630" letter-spacing="2" textLength="62" lengthAdjust="spacingAndGlyphs">COMING SOON</text></g>
  <circle cx="75" cy="10" r="3.5" fill="#d22630"/><circle cx="74" cy="9" r="1.2" fill="#fff" opacity=".7"/>
</svg>'''

def poster_world():
    cols = ['#ff0000', '#00ff00', '#ffff00', '#00ffff', '#ff00ff', '#ffffff']
    return '''<svg viewBox="0 0 150 205" role="img" aria-label="Poster: Around the World on CALFAX 302">
  <rect x="2" y="4" width="146" height="199" rx="2" fill="#111"/>
  <rect x="10" y="12" width="130" height="140" fill="#000"/>
  <text x="16" y="26" font-family="'Courier New', monospace" font-weight="700" font-size="9" fill="#fff">P302</text><text x="134" y="26" text-anchor="end" font-family="'Courier New', monospace" font-weight="700" font-size="9" fill="#ff0">CALFAX</text>
  ''' + ''.join(f'<rect x="{14+i*12.2:.1f}" y="32" width="10" height="{6+(i*7)%8}" fill="#0ff" opacity="{.6+(i%3)*.2:.1f}"/>' for i in range(10)) + '''
  <circle cx="75" cy="92" r="34" fill="#00f"/><path d="M50 80 Q60 70 72 78 T96 74 L100 92 Q86 100 72 96 T48 100 Z M60 108 Q72 104 84 110 L80 120 Q70 118 62 120 Z" fill="#0f0"/>
  <ellipse cx="75" cy="92" rx="34" ry="12" fill="none" stroke="#0ff" stroke-width="1"/><ellipse cx="75" cy="92" rx="14" ry="34" fill="none" stroke="#0ff" stroke-width="1"/>
  <text x="75" y="145" text-anchor="middle" font-family="'Courier New', monospace" font-weight="700" font-size="11" fill="#ff0" textLength="118" lengthAdjust="spacingAndGlyphs">LIVE + LOCAL BEER</text>
  <text x="75" y="172" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="21" fill="#ffffff" letter-spacing="1" textLength="124" lengthAdjust="spacingAndGlyphs">AROUND THE WORLD</text>
  ''' + ''.join(f'<rect x="{10+i*21.7:.1f}" y="180" width="21.7" height="8" fill="{c}"/>' for i, c in enumerate(cols)) + '''
  <circle cx="75" cy="10" r="3.5" fill="#1e3f9a"/><circle cx="74" cy="9" r="1.2" fill="#fff" opacity=".7"/>
</svg>'''

def shelf_svg():
    rnd = random.Random(9)
    g = ['<svg viewBox="0 0 220 240" aria-hidden="true">']
    g.append('<rect x="70" y="0" width="80" height="58" rx="4" fill="#0a1838"/><text x="110" y="25" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="17" fill="#ffcd00" letter-spacing="2">THE</text><text x="110" y="46" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="17" fill="#ffcd00" letter-spacing="1">LOCAL</text>')
    for shelf in (140, 230):
        g.append(f'<rect x="0" y="{shelf}" width="220" height="10" fill="#5a361b"/>')
        x = 8
        while x < 205:
            w = rnd.choice([12, 14, 16]); h = rnd.randint(38, 62); c = rnd.choice(['#2f6b3c', '#7a4b27', '#c9a227', '#3a5aa0', '#a8322e', '#d8d2c4'])
            g.append(f'<rect x="{x}" y="{shelf-h}" width="{w}" height="{h-14}" rx="3" fill="{c}" opacity=".9"/><rect x="{x+w/2-2}" y="{shelf-h-10}" width="4" height="12" fill="{c}"/><rect x="{x+2}" y="{shelf-h+14}" width="{w-4}" height="10" fill="#f7f2e4" opacity=".75"/>')
            x += w + 6
    g.append('</svg>')
    return ''.join(g)

def bar_top_svg():
    # pumps and pints sitting on the bar (stretches across the screen)
    g = ['<svg viewBox="0 0 1200 90" preserveAspectRatio="xMidYMax meet" aria-hidden="true">']
    for i, x in enumerate((470, 520, 570, 630, 680, 730)):
        g.append(f'<rect x="{x-5}" y="38" width="10" height="52" rx="3" fill="#f2efe6"/><rect x="{x-9}" y="14" width="18" height="28" rx="4" fill="{["#1e3f9a", "#a8322e", "#2f6b3c", "#c9a227", "#1e3f9a", "#7a1f2b"][i]}"/><rect x="{x-7}" y="22" width="14" height="10" fill="#f7f2e4"/>')
    for x, full in ((260, 1), (310, .6), (900, 1), (950, .8), (1080, 1), (130, .9)):
        g.append(f'<path d="M{x-12} 90 L{x-15} 50 L{x+15} 50 L{x+12} 90 Z" fill="#f7f2e4" opacity=".35"/><path d="M{x-12} 90 L{x-14.5} {90-40*full:.0f} L{x+14.5} {90-40*full:.0f} L{x+12} 90 Z" fill="#e8a317"/><rect x="{x-15}" y="{86-40*full:.0f}" width="30" height="6" rx="3" fill="#ffffff"/>')
    g.append('</svg>')
    return ''.join(g)

PUB_CSS = """
  html{height:100%}
  body.pubpage{min-height:100vh;min-height:100dvh;overflow-x:hidden;
    background:
      radial-gradient(ellipse 20% 34% at 12% 0,rgba(255,217,138,.30),transparent 70%),
      radial-gradient(ellipse 24% 38% at 50% 0,rgba(255,217,138,.30),transparent 70%),
      radial-gradient(ellipse 20% 34% at 88% 0,rgba(255,217,138,.30),transparent 70%),
      repeating-linear-gradient(90deg,rgba(255,255,255,.035) 0 18px,transparent 18px 40px),
      linear-gradient(#1f3d30,#14261c)}
  body.pubpage header{position:relative;z-index:3;max-width:none;padding:14px clamp(16px,3vw,40px)}
  .lamps{position:absolute;left:22%;right:22%;top:0;justify-content:space-between!important;display:flex;justify-content:space-around;pointer-events:none;z-index:1}
  .lamps i{display:block;width:40px;height:38px;position:relative}
  .lamps i::before{content:"";position:absolute;left:19px;top:0;width:2px;height:22px;background:#2a2a2a}
  .lamps i::after{content:"";position:absolute;left:0;top:22px;width:40px;height:16px;background:#c9a227;clip-path:polygon(22% 0,78% 0,100% 100%,0 100%)}
  main.wall{position:relative;z-index:2;flex:1;display:flex;flex-direction:column;justify-content:space-evenly;gap:clamp(8px,1.6vh,20px);padding:0 16px}
  .sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
  .hubtv>svg,.tvl>svg,.shelf>svg{width:100%;height:auto;display:block;overflow:visible}
  .tier{display:flex;align-items:center;justify-content:center;gap:clamp(14px,4vw,70px)}
  .tier.low{align-items:flex-end;gap:clamp(10px,2.6vw,44px)}
  .hubtv{width:min(46vw,46vh,720px);filter:drop-shadow(0 18px 22px rgba(0,0,0,.5))}
  .tvl{display:block;text-decoration:none;outline:none;transition:transform .3s ease,filter .3s ease;filter:drop-shadow(0 16px 18px rgba(0,0,0,.45))}
  .tvl:hover,.tvl:focus-visible{transform:translateY(-6px) scale(1.03);filter:drop-shadow(0 0 22px rgba(255,205,0,.55)) drop-shadow(0 16px 18px rgba(0,0,0,.45))}
  .tvl:focus-visible{outline:3px solid #fff;outline-offset:6px;border-radius:12px}
  .tv-leeds{width:min(28vw,39vh,480px)}
  .tv-world{width:min(25vw,33vh,430px)}
  .shelf{width:min(13vw,20vh,210px)}
  .poster{width:min(12vw,24vh,200px);transform:rotate(var(--r));transform-origin:50% 0}
  .poster:hover,.poster:focus-visible{transform:rotate(0) translateY(-6px) scale(1.06)}
  .pbar{position:relative;z-index:2;margin-top:clamp(4px,1vh,10px)}
  .bartop{width:min(100%,1400px);margin:0 auto;height:clamp(44px,8vh,84px)}
  .bartop>svg{width:100%;height:100%;display:block}
  .counter{height:16px;background:linear-gradient(#b07a4a 0 5px,#8a5a32 5px);box-shadow:0 4px 8px rgba(0,0,0,.35)}
  .front{height:clamp(40px,7vh,80px);background:repeating-linear-gradient(90deg,transparent 0 16px,#3b2312 16px 20px,transparent 20px 116px,#3b2312 116px 120px),linear-gradient(#5a361b,#4a2c16)}
  body.pubpage footer{padding:12px 16px}
  .ticker{animation:tick 28s linear infinite}
  @keyframes tick{from{transform:translateX(0)}to{transform:translateX(-50%)}}
  @media (max-width:820px),(max-aspect-ratio:1/1){
    main.wall{justify-content:flex-start;gap:20px;padding-top:4px}
    .hubtv{width:min(92vw,560px);margin:0 auto}
    .lamps{display:none}
    .tier.top{flex-wrap:wrap}
    .tier.top .poster{display:none}
    .tier.low{flex-direction:column;align-items:center;gap:22px}
    .tier.low .shelf{display:none}
    .tv-leeds{width:min(84vw,420px)}
    .tv-world{width:min(76vw,380px)}
    .tier.posters{display:flex!important;gap:26px;padding-top:8px}
    .tier.posters .poster{width:min(36vw,170px)}
  }
  .tier.posters{display:none}
  @media (max-height:700px) and (min-aspect-ratio:1/1){body.pubpage header{padding-top:8px;padding-bottom:4px}.front{height:24px}body.pubpage footer{padding:6px 16px}}
  @media (prefers-reduced-motion:reduce){.ticker{animation:none}.tvl,.poster{transition:none}}
"""
