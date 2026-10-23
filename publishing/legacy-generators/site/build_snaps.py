import sys, json, subprocess
sys.path.insert(0, '/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad')
S = {}
import glob, os
for m in sorted(os.path.basename(f)[:-3] for f in glob.glob(os.path.join(os.path.dirname(__file__) or '.', 'snaps[0-9]*.py'))):
    S.update(__import__(m).S)
p = '/home/claude/site/travel-guides/guides.js'
G = json.loads(subprocess.run(['node', '-e', "global.window={};require('" + p + "');process.stdout.write(JSON.stringify(window.GUIDES))"], capture_output=True, text=True).stdout)
from shelves import SHELF_OF_JS
pairs = json.loads(subprocess.run(['node', '-e', "global.window={};require('" + p + "');" + SHELF_OF_JS + ";process.stdout.write(JSON.stringify(window.GUIDES.map(g=>[g.city,shelfOf(g)])))"], capture_output=True, text=True).stdout)
# a book can have its own picture for a city that is also in another book: key "shelf|city"
key = lambda c, b: (b + '|' + c) if (b + '|' + c) in S else c
missing = [c + ' (' + b + ')' for c, b in pairs if key(c, b) not in S]
used = {key(c, b) for c, b in pairs}; extra = [k for k in S if k not in used]
print('missing', missing, 'extra', extra)
out = {c: {'t': S[c][0], 'n': S[c][1], 'svg': S[c][2]} for c, b in pairs if '|' not in key(c, b) and c in S}
js = '// Polaroid illustrations for the travel guides, keyed by city. Generated - edit snaps*.py and rebuild.\nwindow.SNAPS = ' + json.dumps(out, ensure_ascii=False) + ';\n'
open('/home/claude/site/travel-guides/snaps.js', 'w').write(js)
print(len(out), round(len(js) / 1024), 'KB')
os.makedirs('/home/claude/site/travel-guides/snaps', exist_ok=True)
for bk in sorted({b for c, b in pairs}):
    part = {}
    for c, b in pairs:
        k = key(c, b)
        if b == bk and k in S: part[c] = {'t': S[k][0], 'n': S[k][1], 'svg': S[k][2]}
    open(f'/home/claude/site/travel-guides/snaps/{bk}.js', 'w').write('// Polaroids for one book. Generated - edit snaps*.py and rebuild.\nwindow.SNAPS = ' + json.dumps(part, ensure_ascii=False) + ';\n')
    print(bk, len(part), round(len(json.dumps(part)) / 1024), 'KB')
