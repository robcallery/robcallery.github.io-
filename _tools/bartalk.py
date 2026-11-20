#!/usr/bin/env python3
"""Add a Bar Talk post, or a Make It Make Sense?! rant, to callery.co.uk.

    python3 _tools/bartalk.py _tools/posts/<folder>        # post.md + post.json

A post with "rant": true goes in the VAR & Firkin toilets (/var-and-firkin/bar-talk/make-it-make-sense/<slug>/);
anything else is a Bar Talk post (/var-and-firkin/bar-talk/<slug>/). Either way the Bar Talk page (feature,
noticeboard, filters, the gents door), the Callery Chronicle, the sitemap and the share image are updated.
"""
import os, re, sys, json, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kit
from kit import esc

BT = '/var-and-firkin/bar-talk/'
MIMS = BT + 'make-it-make-sense/'
POST_TEMPLATE = BT + 'banana-ball-barmy-cricket/index.html'
RANT_TEMPLATE = MIMS + 'razor-blade-rip-off/index.html'
TELL = ('<p class="tell">Tell me in the chat next time I’m live on <a href="https://www.twitch.tv/robcallery" target="_blank" rel="noopener">Twitch</a>, '
        'or on <a href="https://x.com/calz88" target="_blank" rel="noopener">X @calz88</a>.</p>')


# ------------------------------------------------------------------ art
ICONS = {
    'cricket': ('<rect x="820" y="150" width="20" height="300" rx="6" fill="#efe3c4"/><rect x="880" y="150" width="20" height="300" rx="6" fill="#efe3c4"/><rect x="940" y="150" width="20" height="300" rx="6" fill="#efe3c4"/>'
                '<rect x="814" y="140" width="76" height="12" rx="6" fill="#d9b45a" transform="rotate(-24 852 146)"/><rect x="900" y="132" width="70" height="12" rx="6" fill="#d9b45a" transform="rotate(30 935 138)"/>'
                '<circle cx="1040" cy="230" r="62" fill="#b3121f"/><path d="M990 196 Q1040 232 1090 196 M990 266 Q1040 230 1090 266" fill="none" stroke="#f4efe2" stroke-width="5" stroke-dasharray="7 6"/>'
                '<g stroke="#ffcd00" stroke-width="6" stroke-linecap="round" opacity=".8"><path d="M1120 180 l40 -24 M1124 236 l48 0 M1120 288 l40 24"/></g>'
                '<path d="M640 470 Q760 330 980 300" fill="none" stroke="#f4efe2" stroke-opacity=".25" stroke-width="5" stroke-dasharray="14 12"/>'),
    'darts': ('<g transform="translate(930 300)"><circle r="190" fill="#1b1b1b"/><circle r="170" fill="#f4efe2"/>'
              + ''.join(f'<path d="M0 0 L{170 * __import__("math").cos(a / 10 * 3.14159):.1f} {170 * __import__("math").sin(a / 10 * 3.14159):.1f} A170 170 0 0 1 {170 * __import__("math").cos((a + 1) / 10 * 3.14159):.1f} {170 * __import__("math").sin((a + 1) / 10 * 3.14159):.1f} Z" fill="#1b1b1b"/>' for a in range(0, 20, 2)) +
              '<circle r="112" fill="none" stroke="#b3121f" stroke-width="14"/><circle r="164" fill="none" stroke="#1d7a3a" stroke-width="12"/><circle r="22" fill="#1d7a3a"/><circle r="10" fill="#b3121f"/></g>'
              '<g transform="translate(880 250) rotate(-35)"><rect x="0" y="-5" width="150" height="10" rx="3" fill="#c9cdd4"/><path d="M150 -5 L210 -24 L210 24 L150 5 Z" fill="#ffcd00"/></g>'),
    'football': ('<g transform="translate(950 300)"><circle r="170" fill="#f4efe2"/><path d="M0 -60 L57 -18 L35 49 L-35 49 L-57 -18 Z" fill="#1b1b1b"/>'
                 '<g stroke="#1b1b1b" stroke-width="10"><path d="M0 -60 L0 -168 M57 -18 L160 -52 M35 49 L99 137 M-35 49 L-99 137 M-57 -18 L-160 -52"/></g></g>'),
    'pint': ('<g transform="translate(900 120)"><path d="M0 0 L200 0 L180 380 L20 380 Z" fill="#d9921f" opacity=".92"/><path d="M-6 -40 Q20 -80 60 -50 Q100 -90 140 -50 Q180 -80 206 -40 L200 10 L0 10 Z" fill="#f4efe2"/>'
             '<path d="M0 0 L200 0 L180 380 L20 380 Z" fill="none" stroke="#f4efe2" stroke-opacity=".6" stroke-width="6"/></g>'),
}


