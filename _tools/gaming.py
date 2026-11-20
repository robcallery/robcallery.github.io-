#!/usr/bin/env python3
"""Add a Calz Plays (gaming blog) post to callery.co.uk.

    python3 _tools/gaming.py posts/<folder>        # post.md + post.json (+ an optional screenshot)

Builds /gaming/blog/<slug>/ from the standard post layout, then updates the blog front page, every category
page (making a new one if needed), the previous post's 'Newer post' link, the Callery Chronicle, the sitemap
and the share image. The art on the monitor is the game's own art from earlier posts, or Rob's screenshot.
"""
import os, re, sys, json, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kit
from kit import esc

BASE = '/gaming/blog/'
TEMPLATE = BASE + 'fm27-free-launch-preview/index.html'
CAT_TEMPLATE = BASE + 'category/fc-27/index.html'


# ------------------------------------------------------------------ data from the live pages
def posts_from_site():
    h = kit.read(BASE + 'index.html')
    out = []
    pat = r'<a (?:class="feat" )?href="(/gaming/blog/[^"]+/)"><div class="thumb">(<svg.*?</svg>)</div><div class="(?:fb|cb)"><p class="labs">(.*?)</p><h3>(.*?)</h3>(.*?)</div></a>'
    for m in re.finditer(pat, h, re.S):
        rest = m.group(5)
        labs = re.findall(r'<span class="lab" style="--c:(#[0-9a-fA-F]+)">(.*?)</span>', m.group(3))
        out.append({'url': m.group(1), 'thumb': m.group(2), 'labs': [(html.unescape(n), c) for c, n in labs], 'title': html.unescape(m.group(4)),
                    'date': re.search(r'datetime="([\d-]+)"', rest).group(1), 'mins': int(re.search(r'(\d+) min read', rest).group(1)),
                    'sum': html.unescape(re.search(r'<p class="sum">(.*?)</p>', rest, re.S).group(1))})
    return out


def cats_from_site():
    h = kit.read(BASE + 'index.html')
    cats = []
    for m in re.finditer(r'<a href="/gaming/blog/category/([\w-]+)/" style="--c:(#[0-9a-fA-F]+)">(.*?) <small>\d+</small></a>', h):
        slug, col, name = m.group(1), m.group(2), html.unescape(m.group(3))
        c = kit.read(f'{BASE}category/{slug}/index.html')
        tag = html.unescape(re.search(r'<div class="mast small"[^>]*>.*?<p class="tag">(.*?)</p>', c, re.S).group(1))
        cats.append({'slug': slug, 'name': name, 'colour': col, 'tag': tag})
    return cats


# ------------------------------------------------------------------ art
def reprefix(svg, new):
    ids = re.findall(r'id="([^"]+)"', svg)
    for i in sorted(set(ids), key=len, reverse=True):
        svg = re.sub(r'(id="|url\(#|href="#)' + re.escape(i) + r'(["\)])', lambda m: m.group(1) + new + i[-6:].replace('-', '') + '_' + str(ids.index(i)) + m.group(2), svg)
    return svg


def art(p, posts, prefix):
    """The monitor art: Rob's screenshot if given, else the art from the newest earlier post in the same category."""
    if p.get('screenshot_file'):
        return (f'<svg viewBox="0 0 1200 630" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">'
                f'<image href="{BASE}{p["slug"]}/{p["screenshot_file"]}" width="1200" height="630" preserveAspectRatio="xMidYMid slice"/></svg>')
    cat = p['categories'][0]
    for q in posts:
        if any(n == cat for n, _ in q['labs']):
            return reprefix(q['thumb'], prefix)
    col = p['colour']   # a fresh category: a plain glowing controller
    return (f'<svg viewBox="0 0 1200 630" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false"><defs><linearGradient id="{prefix}g" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="#14123a"/><stop offset=".6" stop-color="#1d1650"/><stop offset="1" stop-color="{col}"/></linearGradient>'
            f'<radialGradient id="{prefix}r" cx=".62" cy=".45" r=".5"><stop offset="0" stop-color="{col}" stop-opacity=".55"/><stop offset="1" stop-color="{col}" stop-opacity="0"/></radialGradient></defs>'
            f'<rect width="1200" height="630" fill="url(#{prefix}g)"/><rect width="1200" height="630" fill="url(#{prefix}r)"/>'
            '<g transform="translate(740 300)"><path d="M-230 -70 Q-200 -120 -130 -118 L130 -118 Q200 -120 230 -70 L280 110 Q296 180 230 190 Q180 196 140 130 L100 80 L-100 80 L-140 130 Q-180 196 -230 190 Q-296 180 -280 110 Z" fill="#0d0b26" stroke="#fff" stroke-opacity=".5" stroke-width="6"/>'
            '<rect x="-170" y="-50" width="26" height="80" rx="6" fill="#fff" opacity=".85"/><rect x="-197" y="-23" width="80" height="26" rx="6" fill="#fff" opacity=".85"/>'
            f'<circle cx="150" cy="-40" r="20" fill="{col}"/><circle cx="195" cy="0" r="20" fill="#ffcd00"/><circle cx="105" cy="0" r="20" fill="#ff3b8d"/><circle cx="150" cy="40" r="20" fill="#2fbf71"/></g></svg>')


