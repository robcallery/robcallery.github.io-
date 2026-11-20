# Blog post tools for callery.co.uk

These scripts add posts straight into the published site files in this repo. They live in `_tools/`,
which `.assetsignore` keeps off the website. Run them from the repo root, then commit and push to `main`;
Cloudflare rebuilds the site on every push.

Each post is a folder (keep drafts in `_tools/posts/<name>/`) holding:

- `post.md`: the words, as Rob writes them. `# Title`, `## Heading`, a whole line in `**bold**` becomes a
  pull quote, a whole line in `*italics*` becomes an aside, `- ` lists, `---` a rule, and three or more short
  lines in a row (28 characters or fewer) become a "beats" block. `[text](https://link)` makes a link.
- `post.json`: the facts (below), plus any photos, video or screenshot it names.

Every tool also updates the Callery Chronicle (`/blog/`, from `data/hub.json`), `sitemap.xml` and the share image.

## Football Tales: `python3 _tools/football.py _tools/posts/<folder>`

```json
{"date": "2026-11-22", "competition": "Premier League", "season": "26/27", "matchday": 12,
 "venue": "Turf Moor", "attendance": "21,500", "kind": "away",
 "home": {"name": "Burnley", "short": "BUR", "kit": ["plain", "#6c1d45", "#99d6ea", "#ffffff"]},
 "away": {"name": "Leeds United", "short": "LEE", "kit": ["plain", "#ffcd00", "#1d428a", "#ffcd00"]},
 "score": [1, 2], "scorers": "Foster 30' · Piroe 55', Okafor 88'",
 "slug": "burnley-1-2-leeds-2026-11-22",
 "stats": [["Shots", 9, 14], ["On target", 3, 6], ["Possession", "44%", "56%"], ["Bookings", 2, 1]],
 "teaser": "one line for the album card and the Chronicle",
 "description": "one or two sentences for Google and shares",
 "star": {"first": "Joe", "last": "Rodon", "pos": "Defender",
          "stats": [["Clearances", "9"], ["Duels won", "7"], ["Result", "1–2"]],
          "line": "one line under the card", "big": "9", "caption": "Clearances"},
 "sources": [["101 Great Goals: Burnley 1-2 Leeds", "https://..."]],
 "board": ["THREE", "SHORT", "LINES"]}
```

- `kit` is `["plain", main, trim, trim2]` or `["stripes", colour1, colour2]`. Leeds: home `["plain","#ffffff","#1d428a","#ffcd00"]`, yellow away `["plain","#ffcd00","#1d428a","#ffcd00"]`.
- `kind` is `home` or `away`. In `post.md`, put `## Star man: Name` where the star-man card goes and finish with `## My verdict: one line`.
- `board` is the three-line headline on the home page newsstand. Optional: `kicker` ("Home day"), `og_title`, `sign_off`, `hub_kick`.

## Travel Tales: `python3 _tools/travel.py _tools/posts/<folder>`

```json
{"slug": "kennedy-space-center", "date": "2026-11-21", "place": "Cape Canaveral", "country": "Florida, USA",
 "label": "Days out", "tags": ["Kennedy Space Center", "Florida"],
 "dek": "the line under the headline", "teaser": "one line for cards",
 "description": "one or two sentences for Google and shares",
 "photos": [{"file": "IMG_1234.jpg", "caption": "handwritten caption"}],
 "video": {"file": "IMG_1235.MOV", "caption": "what's in the clip", "keep_sound": false},
 "referral": {"head": "Get $10 off", "line": "...", "url": "https://...", "code": "ABC", "button": "Get the app", "icon": "🚕"},
 "verdict": "Would I Do It Again?",
 "reading": [["Page title", "Site name", "https://..."]]}
```

- In `post.md`, `[[photo1]]`, `[[photo2]]`… place photos, `[[video]]` the clip, `[[referral]]` the referral box.
- Photos are resized and saved **without their location data**; videos are muted (unless `keep_sound`) and stripped too.
- A heading `## The Verdict – …`, or the one named in `verdict`, gets the dark verdict panel.

## Calz Plays (gaming): `python3 _tools/gaming.py _tools/posts/<folder>`

```json
{"slug": "gta-vi-first-weekend", "date": "2026-11-21", "categories": ["GTA VI"], "game": "Grand Theft Auto VI",
 "tags": ["GTA VI", "Vice City"], "dek": "...", "teaser": "...", "description": "...",
 "screenshot": "my-grab.png", "caption": "My own grab from the first night",
 "ask": ["Question for readers?"], "sign_off": "Marching On Together.",
 "new_categories": {"Racing": {"colour": "#ffd23b", "tag": "a line about the category"}}}
```

- The monitor art is Rob's `screenshot` if given (location data removed), otherwise the art from the
  newest earlier post in the same category. `new_categories` is only needed for a category that doesn't exist yet.

## If the Chronicle gets out of step

If `/blog/index.html` is ever edited by hand, refresh the data from it with:
`python3 -c "import sys; sys.path.insert(0,'_tools'); import kit; kit.save('hub', kit.Hub.parse())"`

Fonts in `fonts/` are from Google Fonts under the SIL Open Font License (`OFL.txt`), used to draw share images.