def chalk_art(sport, icon, uid):
    g = f'{uid}g'
    return (f'<svg viewBox="0 0 1200 630" preserveAspectRatio="xMidYMid meet" aria-hidden="true" focusable="false"><defs><radialGradient id="{g}" cx=".35" cy=".35" r=".9">'
            '<stop offset="0" stop-color="#3a4a40"/><stop offset="1" stop-color="#1c2620"/></radialGradient></defs><rect width="1200" height="630" fill="#5a3a1e"/>'
            f'<rect x="22" y="22" width="1156" height="586" rx="10" fill="url(#{g})"/><g fill="none" stroke="#f4efe2" stroke-opacity=".08" stroke-width="14"><path d="M80 60 q60 40 140 10"/>'
            '<path d="M340 60 q60 40 140 10"/><path d="M600 60 q60 40 140 10"/><path d="M860 60 q60 40 140 10"/></g>' + ICONS.get(icon, ICONS['pint']) +
            '<text x="70" y="140" font-family="Bebas Neue,Impact,sans-serif" font-size="110" fill="#ffcd00" letter-spacing="4">BAR TALK</text>'
            '<text x="74" y="200" font-family="Georgia,serif" font-style="italic" font-size="38" fill="#f4efe2" opacity=".85">from the VAR &amp; Firkin</text>'
            f'<text x="70" y="560" font-family="Bebas Neue,Impact,sans-serif" font-size="96" fill="#f4efe2" letter-spacing="2" textLength="{min(560, 42 * len(sport))}" lengthAdjust="spacingAndGlyphs">{esc(sport.upper())}</text>'
            '<rect x="74" y="580" width="160" height="8" fill="#ffcd00"/></svg>')


def tile_art(question, uid):
    """Make It Make Sense?!: white tiles, a neon sign and the question."""
    lines = kit.wrap(question, 30)[:3]
    q = ''.join(f'<text x="600" y="{400 + 54 * k}" text-anchor="middle" font-family="Georgia,serif" font-style="italic" font-size="44" fill="#1b2a24">{esc(x)}</text>' for k, x in enumerate(lines))
    return (f'<svg viewBox="0 0 1200 630" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false"><defs><pattern id="{uid}t" width="80" height="80" patternUnits="userSpaceOnUse">'
            '<rect width="80" height="80" fill="#eef1ee"/><rect width="80" height="80" fill="none" stroke="#c9d2cd" stroke-width="3"/></pattern>'
            f'<filter id="{uid}n"><feGaussianBlur stdDeviation="6"/></filter></defs><rect width="1200" height="630" fill="url(#{uid}t)"/>'
            '<rect x="0" y="0" width="1200" height="40" fill="#1b2a24"/><rect x="90" y="110" width="1020" height="190" rx="22" fill="#1b2a24"/>'
            f'<g font-family="Bebas Neue,Impact,sans-serif" font-size="120" text-anchor="middle" letter-spacing="6"><text x="600" y="250" fill="#ff3b8d" filter="url(#{uid}n)" opacity=".8">MAKE IT MAKE SENSE?!</text>'
            '<text x="600" y="250" fill="#ffe6f1">MAKE IT MAKE SENSE?!</text></g>' + q + '</svg>')


# ------------------------------------------------------------------ the Bar Talk page
def notes_from_site():
    h = kit.read(BT + 'index.html')
    out = []
    for m in re.finditer(r'<li class="note n\d+" data-cat="([\w-]+)"><a href="([^"]+)"><span class="pin" aria-hidden="true"></span><span class="nl">(.*?) · <i>(.*?)</i></span><h3>(.*?)</h3><p>(.*?)</p><time datetime="([\d-]+)">[^·]*· (\d+) min read</time></a></li>', h):
        out.append({'cat': m.group(1), 'url': m.group(2), 'label': html.unescape(m.group(3)), 'sub': html.unescape(m.group(4)), 'title': html.unescape(m.group(5)),
                    'teaser': html.unescape(m.group(6)), 'date': m.group(7), 'mins': int(m.group(8))})
    return out