# ------------------------------------------------------------------ bits of page
def lab_spans(labs):
    return ''.join(f'<span class="lab" style="--c:{c}">{esc(n)}</span>' for n, c in labs)


def card(q):
    return (f'<li class="card"><a href="{q["url"]}"><div class="thumb">{q["thumb"]}</div><div class="cb"><p class="labs">{lab_spans(q["labs"])}</p>'
            f'<h3>{esc(q["title"])}</h3><p class="sum">{esc(q["sum"])}</p><p class="meta"><time datetime="{q["date"]}">{kit.long_date(q["date"])}</time> · {q["mins"]} min read</p></div></a></li>')


def chips(cats, posts, current=None):
    n = lambda c: sum(1 for q in posts if any(x == c['name'] for x, _ in q['labs']))
    s = f'<a href="/gaming/blog/"{" aria-current=\"page\"" if current is None else ""}>All posts <small>{len(posts)}</small></a>'
    for c in sorted(cats, key=lambda c: c['name'].lower()):
        s += f'<a href="/gaming/blog/category/{c["slug"]}/" style="--c:{c["colour"]}"{" aria-current=\"page\"" if current == c["slug"] else ""}>{esc(c["name"])} <small>{n(c)}</small></a>'
    return s


def render_index(posts, cats):
    h = kit.read(BASE + 'index.html')
    f = posts[0]
    feat = (f'<a class="feat" href="{f["url"]}"><div class="thumb">{f["thumb"]}</div><div class="fb"><p class="labs">{lab_spans(f["labs"])}</p><h3>{esc(f["title"])}</h3>'
            f'<p class="meta"><time datetime="{f["date"]}">{kit.long_date(f["date"])}</time> · {f["mins"]} min read</p><p class="sum">{esc(f["sum"])}</p>'
            '<span class="cta">Read the full post <span aria-hidden="true">→</span></span></div></a>')
    h = re.sub(r'<a class="feat" href=.*?</a>(?=</section>)', lambda m: feat, h, count=1, flags=re.S)
    h = re.sub(r'(<nav class="chips" aria-label="Categories">).*?(</nav>)', lambda m: m.group(1) + chips(cats, posts) + m.group(2), h, count=1, flags=re.S)
    h = re.sub(r'(<section class="more"[^>]*><h2[^>]*>.*?</h2><ul class="cards">).*?(</ul></section>)', lambda m: m.group(1) + ''.join(card(q) for q in posts[1:]) + m.group(2), h, count=1, flags=re.S)
    h = set_ld_list(h, posts, 'blogPost', lambda q: {'@type': 'BlogPosting', 'headline': q['title'], 'url': kit.ORIGIN + q['url'], 'datePublished': q['date']})
    kit.write(BASE + 'index.html', h)


def set_ld_list(h, posts, key, fn):
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    ld = json.loads(m.group(1)); ld['@graph'][0][key] = [fn(q) for q in posts]
    return h[:m.start(1)] + json.dumps(ld, ensure_ascii=False) + h[m.end(1):]


