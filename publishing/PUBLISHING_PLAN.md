# Travel Guides publishing system: technical plan

*Draft 2, 21 October 2026. Plan only: nothing here changes the live website.*

*Draft 2 corrects the 8.25" × 11" paperback availability, confirms the hardcover page range and adds KDP UK printing costs for each option (section 3).*

## 1. Goals

Publish four editions from the same destination data that powers callery.co.uk/travel-guides:

| # | Edition | Format | Channel |
|---|---|---|---|
| 1 | Collector's Edition | Large-format, full-colour hardback (paperback optional) | Amazon KDP |
| 2 | Traveller's Edition | Smaller, portable colour paperback | Amazon KDP |
| 3 | Apple Books edition | Fixed-layout EPUB 3 | Apple Books |
| 4 | Kindle edition | Kindle-compatible ebook | Amazon KDP |

Every build selects destinations by **country**, **UK region**, **custom collection** or a hand-picked list, instead of always exporting all 207.

Ground rules:

- The website keeps working exactly as it does today. Publishing never pushes to the website.
- One source of truth: `guides.js` + `snaps.js` (and `beers.js` for cross-references).
- Every release is reproducible. It records exactly which data commit it was built from.

## 2. Where things stand today

- **Site:** static HTML/CSS/JS on GitHub Pages, deployed automatically from `main` ("pages build and deployment"). No build step runs in the repo.
- **Data:** `travel-guides/guides.js` has 207 destinations, grouped as 11 UK regions, then 7 countries, then Airports. `travel-guides/snaps.js` has one polaroid per destination: inline SVG (about 1.9MB, about 190KB gzipped), plus a title and a "Did you know?" fact.
- **Rendering:** `travel-guides/index.html` builds the pages in the browser: cover, contents, then for each destination a guide page (left) and a polaroid page (right).
- **Generators:** Python scripts, now saved under `publishing/legacy-generators/` on the `publishing` branch. They contain absolute paths from the original working session.
- **Fonts:** Inter, Bebas Neue, Caveat, DM Serif Display and Space Mono, loaded from Google Fonts.

## 3. Recommended KDP trim sizes

KDP specifications checked October 2026 (Paper and Trim Size Options, Print Options). Re-check before each release, because KDP changes them.

### Collector's Edition: 8.25" × 11" hardcover, premium colour

- 8.25" × 11" is KDP's largest hardcover trim, and hardcover is premium colour only.
- It gives about 60% more page area than the Traveller's Edition. That leaves room for the bigger layout described in section 4.
- **Paperback option:** KDP also offers **8.25" × 11" as a premium colour paperback** (24–590 pages). One layout and one interior PDF can therefore serve both the hardcover and a paperback; only the covers differ.
- **Page range:** hardcover premium colour is 75–550 pages; paperback premium colour at this size is 24–590.
- **Bleed:** yes. The hero bands and polaroid backgrounds run to the edge.
- **Page size with bleed:** 8.375" × 11.25".

### Traveller's Edition: 6" × 9" paperback, standard colour

- 6" × 9" is a 2:3 ratio, very close to the current web page ratio (about 0.70). The existing two-page design moves over with the fewest changes.
- The same 2:3 ratio is used for the fixed-layout EPUB, so one page design serves both.
- **Standard colour** (72–600 pages) is much cheaper per page than premium colour. That matters for a 400-plus-page book people will carry around. The polaroids are flat colour, which prints well on standard colour.
- **Page size with bleed:** 6.125" × 9.25".
- **Not recommended:** 5.5" × 8.5" is more pocketable, but at 400+ pages the gutter alone is 0.625", and the guide page text would drop below a comfortable 8pt. Revisit it only for small regional volumes.

### Page counts drive cost

The full guide is 207 destinations × 2 pages plus front and back matter. With region divider spreads (which also keep every destination on a left/right pair) it comes to roughly **430–476 pages**.