def note(q, i):
    return (f'<li class="note n{i % 6}" data-cat="{q["cat"]}"><a href="{q["url"]}"><span class="pin" aria-hidden="true"></span><span class="nl">{esc(q["label"])} · <i>{esc(q["sub"])}</i></span>'
            f'<h3>{esc(q["title"])}</h3><p>{esc(q["teaser"])}</p><time datetime="{q["date"]}">{kit.long_date(q["date"])} · {q["mins"]} min read</time></a></li>')


def render_bartalk(notes, feat_art=None, rant=None):
    h = kit.read(BT + 'index.html')
    h = re.sub(r'(<ul class="notes" id="notes">).*?(</ul>)', lambda m: m.group(1) + ''.join(note(q, i) for i, q in enumerate(notes)) + m.group(2), h, count=1, flags=re.S)
    cats = []
    for q in notes:
        if q['cat'] not in [c[0] for c in cats]:
            cats.append((q['cat'], q['label']))
    cats = sorted([c for c in cats if c[0] != 'make-it-make-sense'], key=lambda c: c[1].lower()) + [c for c in cats if c[0] == 'make-it-make-sense']
    fb = f'<button type="button" class="fb" aria-pressed="true" data-f="all">Everything <span>{len(notes)}</span></button>' + ''.join(
        f'<button type="button" class="fb" aria-pressed="false" data-f="{c}">{esc(l)} <span>{sum(1 for q in notes if q["cat"] == c)}</span></button>' for c, l in cats)
    h = re.sub(r'(<div class="filters" role="group" aria-label="Filter the noticeboard" hidden>).*?(</div>)', lambda m: m.group(1) + fb + m.group(2), h, count=1, flags=re.S)
    if feat_art:   # newest Bar Talk post (not a rant) on the chalkboard
        q = feat_art[0]
        feat = (f'<section class="feat" aria-labelledby="ft-h"><a href="{q["url"]}"><div class="ft-img">{feat_art[1]}<span class="special" aria-hidden="true">Today’s special</span></div>'
                f'<div class="ft-b"><p class="fresh">Fresh on the board</p><p class="ft-cat"><span>{esc(q["label"])}</span> {esc(q["sub"])}</p><h2 id="ft-h">{esc(q["title"])}</h2>'
                f'<p class="ft-t">{esc(q["teaser"])}</p><p class="ft-m"><time datetime="{q["date"]}">{kit.long_date(q["date"])}</time> · {q["mins"]} min read</p><span class="ft-go">Pull up a stool →</span></div></a></section>')
        h = re.sub(r'<section class="feat".*?</section>', lambda m: feat, h, count=1, flags=re.S)
    if rant:
        h = re.sub(r'<span class="door-latest"><small>Latest rant</small>.*?</span>', f'<span class="door-latest"><small>Latest rant</small>{esc(rant)}</span>', h, count=1)
    kit.write(BT + 'index.html', h)
    kit.sitemap_touch(BT, notes[0]['date'])


def related(notes, me_url):
    return ''.join(note(q, i) for i, q in enumerate([q for q in notes if q['url'] != me_url][:2]))


def ask_box(ask):
    return f'<aside class="ask" aria-labelledby="ask-h"><h2 id="ask-h">Over to you</h2><p>{esc(ask)}</p>\n      {TELL}</aside>' if ask else ''


