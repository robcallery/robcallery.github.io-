// ===== Rob's Beer Passport =====
// One block per beer. Only name is required - everything else is optional and hidden if blank.
//   brewery / brewedIn / brewedCountry : who made it and where (shown on the stamp)
//   where / city / date ("YYYY-MM-DD") : where you had it
//   rating: 1-5 pints   notes: a line in your own words   style / abv
//   ink: "red", "blue", "green", "purple", "orange" or "black" (otherwise picked by country)
window.BEERS = [
  { name: "Baby-Faced Assassin", brewery: "Rooster's Brewing Co.", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Black Forest", brewery: "Pennine Brewing Co.", brewedIn: "Well, nr Masham", brewedCountry: "England" },
  { name: "Black Sheep", brewery: "Black Sheep Brewery", brewedIn: "Masham", brewedCountry: "England" },
  { name: "Blonde", brewery: "Daleside Brewery", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Brooklyn Lager", brewery: "Brooklyn Brewery", brewedIn: "Brooklyn, New York", brewedCountry: "USA" },
  { name: "Brooklyn Session", brewery: "Brooklyn Brewery", brewedIn: "Brooklyn, New York", brewedCountry: "USA" },
  { name: "Bud Light", brewery: "Anheuser-Busch", brewedIn: "St. Louis, Missouri", brewedCountry: "USA" },
  { name: "Budweiser", brewery: "Anheuser-Busch", brewedIn: "St. Louis, Missouri", brewedCountry: "USA" },
  { name: "Cerveza Victoria", brewery: "Cervezas Victoria", brewedIn: "Málaga", brewedCountry: "Spain" },
  { name: "Cold Bath Lager", brewery: "Cold Bath Brewing", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Cold Bath Pale", brewery: "Cold Bath Brewing", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Cold Beer", brewery: "BrewDog", brewedIn: "Ellon, Aberdeenshire", brewedCountry: "Scotland" },
  { name: "Cruzcampo", brewery: "Cruzcampo", brewedIn: "Seville", brewedCountry: "Spain" },
  { name: "Cruzcampo Radler", brewery: "Cruzcampo", brewedIn: "Seville", brewedCountry: "Spain" },
  { name: "Disco King", brewery: "Turning Point Brew Co.", brewedIn: "Knaresborough", brewedCountry: "England" },
  { name: "Dockside Haze", brewery: "Florida Avenue Brewing Co.", brewedIn: "Tampa, Florida", brewedCountry: "USA" },
  { name: "Easy Going Assassin", brewery: "Rooster's Brewing Co.", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Echo Chamber", brewery: "Rooster's Brewing Co.", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Elvis Juice", brewery: "BrewDog", brewedIn: "Ellon, Aberdeenshire", brewedCountry: "Scotland" },
  { name: "Estrella Damm", brewery: "Damm", brewedIn: "Barcelona", brewedCountry: "Spain" },
  { name: "Hazy Jane", brewery: "BrewDog", brewedIn: "Ellon, Aberdeenshire", brewedCountry: "Scotland" },
  { name: "Heineken", brewery: "Heineken", brewedIn: "Amsterdam", brewedCountry: "Netherlands" },
  { name: "Island Citrus Blonde Ale", brewery: "Islamorada Brewing Co.", brewedIn: "Islamorada, Florida", brewedCountry: "USA" },
  { name: "Kronenbourg 1664", brewery: "Kronenbourg", brewedIn: "Strasbourg", brewedCountry: "France" },
  { name: "Lagunitas IPA", brewery: "Lagunitas Brewing Co.", brewedIn: "Petaluma, California", brewedCountry: "USA" },
  { name: "Mahou", brewery: "Mahou", brewedIn: "Madrid", brewedCountry: "Spain" },
  { name: "Marcelo", brewery: "Kirkstall Brewery", brewedIn: "Leeds", brewedCountry: "England" },
  { name: "New England Assassin", brewery: "Rooster's Brewing Co.", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Pennine IPA", brewery: "Pennine Brewing Co.", brewedIn: "Well, nr Masham", brewedCountry: "England" },
  { name: "Peroni Gran Riserva", brewery: "Peroni", brewedIn: "Rome", brewedCountry: "Italy" },
  { name: "Peroni Limone di Sicilia 0.0", brewery: "Peroni", brewedIn: "Rome", brewedCountry: "Italy" },
  { name: "Peroni Nastro Azzurro", brewery: "Peroni", brewedIn: "Rome", brewedCountry: "Italy" },
  { name: "Peroni Red", brewery: "Peroni", brewedIn: "Rome", brewedCountry: "Italy" },
  { name: "Punk IPA", brewery: "BrewDog", brewedIn: "Ellon, Aberdeenshire", brewedCountry: "Scotland" },
  { name: "Smithwick's Irish Pale Ale", brewery: "Smithwick's", brewedIn: "Dublin", brewedCountry: "Ireland" },
  { name: "Stanley Pilsner" },
  { name: "Three Wishes IPA", brewery: "D3 Brewing Co.", brewedIn: "Orlando, Florida", brewedCountry: "USA" },
  { name: "Wingman", brewery: "BrewDog", brewedIn: "Ellon, Aberdeenshire", brewedCountry: "Scotland" },
  { name: "Yankee", brewery: "Rooster's Brewing Co.", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Yippy IPA", brewery: "Porterhouse Brew Co.", brewedIn: "Dublin", brewedCountry: "Ireland" }
];
