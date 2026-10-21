// ===== Rob's Travel Guides =====
// Add a city by copying one block below and filling it in. Leave out anything you don't need.
// tip: a top tip, shown handwritten in biro.
// visited: "YYYY-MM".  rating: 1-5 (would you go back?) - leave out to hide it.
// colour: "teal", "red", "blue", "green", "orange" or "purple".
// Pubs and facts were researched online in October 2026 - pint prices are rough estimates.
window.GUIDES = [
  {
    "city": "Leeds",
    "region": "West Yorkshire",
    "country": "United Kingdom",
    "colour": "blue",
    "pint": "~£5",
    "localBeer": "Kirkstall Brewery",
    "bestFor": "Historic pubs & matchdays",
    "spoons": {
      "name": "Stick or Twist",
      "note": "big city-centre Spoons near the Arena"
    },
    "bars": [
      {
        "name": "Whitelock's Ale House",
        "note": "dates back to 1715, tucked down a city-centre yard"
      },
      {
        "name": "The Victoria & Commercial",
        "note": "restored Grade II-listed Victorian interior"
      },
      {
        "name": "Kirkstall Bridge Inn",
        "note": "riverside, pouring Kirkstall's own beers"
      }
    ],
    "eat": "Graze Kirkgate Market, or steak and ale pie at the Lamb & Flag by the Minster.",
    "dontMiss": "A night match under the lights at Elland Road.",
    "football": "Leeds United at Elland Road. Headingley for the Rhinos and Yorkshire cricket.",
    "gettingThere": "Leeds station is a major hub: direct trains from London, Manchester, York and beyond.",
    "tip": "Get to Whitelock's early on matchday - it's tiny and fills fast."
  },
  {
    "city": "Wakefield",
    "region": "West Yorkshire",
    "country": "United Kingdom",
    "colour": "red",
    "pint": "~£5",
    "localBeer": "Ossett Brewery",
    "bestFor": "Real ale crawl",
    "spoons": {
      "name": "The Six Chimneys",
      "note": "Kirkgate, open from 8am, award-winning loos"
    },
    "bars": [
      {
        "name": "Harry's Bar",
        "note": "log fires, timber beams, up to eight casks"
      },
      {
        "name": "The Black Rock",
        "note": "Grade II-listed, near the cathedral"
      },
      {
        "name": "Luis Bar",
        "note": "Ossett's bar in the old Fernandes maltings"
      }
    ],
    "eat": "Anything with Yorkshire forced rhubarb - Wakefield is the heart of the Rhubarb Triangle.",
    "dontMiss": "The Hepworth Wakefield gallery, then a pint at the Exchange Tap.",
    "football": "Wakefield Trinity rugby league at Belle Vue (DIY Kitchens Stadium).",
    "gettingThere": "Wakefield Westgate is on the East Coast Main Line - quick from Leeds or London.",
    "tip": "Do Westgate as a crawl - Harry's, Black Rock and the Hop are all within a few minutes."
  },
  {
    "city": "Batley",
    "region": "West Yorkshire",
    "country": "United Kingdom",
    "colour": "green",
    "pint": "~£4.50",
    "localBeer": "Yorkshire cask guests",
    "bestFor": "No-frills locals",
    "spoons": {
      "name": "The Union Rooms",
      "note": "in the grand old Union Bank, local guest ales"
    },
    "bars": [
      {
        "name": "Irish Democratic League Club (Batley Nash)",
        "note": "friendly club, interesting guest ales, Leeds on the telly"
      }
    ],
    "eat": "Batley is home to Fox's Biscuits - grab some for the train.",
    "dontMiss": "Bagshaw Museum in Wilton Park, then up the road to Oakwell Hall.",
    "football": "Batley Bulldogs rugby league at Mount Pleasant - famous for its sloping pitch.",
    "gettingThere": "Batley station is on the Huddersfield line between Leeds and Manchester.",
    "tip": "The Union Rooms opens at 8am - breakfast and a pint in an old bank."
  },
  {
    "city": "Dewsbury",
    "region": "West Yorkshire",
    "country": "United Kingdom",
    "colour": "purple",
    "pint": "~£4.50",
    "localBeer": "Timothy Taylor Landlord",
    "bestFor": "Station pub & canal pints",
    "bars": [
      {
        "name": "West Riding Refreshment Rooms",
        "note": "on the station platform, ten handpumps"
      },
      {
        "name": "Leggers Inn",
        "note": "hayloft bar above old stables by the canal basin"
      }
    ],
    "eat": "Wander the market (Wednesdays and Saturdays) for a cheap lunch.",
    "dontMiss": "Dewsbury Minster - its bell 'Black Tom' tolls the Devil's Knell every Christmas Eve.",
    "football": "Dewsbury Rams rugby league at Crown Flatt (FLAIR Stadium).",
    "gettingThere": "TransPennine trains stop here - a good start to the Transpennine Real Ale Trail.",
    "tip": "Start the Transpennine Ale Trail at the West Riding - it's on the platform."
  },
  {
    "city": "Huddersfield",
    "region": "West Yorkshire",
    "country": "United Kingdom",
    "colour": "teal",
    "pint": "~£4.50",
    "localBeer": "Magic Rock",
    "bestFor": "Real ale trail",
    "spoons": {
      "name": "The Lord Wilson",
      "note": "King Street, up to five guest ales"
    },
    "bars": [
      {
        "name": "King's Head",
        "note": "inside the Grade I-listed station, two wood burners"
      },
      {
        "name": "Magic Rock Tap",
        "note": "brewery taproom, food trucks at weekends"
      },
      {
        "name": "The Sportsman",
        "note": "1930s pub, a CAMRA favourite"
      }
    ],
    "eat": "Pie and peas at the Slubbers Arms.",
    "dontMiss": "The station's grand frontage in St George's Square, then out along the ale trail.",
    "football": "Huddersfield Town at the Accu Stadium (the old John Smith's).",
    "gettingThere": "On the TransPennine line - about 20 minutes from Leeds.",
    "tip": "Grab a pint at the King's Head before your train - it's in the station."
  },
  {
    "city": "Sheffield",
    "region": "South Yorkshire",
    "country": "United Kingdom",
    "colour": "orange",
    "pint": "~£4.50",
    "localBeer": "Abbeydale Moonshine",
    "bestFor": "Kelham Island pub crawl",
    "spoons": {
      "name": "The Bankers Draft",
      "note": "1904 bank by Castle Square, one of Sheffield's first Spoons"
    },
    "bars": [
      {
        "name": "Sheffield Tap",
        "note": "right in the station, with its own Tapped brewery"
      },
      {
        "name": "Kelham Island Tavern",
        "note": "rotating real ales and a leafy beer garden"
      },
      {
        "name": "The Fat Cat",
        "note": "a Kelham Island classic"
      }
    ],
    "eat": "Anything with a splash of Henderson's Relish - it's the law round here.",
    "dontMiss": "A crawl round Kelham Island's old industrial streets.",
    "football": "Sheffield United at Bramall Lane, Sheffield Wednesday at Hillsborough.",
    "gettingThere": "Sheffield station on the Midland Main Line; about 40 minutes from Leeds.",
    "tip": "Walk Kelham Island in a loop - Fat Cat, Kelham Island Tavern, then the Riverside."
  },
  {
    "city": "Morley",
    "region": "West Yorkshire",
    "country": "United Kingdom",
    "colour": "blue",
    "pint": "~£4.50",
    "localBeer": "West Yorkshire guests",
    "bestFor": "Queen Street bar hop",
    "spoons": {
      "name": "The Picture House",
      "note": "bigger than it looks, balcony and West Yorkshire guests"
    },
    "bars": [
      {
        "name": "Dyeworks",
        "note": "micropub and bottle shop with local keg and cans"
      },
      {
        "name": "Nomad",
        "note": "small bar, good keg range and platters"
      }
    ],
    "eat": "Platters of dips and charcuterie at Nomad.",
    "dontMiss": "Morley Town Hall - Grade I listed, with a 160ft domed clock tower.",
    "football": "A short hop to Elland Road for Leeds United.",
    "gettingThere": "Morley station is on the Huddersfield line; buses run along Queen Street.",
    "tip": "Nomad and Dyeworks are both closed early in the week - go Thursday to Sunday."
  },
  {
    "city": "Harrogate",
    "region": "North Yorkshire",
    "country": "United Kingdom",
    "colour": "green",
    "pint": "~£5",
    "localBeer": "Cold Bath Brewing Co",
    "bestFor": "Spa town pints",
    "spoons": {
      "name": "The Winter Gardens",
      "note": "inside the Victorian Royal Baths, with a grand staircase"
    },
    "bars": [
      {
        "name": "Cold Bath Brewing Co",
        "note": "taproom with ever-changing small batches"
      },
      {
        "name": "The Little Ale House",
        "note": "cosy micropub, good ale range"
      },
      {
        "name": "Harrogate Tap",
        "note": "station pub that tops the 'best station pub' lists"
      }
    ],
    "eat": "Tea and a Fat Rascal at Bettys, or small plates at the Fat Badger.",
    "dontMiss": "A stroll through Valley Gardens and across the Stray.",
    "football": "Harrogate Town at Wetherby Road (Marcy Fitness Stadium).",
    "gettingThere": "Harrogate Line trains from Leeds and York.",
    "tip": "The Winter Gardens staircase is worth the visit alone."
  },
  {
    "city": "Knaresborough",
    "region": "North Yorkshire",
    "country": "United Kingdom",
    "colour": "red",
    "pint": "~£5",
    "localBeer": "Blind Jack's beer board",
    "bestFor": "Riverside pubs",
    "spoons": {
      "name": "The Crown Inn",
      "note": "High Street, twelve handpumps"
    },
    "bars": [
      {
        "name": "Blind Jack's",
        "note": "named UK's Best Beer Pub at the 2025 Great British Pub Awards"
      },
      {
        "name": "The World's End",
        "note": "good beer and home cooking by the River Nidd"
      }
    ],
    "eat": "Home-cooked pub food at the World's End.",
    "dontMiss": "The view of the railway viaduct over the Nidd from the castle, then Mother Shipton's Cave.",
    "football": "Knaresborough Town at Manse Lane.",
    "gettingThere": "On the Harrogate Line between Leeds and York.",
    "tip": "Have one by the river at the World's End, then walk up to the castle for the viaduct view."
  },
  {
    "city": "Boroughbridge",
    "region": "North Yorkshire",
    "country": "United Kingdom",
    "colour": "purple",
    "pint": "~£5",
    "localBeer": "Rudgate Jorvik Blonde",
    "bestFor": "Historic interiors",
    "bars": [
      {
        "name": "Tap on the Tutt",
        "note": "1930s interior CAMRA rates of national importance"
      },
      {
        "name": "The Crown Hotel",
        "note": "17th-century coaching inn on the old Great North Road"
      }
    ],
    "eat": "Lunch or dinner at the Crown Hotel.",
    "dontMiss": "The Devil's Arrows - Bronze Age standing stones, the tallest 22ft.",
    "gettingThere": "Just off the A1(M); no station, so it's a drive or bus from Harrogate or York.",
    "tip": "Ask for a look round Tap on the Tutt's 1930s rooms - they're barely changed."
  },
  {
    "city": "Thirsk",
    "region": "North Yorkshire",
    "country": "United Kingdom",
    "colour": "teal",
    "pint": "~£5",
    "localBeer": "Black Sheep & Hambleton",
    "bestFor": "Market town pubs",
    "spoons": {
      "name": "The Three Tuns",
      "note": "1740 coaching inn where James Herriot drank"
    },
    "bars": [
      {
        "name": "Little 3",
        "note": "low-beamed warren of nooks, history back to 1214"
      },
      {
        "name": "Golden Fleece Hotel",
        "note": "grand old hotel on the market place, Black Sheep on"
      }
    ],
    "eat": "Market day (Mondays and Saturdays), then the Golden Fleece restaurant.",
    "dontMiss": "The World of James Herriot, in the vet's old surgery. Racecourse in summer.",
    "football": "Thirsk Falcons in the Teesside League.",
    "gettingThere": "Thirsk station is on the East Coast Main Line, about 1.5 miles out of town.",
    "tip": "Go on a Monday or Saturday for the market, then the Three Tuns."
  },
  {
    "city": "Northallerton",
    "region": "North Yorkshire",
    "country": "United Kingdom",
    "colour": "orange",
    "pint": "~£5",
    "localBeer": "Black Sheep Best Bitter",
    "bestFor": "High Street pubs",
    "spoons": {
      "name": "The Buck Inn",
      "note": "north end of the High Street, six changing casks"
    },
    "bars": [
      {
        "name": "Harewood Arms",
        "note": "narrow single-bar pub with changing local guests"
      },
      {
        "name": "Golden Lion Hotel",
        "note": "listed coaching inn with a golden lion over the porch"
      },
      {
        "name": "The Fleece Inn",
        "note": "15th-century building with oak-beamed ceilings"
      }
    ],
    "eat": "Bettys on the High Street, or a meal at the Golden Lion.",
    "dontMiss": "Market day on the High Street (Wednesdays and Saturdays).",
    "football": "Northallerton Town at the Calvert Stadium.",
    "gettingThere": "Northallerton is on the East Coast Main Line.",
    "tip": "Wednesday and Saturday are market days - the High Street pubs are buzzing."
  },
  {
    "city": "York",
    "region": "North Yorkshire",
    "country": "United Kingdom",
    "colour": "red",
    "pint": "~£5",
    "localBeer": "Brew York",
    "bestFor": "Medieval pub crawl",
    "spoons": {
      "name": "The Punch Bowl",
      "note": "on Blossom Street, near Micklegate Bar"
    },
    "bars": [
      {
        "name": "York Tap",
        "note": "in the station's old tearooms"
      },
      {
        "name": "House of the Trembling Madness",
        "note": "Stonegate, beers over a medieval hall"
      },
      {
        "name": "Ye Olde Starre Inne",
        "note": "Stonegate, one of York's oldest licensed pubs"
      }
    ],
    "eat": "Wander the Shambles and Shambles Market for lunch.",
    "dontMiss": "York Minster, then a lap of the city walls.",
    "football": "York City at the LNER Community Stadium.",
    "gettingThere": "On the East Coast Main Line - about 25 minutes from Leeds.",
    "tip": "Walk the walls first - then you've earned the York Tap."
  },
  {
    "city": "Wetherby",
    "region": "West Yorkshire",
    "country": "United Kingdom",
    "colour": "green",
    "pint": "~£5",
    "localBeer": "Wetherby Brew Co",
    "bestFor": "Market-town pints",
    "spoons": {
      "name": "The Angel Inn",
      "note": "High Street, opened Christmas 2025 in a listed building"
    },
    "bars": [
      {
        "name": "Swan & Talbot",
        "note": "quaint old coaching inn with rooms"
      },
      {
        "name": "Wetherby Brew Co",
        "note": "brewery taproom, street food and live music"
      }
    ],
    "eat": "Pub grub at the Swan & Talbot.",
    "dontMiss": "A walk along the River Wharfe from the old bridge.",
    "football": "Leeds United are about half an hour away.",
    "gettingThere": "Buses from Leeds, Harrogate and York; just off the A1(M).",
    "tip": "Wetherby Brew Co's taproom is only open Thursday to Sunday."
  },
  {
    "city": "Yeadon",
    "region": "West Yorkshire",
    "country": "United Kingdom",
    "colour": "blue",
    "pint": "~£4.50",
    "localBeer": "West Yorkshire cask",
    "bestFor": "Pre-flight pints",
    "spoons": {
      "name": "The Clothier's Arms",
      "note": "Yeadon's Spoons, a short hop from the airport"
    },
    "bars": [
      {
        "name": "Nest",
        "note": "neighbourhood bar in the old NatWest bank"
      },
      {
        "name": "Beer House",
        "note": "airside at Leeds Bradford Airport, by gates 7-8"
      }
    ],
    "eat": "Breakfast in town before heading up to the airport.",
    "dontMiss": "Yeadon Tarn - watch the planes come in over the water.",
    "football": "Guiseley AFC at Nethermoor Park, next door.",
    "gettingThere": "Right by Leeds Bradford Airport; buses from Leeds and Bradford.",
    "tip": "The airport Beer House opens at 5am for early flights."
  },
  {
    "city": "Bingley",
    "region": "West Yorkshire",
    "country": "United Kingdom",
    "colour": "orange",
    "pint": "~£4.50",
    "localBeer": "Timothy Taylor",
    "bestFor": "Canal-side pints",
    "spoons": {
      "name": "The Myrtle Grove",
      "note": "Bingley's Spoons on Main Street"
    },
    "bars": [
      {
        "name": "Brown Cow",
        "note": "riverside by a 13th-century bridge, Timothy Taylor's"
      },
      {
        "name": "Old White Horse Inn",
        "note": "Grade II-listed coaching inn"
      }
    ],
    "eat": "Meals at the Brown Cow.",
    "dontMiss": "Bingley Five Rise Locks on the Leeds-Liverpool Canal.",
    "football": "Bradford City at Valley Parade, 15 minutes away.",
    "gettingThere": "Airedale line trains from Leeds and Bradford.",
    "tip": "Walk the Five Rise Locks, then the Brown Cow by the old bridge."
  },
  {
    "city": "Halifax",
    "region": "West Yorkshire",
    "country": "United Kingdom",
    "colour": "purple",
    "pint": "~£4.50",
    "localBeer": "Calderdale cask",
    "bestFor": "Piece Hall pints",
    "spoons": {
      "name": "The Barum Top Inn",
      "note": "Rawson Street, in the town centre"
    },
    "bars": [
      {
        "name": "Hop Yard",
        "note": "inside the Piece Hall, cask and keg"
      },
      {
        "name": "Dukes",
        "note": "micropub in a Victorian arcade"
      },
      {
        "name": "Westgate",
        "note": "refurbished town-centre local, good for sport"
      }
    ],
    "eat": "Grab something in the Piece Hall's courtyard.",
    "dontMiss": "The Piece Hall - a restored 18th-century cloth hall.",
    "football": "FC Halifax Town at The Shay.",
    "gettingThere": "Trains from Leeds in about 35 minutes.",
    "tip": "Go when there's something on in the Piece Hall - the Hop Yard is right inside."
  },
  {
    "city": "Ripon",
    "region": "North Yorkshire",
    "country": "United Kingdom",
    "colour": "teal",
    "pint": "~£5",
    "localBeer": "Theakston & Black Sheep",
    "bestFor": "Cathedral city pubs",
    "spoons": {
      "name": "The Unicorn Hotel",
      "note": "on the Market Place"
    },
    "bars": [
      {
        "name": "One Eyed Rat",
        "note": "narrow old local with a big beer garden"
      },
      {
        "name": "Royal Oak",
        "note": "Timothy Taylor's pub with rooms"
      }
    ],
    "eat": "Market day on Thursday, then pub lunch.",
    "dontMiss": "The Hornblower sets the watch in the Market Square at 9pm every night.",
    "football": "Ripon Racecourse in summer; Harrogate Town are 20 minutes away.",
    "gettingThere": "No station - buses from Harrogate and Leeds.",
    "tip": "Be in the Market Square at 9pm for the Hornblower, then straight to the pub."
  },
  {
    "city": "Masham",
    "region": "North Yorkshire",
    "country": "United Kingdom",
    "colour": "green",
    "pint": "~£5",
    "localBeer": "Theakston & Black Sheep",
    "bestFor": "Two breweries, one town",
    "bars": [
      {
        "name": "Black Sheep Brewery",
        "note": "tours, bistro and the Baa...r"
      },
      {
        "name": "Black Bull in Paradise",
        "note": "Theakston's brewery tap"
      },
      {
        "name": "The White Bear",
        "note": "gastropub next to Black Sheep"
      }
    ],
    "eat": "Lunch at the Black Sheep bistro or the White Bear.",
    "dontMiss": "Tours of both breweries - Theakston Old Peculier at source.",
    "gettingThere": "No station - drive or bus from Ripon.",
    "tip": "Book both brewery tours on the same day - they're five minutes apart."
  },
  {
    "city": "Pateley Bridge",
    "region": "North Yorkshire",
    "country": "United Kingdom",
    "colour": "red",
    "pint": "~£5",
    "localBeer": "Dales cask ales",
    "bestFor": "Nidderdale walks",
    "bars": [
      {
        "name": "Royal Oak",
        "note": "open fire and four local ales"
      },
      {
        "name": "Bridge Inn",
        "note": "old stone pub a mile up the dale"
      }
    ],
    "eat": "A brew and a cake on the steep High Street.",
    "dontMiss": "Brimham Rocks, and the oldest sweet shop in England on the High Street.",
    "gettingThere": "Buses from Harrogate; it's in the heart of Nidderdale.",
    "tip": "Park at the bottom and walk the High Street - it's steep."
  },
  {
    "city": "Malton",
    "region": "North Yorkshire",
    "country": "United Kingdom",
    "colour": "orange",
    "pint": "~£5",
    "localBeer": "Brass Castle",
    "bestFor": "Food town & racing stables",
    "bars": [
      {
        "name": "Brass Castle Brewery Tap House",
        "note": "award-winning beer brewed next door"
      },
      {
        "name": "Royal Oak",
        "note": "Market Place, big dog-friendly beer garden"
      },
      {
        "name": "Wentworth Arms",
        "note": "coaching inn in Old Malton"
      }
    ],
    "eat": "Malton calls itself Yorkshire's food capital - try the monthly food market.",
    "dontMiss": "Castle Howard, a few miles down the road.",
    "gettingThere": "Trains from York in about 25 minutes.",
    "tip": "Time it for the monthly food market, then Brass Castle's tap."
  },
  {
    "city": "Settle",
    "region": "North Yorkshire",
    "country": "United Kingdom",
    "colour": "blue",
    "pint": "~£5",
    "localBeer": "Settle Brewery",
    "bestFor": "Dales walks & pubs",
    "bars": [
      {
        "name": "The Talbot",
        "note": "claims 1642, five casks, CAMRA favourite"
      },
      {
        "name": "The Golden Lion",
        "note": "old coaching inn on the market place"
      }
    ],
    "eat": "Pub food at the Talbot.",
    "dontMiss": "Malham Cove and Malham Tarn, a short drive away.",
    "gettingThere": "On the Settle-Carlisle line - one of Britain's great railway journeys.",
    "tip": "Ride the Settle-Carlisle line out and back - the Talbot's by the station."
  },
  {
    "city": "Bentham",
    "region": "North Yorkshire",
    "country": "United Kingdom",
    "colour": "purple",
    "pint": "~£4.50",
    "localBeer": "Dales cask ales",
    "bestFor": "Quiet country pints",
    "bars": [
      {
        "name": "The Coach House",
        "note": "17th-century coaching inn with a log fire"
      }
    ],
    "eat": "Pub food at the Coach House.",
    "dontMiss": "The Great Stone of Fourstones on the heritage trail.",
    "gettingThere": "Bentham station is on the Leeds-Morecambe line.",
    "tip": "Ring the Coach House ahead for food - it's the main pub left in town."
  },
  {
    "city": "Whitby",
    "region": "North Yorkshire",
    "country": "United Kingdom",
    "colour": "teal",
    "pint": "~£5",
    "localBeer": "Whitby Brewery",
    "bestFor": "Seaside pints & fish and chips",
    "spoons": {
      "name": "The Angel Hotel",
      "note": "old coaching inn by the harbour"
    },
    "bars": [
      {
        "name": "The Duke of York",
        "note": "at the foot of the 199 steps, harbour views"
      },
      {
        "name": "Whitby Brewery",
        "note": "brewery tap up by the abbey"
      }
    ],
    "eat": "Fish and chips by the harbour.",
    "dontMiss": "Climb the 199 steps to Whitby Abbey.",
    "football": "Whitby Town at the Turnbull Ground.",
    "gettingThere": "Esk Valley line from Middlesbrough, or the steam railway from Pickering.",
    "tip": "Get fish and chips at the bottom of the 199 steps, after you've climbed them."
  },
  {
    "city": "Scarborough",
    "region": "North Yorkshire",
    "country": "United Kingdom",
    "colour": "blue",
    "pint": "~£4.50",
    "localBeer": "North Riding Brewery",
    "bestFor": "Seaside pubs",
    "spoons": {
      "name": "The Lord Rosebery",
      "note": "in the old Liberal Club"
    },
    "bars": [
      {
        "name": "North Riding Hotel",
        "note": "pub with its own brewery"
      }
    ],
    "eat": "Fish and chips on the South Bay seafront.",
    "dontMiss": "Scarborough Castle, then the North Bay Railway.",
    "football": "Scarborough Athletic.",
    "gettingThere": "Trains from York in about 50 minutes.",
    "tip": "South Bay for chips, North Bay for a quieter pint."
  },
  {
    "city": "Redcar",
    "region": "North Yorkshire",
    "country": "United Kingdom",
    "colour": "red",
    "pint": "~£4.50",
    "localBeer": "Teesside cask",
    "bestFor": "Seafront pints",
    "spoons": {
      "name": "The Plimsoll Line",
      "note": "High Street, huge beer garden"
    },
    "eat": "Chips on the seafront.",
    "dontMiss": "Redcar Beacon and the long sandy beach.",
    "football": "Middlesbrough at the Riverside, 20 minutes away.",
    "gettingThere": "Trains from Middlesbrough and Darlington.",
    "tip": "The Plimsoll Line's beer garden runs right through to Lord Street - grab a table outside."
  },
  {
    "city": "Saltburn-by-the-Sea",
    "region": "North Yorkshire",
    "country": "United Kingdom",
    "colour": "green",
    "pint": "~£5",
    "localBeer": "Teesside cask",
    "bestFor": "Victorian seaside pubs",
    "bars": [
      {
        "name": "The Ship Inn",
        "note": "smugglers' pub on the beach, over 500 years old"
      },
      {
        "name": "The Victoria",
        "note": "near the station, wide range of regional ales"
      },
      {
        "name": "The Guns Bar",
        "note": "craft ale and gin on Milton Street"
      }
    ],
    "eat": "Homemade pies at the Guns on a Saturday.",
    "dontMiss": "The cliff lift and the pier.",
    "football": "Middlesbrough at the Riverside, half an hour away.",
    "gettingThere": "End of the line from Darlington and Middlesbrough.",
    "tip": "Take the cliff lift down to the Ship Inn - and back up after."
  },
  {
    "city": "Keswick",
    "region": "Cumbria",
    "country": "United Kingdom",
    "colour": "teal",
    "pint": "~£5",
    "localBeer": "Keswick Brewing Co",
    "bestFor": "Lake District pubs",
    "spoons": {
      "name": "Chief Justice of the Common Pleas",
      "note": "Keswick's Spoons"
    },
    "bars": [
      {
        "name": "Dog & Gun",
        "note": "real ales and famous Hungarian goulash"
      },
      {
        "name": "The George",
        "note": "the town's oldest drinking house"
      },
      {
        "name": "Fox Tap",
        "note": "Keswick Brewing Co's bar on Brewery Lane"
      }
    ],
    "eat": "Goulash at the Dog & Gun.",
    "dontMiss": "A boat on Derwentwater, or the climb up Catbells.",
    "gettingThere": "Train to Penrith, then the bus into Keswick.",
    "tip": "Book ahead for the Dog & Gun's goulash on a weekend."
  },
  {
    "city": "Alnwick",
    "region": "Northumberland",
    "country": "United Kingdom",
    "colour": "purple",
    "pint": "~£5",
    "localBeer": "Northumberland cask",
    "bestFor": "Castle town & coast",
    "bars": [
      {
        "name": "The Tanners Arms",
        "note": "CAMRA's best pub in north Northumberland"
      },
      {
        "name": "The Dirty Bottles",
        "note": "1600s inn with ales and cocktails"
      },
      {
        "name": "The Hog's Head Inn",
        "note": "named after the Harry Potter tavern"
      }
    ],
    "eat": "Browse Barter Books in the old station, then a pub lunch.",
    "dontMiss": "Alnwick Castle, then out to Craster and Beadnell on the coast.",
    "gettingThere": "Alnmouth station on the East Coast Main Line, then a short bus.",
    "tip": "Barter Books first, then the Tanners Arms."
  },
  {
    "city": "Bakewell",
    "region": "Derbyshire",
    "country": "United Kingdom",
    "colour": "orange",
    "pint": "~£5",
    "localBeer": "Thornbridge",
    "bestFor": "Peak District pints",
    "bars": [
      {
        "name": "Thornbridge Brewery Tap Room",
        "note": "at the brewery, cask, keg and pizzas"
      }
    ],
    "eat": "A proper Bakewell pudding - not a tart.",
    "dontMiss": "Chatsworth House, and the plague village of Eyam nearby.",
    "gettingThere": "Buses from Sheffield, Matlock and Buxton.",
    "tip": "Bakewell pudding, not tart - the locals will correct you."
  },
  {
    "city": "Manchester",
    "region": "Greater Manchester",
    "country": "United Kingdom",
    "colour": "red",
    "pint": "~£5.50",
    "localBeer": "Marble",
    "bestFor": "Football & Northern Quarter bars",
    "spoons": {
      "name": "The Moon Under Water",
      "note": "Deansgate, one of the biggest Spoons"
    },
    "bars": [
      {
        "name": "Peveril of the Peak",
        "note": "tiled Victorian pub"
      },
      {
        "name": "Marble Arch",
        "note": "Marble Brewery's original pub"
      },
      {
        "name": "Port Street Beer House",
        "note": "Northern Quarter craft bar"
      }
    ],
    "eat": "Curry Mile, or anything in the Northern Quarter.",
    "dontMiss": "A stadium tour - plus Salford Quays and the Lowry.",
    "football": "Man United at Old Trafford, Man City at the Etihad.",
    "gettingThere": "About an hour from Leeds by train; big airport too.",
    "tip": "Peveril of the Peak before anywhere else - it's an island of a pub."
  },
  {
    "city": "Liverpool",
    "region": "Merseyside",
    "country": "United Kingdom",
    "colour": "blue",
    "pint": "~£5",
    "localBeer": "Neptune Brewery",
    "bestFor": "Grand old pubs & docks",
    "spoons": {
      "name": "The North Western",
      "note": "in the old Lime Street station hotel"
    },
    "bars": [
      {
        "name": "Philharmonic Dining Rooms",
        "note": "ornate Victorian gin palace"
      },
      {
        "name": "Baltic Fleet",
        "note": "dockside pub"
      },
      {
        "name": "Ye Cracke",
        "note": "back-street pub where John Lennon drank"
      }
    ],
    "eat": "Scouse, obviously.",
    "dontMiss": "The Albert Dock, then the Cavern Quarter.",
    "football": "Liverpool at Anfield; Everton at the Hill Dickinson Stadium.",
    "gettingThere": "About 1.5 hours from Leeds by train.",
    "tip": "Visit the Philharmonic's gents - honestly, it's listed."
  },
  {
    "city": "Leicester",
    "region": "Leicestershire",
    "country": "United Kingdom",
    "colour": "teal",
    "pint": "~£4.50",
    "localBeer": "Everards",
    "bestFor": "Motorway pit stop",
    "spoons": {
      "name": "The Corn Exchange",
      "note": "on the Market Place"
    },
    "bars": [
      {
        "name": "The Ale Wagon",
        "note": "traditional real ale pub near the station"
      }
    ],
    "eat": "Curry on the Golden Mile.",
    "dontMiss": "King Richard III Visitor Centre.",
    "football": "Leicester City at the King Power Stadium.",
    "gettingThere": "Just off the M1; trains on the Midland Main Line.",
    "tip": "The Corn Exchange is right on the market - handy for a quick stop."
  },
  {
    "city": "Daventry",
    "region": "Northamptonshire",
    "country": "United Kingdom",
    "colour": "green",
    "pint": "~£4.50",
    "localBeer": "Midlands cask",
    "bestFor": "M1 pit stop",
    "spoons": {
      "name": "The Saracens Head",
      "note": "Grade II*-listed old inn on Brook Street"
    },
    "eat": "Breakfast at the Saracens Head.",
    "dontMiss": "A walk up Borough Hill.",
    "gettingThere": "Off the M1 near Watford Gap.",
    "tip": "The Saracens Head is a proper old inn - worth the M1 detour."
  },
  {
    "city": "Westminster",
    "region": "London",
    "country": "United Kingdom",
    "colour": "red",
    "pint": "~£6.50",
    "localBeer": "Fuller's London Pride",
    "bestFor": "Sights & West End pubs",
    "spoons": {
      "name": "Wetherspoons, Victoria Station",
      "note": "on the station concourse, with terraces"
    },
    "bars": [
      {
        "name": "Lamb & Flag",
        "note": "Covent Garden, one of the West End's oldest pubs"
      },
      {
        "name": "The Harp",
        "note": "Covent Garden, cask-ale favourite"
      }
    ],
    "eat": "Covent Garden or Chinatown.",
    "dontMiss": "Trafalgar Square, then Big Ben from Westminster Bridge.",
    "gettingThere": "About 2h15 from Leeds to King's Cross, then the Tube.",
    "tip": "Victoria station's Spoons has terraces - good for watching the world go by."
  },
  {
    "city": "Southwark",
    "region": "London",
    "country": "United Kingdom",
    "colour": "orange",
    "pint": "~£6.50",
    "localBeer": "Southwark brewery taps",
    "bestFor": "Borough Market & riverside pubs",
    "spoons": {
      "name": "The Pommelers Rest",
      "note": "Tower Bridge Road"
    },
    "bars": [
      {
        "name": "The George Inn",
        "note": "London's last galleried coaching inn"
      },
      {
        "name": "The Market Porter",
        "note": "early-opening pub by Borough Market"
      },
      {
        "name": "The Anchor Bankside",
        "note": "riverside on the South Bank"
      }
    ],
    "eat": "Borough Market.",
    "dontMiss": "Walk across Tower Bridge, then along to Shakespeare's Globe.",
    "football": "Millwall at The Den.",
    "gettingThere": "London Bridge station, or the Jubilee line.",
    "tip": "The Market Porter opens early on market days."
  },
  {
    "city": "Tower Hamlets",
    "region": "London",
    "country": "United Kingdom",
    "colour": "purple",
    "pint": "~£6.50",
    "localBeer": "East London craft",
    "bestFor": "Old riverside pubs & Docklands",
    "spoons": {
      "name": "The Ledger Building",
      "note": "West India Quay, terrace over the moored boats"
    },
    "bars": [
      {
        "name": "Prospect of Whitby",
        "note": "Wapping, claims to be the oldest riverside pub"
      },
      {
        "name": "The Grapes",
        "note": "Limehouse, tiny old pub on the Thames"
      }
    ],
    "eat": "Curry on Brick Lane.",
    "dontMiss": "The Tower of London, then the DLR out to Canary Wharf.",
    "gettingThere": "Tower Hill or Canary Wharf on the Tube and DLR.",
    "tip": "Prospect of Whitby has a terrace right on the Thames."
  },
  {
    "city": "Newham",
    "region": "London",
    "country": "United Kingdom",
    "colour": "teal",
    "pint": "~£6",
    "localBeer": "Tap East",
    "bestFor": "Matchdays at the Olympic Park",
    "spoons": {
      "name": "Goldengrove",
      "note": "The Grove, Stratford"
    },
    "bars": [
      {
        "name": "Tap East",
        "note": "brewpub by Westfield, with a Bobby Moore blonde"
      },
      {
        "name": "The Cart & Horses",
        "note": "Maryland, the birthplace of Iron Maiden"
      }
    ],
    "eat": "Westfield Stratford City.",
    "dontMiss": "Queen Elizabeth Olympic Park and the ArcelorMittal Orbit.",
    "football": "West Ham at the London Stadium.",
    "gettingThere": "Stratford station - Central line, Elizabeth line, DLR and Jubilee.",
    "tip": "Tap East is inside Westfield - easy pre-match on West Ham days."
  },
  {
    "city": "Brent",
    "region": "London",
    "country": "United Kingdom",
    "colour": "blue",
    "pint": "~£6",
    "localBeer": "Big-brand lagers",
    "bestFor": "Wembley days",
    "spoons": {
      "name": "J.J. Moon's",
      "note": "Wembley High Road"
    },
    "bars": [
      {
        "name": "Green Man",
        "note": "the best-known Wembley pub, fills up fast"
      },
      {
        "name": "The Torch",
        "note": "big beer garden east of the stadium"
      },
      {
        "name": "The Robin",
        "note": "big beer range, cheap food, 15 minutes' walk"
      }
    ],
    "eat": "Curry on Ealing Road.",
    "dontMiss": "Walking up Olympic Way with the arch in front of you.",
    "football": "Wembley Stadium - England, cup finals and play-offs.",
    "gettingThere": "Wembley Park on the Jubilee/Metropolitan, or Wembley Stadium from Marylebone.",
    "tip": "The Green Man goes one-in-one-out on matchdays - get there early."
  },
  {
    "city": "Greenwich",
    "region": "London",
    "country": "United Kingdom",
    "colour": "green",
    "pint": "~£6",
    "localBeer": "Meantime",
    "bestFor": "Riverside pints & maritime history",
    "spoons": {
      "name": "The Gate Clock",
      "note": "Creek Road, near the Cutty Sark"
    },
    "bars": [
      {
        "name": "Trafalgar Tavern",
        "note": "Regency riverside pub"
      },
      {
        "name": "Cutty Sark Tavern",
        "note": "old pub on the river"
      }
    ],
    "eat": "Greenwich Market.",
    "dontMiss": "Stand on the Prime Meridian at the Royal Observatory.",
    "football": "Charlton Athletic at The Valley.",
    "gettingThere": "DLR to Cutty Sark, or the Uber Boat from central London.",
    "tip": "Get the Uber Boat in from central London - it's the best way to arrive."
  },
  {
    "city": "Newport",
    "region": "Isle of Wight",
    "country": "United Kingdom",
    "colour": "blue",
    "pint": "~£5",
    "localBeer": "Goddards",
    "bestFor": "Island pints",
    "spoons": {
      "name": "The Man in the Moon",
      "note": "in a former church"
    },
    "eat": "Island seafood - crab if it's on.",
    "dontMiss": "Carisbrooke Castle, just outside town.",
    "gettingThere": "Ferry from Portsmouth or Southampton, then the bus.",
    "tip": "The Man in the Moon is in an old church - look up."
  },
  {
    "city": "Llanrwst",
    "region": "Wales",
    "country": "United Kingdom",
    "colour": "red",
    "pint": "~£4.50",
    "localBeer": "Welsh cask",
    "bestFor": "Snowdonia pints",
    "bars": [
      {
        "name": "Pen-y-Bryn",
        "note": "17th-century coaching inn on Ancaster Square"
      }
    ],
    "eat": "Tea and Welsh cakes at Tu Hwnt i'r Bont by the old bridge.",
    "dontMiss": "Swallow Falls and Betws-y-Coed, just up the valley.",
    "gettingThere": "Conwy Valley line from Llandudno Junction.",
    "tip": "Tea at Tu Hwnt i'r Bont by the old bridge before the Pen-y-Bryn."
  },
  {
    "city": "Dublin",
    "region": "Leinster",
    "country": "Ireland",
    "colour": "green",
    "pint": "~€7",
    "localBeer": "Guinness",
    "bestFor": "The perfect pint",
    "spoons": {
      "name": "Keavan's Port",
      "note": "Camden Street, pub and hotel"
    },
    "bars": [
      {
        "name": "The Brazen Head",
        "note": "claims to be Ireland's oldest pub"
      },
      {
        "name": "The Long Hall",
        "note": "Victorian bar on South Great George's Street"
      },
      {
        "name": "Mulligan's",
        "note": "legendary Guinness on Poolbeg Street"
      }
    ],
    "eat": "Stew and soda bread.",
    "dontMiss": "The Guinness Storehouse and its Gravity Bar.",
    "football": "Shamrock Rovers or Bohemians; Ireland at the Aviva.",
    "gettingThere": "Short flight from Leeds Bradford or Manchester.",
    "tip": "Skip Temple Bar's prices - Mulligan's and the Long Hall pour a better pint."
  },
  {
    "city": "Málaga",
    "region": "Andalusia",
    "country": "Spain",
    "colour": "orange",
    "pint": "~€3",
    "localBeer": "Victoria",
    "bestFor": "Tapas & sweet wine",
    "bars": [
      {
        "name": "Antigua Casa de Guardia",
        "note": "pouring Málaga wine from the barrel since 1840"
      },
      {
        "name": "El Pimpi",
        "note": "huge old bodega by the Roman theatre"
      },
      {
        "name": "La Tranca",
        "note": "tiny, loud, brilliant tapas bar"
      }
    ],
    "eat": "Espetos - sardines grilled on the beach.",
    "dontMiss": "The Alcazaba and the Gibralfaro castle view.",
    "football": "Málaga CF at La Rosaleda.",
    "gettingThere": "Direct flights from the UK; the airport is 15 minutes from town.",
    "tip": "Antigua Casa de Guardia chalks your bill on the bar - don't wipe it off."
  },
  {
    "city": "Benalmádena",
    "region": "Andalusia",
    "country": "Spain",
    "colour": "red",
    "pint": "~€3",
    "localBeer": "Victoria",
    "bestFor": "Marina bars & beaches",
    "bars": [
      {
        "name": "Dec's at the Marina",
        "note": "busy pub in Puerto Marina"
      },
      {
        "name": "Casey Dukes",
        "note": "Irish bar by 24 Hour Square"
      },
      {
        "name": "The Drunken Sailor",
        "note": "views by the windmill roundabout"
      }
    ],
    "eat": "Seafood along the promenade.",
    "dontMiss": "The cable car up Monte Calamorro, and the Buddhist Stupa.",
    "football": "Junior Firpo grew up here; Málaga CF are 20 minutes away.",
    "gettingThere": "15 minutes from Málaga airport; the coastal train stops here.",
    "tip": "Get the cable car up Calamorro for the view, then the marina bars at sunset."
  },
  {
    "city": "Paris",
    "region": "Île-de-France",
    "country": "France",
    "colour": "blue",
    "pint": "~€8",
    "localBeer": "Brasserie de la Goutte d'Or",
    "bestFor": "Café terraces",
    "bars": [
      {
        "name": "Harry's New York Bar",
        "note": "classic bar near the Opéra since 1911"
      },
      {
        "name": "Le Bombardier",
        "note": "British pub by the Panthéon"
      }
    ],
    "eat": "Steak frites at any proper brasserie.",
    "dontMiss": "Sunset from Montmartre.",
    "football": "PSG at the Parc des Princes.",
    "gettingThere": "Eurostar from London, or fly into Charles de Gaulle.",
    "tip": "A pint costs a fortune - drink wine or a demi instead."
  },
  {
    "city": "Marne-la-Vallée",
    "region": "Île-de-France",
    "country": "France",
    "colour": "purple",
    "pint": "~€9",
    "localBeer": "Kronenbourg",
    "bestFor": "Disneyland Paris",
    "bars": [
      {
        "name": "The Royal Pub",
        "note": "English-style pub in Disney Village"
      },
      {
        "name": "Billy Bob's Country Western Saloon",
        "note": "Disney Village, busy after the parks"
      }
    ],
    "eat": "Disney Village, or head into Paris.",
    "dontMiss": "The fireworks over the castle at closing time.",
    "gettingThere": "TGV or RER to Marne-la-Vallée-Chessy; shuttles from CDG.",
    "tip": "Stay for the castle fireworks, then the Royal Pub in Disney Village."
  },
  {
    "city": "Amsterdam",
    "region": "North Holland",
    "country": "Netherlands",
    "colour": "orange",
    "pint": "~€6",
    "localBeer": "Brouwerij 't IJ",
    "bestFor": "Brown cafés & canals",
    "bars": [
      {
        "name": "Brouwerij 't IJ",
        "note": "brewery taproom under a windmill"
      },
      {
        "name": "In de Wildeman",
        "note": "classic beer café"
      },
      {
        "name": "Café Hoppe",
        "note": "brown café on the Spui since 1670"
      }
    ],
    "eat": "Bitterballen with every round.",
    "dontMiss": "The Heineken Experience, then a canal boat.",
    "football": "Ajax at the Johan Cruijff ArenA.",
    "gettingThere": "Fly into Schiphol - 15 minutes by train to Centraal.",
    "tip": "Brouwerij 't IJ under the windmill - go early, it's packed by six."
  },
  {
    "city": "Malia",
    "region": "Crete",
    "country": "Greece",
    "colour": "teal",
    "pint": "~€4",
    "localBeer": "Mythos",
    "bestFor": "Beach Road nights",
    "bars": [
      {
        "name": "Malia Beach Road",
        "note": "the famous strip, pedestrianised at night"
      },
      {
        "name": "Old Town tavernas",
        "note": "quieter, sometimes with live Greek music"
      }
    ],
    "eat": "Gyros late at night, or a slow taverna dinner in the old town.",
    "dontMiss": "The Minoan Palace of Malia, just outside town.",
    "football": "OFI Crete in Heraklion.",
    "gettingThere": "About 40 minutes from Heraklion airport.",
    "tip": "Old Town tavernas for dinner, Beach Road after midnight."
  },
  {
    "city": "Tokyo",
    "region": "Kanto",
    "country": "Japan",
    "colour": "red",
    "pint": "¥600–1,200",
    "localBeer": "Japanese craft on tap",
    "bestFor": "Craft bars & tiny back-alley drinking",
    "bars": [
      {
        "name": "Mikkeller Bar Tokyo",
        "note": "Shibuya, 20 taps over two floors"
      },
      {
        "name": "DevilCraft",
        "note": "Kanda/Nihonbashi, house IPAs and deep-dish pizza"
      },
      {
        "name": "Tokyo Beerzilla",
        "note": "Asakusa, British craft beer and cider"
      }
    ],
    "eat": "Yakitori and a cold one in the tiny bars under the train tracks.",
    "dontMiss": "Bar-hopping the tiny alley bars of Golden Gai in Shinjuku.",
    "football": "FC Tokyo at Ajinomoto Stadium.",
    "gettingThere": "Direct flights from London to Haneda and Narita.",
    "tip": "Golden Gai bars are tiny and some charge a cover - check the sign on the door."
  },
  {
    "city": "Osaka",
    "region": "Kansai",
    "country": "Japan",
    "colour": "orange",
    "pint": "¥600–1,500",
    "localBeer": "Minoh Beer",
    "bestFor": "Street food & beer",
    "bars": [
      {
        "name": "Beer Belly Tenma",
        "note": "Minoh Brewery's flagship, a dozen of their beers, no cover charge"
      },
      {
        "name": "Dotonbori Brewery Factory",
        "note": "brewed on site under the Shochikuza theatre"
      },
      {
        "name": "Craft Beer Works Kamikaze",
        "note": "west of Shinsaibashi, almost two dozen taps"
      }
    ],
    "eat": "Takoyaki and okonomiyaki on the go around Dotonbori.",
    "dontMiss": "Dotonbori's neon canal at night, then Osaka Castle by day.",
    "football": "Gamba Osaka or Cerezo Osaka - two J.League clubs in one city.",
    "gettingThere": "Shinkansen from Tokyo in about 2.5 hours, or fly into Kansai Airport.",
    "tip": "Beer Belly Tenma has no cover charge - a rarity in Osaka."
  },
  {
    "city": "Narita",
    "region": "Chiba",
    "country": "Japan",
    "colour": "red",
    "pint": "~¥900",
    "localBeer": "Japanese lager",
    "bestFor": "Pints before the flight",
    "bars": [
      {
        "name": "The Barge Inn",
        "note": "British-style pub, a Narita institution"
      }
    ],
    "eat": "Grilled eel along the Naritasan Omotesando.",
    "dontMiss": "Naritasan Shinshoji temple.",
    "gettingThere": "Right by Narita Airport; trains into Tokyo.",
    "tip": "The Barge Inn is a short taxi from the airport - perfect for a long layover."
  },
  {
    "city": "Kyoto",
    "region": "Kansai",
    "country": "Japan",
    "colour": "purple",
    "pint": "¥800–1,200",
    "localBeer": "Kyoto Brewing Co",
    "bestFor": "Temples & tiny beer bars",
    "bars": [
      {
        "name": "Kyoto Brewing Co",
        "note": "taproom in south Kyoto, weekends"
      },
      {
        "name": "Bungalow",
        "note": "10 taps and fresh bread"
      },
      {
        "name": "Beer Komachi",
        "note": "tiny bar near Higashiyama, seven Japanese taps"
      }
    ],
    "eat": "Kaiseki, or street food in Nishiki Market.",
    "dontMiss": "The torii gate tunnels at Fushimi Inari.",
    "football": "Kyoto Sanga at Sanga Stadium by Kyocera.",
    "gettingThere": "Shinkansen from Tokyo in about 2h15; 15 minutes from Osaka.",
    "tip": "Fushimi Inari at sunrise, Kyoto Brewing Co at the weekend."
  },
  {
    "city": "Orlando",
    "region": "Florida",
    "country": "United States",
    "colour": "purple",
    "pint": "~$7–9",
    "localBeer": "Ivanhoe Park Brewing",
    "bestFor": "Breaks between the parks",
    "bars": [
      {
        "name": "Redlight Redlight",
        "note": "Audubon Park, long-time beer bar turned microbrewery"
      },
      {
        "name": "Ivanhoe Park Brewing Co.",
        "note": "Ivanhoe Village, themed on a lost lakeside amusement park"
      },
      {
        "name": "Hammered Lamb",
        "note": "downtown, lake views and 70+ beers"
      }
    ],
    "eat": "Mills 50 for the best Vietnamese and Asian food in town.",
    "dontMiss": "A sunset lap of Lake Eola downtown, away from the theme parks.",
    "football": "Orlando City SC at Inter&Co Stadium, downtown.",
    "gettingThere": "Direct flights from the UK into Orlando International (MCO).",
    "tip": "Redlight Redlight for the best beer list in town."
  },
  {
    "city": "Tampa Bay",
    "region": "Florida",
    "country": "United States",
    "colour": "teal",
    "pint": "~$7–9",
    "localBeer": "Cigar City Jai Alai",
    "bestFor": "Brewery hopping",
    "bars": [
      {
        "name": "Sky Puppy Brewing",
        "note": "Ybor City, inside Tampa's oldest original firehouse"
      },
      {
        "name": "BarrieHaus Beer Co.",
        "note": "Ybor City lager specialists with a beer-garden feel"
      },
      {
        "name": "Angry Chair Brewing",
        "note": "Seminole Heights, famous for its stouts"
      }
    ],
    "eat": "A Cuban sandwich in Ybor City, where Tampa reckons it was invented.",
    "dontMiss": "A stroll along the Tampa Riverwalk, then out to Ybor's 7th Avenue.",
    "football": "Tampa Bay Rowdies at Al Lang Stadium, St. Petersburg.",
    "gettingThere": "Fly into Tampa International, or drive about 1.5 hours from Orlando.",
    "tip": "Ybor City on 7th Avenue for brewery-hopping - Sky Puppy's in the old firehouse."
  },
  {
    "city": "Kissimmee",
    "region": "Florida",
    "country": "United States",
    "colour": "green",
    "pint": "~$7–9",
    "localBeer": "Florida craft on tap",
    "bestFor": "Pints near the parks",
    "bars": [
      {
        "name": "The Fox & Hounds Public House",
        "note": "British pub food and pints for when you're homesick"
      },
      {
        "name": "Rock & Brews",
        "note": "craft beer, comfort food and rock music"
      },
      {
        "name": "Charley's Pub",
        "note": "happy hour noon till 7, Monday to Saturday"
      }
    ],
    "eat": "Pub grub at the Fox & Hounds, or a giant American breakfast anywhere on the 192.",
    "dontMiss": "Old Town's Saturday night classic car cruise.",
    "football": "Orlando City SC are about half an hour away downtown.",
    "gettingThere": "Right next to Walt Disney World, about 25 minutes from Orlando airport.",
    "tip": "The Fox & Hounds does a proper British breakfast when you're homesick."
  },
  {
    "city": "Chicago",
    "region": "Illinois",
    "country": "United States",
    "colour": "blue",
    "pint": "~$7–9",
    "localBeer": "Goose Island",
    "bestFor": "Historic taverns",
    "bars": [
      {
        "name": "Billy Goat Tavern",
        "note": "home of the 1945 'Curse of the Billy Goat' on the Cubs"
      },
      {
        "name": "The Berghoff",
        "note": "holds Chicago liquor licence No. 1"
      },
      {
        "name": "Marge's Still",
        "note": "Old Town, claims to be the city's oldest tavern, from 1885"
      }
    ],
    "eat": "Deep dish pizza, an Italian beef, or a Chicago dog - no ketchup.",
    "dontMiss": "A Cubs game at Wrigley Field, then the bars of Wrigleyville.",
    "football": "Chicago Fire FC at Soldier Field.",
    "gettingThere": "Direct flights from London into O'Hare.",
    "tip": "Order a 'cheezborger' at the Billy Goat - no fries, chips."
  },
  {
    "city": "Philadelphia",
    "region": "Pennsylvania",
    "country": "United States",
    "colour": "red",
    "pint": "~$7–9",
    "localBeer": "Yards Brewing",
    "bestFor": "Old taverns & Belgian beer",
    "bars": [
      {
        "name": "McGillin's Olde Ale House",
        "note": "since 1860, the oldest continuously operating bar in Philly"
      },
      {
        "name": "Monk's Café",
        "note": "Rittenhouse, a Belgian beer emporium"
      },
      {
        "name": "Yards Brewing",
        "note": "the city's own brewery and taproom"
      }
    ],
    "eat": "A cheesesteak, obviously, then graze Reading Terminal Market.",
    "dontMiss": "The Liberty Bell and Independence Hall, then run the Rocky steps.",
    "football": "Philadelphia Union at Subaru Park in Chester.",
    "gettingThere": "Direct flights from London into Philadelphia International.",
    "tip": "McGillin's has every bar's sign from Philly's history on its walls."
  },
  {
    "city": "Lake Buena Vista",
    "region": "Florida",
    "country": "United States",
    "colour": "blue",
    "pint": "~$9–12",
    "localBeer": "Florida craft",
    "bestFor": "Walt Disney World",
    "bars": [
      {
        "name": "Raglan Road",
        "note": "Irish pub at Disney Springs"
      },
      {
        "name": "Rose & Crown Pub",
        "note": "Epcot's UK pavilion - a pint of home"
      },
      {
        "name": "Jock Lindsey's Hangar Bar",
        "note": "Disney Springs, Indiana Jones-themed"
      }
    ],
    "eat": "Disney Springs has everything.",
    "dontMiss": "Magic Kingdom fireworks.",
    "football": "Orlando City SC, about half an hour away downtown.",
    "gettingThere": "About 25 minutes from Orlando International Airport.",
    "tip": "Rose & Crown in Epcot - the closest thing to a proper pint in Florida."
  }
];
