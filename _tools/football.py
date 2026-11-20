#!/usr/bin/env python3
"""Add a Football Tale (match report) to callery.co.uk.

    python3 _tools/football.py posts/<folder>          # folder holds post.md + post.json (see README)

Builds /football-tales/<slug>/ from the newest match card, then updates the album, the previous card's
'Next card' link, the Callery Chronicle, the home page newsstand, the sitemap and the share image.
"""
import os, re, sys, json, html, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kit
from kit import esc

BASE = '/football-tales/'
LEEDS = {'name': 'Leeds United', 'short': 'LEE'}
WJ = '⁠'   # word joiner: keeps "1–0" together in headlines


# ------------------------------------------------------------------ kits
def board_kit(kit_, side):
    t = kit_[0]
    if t == 'stripes':
        return f'repeating-linear-gradient(90deg,{kit_[1]} 0 25%,{kit_[2]} 25% 50%)'
    main, t1, t2 = kit_[1], kit_[2], kit_[3]
    if side == 'home':
        return f'linear-gradient(90deg,{t2} 0 20%,{t1} 20% 40%,{main} 40%)'
    return f'linear-gradient(90deg,{main} 0 60%,{t1} 60% 80%,{t2} 80%)'


def card_half(kit_, side):
    x0 = 18 if side == 'home' else 120
    if kit_[0] == 'stripes':
        return ''.join(f'<rect x="{x0 + 17 * k:.1f}" y="44" width="17.0" height="196" fill="{kit_[1 + k % 2]}"/>' for k in range(6))
    main, t1, t2 = kit_[1], kit_[2], kit_[3]
    if side == 'home':
        return (f'<rect x="18" y="44" width="102" height="196" fill="{main}"/><rect x="110" y="44" width="4" height="196" fill="{t2}"/>'
                f'<rect x="114" y="44" width="6" height="196" fill="{t1}"/>')
    return (f'<rect x="120" y="44" width="102" height="196" fill="{main}"/><rect x="120" y="44" width="6" height="196" fill="{t1}"/>'
            f'<rect x="126" y="44" width="4" height="196" fill="{t2}"/>')


def main_colour(kit_):
    return kit_[1]


def ink_colour(kit_):
    """A readable colour to write on the kit's main colour."""
    if kit_[0] == 'stripes':
        return '#ffffff'
    c = kit_[1].lstrip('#'); r, g, b = (int(c[i:i + 2], 16) for i in (0, 2, 4))
    light = (0.299 * r + 0.587 * g + 0.114 * b) > 150
    return kit_[2] if light else '#ffffff'


