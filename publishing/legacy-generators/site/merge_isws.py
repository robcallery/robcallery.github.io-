import sys, openpyxl, json
sys.path.insert(0,'/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad')
from regions import load, save
import isws_data as D
ws=openpyxl.load_workbook('/mnt/user-data/attachments/9cac7207-2d1b-5bf4-969e-62974606aff5/93419b9b-Travel_Guides_Ireland_Scotland_Wales_Spain_80.xlsx')['Travel Guides']
hdr=[c.value for c in ws[1]]
fix=lambda v: v.replace('’',"'") if isinstance(v,str) else v
rows=[{k:(fix(v) if k in ('Bar 1','Bar 2','Don’t miss','Best for','Snapshot illustration') else v) for k,v in zip(hdr,r)} for r in ws.iter_rows(min_row=2,values_only=True) if r[2]]
SHELF={'Travelling Ireland':'ireland','Travelling Scotland':'scotland','Travelling Wales':'wales','Travelling Spain':'spain'}
SRC={'ireland':D.IE,'scotland':D.SC,'wales':D.WA,'spain':D.ES}
DROP={'The Sussex','La Surfera'}   # Wetherspoons / couldn't be found
pre,G=load(); by={g['city']:g for g in G}
cols=['teal','orange','blue','green','red','purple']
SNAP={}
new=[]
for i,r in enumerate(rows):
    sh=SHELF[r['Book']]; place=r['Place']
    bars=[b for b in (r['Bar 1'],r['Bar 2']) if b and b not in DROP]
    if place in D.EXIST_BARS:            # already on the site: swap to the sheet's two bars, keep everything else
        g=by[place]; old={b['name']:b.get('note') for b in g.get('bars',[])}
        alias={'The Bow Bar':'The Bow Bar','The Prince of Wales':'Prince of Wales','The No Sign Wine Bar':'No Sign Bar'}
        nb=[]
        for b in bars:
            note=D.EXIST_BARS[place].get(b) or old.get(b) or old.get(alias.get(b,''))
            nb.append({'name':b,**({'note':note} if note else {})})
        gone=[b for b in g.get('bars',[]) if b['name'] not in bars and b['name'] not in [alias.get(x) for x in bars]]
        if gone: g['archivedBars']=g.get('archivedBars',[])+gone
        g['bars']=nb; g['shelf']=sh; g['group']=D.EXIST_GROUP[place]
        continue
    name='Newport, Wales' if (place=='Newport' and sh=='wales') else place
    county,grp,pint,beer,eat,fb,gt,tip,dyk,notes=SRC[sh][name]
    e={'city':name,'region':county,'country':'Spain' if sh=='spain' else ('Ireland' if sh=='ireland' and 'Northern' not in (r['Country'] or '') else 'United Kingdom'),
       'shelf':sh,'group':grp,'colour':cols[i%6],'pint':pint,'localBeer':beer,'bestFor':r['Best for'],
       'bars':[{'name':b,**({'note':notes[b]} if notes.get(b) else {})} for b in bars],
       'eat':eat,'dontMiss':r['Don’t miss']+('.' if not r['Don’t miss'].endswith('.') else '')}
    if fb: e['football']=fb
    e['gettingThere']=gt; e['tip']=tip
    new.append(e); SNAP[name]=(r['Snapshot illustration'],dyk)
for c,gp in D.EXIST_GROUP.items():
    if c in by: by[c]['group']=gp; by[c]['shelf']={'Leinster':'ireland','Ulster':'ireland'}.get(gp) or ('scotland' if gp in D.GROUP_ORDER['scotland'] else 'wales' if gp in D.GROUP_ORDER['wales'] else 'spain')
assert not [e for e in new if e['city'] in by], [e['city'] for e in new if e['city'] in by]
G+=new
# keep each book's contents grouped: order by region heading, then existing places first, then the sheet order
pos={id(g):k for k,g in enumerate(G)}
def key(g):
    sh=g.get('shelf')
    if sh in D.GROUP_ORDER and g.get('group')!='Airports':
        # put these books where the first of them currently sits, grouped
        return (0,sh,D.GROUP_ORDER[sh].index(g['group']),pos[id(g)])
    return (1,pos[id(g)])
books=[g for g in G if g.get('shelf') in D.GROUP_ORDER and g.get('group')!='Airports']
rest=[g for g in G if not (g.get('shelf') in D.GROUP_ORDER and g.get('group')!='Airports')]
books.sort(key=key)
# insert the four books after the last UK regional entry (before the non-UK entries) - order in the file doesn't affect shelves
G=rest+books
save(pre,G)
json.dump(SNAP,open('/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/isws_snaps.json','w'),ensure_ascii=False,indent=1)
print('added',len(new),'total',len(G))
