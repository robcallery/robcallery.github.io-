# Shared: UK region grouping + ordering for the travel guide
import json, subprocess

P = '/home/claude/site/travel-guides/guides.js'

UK_ORDER = ['Yorkshire', 'North East', 'North West', 'Scotland', 'Northern Ireland', 'Wales', 'Midlands',
            'East of England', 'London', 'South East', 'South West']
OTHER_ORDER = ['Ireland', 'Spain', 'France', 'Netherlands', 'Greece', 'Japan', 'United States', 'Airports']

EXISTING = {
    'Yorkshire': ['Redcar', 'Saltburn-by-the-Sea'],
    'North East': ['Alnwick'],
    'South East': ['Newport'],
    'North West': ['Keswick', 'Manchester', 'Liverpool'],
    'Midlands': ['Bakewell', 'Leicester', 'Daventry'],
    'London': ['Westminster', 'Southwark', 'Tower Hamlets', 'Newham', 'Brent', 'Greenwich'],
    'Wales': ['Llanrwst'],
}

def load():
    src = open(P).read()
    pre = src[:src.index('window.GUIDES')]
    G = json.loads(subprocess.run(['node', '-e', "global.window={};require('" + P + "');process.stdout.write(JSON.stringify(window.GUIDES))"], capture_output=True, text=True).stdout)
    return pre, G

def regroup(G):
    look = {c: grp for grp, cs in EXISTING.items() for c in cs}
    for g in G:
        if g.get('country') == 'United Kingdom' and g.get('group') != 'Airports':
            g['group'] = look[g['city']] if g['city'] in look else (g.get('group') if g.get('group') in UK_ORDER else 'Yorkshire')
    order = UK_ORDER + OTHER_ORDER
    idx = {id(g): i for i, g in enumerate(G)}
    G.sort(key=lambda g: (order.index(g.get('group') or g['country']), idx[id(g)]))
    return G

def save(pre, G):
    open(P, 'w').write(pre + 'window.GUIDES = ' + json.dumps(G, ensure_ascii=False, indent=2) + ';\n')

def add(G, entries, group):
    have = {g['city'] for g in G}
    cols = ['blue', 'red', 'green', 'purple', 'orange', 'teal']
    n = 0
    for i, e in enumerate(entries):
        if e['city'] in have:
            print('skip dup', e['city']); continue
        e = {'city': e['city'], 'region': e['region'], 'country': e.get('country', 'United Kingdom'), 'group': group,
             'colour': e.get('colour', cols[(len(G) + i) % len(cols)]), **{k: v for k, v in e.items() if k not in ('city', 'region', 'country', 'group', 'colour')}}
        G.append(e); n += 1
    print('added', n, 'to', group)
    return G

def d(city, region, pint, beer, best, spoons, bars, eat, dm, fb, gt, tip):
    e = dict(city=city, region=region, pint=pint, localBeer=beer, bestFor=best, eat=eat, dontMiss=dm, gettingThere=gt, tip=tip)
    if fb: e['football'] = fb
    if spoons: e['spoons'] = {'name': spoons[0], 'note': spoons[1]}
    if bars: e['bars'] = [{'name': n, 'note': t} for n, t in bars]
    return e

def run(E, group):
    pre, G = load()
    G = add(G, E, group)
    G = regroup(G)
    save(pre, G)
    print(len(G))