def render_category(c, posts, cats):
    path = f'{BASE}category/{c["slug"]}/index.html'
    mine = [q for q in posts if any(n == c['name'] for n, _ in q['labs'])]
    if os.path.exists(os.path.join(kit.ROOT, path.lstrip('/'))):
        h = kit.read(path)
    else:   # a new category: copy another category page and rename it
        h = kit.read(CAT_TEMPLATE); old = re.search(r'<li aria-current="page">(.*?)</li>', h).group(1)
        url = kit.ORIGIN + f'{BASE}category/{c["slug"]}/'
        desc = f'{c["name"]} posts from Calz Plays, Rob Callery’s gaming blog.'
        h = kit.set_seo(h, kit.seo_block(desc, url, f'{c["name"]} - Calz Plays - Rob Callery', kit.ORIGIN + BASE + 'og.jpg', og_type='website', extra=re.search(r'(<script type="application/ld\+json">.*?</script>\n)', h, re.S).group(1)),
                        f'{c["name"]} - Calz Plays | Callery.co.uk')
        h = h.replace(f'<li aria-current="page">{old}</li>', f'<li aria-current="page">{esc(c["name"])}</li>')
        h = re.sub(r'<div class="mast small" style="--c:[^"]+"><p class="mk">Calz Plays · Category</p><h1>.*?</h1><p class="tag">.*?</p></div>',
                   f'<div class="mast small" style="--c:{c["colour"]}"><p class="mk">Calz Plays · Category</p><h1>{esc(c["name"])}</h1><p class="tag">{esc(c["tag"])}</p></div>', h, count=1, flags=re.S)
        m = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S); ld = json.loads(m.group(1))
        ld['@graph'][0]['name'] = f'{c["name"]} - Calz Plays'; ld['@graph'][0]['url'] = url
        ld['@graph'][1]['itemListElement'][-1].update({'name': c['name'], 'item': url})
        h = h[:m.start(1)] + json.dumps(ld, ensure_ascii=False) + h[m.end(1):]
        kit.sitemap_add(f'{BASE}category/{c["slug"]}/', mine[0]['date'])
    h = re.sub(r'(<nav class="chips" aria-label="Categories">).*?(</nav>)', lambda m: m.group(1) + chips(cats, posts, c['slug']) + m.group(2), h, count=1, flags=re.S)
    h = re.sub(r'<h2 id="cl-h" class="sech">\d+ posts?</h2><ul class="cards">.*?</ul>',
               lambda m: f'<h2 id="cl-h" class="sech">{len(mine)} post{"s" if len(mine) != 1 else ""}</h2><ul class="cards">' + ''.join(card(q) for q in mine) + '</ul>', h, count=1, flags=re.S)
    h = set_ld_list(h, mine, 'hasPart', lambda q: {'@type': 'BlogPosting', 'headline': q['title'], 'url': kit.ORIGIN + q['url']})
    kit.write(path, h)
    if mine:
        kit.sitemap_touch(f'{BASE}category/{c["slug"]}/', mine[0]['date'])


def split_title(t):
    m = re.match(r'(.+?[–:!?])\s+(.+)', t)
    return f'{esc(m.group(1))}<br> <span class="hl">{esc(m.group(2))}</span>' if m else esc(t)


