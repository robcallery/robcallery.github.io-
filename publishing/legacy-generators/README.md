# Legacy generators (snapshot, 21 October 2026)

These are the Python scripts that currently generate callery.co.uk. They were written and run
in a Claude working session and are saved here **unchanged** so nothing is lost. They are the
starting point for the publishing system described in `../PUBLISHING_PLAN.md`.

> They will not run as-is from this folder. They contain absolute paths from the original
> working session (`/home/claude/...` and a temporary scratchpad folder). Making them runnable
> from the repo is Phase 0 of the plan.

## What's here

| Folder | Contents |
|---|---|
| `site/` | Page generators: `guide.py` (Travel Guides page), `passport.py` (Beer Passport, also supplies the shared book template that `guide.py` reuses), `hub.py` (Explore hub + Football Tales), `seo.py` (meta tags, sitemap, robots), `build_snaps.py` (bundles polaroids into `snaps.js`), `regions.py` (UK region grouping and ordering for `guides.js`), `publish_guides.sh` (build + check + push) |
| `polaroids/` | `snaplib.py` (drawing helpers) and `snaps1.py` … `snaps13.py` (one SVG scene per destination, with title and "Did you know?" fact). `sheet.py` renders a contact sheet of all polaroids |
| `data-imports/` | One-off scripts that added data: beer batches (`batch3.py`, `fest.py`, `epcot.py`), guide batches (`places4.py`, `r_yorkshire.py`, `r_northeast.py`, `r_northwest.py`, `r_scotwales.py`, `r_midlands.py`, `r_east.py`, `r_southeast.py`, `r_southwest.py`) and early place lists (`new_places.js`, `london.js`) |
| `qa/` | Playwright checks and screenshot helpers (overflow checks at 1280×800, 1024×640, 390×844, 1366×650) |
| `home-page-and-misc/` | One-off patches to the home page scene, Starting Soon page and experiments (season decorations, weather, fixtures, etc.). Kept for reference |

## Data these scripts produce

- `travel-guides/guides.js` – `window.GUIDES`, one object per destination
- `travel-guides/snaps.js` – `window.SNAPS`, keyed by city: `{ t: title, n: fact, svg: "<svg…>" }`
- `beer-passport/beers.js` – `window.BEERS`

The published data files on `main` are the source of truth. These scripts are how they were made.
