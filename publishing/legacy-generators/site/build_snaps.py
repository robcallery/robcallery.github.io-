import sys, json, subprocess
sys.path.insert(0, '/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad')
S = {}
import glob, os
for m in sorted(os.path.basename(f)[:-3] for f in glob.glob(os.path.join(os.path.dirname(__file__) or '.', 'snaps[0-9]*.py'))):
    S.update(__import__(m).S)
p = '/home/claude/site/travel-guides/guides.js'
G = json.loads(subprocess.run(['node', '-e', "global.window={};require('" + p + "');process.stdout.write(JSON.stringify(window.GUIDES))"], capture_output=True, text=True).stdout)
cities = [g['city'] for g in G]
missing = [c for c in cities if c not in S]; extra = [c for c in S if c not in cities]
print('missing', missing, 'extra', extra)
out = {c: {'t': S[c][0], 'n': S[c][1], 'svg': S[c][2]} for c in cities if c in S}
js = '// Polaroid illustrations for the travel guides, keyed by city. Generated - edit snaps*.py and rebuild.\nwindow.SNAPS = ' + json.dumps(out, ensure_ascii=False) + ';\n'
open('/home/claude/site/travel-guides/snaps.js', 'w').write(js)
print(len(out), round(len(js) / 1024), 'KB')