def head(t, p, title, url, desc, section, crumbs, tags, src, mins, series=None):
    ld = {'@context': 'https://schema.org', '@graph': [{
        '@type': 'BlogPosting', '@id': url + '#post', 'headline': title, 'alternativeHeadline': p.get('question') or p['dek'], 'description': desc, 'url': url, 'mainEntityOfPage': url,
        'image': {'@type': 'ImageObject', 'url': url + 'og.jpg', 'width': 1200, 'height': 630}, 'datePublished': p['date'], 'dateModified': p['date'],
        'author': kit.ROB, 'publisher': kit.ROB, 'isPartOf': series or {'@type': 'Blog', '@id': kit.ORIGIN + BT + '#blog', 'name': 'Bar Talk', 'url': kit.ORIGIN + BT},
        'articleSection': section, 'keywords': ', '.join(tags), 'wordCount': kit.words(src), 'timeRequired': f'PT{mins}M', 'inLanguage': 'en-GB'},
        {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': k + 1, 'name': n, 'item': kit.ORIGIN + hh} for k, (n, hh) in enumerate(crumbs)]}]}
    extra = (f'<meta property="article:published_time" content="{p["date"]}">\n<meta property="article:author" content="Rob Callery">\n<meta property="article:section" content="{esc(section)}">\n'
             + ''.join(f'<meta property="article:tag" content="{esc(x)}">\n' for x in tags) + f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n')
    return kit.set_seo(t, kit.seo_block(desc, url, title + (' - Make It Make Sense?! - Rob Callery' if series else ' - Bar Talk - Rob Callery'), url + 'og.jpg', extra=extra),
                       title + (' - Make It Make Sense?! - Rob Callery' if series else ' - Bar Talk - Rob Callery'))


# ------------------------------------------------------------------ a Bar Talk post
def build_post(p, src, title, body):
    slug = p['slug']; path = BT + slug + '/'; url = kit.ORIGIN + path; mins = kit.mins(src)
    notes = [q for q in notes_from_site() if q['url'] != path]
    cat = kit.slugify(p['sport'])
    sub = p.get('sub') or next((q['sub'] for q in notes if q['cat'] == cat), p['sport'])
    t = kit.read(POST_TEMPLATE)
    crumbs = [('Callery.co.uk', '/'), ('The VAR & Firkin', '/var-and-firkin/'), ('Bar Talk', BT), (title, path)]
    t = head(t, p, title, url, p['description'], p['sport'], crumbs, p.get('tags', []), src, mins)
    t = re.sub(r'<li aria-current="page">[^<]*</li></ol></nav>', f'<li aria-current="page">{esc(p["sport"])}</li></ol></nav>', t, count=1)
    board = (f'<header class="board chalk" style="display:block;max-width:none;padding:22px 18px"><span class="mat" aria-hidden="true">{esc(p["sport"])}</span>\n'
             f'    <p class="kick">Bar Talk · {esc(p["sport"])}</p><h1 class="chalk">{esc(title)}</h1>\n    <p class="dek">{esc(p["dek"])}</p>\n'
             f'    <p class="by">By <a href="/">Rob Callery</a> · <time datetime="{p["date"]}">{kit.long_date(p["date"])}</time> · {mins} min read</p></header>')
    t = re.sub(r'<header class="board chalk".*?</header>', lambda m: board, t, count=1, flags=re.S)
    body = re.sub(r'<!--w:[\w-]+-->', '', body)
    paper = f'<div class="paper">\n    <div class="prose">{body}</div>\n    {ask_box(p.get("ask"))}\n    {kit.share(title, url)}\n  </div>'
    t = re.sub(r'<div class="paper">.*?</section>\n  </div>(?=\n  <section class="board-wrap rel")', lambda m: paper, t, count=1, flags=re.S)
    me = {'cat': cat, 'url': path, 'label': p['sport'], 'sub': sub, 'title': title, 'teaser': p['teaser'], 'date': p['date'], 'mins': mins}
    t = re.sub(r'(<section class="board-wrap rel"[^>]*><h2[^>]*>.*?</h2><ul class="notes">).*?(</ul></section>)', lambda m: m.group(1) + related(notes, path) + m.group(2), t, count=1, flags=re.S)
    kit.write(path + 'index.html', t)
    notes.insert(0, me)
    art = chalk_art(p['sport'], p.get('icon', cat), 'ft' + slug.replace('-', '')[:18])
    render_bartalk(notes, (me, art))
    kit.Hub.add({'url': path, 'section': 'Bar Talk', 'date': p['date'], 'title': title, 'kick': p.get('hub_kick', p['sport']), 'teaser': p['teaser'],
                 'standfirst': p['dek'], 'dek': p['description'], 'thumb': chalk_art(p['sport'], p.get('icon', cat), 's' + slug.replace('-', '')[:18]).replace('meet', 'slice', 1)})
    kit.sitemap_add(path, p['date'])
    og = kit.og_card(kit.svg_inner(chalk_art(p['sport'], p.get('icon', cat), 'og')).replace('<text x="70" y="560"', '<text x="70" y="-560"'), None, title,
                     f'Bar Talk · {p["sport"]} · callery.co.uk')
    kit.og_jpg(og, path + 'og.jpg')
    return path


# ------------------------------------------------------------------ a Make It Make Sense?! rant
def rants_from_site():
    """Oldest first, from the toilet-roll menu on the toilets page."""
    h = kit.read(MIMS + 'index.html')
    out = []
    for m in re.finditer(r'<li><a href="(' + re.escape(MIMS) + r'[\w-]+/)"(?: aria-current="page")?><span class="perf" aria-hidden="true">\d+</span>Rant No\. (\d+): (.*?)</a></li>', h):
        q = kit.read(m.group(1) + 'index.html')
        out.append({'url': m.group(1), 'no': int(m.group(2)), 'question': html.unescape(m.group(3)),
                    'title': html.unescape(re.search(r'<h1>(.*?)</h1>', q).group(1)), 'date': re.search(r'<p class="by">.*?datetime="([\d-]+)"', q).group(1)})
    return sorted(out, key=lambda r: r['no'])


def roll(rants, current):
    items = [('/var-and-firkin/', 'Back to the bar'), (BT, 'Bar Talk'), (MIMS, 'The toilets')] + [(r['url'], f'Rant No. {r["no"]}: {r["question"]}') for r in rants]
    return ('<nav class="roll" aria-label="Toilet roll menu"><div class="holder" aria-hidden="true"><span class="bar"></span><span class="tp"></span></div>'
            '<button type="button" class="pull" aria-expanded="false" aria-controls="sheets">Pull for the menu</button><ol class="sheets" id="sheets" hidden>' +
            ''.join(f'<li><a href="{u}"{" aria-current=\"page\"" if u == current else ""}><span class="perf" aria-hidden="true">{k + 1}</span>{esc(n)}</a></li>' for k, (u, n) in enumerate(items)) + '</ol></nav>')


def set_roll(t, rants, current):
    return re.sub(r'<nav class="roll".*?</ol></nav>', lambda m: roll(rants, current), t, count=1, flags=re.S)


def build_rant(p, src, title, body):
    slug = p['slug']; path = MIMS + slug + '/'; url = kit.ORIGIN + path; mins = kit.mins(src)
    rants = [r for r in rants_from_site() if r['url'] != path]
    no = p.get('no') or (max([r['no'] for r in rants] or [0]) + 1)
    toilets = kit.read(MIMS + 'index.html')
    upcoming = [html.unescape(x) for x in re.findall(r'<li>(.*?) <b>Upcoming</b></li>', toilets)]
    upcoming = [u for u in upcoming if u.strip().lower() != p['question'].strip().lower()]
    me = {'url': path, 'no': no, 'question': p['question'], 'title': title, 'date': p['date']}
    rants.append(me); rants.sort(key=lambda r: r['no'])
    prev = next((r for r in reversed(rants) if r['no'] < no), None)

    t = kit.read(RANT_TEMPLATE)
    series = {'@type': 'CreativeWorkSeries', '@id': kit.ORIGIN + MIMS + '#series', 'name': 'Make It Make Sense?!', 'url': kit.ORIGIN + MIMS,
              'isPartOf': {'@type': 'Blog', 'name': 'Bar Talk', 'url': kit.ORIGIN + BT}}
    crumbs = [('Callery.co.uk', '/'), ('The VAR & Firkin', '/var-and-firkin/'), ('Bar Talk', BT), ('Make It Make Sense?!', MIMS), (title, path)]
    t = head(t, p, title, url, p['description'], 'Make It Make Sense?!', crumbs, ['Make It Make Sense', 'Bar Talk', 'Rants'], src, mins, series)
    sheet = (f'<div class="sheet">\n    <p class="f-k"><span>Make it make sense?!</span>Rant No. {no}</p>\n    <h1>{esc(title)}</h1>\n    <p class="q">{esc(p["question"])}</p>\n'
             f'    <p class="by">By <a href="/">Rob Callery</a> · <time datetime="{p["date"]}">{kit.long_date(p["date"])}</time> · {mins} min read · Found on the wall of the VAR &amp; Firkin gents</p>\n'
             f'    <div class="prose">{re.sub(r"<!--w:[\w-]+-->", "", body)}</div>\n    {ask_box(p.get("ask"))}\n    {kit.share(title, url)}\n  </div>')
    t = re.sub(r'<div class="sheet">.*?</section>\n  </div>', lambda m: sheet, t, count=1, flags=re.S)
    pv = (f'<a class="rn prev" href="{prev["url"]}" rel="prev"><small>← Previous rant</small><b>{esc(prev["question"])}</b></a>' if prev
          else '<div class="rn none prev"><small>Previous rant</small><b>This is where it all started.</b></div>')
    nx = f'<div class="rn none next"><small>Next rant · coming soon</small><b>{esc(upcoming[0])}</b></div>' if upcoming else ''
    t = re.sub(r'<nav class="rantnav" aria-label="More rants">.*?</nav>', lambda m: f'<nav class="rantnav" aria-label="More rants">{pv}{nx}</nav>', t, count=1, flags=re.S)
    t = set_roll(t, rants, path)
    kit.write(path + 'index.html', t)

    for r in rants:   # every rant page: menu, and the one before this gets a 'Next rant' link
        if r['url'] == path:
            continue
        q = set_roll(kit.read(r['url'] + 'index.html'), rants, r['url'])
        if prev and r['url'] == prev['url']:
            q = re.sub(r'(<nav class="rantnav" aria-label="More rants">.*?)(<div class="rn none next">.*?</div>|<a class="rn next".*?</a>)?</nav>',
                       lambda m: m.group(1) + f'<a class="rn next" href="{path}" rel="next"><small>Next rant →</small><b>{esc(p["question"])}</b></a></nav>', q, count=1, flags=re.S)
        kit.write(r['url'] + 'index.html', q)

    # the toilets page: newest rant featured, older ones listed, the question crossed off 'coming soon'
    feat = (f'<article class="feature" aria-labelledby="f-h"><p class="f-k"><span>Latest rant</span>No. {no}</p><h2 id="f-h"><a href="{path}">{esc(title)}</a></h2>'
            f'<p class="f-q">{esc(p["question"])}</p><p class="f-p">{esc(p["teaser"])}</p><p class="f-meta"><time datetime="{p["date"]}">{kit.long_date(p["date"])}</time> · {mins} min read</p>'
            f'<a class="f-go" href="{path}">Read the full rant →</a>' + (f'<p class="f-scrawl" aria-hidden="true">{esc(p["scrawl"])}</p>' if p.get('scrawl') else '') + '</article>')
    older = ''.join(f'<li><a href="{r["url"]}">{esc(r["title"])}</a></li>' for r in reversed(rants) if r['url'] != path)
    if older:
        feat += f'<section class="soon" aria-labelledby="old-h"><h2 id="old-h">Earlier on the wall</h2><ul>{older}</ul></section>'
    toilets = re.sub(r'<div class="wall"><div>.*?</div>(?=<section class="soon" aria-labelledby="soon-h">)', lambda m: f'<div class="wall"><div>{feat}</div>', toilets, count=1, flags=re.S)
    toilets = re.sub(r'(<section class="soon" aria-labelledby="soon-h">.*?<ul>).*?(</ul></section>)', lambda m: m.group(1) + ''.join(f'<li>{esc(u)} <b>Upcoming</b></li>' for u in upcoming) + m.group(2), toilets, count=1, flags=re.S)
    toilets = set_roll(toilets, rants, MIMS)
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', toilets, re.S)
    if m:
        ld = json.loads(m.group(1)); ld['@graph'][0]['hasPart'] = [{'@type': 'BlogPosting', 'headline': r['title'], 'url': kit.ORIGIN + r['url']} for r in reversed(rants)]
        toilets = toilets[:m.start(1)] + json.dumps(ld, ensure_ascii=False) + toilets[m.end(1):]
    kit.write(MIMS + 'index.html', toilets)

    notes = [q for q in notes_from_site() if q['url'] != path]
    notes.insert(0, {'cat': 'make-it-make-sense', 'url': path, 'label': 'The gents', 'sub': 'Thoughts from the gents', 'title': title, 'teaser': p['teaser'], 'date': p['date'], 'mins': mins})
    render_bartalk(notes, rant=p['question'])
    kit.Hub.add({'url': path, 'section': 'Bar Talk', 'date': p['date'], 'title': title, 'kick': 'Make It Make Sense?!', 'teaser': p['teaser'],
                 'standfirst': p['question'], 'dek': p['description'], 'thumb': tile_art(p['question'], 's' + slug.replace('-', '')[:18])})
    kit.sitemap_add(path, p['date']); kit.sitemap_touch(MIMS, p['date'])
    og = kit.og_card(kit.svg_inner(tile_art('', 'og')), None, title, 'Make It Make Sense?! · callery.co.uk')
    kit.og_jpg(og, path + 'og.jpg')
    return path


def build(folder):
    p = json.load(open(os.path.join(folder, 'post.json'), encoding='utf-8'))
    src = open(os.path.join(folder, 'post.md'), encoding='utf-8').read()
    title, body, _ = kit.md(src, ul_class='facts')
    p['date'] = kit.iso(p['date'])
    path = (build_rant if p.get('rant') else build_post)(p, src, title, body)
    print('Bar Talk written:', path)
    return path


if __name__ == '__main__':
    build(sys.argv[1])
