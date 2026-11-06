# Restaurant website design — editorial and handover record

- Article: Restaurant website design: what to include before you hire
- URL: https://sorvel.agency/blog/restaurant-website-design
- Publication date: 2026-11-06 (Europe/Madrid).
- Source of truth: `_source/site/blog_posts.py`; generated page: `website/blog/restaurant-website-design.html`.
- Related older article changed: `website-redesign-cost`, with a contextual link to this guide.
- Author requested by the owner: Mykola Tanasiichuk <koliafree1@gmail.com>.

## Topic and timing

`git pull` ran before editing. The latest existing article was `webflow-pricing`, dated 2026-11-04, added by commit `6bbdafe` at 2026-11-04T08:33:55+01:00. More than 40 hours had passed. All existing slugs, headings and card descriptions were inspected; none covered restaurant website procurement. The preceding post concerned platform pricing, so this also rotates the industry.

Target queries: restaurant website design; restaurant website design agency; restaurant website redesign; restaurant website design brief. The intent is choosing a supplier and defining paid project scope, rather than general restaurant marketing.

Search research on 2026-11-06: Yahoo results for ["restaurant website design" agency](https://search.yahoo.com/search?p=%22restaurant+website+design%22+agency) included specialist restaurant agency listings and agency service pages. This supports a qualitative buying-intent assessment, not a search-volume or trend claim. Google returned a JavaScript interstitial; DuckDuckGo a bot challenge; Bing results were insufficiently relevant; Google Trends returned HTTP 429. No volume estimates, AI summaries, competitor statistics or ranking claims were used as article evidence.

## Fact checks — fetched and read on 2026-11-06

The article distinguishes our recommended scope and example workflows from externally verifiable technical facts. No market price, plan fee, provider limit, client result, quote or review is asserted.

| Technical fact used | Source one | Source two |
| --- | --- | --- |
| Informative images need an equivalent text alternative; a menu image should not be the only way to understand the menu. | [W3C Images Tutorial](https://www.w3.org/WAI/tutorials/images/) | [WCAG: Non-text Content](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html) |
| Restaurant structured data can describe address, opening hours and the menu URL. | [Google Local Business documentation](https://developers.google.com/search/docs/appearance/structured-data/local-business) | [Schema.org Restaurant](https://schema.org/Restaurant) |
| Search appearances are not guaranteed. The article recommends rejecting guaranteed rankings or AI citation promises. | [Google AI features guidance](https://developers.google.com/search/docs/appearance/ai-features) | [Google structured data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) |
| HTTP 301 and 308 are permanent redirects suitable for permanent URL changes. | [Google site moves](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) | [Google redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects) |

Each pair is linked beside its claim in the article. Suggested page structures, acceptance tasks, account ownership arrangements and supplier questions are editorial recommendations, not market statistics or promises of commercial results.

## Cover provenance

- Provider: Pexels; contributor: Pixabay; photo ID: 262978.
- [Photo page](https://www.pexels.com/photo/person-holding-pastry-dishes-on-white-ceramic-plates-262978/).
- [Downloaded original](https://images.pexels.com/photos/262978/pexels-photo-262978.jpeg).
- [Pexels license](https://www.pexels.com/license/), fetched and read on 2026-11-06: free use and modification permitted, attribution optional; do not imply endorsement. The photo page also labels the asset free.
- Original SHA-256: `26ff5339899051fa208c64bdb241cd009e335795333743abcf11a5efffb51767`.
- Original inspected visually: waiter carrying plated food; used as editorial illustration, not a Sorvel client project or restaurant endorsement.
- Compared against existing blog images using a 64-bit difference hash. Nearest distance: 26 bits; no matching cover found.
- Outputs: `c-restaurant-website-design.webp` (1600×900) and `c-restaurant-website-design-800.webp` (800×450), centred 16:9 crop, Pillow LANCZOS, WebP quality 78.
- The owner initially allowed Pexels/Unsplash. Magnific tools were unavailable in this session; Pexels was accessible. The generator now accepts optional per-post `cover_credit=(label, url)` so the new image is correctly credited without changing older Freepik credits.

## Build and validation

Run from `/workspace/sorvel-website/_source`:

```sh
python3 -m pip install pillow
python3 build.py
```

The standalone `pip` launcher in the restored environment had a broken interpreter path; `python3 -m pip` worked and confirmed Pillow 13.0.0.

The existing sitemap generator refreshes all lastmod values to the build date; its generated output is retained.

Article content: 1,643 words including lead and table text, excluding headings and FAQ; eight FAQ items; two tables with thead; one CTA marker; unique rwd-prefixed section IDs; three related article links and the website service link.

Validation completed successfully before commit:

- Full Python build; generated HTML exists; blog index, sitemap.xml and llms.txt include the article.
- No duplicate HTML IDs; all local links and fragment targets resolve; BlogPosting date/headline and eight FAQPage entries checked.
- Both WebP dimensions and format checked; Pexels attribution rendered on this article, older cover credits unchanged.
- Playwright via local Wrangler at 1440px and 390px: no horizontal page scroll, JavaScript exceptions, console errors, failed HTTP responses or broken images.
- Desktop table-of-contents link tested. The mobile template intentionally hides the sidebar below 860px; that is not a failed link.
- Desktop and mobile checked visually, including mobile top and article content after scrolling settled.
- git diff --check passed.

## Shared work with Claude

This record and the article's sources are committed with the generated output and cover files. Git history is the shared record. Before another edit, pull the current main branch and inspect recent commits; edit the generator source rather than the generated HTML. Do not add another article for this same intent. The post date also lets the 48-hour automation observe the new publication and apply its 40-hour guard.
