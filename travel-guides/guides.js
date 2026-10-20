// ===== Rob's Travel Guides =====
// Add a city by copying one block below and filling it in. Leave out anything you don't need.
// visited: "YYYY-MM".  rating: 1-5 (would you go back?) - leave out to hide it.
// colour: "teal", "red", "blue", "green", "orange" or "purple".
// Pubs and facts were researched online in October 2026 - pint prices are rough estimates.
window.GUIDES = [
  {
    city: "Leeds", region: "West Yorkshire", country: "United Kingdom", colour: "blue",
    pint: "~£5", localBeer: "Kirkstall Brewery", bestFor: "Historic pubs & matchdays",
    spoons: { name: "Stick or Twist", note: "big city-centre Spoons near the Arena" },
    bars: [
      { name: "Whitelock's Ale House", note: "dates back to 1715, tucked down a city-centre yard" },
      { name: "The Victoria & Commercial", note: "restored Grade II-listed Victorian interior" },
      { name: "Kirkstall Bridge Inn", note: "riverside, pouring Kirkstall's own beers" }
    ],
    eat: "Graze Kirkgate Market, or steak and ale pie at the Lamb & Flag by the Minster.",
    dontMiss: "A night match under the lights at Elland Road.",
    football: "Leeds United at Elland Road. Headingley for the Rhinos and Yorkshire cricket.",
    gettingThere: "Leeds station is a major hub: direct trains from London, Manchester, York and beyond."
  },
  {
    city: "Wakefield", region: "West Yorkshire", country: "United Kingdom", colour: "red",
    pint: "~£5", localBeer: "Ossett Brewery", bestFor: "Real ale crawl",
    spoons: { name: "The Six Chimneys", note: "Kirkgate, open from 8am, award-winning loos" },
    bars: [
      { name: "Harry's Bar", note: "log fires, timber beams, up to eight casks" },
      { name: "The Black Rock", note: "Grade II-listed, near the cathedral" },
      { name: "Luis Bar", note: "Ossett's bar in the old Fernandes maltings" }
    ],
    eat: "Anything with Yorkshire forced rhubarb - Wakefield is the heart of the Rhubarb Triangle.",
    dontMiss: "The Hepworth Wakefield gallery, then a pint at the Exchange Tap.",
    football: "Wakefield Trinity rugby league at Belle Vue (DIY Kitchens Stadium).",
    gettingThere: "Wakefield Westgate is on the East Coast Main Line - quick from Leeds or London."
  },
  {
    city: "Batley", region: "West Yorkshire", country: "United Kingdom", colour: "green",
    pint: "~£4.50", localBeer: "Yorkshire cask guests", bestFor: "No-frills locals",
    spoons: { name: "The Union Rooms", note: "in the grand old Union Bank, local guest ales" },
    bars: [
      { name: "Irish Democratic League Club (Batley Nash)", note: "friendly club, interesting guest ales, Leeds on the telly" }
    ],
    eat: "Batley is home to Fox's Biscuits - grab some for the train.",
    dontMiss: "Bagshaw Museum in Wilton Park, then up the road to Oakwell Hall.",
    football: "Batley Bulldogs rugby league at Mount Pleasant - famous for its sloping pitch.",
    gettingThere: "Batley station is on the Huddersfield line between Leeds and Manchester."
  },
  {
    city: "Dewsbury", region: "West Yorkshire", country: "United Kingdom", colour: "purple",
    pint: "~£4.50", localBeer: "Timothy Taylor Landlord", bestFor: "Station pub & canal pints",
    bars: [
      { name: "West Riding Refreshment Rooms", note: "on the station platform, ten handpumps" },
      { name: "Leggers Inn", note: "hayloft bar above old stables by the canal basin" }
    ],
    eat: "Wander the market (Wednesdays and Saturdays) for a cheap lunch.",
    dontMiss: "Dewsbury Minster - its bell 'Black Tom' tolls the Devil's Knell every Christmas Eve.",
    football: "Dewsbury Rams rugby league at Crown Flatt (FLAIR Stadium).",
    gettingThere: "TransPennine trains stop here - a good start to the Transpennine Real Ale Trail."
  },
  {
    city: "Huddersfield", region: "West Yorkshire", country: "United Kingdom", colour: "teal",
    pint: "~£4.50", localBeer: "Magic Rock", bestFor: "Real ale trail",
    spoons: { name: "The Lord Wilson", note: "King Street, up to five guest ales" },
    bars: [
      { name: "King's Head", note: "inside the Grade I-listed station, two wood burners" },
      { name: "Magic Rock Tap", note: "brewery taproom, food trucks at weekends" },
      { name: "The Sportsman", note: "1930s pub, a CAMRA favourite" }
    ],
    eat: "Pie and peas at the Slubbers Arms.",
    dontMiss: "The station's grand frontage in St George's Square, then out along the ale trail.",
    football: "Huddersfield Town at the Accu Stadium (the old John Smith's).",
    gettingThere: "On the TransPennine line - about 20 minutes from Leeds."
  },
  {
    city: "Sheffield", region: "South Yorkshire", country: "United Kingdom", colour: "orange",
    pint: "~£4.50", localBeer: "Abbeydale Moonshine", bestFor: "Kelham Island pub crawl",
    spoons: { name: "The Bankers Draft", note: "1904 bank by Castle Square, one of Sheffield's first Spoons" },
    bars: [
      { name: "Sheffield Tap", note: "right in the station, with its own Tapped brewery" },
      { name: "Kelham Island Tavern", note: "rotating real ales and a leafy beer garden" },
      { name: "The Fat Cat", note: "a Kelham Island classic" }
    ],
    eat: "Anything with a splash of Henderson's Relish - it's the law round here.",
    dontMiss: "A crawl round Kelham Island's old industrial streets.",
    football: "Sheffield United at Bramall Lane, Sheffield Wednesday at Hillsborough.",
    gettingThere: "Sheffield station on the Midland Main Line; about 40 minutes from Leeds."
  },
  {
    city: "Morley", region: "West Yorkshire", country: "United Kingdom", colour: "blue",
    pint: "~£4.50", localBeer: "West Yorkshire guests", bestFor: "Queen Street bar hop",
    spoons: { name: "The Picture House", note: "bigger than it looks, balcony and West Yorkshire guests" },
    bars: [
      { name: "Dyeworks", note: "micropub and bottle shop with local keg and cans" },
      { name: "Nomad", note: "small bar, good keg range and platters" }
    ],
    eat: "Platters of dips and charcuterie at Nomad.",
    dontMiss: "Morley Town Hall - Grade I listed, with a 160ft domed clock tower.",
    football: "A short hop to Elland Road for Leeds United.",
    gettingThere: "Morley station is on the Huddersfield line; buses run along Queen Street."
  },
  {
    city: "Harrogate", region: "North Yorkshire", country: "United Kingdom", colour: "green",
    pint: "~£5", localBeer: "Cold Bath Brewing Co", bestFor: "Spa town pints",
    spoons: { name: "The Winter Gardens", note: "inside the Victorian Royal Baths, with a grand staircase" },
    bars: [
      { name: "Cold Bath Brewing Co", note: "taproom with ever-changing small batches" },
      { name: "The Little Ale House", note: "cosy micropub, good ale range" },
      { name: "Harrogate Tap", note: "station pub that tops the 'best station pub' lists" }
    ],
    eat: "Tea and a Fat Rascal at Bettys, or small plates at the Fat Badger.",
    dontMiss: "A stroll through Valley Gardens and across the Stray.",
    football: "Harrogate Town at Wetherby Road (Marcy Fitness Stadium).",
    gettingThere: "Harrogate Line trains from Leeds and York."
  },
  {
    city: "Knaresborough", region: "North Yorkshire", country: "United Kingdom", colour: "red",
    pint: "~£5", localBeer: "Blind Jack's beer board", bestFor: "Riverside pubs",
    spoons: { name: "The Crown Inn", note: "High Street, twelve handpumps" },
    bars: [
      { name: "Blind Jack's", note: "named UK's Best Beer Pub at the 2025 Great British Pub Awards" },
      { name: "The World's End", note: "good beer and home cooking by the River Nidd" }
    ],
    eat: "Home-cooked pub food at the World's End.",
    dontMiss: "The view of the railway viaduct over the Nidd from the castle, then Mother Shipton's Cave.",
    football: "Knaresborough Town at Manse Lane.",
    gettingThere: "On the Harrogate Line between Leeds and York."
  },
  {
    city: "Boroughbridge", region: "North Yorkshire", country: "United Kingdom", colour: "purple",
    pint: "~£5", localBeer: "Rudgate Jorvik Blonde", bestFor: "Historic interiors",
    bars: [
      { name: "Tap on the Tutt", note: "1930s interior CAMRA rates of national importance" },
      { name: "The Crown Hotel", note: "17th-century coaching inn on the old Great North Road" }
    ],
    eat: "Lunch or dinner at the Crown Hotel.",
    dontMiss: "The Devil's Arrows - Bronze Age standing stones, the tallest 22ft.",
    gettingThere: "Just off the A1(M); no station, so it's a drive or bus from Harrogate or York."
  },
  {
    city: "Thirsk", region: "North Yorkshire", country: "United Kingdom", colour: "teal",
    pint: "~£5", localBeer: "Black Sheep & Hambleton", bestFor: "Market town pubs",
    spoons: { name: "The Three Tuns", note: "1740 coaching inn where James Herriot drank" },
    bars: [
      { name: "Little 3", note: "low-beamed warren of nooks, history back to 1214" },
      { name: "Golden Fleece Hotel", note: "grand old hotel on the market place, Black Sheep on" }
    ],
    eat: "Market day (Mondays and Saturdays), then the Golden Fleece restaurant.",
    dontMiss: "The World of James Herriot, in the vet's old surgery. Racecourse in summer.",
    football: "Thirsk Falcons in the Teesside League.",
    gettingThere: "Thirsk station is on the East Coast Main Line, about 1.5 miles out of town."
  },
  {
    city: "Northallerton", region: "North Yorkshire", country: "United Kingdom", colour: "orange",
    pint: "~£5", localBeer: "Black Sheep Best Bitter", bestFor: "High Street pubs",
    spoons: { name: "The Buck Inn", note: "north end of the High Street, six changing casks" },
    bars: [
      { name: "Harewood Arms", note: "narrow single-bar pub with changing local guests" },
      { name: "Golden Lion Hotel", note: "listed coaching inn with a golden lion over the porch" },
      { name: "The Fleece Inn", note: "15th-century building with oak-beamed ceilings" }
    ],
    eat: "Bettys on the High Street, or a meal at the Golden Lion.",
    dontMiss: "Market day on the High Street (Wednesdays and Saturdays).",
    football: "Northallerton Town at the Calvert Stadium.",
    gettingThere: "Northallerton is on the East Coast Main Line."
  },
  {
    city: "Tokyo", region: "Kanto", country: "Japan", colour: "red",
    pint: "¥600–1,200", localBeer: "Japanese craft on tap", bestFor: "Craft bars & tiny back-alley drinking",
    bars: [
      { name: "Mikkeller Bar Tokyo", note: "Shibuya, 20 taps over two floors" },
      { name: "DevilCraft", note: "Kanda/Nihonbashi, house IPAs and deep-dish pizza" },
      { name: "Tokyo Beerzilla", note: "Asakusa, British craft beer and cider" }
    ],
    eat: "Yakitori and a cold one in the tiny bars under the train tracks.",
    dontMiss: "Bar-hopping the tiny alley bars of Golden Gai in Shinjuku.",
    football: "FC Tokyo at Ajinomoto Stadium.",
    gettingThere: "Direct flights from London to Haneda and Narita."
  },
  {
    city: "Osaka", region: "Kansai", country: "Japan", colour: "orange",
    pint: "¥600–1,500", localBeer: "Minoh Beer", bestFor: "Street food & beer",
    bars: [
      { name: "Beer Belly Tenma", note: "Minoh Brewery's flagship, a dozen of their beers, no cover charge" },
      { name: "Dotonbori Brewery Factory", note: "brewed on site under the Shochikuza theatre" },
      { name: "Craft Beer Works Kamikaze", note: "west of Shinsaibashi, almost two dozen taps" }
    ],
    eat: "Takoyaki and okonomiyaki on the go around Dotonbori.",
    dontMiss: "Dotonbori's neon canal at night, then Osaka Castle by day.",
    football: "Gamba Osaka or Cerezo Osaka - two J.League clubs in one city.",
    gettingThere: "Shinkansen from Tokyo in about 2.5 hours, or fly into Kansai Airport."
  },
  {
    city: "Orlando", region: "Florida", country: "United States", colour: "purple",
    pint: "~$7–9", localBeer: "Ivanhoe Park Brewing", bestFor: "Breaks between the parks",
    bars: [
      { name: "Redlight Redlight", note: "Audubon Park, long-time beer bar turned microbrewery" },
      { name: "Ivanhoe Park Brewing Co.", note: "Ivanhoe Village, themed on a lost lakeside amusement park" },
      { name: "Hammered Lamb", note: "downtown, lake views and 70+ beers" }
    ],
    eat: "Mills 50 for the best Vietnamese and Asian food in town.",
    dontMiss: "A sunset lap of Lake Eola downtown, away from the theme parks.",
    football: "Orlando City SC at Inter&Co Stadium, downtown.",
    gettingThere: "Direct flights from the UK into Orlando International (MCO)."
  },
  {
    city: "Tampa Bay", region: "Florida", country: "United States", colour: "teal",
    pint: "~$7–9", localBeer: "Cigar City Jai Alai", bestFor: "Brewery hopping",
    bars: [
      { name: "Sky Puppy Brewing", note: "Ybor City, inside Tampa's oldest original firehouse" },
      { name: "BarrieHaus Beer Co.", note: "Ybor City lager specialists with a beer-garden feel" },
      { name: "Angry Chair Brewing", note: "Seminole Heights, famous for its stouts" }
    ],
    eat: "A Cuban sandwich in Ybor City, where Tampa reckons it was invented.",
    dontMiss: "A stroll along the Tampa Riverwalk, then out to Ybor's 7th Avenue.",
    football: "Tampa Bay Rowdies at Al Lang Stadium, St. Petersburg.",
    gettingThere: "Fly into Tampa International, or drive about 1.5 hours from Orlando."
  },
  {
    city: "Kissimmee", region: "Florida", country: "United States", colour: "green",
    pint: "~$7–9", localBeer: "Florida craft on tap", bestFor: "Pints near the parks",
    bars: [
      { name: "The Fox & Hounds Public House", note: "British pub food and pints for when you're homesick" },
      { name: "Rock & Brews", note: "craft beer, comfort food and rock music" },
      { name: "Charley's Pub", note: "happy hour noon till 7, Monday to Saturday" }
    ],
    eat: "Pub grub at the Fox & Hounds, or a giant American breakfast anywhere on the 192.",
    dontMiss: "Old Town's Saturday night classic car cruise.",
    football: "Orlando City SC are about half an hour away downtown.",
    gettingThere: "Right next to Walt Disney World, about 25 minutes from Orlando airport."
  },
  {
    city: "Chicago", region: "Illinois", country: "United States", colour: "blue",
    pint: "~$7–9", localBeer: "Goose Island", bestFor: "Historic taverns",
    bars: [
      { name: "Billy Goat Tavern", note: "home of the 1945 'Curse of the Billy Goat' on the Cubs" },
      { name: "The Berghoff", note: "holds Chicago liquor licence No. 1" },
      { name: "Marge's Still", note: "Old Town, claims to be the city's oldest tavern, from 1885" }
    ],
    eat: "Deep dish pizza, an Italian beef, or a Chicago dog - no ketchup.",
    dontMiss: "A Cubs game at Wrigley Field, then the bars of Wrigleyville.",
    football: "Chicago Fire FC at Soldier Field.",
    gettingThere: "Direct flights from London into O'Hare."
  },
  {
    city: "Philadelphia", region: "Pennsylvania", country: "United States", colour: "red",
    pint: "~$7–9", localBeer: "Yards Brewing", bestFor: "Old taverns & Belgian beer",
    bars: [
      { name: "McGillin's Olde Ale House", note: "since 1860, the oldest continuously operating bar in Philly" },
      { name: "Monk's Café", note: "Rittenhouse, a Belgian beer emporium" },
      { name: "Yards Brewing", note: "the city's own brewery and taproom" }
    ],
    eat: "A cheesesteak, obviously, then graze Reading Terminal Market.",
    dontMiss: "The Liberty Bell and Independence Hall, then run the Rocky steps.",
    football: "Philadelphia Union at Subaru Park in Chester.",
    gettingThere: "Direct flights from London into Philadelphia International."
  }
];