# ------------------------------------------------------------------ pictures
def card_svg(p, no):
    h, a, sc = p['home'], p['away'], p['score']
    home_game = p['kind'] == 'home'
    frame, band, bandtxt = ('#ffcd00', '#ffcd00', '#1d428a') if home_game else ('#1d428a', '#1d428a', '#ffcd00')
    star = p['star']['first'] + ' ' + p['star']['last']
    return (f'<svg viewBox="0 0 240 336" role="img" aria-label="Card {no}: {esc(h["name"])} {sc[0]}-{sc[1]} {esc(a["name"])}"><defs><clipPath id="pic{200 + no}">'
            '<rect x="18" y="44" width="204" height="196" rx="6"/></clipPath></defs><rect x="2" y="2" width="236" height="332" rx="14" fill="#ffffff" stroke="#d8d2c2" stroke-width="1.5"/>'
            f'<rect x="10" y="10" width="220" height="316" rx="10" fill="{frame}"/><g clip-path="url(#pic{200 + no})">{card_half(h["kit"], "home")}{card_half(a["kit"], "away")}'
            '<path d="M18 200 Q120 170 222 200 L222 240 L18 240 Z" fill="#2f7d32"/><path d="M18 214 Q120 186 222 214" stroke="#ffffff" stroke-width="1.5" fill="none" opacity=".6"/>'
            '<rect x="18" y="44" width="204" height="196" fill="url(#none)" opacity="0"/></g><rect x="62" y="110" width="116" height="64" rx="8" fill="#0a1838" stroke="#ffffff" stroke-width="3"/>'
            f'<text x="120" y="160" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="48" fill="#ffcd00" textLength="86" lengthAdjust="spacingAndGlyphs">{sc[0]} – {sc[1]}</text>'
            f'<rect x="26" y="74" width="54" height="22" rx="4" fill="#0a1838"/><text x="53" y="91" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="18" fill="#ffffff">{esc(h["short"])}</text>'
            f'<rect x="160" y="74" width="54" height="22" rx="4" fill="#0a1838"/><text x="187" y="91" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="18" fill="#ffffff">{esc(a["short"])}</text>'
            f'<rect x="10" y="10" width="220" height="30" fill="{band}"/><text x="120" y="32" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="19" fill="{bandtxt}" letter-spacing="2">SEASON {p["season"]} MD{p["matchday"]}</text>'
            '<rect x="18" y="246" width="204" height="72" rx="6" fill="#ffffff"/>'
            f'<text x="120" y="270" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="21" fill="#0a1838" letter-spacing="1" textLength="190" lengthAdjust="spacingAndGlyphs">{esc(h["name"].upper())} V {esc(a["name"].upper())}</text>'
            f'<text x="120" y="288" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="10.5" fill="#4a5570">{esc(p["venue"])} · {kit.short_date(p["date"])}</text>'
            f'<text x="120" y="308" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="13" fill="#1d428a" letter-spacing="1.5" textLength="186" lengthAdjust="spacingAndGlyphs">STAR MAN: {esc(star.upper())}</text></svg>')


def leeds_kit(p):
    return p['home']['kit'] if p['home']['name'] == 'Leeds United' else p['away']['kit']


def star_art(p):
    s, k = p['star'], leeds_kit(p)
    fill = k[1]; stroke = k[2] if k[0] == 'plain' else '#1d428a'
    if fill.lower() == stroke.lower():
        stroke = '#ffffff'
    stripes = ''.join(f'<rect x="0" y="{y}" width="204" height="14" fill="#2a8243"/>' for y in range(0, 196, 28))
    return ('<svg viewBox="0 0 204 196" aria-hidden="true" focusable="false" preserveAspectRatio="xMidYMid slice"><rect width="204" height="196" fill="#2f8f4a"/>' + stripes +
            '<g fill="none" stroke="#fff" stroke-opacity=".6" stroke-width="2"><rect x="8" y="8" width="188" height="180"/><line x1="102" y1="8" x2="102" y2="188"/><circle cx="102" cy="98" r="26"/>'
            '<rect x="8" y="58" width="30" height="80"/><rect x="166" y="58" width="30" height="80"/></g><g transform="translate(102 70)">'
            f'<path d="M-26 -18 L-12 -26 Q0 -20 12 -26 L26 -18 L20 -2 L14 -6 L14 26 L-14 26 L-14 -6 L-20 -2 Z" fill="{fill}" stroke="{stroke}" stroke-width="3"/></g>'
            f'<text x="102" y="150" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="52" fill="#fff">{esc(s["big"])}</text>'
            f'<text x="102" y="172" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="16" letter-spacing="3" fill="#ffcd00">{esc(s["caption"].upper())}</text></svg>')


def star_card(p):
    s = p['star']
    stats = ''.join(f'<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>' for k, v in s['stats'])
    return (f'<aside class="tcard" aria-labelledby="sm-h"><div class="tc-in"><p class="tc-top"><span>Star man</span><span>MD{p["matchday"]}</span></p>'
            f'<div class="tc-art">{star_art(p)}<span class="tc-no" aria-hidden="true"></span></div>'
            f'<h2 class="tc-name" id="sm-h"><span class="vh">Star man: </span><small>{esc(s["first"])}</small>{esc(s["last"])}</h2>'
            f'<p class="tc-pos">{esc(s["pos"])} · Leeds United</p><dl class="tc-stats">{stats}</dl><p class="tc-line">{esc(s["line"])}</p></div></aside>')