KDP UK paperback printing cost is a fixed £0.85 plus a cost per page (KDP *Printing costs* page, checked 21 October 2026). "Large" means wider than 6.12" or taller than 9". The KDP royalty on a paperback is 60% of list price minus printing, so the break-even list price is printing cost ÷ 0.6.

| Book | Trim and ink | Per page | Print cost (476 pp) | Break-even list price |
|---|---|---|---|---|
| Collector's, full guide | 8.25" × 11" premium colour (large) | £0.0598 | **about £29.31** | about £48.85 |
| Traveller's, full guide | 6" × 9" standard colour (regular) | £0.020 | **about £10.37** | about £17.28 |
| Traveller's, full guide | 5.5" × 8.5" premium colour (regular) | £0.0435 | about £21.56 | about £35.93 |
| Traveller's, *Yorkshire* (33 places, about 82 pp) | 6" × 9" standard colour | £0.020 | about £2.49 | about £4.15 |

Hardcover printing costs are on a separate KDP page and need checking before pricing the Collector's hardback. Standard colour is the main reason the Traveller's Edition is 6" × 9": the same 476-page book costs about half as much to print as in premium colour. The quality trade-off has to be judged on a proof copy.

Two recommendations:

1. **Plan regional volumes,** for example "Yorkshire" (33 destinations, about 82 pages) or "North of England" (66 destinations, about 150 pages). The full Collector's Edition becomes a flagship rather than the only product.
2. **Use a compact layout for the Traveller's Edition** (section 4.3), which roughly halves the page count.

Check every selection against the format's minimum page count:

| Format | Page range |
|---|---|
| Standard colour paperback | 72–600 |
| Premium colour paperback | 24–828; 24–590 at 8.5" × 11" |
| Hardcover (premium colour, incl. 8.25" × 11") | 75–550 |

**Gutter margins by page count:** these follow KDP's table.

| Page count | Inside margin |
|---|---|
| 24–150 | 0.375" |
| 151–300 | 0.5" |
| 301–500 | 0.625" |
| 501–700 | 0.75" |

With bleed, the top, bottom and outside margins must be at least 0.375". The pipeline sets the margins automatically from the final page count.

## 4. How the two-page layout adapts

### 4.1 The rule that carries across every format

Each destination is a **spread**: the guide page on the left (verso, even page number) and the polaroid page on the right (recto). This is the website's layout and the book's signature.

The pipeline enforces it. Front matter, region dividers and any filler pages are counted so that every destination starts on a verso page. If a section would break the pattern, a "Notes" page is inserted, which is what the website already does.

### 4.2 Collector's Edition (8.25" × 11")

**Guide page (verso):**
- A full-bleed colour band for the hero, with a larger skyline.
- The pint / local beer / best-for strip is set as large tiles.
- "Where to drink" becomes two columns, with the Spoons badge kept.
- New space for:
  - a small locator map (UK or country outline with a pin);
  - "Beers I had here", pulled from `beers.js` by matching `city`;
  - visited date and rating;
  - the handwritten tip, set larger.

**Polaroid page (recto):**
- A large polaroid, about 75% of the page width, taped and slightly rotated as on the site.
- Below it, the caption and "Did you know?".
- A ruled "My notes" area and an empty passport-stamp circle for readers to fill in. This makes it a collector's piece.

**Section dividers:** each region or country opens with a divider spread. The left page has the region name and a mini contents list. The right page is a full-bleed illustration, such as a collage of that region's polaroids.

**Extras:**
- A cover built from a polaroid collage.
- Endpapers showing the world logo.
- An index of pubs, with every Spoons and bar listed alphabetically with page numbers.

### 4.3 Traveller's Edition (6" × 9")

**Spread mode (default):** this is almost the website page as-is.
- Body text at 8.5–9pt Inter and section labels at 6.5pt.
- The polaroid takes about 85% of the recto width, with "Did you know?" below it.
- Text that is too long for the smaller page is caught by the overflow check (section 7). It is then shortened through optional `print` overrides in the data, without changing what the website says.

