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
    spoons: { name: "The Union Rooms, Batley", note: "Dewsbury's Timepiece has closed, so it's a short hop to Batley", nearest: true },
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
    spoons: { name: "The Unicorn Hotel, Ripon", note: "no Spoons in Boroughbridge - this is the nearest, on Ripon market place", nearest: true },
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
  }
];
