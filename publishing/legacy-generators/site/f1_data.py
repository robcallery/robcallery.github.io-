# Travelling F1 in 2026 - from Rob's F1 Host Cities workbook, checked against the live 2026 calendar (Jolpica, Oct 2026).
# Bahrain moved to Sepang (Kuala Lumpur); Saudi Arabia dropped. Prices: Numbeo "Domestic Draft Beer (0.5 Liter)", Oct 2026,
# for the host city or the nearest city Numbeo covers. Bars: workbook picks, with placeholders and closed venues replaced.
SHELF = 'f1-2026'
SHORTGP = {'United States GP': 'US GP', 'Mexico City GP': 'Mexico GP', 'Bahrain GP in Malaysia': 'Bahrain GP'}
NOTE = ("Prices are Numbeo's October 2026 average for a half-litre draught in the host city, or the nearest city it covers. "
        "Calendar as of October 2026 - Bahrain's race moved to Sepang and Saudi Arabia was dropped. Bars were checked in October 2026, but check before you go.")
# city, round, GP, date, month, country, colour, pint, local beer, best for, bars[(name, note)], eat, don't miss, football, getting there, tip, polaroid title, did you know
F = [
 ('Melbourne', 1, 'Australian GP', '8 Mar', 'March', 'Australia', 'teal', 'A$14 (0.5L draught)', 'Carlton Draught - brewed in Melbourne since 1864', 'Laneways and sport',
  [('The Lincoln', 'Carlton pub'), ('Heartbreaker', 'CBD bar')], 'A flat white and a meat pie.', 'Federation Square.', 'Melbourne Cricket Ground.',
  'Trams to Albert Park.', 'Walk the Albert Park lake loop before the crowds arrive.', 'Albert Park and the city skyline',
  'Albert Park is built on public roads around the lake, open to traffic for most of the year.'),
 ('Shanghai', 2, 'Chinese GP', '15 Mar', 'March', 'China', 'red', '¥8 (0.5L draught)', "Reeb - Shanghai's own lager (Tsingtao is everywhere too)", 'Skyline and street food',
  [('The BREW', 'Kerry Hotel Pudong'), ('Shanghai Brewery', 'brewpub - check it is open')], 'Xiaolongbao.', 'The Bund.', 'Shanghai Stadium.',
  'Metro Line 11 to the circuit in Jiading.', 'See the Bund skyline at night.', 'The Bund waterfront',
  'The track layout is shaped like 上 (shang), the first character of Shanghai.'),
 ('Suzuka', 3, 'Japanese GP', '29 Mar', 'March', 'Japan', 'purple', '¥500 (0.5L draught, Nagoya)', 'Ise Kadoya - craft beer from Ise, in the same prefecture (Mie)', 'Motorsport heritage',
  [('Heisei Horumon Shiroko', 'grill izakaya near Shiroko station'), ('Sushi Izakaya Minato', 'by Hirata-cho station, on the line to the circuit')], 'Miso katsu.', 'Suzuka Circuit and its amusement park.', 'Suzuka Point Getter Stadium.',
  'Kintetsu rail to Shiroko, then the shuttle.', 'Ride the Ferris wheel at the circuit park.', 'The Suzuka Ferris wheel',
  "Suzuka is F1's only figure-of-eight - the track crosses over itself on a bridge."),
 ('Miami', 4, 'Miami GP', '3 May', 'May', 'United States', 'orange', '$8 (0.5L draught)', "La Rubia from Wynwood Brewing - now brewed at Veza Sur", 'Beaches and nightlife',
  [('Veza Sur Brewing Co.', 'Wynwood - pours Wynwood Brewing beers since its taproom closed'), ('Concrete Beach Brewery', 'Wynwood - check it is open')], 'A Cuban sandwich.', 'Wynwood Walls.', 'Hard Rock Stadium.',
  'Rideshare or the official shuttles.', 'The race is in Miami Gardens, not Miami Beach - plan your travel.', 'Wynwood murals',
  'The circuit wraps around Hard Rock Stadium, home of the Miami Dolphins.'),
 ('Montréal', 5, 'Canadian GP', '24 May', 'May', 'Canada', 'red', 'C$9 (0.5L draught)', 'Dieu du Ciel! - Montréal brewpub beers', 'Festivals and French culture',
  [('Dieu du Ciel!', 'Mile End brewpub'), ('Brutopia', 'downtown brewpub')], 'Poutine.', 'Old Montréal.', 'Stade Saputo.',
  'Metro to Jean-Drapeau.', 'The metro is easiest on race weekend.', 'The Old Port',
  'The circuit is on Île Notre-Dame, an island built for Expo 67.'),
 ('Monaco', 6, 'Monaco GP', '7 Jun', 'June', 'Monaco', 'red', '€9 (0.5L draught)', 'Brasserie de Monaco - brewed on the harbour', 'Harbour glamour',
  [('Brasserie de Monaco', 'Port Hercule'), ('La Rascasse', 'trackside, on the corner of the same name')], 'Barbajuan.', "The Prince's Palace.", 'Stade Louis II.',
  'Rail to Monaco-Monte-Carlo, then walk.', 'Do not drive on race weekend.', 'Yachts in Port Hercule',
  'The Monaco Grand Prix was first held in 1929.'),
 ('Barcelona', 7, 'Barcelona GP', '14 Jun', 'June', 'Spain', 'orange', '€3.50 (0.5L draught)', 'Moritz or Estrella Damm', 'Architecture and tapas',
  [('BierCaB', 'craft beer bar, Eixample'), ('Garage Beer Co.', 'brewpub, Eixample')], 'Pa amb tomàquet.', 'Sagrada Família.', 'Estadi Olímpic / Camp Nou.',
  'Train to Montmeló, then walk or shuttle.', 'The circuit is outside the city - allow time.', 'Park Güell',
  'The Circuit de Barcelona-Catalunya opened in 1991.'),
 ('Spielberg', 8, 'Austrian GP', '28 Jun', 'June', 'Austria', 'red', '€5 (0.5L draught, Graz)', 'Gösser - brewed in Leoben, half an hour away', 'Alpine racing scenery',
  [('Ranissimo', 'Marktpassage, Spielberg'), ('London Inn', 'pub in Knittelfeld, next door')], 'Wiener schnitzel.', 'The Red Bull Ring.', 'Stadion Graz-Liebenau.',
  'Event shuttle or car.', 'Book your bed early - the valley fills up.', 'The Red Bull Ring',
  'The Red Bull Ring started life as the Österreichring in 1969.'),
 ('Silverstone', 9, 'British GP', '5 Jul', 'July', 'United Kingdom', 'blue', '£4.25 (0.5L draught, Northampton)', 'Hook Norton - Oxfordshire ales, just down the road', 'British motorsport',
  [('The White Horse', 'Stocks Hill - a motor racing pub, 10 minutes walk from the circuit'), ('The Green Man', 'A43, Brackley Hatch - handy for the circuit')], 'Fish and chips.', 'The Silverstone Museum.', 'Stadium MK, Milton Keynes.',
  'Official shuttles from nearby rail stations.', 'Stay in Northampton or Milton Keynes.', 'The Silverstone Wing',
  'Silverstone hosted the first ever F1 World Championship race, on 13 May 1950.'),
 ('Spa-Francorchamps', 10, 'Belgian GP', '19 Jul', 'July', 'Belgium', 'green', '€5 (0.5L draught, Liège)', 'Brasserie de Bellevaux from nearby Malmedy - or a Jupiler', 'Ardennes and racing',
  [('Havana Café', 'Rue de la Poste, Spa - Belgian beers')], 'Belgian waffles.', 'Eau Rouge and Raidillon.', 'Stade du Pairay, Seraing.',
  'Shuttles from Verviers and Spa.', 'Pack for sudden rain - the Ardennes has its own weather.', 'Eau Rouge',
  'At just over 7km, Spa is the longest circuit on the calendar.'),
 ('Budapest', 11, 'Hungarian GP', '26 Jul', 'July', 'Hungary', 'green', '1,200 Ft (0.5L draught)', 'Dreher - brewed in Budapest since 1854', 'Thermal baths and ruin bars',
  [('Élesztőház', 'craft beer hall'), ('Kandalló Pub', 'District VII')], 'Goulash.', "Fisherman's Bastion.", 'Puskás Aréna.',
  'HÉV rail and the race shuttle.', 'Soak at the Széchenyi Baths after a hot day trackside.', 'Parliament on the Danube',
  'In 1986 the Hungarian GP became the first F1 race behind the Iron Curtain.'),
 ('Zandvoort', 12, 'Dutch GP', '23 Aug', 'August', 'Netherlands', 'orange', '€7 (0.5L draught, Haarlem)', 'Jopen - brewed in nearby Haarlem', 'Beach and racing',
  [('Bruxelles aan Zee', 'Belgian beer bar'), ('Wapen van Zandvoort', 'café in the village')], 'Bitterballen.', 'Zandvoort beach.', 'Johan Cruyff Arena, Amsterdam.',
  'Train from Amsterdam to Zandvoort.', 'Leave the car at home on race weekend.', 'The Zandvoort dunes',
  'The circuit sits in the dunes and has two steeply banked corners.'),
 ('Monza', 13, 'Italian GP', '6 Sep', 'September', 'Italy', 'red', '€5 (0.5L draught)', 'Birrificio Lambrate from Milan', 'Speed and Italian heritage',
  [('Birrificio Lambrate', 'Milan brewpub'), ('Birrificio Carrobiolo', 'brewpub in Monza')], 'Risotto alla Milanese.', 'The Royal Villa of Monza.', 'U-Power Stadium.',
  'Train to Monza, then the race shuttles.', 'Explore the Parco di Monza around the track.', 'The old Monza banking',
  'Monza opened in 1922 and is known as the Temple of Speed.'),
 ('Madrid', 14, 'Spanish GP', '13 Sep', 'September', 'Spain', 'red', '€3.50 (0.5L draught)', 'Mahou - order a caña', 'Art and tapas',
  [('Fábrica Maravillas', 'brewpub, Malasaña'), ('La Tape', 'craft beer bar')], 'A bocadillo de calamares.', 'The Prado Museum.', 'Santiago Bernabéu.',
  'Metro to IFEMA, then follow the event instructions.', 'Check the travel plan - it is a brand-new circuit.', 'The Gran Vía',
  '2026 is the first year of the Madring, a new circuit around the IFEMA trade-fair grounds.'),
 ('Baku', 15, 'Azerbaijan GP', '26 Sep', 'September', 'Azerbaijan', 'teal', '3 manat (0.5L draught)', "Xirdalan - Azerbaijan's own lager", 'Old City meets skyscrapers',
  [('Paulaner Bräuhaus Baku', 'German brewhouse'), ('Compass Pub', 'pub')], 'Plov.', 'The Maiden Tower.', 'Tofiq Bahramov Stadium.',
  'Metro, or walk - the track is in the city.', 'The Old City walls border the circuit - walk them.', 'The Flame Towers',
  'The track squeezes past the Old City walls through a gap only about 7.6m wide.'),
 ('Kuala Lumpur', 16, 'Bahrain GP in Malaysia', '4 Oct', 'October', 'Malaysia', 'green', 'RM18 (0.5L draught)', 'Tiger and Carlsberg - both brewed in Selangor', 'Street food and skyscrapers',
  [('Taps Beer Bar', 'craft beer bar'), ('Changkat Bukit Bintang', 'the city\'s pub street')], 'Nasi lemak.', 'The Petronas Towers.', 'Bukit Jalil National Stadium.',
  'KLIA Ekspres to the airport, then a short taxi to Sepang.', 'Sepang is next to the airport, an hour south of the city - plan for traffic.', 'The Petronas Towers',
  'Sepang hosted the Malaysian GP from 1999 to 2017 - this year it hosts the Bahrain GP.'),
 ('Singapore', 17, 'Singapore GP', '11 Oct', 'October', 'Singapore', 'purple', 'S$11 (0.5L draught)', 'Tiger - brewed in Singapore since 1932', 'Skyline and hawker food',
  [('Brewerkz', 'brewpub'), ('Level33', 'brewery bar with a skyline view')], 'Hainanese chicken rice.', 'Gardens by the Bay.', 'National Stadium.',
  'MRT - roads close around the track.', 'Stay hydrated - the humidity is no joke.', 'Marina Bay Sands',
  "Singapore hosted F1's first night race, in 2008."),
 ('Austin', 18, 'United States GP', '25 Oct', 'October', 'United States', 'orange', '$8 (0.5L draught)', 'Austin Beerworks', 'Live music and barbecue',
  [('Austin Beerworks', 'brewery taproom'), ('Zilker Brewing', 'East Austin brewery')], 'Texas brisket.', 'The Texas State Capitol.', 'Q2 Stadium.',
  'Event shuttle or car.', 'Spend an evening on South Congress.', 'The Texas State Capitol',
  "COTA's first corner climbs a hill about 40m high."),
 ('Mexico City', 19, 'Mexico City GP', '1 Nov', 'November', 'Mexico', 'green', 'Mex$60 (0.5L draught)', 'Victoria - brewed in Mexico since 1865 - or local craft', 'Art and street food',
  [('Falling Piano Brewing Co.', 'Condesa brewery bar'), ('Hop The Beer Experience', 'craft beer bar')], 'Tacos al pastor.', 'Palacio de Bellas Artes.', 'Estadio Azteca.',
  'Metro to Ciudad Deportiva.', 'Take it easy - the altitude makes beer hit harder.', 'Palacio de Bellas Artes',
  'At about 2,200m it is the highest circuit on the calendar, and the track runs through a stadium.'),
 ('São Paulo', 20, 'Brazilian GP', '8 Nov', 'November', 'Brazil', 'green', 'R$15 (0.5L draught)', 'Colorado - craft beer from São Paulo state', 'Food and nightlife',
  [('Cervejaria Nacional', 'brewpub, Pinheiros'), ('Empório Alto dos Pinheiros', 'craft beer bar')], 'Pastel and feijoada.', 'Ibirapuera Park.', 'Allianz Parque.',
  'CPTM train to Autódromo.', 'Allow plenty of time - the traffic is legendary.', 'The São Paulo skyline',
  "Interlagos runs anticlockwise - it was Ayrton Senna's home race."),
 ('Las Vegas', 21, 'Las Vegas GP', '22 Nov', 'November', 'United States', 'purple', '$7.50 (0.5L draught)', 'Able Baker Brewing - Las Vegas brewery', 'Neon nightlife',
  [('Able Baker Brewing', 'brewery taproom'), ('Atomic Liquors', 'the oldest freestanding bar in Las Vegas')], 'A shrimp cocktail.', 'Fremont Street.', 'Allegiant Stadium.',
  'Walk or take the monorail - roads close.', 'The track runs along the Strip - check road closures.', 'The Welcome to Las Vegas sign',
  'The race runs late on a Saturday night, straight down the Strip.'),
 ('Lusail', 22, 'Qatar GP', '29 Nov', 'November', 'Qatar', 'teal', None, 'No local beer - alcohol is only served in licensed hotel bars', 'Modern architecture',
  [('The Bar at Provok', 'rooftop bar at Fairmont Doha, Lusail'), ('Rixos Premium Qetaifan Island North', 'hotel bars - check entry')], 'Machboos.', 'Lusail Marina.', 'Lusail Stadium.',
  'Metro and the event shuttle.', 'Respect the alcohol laws - licensed hotels only.', 'The Lusail Marina skyline',
  'Lusail was built for MotoGP in 2004; F1 first raced there in 2021.'),
 ('Abu Dhabi', 23, 'Abu Dhabi GP', '6 Dec', 'December', 'United Arab Emirates', 'blue', 'Dh42.50 (0.5L draught)', 'No local brewery - imported lagers in licensed venues', 'Island attractions',
  [("Stars 'N' Bars", 'Yas Marina'), ('Belgian Café', 'Radisson Blu Yas Island - check it is open')], 'Luqaimat.', 'Sheikh Zayed Grand Mosque.', 'Zayed Sports City Stadium.',
  'Taxi or the event shuttle.', 'Make a trip of it with the Yas Island theme parks.', 'The Yas Marina hotel',
  'The Yas Marina hotel straddles the track, and the race runs from day into night.'),
]

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad')
    from regions import load, save
    import json
    pre, G = load()
    G = [g for g in G if g.get('shelf') != SHELF]
    for (city, rnd, gp, date, month, country, colour, pint, beer, best, bars, eat, dm, foot, get, tip, ptitle, dyk) in F:
        g = {'city': city, 'region': f'{SHORTGP.get(gp, gp)} · {date}', 'country': country, 'shelf': SHELF, 'group': month, 'colour': colour}
        if pint: g['pint'] = pint
        g.update({'localBeer': beer, 'bestFor': best, 'bars': [{'name': n, 'note': t} for n, t in bars], 'eat': eat, 'dontMiss': dm,
                  'football': 'Football: ' + foot, 'gettingThere': get, 'tip': tip})
        G.append(g)
    save(pre, G)
    json.dump({c[0]: [c[16], c[17]] for c in F}, open('/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/f1_snaps.json', 'w'), ensure_ascii=False, indent=1)
    print('guides', len(G), 'f1', len(F))
