// ===== Rob's Beer Passport =====
// One block per beer. Only name is required - everything else is optional and hidden if blank.
//   brewery / brewedIn / brewedCountry : who made it and where (shown on the stamp)
//   added: date it went in the passport (shown on the stamp unless date is given)
//   where / city / date ("YYYY-MM-DD") : where you had it
//   brewerSays: how the brewery describes the beer
//   rating: 1-5 pints   notes: a line in your own words   style / abv
//   ink: "red", "blue", "green", "purple", "orange" or "black" (otherwise picked by country)
window.BEERS = [
  { name: "Baby-Faced Assassin", added: "2026-10-20", brewerSays: "Citra-hopped IPA (6.1%) - mango, apricot and grapefruit, dangerously easy to drink for its strength.", brewery: "Rooster's Brewing Co.", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Black Forest", added: "2026-10-20", brewery: "Pennine Brewing Co.", brewedIn: "Well, nr Masham", brewedCountry: "England" },
  { name: "Black Sheep", added: "2026-10-20", brewerSays: "A bold, grassy and peppery best bitter (3.8%) brewed with Dales water in Masham.", brewery: "Black Sheep Brewery", brewedIn: "Masham", brewedCountry: "England" },
  { name: "Blonde", added: "2026-10-20", brewerSays: "Golden, with a crisp, fresh palate of citrus fruit and floral notes.", brewery: "Daleside Brewery", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Brooklyn Lager", added: "2026-10-20", brewerSays: "Brooklyn's flagship amber lager (5%) - once told it was 'too flavourful'.", brewery: "Brooklyn Brewery", brewedIn: "Brooklyn, New York", brewedCountry: "USA" },
  { name: "Brooklyn Session", added: "2026-10-20", brewery: "Brooklyn Brewery", brewedIn: "Brooklyn, New York", brewedCountry: "USA" },
  { name: "Bud Light", added: "2026-10-20", brewerSays: "Light American lager - crisp, clean and easy-drinking.", brewery: "Anheuser-Busch", brewedIn: "St. Louis, Missouri", brewedCountry: "USA" },
  { name: "Budweiser", added: "2026-10-20", brewerSays: "The 'King of Beers' - a crisp American lager, beechwood aged.", brewery: "Anheuser-Busch", brewedIn: "St. Louis, Missouri", brewedCountry: "USA" },
  { name: "Cerveza Victoria", added: "2026-10-20", brewerSays: "'Malague\u00f1a y exquisita' - the authentic beer of M\u00e1laga, brewed since 1928.", brewery: "Cervezas Victoria", brewedIn: "Málaga", brewedCountry: "Spain" },
  { name: "Cold Bath Lager", added: "2026-10-20", brewery: "Cold Bath Brewing", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Cold Bath Pale", added: "2026-10-20", brewerSays: "Easy-drinking session pale (3.8%) - tangerine, citrus and gooseberry with gentle bitterness.", brewery: "Cold Bath Brewing", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Cold Beer", added: "2026-10-20", brewerSays: "'Crisp, cold, classic' - a light lager (3.4%) with subtle lemon notes. Serve ice cold.", brewery: "BrewDog", brewedIn: "Ellon, Aberdeenshire", brewedCountry: "Scotland" },
  { name: "Cruzcampo", added: "2026-10-20", brewerSays: "Andalusia's pilsner, brewed in Seville since 1904.", brewery: "Cruzcampo", brewedIn: "Seville", brewedCountry: "Spain" },
  { name: "Cruzcampo Radler", added: "2026-10-20", brewerSays: "Cruzcampo mixed with natural lemon juice - low strength, made for the heat.", brewery: "Cruzcampo", brewedIn: "Seville", brewedCountry: "Spain" },
  { name: "Disco King", added: "2026-10-20", brewerSays: "Their flagship American pale (5.1%) - Mosaic and Chinook, 'a real juicy little disco of a beer'.", brewery: "Turning Point Brew Co.", brewedIn: "Knaresborough", brewedCountry: "England" },
  { name: "Dockside Haze", added: "2026-10-20", brewery: "Florida Avenue Brewing Co.", brewedIn: "Tampa, Florida", brewedCountry: "USA" },
  { name: "Easy Going Assassin", added: "2026-10-20", brewerSays: "Gluten-free session IPA (4.3%) - the Assassin's punchy citrus and tropical fruit at lower strength.", brewery: "Rooster's Brewing Co.", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Echo Chamber", added: "2026-10-20", brewery: "Rooster's Brewing Co.", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Elvis Juice", added: "2026-10-20", brewerSays: "Grapefruit-infused IPA - big citrus, bitter finish.", brewery: "BrewDog", brewedIn: "Ellon, Aberdeenshire", brewedCountry: "Scotland" },
  { name: "Estrella Damm", added: "2026-10-20", brewerSays: "Barcelona's Mediterranean lager, brewed with barley malt, rice and hops since 1876.", brewery: "Damm", brewedIn: "Barcelona", brewedCountry: "Spain" },
  { name: "Hazy Faced Assassin", added: "2026-10-20", brewerSays: "Soft, juicy hazy IPA (5.7%) - Citra, Galaxy and Mosaic with mango and peach.", brewery: "Rooster's Brewing Co.", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Hazy Jane", added: "2026-10-20", brewerSays: "Juicy New England IPA - soft, hazy and full of tropical fruit.", brewery: "BrewDog", brewedIn: "Ellon, Aberdeenshire", brewedCountry: "Scotland" },
  { name: "Heineken", added: "2026-10-20", brewerSays: "Pure malt lager brewed with Heineken's own A-yeast.", brewery: "Heineken", brewedIn: "Amsterdam", brewedCountry: "Netherlands" },
  { name: "Island Citrus Ale", added: "2026-10-20", brewerSays: "A simply brewed citrus ale (5%) made for hot days on the water - pairs with shellfish and spicy food.", brewery: "Islamorada Beer Company", brewedIn: "Islamorada, Florida", brewedCountry: "USA" },
  { name: "Kronenbourg 1664", added: "2026-10-20", brewerSays: "French premium lager brewed with aromatic Strisselspalt hops from Alsace.", brewery: "Kronenbourg", brewedIn: "Strasbourg", brewedCountry: "France" },
  { name: "Lagunitas IPA", added: "2026-10-20", brewerSays: "West Coast IPA (6.2%) - 'electric citrus, unapologetic hops'.", brewery: "Lagunitas Brewing Co.", brewedIn: "Petaluma, California", brewedCountry: "USA" },
  { name: "Mahou", added: "2026-10-20", brewerSays: "Madrid's lager, brewed in the city since 1890.", brewery: "Mahou", brewedIn: "Madrid", brewedCountry: "Spain" },
  { name: "Marcelo", added: "2026-10-20", brewery: "Kirkstall Brewery", brewedIn: "Leeds", brewedCountry: "England" },
  { name: "New England Assassin", added: "2026-10-20", brewery: "Rooster's Brewing Co.", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Pennine IPA", added: "2026-10-20", brewerSays: "A crisp golden IPA (4.4%) - zesty fruit with mild liquorice and black pepper undertones.", brewery: "Pennine Brewing Co.", brewedIn: "Well, nr Masham", brewedCountry: "England" },
  { name: "Peroni Gran Riserva", added: "2026-10-20", brewerSays: "Full-bodied, easy-drinking Vienna-style lager (6.6%) made with 100% Italian malt.", brewery: "Peroni", brewedIn: "Rome", brewedCountry: "Italy" },
  { name: "Peroni Limone di Sicilia 0.0", added: "2026-10-20", brewerSays: "Alcohol-free Peroni blended with Sicilian lemon juice.", brewery: "Peroni", brewedIn: "Rome", brewedCountry: "Italy" },
  { name: "Peroni Nastro Azzurro", added: "2026-10-20", brewerSays: "Crisp, refreshing Italian lager brewed with Italian maize.", brewery: "Peroni", brewedIn: "Rome", brewedCountry: "Italy" },
  { name: "Peroni Red", added: "2026-10-20", brewerSays: "The original Peroni from 1846 (4.7%) - 100% Italian malt, a rounded bitter-sweet taste.", brewery: "Peroni", brewedIn: "Rome", brewedCountry: "Italy" },
  { name: "Punk IPA", added: "2026-10-20", brewerSays: "BrewDog's 'post-modern classic' - tropical fruit and grapefruit with a bitter finish.", brewery: "BrewDog", brewedIn: "Ellon, Aberdeenshire", brewedCountry: "Scotland" },
  { name: "Smithwick's Irish Pale Ale", added: "2026-10-20", brewerSays: "Amarillo-hopped pale ale with 100% pale malt - rich golden, creamy head, long finish.", brewery: "Smithwick's", brewedIn: "Dublin", brewedCountry: "Ireland" },
  { name: "Stanley Pilsner", added: "2026-10-20" },
  { name: "Three Wishes IPA", added: "2026-10-20", brewerSays: "Hazy double IPA (8.5%) brewed with Galaxy hops.", brewery: "D3 Brewing Co.", brewedIn: "Orlando, Florida", brewedCountry: "USA" },
  { name: "Wingman", added: "2026-10-20", brewerSays: "Session IPA (4.3%) - 'citrus, biscuit, fruity', with tropical fruit and pine.", brewery: "BrewDog", brewedIn: "Ellon, Aberdeenshire", brewedCountry: "Scotland" },
  { name: "Yankee", added: "2026-10-20", brewerSays: "Light, easy-drinking pale ale (4.3%) - floral and citrus from Cascade hops.", brewery: "Rooster's Brewing Co.", brewedIn: "Harrogate", brewedCountry: "England" },
  { name: "Yippy IPA", added: "2026-10-20", brewery: "Porterhouse Brew Co.", brewedIn: "Dublin", brewedCountry: "Ireland" }
];
