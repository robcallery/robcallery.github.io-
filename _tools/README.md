# Blog post tools for callery.co.uk

These scripts add posts (Football Tales, Travel Tales, Calz Plays, Bar Talk and Make It Make Sense?!) straight into the published site files in this repo. They live in `_tools/`,
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

## Bar Talk and Make It Make Sense?!: `python3 _tools/bartalk.py _tools/posts/<folder>`

A Bar Talk post (`/var-and-firkin/bar-talk/<slug>/`):

```json
{"slug": "kick-off-times", "date": "2026-11-21", "sport": "Football", "sub": "Kick-off times and other crimes",
 "icon": "football", "tags": ["Football", "TV"], "dek": "...", "teaser": "...", "description": "...",
 "ask": "the 'Over to you' question"}
```

- `sport` is the category (Cricket, Darts, Football…). `sub` is the italic line on its noticeboard pin; only needed for a new category.
- `icon` draws the chalkboard art: `cricket`, `darts`, `football` or `pint` (the default).

A rant in the toilets (`/var-and-firkin/bar-talk/make-it-make-sense/<slug>/`):

```json
{"rant": true, "slug": "printer-ink-racket", "date": "2026-11-22",
 "question": "Why does printer ink cost more than the printer?", "teaser": "...", "description": "...",
 "ask": "the 'Over to you' question", "scrawl": "graffiti under the latest rant"}
```

- The rant is numbered automatically, the previous rant gets a "Next rant" link, the toilet-roll menu on every rant
  is updated, and if the question was on the "coming soon" list it is crossed off.
- Either kind updates the Bar Talk page: a Bar Talk post goes on the chalkboard as today's special, a rant goes on the gents door.

## If the Chronicle gets out of step

If `/blog/index.html` is ever edited by hand, refresh the data from it with:
`python3 -c "import sys; sys.path.insert(0,'_tools'); import kit; kit.save('hub', kit.Hub.parse())"`

Fonts in `fonts/` are from Google Fonts under the SIL Open Font License (`OFL.txt`), used to draw share images.

## calz88 Live (`/live/`)

No script needed: edit two small JSON files and push.

**Upcoming streams** — `live/schedule.json`. Times in UTC (`Z`) or with an offset; the page shows UK time, plus the
visitor's own time if they're somewhere else. Past streams drop off by themselves (4 hours after `start`, or at `end`).

```json
{"streams": [
  {"title": "FC 27 Saturday session", "start": "2026-11-28T19:00:00Z", "end": "2026-11-28T22:00:00Z",
   "category": "Gaming", "description": "One line about it.", "link": "https://www.twitch.tv/robcallery"}
]}
```

`category` is one of `Gaming`, `Football`, `VAR & Firkin` or `Special event` (anything else shows as written).
`end`, `description` and `link` are optional.

**Highlights** — `live/highlights.json`, newest first, up to 8 shown.

```json
{"highlights": [
  {"title": "...", "date": "2026-11-20", "platform": "YouTube", "url": "https://www.youtube.com/watch?v=...",
   "thumb": "/live/thumbs/my-video.jpg"}
]}
```

Thumbnails must be files on this site (a path starting with `/`), so the page never loads images from YouTube or
Twitch before anyone clicks. Without a `thumb` the card shows a plain branded panel.

**Live status** comes from the Worker at `/api/live`, which asks Twitch's API. It needs two Worker secrets, set in the
Cloudflare dashboard (Workers & Pages → callery → Settings → Variables and Secrets, type "Secret"):
`TWITCH_CLIENT_ID` and `TWITCH_CLIENT_SECRET`, from an application registered at dev.twitch.tv/console.
Without them the page says "Status unavailable" and the stream still works.
