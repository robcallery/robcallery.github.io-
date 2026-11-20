"""Shared bits for adding blog posts to callery.co.uk.

The site is plain files in this repo. These tools edit the published pages directly:
 - md()        turns Rob's Markdown into the site's article HTML
 - Hub         keeps the Callery Chronicle front page (/blog/) in step
 - sitemap_add adds or refreshes a page in sitemap.xml
 - og_jpg      draws a 1200x630 share image from SVG, with the site's own fonts
Nothing here is served: _tools is listed in .assetsignore.
"""
import os, re, json, html, datetime, subprocess, tempfile, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, '_tools')
DATA = os.path.join(TOOLS, 'data')
ORIGIN = 'https://callery.co.uk'
ROB = {'@type': 'Person', '@id': ORIGIN + '/#rob', 'name': 'Rob Callery', 'url': ORIGIN + '/'}


def esc(s, quote=True):
    return html.escape(str(s), quote=quote)


def read(path):
    return open(os.path.join(ROOT, path.lstrip('/')), encoding='utf-8').read()


def write(path, text):
    p = os.path.join(ROOT, path.lstrip('/'))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(text)


def load(name):
    return json.load(open(os.path.join(DATA, name + '.json'), encoding='utf-8'))


def save(name, obj):
    json.dump(obj, open(os.path.join(DATA, name + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def slugify(t):
    """Heading ids as the site makes them: 'What's New in FM27?' -> 'what-s-new-in-fm27' (accents dropped)."""
    t = re.sub(r'<[^>]+>', '', t).lower()
    t = re.sub(r'[^a-z0-9]+', '-', t)
    return t.strip('-')


def iso(d):
    """'7 November 2026' or '2026-11-07' -> '2026-11-07'"""
    if re.match(r'\d{4}-\d\d-\d\d$', d):
        return d
    return datetime.datetime.strptime(d, '%d %B %Y').date().isoformat()


def dt(d):
    return datetime.date.fromisoformat(iso(d))


def long_date(d):      # 7 November 2026
    x = dt(d); return f'{x.day} {x:%B %Y}'


def short_date(d):     # 7 Nov 2026
    x = dt(d); return f'{x.day} {x:%b %Y}'


def day_date(d):       # Saturday 7 November 2026
    x = dt(d); return f'{x:%A} {x.day} {x:%B %Y}'


def words(md_src):
    return len(re.findall(r"[A-Za-z0-9£'’–-]+", re.sub(r'^#.*$', '', md_src, count=1, flags=re.M)))


def mins(md_src):
    return max(1, -(-words(md_src) // 220))


# ---------------------------------------------------------------------------------------------
# Markdown, the way Rob writes it:
#   # Title / ## Heading / **whole bold line** = pull quote / *whole italic line* = aside
#   - list / --- rule / [[widget]] / short lines in a run of 3+ become a 'beats' block
# ---------------------------------------------------------------------------------------------
def inline(s):
    out, pos = [], 0
    for m in re.finditer(r'\[([^\]]+)\]\((https?://[^)\s]+|/[^)\s]*)\)', s):
        out.append(_fmt(s[pos:m.start()]))
        ext = m.group(2).startswith('http')
        out.append(f'<a href="{esc(m.group(2))}"' + (' target="_blank" rel="noopener"' if ext else '') + f'>{_fmt(m.group(1))}</a>')
        pos = m.end()
    out.append(_fmt(s[pos:]))
    return ''.join(out)


def _fmt(s):
    s = esc(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', s)
    return s


BEAT = 28   # a 'beat' is a short line like "Five." "Miles." "Per." "Hour."


def md(src, ul_class=None, lead=True):
    """Returns (title, html, headings[(id, text)])."""
    lines = src.replace('\r', '').split('\n')
    title, blocks, para = None, [], []

    def flush():
        if para:
            blocks.append(('p', ' '.join(x.strip() for x in para)))
            para.clear()
    for raw in lines:
        s = raw.strip()
        if not s:
            flush(); continue
        if s.startswith('# ') and title is None:
            flush(); title = s[2:].strip(); continue
        if s.startswith('## ') or s.startswith('### '):
            flush(); blocks.append(('h2' if s.startswith('## ') else 'h3', s.split(' ', 1)[1].strip())); continue
        if re.match(r'^(-{3,}|⸻|\*{3,})$', s):
            flush(); blocks.append(('hr', '')); continue
        if re.match(r'^\[\[[\w-]+\]\]$', s):
            flush(); blocks.append(('w', s[2:-2])); continue
        if re.match(r'^[-*•] ', s) and not re.match(r'^\*[^*]+\*$', s):
            flush()
            if blocks and blocks[-1][0] == 'ul':
                blocks[-1][1].append(s[2:].strip())
            else:
                blocks.append(('ul', [s[2:].strip()]))
            continue
        para.append(s)
        flush()          # Rob writes one paragraph per line
    flush()

    out, heads, i, first = [], [], 0, lead
    while i < len(blocks):
        k, v = blocks[i]
        if k == 'p':
            # a run of 3+ short plain lines -> beats
            j = i
            while j < len(blocks) and blocks[j][0] == 'p' and len(blocks[j][1]) <= BEAT and not re.match(r'^(\*\*.*\*\*|\*.*\*)$', blocks[j][1]):
                j += 1
            if j - i >= 3 and not first:
                out.append('<div class="beats">' + ''.join(f'<p>{inline(b[1])}</p>' for b in blocks[i:j]) + '</div>')
                i = j; continue
            if re.match(r'^\*\*[^*].*\*\*$', v) and v.count('**') == 2:
                out.append(f'<blockquote>{inline(v[2:-2])}</blockquote>')
            elif re.match(r'^\*[^*].*\*$', v) and v.count('*') == 2:
                out.append(f'<p class="aside">{inline(v[1:-1])}</p>')
            elif first:
                out.append(f'<p class="lead">{inline(v)}</p>'); first = False
            else:
                out.append(f'<p>{inline(v)}</p>')
        elif k in ('h2', 'h3'):
            hid = slugify(v)
            heads.append((hid, v)) if k == 'h2' else None
            out.append(f'<{k} id="{hid}">{inline(v)}</{k}>')
        elif k == 'ul':
            cls = f' class="{ul_class}"' if ul_class else ''
            out.append(f'<ul{cls}>' + ''.join(f'<li>{inline(x)}</li>' for x in v) + '</ul>')
        elif k == 'hr':
            out.append('<hr>')
        elif k == 'w':
            out.append(f'<!--w:{v}-->')
        i += 1
    return title, ''.join(out), heads


# ---------------------------------------------------------------------------------------------
# sitemap.xml
# ---------------------------------------------------------------------------------------------
def sitemap_add(path, lastmod):
    x = read('sitemap.xml')
    loc = ORIGIN + path
    entry = f'<url><loc>{loc}</loc><lastmod>{iso(lastmod)}</lastmod></url>'
    if f'<loc>{loc}</loc>' in x:
        x = re.sub(r'<url><loc>' + re.escape(loc) + r'</loc>(<lastmod>[^<]*</lastmod>)?</url>', entry, x)
    else:
        x = x.replace('</urlset>', entry + '\n</urlset>')
    write('sitemap.xml', x)


def sitemap_touch(path, lastmod):
    """Refresh lastmod on a listing page that already exists in the sitemap."""
    x = read('sitemap.xml'); loc = ORIGIN + path
    if f'<loc>{loc}</loc>' in x:
        sitemap_add(path, lastmod)


# ---------------------------------------------------------------------------------------------
# Share images: an SVG drawn at 1200x630 with the site's fonts, saved as JPEG
# ---------------------------------------------------------------------------------------------
FONT_CSS = ''.join(
    f'@font-face{{font-family:"{fam}";src:url("file://{os.path.join(TOOLS, "fonts", f)}");font-weight:{w}}}'
    for fam, f, w in [('Bebas Neue', 'BebasNeue-Regular.ttf', 400), ('DM Serif Display', 'DMSerifDisplay-Regular.ttf', 400),
                      ('Caveat', 'Caveat[wght].ttf', '400 700')])


def og_jpg(svg, out_path, base_dir=None):
    """Render an SVG (1200x630 viewBox) to out_path as a JPEG. Relative/absolute site image links resolve from the repo."""
    page = (f'<!doctype html><html><head><meta charset="utf-8"><base href="file://{ROOT}/"><style>{FONT_CSS}'
            'html,body{margin:0;width:1200px;height:630px;overflow:hidden;background:#0a1838}svg{display:block;width:1200px;height:630px}'
            '</style></head><body>' + svg.replace('href="/', f'href="file://{ROOT}/') + '</body></html>')
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf-8') as f:
        f.write(page); tmp = f.name
    png = tmp + '.png'
    js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:630}});"
          f"await p.goto('file://{tmp}');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);await p.screenshot({{path:'{png}'}});await b.close()}})()")
    subprocess.run(['node', '-e', js], check=True, cwd=TOOLS)
    from PIL import Image
    full = os.path.join(ROOT, out_path.lstrip('/'))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    Image.open(png).convert('RGB').save(full, 'JPEG', quality=86, optimize=True, progressive=True)
    os.unlink(tmp); os.unlink(png)


def og_card(art_svg_inner, kicker, title, sub, kicker_bg='#ffcd00', kicker_fg='#0a1838'):
    """The standard share-image layout: art behind, dark fade at the bottom, kicker badge, big title, yellow sub-line."""
    t = wrap(title, 30)[:3]
    ty = 600 - 56 - 62 * len(t)
    lines = ''.join(f'<text x="44" y="{ty + 62 * (k + 1)}" font-family="Inter,sans-serif" font-weight="800" font-size="54" fill="#fff">{esc(x)}</text>' for k, x in enumerate(t))
    kw = 34 + 22 * len(kicker or '')
    return (f'<svg viewBox="0 0 1200 630" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="ogf" x1="0" y1="0" x2="0" y2="1">'
            '<stop offset=".35" stop-color="#0a0e22" stop-opacity="0"/><stop offset="1" stop-color="#0a0e22" stop-opacity=".94"/></linearGradient></defs>'
            f'{art_svg_inner}<rect width="1200" height="630" fill="url(#ogf)"/>'
            + (f'<rect x="40" y="40" width="{kw}" height="62" rx="6" fill="{kicker_bg}"/><text x="{40 + kw / 2}" y="86" text-anchor="middle" font-family="Bebas Neue,Impact,sans-serif" font-size="46" letter-spacing="3" fill="{kicker_fg}">{esc(kicker.upper())}</text>' if kicker else '') +
            f'{lines}<text x="44" y="{ty + 62 * len(t) + 52}" font-family="Bebas Neue,Impact,sans-serif" font-size="36" letter-spacing="3" fill="#ffcd00">{esc(sub.upper())}</text></svg>')


def wrap(text, width):
    out, cur = [], ''
    for w in text.split():
        if len(cur) + len(w) + 1 > width and cur:
            out.append(cur); cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        out.append(cur)
    return out


def svg_inner(svg):
    """An <svg viewBox="0 0 1200 630"> thumbnail -> its children, for drawing inside another SVG."""
    return re.sub(r'^<svg[^>]*>|</svg>$', '', svg.strip())


# ---------------------------------------------------------------------------------------------
# The Callery Chronicle (/blog/): every post across every blog, re-laid out from data/hub.json
# ---------------------------------------------------------------------------------------------
SECTIONS = [  # id, name, blurb, home
    ('football-tales', 'Football Tales', 'Away days, home days, terrace talk and the pubs either side.', '/football-tales/'),
    ('bar-talk', 'Bar Talk', 'Opinions served daily from the VAR &amp; Firkin. Darts, football and whatever else is doing my head in.', '/var-and-firkin/bar-talk/'),
    ('calz-plays', 'Calz Plays', 'FC 27, Football Manager and the odd controller thrown across the room.', '/gaming/blog/'),
    ('travel-tales', 'Travel Tales', 'Trips, pints and the bits in between.', '/travel-tales/'),
]
DESK_MAX = 4


class Hub:
    PATH = 'blog/index.html'

    @staticmethod
    def parse():
        """Read the live /blog/ page into a list of posts (newest first). Used once to seed data/hub.json."""
        h = read(Hub.PATH)
        posts, seen = [], {}
        for m in re.finditer(r'<li><time datetime="([\d-]+)">[^<]*</time><span class="as">([^<]+)</span><a href="([^"]+)">(.*?)</a></li>', h):
            p = {'url': m.group(3), 'section': html.unescape(m.group(2)), 'date': m.group(1), 'title': html.unescape(m.group(4)),
                 'kick': '', 'teaser': '', 'standfirst': '', 'dek': '', 'thumb': None}
            posts.append(p); seen[p['url']] = p
        for m in re.finditer(r'<article class="sec".*?<p class="kick"><span>[^<]*</span>(.*?)</p><h3[^>]*><a href="([^"]+)">.*?</a></h3><p class="tz">(.*?)</p>', h, re.S):
            p = seen.get(m.group(2))
            if p:
                p['kick'] = html.unescape(m.group(1)); p['teaser'] = html.unescape(m.group(3))
        for m in re.finditer(r'href="([^"]+)" tabindex="-1" aria-hidden="true">(<svg.*?</svg>)', h, re.S):
            if m.group(1) in seen and not seen[m.group(1)]['thumb']:
                seen[m.group(1)]['thumb'] = m.group(2)
        m = re.search(r'<article class="lead".*?<p class="kick"><span>[^<]*</span>(.*?)</p><h2[^>]*><a href="([^"]+)">.*?<p class="standfirst">(.*?)</p>.*?<p class="dek"><span class="drop">(.)</span>(.*?)</p>', h, re.S)
        if m and m.group(2) in seen:
            p = seen[m.group(2)]; p['kick'] = p['kick'] or html.unescape(m.group(1))
            p['standfirst'] = html.unescape(m.group(3)); p['dek'] = html.unescape(m.group(4) + m.group(5))
        extra = re.search(r'(<aside class="box" aria-labelledby="np-h">.*?</aside>)', h, re.S)
        return {'posts': posts, 'calz_box': extra.group(1) if extra else ''}

    @staticmethod
    def add(post):
        """post: url, section, date, title, kick, teaser, standfirst, dek, thumb(svg). Newest goes to the top of its day."""
        d = load('hub')
        d['posts'] = [p for p in d['posts'] if p['url'] != post['url']]
        d['posts'].insert(0, post)
        d['posts'].sort(key=lambda p: p['date'], reverse=True)   # stable: the new post stays first on its date
        save('hub', d)
        Hub.render(d)

    @staticmethod
    def _sec(p, sid, i, pic):
        a = f'<article class="sec" aria-labelledby="{sid}{i}-h">'
        if pic and p.get('thumb'):
            a += f'<a class="spic" href="{p["url"]}" tabindex="-1" aria-hidden="true">{p["thumb"]}</a>'
        a += (f'<p class="kick"><span>{esc(p["section"], False)}</span>{esc(p["kick"], False)}</p><h3 id="{sid}{i}-h"><a href="{p["url"]}">{esc(p["title"])}</a></h3>'
              f'<p class="tz">{esc(p["teaser"])}</p><p class="dl">By Rob Callery · <time datetime="{p["date"]}">{short_date(p["date"])}</time></p></article>')
        return a

    @staticmethod
    def render(d=None):
        d = d or load('hub')
        posts = d['posts']; n = len(posts)
        h = read(Hub.PATH)
        lead, rail = posts[0], posts[1:4]
        dek = lead.get('dek') or lead.get('teaser') or ''
        front = (f'<section class="front" aria-label="Front page"><article class="lead" aria-labelledby="lead-h"><p class="kick"><span>{esc(lead["section"], False)}</span>{esc(lead["kick"], False)}</p>'
                 f'<h2 id="lead-h"><a href="{lead["url"]}">{esc(lead["title"])}</a></h2><p class="standfirst">{esc(lead.get("standfirst") or lead["teaser"])}</p>'
                 f'<figure class="pic"><a href="{lead["url"]}" tabindex="-1" aria-hidden="true">{lead.get("thumb") or ""}</a><figcaption>{esc(lead["section"], False)}: {esc(lead["kick"], False)}. Illustration, callery.co.uk</figcaption></figure>'
                 f'<div class="leadcopy"><p class="dl">By Rob Callery · <time datetime="{lead["date"]}">{short_date(lead["date"])}</time></p>'
                 f'<p class="dek"><span class="drop">{esc(dek[:1])}</span>{esc(dek[1:])}</p><p class="more"><a href="{lead["url"]}">Read the full story <span aria-hidden="true">→</span><span class="vh">: {esc(lead["title"])}</span></a></p></div></article>'
                 '<div class="rail">' + ''.join(Hub._sec(p, 'sr', i, i == 0) for i, p in enumerate(rail)))
        counts = {s[0]: sum(1 for p in posts if p['section'] == s[1]) for s in SECTIONS}
        front += ('<aside class="box inside" aria-labelledby="in-h"><h3 id="in-h">Inside today</h3><ul>' +
                  ''.join(f'<li><a href="#{sid}"><span>{name}</span><i aria-hidden="true"></i><b>{counts[sid]} {"story" if counts[sid] == 1 else "stories"}</b></a></li>' for sid, name, _, _ in SECTIONS) +
                  f'<li><a href="#archive"><span>The archive</span><i aria-hidden="true"></i><b>{n} in all</b></a></li></ul></aside></div></section>')
        desks = '<div class="desks">'
        for sid, name, blurb, home in SECTIONS:
            mine = [p for p in posts if p['section'] == name][:DESK_MAX]
            desks += (f'<section class="desk" id="{sid}" aria-labelledby="{sid}-h"><h2 class="flag" id="{sid}-h"><span>{name}</span></h2><p class="deskblurb">{blurb}</p>' +
                      ''.join(Hub._sec(p, 's' + sid, i, i == 0) for i, p in enumerate(mine)) +
                      f'<p class="deskmore"><a href="{home}">More in {name} <span aria-hidden="true">→</span></a></p>' +
                      (d.get('calz_box', '') if sid == 'calz-plays' else '') + '</section>')
        desks += '</div>'
        months = {}
        for p in posts:
            months.setdefault(p['date'][:7], []).append(p)
        arch = '<section class="archive" id="archive" aria-labelledby="ar-h"><h2 id="ar-h">The Archive</h2><p>Every story, newest first.</p><div class="months">'
        for ym, ps in months.items():
            x = datetime.date.fromisoformat(ym + '-01')
            arch += (f'<section class="month" aria-labelledby="m{ym.replace("-", "")}"><h3 id="m{ym.replace("-", "")}">{x:%B %Y}</h3><ol>' +
                     ''.join(f'<li><time datetime="{p["date"]}">{dt(p["date"]).day} {dt(p["date"]):%b}</time><span class="as">{esc(p["section"], False)}</span><a href="{p["url"]}">{esc(p["title"])}</a></li>' for p in ps) +
                     '</ol></section>')
        arch += '</div></section>'
        h = re.sub(r'<section class="front".*?</section>\n  <div class="desks">', lambda m: front + '\n  <div class="desks">', h, count=1, flags=re.S)
        h = re.sub(r'<div class="desks">.*?</div>\n  <section class="archive"', lambda m: desks + '\n  <section class="archive"', h, count=1, flags=re.S)
        h = re.sub(r'<section class="archive".*?</section>\n</main>', lambda m: arch + '\n</main>', h, count=1, flags=re.S)
        h = re.sub(r'Vol\. I · No\. \d+', f'Vol. I · No. {n}', h)
        h = re.sub(r'<span class="ed">\d+ stories', f'<span class="ed">{n} stories', h)
        ld = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S).group(1))
        ld['mainEntity']['itemListElement'] = [{'@type': 'ListItem', 'position': k + 1, 'url': ORIGIN + p['url'], 'name': p['title']} for k, p in enumerate(posts)]
        h = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>', h, count=1, flags=re.S)
        write(Hub.PATH, h)
        sitemap_touch('/blog/', posts[0]['date'])


