#!/usr/bin/env python3
"""Add a Travel Tale to callery.co.uk.

    python3 _tools/travel.py posts/<folder>        # post.md + post.json (+ any photos / video named in post.json)

Builds /travel-tales/<slug>/ in the airmail-postcard style, then updates the Travel Tales page, the Callery
Chronicle, the sitemap and the share image. Photos and videos are resized and have their location data removed.
In post.md: [[video]] places the video, [[photo1]], [[photo2]]... place photos, [[referral]] places a referral box.
"""
import os, re, sys, json, html, shutil, subprocess, base64
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kit
from kit import esc

BASE = '/travel-tales/'
TEMPLATE = BASE + 'waymo-ojai-driverless-taxi-orlando/index.html'   # has every Travel Tales style (video, referral)


def stampdate(d):
    x = kit.dt(d); return f'{x.day} {x:%b %Y}'.upper()


def postmark(place, country, date):
    return f'''<svg class="pm" viewBox="0 0 220 140" role="img" aria-label="Postmarked {esc(place)}, {esc(country)}, {esc(date)}">
<defs><path id="pt" d="M34 70a36 36 0 0 1 72 0"/><path id="pb" d="M30 70a40 40 0 0 0 80 0"/></defs>
<g fill="none" stroke="#1f4fa3" stroke-width="2.4" opacity=".85"><circle cx="70" cy="70" r="52"/><circle cx="70" cy="70" r="44" stroke-width="1.2"/>
<path d="M126 46c12-8 24 8 36 0s24 8 36 0M126 62c12-8 24 8 36 0s24 8 36 0M126 78c12-8 24 8 36 0s24 8 36 0M126 94c12-8 24 8 36 0s24 8 36 0"/></g>
<g fill="#1f4fa3" opacity=".9" font-family="Inter,sans-serif" font-weight="800" text-anchor="middle">
<text font-size="11" letter-spacing="2"><textPath href="#pt" startOffset="50%">{esc(place.upper())}</textPath></text>
<text font-size="9" letter-spacing="1.5"><textPath href="#pb" startOffset="50%">{esc(country.upper())}</textPath></text>
<text x="70" y="75" font-size="12">{esc(date)}</text></g></svg>'''


def headline(t):
    m = re.match(r'(.+?[!?:])\s+(.+)', t)
    return f'<span class="hand">{esc(m.group(1))}</span>{esc(m.group(2))}' if m else esc(t)


def stamp(p):
    perf = ''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="#eaf7fc"/>' for x in range(6, 120, 12) for y in (2, 168)) + \
           ''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="#eaf7fc"/>' for y in range(14, 160, 12) for x in (2, 118))
    return (f'<svg viewBox="0 0 120 170"><rect x="2" y="2" width="116" height="166" fill="#fffdf6"/>{perf}'
            '<rect x="12" y="12" width="96" height="146" fill="#11618f"/><rect x="12" y="104" width="96" height="54" fill="#0b3a5c"/>'
            '<circle cx="82" cy="40" r="14" fill="#ffd86b"/><path d="M12 104 q24 -14 48 0 t48 0 v4 H12z" fill="#3bd1ff" opacity=".7"/>'
            '<path d="M30 70 l40 -10 l8 3 l-30 12 l-6 12 l-5 1 l1 -11 l-10 3 l-4 6 l-4 0 l2 -9z" fill="#fff"/>'
            f'<text x="60" y="128" text-anchor="middle" font-family="Bebas Neue,Impact,sans-serif" font-size="15" fill="#fff" letter-spacing="1" textLength="84" lengthAdjust="spacingAndGlyphs">{esc(p["place"].upper())}</text>'
            f'<text x="60" y="146" text-anchor="middle" font-family="Inter,sans-serif" font-weight="800" font-size="8" fill="#9fe3fb" letter-spacing="1.5">{esc(p["country"].upper())}</text></svg>')


