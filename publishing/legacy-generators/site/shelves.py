import json
# id, title, spine colour, band colour, ink
SHELVES = [
 ('north-england', 'North England', '#1e3f9a', '#ffcd00', '#ffffff'),
 ('south-england', 'South England', '#a8262b', '#f2d27a', '#ffffff'),
 ('east-england', 'East England', '#0f6f73', '#f2d27a', '#ffffff'),
 ('west-england', 'West England', '#2f6b3c', '#f2d27a', '#ffffff'),
 ('wales', 'Wales', '#c8102e', '#00a650', '#ffffff'),
 ('scotland', 'Scotland', '#0b3d91', '#ffffff', '#ffffff'),
 ('ireland', 'Ireland', '#169b62', '#ff883e', '#ffffff'),
 ('spain', 'Spain', '#c60b1e', '#ffc400', '#ffc400'),
 ('france', 'France', '#0055a4', '#ef4135', '#ffffff'),
 ('usa', 'USA', '#2c2b5e', '#b22234', '#ffffff'),
 ('rest-of-world', 'Rest of the World', '#6b4a2b', '#d9b45a', '#f3e2b8'),
 ('airports', 'Airports', '#3f4655', '#ffcd00', '#ffcd00'),
 ('us-capitals', 'US State Capitals', '#7a1f2b', '#d9b45a', '#f3e2b8'),
 ('disney-parks', 'Disney Parks', '#2a3f8f', '#d9b45a', '#ffffff'),
 ('f1-2026', 'F1 in 2026', '#e10600', '#111111', '#ffffff'),
]
# optional extras per book: words before the title, and a note printed in the contents
PREFIX = {'us-capitals': 'Travelling the'}
DEFAULT_NOTE = 'Prices were researched in October 2026 and are a rough guide - check before you go.'
NOTE = {'f1-2026': "Prices are Numbeo's October 2026 average for a half-litre draught in the host city, or the nearest city it covers. Calendar as of October 2026 - Bahrain's race moved to Sepang and Saudi Arabia was dropped. Bars were checked in October 2026, but check before you go.", 'disney-parks': 'Prices are correct as of 22 October 2026, where shown. Beer is not sold everywhere in the parks, and menus, festival booths and prices change often - check before you go.', 'us-capitals': 'Prices are the 2026 statewide median beer order (Toast), not a measured pint in the city. Bars and facts are research leads and are still being checked.'}
SHELF_JSON = json.dumps([{'id': a, 't': b, 'c': c, 'b': d, 'i': e, 'p': PREFIX.get(a, 'Travelling'), 'n': NOTE.get(a, DEFAULT_NOTE)} for a, b, c, d, e in SHELVES])
# which shelf a guide sits on (a guide can also say shelf:"..." itself)
SHELF_OF_JS = r'''function shelfOf(g){
    if(g.shelf)return g.shelf;
    if(g.group==='Airports')return 'airports';
    var gr=g.group||'',c=g.country||'';
    if(c==='United Kingdom'){
      if(/^(Yorkshire|North East|North West)$/.test(gr))return 'north-england';
      if(/^(London|South East)$/.test(gr))return 'south-england';
      if(gr==='South West')return 'west-england';
      if(gr==='East of England')return 'east-england';
      if(gr==='Midlands')return /^(West Midlands|Staffordshire|Shropshire|Herefordshire|Worcestershire|Warwickshire)$/.test(g.region||'')?'west-england':'east-england';
      if(gr==='Wales')return 'wales';if(gr==='Scotland')return 'scotland';if(gr==='Northern Ireland')return 'ireland';
      return 'north-england';
    }
    return {'Ireland':'ireland','Spain':'spain','France':'france','United States':'usa'}[c]||'rest-of-world';
  }'''