def share(title, url):
    """The 'Pass it on' buttons used on post pages."""
    from urllib.parse import quote
    t = quote(title, safe='')
    return (f'<section class="share" aria-labelledby="sh-h"><h2 id="sh-h">Pass it on</h2><div class="sbtns">'
            f'<a class="sb wa" href="https://wa.me/?text={t}%20{quote(url, safe="/")}" target="_blank" rel="noopener">WhatsApp<span class="vh"> (opens WhatsApp)</span></a>'
            f'<a class="sb rd" href="https://www.reddit.com/submit?url={quote(url, safe="")}&amp;title={t}" target="_blank" rel="noopener">Reddit<span class="vh"> (opens Reddit)</span></a>'
            f'<button class="sb copy" type="button" data-url="{url}">Copy link</button><span class="copied" role="status" aria-live="polite"></span></div></section>')


def seo_block(desc, url, title, image, og_type='article', extra=''):
    return (f'<!-- seo -->\n<meta name="description" content="{esc(desc)}">\n<link rel="canonical" href="{url}">\n'
            f'<meta property="og:type" content="{og_type}">\n<meta property="og:site_name" content="Rob Callery">\n'
            f'<meta property="og:title" content="{esc(title)}">\n<meta property="og:description" content="{esc(desc)}">\n'
            f'<meta property="og:url" content="{url}">\n<meta property="og:image" content="{image}">\n'
            '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">\n'
            '<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:site" content="@calz88">\n'
            f'<meta name="twitter:image" content="{image}">\n{extra}<!-- /seo -->')


def set_seo(h, block, title):
    h = re.sub(r'<!-- seo -->.*?<!-- /seo -->', lambda m: block, h, count=1, flags=re.S)
    return re.sub(r'<title>.*?</title>', lambda m: f'<title>{esc(title, False)}</title>', h, count=1, flags=re.S)
