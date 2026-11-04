# Blog autopilot: one new article every 48 hours

Instructions for the scheduled run that adds one article to sorvel.agency. Read AGENTS.md first.

## Goal
Each article should win clients: rank on Google, get quoted by ChatGPT, Claude, Perplexity and Google AI answers, and lead readers to a Sorvel service. One strong article beats two average ones. **If no topic passes the checks below, publish nothing and report why.**

## 1. Pick the topic (about 15 minutes of research)
- Read every existing post in `_source/site/blog_posts.py` (slug, h1, card). Never write a second article for a search intent an existing post already answers. Expanding an existing post can be a better move; if so, expand it instead of adding a new one, and report that.
- Research demand with WebSearch (and Google Trends via WebFetch if it is reachable): what business owners, founders and marketers in any industry search right now about websites, Webflow, Framer, WordPress, Shopify design, landing pages, redesigns, migrations, pricing, AI search (GEO/AEO), UX/CRO.
- Prefer topics with buying intent: cost, pricing, "vs" comparisons, "how to choose", "agency", migrations, redesigns.
- Sorvel wants clients from **every industry**, not only SaaS, fintech and AI. Rotate topics across niches so the blog reaches many kinds of buyers: e-commerce and Shopify stores, real estate and property, healthcare and clinics (dental, medical, wellness), law firms, restaurants and hospitality, travel and tourism, construction and home services, education and online courses, nonprofits and churches, professional services (accounting, consulting, recruiting), beauty and salons, automotive, local service businesses, startups of any kind. Industry guides such as "<industry> website design: what it costs and what it needs" are strong topics. Avoid two articles in a row for the same niche.
- Skip news that will be stale in a month, topics outside Sorvel's services, and anything Sorvel does not do (no HubSpot development, no mobile app development, no consulting).
- Good candidates already noticed in Search Console (use them first, check they are still not covered): Webflow vs Squarespace, Wix vs Webflow (expand the existing post if it exists), Shopify store redesign cost, Webflow for fintech, how much a SaaS website costs (exists: expand rather than duplicate), getting a website cited by ChatGPT and AI search (GEO), tourism website development.

## 2. Write the article
- 1,600 to 2,000 words of body text plus 6 to 9 FAQ items. Plain, natural English. Short sentences. No filler, no hype words ("unlock", "elevate", "seamless", "in today's fast-paced world", "delve").
- Structure that works for SEO and AI answers:
  - `lead`: 1 to 2 sentences that state what the reader will get.
  - First section "The short answer": the direct answer in 2 to 3 sentences, then a `post-note` box with key takeaways. AI assistants quote this part.
  - Question-style or task-style H2s that match real searches.
  - At least two tables (`post-table`, first row in `<thead>`), with concrete numbers where they exist.
  - A decision checklist or step list.
  - `[[cta]]` once, roughly a third of the way in.
  - 2 to 4 internal links to related posts (`../blog/<slug>.html`) and one to the matching service page (`../services/<slug>.html`).
  - FAQ answers that each stand alone in one or two sentences.
- Facts: check every price, plan, limit or date against at least two current sources found with WebSearch/WebFetch. Never invent statistics, client results, quotes or reviews. If a number cannot be confirmed, leave it out. Say "as of <month year>" for prices.
- Sorvel facts that may be used: landing pages from $2,400 (extra pages from $600, live in 1 to 2 weeks), websites from $6,900, website migrations from $2,900, product UI from $4,800, brand identity from $3,900, UX audit $750; written plan and fixed quote within 24 hours; design in Figma, builds in Webflow, Framer, WordPress; Shopify design. Site copy uses "we" and the brand name Sorvel. Never mention AltCreative.
- Section ids must be unique and prefixed with a short code for the post (for example `wfp-short`); never use ids that exist on the page template such as `brief`, `contact`, `top`, `faq`, `work`.

## 3. Add it to the site
- Append one `dict(...)` to the end of `POSTS` in `_source/site/blog_posts.py`, following the format of the last post (slug, title ≤ 70 chars ending in "| Sorvel", h1, card, desc 140 to 160 chars, cat, date = today, svc, cover, lead, sections, faq).
- Cover: find a fitting photo on Freepik with the Magnific connector (`stock_search`, landscape, no AI-generated, not already used), `stock_download`, then save two WebP files: `website/img/blog/c-<slug>.webp` at 1600×900 and `c-<slug>-800.webp` at 800×450 (centre crop to 16:9, quality about 78). Look at the image before using it.
- Add a link to the new post from one closely related older post (one sentence, natural anchor text).
- Build: `cd _source && python3 build.py`. Check: the page exists, no duplicate ids, it is in `sitemap.xml` and `llms.txt`, FAQPage schema present, and a Playwright check at 1440px and 390px shows no JS errors and no horizontal scroll.

## 4. Publish and report
- Commit and push to `main` (Cloudflare deploys automatically). Author: Mykola Tanasiichuk, koliafree1@gmail.com.
- Report in Ukrainian, short: the article title, the URL `https://sorvel.agency/blog/<slug>` to submit in Google Search Console (URL Inspection → Request indexing), the search queries it targets and why this topic was chosen, plus the sources used for facts.
