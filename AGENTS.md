# Sorvel website — notes for coding agents

Static site for sorvel.agency, deployed by Cloudflare on every push to `main`.

## Layout
- `website/` — the published site (what Cloudflare serves). Never edit generated pages here by hand; they are overwritten by the build.
- `_source/` — Python generators that write most pages into `website/`.
- `src/` — Cloudflare Worker (analytics, `/stats` dashboard). Secrets live in Cloudflare only; never put keys in code.

## Which file to edit
- Home page `website/index.html` is hand-built: edit it directly.
- Service, pricing, about, process, reviews, contact, work grid: `_source/site/*.py` (`services.py`, `pricing.py`, `main_pages.py`, `rest.py`, shared parts in `common.py`).
- Blog posts: `_source/site/blog_posts.py` (content) and `blog.py` (layout). Glossary: `glossary.py`.
- Case studies: `_source/*_page.py` (`nc_page.py` holds the newer Figma-based cases), case list/order in `_source/chapters.py` and `CASES`/`PREVIEW` in `common.py`.
- SEO, schema, sitemap, robots.txt, llms.txt, nav injections, asset versions: `_source/seo.py`.
- Styles: `website/css/*.css` (`apple.css` loads last). Scripts: `website/js/*.js`.

## After any change
1. `cd _source && python3 build.py` (needs Python 3 + Pillow).
2. If you edited a CSS/JS file, bump its number in `ASSET_V` (or `CASE_V` for `case.css`) in `_source/seo.py`, then rebuild. If you replaced a case image under `website/img/work/`, bump `IMG_V`.
3. Check the page in a browser at desktop and 390px width (no horizontal scroll).
4. Commit and push to `main`.

## Rules
- Case study pages stay `noindex` (`NOINDEX_CASES` in `seo.py`) unless the owner says otherwise. The ServersCamp case is hidden (`HIDDEN` in `common.py`).
- Never invent client results, metrics or reviews. Use facts about scope and design only.
- Keep copy in plain, natural English. Brand name: Sorvel. Never mention "AltCreative".
