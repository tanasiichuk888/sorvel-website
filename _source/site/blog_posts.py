# Blog articles. Each post: slug, title (search title), h1, desc, cat, date, lead, toc sections, faq, service link.
# Body HTML uses a few helpers from blog.py: [[cta:...]] markers are replaced with an inline call-to-action box.

POSTS = [
dict(
  slug="wordpress-to-webflow-migration-cost",
  title="WordPress to Webflow Migration Cost in 2026 | Sorvel",
  h1="What a WordPress to Webflow migration costs in 2026",
  card="What a WordPress to Webflow migration really costs, what moves the price, and the hidden costs of doing it cheaply.",
  desc="How much a WordPress to Webflow migration costs in 2026, what drives the price, the running costs after launch, and how to get an exact fixed quote.",
  cat="Migrations", date="2026-10-25", svc=("wordpress-to-webflow-migration", "WordPress to Webflow migration"),
  cover=("mig-cover", "A web developer working on a website migration at a desk late in the evening"),
  lead="Most quotes for moving a WordPress site to Webflow land somewhere between a few hundred and tens of thousands of dollars. Here is what sits behind those numbers, so you can tell a fair quote from a risky one.",
  sections=[
("short", "The short answer", """
<p>For a typical company site of 10 to 30 pages with a blog, a careful migration to Webflow costs <b>from $2,900</b> and takes <b>1 to 3 weeks</b>. That covers the content audit, the CMS setup, the content import, the template rebuild, a full 301 redirect map and checks after launch.</p>
<p>A migration combined with a redesign is a website project, not a migration, and usually starts around <b>$6,900</b>. Content-heavy sites with hundreds or thousands of posts are priced after an audit, because the work depends on how clean the content is, not only on how much there is.</p>
<div class="post-note"><b>Rule of thumb</b><p>You pay for the number of different page layouts and the state of your content, not for the number of pages. Fifty blog posts on one template cost far less to move than ten pages that are each built differently.</p></div>
"""),
("what", "What you are actually paying for", """
<p>A migration looks like copying pages from one tool to another. The copying is the easy part. The work that protects your traffic and your team's time is everything around it:</p>
<ul>
<li><b>Content and SEO audit.</b> Every page, post and template listed, with the ones that bring visits and links marked, so nothing that earns traffic gets lost.</li>
<li><b>CMS model.</b> Collections for posts, categories, authors, case studies or resources, with fields for SEO titles, descriptions and images, set up for how your team publishes.</li>
<li><b>Content import.</b> Posts, images and metadata moved as CMS items through a cleaned export, not pasted by hand.</li>
<li><b>Template rebuild.</b> Each page layout rebuilt natively in Webflow with a clean class system, so the site stays easy to edit.</li>
<li><b>Redirect map.</b> Every old URL pointed to its new home with a 301 redirect. This is the step that keeps your rankings.</li>
<li><b>Checks before and after launch.</b> Broken links, meta tags, speed, forms and indexing, then a few weeks of watching Search Console.</li>
</ul>
<p>When a quote is far below the market, one or more of these steps is usually missing. Most often it is the redirect map and the checks after launch, which are exactly the parts you only notice when traffic drops.</p>
"""),
("factors", "Six things that move the price", """
<h3>1. How many different layouts you have</h3>
<p>A home page, a services page, a blog post and a case study are four templates. Each one is designed or rebuilt once, then reused. A site with 40 pages on 6 templates is a smaller job than a site with 15 pages where every page was built differently in a page builder.</p>
[[fig:templates]]
<h3>2. How much content, and how clean it is</h3>
<p>A few hundred clean posts import quickly. Posts full of page builder markup, shortcodes, embedded galleries or custom fields take longer, because each pattern has to be cleaned or rebuilt before it fits Webflow's rich text.</p>
<h3>3. Your URL structure</h3>
<p>Webflow places CMS items under a collection folder, for example <code>/blog/post-name</code>. If your WordPress posts live at the root or under dates like <code>/2024/05/post-name</code>, every one of those URLs changes and needs a redirect. That is normal and safe when it is planned, but it adds work to the redirect map and testing.</p>
<h3>4. Plugins that need a replacement</h3>
<p>Forms, search, memberships, multilingual content, events or calculators often run on WordPress plugins. In Webflow some become native features, some need a small integration, and a few need a different approach. Each one is listed in the audit and priced, so there are no surprises later.</p>
<h3>5. Move as is, or redesign on the way</h3>
<p>Keeping today's design is the fastest route. Many teams use the move to fix the design as well, which makes sense because the templates are rebuilt anyway. Just know it turns a migration into a website project, with design rounds and a longer timeline.</p>
<h3>6. Integrations and tracking</h3>
<p>CRM forms, analytics, tag manager, cookie consent, chat widgets and ad pixels all need to be reconnected and tested on the new site. A typical company site has between three and eight of these.</p>
"""),
("ongoing", "Running costs after the move", """
<p>The migration is a one-off. After launch you pay Webflow for hosting instead of paying for WordPress hosting, premium plugins and the developer time that keeps them updated.</p>
<ul>
<li><b>Webflow site plan.</b> Billed per site, yearly or monthly. The plan you need depends mostly on how many CMS items you have. Webflow reworked its site plans in 2026, so check the current limits on <a href="https://webflow.com/pricing" target="_blank" rel="noopener">webflow.com/pricing</a> before you compare.</li>
<li><b>Workspace seats.</b> Only needed for people who build or design in Webflow. Content editors can usually publish without a paid seat.</li>
<li><b>Third-party tools.</b> Only if a plugin had no native replacement, for example an advanced site search.</li>
</ul>
<p>What usually disappears is the maintenance line: plugin updates, security patches, broken layouts after an update and the developer hours spent fixing them. For most marketing sites that is the real saving, and the reason teams move in the first place.</p>
"""),
("diy", "Doing it yourself, a freelancer or a studio", """
<p><b>Doing it yourself</b> works for a small blog with simple posts. You can export your content, convert it to CSV, import it into a Webflow collection and add redirects in the site settings. The risk is in the details: images still loading from the old server, missing meta descriptions, redirects that point to the wrong place, or a staging site that gets indexed by mistake.</p>
<p><b>A freelancer</b> is a good fit when the site is small and you already know what you want. Ask how they handle redirects and what they check after launch. If the answer is vague, the price is low for a reason.</p>
<p><b>A studio</b> makes sense when traffic matters, when the content is large or messy, or when you want a redesign at the same time. You get a written plan, one team responsible for design, build and SEO, and someone watching the numbers after launch.</p>
"""),
("cheap", "The hidden cost of a cheap migration", """
<p>The expensive migration is the one that has to be fixed later. These are the problems we are asked to repair most often:</p>
<ul>
<li><b>Lost rankings.</b> Old URLs return 404 errors instead of redirecting, and the pages that brought leads disappear from Google within weeks.</li>
<li><b>Images that vanish.</b> Images inside blog posts still point to the old WordPress server. Everything looks fine until the old hosting is cancelled.</li>
<li><b>Empty meta tags.</b> Titles and descriptions were not mapped to CMS fields, so every post now shares the same generic snippet in search results.</li>
<li><b>A site nobody can edit.</b> Classes named <code>div-block-42</code> and copied styles mean every change risks breaking a layout, which defeats the point of Webflow.</li>
</ul>
<p>Fixing these after launch usually costs more than doing them properly the first time, and lost traffic takes months to come back.</p>
[[cta]]
"""),
("quote", "How to get an exact quote", """
<p>You can get a precise, fixed price for a migration in a day if you share four things:</p>
<ol>
<li>Your current site address.</li>
<li>A rough count of pages and posts, or simply your <code>/sitemap.xml</code> link.</li>
<li>The plugins you rely on: forms, memberships, search, languages, anything custom.</li>
<li>Whether you want to keep the current design or refresh it during the move.</li>
</ol>
<p>With that, we can send a written plan with scope, timeline and a fixed price within 24 hours. No call needed.</p>
[[img:mig-plan|A laptop and a notebook with a hand-written migration plan on a desk|A good quote starts with a written plan: every page, template and plugin listed before a price is given.]]
"""),
  ],
  faq=[("Is moving from WordPress to Webflow worth it?", "For marketing sites, usually yes: your team edits pages visually, there are no plugins to update, and the site is easier to keep fast. For complex stores, membership sites or apps built on plugins, WordPress or Shopify can still be the better fit."),
       ("Will I lose my Google rankings?", "Not if every old URL is redirected to the right new page, meta tags are kept and Search Console is checked after launch. Rankings can move slightly for a few weeks, then settle."),
       ("Can I keep my current design?", "Yes. The layouts are rebuilt natively in Webflow to look the same. Many teams still use the move to fix things they never liked."),
       ("How long does a migration take?", "Usually 1 to 3 weeks for a company site. Large blogs or a redesign on top add time, and the written plan gives you the exact dates."),
       ("Do I need to pay for Webflow hosting?", "Yes. Hosting is a Webflow site plan billed per site. In most cases it replaces what you paid for WordPress hosting, premium plugins and maintenance.")],
),

dict(
  slug="migrate-wordpress-to-webflow-without-losing-seo",
  title="How to Migrate WordPress to Webflow Without Losing SEO | Sorvel",
  h1="How to migrate from WordPress to Webflow without losing SEO",
  card="A step-by-step checklist for moving to Webflow while keeping your rankings, links and traffic.",
  desc="A step-by-step checklist for moving a site from WordPress to Webflow while keeping your rankings: inventory, CMS model, content import, 301 redirects, meta tags and post-launch checks.",
  cat="Migrations", date="2026-10-25", svc=("wordpress-to-webflow-migration", "WordPress to Webflow migration"),
  cover=("seo-cover", "A desktop screen showing website traffic and search performance charts"),
  lead="Traffic rarely drops because of Webflow. It drops because URLs, meta tags or images were lost on the way. This is the checklist we follow on every migration, in the order we do it.",
  sections=[
("inventory", "1. List everything you have", """
<p>Before anything moves, get a complete list of URLs on the current site. Three sources together cover almost everything:</p>
<ul>
<li><b>A crawl</b> of the live site with a tool such as Screaming Frog, which lists every page, image and redirect it can reach.</li>
<li><b>Your WordPress sitemap</b>, usually at <code>/sitemap.xml</code> or <code>/sitemap_index.xml</code>, which also catches pages that are no longer linked from the menu.</li>
<li><b>Google Search Console</b>, Performance report, Pages tab, set to the longest date range. This shows which URLs actually get impressions and clicks.</li>
</ul>
<p>Put it all into one spreadsheet with a column for each URL's traffic and backlinks. This sheet becomes your redirect map later.</p>
"""),
("priorities", "2. Mark the pages that earn traffic", """
<p>Usually a small share of pages brings most of the visits and links. Mark them clearly. They need the closest attention: the same topic, the same heading, the same depth of content and, if possible, the same URL.</p>
<p>This is also the moment to decide what not to move. Thin tag pages, old event pages and duplicate posts with no traffic can be merged or redirected to a stronger page. Moving less is often better for SEO, as long as every removed URL still redirects somewhere useful.</p>
"""),
("urls", "3. Plan the new URL structure", """
<p>Static pages in Webflow can live at any path, so <code>/about</code> or <code>/services/design</code> stay exactly as they are. CMS items work differently: every item lives under its collection folder, for example <code>/blog/post-name</code>.</p>
<p>That means WordPress posts at the root, like <code>/post-name</code>, or under dates, like <code>/2024/05/post-name</code>, will get a new URL. That is fine. Choose the new pattern once, keep the slugs identical, and every change gets a redirect in step 7.</p>
<div class="post-note"><b>Keep the slugs</b><p>When the last part of the URL stays the same, Google connects the old and new page faster, and one pattern redirect can cover hundreds of posts at once.</p></div>
"""),
("cms", "4. Model the CMS before importing", """
<p>Create the collections first: usually posts, categories and authors, plus case studies or resources if you have them. For each post, plan fields for:</p>
<ul>
<li>name, slug and publish date;</li>
<li>the main content as rich text;</li>
<li>a featured image with alt text;</li>
<li>a separate SEO title and meta description;</li>
<li>references to the category and the author.</li>
</ul>
<p>Separate SEO fields matter. They let you bind the page title and description to each item, so every post keeps its own snippet in search results instead of sharing one generic line.</p>
"""),
("content", "5. Export, clean and import the content", """
<p>Export posts from WordPress with the built-in export tool or an export plugin that outputs CSV. Then clean the export before it touches Webflow:</p>
<ul>
<li>remove shortcodes and page builder markup that Webflow's rich text can't read;</li>
<li>convert galleries, embeds and tables into formats that work in rich text, or rebuild them as components;</li>
<li>check that every post has a slug, a title and a date.</li>
</ul>
<p>Import the CSV into the collection, then open a sample of posts and compare them side by side with the originals. Pay special attention to images inside the text. If they still load from the old WordPress domain, they will break when the old hosting is switched off. Move them to Webflow before launch.</p>
"""),
("onpage", "6. Rebuild templates and keep on-page SEO", """
<p>Rebuild each template natively, with one clear H1 per page and the heading structure the old pages used. Then go through the on-page details that rankings depend on:</p>
<ul>
<li>page titles and meta descriptions, bound to the CMS fields from step 4;</li>
<li>alt text on images;</li>
<li>Open Graph images for sharing;</li>
<li>structured data, such as Article or FAQ schema, added through the page settings;</li>
<li>internal links inside posts, updated to the new URLs so they don't go through redirects.</li>
</ul>
"""),
("redirects", "7. Build and test the 301 redirect map", """
<p>This step decides whether your rankings survive. Every old URL that changes must point to its new address with a permanent 301 redirect. In Webflow, redirects live in the site settings under Publishing, and they support patterns, so a single rule can move a whole folder:</p>
<pre><code>/2024/05/(.*)   →   /blog/%1
/category/(.*)  →   /blog/category/%1</code></pre>
[[fig:redirects]]
<p>Use your spreadsheet from step 1 as the source. Redirect each URL to the most relevant new page, not to the home page. Google treats mass redirects to the home page much like missing pages.</p>
<p>After publishing, test the full list: every old URL should answer with one 301 and land on a page that returns 200. Watch for chains, where one redirect leads to another.</p>
[[cta]]
"""),
("qa", "8. Check everything before switching the domain", """
<ul>
<li>Make sure the Webflow staging address is not indexed, so Google does not see two copies of your site.</li>
<li>Crawl the staging site for broken links and missing titles or descriptions.</li>
<li>Compare titles and descriptions of your top pages against the old site.</li>
<li>Test every form, integration and tracking tag.</li>
<li>Check speed and mobile layouts on real phones, not only in the browser.</li>
</ul>
"""),
("launch", "9. Launch and tell Google", """
<p>Connect the domain in Webflow, publish, and then:</p>
<ul>
<li>open your redirect list and spot-check the most important URLs live;</li>
<li>submit the new sitemap in Google Search Console;</li>
<li>use URL Inspection on your top pages to request indexing;</li>
<li>check that <code>robots.txt</code> allows crawling.</li>
</ul>
<p>Keep the old WordPress site available on a private address for a few weeks, in case you need to recover a page or an image.</p>
"""),
("watch", "10. Watch the numbers for 30 days", """
<p>Rankings often wobble for a week or two after a move while Google recrawls the site. That is normal. What is not normal is a steady drop. During the first month, check Search Console every few days:</p>
<ul>
<li><b>Pages report:</b> new "Not found (404)" errors mean a redirect is missing. Add it.</li>
<li><b>Performance report:</b> compare clicks for your top pages with the weeks before the move.</li>
<li><b>Sitemaps:</b> make sure the new sitemap is read without errors.</li>
</ul>
<p>Most issues show up in the first two weeks and take minutes to fix when someone is watching.</p>
[[img:seo-watch|A laptop on an office desk showing search traffic charts|The first 30 days after launch: watch clicks, 404 errors and the sitemap, and fix gaps as they appear.]]
"""),
("mistakes", "The mistakes we see most often", """
<ul>
<li>Redirecting every old URL to the home page.</li>
<li>Forgetting images inside blog posts that still load from the old server.</li>
<li>One shared meta description for the whole blog.</li>
<li>The staging site indexed alongside the live one.</li>
<li>Changing slugs and content at the same time on the pages that earn the most traffic.</li>
</ul>
"""),
  ],
  faq=[("Will my rankings drop after moving to Webflow?", "A short wobble is common while Google recrawls the site. With a complete redirect map and the same on-page SEO, rankings usually settle within a few weeks, and faster pages often help."),
       ("Can I keep the same URLs in Webflow?", "Static pages, yes. CMS items always live under a collection folder, such as /blog/post-name, so root-level or date-based post URLs change and need 301 redirects."),
       ("How do I move hundreds of blog posts?", "Export them to CSV, clean the content, and import the file into a Webflow collection. Large or messy content is best cleaned with a script before import."),
       ("Do redirects slow the site down?", "No. A single 301 redirect is handled almost instantly. Avoid chains of several redirects in a row."),
       ("How long should I keep the old WordPress site?", "Keep it on a private address for a few weeks after launch, in case a page, an image or a file needs to be recovered.")],
),

dict(
  slug="saas-website-cost",
  title="How Much Does a SaaS Website Cost in 2026? | Sorvel",
  h1="How much does a SaaS website cost in 2026?",
  card="Realistic price ranges for a SaaS marketing site, what drives the cost, and how to avoid paying for the wrong things.",
  desc="Realistic 2026 price ranges for a SaaS marketing website, from templates to agencies, what drives the cost, which pages you need at launch, and running costs after.",
  cat="SaaS websites", date="2026-10-25", svc=("saas-website-design", "SaaS website design"),
  cover=("saas-cover", "A startup team reviewing their website design together on a large screen"),
  lead="A SaaS website can cost almost nothing or more than your first engineer. The difference is rarely the number of pages. It is how much thinking goes into what the site says, and how well it shows the product.",
  sections=[
("short", "The short answer", """
<p>For a custom-designed SaaS marketing site of 5 to 10 pages, built in Webflow or Framer so your team can edit it, expect to pay <b>from about $6,900</b> with a senior studio, delivered in <b>3 to 6 weeks</b>. Templates cost less but look like everyone else. Large agencies cost many times more and take months.</p>
<p>The rough ranges below come from the market as it looks in 2026. Your own quote depends on the factors further down.</p>
"""),
("options", "Four ways to get a SaaS website", """
<div class="post-table" role="region" aria-label="SaaS website options compared" tabindex="0"><table>
<thead><tr><th>Option</th><th>Typical cost</th><th>Time</th><th>Best for</th></tr></thead>
<tbody>
<tr><td><b>Template, built in-house</b></td><td>Under $2,000 plus your team's time</td><td>1 to 4 weeks</td><td>Pre-launch, testing an idea</td></tr>
<tr><td><b>Freelancer</b></td><td>About $3,000 to $15,000</td><td>3 to 8 weeks</td><td>Small sites with a clear brief</td></tr>
<tr><td><b>Senior studio</b></td><td>From $6,900</td><td>3 to 6 weeks</td><td>Seed to Series B, redesign after a raise</td></tr>
<tr><td><b>Large agency</b></td><td>$40,000 and up</td><td>3 to 6 months</td><td>Big rebrands with research and many stakeholders</td></tr>
</tbody></table></div>
<p>The jump in price between options is mostly about who does the thinking. With a template, you write the story and make every decision. With a studio or agency, someone experienced shapes the messaging, the page structure and the product visuals with you.</p>
"""),
("drivers", "What drives the cost", """
<h3>Unique page layouts</h3>
<p>A home page, a product page, pricing, a use case, an integration page and a blog post are six layouts. Once each one exists, new pages on the same layout are cheap. Count layouts, not pages.</p>
[[fig:layouts]]
<h3>Product visuals</h3>
<p>Generic illustrations are cheap and forgettable. Clean, simplified scenes of your real interface take more work but explain the product in seconds, which is the main job of a SaaS homepage.</p>
<h3>Messaging and copy</h3>
<p>If you already know what to say and to whom, the project is faster. If positioning is still fuzzy, budget time for it. A beautiful site with an unclear headline converts worse than a plain one that is clear.</p>
<h3>CMS and content types</h3>
<p>Blog, changelog, customer stories, integrations directory, docs links, careers. Each content type is a collection and a template. Start with the ones you will actually update.</p>
<h3>Motion and interactions</h3>
<p>Subtle scroll and hover motion is affordable. Heavy custom animation, 3D or interactive product demos are where budgets grow quickly.</p>
<h3>Integrations</h3>
<p>Demo booking, CRM forms, product sign-up, analytics events and cookie consent. Each is small, but they add up and need testing.</p>
"""),
("pages", "Which pages you need at launch", """
<p>You don't need everything on day one. A SaaS site that converts well at launch usually has:</p>
<ul>
<li><b>Home</b>, which explains what the product does, for whom, and shows it;</li>
<li><b>Product or features</b>, the core workflows with real screens;</li>
<li><b>Pricing</b>, even if it says "talk to us";</li>
<li><b>One or two use cases</b> for your main types of buyer;</li>
<li><b>Demo or sign-up</b>, with as few fields as possible;</li>
<li><b>Legal pages</b> such as privacy and terms.</li>
</ul>
[[img:saas-team|A product team discussing their website pages around a laptop|Start with the pages that sell, then grow the site on the same building blocks.]]
<p>Blog, comparisons, integrations and customer stories can follow once the core pages work. Built on the same components, they are quick to add.</p>
[[cta]]
"""),
("running", "Running costs after launch", """
<ul>
<li><b>Hosting.</b> A Webflow or Framer site plan, from around $15 to $40 a month for most marketing sites, depending on the plan and CMS size. Check current prices on the platform's site, as plans changed in 2026.</li>
<li><b>Tools.</b> Analytics, forms or a CRM you probably already pay for.</li>
<li><b>Updates.</b> New landing pages, a pricing change, a feature launch. Your team can do most of it in the CMS. For regular design work, a monthly design plan is usually cheaper than one-off projects.</li>
</ul>
"""),
("overpay", "How not to overpay", """
<ul>
<li><b>Fix the message first.</b> Writing or briefing the homepage story before design saves rounds of revisions.</li>
<li><b>Count layouts, not pages.</b> Ask for a quote based on templates, then add pages yourself in the CMS.</li>
<li><b>Show the real product.</b> One accurate product scene beats ten abstract illustrations.</li>
<li><b>Pick a platform your team can use.</b> Webflow suits teams that publish a lot. Framer suits fast, motion-rich sites with fewer content types.</li>
<li><b>Get it in writing.</b> A fixed scope, timeline and price before work starts is the easiest way to avoid surprise invoices.</li>
</ul>
"""),
  ],
  faq=[("How long does it take to build a SaaS website?", "Usually 3 to 6 weeks for 5 to 10 pages with a senior studio, depending on how ready the content is and how fast feedback comes."),
       ("Webflow or Framer for a SaaS website?", "Webflow if marketing publishes a lot and needs a strong CMS for blog, changelog or integrations. Framer if you want a fast, motion-rich site with fewer content types."),
       ("Can we start small and grow the site later?", "Yes, and it is usually the smart way. Launch the core pages on a component system, then add pages on the same building blocks."),
       ("Do we need a brand before the website?", "It helps, but it is not required. A logo, colours and type can be designed together with the site so they match from the start."),
       ("Is it cheaper to use a template?", "Upfront, yes. But templates rarely fit your product story, and many teams pay for a redesign within a year. A template is a good choice before product-market fit.")],
),
dict(
  slug="webflow-vs-framer",
  title="Webflow vs Framer in 2026: Which Is Better for Your Website? | Sorvel",
  h1="Webflow vs Framer: which one to choose in 2026",
  card="An honest comparison from a studio that builds on both: CMS, SEO, speed, editing, cost and which one fits your team.",
  desc="Webflow vs Framer compared by a studio that builds on both: CMS, SEO, design freedom, editing, cost and when to pick each one for a SaaS, startup or B2B website.",
  cat="Platforms", date="2026-10-31", svc=("saas-website-design", "SaaS website design"),
  cover=("c-webflow-vs-framer", "A designer working on a laptop in a studio"),
  lead="We design and build on both Webflow and Framer every month, so we have no reason to push one. Here is the short answer, then the details that should decide it for your team.",
  sections=[
("short", "The short answer", """
<p><b>Choose Webflow</b> if your marketing team publishes a lot: a blog, case studies, a changelog, integrations or hundreds of SEO pages. Its CMS, roles and structure scale better as the site grows.</p>
<p><b>Choose Framer</b> if you need a fast, motion-rich site with fewer content types, and your team wants to edit pages as easily as a design file. It is often quicker to launch.</p>
<div class="post-note"><b>Rule of thumb</b><p>Count your content types, not your pages. One or two content types: Framer is usually enough. Four or more, or a content team that publishes weekly: Webflow.</p></div>
"""),
("table", "Webflow vs Framer at a glance", """
<div class="post-table" role="region" aria-label="Webflow and Framer compared" tabindex="0"><table>
<thead><tr><th></th><th>Webflow</th><th>Framer</th></tr></thead>
<tbody>
<tr><td><b>Best for</b></td><td>Content-heavy marketing sites, SEO at scale</td><td>Launch sites, startups, design-led pages</td></tr>
<tr><td><b>CMS</b></td><td>Strong: many collections, references, filters</td><td>Good for simple collections like a blog</td></tr>
<tr><td><b>Design and motion</b></td><td>Full control, interactions take more setup</td><td>Very fast motion and effects, close to Figma</td></tr>
<tr><td><b>Editing by your team</b></td><td>Structured editor, safe for non-designers</td><td>Edit on the canvas, very easy, easier to break layout</td></tr>
<tr><td><b>SEO</b></td><td>Full control of meta, schema, redirects</td><td>Covers the basics well, less control for big sites</td></tr>
<tr><td><b>Speed to launch</b></td><td>Medium</td><td>Fast</td></tr>
<tr><td><b>Build cost with a studio</b></td><td>Usually a bit higher</td><td>Usually a bit lower</td></tr>
</tbody></table></div>
<p>Both host your site on a fast global network, both handle SSL and forms, and both can reach good Core Web Vitals when the build is clean. The real differences are content structure and how your team will work after launch.</p>
"""),
("webflow", "When Webflow is the better choice", """
<ul>
<li><b>You plan to grow through content.</b> Blog, guides, comparison pages, glossary, integrations directory. Webflow's CMS handles linked collections and filtering well.</li>
<li><b>Several people edit the site.</b> Roles and a structured editor keep content people away from the layout.</li>
<li><b>SEO is a main channel.</b> You get fine control over redirects, meta per item, schema and clean URL structures.</li>
<li><b>You are moving from WordPress.</b> Webflow is the most common target for content-rich WordPress sites. See <a href="../blog/migrate-wordpress-to-webflow-without-losing-seo.html">how to migrate without losing SEO</a>.</li>
</ul>
"""),
("framer", "When Framer is the better choice", """
<ul>
<li><b>You need to launch quickly.</b> A pre-seed or seed startup, a product launch, a waitlist or a campaign site.</li>
<li><b>Motion is part of the story.</b> Scroll effects, interactive product scenes and polished transitions are faster to build in Framer.</li>
<li><b>Your designer will own the site.</b> Framer feels like a design tool, so the person who designs can also update it.</li>
<li><b>The content is simple.</b> A handful of pages plus a blog fits Framer's CMS without workarounds.</li>
</ul>
[[cta]]
"""),
("cost", "What each one costs", """
<p>Both platforms charge a monthly site plan, and prices change, so check their current pricing pages. The bigger cost is the design and build. With our studio a website starts <b>from $6,900</b> and a single landing page <b>from $2,400</b>, on either platform. A Framer build is usually slightly cheaper for the same design; a Webflow build pays back when the site grows through content.</p>
"""),
("switch", "Can you switch later?", """
<p>Yes, but it is a rebuild, not an export. Pages have to be recreated and the CMS content moved with redirects in place. Picking the right platform first is cheaper than switching a year later, which is why we ask how your team will publish before we recommend one.</p>
"""),
  ],
  faq=[("Is Framer better than Webflow for SEO?", "For small sites both are fine. For sites that grow through content, Webflow gives more control over CMS structure, redirects and schema, which matters at scale."),
       ("Is Framer cheaper than Webflow?", "The site plans are in a similar range. A Framer build is often a little cheaper and faster, while Webflow pays back on content-heavy sites."),
       ("Which is easier for a marketing team to edit?", "Framer is easier for designers and quick text changes. Webflow's editor is safer for larger teams because people edit content without touching the layout."),
       ("Can you build on both?", "Yes. We design in Figma and build in Webflow or Framer, and recommend one after looking at your content and team."),
       ("Should a SaaS startup use Webflow or Framer?", "Pre-launch or seed with a few pages: Framer. Series A and later with a blog, changelog and SEO plans: Webflow."),
  ],
),
dict(
  slug="webflow-vs-wordpress",
  title="Webflow vs WordPress in 2026: An Honest Comparison | Sorvel",
  h1="Webflow vs WordPress: which is better for a business website in 2026",
  card="Security, speed, editing, SEO, plugins and total cost: when Webflow wins, when WordPress is still the right call.",
  desc="Webflow vs WordPress for business websites in 2026: security, speed, SEO, editing, plugins and total cost of ownership, with clear advice on when to choose each.",
  cat="Platforms", date="2026-10-31", svc=("wordpress-to-webflow-migration", "WordPress to Webflow migration"),
  cover=("c-webflow-vs-wordpress", "A developer working at a desktop computer"),
  lead="We build on both platforms and migrate sites in both directions. For most marketing websites the answer is clear, but there are cases where WordPress is still the better tool.",
  sections=[
("short", "The short answer", """
<p><b>Choose Webflow</b> for a marketing website that your team edits without a developer: no plugin updates, no security patches, hosting included and clean, fast pages.</p>
<p><b>Choose WordPress</b> if you need things a website builder does not do well: complex membership or LMS features, very large content libraries with custom logic, deep WooCommerce stores, or full control over your own server.</p>
<div class="post-note"><b>Rule of thumb</b><p>If your site is mainly pages, a blog and forms, Webflow costs less to run. If your site is really an application, WordPress (or custom code) gives you more room.</p></div>
"""),
("table", "Webflow vs WordPress at a glance", """
<div class="post-table" role="region" aria-label="Webflow and WordPress compared" tabindex="0"><table>
<thead><tr><th></th><th>Webflow</th><th>WordPress</th></tr></thead>
<tbody>
<tr><td><b>Hosting and security</b></td><td>Managed, included, no plugins to patch</td><td>Your responsibility: hosting, updates, backups</td></tr>
<tr><td><b>Speed</b></td><td>Fast by default with a clean build</td><td>Depends on theme, plugins and hosting</td></tr>
<tr><td><b>Editing</b></td><td>Visual editor on the live design</td><td>Block editor or page builder, varies by setup</td></tr>
<tr><td><b>SEO</b></td><td>Meta, schema, redirects, sitemap built in</td><td>Strong with plugins like Yoast or Rank Math</td></tr>
<tr><td><b>Plugins and features</b></td><td>Fewer, covered by integrations and code</td><td>Huge ecosystem for almost anything</td></tr>
<tr><td><b>E-commerce</b></td><td>Fine for small catalogues</td><td>WooCommerce for large, complex stores</td></tr>
<tr><td><b>Running cost</b></td><td>Predictable monthly plan</td><td>Low hosting, but maintenance time adds up</td></tr>
</tbody></table></div>
"""),
("webflow", "Why many teams move to Webflow", """
<ul>
<li><b>No maintenance work.</b> No plugin conflicts, no core updates breaking the layout, no security patches on a Friday night.</li>
<li><b>Marketing ships without developers.</b> New landing pages and posts are built from the existing components.</li>
<li><b>Design stays consistent.</b> The site keeps looking like the design, instead of drifting with every page builder edit.</li>
<li><b>Good Core Web Vitals.</b> Clean markup and global hosting make fast pages easier to keep.</li>
</ul>
[[cta]]
"""),
("wordpress", "When WordPress is still the right choice", """
<ul>
<li><b>Complex functionality.</b> Memberships, courses, bookings with custom rules, multi-language with many editors, or deep integrations with your own systems.</li>
<li><b>Large stores.</b> WooCommerce handles big catalogues and custom checkout logic better than a website builder.</li>
<li><b>You have a developer on hand.</b> With someone maintaining it, WordPress is flexible and cheap to host.</li>
</ul>
<p>We also build on WordPress, so if your project needs it, that is what we recommend.</p>
"""),
("cost", "Total cost of ownership", """
<p>WordPress looks cheaper because hosting can cost a few dollars a month. The real cost is maintenance: updates, plugin licences, security, fixes after updates and developer time for small changes. Webflow costs more per month but usually less per year once that time is counted. Moving an existing site from WordPress to Webflow with us starts <b>from $2,900</b>; see <a href="../blog/wordpress-to-webflow-migration-cost.html">what a migration costs</a>.</p>
"""),
  ],
  faq=[("Is Webflow better than WordPress for SEO?", "Both can rank equally well. Webflow has the SEO basics built in and tends to be faster out of the box; WordPress reaches the same level with good plugins and hosting."),
       ("Is Webflow more expensive than WordPress?", "Per month, usually yes. Per year, often not, because there is no maintenance, plugin licences or developer time for routine changes."),
       ("Can I move from WordPress to Webflow without losing rankings?", "Yes, with a content audit, a full 301 redirect map, kept meta data and checks in Search Console after launch."),
       ("Is WordPress more secure than Webflow?", "WordPress can be secure, but security is your job. Webflow handles hosting, SSL and platform updates for you, so there are no plugins to patch."),
       ("Do you build on both?", "Yes. We design in Figma and build in Webflow, Framer or WordPress, and recommend the platform after looking at what your site needs to do."),
  ],
),
dict(
  slug="webflow-website-cost",
  title="How Much Does a Webflow Website Cost in 2026? | Sorvel",
  h1="How much a Webflow website costs in 2026",
  card="Real price ranges for a Webflow website, what moves the number, plan costs after launch and how to get a fixed quote.",
  desc="How much a Webflow website costs in 2026: price ranges for templates, freelancers and studios, what drives the cost, Webflow plan fees and how to get a fixed quote.",
  cat="Pricing", date="2026-10-31", svc=("webflow-agency", "Webflow design and development"),
  cover=("c-webflow-website-cost", "A designer working at a desk in a creative office"),
  lead="A Webflow website can cost a few hundred dollars or well over $30,000. The difference comes down to a handful of things you can see in advance, so here they are.",
  sections=[
("short", "The short answer", """
<p>A custom-designed Webflow website for a startup or growing business usually costs <b>$5,000 to $20,000</b> with a professional team and takes <b>3 to 6 weeks</b>. With our studio a website starts <b>from $6,900</b>, a single landing page <b>from $2,400</b>, and moving an existing site to Webflow <b>from $2,900</b>.</p>
<div class="post-note"><b>Rule of thumb</b><p>Price follows the number of unique page layouts, the CMS structure and how much custom motion you need. The number of pages matters much less.</p></div>
"""),
("table", "Typical price ranges", """
<div class="post-table" role="region" aria-label="Webflow website price ranges" tabindex="0"><table>
<thead><tr><th>Option</th><th>Typical cost</th><th>Time</th><th>Best for</th></tr></thead>
<tbody>
<tr><td><b>Template, set up yourself</b></td><td>$0 to $150 plus your time</td><td>1 to 3 weeks</td><td>Testing an idea</td></tr>
<tr><td><b>Template, customised by a freelancer</b></td><td>$1,000 to $4,000</td><td>1 to 3 weeks</td><td>Small sites on a tight budget</td></tr>
<tr><td><b>Custom design and build, studio</b></td><td>$5,000 to $20,000</td><td>3 to 6 weeks</td><td>Startups and growing companies</td></tr>
<tr><td><b>Large site, big agency</b></td><td>$30,000 and up</td><td>2 to 4 months</td><td>Enterprise, many teams and languages</td></tr>
</tbody></table></div>
"""),
("drivers", "What moves the price", """
<ul>
<li><b>Unique layouts.</b> Home, service, pricing, case study and blog templates each take design and build time. Extra pages on an existing layout are cheap.</li>
<li><b>CMS structure.</b> A blog is simple. Linked collections for case studies, integrations, team and resources take more planning.</li>
<li><b>Motion and interactions.</b> Scroll animations and interactive product scenes add days, not hours.</li>
<li><b>Content.</b> Ready copy and images keep the price down. Copywriting and imagery add to it.</li>
<li><b>Integrations and languages.</b> CRM forms, analytics, gated content and extra locales all add scope.</li>
</ul>
[[cta]]
"""),
("running", "Costs after launch", """
<p>Webflow charges a monthly site plan for hosting and the CMS, and a workspace plan if your team needs editing seats. Plan prices change, so check Webflow's pricing page for current numbers. Beyond that there is no plugin licence or server maintenance to pay for, which is where Webflow usually saves money compared with WordPress. See <a href="../blog/webflow-vs-wordpress.html">Webflow vs WordPress</a>.</p>
"""),
("quote", "How to get an accurate quote", """
<ul>
<li>List the page types you need, not just the page count.</li>
<li>Say what content you already have and what needs writing.</li>
<li>Share two or three websites you like and why.</li>
<li>Ask for a fixed price with written scope and timeline before work starts.</li>
</ul>
"""),
  ],
  faq=[("Is Webflow expensive?", "The plan is a monthly fee, but there is no hosting, plugin or maintenance bill on top. Over a year, many teams spend less than on a WordPress site they keep patching."),
       ("How long does a Webflow website take?", "Usually 3 to 6 weeks for 5 to 10 custom pages, depending on how ready the content is."),
       ("Can I edit the site myself after launch?", "Yes. Your team edits text, images and CMS items in the Webflow editor without touching the design."),
       ("Is a Webflow template good enough?", "For testing an idea, yes. Once the site has to sell a real product, a custom design usually converts better and is easier to grow."),
       ("Do you offer fixed prices?", "Yes. You get a written plan with scope, timeline and a fixed price within 24 hours."),
  ],
),
dict(
  slug="web-design-agency-vs-freelancer",
  title="Web Design Agency vs Freelancer: Which Should You Hire? | Sorvel",
  h1="Web design agency vs freelancer: which one to hire",
  card="Cost, speed, risk and quality compared, plus a third option most companies overlook: a small senior studio.",
  desc="Web design agency vs freelancer compared on cost, quality, speed and risk, with a third option, the small senior studio, and questions to ask before you hire.",
  cat="Hiring", date="2026-10-31", svc=("websites", "website design and development"),
  cover=("c-web-design-agency-vs-freelancer", "A freelance web designer working on a laptop"),
  lead="Hiring for a website usually comes down to three choices: a freelancer, a large agency or a small senior studio. Each one fits a different situation.",
  sections=[
("short", "The short answer", """
<p><b>Hire a freelancer</b> for a small, clearly defined job on a tight budget. <b>Hire a large agency</b> when you need many specialists at once: research, content, paid media and development. <b>Hire a small senior studio</b> when you want agency-level design and build quality with one person accountable and a price that fits a startup.</p>
"""),
("table", "Side by side", """
<div class="post-table" role="region" aria-label="Freelancer, agency and studio compared" tabindex="0"><table>
<thead><tr><th></th><th>Freelancer</th><th>Senior studio</th><th>Large agency</th></tr></thead>
<tbody>
<tr><td><b>Typical website cost</b></td><td>$1,000 to $8,000</td><td>$5,000 to $20,000</td><td>$30,000 and up</td></tr>
<tr><td><b>Speed</b></td><td>Fast if available</td><td>Fast, 3 to 6 weeks</td><td>Slower, more meetings</td></tr>
<tr><td><b>Who does the work</b></td><td>One person</td><td>Senior lead does the key work</td><td>Often junior staff</td></tr>
<tr><td><b>Range of skills</b></td><td>Usually one</td><td>Design, build, SEO basics</td><td>Everything</td></tr>
<tr><td><b>Main risk</b></td><td>Disappears or gets overloaded</td><td>Limited capacity</td><td>Cost and handovers</td></tr>
</tbody></table></div>
"""),
("checks", "What to check before you hire anyone", """
<ul>
<li><b>Live work, not only mockups.</b> Ask for links to sites they built that are online today.</li>
<li><b>Verified reviews.</b> Reviews on Upwork, Fiverr or Clutch are harder to fake than quotes on a website.</li>
<li><b>Who does the work.</b> Ask who designs and who builds your site day to day.</li>
<li><b>A written scope.</b> Pages, features, revisions, timeline and price on paper before you start.</li>
<li><b>What happens after launch.</b> Training, support and who owns the files and accounts.</li>
</ul>
[[cta]]
"""),
("us", "Where Sorvel fits", """
<p>Sorvel is a small senior studio. The founder, Mykola Tanasiichuk, has designed and built websites for more than 11 years, with 600+ completed projects and 600+ five-star reviews on Upwork and Fiverr Pro. You get one accountable lead, a fixed price and a site built in Webflow, Framer or WordPress. See <a href="../reviews.html">client reviews</a>.</p>
"""),
  ],
  faq=[("Is a freelancer cheaper than an agency?", "Usually yes, by half or more. The trade-off is capacity and range of skills, which matters more as the project grows."),
       ("What is a boutique web design studio?", "A small team led by a senior designer or developer who does the key work personally, with agency-level process and a smaller overhead."),
       ("How do I know a web designer is reliable?", "Look for live sites, verified platform reviews, a written scope and clear ownership of files and accounts."),
       ("How much should I budget for a business website?", "For a custom site with a professional team, plan $5,000 to $20,000 depending on pages, CMS and content."),
  ],
),
dict(
  slug="framer-vs-wordpress",
  title="Framer vs WordPress in 2026: Which Is Right for Your Website? | Sorvel",
  h1="Framer vs WordPress: which is right for your website",
  card="Speed, design, editing, SEO, plugins and cost: when Framer is the smarter choice and when WordPress still wins.",
  desc="Framer vs WordPress compared for business websites in 2026: design freedom, speed, editing, SEO, plugins, e-commerce and cost, with clear advice on which to choose.",
  cat="Platforms", date="2026-10-31", svc=("websites", "website design and development"),
  cover=("c-framer-vs-wordpress", "A designer working at a desk with app layout printouts"),
  lead="Framer and WordPress sit at opposite ends: one is a design tool that publishes websites, the other a flexible system that can become almost anything. Here is how to choose.",
  sections=[
("short", "The short answer", """
<p><b>Choose Framer</b> for a modern marketing or launch site where design and motion matter, the content is fairly simple and you want zero maintenance.</p>
<p><b>Choose WordPress</b> when the site needs complex features, a large store, memberships or deep custom logic, and you have someone to maintain it.</p>
"""),
("table", "Framer vs WordPress at a glance", """
<div class="post-table" role="region" aria-label="Framer and WordPress compared" tabindex="0"><table>
<thead><tr><th></th><th>Framer</th><th>WordPress</th></tr></thead>
<tbody>
<tr><td><b>Best for</b></td><td>Startup and launch sites, portfolios</td><td>Complex sites, stores, memberships</td></tr>
<tr><td><b>Design and motion</b></td><td>Excellent, close to Figma</td><td>Depends on theme and developer</td></tr>
<tr><td><b>Maintenance</b></td><td>None, hosting included</td><td>Updates, backups, security</td></tr>
<tr><td><b>Speed</b></td><td>Fast by default</td><td>Varies with plugins and hosting</td></tr>
<tr><td><b>CMS</b></td><td>Simple collections</td><td>Very flexible</td></tr>
<tr><td><b>Plugins</b></td><td>Small set</td><td>Huge ecosystem</td></tr>
<tr><td><b>E-commerce</b></td><td>Not a store platform</td><td>WooCommerce</td></tr>
</tbody></table></div>
"""),
("framer", "When Framer wins", """
<ul>
<li>You need to launch in weeks, not months.</li>
<li>The site is mostly pages, a blog and forms.</li>
<li>Your designer wants to update the site directly.</li>
<li>You never want to think about plugin updates or hosting again.</li>
</ul>
[[cta]]
"""),
("wordpress", "When WordPress wins", """
<ul>
<li>Online store with many products and custom checkout rules.</li>
<li>Memberships, courses, bookings or directories.</li>
<li>Large content libraries with custom fields and logic.</li>
<li>You want full control over code and hosting.</li>
</ul>
<p>If your content is growing fast but you do not need WordPress features, Webflow is often the middle ground. See <a href="../blog/webflow-vs-framer.html">Webflow vs Framer</a> and <a href="../blog/webflow-vs-wordpress.html">Webflow vs WordPress</a>.</p>
"""),
  ],
  faq=[("Is Framer good for SEO?", "Yes for most marketing sites: clean pages, fast loading, editable meta tags and sitemaps. Very large content sites get more control on Webflow or WordPress."),
       ("Is Framer cheaper than WordPress?", "Framer has a monthly plan but no maintenance costs. WordPress hosting is cheap, but updates, plugins and fixes add up over a year."),
       ("Can I move from WordPress to Framer?", "Yes. Pages are rebuilt in Framer, blog content is imported and old URLs get 301 redirects to keep rankings."),
       ("Do you build on both?", "Yes. We design in Figma and build in Framer, Webflow or WordPress depending on what the site needs."),
  ],
),
dict(
  slug="website-redesign-cost",
  title="How Much Does a Website Redesign Cost in 2026? | Sorvel",
  h1="How much a website redesign costs in 2026",
  card="Redesign price ranges, what is included, signs you need one, and how to redesign without losing your search traffic.",
  desc="How much a website redesign costs in 2026: price ranges, what drives the cost, a redesign vs a refresh, timelines and how to keep your SEO during a redesign.",
  cat="Pricing", date="2026-10-31", svc=("websites", "website design and development"),
  cover=("c-website-redesign-cost", "A professional working on a website redesign at her desk"),
  lead="A redesign is a chance to fix what is not working, not just to change colours. What it costs depends on how much has to change underneath.",
  sections=[
("short", "The short answer", """
<p>A professional redesign of a small to mid-size business website usually costs <b>$5,000 to $20,000</b> and takes <b>3 to 8 weeks</b>. With our studio a full redesign and rebuild starts <b>from $6,900</b>. If only the look needs updating, a lighter refresh or a monthly design plan can cost much less.</p>
"""),
("types", "Refresh, redesign or rebuild", """
<div class="post-table" role="region" aria-label="Types of website redesign" tabindex="0"><table>
<thead><tr><th>Type</th><th>What changes</th><th>Typical cost</th></tr></thead>
<tbody>
<tr><td><b>Refresh</b></td><td>Visual style, key pages, same platform and structure</td><td>$1,500 to $5,000</td></tr>
<tr><td><b>Redesign</b></td><td>New structure, messaging and design on the same platform</td><td>$5,000 to $15,000</td></tr>
<tr><td><b>Redesign and replatform</b></td><td>New design and a move, for example WordPress to Webflow</td><td>$7,000 to $25,000</td></tr>
</tbody></table></div>
"""),
("signs", "Signs you need a redesign", """
<ul>
<li>Visitors arrive but rarely enquire or sign up.</li>
<li>The site looks older than your product or service.</li>
<li>Your team needs a developer for simple changes.</li>
<li>Pages load slowly on phones or fail Core Web Vitals.</li>
<li>The message no longer matches who you sell to.</li>
</ul>
[[cta]]
"""),
("seo", "How to redesign without losing traffic", """
<ul>
<li>List the pages that bring visits and links before you change anything.</li>
<li>Keep URLs where you can, and 301-redirect every one that changes.</li>
<li>Carry over titles, descriptions and structured data.</li>
<li>Watch Search Console for a few weeks after launch.</li>
</ul>
<p>The full checklist is in <a href="../blog/migrate-wordpress-to-webflow-without-losing-seo.html">how to migrate without losing SEO</a>.</p>
"""),
  ],
  faq=[("How long does a website redesign take?", "Usually 3 to 8 weeks, depending on the number of layouts, content readiness and whether the platform changes."),
       ("Will a redesign hurt my SEO?", "Not if URLs are kept or redirected, metadata is carried over and indexing is checked after launch."),
       ("Should I redesign or just refresh?", "Refresh if the structure and message still work. Redesign if visitors do not convert or the site no longer fits the business."),
       ("Can you redesign my site on the same platform?", "Yes. We redesign on Webflow, Framer or WordPress, or move you to a better fit if it makes sense."),
  ],
),
dict(
  slug="website-design-for-ai-startups",
  title="Website Design for AI Startups: What Works in 2026 | Sorvel",
  h1="Website design for AI startups: what actually works in 2026",
  card="How AI startups explain the product, show it working and earn trust on the website, with costs and timelines.",
  desc="Website design for AI startups in 2026: how to explain an AI product in seconds, show it working, handle trust and data questions, and what a website costs.",
  cat="Niches", date="2026-11-01", svc=("saas-website-design", "SaaS website design"),
  cover=("c-website-design-for-ai-startups", "A developer working with two monitors in a startup office"),
  lead="Every AI startup says it saves time with AI. The websites that convert are the ones that make the product concrete in the first few seconds. Here is how to do that.",
  sections=[
("short", "The short answer", """
<p>A strong AI startup website does three things: it names the job your product does in plain words, it shows the product doing that job with real screens or a short demo, and it answers trust questions about data, accuracy and security before the visitor has to ask.</p>
<p>With our studio an AI startup website starts <b>from $6,900</b> and takes <b>3 to 6 weeks</b>. A single launch or waitlist page starts <b>from $2,400</b>.</p>
"""),
("message", "Lead with the job, not the technology", """
<ul>
<li><b>Name the outcome.</b> "Answer support tickets in seconds" beats "AI-powered customer experience platform".</li>
<li><b>Say who it is for.</b> One audience in the headline converts better than "for teams of all sizes".</li>
<li><b>Skip the buzzwords.</b> Words like "revolutionary" and "next-generation" are what every competitor says.</li>
</ul>
"""),
("show", "Show the product working", """
<p>AI products are hard to picture. Visitors trust what they can see: a real interface, a before and after, a short looping demo of an input becoming an output. Abstract glowing brains and robot illustrations do the opposite.</p>
[[cta]]
"""),
("trust", "Answer trust questions on the page", """
<ul>
<li>Where the data goes and whether it trains the model.</li>
<li>Security and compliance (SOC 2, GDPR) if you have them.</li>
<li>How accurate the output is and how a human stays in control.</li>
<li>Integrations with the tools the buyer already uses.</li>
</ul>
<p>A dedicated "Security" or "How it works" section often lifts demo requests more than another feature block.</p>
"""),
("platform", "Webflow or Framer for an AI startup", """
<p>Pre-seed and seed teams with a few pages usually launch faster on Framer. Teams that publish a changelog, docs, integrations or a blog are better served by Webflow's CMS. See <a href="../blog/webflow-vs-framer.html">Webflow vs Framer</a>.</p>
"""),
  ],
  faq=[("How long does an AI startup website take?", "Usually 3 to 6 weeks for 5 to 10 pages, or 1 to 2 weeks for a single launch page."),
       ("Should an AI startup use a template?", "Before product-market fit, a template can be enough. Once you raise or sell to larger buyers, a custom site that shows your real product usually converts better."),
       ("Do you design product UI as well?", "Yes. We design the product interface in Figma, so the website and the app look like one product."),
  ],
),
dict(
  slug="b2b-website-design",
  title="B2B Website Design: How to Build a Site That Generates Leads | Sorvel",
  h1="B2B website design: how to build a site that generates leads",
  card="What B2B buyers look for, the pages every B2B site needs, and the details that turn visits into qualified leads.",
  desc="B2B website design guide: what B2B buyers look for, the pages and proof every B2B site needs, lead capture that works, and typical costs and timelines.",
  cat="Niches", date="2026-11-01", svc=("websites", "website design and development"),
  cover=("c-b2b-website-design", "A professional working at a computer in a busy office"),
  lead="B2B buyers rarely buy on the first visit. They come back several times, often with colleagues, and the website has to answer a different question each time.",
  sections=[
("short", "The short answer", """
<p>A B2B website that generates leads makes it clear who you help and with what, proves it with case studies and named clients, and gives every type of visitor a next step, from a guide to download to a quote request.</p>
<p>A professional B2B website usually costs <b>$5,000 to $20,000</b>. With our studio it starts <b>from $6,900</b>.</p>
"""),
("pages", "Pages every B2B website needs", """
<div class="post-table" role="region" aria-label="B2B website pages" tabindex="0"><table>
<thead><tr><th>Page</th><th>The question it answers</th></tr></thead>
<tbody>
<tr><td><b>Home</b></td><td>Is this for a company like mine?</td></tr>
<tr><td><b>Solutions or industries</b></td><td>Do they understand my situation?</td></tr>
<tr><td><b>Case studies</b></td><td>Have they done this before?</td></tr>
<tr><td><b>Pricing or how we work</b></td><td>What will it cost and what happens next?</td></tr>
<tr><td><b>About</b></td><td>Who will I actually work with?</td></tr>
<tr><td><b>Contact</b></td><td>How do I start with the least effort?</td></tr>
</tbody></table></div>
"""),
("proof", "Proof beats promises", """
<ul>
<li><b>Case studies with specifics:</b> the problem, what was done and what changed.</li>
<li><b>Named logos and quotes</b> from real people with their role.</li>
<li><b>Certifications and partners</b> that matter in your industry.</li>
</ul>
[[cta]]
"""),
("leads", "Lead capture that works for B2B", """
<ul>
<li>A short contact form: name, email, company, one question. Every extra field costs leads.</li>
<li>A softer option for early researchers, like a guide, checklist or pricing sheet.</li>
<li>Clear response time, for example "reply within one business day".</li>
<li>CRM integration, so no lead sits in an inbox.</li>
</ul>
"""),
  ],
  faq=[("How many pages does a B2B website need?", "Most start with 6 to 12 pages and grow through case studies, industry pages and articles."),
       ("Which platform is best for a B2B website?", "Webflow is a strong default for marketing teams that publish often. WordPress fits when you need complex functionality."),
       ("How long does a B2B website take?", "Usually 4 to 8 weeks, depending on the number of layouts and how ready the content is."),
  ],
),
dict(
  slug="law-firm-website-design",
  title="Law Firm Website Design: What Clients Look For in 2026 | Sorvel",
  h1="Law firm website design: what clients look for before they call",
  card="Trust signals, practice area pages, calls to action and local SEO for law firm websites that turn visitors into consultations.",
  desc="Law firm website design guide for 2026: the trust signals clients look for, practice area pages, call-first design, local SEO and what a law firm website costs.",
  cat="Niches", date="2026-11-01", svc=("websites", "website design and development"),
  cover=("c-law-firm-website-design", "A lawyer on the phone working on a laptop"),
  lead="People looking for a lawyer are often stressed and in a hurry. A good law firm website calms them down and makes the next step obvious.",
  sections=[
("short", "The short answer", """
<p>A law firm website that brings in consultations shows who you help and where, proves experience early, and puts a way to call or book on every screen, especially on mobile. Practice area pages and local SEO bring most of the search traffic.</p>
"""),
("trust", "Trust signals clients look for", """
<ul>
<li>Real photos of the attorneys, with bar admissions and years of practice.</li>
<li>Results and reviews, within the rules of your bar.</li>
<li>Languages spoken, if you serve more than one community.</li>
<li>A clear, calm tone with no legal jargon in the headlines.</li>
</ul>
"""),
("pages", "Practice area pages", """
<p>Each practice area deserves its own page: what it covers, typical situations, how the process works and an FAQ. These pages rank for searches like "DUI lawyer in Houston" and give visitors confidence you handle their exact case.</p>
[[cta]]
"""),
("mobile", "Call-first on mobile", """
<p>Most legal searches happen on phones. A sticky call button, a short contact form and click-to-call numbers matter more than any animation. We built this approach for a bilingual criminal defense landing page in Webflow.</p>
"""),
  ],
  faq=[("How much does a law firm website cost?", "A custom site with a professional team usually costs $5,000 to $20,000; with our studio from $6,900, or a single landing page from $2,400."),
       ("Which platform is best for a law firm?", "Webflow or WordPress. Both handle practice area pages, blogs and local SEO well."),
       ("Can the site be bilingual?", "Yes. We design and build sites in two or more languages."),
  ],
),
dict(
  slug="travel-website-design",
  title="Travel and Tourism Website Design: A Practical Guide | Sorvel",
  h1="Travel and tourism website design: a practical guide",
  card="How destination and tour websites inspire visitors, help them plan and turn interest into bookings and inquiries.",
  desc="Travel and tourism website design guide: inspiring imagery, experience finders, itineraries, booking and inquiry flows, mobile planning and typical costs.",
  cat="Niches", date="2026-11-01", svc=("websites", "website design and development"),
  cover=("c-travel-website-design", "A person browsing a travel agency website on a laptop"),
  lead="Travel websites sell a feeling first and a plan second. The best ones move visitors from 'that looks amazing' to 'send me a quote' without friction.",
  sections=[
("short", "The short answer", """
<p>A travel or tourism website needs big, honest imagery, a quick way to find the right experience, ready-made itineraries or tours with dates and prices, and a short inquiry or booking form. Most visitors plan on a phone, so mobile comes first.</p>
"""),
("flow", "From inspiration to inquiry", """
<ol>
<li><b>Inspire:</b> a strong hero, the destination's story and real photos.</li>
<li><b>Explore:</b> filters by interest, such as diving, culture, family or adventure.</li>
<li><b>Plan:</b> itineraries with duration, level and price.</li>
<li><b>Act:</b> a short inquiry or booking form with a clear reply time.</li>
</ol>
"""),
("details", "Details that build confidence", """
<ul>
<li>Best time to visit, how to get there and practical info.</li>
<li>Named reviews with the trip and date.</li>
<li>Responsible travel and local partners, if they matter to your audience.</li>
</ul>
[[cta]]
"""),
("platform", "Platform choice", """
<p>WordPress suits content-rich destination sites with many tours and booking plugins. Webflow suits design-led tour operators that want an easy CMS without plugin maintenance.</p>
"""),
  ],
  faq=[("How much does a travel website cost?", "A custom design and build usually costs $5,000 to $20,000 with a professional team; with our studio from $6,900."),
       ("Can you add online booking?", "Yes, through booking integrations or a simple inquiry flow, depending on how you sell trips."),
       ("Do you design for mobile first?", "Yes. Every page is designed for phones in Figma, not squeezed afterwards."),
  ],
),
dict(
  slug="landing-page-cost",
  title="How Much Does a Landing Page Cost in 2026? Full Price Guide | Sorvel",
  h1="How much a landing page costs in 2026",
  card="Price ranges for landing pages from templates to studios, a line-by-line cost breakdown, hidden costs and how to get a fixed quote.",
  desc="How much a landing page costs in 2026: price ranges from DIY to studios, a cost breakdown by task, what drives the price, hidden costs, timelines and how to get a fixed quote.",
  cat="Pricing", date="2026-11-01", svc=("websites", "website design and development"),
  cover=("c-landing-page-cost", "An entrepreneur reviewing charts on a desktop computer"),
  lead="A landing page has one job: turn a specific visitor into a lead, a sign-up or a sale. What you pay depends on how much strategy, design, building and testing goes into that one job. Here is the full picture, with real numbers.",
  sections=[
("short", "The short answer", """
<p>A professionally designed and built landing page usually costs <b>$1,500 to $6,000</b> in 2026. A template you set up yourself can cost almost nothing, and a page from a conversion agency with ongoing testing can cost <b>$5,000 or more every month</b>.</p>
<p>With our studio a landing page starts <b>from $2,400</b>, each extra page on the same design <b>from $600</b>, and it is usually live in <b>1 to 2 weeks</b>.</p>
<div class="post-note"><b>Key takeaways</b><p>You pay for strategy and conversion work, not for the number of sections. A cheap page that does not convert is the most expensive option once you add up ad spend. Always ask what is included: copy, integrations, tracking and revisions.</p></div>
"""),
("table", "Landing page price ranges in 2026", """
<div class="post-table" role="region" aria-label="Landing page price ranges" tabindex="0"><table>
<thead><tr><th>Option</th><th>Typical cost</th><th>Time</th><th>Best for</th></tr></thead>
<tbody>
<tr><td><b>Template or page builder, yourself</b></td><td>$0 to $300 plus your time</td><td>1 to 5 days</td><td>Quick tests, very small budgets</td></tr>
<tr><td><b>Freelancer</b></td><td>$500 to $3,000</td><td>1 to 3 weeks</td><td>Simple campaigns with ready copy</td></tr>
<tr><td><b>Senior studio</b></td><td>$2,400 to $6,000</td><td>1 to 2 weeks</td><td>Paid traffic, launches, lead generation</td></tr>
<tr><td><b>CRO agency with testing</b></td><td>$5,000+ per month</td><td>Ongoing</td><td>High ad spend, constant experiments</td></tr>
</tbody></table></div>
<p>The ranges overlap because "landing page" means very different things. A one-screen waitlist page and a long sales page for a $10,000 service are both landing pages, but the second needs far more thinking, writing and proof.</p>
"""),
("breakdown", "Where the money goes: a cost breakdown", """
<p>For a typical studio landing page, the budget is roughly split like this:</p>
<div class="post-table" role="region" aria-label="Landing page cost breakdown" tabindex="0"><table>
<thead><tr><th>Task</th><th>Share of budget</th><th>What it covers</th></tr></thead>
<tbody>
<tr><td><b>Strategy and structure</b></td><td>15 to 20%</td><td>Audience, offer, objections, section order, the one action</td></tr>
<tr><td><b>Copy and messaging</b></td><td>10 to 20%</td><td>Headline, proof points, calls to action (if not supplied)</td></tr>
<tr><td><b>Design</b></td><td>30 to 35%</td><td>Desktop and mobile layouts in Figma, visuals, product scenes</td></tr>
<tr><td><b>Build</b></td><td>25 to 30%</td><td>Webflow, Framer or WordPress, responsive, fast, editable</td></tr>
<tr><td><b>Integrations and QA</b></td><td>5 to 10%</td><td>Forms, CRM, analytics, ad pixels, testing on devices</td></tr>
</tbody></table></div>
<p>When a quote is much lower than the market, one of these lines is usually missing. Most often it is strategy and QA, which are exactly the parts that decide whether the page converts and whether your tracking works.</p>
"""),
("drivers", "What moves the price up or down", """
<ul>
<li><b>Copy.</b> Ready, tested copy keeps the price down. Writing from scratch adds time, especially for complex B2B offers.</li>
<li><b>Length and proof.</b> A short page for a free trial needs less than a long page that sells a high-ticket service with case studies, pricing and FAQ.</li>
<li><b>Custom visuals.</b> Product scenes, illustrations and motion take longer than photography and simple layouts.</li>
<li><b>Integrations.</b> HubSpot, Salesforce, booking tools, payment links and event tracking each add setup and testing.</li>
<li><b>Variants.</b> Different pages for each ad campaign or audience are cheaper when they share one design system.</li>
<li><b>Languages.</b> A second language means a second round of layout checks, not only translation.</li>
<li><b>Platform.</b> Framer and Webflow are usually faster to build than a custom WordPress theme.</li>
</ul>
[[cta]]
"""),
("hidden", "Hidden costs to plan for", """
<ul>
<li><b>Platform plan.</b> Webflow and Framer charge a monthly site plan. Check their current pricing pages.</li>
<li><b>Tools.</b> Form tools, schedulers, CRM seats and analytics can add a small monthly cost.</li>
<li><b>Ad spend.</b> The page is only half of a campaign. A page that converts at 4% instead of 2% halves your cost per lead.</li>
<li><b>Changes after launch.</b> New offers and tests are easier if the page is built on reusable components your team can edit.</li>
</ul>
"""),
("roi", "How to judge if a landing page is worth it", """
<p>Work backwards from your numbers. If you spend $3,000 a month on ads and the page converts at 2%, moving it to 3% gives you 50% more leads for the same budget. For most businesses running paid traffic, a well-built page pays for itself within the first one or two months.</p>
<p>If you have no traffic plan yet, start smaller: one strong page, a clear offer and basic tracking. Then improve it with real data instead of guessing.</p>
"""),
("process", "How a landing page project runs", """
<ol>
<li><b>Brief.</b> You share the offer, audience, traffic source and examples you like.</li>
<li><b>Structure.</b> A section-by-section outline, agreed before design starts.</li>
<li><b>Design.</b> Desktop and mobile layouts in Figma, with one round of feedback built in.</li>
<li><b>Build.</b> The page goes live in Webflow, Framer or WordPress with forms and tracking connected.</li>
<li><b>Launch and check.</b> Speed, forms, pixels and mobile tested before traffic arrives.</li>
</ol>
<p>A page built this way is a good base for A/B tests later. See our <a href="../services/landing-pages.html">landing pages service</a>.</p>
"""),
("checklist", "Checklist before you ask for quotes", """
<ul>
<li>What is the single action you want visitors to take?</li>
<li>Where will traffic come from: ads, email, social or search?</li>
<li>Do you have copy, or do you need it written?</li>
<li>Which tools must the form connect to?</li>
<li>Two or three landing pages you like, and why.</li>
<li>Your budget range and launch date.</li>
</ul>
<p>Need a starting point? Use our <a href="../blog/website-brief-template.html">website brief template</a>.</p>
"""),
("mistakes", "Common mistakes that waste budget", """
<ul>
<li>Sending ad traffic to the homepage instead of a page built for that offer.</li>
<li>Several competing calls to action on one page.</li>
<li>A desktop-only design when most ad clicks come from phones.</li>
<li>No conversion tracking, so nobody knows what works.</li>
<li>Choosing the cheapest quote and rebuilding the page three months later.</li>
</ul>
"""),
  ],
  faq=[("How much does a landing page cost?", "Usually $1,500 to $6,000 with a professional team in 2026. With our studio from $2,400, extra pages on the same design from $600."),
       ("How long does a landing page take?", "Usually 1 to 2 weeks from brief to launch, depending on copy and integrations."),
       ("Is a landing page cheaper than a website?", "Yes, usually. A full website with several layouts and a CMS starts around $6,900 with our studio."),
       ("Which platform is best for a landing page?", "Framer or Webflow for speed and easy edits; WordPress if the rest of your site already runs on it."),
       ("Do you write the copy?", "We shape the structure and messaging. Full copywriting can be added to the scope."),
       ("Can you connect the form to our CRM?", "Yes. HubSpot, Salesforce, Pipedrive, email tools and booking tools are all common."),
       ("Do you offer A/B testing?", "Yes, as a monthly optimisation plan after launch, when the page has enough traffic to test."),
  ],
),
dict(
  slug="framer-website-cost",
  title="How Much Does a Framer Website Cost in 2026? Full Price Guide | Sorvel",
  h1="How much a Framer website costs in 2026",
  card="What a Framer site costs with templates, freelancers and studios, a cost breakdown, plan fees after launch and when Framer is the right choice.",
  desc="How much a Framer website costs in 2026: template, freelancer and studio price ranges, a cost breakdown, Framer plan fees, timelines, hidden costs and when to choose Framer over Webflow.",
  cat="Pricing", date="2026-11-01", svc=("websites", "website design and development"),
  cover=("c-framer-website-cost", "A designer sketching on a graphics tablet"),
  lead="Framer has become one of the fastest ways for startups and design-led brands to launch a polished, motion-rich website. Here is what it costs to do it properly, and what to watch for.",
  sections=[
("short", "The short answer", """
<p>A custom Framer website built by a professional team usually costs <b>$3,000 to $15,000</b> in 2026 and takes <b>2 to 5 weeks</b>. A single Framer landing page usually costs <b>$1,500 to $5,000</b>.</p>
<p>With our studio a Framer website starts <b>from $6,900</b> and a Framer landing page <b>from $2,400</b>. On top of that, Framer charges a monthly site plan; check Framer's pricing page for current fees.</p>
<div class="post-note"><b>Key takeaways</b><p>Framer is usually a little faster and cheaper to build than Webflow for the same design. The price follows the number of unique layouts and the amount of custom motion, not the number of pages.</p></div>
"""),
("table", "Framer website price ranges", """
<div class="post-table" role="region" aria-label="Framer website price ranges" tabindex="0"><table>
<thead><tr><th>Option</th><th>Typical cost</th><th>Time</th><th>Best for</th></tr></thead>
<tbody>
<tr><td><b>Template, set up yourself</b></td><td>$0 to $150</td><td>Days</td><td>Testing an idea</td></tr>
<tr><td><b>Template, customised by a freelancer</b></td><td>$800 to $3,000</td><td>1 to 2 weeks</td><td>Small sites on a tight budget</td></tr>
<tr><td><b>Custom design and build, senior studio</b></td><td>$3,000 to $15,000</td><td>2 to 5 weeks</td><td>Startups, SaaS, design-led brands</td></tr>
<tr><td><b>Large site, big agency</b></td><td>$20,000+</td><td>1 to 3 months</td><td>Many languages, complex CMS, big teams</td></tr>
</tbody></table></div>
"""),
("breakdown", "What you pay for", """
<div class="post-table" role="region" aria-label="Framer project cost breakdown" tabindex="0"><table>
<thead><tr><th>Part of the project</th><th>Typical share</th><th>Includes</th></tr></thead>
<tbody>
<tr><td><b>Discovery and structure</b></td><td>10 to 15%</td><td>Goals, sitemap, page outlines</td></tr>
<tr><td><b>Design in Figma</b></td><td>35 to 40%</td><td>Desktop and mobile, components, style system</td></tr>
<tr><td><b>Framer build</b></td><td>30 to 35%</td><td>Pages, breakpoints, CMS, interactions</td></tr>
<tr><td><b>Motion and polish</b></td><td>5 to 15%</td><td>Scroll effects, hover states, transitions</td></tr>
<tr><td><b>SEO and launch</b></td><td>5 to 10%</td><td>Meta tags, redirects, analytics, domain, QA</td></tr>
</tbody></table></div>
<p>Some freelancers design directly in Framer and skip Figma. That can be cheaper for very small sites, but a Figma design makes it easier to agree on the look before the build and to reuse the design later.</p>
"""),
("drivers", "What drives the price", """
<ul>
<li><b>Unique layouts.</b> Home, product, pricing, about and blog post templates each take design and build time. Extra pages on an existing layout are cheap.</li>
<li><b>Motion.</b> Subtle fades are quick. Scroll-driven product stories and interactive components take days.</li>
<li><b>CMS.</b> A simple blog is easy. Several linked collections, such as case studies, team and integrations, take more planning.</li>
<li><b>Content.</b> Ready copy and images keep the price down. Copywriting, illustration and photography add to it.</li>
<li><b>Languages.</b> Framer supports localisation, but every language needs layout checks.</li>
</ul>
[[cta]]
"""),
("running", "Costs after launch", """
<ul>
<li><b>Framer site plan,</b> billed monthly or yearly, depending on traffic, CMS limits and features.</li>
<li><b>Domain,</b> usually a small yearly fee with your registrar.</li>
<li><b>Tools,</b> such as form handling, analytics or a scheduler, if you use paid versions.</li>
<li><b>Updates.</b> Your team can edit text, images and CMS items itself. New layouts or sections are usually a small paid task or part of a monthly plan.</li>
</ul>
<p>There are no plugins to update and no servers to maintain, which is where Framer and Webflow save money compared with WordPress over a year.</p>
"""),
("when", "When Framer is the right choice, and when it is not", """
<div class="post-table" role="region" aria-label="When to choose Framer" tabindex="0"><table>
<thead><tr><th>Choose Framer if</th><th>Consider Webflow or WordPress if</th></tr></thead>
<tbody>
<tr><td>You need to launch in weeks</td><td>You publish a lot of content every week</td></tr>
<tr><td>Motion and visuals are part of the story</td><td>You need complex CMS structures and filters</td></tr>
<tr><td>Your designer will update the site</td><td>Many editors with roles work on the site</td></tr>
<tr><td>The content is simple: pages plus a blog</td><td>You need memberships, a store or custom logic</td></tr>
</tbody></table></div>
<p>More detail in <a href="../blog/webflow-vs-framer.html">Webflow vs Framer</a> and <a href="../blog/framer-vs-wordpress.html">Framer vs WordPress</a>.</p>
"""),
("process", "How a Framer project runs with us", """
<ol>
<li><b>Brief and plan.</b> You send a short brief and get a written plan with scope, timeline and a fixed price within 24 hours.</li>
<li><b>Design.</b> Every page designed in Figma for desktop and mobile, on one set of components.</li>
<li><b>Build.</b> The design is built natively in Framer with breakpoints, CMS and motion.</li>
<li><b>Launch.</b> SEO basics, redirects, analytics and testing on real devices.</li>
<li><b>Handover.</b> A short guide so your team can edit the site on its own.</li>
</ol>
"""),
("mistakes", "Mistakes that make Framer sites expensive", """
<ul>
<li>Starting the build before the content and structure are agreed.</li>
<li>Adding heavy motion everywhere, which slows the site and the project.</li>
<li>Choosing Framer for a site that will soon need a large CMS.</li>
<li>Skipping mobile design and fixing it after launch.</li>
</ul>
"""),
  ],
  faq=[("How much does a Framer website cost?", "Usually $3,000 to $15,000 with a professional team. With our studio from $6,900, or from $2,400 for a single landing page."),
       ("Is Framer cheaper than Webflow?", "A Framer build is often a little cheaper and faster for the same design. Plan fees are in a similar range."),
       ("How long does a Framer site take?", "Usually 2 to 5 weeks for a custom multi-page site, 1 to 2 weeks for a landing page."),
       ("Can my team edit a Framer site?", "Yes. Text, images and CMS items can be edited without a designer."),
       ("Is Framer good for SEO?", "For most marketing sites, yes: fast pages, editable meta tags, sitemaps and clean URLs."),
       ("Can you move my site to Framer?", "Yes. Pages are rebuilt in Framer, blog content is imported and old URLs get 301 redirects."),
  ],
),
dict(
  slug="shopify-store-design",
  title="Shopify Store Design in 2026: What Makes a Store Convert | Sorvel",
  h1="Shopify store design: what makes a store convert in 2026",
  card="Homepage, collection and product page design that sells, mobile shopping, trust signals, costs and how a custom Shopify design project works.",
  desc="Shopify store design guide for 2026: homepage, collection, product and cart design that converts, mobile-first shopping, trust signals, theme vs custom design and typical costs.",
  cat="E-commerce", date="2026-11-01", svc=("websites", "website design and development"),
  cover=("c-shopify-store-design", "An online store owner preparing orders in her shop"),
  lead="Most Shopify stores start from the same themes, so they end up looking alike. The stores that sell more are designed around how their customers actually shop, page by page. Here is what that means in practice.",
  sections=[
("short", "The short answer", """
<p>A Shopify store converts when shoppers find the right product in a few taps, understand why it is worth the price and trust the store enough to buy. That comes down to clear navigation, strong product pages, visible trust signals and a smooth cart, all designed for mobile first.</p>
<div class="post-note"><b>Key takeaways</b><p>Design the product page first, because that is where the decision happens. Put reviews, delivery and returns next to the buy button. Most store traffic is mobile, so the phone layout is the main layout.</p></div>
"""),
("pages", "The pages that matter most", """
<div class="post-table" role="region" aria-label="Key Shopify pages" tabindex="0"><table>
<thead><tr><th>Page</th><th>What it must do</th><th>Common mistake</th></tr></thead>
<tbody>
<tr><td><b>Homepage</b></td><td>Say what you sell and for whom, and route shoppers to the right collection</td><td>A slideshow of banners with no clear path</td></tr>
<tr><td><b>Collection</b></td><td>Make filtering, sorting and comparing easy</td><td>Too many products with no filters on mobile</td></tr>
<tr><td><b>Product</b></td><td>Show the product well, answer questions, make variants clear</td><td>Small photos and key details hidden in tabs</td></tr>
<tr><td><b>Cart</b></td><td>Remove doubt with totals, delivery and returns</td><td>Surprise costs at the last step</td></tr>
<tr><td><b>About and FAQ</b></td><td>Build trust in a brand people do not know yet</td><td>Generic copy with no real people or story</td></tr>
</tbody></table></div>
"""),
("product", "Designing a product page that sells", """
<ul>
<li><b>Large, real photos</b> with zoom, plus at least one image that shows scale or the product in use.</li>
<li><b>A clear price and variants.</b> Colour swatches beat dropdowns when colour matters.</li>
<li><b>Benefits before specs.</b> Three short reasons to buy, then the details.</li>
<li><b>Delivery and returns</b> next to the button, not only in the footer.</li>
<li><b>Reviews with photos</b> close to the top.</li>
<li><b>A sticky add-to-cart button</b> on mobile.</li>
</ul>
<p>For a varsity jacket brand we linked 44 colourways with swatches on one product page, so shoppers could compare without leaving it.</p>
[[cta]]
"""),
("mobile", "Mobile first, not mobile later", """
<p>On most stores the majority of visits come from phones. Design decisions should start there: thumb-friendly buttons, filters that open in a drawer, short forms and fast-loading images. A store that looks great on desktop and awkward on a phone loses the majority of its shoppers.</p>
"""),
("trust", "Trust signals that sell", """
<ul>
<li>Reviews and ratings, ideally with customer photos.</li>
<li>Clear delivery times, costs and returns.</li>
<li>Secure checkout and familiar payment options shown before checkout.</li>
<li>Real people behind the brand: founders, makers, the team.</li>
<li>Press mentions or partner logos if you have them.</li>
</ul>
"""),
("theme", "Theme or custom design?", """
<div class="post-table" role="region" aria-label="Shopify theme vs custom design" tabindex="0"><table>
<thead><tr><th></th><th>Theme with custom sections</th><th>Fully custom design</th></tr></thead>
<tbody>
<tr><td><b>Typical cost</b></td><td>Lower</td><td>Higher</td></tr>
<tr><td><b>Time</b></td><td>1 to 3 weeks</td><td>4 to 8 weeks</td></tr>
<tr><td><b>Brand fit</b></td><td>Good, within the theme's limits</td><td>Built around your brand</td></tr>
<tr><td><b>Best for</b></td><td>New stores, small catalogues</td><td>Brands that need to stand out</td></tr>
</tbody></table></div>
<p>Many stores do well with a strong theme plus custom-designed key pages: homepage, product page and collection. That keeps the cost down where it matters less.</p>
"""),
("process", "How a Shopify design project works with us", """
<ol>
<li><b>Brief.</b> Your products, customers, competitors and stores you like.</li>
<li><b>Structure.</b> Navigation, collections and the homepage flow.</li>
<li><b>Design in Figma.</b> Homepage, collection, product, cart and content pages, for desktop and mobile.</li>
<li><b>Build.</b> A custom Shopify theme or custom sections in your current theme.</li>
<li><b>Launch.</b> Testing on real devices, speed checks and a handover.</li>
</ol>
<p>Recent examples include a store for personalised children's books where the child is the hero, and a fashion store with 44 colourways.</p>
"""),
("mistakes", "Common Shopify design mistakes", """
<ul>
<li>Too many apps that slow the store down.</li>
<li>Pop-ups that cover the product on mobile.</li>
<li>Hiding shipping costs until checkout.</li>
<li>Stock photos instead of real product photography.</li>
<li>A homepage that tries to show every product at once.</li>
</ul>
"""),
  ],
  faq=[("How much does Shopify store design cost?", "It depends on the number of page templates and whether you use a theme or a fully custom design. We quote a fixed price after a short brief."),
       ("How long does a Shopify store design take?", "Usually 2 to 4 weeks for the design, and a similar time for the build."),
       ("Do I need a custom theme?", "Not always. A good theme with custom key pages works for many stores; fully custom design suits brands that need to stand out."),
       ("Can you redesign my existing store?", "Yes. We keep your products, customers and SEO, and redesign the pages that matter most."),
       ("Do you design for mobile?", "Yes. Every template is designed for phones first."),
       ("Can you move my store from WooCommerce to Shopify?", "Yes, as part of a redesign, with products, customers and redirects moved over."),
  ],
),
dict(
  slug="webflow-vs-wix",
  title="Webflow vs Wix in 2026: Which Is Better for a Business Website? | Sorvel",
  h1="Webflow vs Wix: which is better for a business website in 2026",
  card="Design freedom, SEO, speed, CMS and cost compared, with clear advice on when Wix is enough and when to move to Webflow.",
  desc="Webflow vs Wix for business websites in 2026: design freedom, SEO, speed, CMS, editing and cost compared, with advice on when to choose each.",
  cat="Platforms", date="2026-11-01", svc=("webflow-agency", "Webflow design and development"),
  cover=("c-webflow-vs-wix", "A business owner working on a laptop"),
  lead="Wix is easy to start with. Webflow is built for teams that want a professional, custom site they can grow. Here is how to choose.",
  sections=[
("short", "The short answer", """
<p><b>Choose Wix</b> if you are building a small site yourself and want the simplest setup. <b>Choose Webflow</b> if you want a custom design, clean code, strong SEO control and a CMS that scales as your business grows.</p>
"""),
("table", "Webflow vs Wix at a glance", """
<div class="post-table" role="region" aria-label="Webflow and Wix compared" tabindex="0"><table>
<thead><tr><th></th><th>Webflow</th><th>Wix</th></tr></thead>
<tbody>
<tr><td><b>Best for</b></td><td>Custom, professional sites</td><td>DIY small business sites</td></tr>
<tr><td><b>Design freedom</b></td><td>Full control</td><td>Template-based</td></tr>
<tr><td><b>CMS</b></td><td>Structured collections</td><td>Basic</td></tr>
<tr><td><b>SEO control</b></td><td>Fine control of meta, schema, redirects</td><td>Covers the basics</td></tr>
<tr><td><b>Learning curve</b></td><td>Steeper, usually built by a pro</td><td>Very easy</td></tr>
</tbody></table></div>
"""),
("move", "Signs it is time to move from Wix", """
<ul>
<li>The site looks like a template and no longer fits your brand.</li>
<li>You need more pages, a blog or case studies with structure.</li>
<li>SEO matters and you want more control.</li>
</ul>
[[cta]]
"""),
("how", "Moving from Wix to Webflow", """
<p>A move means rebuilding the design in Webflow, importing content and adding 301 redirects so you keep your rankings. The same principles apply as in our <a href="../blog/migrate-wordpress-to-webflow-without-losing-seo.html">WordPress to Webflow checklist</a>.</p>
"""),
  ],
  faq=[("Is Webflow better than Wix for SEO?", "Webflow gives more control over structure, schema and redirects, which matters as a site grows."),
       ("Is Webflow more expensive than Wix?", "Plans cost more and a professional build is usually needed, but you get a custom site that scales."),
       ("Can you move my Wix site to Webflow?", "Yes, with a content import and redirect map to keep rankings."),
  ],
),
dict(
  slug="website-brief-template",
  title="How to Write a Website Brief (Free Template) | Sorvel",
  h1="How to write a website brief, with a free template",
  card="What to include in a website brief so you get accurate quotes, plus a copy-ready template.",
  desc="How to write a website design brief: the questions to answer, what to include so agencies can quote accurately, and a free copy-ready brief template.",
  cat="Hiring", date="2026-11-01", svc=("websites", "website design and development"),
  cover=("c-website-brief-template", "A person writing notes next to a laptop"),
  lead="A clear brief gets you accurate quotes, fewer revisions and a better website. It does not need to be long, just specific.",
  sections=[
("short", "The short answer", """
<p>A good website brief answers seven questions: who you are, who the site is for, what visitors should do, which pages you need, what content you already have, which sites you like and why, and your budget and deadline.</p>
"""),
("template", "Copy-ready brief template", """
<ol>
<li><b>About us:</b> what we do in one or two sentences.</li>
<li><b>Audience:</b> who we sell to and what they care about.</li>
<li><b>Goal:</b> the main action, such as demo requests, sales or calls.</li>
<li><b>Pages:</b> list of page types, for example home, services, pricing, case studies, blog, contact.</li>
<li><b>Content:</b> what is ready (copy, photos, logo) and what we need help with.</li>
<li><b>References:</b> two or three websites we like, and what we like about them.</li>
<li><b>Platform and integrations:</b> Webflow, Framer, WordPress or open; CRM, booking, analytics.</li>
<li><b>Budget and timeline:</b> a range and a launch date.</li>
</ol>
[[cta]]
"""),
("mistakes", "Common brief mistakes", """
<ul>
<li>Listing features without saying what the site should achieve.</li>
<li>No budget range, which makes quotes impossible to compare.</li>
<li>"Modern and clean" as the only design direction. Show examples instead.</li>
</ul>
"""),
  ],
  faq=[("How long should a website brief be?", "One or two pages is plenty if it answers the key questions."),
       ("Should I include a budget?", "Yes. A range helps agencies suggest the right scope instead of guessing."),
       ("Can I send a brief to Sorvel?", "Yes. Use the brief form on the contact page and you get a written plan with a fixed price within 24 hours."),
  ],
),
dict(
  slug="how-to-choose-a-web-design-agency",
  title="How to Choose a Web Design Agency in 2026: 12 Questions to Ask | Sorvel",
  h1="How to choose a web design agency: 12 questions to ask",
  card="The questions that separate reliable web design partners from risky ones, how to compare proposals and the red flags to watch for.",
  desc="How to choose a web design agency in 2026: where to find good options, 12 questions to ask before you hire, how to compare proposals fairly and the red flags to watch for.",
  cat="Hiring", date="2026-11-01", svc=("websites", "website design and development"),
  cover=("c-how-to-choose-a-web-design-agency", "Two business partners reviewing a proposal on a laptop"),
  lead="Most website projects that go wrong could have been spotted before they started. A few good questions, asked early, show you who will deliver and who will disappear halfway. Here is how to choose with confidence.",
  sections=[
("short", "The short answer", """
<p>Choose the agency that shows relevant live work, explains a clear process, gives you a written fixed scope and price, and tells you exactly who will do the work. Price matters, but unclear scope is what usually makes a website project expensive.</p>
<div class="post-note"><b>Key takeaways</b><p>Shortlist two or three teams, send them the same brief, and compare written proposals line by line. Ask to see live sites, not only mockups. Make sure you own the domain, files and accounts.</p></div>
"""),
("where", "Where to find good options", """
<ul>
<li><b>Referrals</b> from founders or marketers you trust.</li>
<li><b>Directories with verified reviews,</b> such as Clutch or the Webflow Experts directory.</li>
<li><b>Freelance platforms</b> like Upwork and Fiverr Pro, where reviews come from real paid projects.</li>
<li><b>Sites you admire.</b> Many sites credit their studio in the footer.</li>
</ul>
"""),
("questions", "12 questions to ask before you hire", """
<ol>
<li><b>Can I see live websites you built?</b> Mockups are easy to polish. Live sites show real build quality and speed.</li>
<li><b>Have you worked in my industry or with similar buyers?</b> Not essential, but it shortens the learning curve.</li>
<li><b>Who designs and who builds my site day to day?</b> Make sure the senior person you talk to is involved in the work.</li>
<li><b>What exactly is included in the price?</b> Pages, copy, images, SEO setup, integrations, training.</li>
<li><b>How many revision rounds are included?</b> And what happens if you need more.</li>
<li><b>What is the timeline, and what do you need from us?</b> Most delays come from missing content and slow feedback.</li>
<li><b>Which platform do you recommend, and why?</b> A good answer depends on how your team will use the site.</li>
<li><b>Will my team be able to edit the site without you?</b> Ask to see the editor.</li>
<li><b>How do you handle SEO, speed and accessibility?</b> Especially redirects if you are replacing an existing site.</li>
<li><b>Who owns the design files, domain and accounts?</b> The answer should be: you.</li>
<li><b>What happens after launch?</b> Support, fixes, training and the cost of small changes.</li>
<li><b>Where can I read verified client reviews?</b> Reviews on platforms with real transactions are harder to fake.</li>
</ol>
[[cta]]
"""),
("compare", "How to compare proposals fairly", """
<div class="post-table" role="region" aria-label="Comparing website proposals" tabindex="0"><table>
<thead><tr><th>Check</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td><b>Same scope</b></td><td>A cheaper quote often has fewer pages or no copy, SEO or integrations</td></tr>
<tr><td><b>Fixed price or estimate</b></td><td>Estimates can grow; fixed prices protect your budget</td></tr>
<tr><td><b>Timeline with milestones</b></td><td>Shows the team has planned the work</td></tr>
<tr><td><b>Payment terms</b></td><td>Payments tied to delivered stages reduce risk</td></tr>
<tr><td><b>Ownership and handover</b></td><td>You should own everything at the end</td></tr>
</tbody></table></div>
"""),
("budget", "What a fair budget looks like", """
<p>For a custom business website with a professional team, plan roughly <b>$5,000 to $20,000</b>. A single landing page usually costs <b>$1,500 to $6,000</b>. Large sites with many teams and languages can cost much more. See <a href="../blog/webflow-website-cost.html">what a Webflow website costs</a> and <a href="../blog/landing-page-cost.html">what a landing page costs</a>.</p>
"""),
("flags", "Red flags", """
<ul>
<li>No written scope, or a price that changes after the first conversation.</li>
<li>Only mockups and no live sites.</li>
<li>Vague answers about who does the work.</li>
<li>Pressure to sign quickly with a big upfront payment.</li>
<li>Keeping your domain, hosting or accounts in their name.</li>
<li>No questions about your business, only about the design you want.</li>
</ul>
"""),
("type", "Agency, studio or freelancer?", """
<p>A large agency suits big projects that need many specialists. A freelancer suits small, clear jobs. A small senior studio sits in between: agency-level quality with one accountable lead. See <a href="../blog/web-design-agency-vs-freelancer.html">agency vs freelancer</a> for the full comparison.</p>
"""),
("brief", "Make it easy to compare: send the same brief", """
<p>The fastest way to get comparable quotes is to send every team the same short brief: goals, pages, content status, examples, budget and deadline. Use our <a href="../blog/website-brief-template.html">website brief template</a>.</p>
"""),
  ],
  faq=[("How many agencies should I talk to?", "Two or three is usually enough to compare scope, price and fit."),
       ("Is the cheapest quote a risk?", "Often. Very low quotes usually leave out content, SEO, redirects or testing."),
       ("Should I choose a local agency?", "Not necessarily. Remote teams with a clear process and good reviews work well for most website projects."),
       ("What should a website contract include?", "Scope, timeline, price, payment stages, revisions, ownership and what happens after launch."),
       ("How long does choosing an agency take?", "One to two weeks is typical: shortlist, brief, proposals and a decision."),
       ("How does Sorvel quote?", "You send a short brief and get a written plan with scope, timeline and a fixed price within 24 hours."),
  ],
),
]
