# Construction website design — editorial and shared-work record

- Title: Construction website design: cost, scope and choosing an agency
- URL: https://sorvel.agency/blog/construction-website-design
- Date: 2026-11-10, Europe/Madrid.
- Source: `_source/site/blog_posts.py`; edit this rather than the generated HTML.
- Author: Mykola Tanasiichuk <koliafree1@gmail.com>.
- Related older article updated: `how-to-choose-a-web-design-agency`, with a contextual link to this guide.

## Coordination and topic choice

Pulled main before editing. Baseline was `066bb52`, including Claude's dental article, GA4 integration and dashboard changes. The latest post was dental-website-design, added in `54817ac` on 2026-11-08 at 10:33:58+01:00. At the start of this task on 2026-11-10, more than 45 hours had elapsed, satisfying the existing 40-hour guard.

Reviewed all prior post slugs, headings and card descriptions. There was no construction/contractor website procurement guide. This rotates away from dental/healthcare and addresses paid website scope, supplier selection and quote requests rather than general construction advice.

Target queries: construction website design; construction website design cost; construction website design agency; contractor website design; construction company website redesign.

Search research: [Yahoo, construction website design agency cost](https://search.yahoo.com/search?p=construction+website+design+agency+cost), fetched 2026-11-10. Results included construction agency directories and web-design pricing guides. Used only as qualitative evidence of buying intent; no search volume, competitor price, review, AI summary or market-average estimate was copied into the article. Search appearance and commercial results are not promised.

## Current sources and fact checks

All sources below were fetched and read on 2026-11-10.

| Article fact | First source | Second source |
| --- | --- | --- |
| Sorvel website design and build starts from $6,900 USD, as of November 2026. This is Sorvel's starting price, not a construction-industry average. | [Live pricing page](https://sorvel.agency/pricing) | [Live website service page](https://sorvel.agency/services/websites) |
| GeneralContractor belongs to the LocalBusiness hierarchy; use the most specific applicable local-business subtype. | [Schema.org GeneralContractor](https://schema.org/GeneralContractor) | [Google Local Business documentation](https://developers.google.com/search/docs/appearance/structured-data/local-business) |
| Forms need labels and instructions for information users must supply. | [W3C Forms Tutorial](https://www.w3.org/WAI/tutorials/forms/) | [WCAG Labels or Instructions](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html) |
| Google AI search uses established SEO practices; search appearances are not guaranteed by eligibility or correct markup. | [Google AI features guidance](https://developers.google.com/search/docs/appearance/ai-features) | [Google structured data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) |

Each fact pair is linked in the relevant article section. Page structures, project templates, form questions, supplier evaluation and example briefs are explicitly editorial recommendations, not statistics or supposed client results. No external market price ranges, invented project outcomes, testimonials, certifications or client quotes are used.

## Photo provenance

- Provider: Pexels; contributor: Anamul Rezwan; asset ID: 1216589.
- [Canonical photo page](https://www.pexels.com/photo/two-man-holding-white-paper-1216589/), which labels the photo free.
- [Downloaded original](https://images.pexels.com/photos/1216589/pexels-photo-1216589.jpeg).
- [Pexels license](https://www.pexels.com/license/), checked 2026-11-10: free use and modification permitted; attribution optional; no implied endorsement.
- Original SHA-256: `4f31a7a4fa6a80e75254ad6944606e732ae445110c7d68b56ef5ca86b1035308`.
- Visually inspected: construction workers reviewing plans at a worksite. Editorial illustration, not presented as Sorvel client work.
- Compared with existing blog images using a 64-bit difference hash; nearest existing image differed by 19 bits, so no matching cover was found.
- Outputs: `website/img/blog/c-construction-website-design.webp` (1600×900) and `c-construction-website-design-800.webp` (800×450), centred 16:9 crop, Pillow LANCZOS, WebP quality 78.
- Uses the existing per-post cover_credit support. No template changes were required. Magnific tools were unavailable; Pexels remains authorised by the owner's original instructions.

## Reproduction and shared work with Claude

Run the build from `/workspace/sorvel-website/_source`:

```sh
python3 -m pip install pillow
python3 build.py
```

Pillow 13.0.0 was already available. The sitemap generator updates all lastmod dates to the build date; the generated output is retained.

The body is 1,702 words including lead and tables, excluding headings and FAQ. There are eight FAQ items, two tables with thead, a checklist, one CTA, cwd-prefixed section IDs, three related article links and a link to the website service.

Git history and this file are the shared record. Before further changes, pull main, check recent commits and the latest post date. Do not duplicate the construction/contractor procurement intent. Keep Claude's existing analytics and privacy changes intact. Browser QA is performed against the local Worker; external GA scripts/requests are stubbed during QA so tests do not send visits to the production analytics property.

## Validation before commit

- Full Python build passed; new article is linked from the blog index, sitemap.xml and llms.txt.
- Canonical URL, indexability and 149-character description checked.
- No duplicate IDs; local links (including clean cookie-banner URLs) and fragment targets resolve.
- BlogPosting headline/date and eight FAQPage entries match the source.
- Both WebP dimensions/format and the per-post Pexels credit checked.
- Playwright at 1440px and 390px: no horizontal page scrolling, JavaScript exceptions, console errors, failed HTTP responses or broken images.
- Desktop contents link tested; the mobile sidebar remains intentionally hidden by the existing template.
- Desktop and mobile screenshots inspected visually after scroll animations settled.
- git diff --check passed.