def thumb_svg(p, no):
    """Chronicle thumbnail (1200x630)."""
    h, a, sc = p['home'], p['away'], p['score']
    gid = f'ft{no}g'
    return (f'<svg viewBox="0 0 1200 630" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false"><defs><linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="#0a1838"/><stop offset="1" stop-color="#1d428a"/></linearGradient></defs><rect width="1200" height="630" fill="url(#{gid})"/>'
            '<rect x="1020" y="0" width="60" height="630" fill="#ffffff" opacity=".9"/><rect x="1080" y="0" width="60" height="630" fill="#ffcd00" opacity=".9"/><rect x="1140" y="0" width="60" height="630" fill="#1d428a" opacity=".9"/>'
            '<rect x="40" y="40" width="330" height="62" rx="6" fill="#ffcd00"/><text x="205" y="86" text-anchor="middle" font-family="Bebas Neue,Impact,sans-serif" font-size="46" letter-spacing="4" fill="#0a1838" textLength="290" lengthAdjust="spacingAndGlyphs">FOOTBALL TALES</text>'
            f'<text x="980" y="86" text-anchor="end" font-family="Bebas Neue,Impact,sans-serif" font-size="44" letter-spacing="4" fill="#ffcd00">CARD {no}</text><g font-family="Bebas Neue,Impact,sans-serif" text-anchor="middle">'
            f'<rect x="60" y="190" width="260" height="230" rx="14" fill="{main_colour(h["kit"])}"/><text x="190" y="352" font-size="130" fill="{ink_colour(h["kit"])}" textLength="190" lengthAdjust="spacingAndGlyphs">{esc(h["short"])}</text>'
            f'<rect x="680" y="190" width="260" height="230" rx="14" fill="{main_colour(a["kit"])}"/><text x="810" y="352" font-size="130" fill="{ink_colour(a["kit"])}" textLength="190" lengthAdjust="spacingAndGlyphs">{esc(a["short"])}</text>'
            f'<text x="500" y="360" font-size="170" fill="#fff" textLength="230" lengthAdjust="spacingAndGlyphs">{sc[0]}–{sc[1]}</text></g>'
            f'<text x="60" y="560" font-family="Inter,sans-serif" font-weight="800" font-size="40" fill="#fff">{esc(p["venue"])}</text></svg>')