def og_art(p, link=False):
    poster = p.get('poster')
    img = ''
    if poster:
        src = f'{BASE}{p["slug"]}/{poster}' if link else 'data:image/jpeg;base64,' + base64.b64encode(open(os.path.join(kit.ROOT, BASE.strip('/'), p['slug'], poster), 'rb').read()).decode()
        img = (f'<image href="{src}" x="-100" y="-300" width="1400" height="1240" preserveAspectRatio="xMidYMid slice" opacity=".55"/>'
               f'<rect x="806" y="28" width="330" height="574" rx="18" fill="#fffdf6"/><image href="{src}" x="818" y="40" width="306" height="550" preserveAspectRatio="xMidYMid slice"/>')
    pid = 'air' + kit.slugify(p['slug'])[:12].replace('-', '')
    return (f'<svg viewBox="0 0 1200 630" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><defs><pattern id="{pid}" width="48" height="48" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)">'
            f'<rect width="16" height="48" fill="#d6343a"/><rect x="24" width="16" height="48" fill="#1f4fa3"/></pattern></defs>'
            f'<rect width="1200" height="630" fill="#0b3a5c"/>{img}<rect width="1200" height="14" fill="url(#{pid})"/><rect y="616" width="1200" height="14" fill="url(#{pid})"/>'
            f'<text x="44" y="96" font-family="Bebas Neue,Impact,sans-serif" font-size="58" fill="#3bd1ff" letter-spacing="3">TRAVEL TALES</text>'
            f'<text x="46" y="140" font-family="Inter,sans-serif" font-weight="800" font-size="28" fill="#fff">{esc(p["place"])} · {esc(p["country"])}</text></svg>')


# ------------------------------------------------------------------ media (location data always removed)
def photo(src, out, width=1600):
    from PIL import Image, ImageOps
    im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(out, 'JPEG', quality=84, optimize=True, progressive=True)   # saved without EXIF: no GPS, no phone details
    return im.size


def video(src, outdir, name, keep_sound=False):
    a = ['-c:a', 'aac', '-b:a', '128k'] if keep_sound else ['-an']
    mp4, webm, poster = (os.path.join(outdir, name + x) for x in ('.mp4', '.webm', '-poster.jpg'))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-map', '0:v:0'] + (['-map', '0:a:0?'] if keep_sound else []) + a +
                   ['-map_metadata', '-1', '-map_chapters', '-1', '-vf', 'scale=720:-2,fps=30', '-c:v', 'libx264', '-profile:v', 'high', '-pix_fmt', 'yuv420p',
                    '-crf', '25', '-preset', 'slow', '-movflags', '+faststart', mp4], check=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', mp4] + (['-c:a', 'libopus'] if keep_sound else ['-an']) +
                   ['-map_metadata', '-1', '-c:v', 'libvpx-vp9', '-b:v', '0', '-crf', '36', '-row-mt', '1', '-deadline', 'good', '-cpu-used', '3', webm], check=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', '3', '-i', mp4, '-frames:v', '1', '-q:v', '3', poster], check=True)
    return name + '.mp4', name + '.webm', name + '-poster.jpg'


PHOTO_CSS = ('.snap{margin:1.6em auto;max-width:560px;background:#fff;padding:10px 10px 8px;border-radius:4px;box-shadow:0 10px 26px rgba(10,40,70,.2);transform:rotate(-1deg)}'
             '.snap:nth-of-type(even){transform:rotate(1deg)}.snap img{display:block;width:100%;height:auto;border-radius:2px}'
             '.snap figcaption{margin-top:8px;font-family:Caveat,cursive;font-weight:700;font-size:1.25rem;line-height:1.2;color:var(--deep);text-align:center}')


