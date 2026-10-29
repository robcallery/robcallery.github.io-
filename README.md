# callery.co.uk

Rob Callery's site: travelling the world one beer at a time, and always heading home to Elland Road.

The site is plain static files. It is served by the Cloudflare Worker `callery`, set up in `wrangler.jsonc`.
Pushing to `main` deploys it through Cloudflare Workers Builds, so there's no need to upload zips.
Files listed in `.assetsignore` stay in the repo but are not published.