def og_svg(p, no, title):
    h, a, sc = p['home'], p['away'], p['score']
    def panel(x, k, short, side):
        trim = ''
        if k[0] == 'plain':
            trim = (f'<rect x="{x + 300}" y="110" width="12" height="200" fill="{k[3]}"/><rect x="{x + 312}" y="110" width="8" height="200" fill="{k[2]}"/>' if side == 'home'
                    else f'<rect x="{x}" y="110" width="12" height="200" fill="{k[2]}"/><rect x="{x + 12}" y="110" width="8" height="200" fill="{k[3]}"/>')
            body = f'<rect x="{x}" y="110" width="320" height="200" rx="14" fill="{k[1]}"/>'
        else:
            body = f'<clipPath id="og{side}"><rect x="{x}" y="110" width="320" height="200" rx="14"/></clipPath><g clip-path="url(#og{side})">' + ''.join(
                f'<rect x="{x + 40 * i}" y="110" width="40" height="200" fill="{k[1 + i % 2]}"/>' for i in range(8)) + '</g>'
        lx = x + 160 if side == 'home' else x + 160
        return body + trim + f'<rect x="{lx - 70}" y="236" width="140" height="56" rx="8" fill="#0a1838"/><text x="{lx}" y="280" text-anchor="middle" font-family="Bebas Neue,Impact,sans-serif" font-size="44" fill="#fff" letter-spacing="2">{esc(short)}</text>'
    t = kit.wrap(title, 36)[:2]
    lines = ''.join(f'<text x="44" y="{470 + 66 * k}" font-family="Inter,sans-serif" font-weight="800" font-size="56" fill="#fff">{esc(x)}</text>' for k, x in enumerate(t))
    sub = f'{p["competition"]} · {kit.short_date(p["date"])} · callery.co.uk'.upper()
    return ('<svg viewBox="0 0 1200 630" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a1838"/>'
            '<stop offset="1" stop-color="#0b1a3e"/></linearGradient></defs><rect width="1200" height="630" fill="url(#bg)"/><rect width="1200" height="12" fill="#ffcd00"/>'
            '<text x="44" y="78" font-family="Bebas Neue,Impact,sans-serif" font-size="44" letter-spacing="4" fill="#ffcd00">FOOTBALL TALES</text>'
            f'<text x="1156" y="78" text-anchor="end" font-family="Bebas Neue,Impact,sans-serif" font-size="44" letter-spacing="4" fill="#fff">CARD NO. {no}</text>'
            + panel(80, h['kit'], h['short'], 'home') + panel(800, a['kit'], a['short'], 'away') +
            '<rect x="440" y="120" width="320" height="180" rx="18" fill="#0a1838" stroke="#fff" stroke-width="6"/>'
            f'<text x="600" y="262" text-anchor="middle" font-family="Bebas Neue,Impact,sans-serif" font-size="170" fill="#ffcd00">{sc[0]}–{sc[1]}</text>'
            f'{lines}<text x="44" y="{470 + 66 * len(t) + 10}" font-family="Bebas Neue,Impact,sans-serif" font-size="34" letter-spacing="3" fill="#ffcd00">{esc(sub)}</text></svg>')


# ------------------------------------------------------------------ album data
def album_cards():
    """Every card on the album page, oldest first, read straight from the published page."""
    h = kit.read(BASE + 'index.html')
    cards = []
    for m in re.finditer(r'<div class="slot" data-kind="(\w+)"><a class="flip" href="([^"]+)" aria-label="Card (\d+): (.*?)">\s*<div class="f">(<svg.*?</svg>)</div><div class="b"><div class="back-in"><div class="bno">(.*?)</div><p class="tease">(.*?)</p>(.*?)<span class="read">', h, re.S):
        cards.append({'kind': m.group(1), 'url': m.group(2), 'no': int(m.group(3)), 'title': html.unescape(m.group(4)), 'svg': m.group(5),
                      'bno': m.group(6), 'tease': m.group(7), 'rows': m.group(8)})
    tl = {m.group(1): (m.group(2), m.group(3)) for m in re.finditer(r'<li><a href="([^"]+)"><span class="tl-no">No\. \d+</span><span class="tl-k">(.*?)</span><b>.*?</b><time datetime="([\d-]+)">', h)}
    for c in cards:
        c['kicker'], c['date'] = tl.get(c['url'], ('', ''))
    return sorted(cards, key=lambda c: c['no'])


