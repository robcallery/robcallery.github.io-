import sys, importlib, html
sys.path.insert(0, '.')
mods = sys.argv[2:]
S = {}
for m in mods: S.update(importlib.import_module(m).S)
cells = ''.join(f'<div class="c"><div class="ph">{svg}</div><b>{html.escape(city)}</b> · {html.escape(t)}</div>' for city, (t, n, svg) in S.items())
open('sheet.html', 'w').write(f'<html><body style="margin:0;background:#ddd;font:12px sans-serif"><div style="display:grid;grid-template-columns:repeat(4,320px);gap:8px;padding:8px">{cells}</div><style>.ph svg{{width:320px;height:256px;display:block}}</style></body></html>')
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1960, "height": 400})
    pg.goto('file://' + __import__('os').path.abspath('sheet.html')); pg.wait_for_timeout(300)
    pg.screenshot(path=sys.argv[1], full_page=True); b.close()
print(len(S))
