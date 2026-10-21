// ===== Rob's Beer Passport =====
// One block per beer. Only name is required - everything else is optional and hidden if blank.
//   brewery / brewedIn / brewedCountry : who made it and where (shown on the stamp)
//   added: date it went in the passport (shown on the stamp unless date is given)
//   where / city / date ("YYYY-MM-DD") : where you had it
//   rating: 1-5 pints   notes: a line in your own words   style / abv
//   ink: "red", "blue", "green", "purple", "orange" or "black" (otherwise picked by country)
window.BEERS = [
  { name: "Baby-Faced Assassin", added: "2026-10-20", brewery: "Rooster's Brewing Co.", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Black Forest", added: "2026-10-20", brewery: "Pennine Brewing Co.", brewedIn: "Well, nr Masham", brewedCountry: "England" },
  { name: "Black Sheep", added: "2026-10-20", brewery: "Black Sheep Brewery", brewedIn: "Masham", brewedCountry: "England" },
  { name: "Blonde", added: "2026-10-20", brewery: "Daleside Brewery", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Brooklyn Lager", added: "2026-10-20", brewery: "Brooklyn Brewery", brewedIn: "Brooklyn, New York", brewedCountry: "USA" },
  { name: "Brooklyn Session", added: "2026-10-20", brewery: "Brooklyn Brewery", brewedIn: "Brooklyn, New York", brewedCountry: "USA" },
  { name: "Bud Light", added: "2026-10-20", brewery: "Anheuser-Busch", brewedIn: "St. Louis, Missouri", brewedCountry: "USA" },
  { name: "Budweiser", added: "2026-10-20", brewery: "Anheuser-Busch", brewedIn: "St. Louis, Missouri", brewedCountry: "USA" },
  { name: "Cerveza Victoria", added: "2026-10-20", brewery: "Cervezas Victoria", brewedIn: "Málaga", brewedCountry: "Spain" },
  { name: "Cold Bath Lager", added: "2026-10-20", brewery: "Cold Bath Brewing", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Cold Bath Pale", added: "2026-10-20", brewery: "Cold Bath Brewing", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Cold Beer", added: "2026-10-20", brewery: "BrewDog", brewedIn: "Ellon, Aberdeenshire", brewedCountry: "Scotland" },
  { name: "Cruzcampo", added: "2026-10-20", brewery: "Cruzcampo", brewedIn: "Seville", brewedCountry: "Spain" },
  { name: "Cruzcampo Radler", added: "2026-10-20", brewery: "Cruzcampo", brewedIn: "Seville", brewedCountry: "Spain" },
  { name: "Disco King", added: "2026-10-20", brewery: "Turning Point Brew Co.", brewedIn: "Knaresborough", brewedCountry: "England" },
  { name: "Dockside Haze", added: "2026-10-20", brewery: "Florida Avenue Brewing Co.", brewedIn: "Tampa, Florida", brewedCountry: "USA" },
  { name: "Easy Going Assassin", added: "2026-10-20", brewery: "Rooster's Brewing Co.", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Echo Chamber", added: "2026-10-20", brewery: "Rooster's Brewing Co.", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Elvis Juice", added: "2026-10-20", brewery: "BrewDog", brewedIn: "Ellon, Aberdeenshire", brewedCountry: "Scotland" },
  { name: "Estrella Damm", added: "2026-10-20", brewery: "Damm", brewedIn: "Barcelona", brewedCountry: "Spain" },
  { name: "Hazy Faced Assassin", added: "2026-10-20", brewery: "Rooster's Brewing Co.", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Hazy Jane", added: "2026-10-20", brewery: "BrewDog", brewedIn: "Ellon, Aberdeenshire", brewedCountry: "Scotland" },
  { name: "Heineken", added: "2026-10-20", brewery: "Heineken", brewedIn: "Amsterdam", brewedCountry: "Netherlands" },
  { name: "Island Citrus Ale", added: "2026-10-20", brewery: "Islamorada Beer Company", brewedIn: "Islamorada, Florida", brewedCountry: "USA" },
  { name: "Kronenbourg 1664", added: "2026-10-20", brewery: "Kronenbourg", brewedIn: "Strasbourg", brewedCountry: "France" },
  { name: "Lagunitas IPA", added: "2026-10-20", brewery: "Lagunitas Brewing Co.", brewedIn: "Petaluma, California", brewedCountry: "USA" },
  { name: "Mahou", added: "2026-10-20", brewery: "Mahou", brewedIn: "Madrid", brewedCountry: "Spain" },
  { name: "Marcelo", added: "2026-10-20", brewery: "Kirkstall Brewery", brewedIn: "Leeds", brewedCountry: "England" },
  { name: "New England Assassin", added: "2026-10-20", brewery: "Rooster's Brewing Co.", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Pennine IPA", added: "2026-10-20", brewery: "Pennine Brewing Co.", brewedIn: "Well, nr Masham", brewedCountry: "England" },
  { name: "Peroni Gran Riserva", added: "2026-10-20", brewery: "Peroni", brewedIn: "Rome", brewedCountry: "Italy" },
  { name: "Peroni Limone di Sicilia 0.0", added: "2026-10-20", brewery: "Peroni", brewedIn: "Rome", brewedCountry: "Italy" },
  { name: "Peroni Nastro Azzurro", added: "2026-10-20", brewery: "Peroni", brewedIn: "Rome", brewedCountry: "Italy" },
  { name: "Peroni Red", added: "2026-10-20", brewery: "Peroni", brewedIn: "Rome", brewedCountry: "Italy" },
  { name: "Punk IPA", added: "2026-10-20", brewery: "BrewDog", brewedIn: "Ellon, Aberdeenshire", brewedCountry: "Scotland" },
  { name: "Smithwick's Irish Pale Ale", added: "2026-10-20", brewery: "Smithwick's", brewedIn: "Dublin", brewedCountry: "Ireland" },
  { name: "Stanley Pilsner", added: "2026-10-20" },
  { name: "Three Wishes IPA", added: "2026-10-20", brewery: "D3 Brewing Co.", brewedIn: "Orlando, Florida", brewedCountry: "USA" },
  { name: "Wingman", added: "2026-10-20", brewery: "BrewDog", brewedIn: "Ellon, Aberdeenshire", brewedCountry: "Scotland" },
  { name: "Yankee", added: "2026-10-20", brewery: "Rooster's Brewing Co.", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Yippy IPA", added: "2026-10-20", brewery: "Porterhouse Brew Co.", brewedIn: "Dublin", brewedCountry: "Ireland" }
];