def render_album(cards):
    h = kit.read(BASE + 'index.html')
    n = len(cards); total = max(8, (n // 4 + 1) * 4)
    slots = ''.join(f'<div class="slot" data-kind="{c["kind"]}"><a class="flip" href="{c["url"]}" aria-label="Card {c["no"]}: {esc(c["title"])}">\n'
                    f'      <div class="f">{c["svg"]}</div><div class="b"><div class="back-in"><div class="bno">{c["bno"]}</div><p class="tease">{c["tease"]}</p>{c["rows"]}<span class="read">Read the tale →</span></div></div></a></div>'
                    for c in reversed(cards))
    slots += ''.join(f'<div class="slot empty"><div class="ghost"><span class="gno">{k}</span><span class="gtxt">Got, got, need</span><span class="gsoon">Space for card {k}</span></div></div>' for k in range(n + 1, total + 1))
    h = re.sub(r'<div class="grid">.*?</div>\n    <p class="none"', lambda m: f'<div class="grid">{slots}</div>\n    <p class="none"', h, count=1, flags=re.S)
    h = re.sub(r'<p class="count">\d+ of \d+ cards collected</p>', f'<p class="count">{n} of {total} cards collected</p>', h)
    tales = ''.join(f'<li><a href="{c["url"]}"><span class="tl-no">No. {c["no"]}</span><span class="tl-k">{c["kicker"]}</span><b>{esc(c["title"])}</b><time datetime="{c["date"]}">{kit.short_date(c["date"])}</time></a></li>' for c in reversed(cards))
    h = re.sub(r'(<section class="tales"[^>]*>\s*<h2[^>]*>.*?</h2>\s*<ol>).*?(</ol>)', lambda m: m.group(1) + tales + m.group(2), h, count=1, flags=re.S)
    kit.write(BASE + 'index.html', h)


# ------------------------------------------------------------------ the post
def build(folder, dry=False):
    p = json.load(open(os.path.join(folder, 'post.json'), encoding='utf-8'))
    src = open(os.path.join(folder, 'post.md'), encoding='utf-8').read()
    title, body, heads = kit.md(src)
    p['date'] = kit.iso(p['date'])
    h, a, sc = p['home'], p['away'], p['score']
    p.setdefault('slug', f'{kit.slugify(h["short"] if False else h["name"].split()[0])}-{sc[0]}-{sc[1]}-{kit.slugify(a["name"].split()[0])}-{p["date"]}')
    slug = p['slug']; url = kit.ORIGIN + BASE + slug + '/'
    cards = album_cards()
    if any(c['url'] == BASE + slug + '/' for c in cards):
        cards = [c for c in cards if c['url'] != BASE + slug + '/']
    no = p.get('card') or (max([c['no'] for c in cards] or [0]) + 1)
    prev = max([c for c in cards if c['no'] < no], key=lambda c: c['no'], default=None)
    kicker = p.get('kicker') or ('Home day' if p['kind'] == 'home' else 'Away day')
    title_disp = re.sub(r'(\d)\s*–\s*(\d)', lambda m: m.group(1) + WJ + '–' + WJ + m.group(2), title)

    # template: the newest match report (it has a scoreboard)
    tpl_url = next(c['url'] for c in reversed(cards) if c['kind'] in ('home', 'away'))
    t = kit.read(tpl_url + 'index.html')

    # head
    desc = p['description']
    t = kit.set_seo(t, kit.seo_block(desc, url, p.get('og_title', title) + ' - Football Tales - Rob Callery', url + 'og.jpg'), f'{title} - Football Tales - Rob Callery')
    # programme bar
    t = re.sub(r'<span>Card No\. \d+</span></p>', f'<span>Card No. {no}</span></p>', t, count=1)
    # scoreboard
    stats = ''
    for lab, x, y in p.get('stats', []):
        nx = float(str(x).rstrip('%')); ny = float(str(y).rstrip('%'))
        w = 50 if nx + ny == 0 else round(nx / (nx + ny) * 100)
        stats += f'<div class="stat"><div class="v">{x}–{y}</div><div class="l">{esc(lab)}</div><div class="bar"><span style="width:{w}%"></span><span style="width:{100 - w}%"></span></div></div>'
    meta = f'{p["competition"]} · {kit.day_date(p["date"])} · {esc(p["venue"])}' + (f' · Attendance: {p["attendance"]}' if p.get('attendance') else '') + (f'<br>{esc(p["scorers"])}' if p.get('scorers') else '')
    board = (f'<div class="board" role="img" aria-label="Full time: {esc(h["name"])} {sc[0]}, {esc(a["name"])} {sc[1]}">\n'
             f'    <div class="top"><span>{esc(p["competition"].upper())}</span><span>FULL TIME</span></div>\n    <div class="score">\n'
             f'      <div class="team"><i style="background:{board_kit(h["kit"], "home")}"></i><span class="ln">{esc(h["name"])}</span><span class="sn">{esc(h["short"])}</span></div>\n'
             f'      <div class="nums"><b>{sc[0]}</b><em>–</em><b>{sc[1]}</b></div>\n'
             f'      <div class="team a"><span class="ln">{esc(a["name"])}</span><span class="sn">{esc(a["short"])}</span><i style="background:{board_kit(a["kit"], "away")}"></i></div>\n'
             f'    </div>\n    <div class="meta">{meta}</div>\n    <div class="stats">{stats}</div>\n  </div>')
    t = re.sub(r'<div class="board".*?</div>\n  </div>', lambda m: board, t, count=1, flags=re.S)
    # ticket + album card
    att = f'<div><dt>Attendance</dt><dd>{esc(p["attendance"])}</dd></div>' if p.get('attendance') else ''
    csvg = card_svg(p, no)
    scrap = (f'<div class="scrap" aria-label="From the scrapbook"><figure class="ticket" aria-labelledby="tk-h"><div class="tk-main"><p class="tk-top"><span>{esc(p["competition"])}</span>'
             f'<span>Season {p["season"]} · Matchday {p["matchday"]}</span></p><h2 class="tk-fix" id="tk-h"><span>{esc(h["name"])}</span> <i>v</i> <span>{esc(a["name"])}</span></h2>'
             f'<dl class="tk-dl"><div><dt>Date</dt><dd>{kit.day_date(p["date"])}</dd></div><div><dt>Venue</dt><dd>{esc(p["venue"])}</dd></div>'
             f'<div><dt>Full time</dt><dd class="tk-score">{esc(h["short"])} {sc[0]}–{sc[1]} {esc(a["short"])}</dd></div>{att}</dl></div>'
             f'<div class="tk-stub" aria-label="Football Tales card number {no}"><span class="tk-k">Football Tales</span><b>No. {no}</b><span class="tk-k">Card</span><span class="tk-bar" aria-hidden="true"></span></div>'
             f'<span class="tape t1" aria-hidden="true"></span><span class="tape t2" aria-hidden="true"></span></figure><div class="scrapcard"><a href="/football-tales/" aria-label="Card {no} in the Football Tales album">{csvg}</a>'
             '<span class="tape t3" aria-hidden="true"></span></div></div>')
    t = re.sub(r'<div class="scrap" aria-label="From the scrapbook">.*?<span class="tape t3" aria-hidden="true"></span></div></div>', lambda m: scrap, t, count=1, flags=re.S)
    # the story
    body = re.sub(r'(<h2 id="[^"]+">Star man[^<]*</h2>)', lambda m: m.group(1) + star_card(p), body, count=1) if p.get('star') else body
    body = re.sub(r'<h2 id="([^"]+)">My verdict[:–-]\s*(.*?)</h2>', r'<h2 class="verdict" id="my-verdict"><span class="vk">My verdict</span><span class="vh">: </span><span class="vt">\2</span></h2>', body, count=1)
    srcs = ''.join(f'<li><a href="{esc(u)}" target="_blank" rel="noopener">{esc(n)}</a></li>' for n, u in p.get('sources', []))
    story = (f'<div class="story paper">\n    <p class="kicker"><span>Match report</span>{esc(kicker)}</p>\n    <h1>{esc(title_disp, False)}</h1>\n'
             f'    <p class="by">By Rob Callery · <time datetime="{p["date"]}">{kit.day_date(p["date"])}</time> · {esc(p["venue"])}</p>\n    {body}\n'
             f'    <p class="mot">{esc(p.get("sign_off", "Marching On Together."))}</p>\n'
             + (f'    <details class="srcfold"><summary>Sources for the match facts</summary><ul>{srcs}</ul></details>\n' if srcs else '') + '  </div>')
    t = re.sub(r'<div class="story paper">.*?\n  </div>\n  <nav class="cardnav"', lambda m: story + '\n  <nav class="cardnav"', t, count=1, flags=re.S)
    # card to card
    pv = (f'<a class="cn-tile cn-prev" href="{prev["url"]}" rel="prev"><span class="cn-k"><span aria-hidden="true">← </span>Previous card</span>'
          f'<span class="cn-no">No. {prev["no"]} · {prev["kicker"]}</span><b>{esc(prev["title"])}</b></a>') if prev else '<div class="cn-tile cn-none"><span class="cn-k">Previous card</span><span>The first card in the album.</span></div>'
    nav = (f'<nav class="cardnav" aria-label="Card to card">{pv}<a class="cn-album" href="/football-tales/">Back to the album</a>'
           '<div class="cn-tile cn-none"><span class="cn-k">Next card</span><span>The newest card in the album.</span></div></nav>')
    t = re.sub(r'<nav class="cardnav".*?</nav>', lambda m: nav, t, count=1, flags=re.S)
    kit.write(BASE + slug + '/index.html', t)

    # the previous card now points here
    if prev:
        q = kit.read(prev['url'] + 'index.html')
        nxt = (f'<a class="cn-tile cn-next" href="{BASE}{slug}/" rel="next"><span class="cn-k">Next card<span aria-hidden="true"> →</span></span>'
               f'<span class="cn-no">No. {no} · {esc(kicker)}</span><b>{esc(title)}</b></a>')
        q = re.sub(r'(<a class="cn-album"[^>]*>[^<]*</a>)(<div class="cn-tile cn-none">.*?</div>|<a class="cn-tile cn-next".*?</a>)', lambda m: m.group(1) + nxt, q, count=1, flags=re.S)
        kit.write(prev['url'] + 'index.html', q)

    # the album
    rows = ''.join(f'<div class="srow"><span>{esc(lab)}</span><b>{x} – {y}</b></div>' for lab, x, y in p.get('stats', [])[:4])
    cards.append({'kind': p['kind'], 'url': BASE + slug + '/', 'no': no, 'title': title, 'svg': csvg, 'bno': f'No. {no}', 'tease': esc(p['teaser']),
                  'rows': rows, 'kicker': kicker, 'date': p['date']})
    render_album(sorted(cards, key=lambda c: c['no']))

    # Chronicle, newsstand, sitemap, share image
    kit.Hub.add({'url': BASE + slug + '/', 'section': 'Football Tales', 'date': p['date'], 'title': title, 'kick': p.get('hub_kick', 'Leeds United' if p['kind'] == 'home' else 'Away day'),
                 'teaser': p['teaser'], 'standfirst': p.get('standfirst', p['teaser']), 'dek': desc, 'thumb': thumb_svg(p, no)})
    newsstand(BASE + slug + '/', title, p.get('board') or kit.wrap(title.upper(), 11)[:3])
    kit.sitemap_add(BASE + slug + '/', p['date']); kit.sitemap_touch(BASE, p['date'])
    kit.og_jpg(og_svg(p, no, title), BASE + slug + '/og.jpg')
    print('Football Tale', no, 'written:', BASE + slug + '/')
    return BASE + slug + '/'


def newsstand(url, title, lines):
    h = kit.read('index.html')
    i = h.index('<!-- newsstand -->'); j = h.index('</a>', i)
    s = h[i:j]
    s = re.sub(r'<a href="[^"]+" class="egg newsegg" tabindex="-1" aria-label="[^"]*"', f'<a href="{url}" class="egg newsegg" tabindex="-1" aria-label="Latest Football Tale: {esc(title)}"', s, count=1)
    k = iter((lines + ['', '', ''])[:3])
    s = re.sub(r'(<text x="-26" y="-(?:44|33|22)"[^>]*>)[^<]*(</text>)', lambda m: m.group(1) + esc(next(k)) + m.group(2), s)
    kit.write('index.html', h[:i] + s + h[j:])


if __name__ == '__main__':
    build(sys.argv[1])