def build(folder):
    p = json.load(open(os.path.join(folder, 'post.json'), encoding='utf-8'))
    src = open(os.path.join(folder, 'post.md'), encoding='utf-8').read()
    title, body, _ = kit.md(src, ul_class='facts')
    p['date'] = kit.iso(p['date']); slug = p['slug']; url = kit.ORIGIN + BASE + slug + '/'
    outdir = os.path.join(kit.ROOT, BASE.strip('/'), slug); os.makedirs(outdir, exist_ok=True)
    mins = kit.mins(src)

    # media
    if p.get('video'):
        v = p['video']
        mp4, webm, poster = video(os.path.join(folder, v['file']), outdir, v.get('name', slug.split('-')[0]), v.get('keep_sound', False))
        p['poster'] = p.get('poster') or poster
        clip = (f'<figure class="clip"><div class="phone"><video poster="{poster}" muted autoplay loop playsinline controls preload="metadata" aria-label="{esc(v["caption"])}">'
                f'<source src="{mp4}" type="video/mp4"><source src="{webm}" type="video/webm"></video></div><figcaption>{esc(v["caption"])}'
                f'<small>Filmed by Rob · {"sound on" if v.get("keep_sound") else "sound off"}</small></figcaption></figure>')
        body = body.replace('<!--w:video-->', clip)
    for k, ph in enumerate(p.get('photos', []), 1):
        name = ph.get('name', f'photo{k}.jpg')
        w, hh = photo(os.path.join(folder, ph['file']), os.path.join(outdir, name))
        p.setdefault('poster', name)
        fig = (f'<figure class="snap"><img src="{name}" alt="{esc(ph.get("alt", ph.get("caption", "")))}" width="{w}" height="{hh}" loading="lazy">'
               + (f'<figcaption>{esc(ph["caption"])}</figcaption>' if ph.get('caption') else '') + '</figure>')
        body = body.replace(f'<!--w:photo{k}-->', fig)
    if p.get('referral'):
        r = p['referral']
        body = body.replace('<!--w:referral-->', (
            f'<aside class="ref" aria-labelledby="ref-h"><span class="ref-ic" aria-hidden="true">{r.get("icon", "🎟️")}</span><div><h2 id="ref-h">{esc(r["head"])}</h2><p>{esc(r["line"])}</p>'
            f'<div class="ref-row"><a class="ref-go" href="{esc(r["url"])}" target="_blank" rel="noopener sponsored">{esc(r.get("button", "Get the app"))}<span class="vh"> (opens in a new tab)</span></a>'
            + (f'<button type="button" class="ref-code" data-code="{esc(r["code"])}" aria-label="Copy code {esc(r["code"])}"><span>Code</span><b>{esc(r["code"])}</b></button>' if r.get('code') else '')
            + '<span class="ref-ok" role="status" aria-live="polite"></span></div>'
            f'<p class="ref-small">{esc(r.get("note", "This is my own referral link."))}</p></div></aside>'))
    body = re.sub(r'<!--w:[\w-]+-->', '', body)
    if p.get('verdict'):
        body = re.sub(r'<h2 id="([^"]+)">' + re.escape(esc(p['verdict'], False)) + '</h2>',
                      lambda m: f'<h2 class="verdict" id="{m.group(1)}"><span class="vk">The verdict</span>{esc(p["verdict"])}</h2>', body, count=1)
    body = re.sub(r'<h2 id="([^"]+)">The Verdict\s*[–:-]\s*(.*?)</h2>', r'<h2 class="verdict" id="\1"><span class="vk">The verdict</span>\2</h2>', body, count=1)

    t = kit.read(TEMPLATE)
    tags = p.get('tags', [])
    crumbs = [('Callery.co.uk', '/'), ('The Callery Chronicle', '/blog/'), ('Travel Tales', BASE), (p['place'], None)]
    ld = {'@context': 'https://schema.org', '@graph': [{
        '@type': 'BlogPosting', '@id': url + '#post', 'headline': title, 'alternativeHeadline': p['dek'], 'description': p['description'], 'url': url, 'mainEntityOfPage': url,
        'image': {'@type': 'ImageObject', 'url': url + 'og.jpg', 'width': 1200, 'height': 630}, 'datePublished': p['date'], 'dateModified': p['date'],
        'author': kit.ROB, 'publisher': kit.ROB, 'isPartOf': {'@type': 'Blog', '@id': kit.ORIGIN + BASE + '#blog', 'name': 'Travel Tales', 'url': kit.ORIGIN + BASE},
        'articleSection': 'Travel', 'keywords': ', '.join(tags), 'wordCount': kit.words(src), 'timeRequired': f'PT{mins}M', 'inLanguage': 'en-GB'},
        {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': k + 1, 'name': n, 'item': kit.ORIGIN + (hh or BASE + slug + '/')} for k, (n, hh) in enumerate(crumbs)]}]}
    extra = (f'<meta property="article:published_time" content="{p["date"]}">\n<meta property="article:author" content="Rob Callery">\n<meta property="article:section" content="Travel">\n'
             + ''.join(f'<meta property="article:tag" content="{esc(x)}">\n' for x in tags) + f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n')
    t = kit.set_seo(t, kit.seo_block(p['description'], url, f'{title} - Travel Tales - Rob Callery', url + 'og.jpg', extra=extra), f'{title} - Travel Tales - Rob Callery')
    if 'class="snap"' in body and '.snap{' not in t:
        t = t.replace('</style>', PHOTO_CSS + '</style>', 1)
    t = re.sub(r'<li aria-current="page">[^<]*</li></ol></nav>', f'<li aria-current="page">{esc(p["place"])}</li></ol></nav>', t, count=1)
    head = (f'<p class="kick">Travel Tales <span>{esc(p["label"])}</span></p><h1>{headline(title)}</h1>\n    <p class="dek">{esc(p["dek"])}</p>\n'
            f'    <p class="by">By <a href="/">Rob Callery</a> · <time datetime="{p["date"]}">{kit.long_date(p["date"])}</time> · {mins} min read</p></div>\n    '
            + postmark(p['place'], p['country'], stampdate(p['date'])))
    t = re.sub(r'<p class="kick">Travel Tales.*?</svg>(?=</div></div></header>)', lambda m: head, t, count=1, flags=re.S)
    reading = ''.join(f'<li><a href="{esc(u)}" target="_blank" rel="noopener">{esc(n)}</a> <span>{esc(s)}</span></li>' for n, s, u in p.get('reading', []))
    paper = (f'<div class="prose">{body}</div>\n    '
             + (f'<section class="read" aria-labelledby="rd-h"><h2 id="rd-h">Further reading</h2><ul>{reading}</ul></section>\n    ' if reading else '')
             + kit.share(title, url) + '\n  </div>')
    t = re.sub(r'<div class="prose">.*?</section>\n  </div>(?=\n  <nav class="wayout")', lambda m: paper, t, count=1, flags=re.S)
    if not p.get('referral'):
        t = re.sub(r"<script>document\.querySelectorAll\('\.ref-code'\).*?</script>", '', t, count=1, flags=re.S)
    kit.write(BASE + slug + '/index.html', t)

    # Travel Tales page: new card on top
    L = kit.read(BASE + 'index.html')
    art = (f'<img src="{slug}/{esc(p["poster"])}" alt="" loading="lazy" width="120" height="170">' if p.get('poster') else f'<span class="stamp" aria-hidden="true">{stamp(p)}</span>')
    card = (f'<li class="pc"><a href="{BASE}{slug}/">{art}<div><p class="k">{esc(p["place"])} · {esc(p["label"])}</p><b>{esc(title)}</b><p>{esc(p["teaser"])}</p>'
            f'<time datetime="{p["date"]}">{kit.long_date(p["date"])}</time></div></a></li>')
    L = re.sub(r'<li class="pc"><a href="' + re.escape(BASE + slug + '/') + r'">.*?</li>', '', L, flags=re.S)
    L = L.replace('<ul class="cards">', '<ul class="cards">' + card, 1)
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', L, re.S)
    ldl = json.loads(m.group(1)); g = ldl['@graph'][0]
    g['blogPost'] = [{'@type': 'BlogPosting', 'headline': title, 'url': url, 'datePublished': p['date']}] + [b for b in g.get('blogPost', []) if b['url'] != url]
    L = L[:m.start(1)] + json.dumps(ldl, ensure_ascii=False) + L[m.end(1):]
    kit.write(BASE + 'index.html', L)

    kit.Hub.add({'url': BASE + slug + '/', 'section': 'Travel Tales', 'date': p['date'], 'title': title, 'kick': p['label'], 'teaser': p['teaser'],
                 'standfirst': p['dek'], 'dek': p['description'], 'thumb': og_art(p, link=True)})
    kit.sitemap_add(BASE + slug + '/', p['date']); kit.sitemap_touch(BASE, p['date'])
    kit.og_jpg(og_art(p), BASE + slug + '/og.jpg')
    print('Travel Tale written:', BASE + slug + '/')
    return BASE + slug + '/'


if __name__ == '__main__':
    build(sys.argv[1])