# ------------------------------------------------------------------ the post
def build(folder):
    p = json.load(open(os.path.join(folder, 'post.json'), encoding='utf-8'))
    src = open(os.path.join(folder, 'post.md'), encoding='utf-8').read()
    title, body, heads = kit.md(src)
    p['date'] = kit.iso(p['date']); slug = p['slug']; url = kit.ORIGIN + BASE + slug + '/'; mins = kit.mins(src)
    posts = [q for q in posts_from_site() if q['url'] != BASE + slug + '/']
    cats = cats_from_site()
    for name in p['categories']:   # new categories need a colour and a line about them
        if not any(c['name'] == name for c in cats):
            nc = p['new_categories'][name]
            cats.append({'slug': kit.slugify(name), 'name': name, 'colour': nc['colour'], 'tag': nc['tag']})
    labs = [(c['name'], c['colour']) for n in p['categories'] for c in cats if c['name'] == n]
    p['colour'] = labs[0][1]
    os.makedirs(os.path.join(kit.ROOT, BASE.strip('/'), slug), exist_ok=True)
    if p.get('screenshot'):
        from travel import photo
        photo(os.path.join(folder, p['screenshot']), os.path.join(kit.ROOT, BASE.strip('/'), slug, 'screen.jpg'), 1600)
        p['screenshot_file'] = 'screen.jpg'
    hero = art(p, posts, 'h' + slug.replace('-', '')[:16])
    thumb = art(p, posts, 't' + slug.replace('-', '')[:16])

    t = kit.read(TEMPLATE)
    c0 = next(c for c in cats if c['name'] == p['categories'][0])
    crumbs = [('Callery.co.uk', '/'), ('Gaming setup', '/gaming/'), ('Calz Plays', BASE), (c0['name'], f'{BASE}category/{c0["slug"]}/'), (title, BASE + slug + '/')]
    ld = {'@context': 'https://schema.org', '@graph': [{
        '@type': 'BlogPosting', '@id': url + '#post', 'headline': title, 'alternativeHeadline': p['dek'], 'description': p['description'], 'url': url, 'mainEntityOfPage': url,
        'image': {'@type': 'ImageObject', 'url': url + 'og.jpg', 'width': 1200, 'height': 630}, 'datePublished': p['date'], 'dateModified': p['date'],
        'author': kit.ROB, 'publisher': kit.ROB, 'isPartOf': {'@type': 'Blog', '@id': kit.ORIGIN + BASE + '#blog', 'name': 'Calz Plays', 'url': kit.ORIGIN + BASE},
        'articleSection': p['categories'], 'keywords': ', '.join(p.get('tags', [])), **({'about': {'@type': 'VideoGame', 'name': p['game']}} if p.get('game') else {}),
        'wordCount': kit.words(src), 'timeRequired': f'PT{mins}M', 'inLanguage': 'en-GB'},
        {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': k + 1, 'name': n, 'item': kit.ORIGIN + hh} for k, (n, hh) in enumerate(crumbs)]}]}
    extra = (f'<meta property="article:published_time" content="{p["date"]}">\n<meta property="article:author" content="Rob Callery">\n<meta property="article:section" content="{esc(p["categories"][0])}">\n'
             + ''.join(f'<meta property="article:tag" content="{esc(x)}">\n' for x in p.get('tags', [])[:6]) + f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n')
    t = kit.set_seo(t, kit.seo_block(p['description'], url, title, url + 'og.jpg', extra=extra), f'{title} | Callery.co.uk')
    t = re.sub(r'<nav class="crumbs".*?</nav>', lambda m: '<nav class="crumbs" aria-label="Breadcrumb"><ol>' + ''.join(f'<li><a href="{hh}">{esc(n)}</a></li>' for n, hh in crumbs[:-1]) + '</ol></nav>', t, count=1, flags=re.S)
    ahead = (f'<header class="ahead"><p class="ribbon"><span>Calz Plays</span><span>{esc(p.get("game", c0["name"]))}</span></p><p class="labs">'
             + ''.join(f'<a class="lab" style="--c:{c}" href="{BASE}category/{kit.slugify(n)}/">{esc(n)}</a>' for n, c in labs) + f'</p><h1>{split_title(title)}</h1>'
             f'<p class="dek">{esc(p["dek"])}</p><p class="byline"><span class="av" aria-hidden="true">RC</span><span>By <a href="/">Rob Callery</a></span>'
             f'<span><time datetime="{p["date"]}">{kit.long_date(p["date"])}</time></span><span>{mins} min read</span></p></header>')
    t = re.sub(r'<header class="ahead">.*?</header>', lambda m: ahead, t, count=1, flags=re.S)
    cap = f'<figcaption>{esc(p["caption"])}</figcaption>' if p.get('caption') else ''
    t = re.sub(r'<figure class="hero">.*?</figure>', lambda m: f'<figure class="hero"><div class="mon"><div class="scr">{hero}</div></div><div class="deskline" aria-hidden="true"></div>{cap}</figure>', t, count=1, flags=re.S)
    toc = ('<details class="toc"><summary>In this article <small>' + f'{len(heads)} sections</small></summary><ol>' + ''.join(f'<li><a href="#{i}">{esc(x)}</a></li>' for i, x in heads) + '</ol></details>') if len(heads) >= 3 else ''
    if p.get('ask'):
        body += ('<aside class="yourturn" aria-labelledby="yourturn-h"><h2 id="yourturn-h"><span aria-hidden="true">🎮</span> Over to you</h2><ul>' + ''.join(f'<li>{esc(x)}</li>' for x in p['ask']) +
                 '</ul><p class="yt-cta">Tell me in the chat next time I\'m live on <a href="https://www.twitch.tv/robcallery" target="_blank" rel="noopener">Twitch</a>, or on <a href="https://x.com/calz88" target="_blank" rel="noopener">X @calz88</a>.</p></aside>')
    if p.get('sign_off'):
        body += f'<p class="mot">{esc(p["sign_off"])}</p>'
    body = re.sub(r'<!--w:[\w-]+-->', '', body)
    story = f'<div class="story">{toc}\n    <div class="prose">{body}</div>\n    {kit.share(title, url)}\n  </div>'
    t = re.sub(r'<div class="story">.*?</section>\n  </div>(?=\n  <section class="related")', lambda m: story, t, count=1, flags=re.S)
    me = {'url': BASE + slug + '/', 'thumb': thumb, 'labs': labs, 'title': title, 'date': p['date'], 'mins': mins, 'sum': p['teaser']}
    rel = ''.join(card(q) for q in posts[:2])
    t = re.sub(r'(<section class="related"[^>]*><h2[^>]*>.*?</h2><ul class="cards">).*?(</ul></section>)', lambda m: m.group(1) + rel + m.group(2), t, count=1, flags=re.S)
    older = posts[0] if posts else None
    t = re.sub(r'<nav class="pnav".*?</nav>', lambda m: '<nav class="pnav" aria-label="More posts"><a href="/gaming/blog/">All posts</a>' + (f'<a href="{older["url"]}">← Older post</a>' if older else '') + '</nav>', t, count=1, flags=re.S)
    scripts = re.findall(r'<script>.*?</script>', t[t.index('</article>'):], re.S)
    for s in scripts:
        if "querySelectorAll('.copy')" not in s:
            t = t.replace(s, '', 1)
    kit.write(BASE + slug + '/index.html', t)

    if older:   # the previous newest post gets a 'Newer post' link
        q = kit.read(older['url'] + 'index.html')
        q = re.sub(r'<a href="[^"]+">Newer post →</a>', '', q)
        q = re.sub(r'(<nav class="pnav" aria-label="More posts">.*?)(</nav>)', lambda m: m.group(1) + f'<a href="{BASE}{slug}/">Newer post →</a>' + m.group(2), q, count=1, flags=re.S)
        kit.write(older['url'] + 'index.html', q)

    posts.insert(0, me)
    render_index(posts, cats)
    for c in cats:
        render_category(c, posts, cats)
    kit.Hub.add({'url': BASE + slug + '/', 'section': 'Calz Plays', 'date': p['date'], 'title': title, 'kick': p.get('hub_kick', p['categories'][0]),
                 'teaser': p['teaser'], 'standfirst': p['dek'], 'dek': p['description'], 'thumb': reprefix(thumb, 'c' + slug.replace('-', '')[:16])})
    kit.sitemap_add(BASE + slug + '/', p['date']); kit.sitemap_touch(BASE, p['date'])
    oart = kit.svg_inner(art(p, posts[1:], 'o' + slug.replace('-', '')[:16]))
    oart = re.sub(r'<text[^>]* y="(4[5-9]\d|5\d\d|6\d\d)(?:\.\d+)?"[^>]*>.*?</text>', '', oart, flags=re.S)   # the art's own caption sits where the title goes
    if 'CALZ PLAYS' not in oart:
        oart = oart + ''
    og = kit.og_card(oart, None if 'CALZ PLAYS' in oart else 'Calz Plays', title, f'{p.get("game", c0["name"])} · Calz Plays · callery.co.uk')
    kit.og_jpg(og, BASE + slug + '/og.jpg')
    print('Calz Plays post written:', BASE + slug + '/')
    return BASE + slug + '/'


if __name__ == '__main__':
    build(sys.argv[1])