**Compact mode (optional):** one page per destination, roughly halving the page count.
- The polaroid shrinks to a thumbnail, about 40% width, in the hero corner.
- Practical sections are kept: drink, eat, getting there, tip.
- "Don't miss", football and the long fact are dropped.
- This is the right choice for a true pocket guide or a cheap regional book.

**Practical extras:**
- A thumb-index colour tab on the outer edge per region. It is in the bleed, so it shows on the page edge.
- A fold-out-style region map at the front.
- Running heads showing the region.

### 4.4 Apple Books: fixed-layout EPUB 3

- **Page size:** each page is its own XHTML document with a fixed viewport of **1200 × 1800** (2:3, the same design as the Traveller's Edition).
- **Package settings:** `rendition:layout = pre-paginated` and `rendition:spread = auto`.
- **Spine:** the guide page carries `page-spread-left` and the polaroid page `page-spread-right`. In landscape on iPad or Mac, readers see exactly the website spread. In portrait they see one page at a time.
- **Fonts:** embedded, with `ibooks:specified-fonts = true` so Apple Books keeps the typography.
- **Polaroids:** stay as inline SVG, which is crisp at any zoom. Each gets a text alternative (title plus fact) for accessibility.
- **Contents:** the contents pages become a real navigation document, with tappable links per destination, plus the EPUB's own table of contents.
- **No JavaScript:** none is needed and none is used. That keeps the book simple to approve.

### 4.5 Kindle edition

Kindle's fixed-layout support is limited:
- KDP no longer accepts MOBI for fixed-layout books (from March 2025).
- Fixed layout on Kindle is mainly for comics and children's books via Kindle Create.
- Print Replica (from a PDF) doesn't display on all Kindle devices.

**Recommendation: a reflowable Kindle EPUB, built from the same data.**
- One chapter per destination. The polaroid appears at the top as a raster image (PNG, 1600px on the long edge), followed by the title and region.
- The "at a glance" tiles become a short definition list, followed by drink (with the Spoons badge as a small inline label), eat, don't miss, football, getting there, and the tip.
- The tip is styled in Caveat. Readers who override fonts still see it in italics.
- Chapters are grouped into parts by region or country. The navigation document mirrors the contents.
- Upload to KDP as EPUB. Validate first in **Kindle Previewer**, which runs on Mac or Windows, so this is a manual step on your computer.

**Optional later:** a Print Replica edition made from the Traveller's PDF using Kindle Create. It is only for tablets and apps, so it should not be the main Kindle edition.

## 5. Architecture

```
publishing/
  PUBLISHING_PLAN.md            this document
  legacy-generators/            today's scripts (snapshot, unchanged)
  pyproject.toml                pinned Python deps (jinja2, pyyaml, jsonschema, playwright, pypdf, pillow, cairosvg)
  callery_publish/              the build tool (Python package)
    extract.py                  guides.js / snaps.js / beers.js -> normalised JSON (runs Node to read the JS)
    schema/destination.json     JSON Schema for one destination
    select.py                   manifest -> ordered list of destinations
    layout/                     page planning: spreads, dividers, parity, front/back matter
    render_pdf.py               HTML+CSS (Paged.js) -> Chromium PDF via Playwright
    render_epub_fxl.py          fixed-layout EPUB 3
    render_kindle.py            reflowable EPUB for KDP
    covers.py                   wraparound cover PDF from KDP spine width
    preflight.py                print + EPUB checks, HTML QA report
  templates/
    collector/                  page templates + CSS (@page sizes, bleeds)
    traveller/
    epub-fxl/
    kindle/
  fonts/                        vendored OFL font files + OFL.txt (pinned versions)
  collections/                  custom collection definitions (YAML)
  editions/                     release manifests (YAML), one per book
  build/                        output (git-ignored)
```

### 5.1 Single source, normalised

`extract.py` loads the three JS files with Node, exactly as the site does, and writes `build/data/destinations.json`. Each destination gets:

- a stable `id` (a slug, e.g. `newcastle-upon-tyne`);
- its existing fields;
- its polaroid SVG, saved separately as `build/data/snaps/<id>.svg`;
- any beers from the passport whose `city` matches.

It is validated against a JSON Schema: required fields, text length limits per format, no duplicate cities, and polaroids present.

**Proposed data additions.** These are optional and backwards-compatible, and the website ignores them:

| Field | Purpose |
|---|---|
| `id` | Stable slug, so books don't break if a display name changes |
| `lastVerified` | e.g. `"2026-10"`, the date the pubs and facts were last checked. Printed on the copyright page as "information correct at" |
| `sources` | Where the pub details came from, for re-checking before a new edition |
| `collections` | Tags such as `"florida-2015"` or `"leeds-away-days"` |
| `print` | Per-format overrides, e.g. a shorter `dontMiss` for the Traveller's Edition, or `exclude: true` |

### 5.2 Selecting destinations

Custom collections live in `collections/*.yml`:

```yaml
# collections/leeds-away-days.yml
title: Leeds Away Days
description: Every ground I've followed Leeds to
cities: [Sunderland, Middlesbrough, Hull, Sheffield, Barnsley, ...]
```

A release manifest describes one book:

```yaml
# editions/travellers-yorkshire-2027.yml
edition: traveller            # collector | traveller | epub-fxl | kindle
layout: spread                # spread | compact
title: "Rob Callery's Travel Guides"
subtitle: "Yorkshire"
series: { name: "One Beer at a Time", number: 1 }
select:
  groups: [Yorkshire]         # UK regions or 'Airports'
  countries: []               # e.g. [Japan, United States]
  collections: []             # e.g. [leeds-away-days]
  include: []                 # extra cities
  exclude: []                 # cities to drop
order: as-site                # as-site | alphabetical | custom list
frontmatter: [title, copyright, how-to-use, contents, region-map]
backmatter: [pub-index, notes]
data_commit: 5497b67          # pinned source data (set by the release job)
identifiers: { isbn: "978-…", asin: null }
version: 1.0.0
```

The tool lists what it selected and the projected page count, and warns before rendering if the result falls outside the format's page limits.

### 5.3 Rendering

**Print PDF**
- The page templates are HTML+CSS, using Jinja2 with the same visual language as the site.
- They are laid out with **Paged.js** in headless **Chromium** (Playwright, which the QA scripts already use).
- CSS paged media handles:
  - the trim size and bleed (`@page { size; bleed }`);
  - left and right page margins, so the gutter is always on the spine side;
  - running heads and page numbers;
  - contents page numbers filled in automatically.
- Chromium writes a PDF with embedded, subsetted fonts, and the SVG polaroids stay as vectors.

**Post-processing**
- Ghostscript flattens transparency (the polaroids use opacity) and normalises the PDF.
- qpdf checks the result for structural problems.
- An optional proof PDF in CMYK is produced for viewing only (section 6.3).

**Covers**
- `covers.py` builds the wraparound cover PDF: back, spine and front, with bleed.
- The spine width comes from the final page count and paper type, taken from KDP's cover calculator.
- The spine text is suppressed if the book is too thin for it (KDP requires more than 79 pages for spine text).
- The ISBN barcode area is left clear on the back, because KDP adds the barcode.

**Fixed-layout EPUB**
- One XHTML per page, from the same templates at the 1200 × 1800 viewport.
- A navigation document and the OPF package file are written with the fixed-layout and accessibility metadata. The fonts and SVGs are packaged with it.
- It is validated with **epubcheck**.

**Kindle EPUB**
- A reflowable XHTML chapter per destination.
- The polaroids are rasterised to PNG via cairosvg or Chromium, in sRGB.
- It is validated with epubcheck, then Kindle Previewer (manual step).

**QA report**
- Every build writes `build/<release>/report.html`, containing:
  - page thumbnails;
  - the overflow list;
  - the preflight results;
  - page count and spine width;
  - a diff of which destinations changed since the last release.

## 6. Quality, licensing, images, metadata

### 6.1 Print-quality checks (automated, in `preflight.py`)

**Geometry**
- The page size exactly equals trim plus bleed on every page.
- The page count is even and within KDP's range for the format.
- The gutter margin matches the page-count table.
- No text or important artwork is inside the 0.375" safe zone.
- No crop marks. KDP rejects files that have them.

**Layout**
- Every page is rendered and measured for text overflow or clipping. This uses the same technique as today's Playwright checks, at print size.
- Every destination spread lands verso then recto.
- No widowed section headings.
- Page numbers in the contents match the actual pages.

**Fonts**
- All fonts are embedded and subsetted, and there are no Type 3 fonts (checked with `pdffonts`).
- The smallest text is at least 6.5pt, and body text at least 8.5pt.

**Artwork**
- Strokes in the SVGs are at least 0.25pt at print scale. Some fine details, like the bridge cables, are drawn at 0.6px and need checking.
- Any raster image is at least 300 ppi at placed size (checked with `pdfimages -list`).
- Transparency is flattened.

**Colour**
- The output is kept in RGB, which KDP accepts and converts at print.
- The proof also gets a soft-proof render through a CMYK profile, flagging very saturated blues and greens and dark night scenes that may shift or print muddy.
- An ink-coverage report flags heavy areas, such as the night skies in Whitby, EPCOT and Tokyo.

**Files**
- PDF size is well under KDP's limit, with no form fields, annotations or JavaScript.

**Physical proof**
- Before publishing, order at least one KDP proof copy of each physical edition and check colour, gutter and readability by hand. Nothing replaces this.

**EPUB checks**
- epubcheck passes with zero errors.
- Accessibility is checked with **Ace by DAISY**: alt text on every polaroid, a language set, a reading order and navigation.
- The book opens and pages through correctly in Apple Books on iPad (portrait and landscape) and on Mac.
- The Kindle EPUB renders in Kindle Previewer on a phone, a tablet and an e-ink device.

**Content checks**
- en-GB spell check, with a custom word list for pub and place names.
- Smart quotes and apostrophes for print. The data currently mixes straight `'` and `-` as a dash; templates convert them for print only, so the site is untouched.
- Prices keep the "~" prefix, plus a dated note that they are estimates.
- Any destination whose `lastVerified` date is older than 12 months is flagged before a release.

### 6.2 Font licensing

All five fonts are under the **SIL Open Font License 1.1**: Inter, Bebas Neue, Caveat, DM Serif Display and Space Mono.

**What the OFL allows:**
- Embedding in PDFs and EPUBs, including books that are sold.
- Subsetting.
- Commercial use.

**What it doesn't allow:** selling the font files on their own.

**Plan:**
- **Vendor the fonts:** store the exact font files and versions in `publishing/fonts/`, with their `OFL.txt`, instead of loading them from Google's servers. Every build then uses identical fonts and works offline.
- **Variable fonts:** Inter is a variable font. Use static instances for print to avoid variable-font rendering differences.
- **In the EPUB:** include the OFL text in the EPUB package and add a short font credit on the copyright page. Font obfuscation isn't required by the OFL; it's optional.
- **Text inside drawings:** some polaroids contain text in Bebas Neue, such as "ELLAND ROAD" or "MOLINEUX". Those fonts must be embedded too. Chromium does this automatically for PDF; for the Kindle PNGs the text is rasterised.

### 6.3 Image handling

**Master format**
- The vector SVG per destination is the master, extracted from `snaps.js` to `snaps/<id>.svg`.
- Vectors scale cleanly from a 6" × 9" page to an 8.25" × 11" page.
- Never upscale rasters.

**Derivatives per format**

| Format | How the polaroids are used |
|---|---|
| Print PDF | Inline vector, fonts embedded, transparency flattened at export |
| Fixed-layout EPUB | Inline SVG, with a `<title>`/`aria-label` taken from the title and fact |
| Kindle | PNG (or high-quality JPEG) at 1600px on the long edge, sRGB, compressed, with alt text |
| Cover | Rendered at 300 ppi at full cover size, then placed in the cover PDF |

**Rights review before a commercial release**
- Some drawings feature trademark-heavy subjects. The ones to review:
  - the castles and the Tower of Terror at Disneyland Paris, Magic Kingdom and Hollywood Studios;
  - the Universal parks;
  - stadium names such as King Power Stadium;
  - the "BALTIC" and "H&W" lettering.
- Recommendation for the sold editions: replace or simplify anything that relies on a company's trademark or branding.
- Add an "unofficial guide, not affiliated with any venue or brand" line to the copyright page.

**AI disclosure**
- The polaroid illustrations and much of the written text were produced with an AI assistant.
- KDP asks publishers to disclose AI-generated content (text and images) when publishing.
- Each edition's metadata will record this so the KDP form can be answered accurately.

### 6.4 Publishing metadata (per edition, in the manifest)

**Identity**
- Title, subtitle, series name and number, and an edition statement ("Collector's Edition" or "Traveller's Edition").
- Author "Rob Callery", and the publisher or imprint name.

**Identifiers**
- Each format needs its own ISBN: the hardback, each paperback, and the Apple EPUB if you want one. Each regional volume is a separate book with its own ISBNs.
- **Option A:** use free KDP ISBNs. They are only valid on Amazon, and KDP appears as the imprint.
- **Option B:** buy your own ISBNs from Nielsen (the UK ISBN agency). You then become the publisher.
- **Ebooks:** the Kindle edition gets an ASIN automatically. Apple Books doesn't require an ISBN.

**Description and discovery**
- A description up to 4,000 characters.
- 7 KDP keyword slots.
- Categories: the BISAC *Travel / Europe / Great Britain* code for the UK volumes (look up the exact TRV009… code on the BISG list at release) plus Thema WTH (travel guides).
- Language `en-GB`.
- Publication date and territories.

**Pricing**
- List prices per marketplace, set from KDP's printing-cost calculator. Premium colour at 400+ pages needs a high list price, which is another reason for regional volumes.

**EPUB metadata**
- `dc:identifier`, `dc:title`, `dc:creator`, `dc:language`, `dc:publisher` and `dcterms:modified`.
- A cover image.
- The fixed-layout settings.
- Accessibility metadata: `schema:accessMode`, `accessibilityFeature`, `accessibilityHazard` and `accessibilitySummary`.
  - The EU Accessibility Act applies to ebooks sold in the EU from June 2025. A sole author is likely exempt as a micro-enterprise, but the stores increasingly expect this metadata anyway.

**Copyright page contents**
- © Rob Callery, the edition and printing number, and the ISBN.
- The data commit and build date.
- "Information correct at <latest lastVerified>".
- "Please drink responsibly."
- The unofficial-guide disclaimer and the font credits.

**Legal deposit (UK)**
- If you publish under your own ISBN, a copy of each print edition must be deposited with the British Library within a month of publication.

## 7. Workflow, kept separate from the website

### 7.1 Branches and repositories

| Branch | Purpose | Deploys? |
|---|---|---|
| `main` | The website, exactly as today | Yes, GitHub Pages builds from `main` |
| `publishing` | Publishing tool, templates, manifests, plan | **No** |
| `edition/<name>` (optional) | Long-running work on one book, e.g. text overrides | No |

**Getting fresh data:** the publishing tool reads the guide data from a chosen commit of `main` (`git show <commit>:travel-guides/guides.js`). The website and the books never have to be in sync. A book can be frozen on October's data while the site keeps changing.

**Things to decide later:**
- **Merging into `main`:** if the publishing folder is ever merged, it would also be served publicly under `callery.co.uk/publishing/`. Before that, either keep publishing on its own branch, or switch Pages to a GitHub Actions deploy that only publishes the site files. That is a website change, so it's deferred and needs your sign-off.
- **A private repository:** consider a private repo for manuscripts, ISBNs, covers and pricing, because the current repo is public. Book drafts would then not be visible before release.

### 7.2 Release steps

1. **Draft:** create `editions/<book>.yml`. Run `callery-publish plan editions/<book>.yml`, which prints the selection, page count, spine width, any page-limit warnings, and stale `lastVerified` flags.
2. **Verify data:** re-check pubs for the selected destinations and update `lastVerified`. These are website data changes on `main` and go live as normal.
3. **Build:** run `callery-publish build editions/<book>.yml` to produce the interior PDF, cover PDF, EPUBs and QA report under `build/<book>/<version>/`.
4. **Review:** read the QA report, fix overflows with `print` overrides, and rebuild until preflight is clean.
5. **Freeze:** tag `release/<book>/v1.0.0` on the `publishing` branch. A manually triggered GitHub Actions workflow (`publish.yml`, `workflow_dispatch` only, never on push) rebuilds from the tag. It attaches the files and QA report to a **GitHub Release** (or a private store), not to the website.
6. **Proof:** upload to KDP as a draft, order proof copies, check them in Apple Books and Kindle Previewer, and fix anything found as v1.0.1.
7. **Publish:** submit to KDP and Apple Books, then record the ASINs and ISBNs in the manifest.
8. **Later editions:** bump the version, rebuild from newer data, and generate a changelog listing what was added, removed or edited since the last release.

## 8. Phased delivery

| Phase | Scope | Outcome |
|---|---|---|
| 0 | Make the legacy scripts runnable from the repo (relative paths, pinned dependencies), vendor the fonts, add `extract.py` and the JSON Schema | A reproducible data export, no visual change |
| 1 | Traveller's Edition PDF (6" × 9", spread mode) for one region, plus the preflight report | First printable proof, e.g. Yorkshire |
| 2 | Covers, the KDP metadata manifest, and the release workflow via GitHub Releases | First real KDP upload (draft) |
| 3 | Fixed-layout EPUB for Apple Books, reusing the Phase 1 templates | Apple Books proof |
| 4 | Kindle reflowable EPUB with raster polaroids | Kindle Previewer pass |
| 5 | Collector's Edition templates (8.25" × 11"), dividers, beer cross-references, pub index | Hardback proof |
| 6 | Compact mode, custom collections, and the changelog between editions | Pocket and themed volumes |

## 9. Decisions needed from you

1. Your own ISBNs (Nielsen) or KDP's free ones?
2. Should the first book be a regional volume (Yorkshire is my suggestion) or the full guide?
3. Should the Collector's Edition be hardback only, or also an 8.25" × 11" paperback (same interior)?
4. Should we create a private repository for book production, or keep it on the public repo's `publishing` branch?
5. For the commercial editions, should we redraw or remove the brand-heavy polaroids (the Disney and Universal parks)?
6. What publisher or imprint name should go on the books?

## Sources

- KDP: Paper and trim size options; print options (bleed, margins, page ranges): https://kdp.amazon.com/en_US/help/topic/GVBQ3CMEQW3W2VL6
- KDP: Standard colour: https://kdp.amazon.com/en_US/help/topic/GX56BFPW4BKNPGFW
- KDP: Supported ebook formats (MOBI no longer accepted for fixed layout from March 2025): https://kdp.amazon.com/en_US/help/topic/G200634390
- KDP: Fixed-layout eBooks (EPUB, DOCX or KPF): https://kdp.amazon.com/en_US/help/topic/GULSQMHU5MNH4EZM
- KDP: Printing costs (paperback premium/standard colour, UK and US): https://kdp.amazon.com/en_US/help/topic/G201834340
- Apple Books Asset Guide: Defining book layout metadata: https://help.apple.com/itc/booksassetguide/en.lproj/itc2cf4d26eb.html
- EPUB 3 Fixed-Layout Documents: https://idpf.org/epub/fxl/
