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
]
