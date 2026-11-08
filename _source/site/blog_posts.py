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
  cat="Migrations", date="2026-11-03", svc=("wordpress-to-webflow-migration", "WordPress to Webflow migration"),
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
("challenges", "Common challenges during a WordPress to Webflow migration", """
<p>Most migrations hit the same problems. Knowing them before you start saves days of fixing after launch.</p>
<div class="post-table" role="region" aria-label="WordPress to Webflow migration challenges" tabindex="0"><table>
<thead><tr><th>Challenge</th><th>Why it happens</th><th>How to solve it</th></tr></thead>
<tbody>
<tr><td><b>Page builder markup</b></td><td>Elementor, Divi or WPBakery wrap content in layers of extra code and shortcodes</td><td>Export clean content, strip shortcodes and rebuild layouts as Webflow templates</td></tr>
<tr><td><b>URLs change for CMS items</b></td><td>Webflow keeps every CMS item inside a collection folder, such as /blog/post-name</td><td>Plan the new pattern once and cover it with 301 redirects</td></tr>
<tr><td><b>Plugin features</b></td><td>Forms, search, comments, memberships and sliders came from plugins</td><td>List each one in the audit and replace it with a Webflow feature, a light embed or a simpler solution</td></tr>
<tr><td><b>Complex categories</b></td><td>WordPress allows nested categories and unlimited tags</td><td>Model them as reference and multi-reference fields, and flatten deep hierarchies</td></tr>
<tr><td><b>CMS limits</b></td><td>Webflow plans have limits on CMS items and fields</td><td>Count posts, authors and categories first and pick the plan before importing</td></tr>
<tr><td><b>Images in posts</b></td><td>Images inside articles still point to the old server</td><td>Re-upload them during import and check that no post loads files from WordPress</td></tr>
<tr><td><b>Tables, embeds and custom blocks</b></td><td>Rich text in Webflow is simpler than the WordPress block editor</td><td>Use custom code embeds or rebuild them as components</td></tr>
</tbody></table></div>
<p>None of these block a migration. They only need to be planned in the audit, not discovered after the old site is switched off.</p>
"""),
("diy-or-hire", "Do it yourself or hire help?", """
<p>A small site with 10 to 20 pages and a short blog can be moved by a confident in-house team with this checklist. Bring in help when the site has hundreds of posts, many plugin features, a store, several languages or pages that bring most of your leads. The cost of a careful migration is small next to a few months of lost organic traffic.</p>
<p>See what a migration usually costs in our <a href="../blog/wordpress-to-webflow-migration-cost.html">WordPress to Webflow migration cost guide</a>, or how we run it on our <a href="../services/wordpress-to-webflow-migration.html">WordPress to Webflow migration</a> page.</p>
"""),
  ],
  faq=[("What are the biggest challenges in a WordPress to Webflow migration?", "Page builder markup and shortcodes, CMS URLs that change, plugin features that need a replacement, nested categories, CMS item limits and images still loading from the old server. All of them can be planned in the audit."),
       ("How long does a WordPress to Webflow migration take?", "Usually 1 to 3 weeks for a company site. Large blogs, a redesign on top or many integrations take longer."),
       ("Will my rankings drop after moving to Webflow?", "A short wobble is common while Google recrawls the site. With a complete redirect map and the same on-page SEO, rankings usually settle within a few weeks, and faster pages often help."),
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
('wf-takeaways', 'Summary', """
<div class="post-note"><b>In one minute</b><p>Both are excellent. Framer is faster for launch sites and motion. Webflow is stronger for content, SEO at scale and larger teams. Count your content types and editors, and the choice usually becomes obvious.</p></div>
"""),
('wf-scenarios', 'Real scenarios', """
<div class="post-table" role="region" aria-label="Webflow or Framer by scenario" tabindex="0"><table>
<thead><tr><th>Scenario</th><th>Better fit</th></tr></thead>
<tbody>
<tr><td>Pre-seed startup, waitlist and 3 pages</td><td>Framer</td></tr>
<tr><td>Series A SaaS with blog, changelog and integrations</td><td>Webflow</td></tr>
<tr><td>Design studio portfolio with heavy motion</td><td>Framer</td></tr>
<tr><td>Fintech firm with gated pages and many editors</td><td>Webflow</td></tr>
<tr><td>Campaign landing page for paid ads</td><td>Either</td></tr>
</tbody></table></div>
"""),
('wf-editing', 'Editing and collaboration', """
<ul>
<li><b>Framer:</b> edit on the canvas like a design file. Quick for designers; non-designers can move things they should not.</li>
<li><b>Webflow:</b> a separate editor for content people, so copy and CMS items change without touching the layout. Better for larger teams.</li>
</ul>
"""),
('wf-performance', 'Speed and SEO in practice', """
<p>Both platforms host on fast global networks and can reach good Core Web Vitals. In practice, speed depends on image sizes, fonts and how much motion is used. For SEO, both handle titles, descriptions and sitemaps; Webflow gives more control over structured CMS pages, redirects and schema when the site grows into hundreds of pages.</p>
"""),
  ],
  faq=[("Is Framer better than Webflow for SEO?", "For small sites both are fine. For sites that grow through content, Webflow gives more control over CMS structure, redirects and schema, which matters at scale."),
       ("Is Framer cheaper than Webflow?", "The site plans are in a similar range. A Framer build is often a little cheaper and faster, while Webflow pays back on content-heavy sites."),
       ("Which is easier for a marketing team to edit?", "Framer is easier for designers and quick text changes. Webflow's editor is safer for larger teams because people edit content without touching the layout."),
       ("Can you build on both?", "Yes. We design in Figma and build in Webflow or Framer, and recommend one after looking at your content and team."),
       ("Should a SaaS startup use Webflow or Framer?", "Pre-launch or seed with a few pages: Framer. Series A and later with a blog, changelog and SEO plans: Webflow."),
       ('Can I start on Framer and move to Webflow later?', 'Yes, but it is a rebuild. If you expect to grow content quickly, starting on Webflow saves that cost.'),
       ('Which is better for a portfolio?', 'Framer, in most cases, thanks to its motion tools and fast editing.'),
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
('ww-takeaways', 'Summary', """
<div class="post-note"><b>In one minute</b><p>For a marketing website your team edits itself, Webflow usually costs less to run and stays faster and more consistent. WordPress is still the right tool for complex functionality, large stores and teams with a developer on hand.</p></div>
"""),
('ww-team', 'How your team will work with each', """
<div class="post-table" role="region" aria-label="Team workflow on Webflow and WordPress" tabindex="0"><table>
<thead><tr><th>Task</th><th>Webflow</th><th>WordPress</th></tr></thead>
<tbody>
<tr><td><b>Publish a blog post</b></td><td>CMS editor, no developer</td><td>Block editor, no developer</td></tr>
<tr><td><b>Launch a new landing page</b></td><td>Built from existing components</td><td>Page builder or developer</td></tr>
<tr><td><b>Change the navigation</b></td><td>Designer in minutes</td><td>Theme settings or developer</td></tr>
<tr><td><b>Keep the site secure</b></td><td>Handled by Webflow</td><td>Your job: updates and backups</td></tr>
</tbody></table></div>
"""),
('ww-migrate', 'Moving from WordPress to Webflow', """
<p>A careful migration keeps your rankings: a content audit, a CMS model for posts and categories, content import, a full 301 redirect map, carried-over meta data and checks in Search Console after launch. It usually takes 1 to 3 weeks for a typical company site. Details in <a href="../blog/migrate-wordpress-to-webflow-without-losing-seo.html">how to migrate without losing SEO</a> and <a href="../blog/wordpress-to-webflow-migration-cost.html">what a migration costs</a>.</p>
"""),
('ww-checklist', 'Quick decision checklist', """
<ul>
<li>Do you need a store with many products or custom checkout? Choose WordPress or Shopify.</li>
<li>Do you need memberships, courses or bookings with custom rules? Choose WordPress.</li>
<li>Is your site mainly pages, a blog, case studies and forms? Choose Webflow.</li>
<li>Do you want no plugin updates and no security work? Choose Webflow.</li>
<li>Do you have a developer who maintains the site? WordPress becomes easier.</li>
</ul>
"""),
  ],
  faq=[("Is Webflow better than WordPress for SEO?", "Both can rank equally well. Webflow has the SEO basics built in and tends to be faster out of the box; WordPress reaches the same level with good plugins and hosting."),
       ("Is Webflow more expensive than WordPress?", "Per month, usually yes. Per year, often not, because there is no maintenance, plugin licences or developer time for routine changes."),
       ("Can I move from WordPress to Webflow without losing rankings?", "Yes, with a content audit, a full 301 redirect map, kept meta data and checks in Search Console after launch."),
       ("Is WordPress more secure than Webflow?", "WordPress can be secure, but security is your job. Webflow handles hosting, SSL and platform updates for you, so there are no plugins to patch."),
       ("Do you build on both?", "Yes. We design in Figma and build in Webflow, Framer or WordPress, and recommend the platform after looking at what your site needs to do."),
       ('How long does a WordPress to Webflow migration take?', 'Usually 1 to 3 weeks for a typical company site with a blog.'),
       ('Can I keep my blog posts when moving to Webflow?', 'Yes. Posts are imported into the Webflow CMS with their images, categories and metadata.'),
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
<p>Webflow charges a monthly site plan for hosting and the CMS, and a workspace plan if your team needs editing seats. Plan prices change, so check our <a href="../blog/webflow-pricing.html">Webflow pricing guide</a> for current numbers. Beyond that there is no plugin licence or server maintenance to pay for, which is where Webflow usually saves money compared with WordPress. See <a href="../blog/webflow-vs-wordpress.html">Webflow vs WordPress</a>.</p>
"""),
("quote", "How to get an accurate quote", """
<ul>
<li>List the page types you need, not just the page count.</li>
<li>Say what content you already have and what needs writing.</li>
<li>Share two or three websites you like and why.</li>
<li>Ask for a fixed price with written scope and timeline before work starts.</li>
</ul>
"""),
('wc-takeaways', 'Summary', """
<div class="post-note"><b>In one minute</b><p>The price of a Webflow website follows unique layouts, CMS structure and motion. Templates are cheap but limiting; a senior studio gives you a custom site your team can grow. Running costs are a monthly plan, with no plugins or servers to maintain.</p></div>
"""),
('wc-breakdown', 'Where the money goes', """
<div class="post-table" role="region" aria-label="Webflow website cost breakdown" tabindex="0"><table>
<thead><tr><th>Part</th><th>Typical share</th><th>Includes</th></tr></thead>
<tbody>
<tr><td><b>Discovery and structure</b></td><td>10 to 15%</td><td>Goals, sitemap, page outlines</td></tr>
<tr><td><b>Design in Figma</b></td><td>35 to 40%</td><td>Desktop and mobile, design system</td></tr>
<tr><td><b>Webflow build</b></td><td>30 to 35%</td><td>Clean classes, CMS, interactions</td></tr>
<tr><td><b>SEO and launch</b></td><td>10 to 15%</td><td>Meta, schema, redirects, QA, training</td></tr>
</tbody></table></div>
"""),
('wc-examples', 'Example scopes and prices', """
<div class="post-table" role="region" aria-label="Webflow website example scopes" tabindex="0"><table>
<thead><tr><th>Scope</th><th>Typical studio price</th><th>Time</th></tr></thead>
<tbody>
<tr><td>Single landing page</td><td>From $2,400</td><td>1 to 2 weeks</td></tr>
<tr><td>5 to 8 page startup site with blog</td><td>From $6,900</td><td>3 to 5 weeks</td></tr>
<tr><td>10 to 20 pages, several CMS collections</td><td>$10,000 to $20,000</td><td>5 to 8 weeks</td></tr>
<tr><td>WordPress to Webflow move, same design</td><td>From $2,900</td><td>1 to 3 weeks</td></tr>
</tbody></table></div>
"""),
('wc-process', 'How a Webflow project runs', """
<ol>
<li>Brief and a written plan with a fixed price within 24 hours.</li>
<li>Structure and messaging agreed.</li>
<li>Design in Figma for desktop and mobile.</li>
<li>Native Webflow build with a clean class system and CMS.</li>
<li>Launch, SEO checks and a short training for your team.</li>
</ol>
"""),
  ],
  faq=[("Is Webflow expensive?", "The plan is a monthly fee, but there is no hosting, plugin or maintenance bill on top. Over a year, many teams spend less than on a WordPress site they keep patching."),
       ("How long does a Webflow website take?", "Usually 3 to 6 weeks for 5 to 10 custom pages, depending on how ready the content is."),
       ("Can I edit the site myself after launch?", "Yes. Your team edits text, images and CMS items in the Webflow editor without touching the design."),
       ("Is a Webflow template good enough?", "For testing an idea, yes. Once the site has to sell a real product, a custom design usually converts better and is easier to grow."),
       ("Do you offer fixed prices?", "Yes. You get a written plan with scope, timeline and a fixed price within 24 hours."),
       ('Do I need a monthly plan after launch?', 'Webflow requires a site plan for hosting. Design support afterwards is optional.'),
       ('Can you build from our existing Figma design?', 'Yes. We build in Webflow from your designs, or design from scratch.'),
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
('af-takeaways', 'Summary', """
<div class="post-note"><b>In one minute</b><p>Freelancers suit small, clear jobs. Large agencies suit big projects with many specialists. A small senior studio gives you agency-level quality, one accountable lead and a startup-friendly price. Whoever you hire, ask for live work, a written scope and ownership of everything.</p></div>
"""),
('af-risk', 'How to reduce the risk with any option', """
<ul>
<li><b>Pay in stages</b> tied to delivered work: design approved, site built, site launched.</li>
<li><b>Get a written scope</b> with pages, features, revisions and timeline.</li>
<li><b>Own your accounts:</b> domain, Webflow or hosting, Figma files, analytics.</li>
<li><b>Ask for a handover:</b> a short training and documentation.</li>
<li><b>Check verified reviews</b> on platforms with real transactions.</li>
</ul>
"""),
('af-when', 'Which to choose by situation', """
<div class="post-table" role="region" aria-label="Choosing by situation" tabindex="0"><table>
<thead><tr><th>Situation</th><th>Best fit</th></tr></thead>
<tbody>
<tr><td>One landing page, copy ready, tight budget</td><td>Freelancer</td></tr>
<tr><td>Startup or growing company, 5 to 20 pages, needs to look established</td><td>Senior studio</td></tr>
<tr><td>Enterprise rebrand with research, content and media</td><td>Large agency</td></tr>
<tr><td>Ongoing design and development every month</td><td>Studio on a monthly plan</td></tr>
</tbody></table></div>
"""),
('af-questions', 'Questions to ask before you hire', """
<p>Ask who does the work, what is included, how revisions work, who owns the files and what happens after launch. The full list is in <a href="../blog/how-to-choose-a-web-design-agency.html">how to choose a web design agency</a>.</p>
"""),
  ],
  faq=[("Is a freelancer cheaper than an agency?", "Usually yes, by half or more. The trade-off is capacity and range of skills, which matters more as the project grows."),
       ("What is a boutique web design studio?", "A small team led by a senior designer or developer who does the key work personally, with agency-level process and a smaller overhead."),
       ("How do I know a web designer is reliable?", "Look for live sites, verified platform reviews, a written scope and clear ownership of files and accounts."),
       ("How much should I budget for a business website?", "For a custom site with a professional team, plan $5,000 to $20,000 depending on pages, CMS and content."),
       ('Can a small studio handle a large site?', 'Yes, for most marketing sites. Very large projects with many workstreams may need a bigger agency.'),
       ('Is it safe to hire remotely?', 'Yes, with a written scope, staged payments, verified reviews and ownership of your accounts.'),
  ],
),
dict(
  slug="framer-vs-wordpress",
  title="Framer vs WordPress in 2026: Which Is Right for Your Website? | Sorvel",
  h1="Framer vs WordPress: which is right for your website",
  card="Speed, design, editing, SEO, plugins and cost: when Framer is the smarter choice and when WordPress still wins.",
  desc="Framer vs WordPress in 2026: SEO, security, speed, design, languages, plugins and cost compared, plus a quick test to pick the right platform for your site.",
  cat="Platforms", date="2026-11-03", svc=("websites", "website design and development"),
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
('fw-takeaways', 'Summary', """
<div class="post-note"><b>In one minute</b><p>Framer wins on speed of launch, design quality and zero maintenance. WordPress wins on functionality: stores, memberships, complex content and thousands of plugins. If you need neither extreme, Webflow is often the middle ground.</p></div>
"""),
('fw-cost', 'Total cost over a year', """
<div class="post-table" role="region" aria-label="Framer and WordPress yearly cost" tabindex="0"><table>
<thead><tr><th></th><th>Framer</th><th>WordPress</th></tr></thead>
<tbody>
<tr><td><b>Build</b></td><td>Often faster, so usually a bit cheaper</td><td>Varies widely with theme and plugins</td></tr>
<tr><td><b>Hosting</b></td><td>Included in the site plan</td><td>Separate, from cheap shared to managed hosting</td></tr>
<tr><td><b>Plugins and licences</b></td><td>Rarely needed</td><td>Often several paid plugins</td></tr>
<tr><td><b>Maintenance</b></td><td>None</td><td>Updates, backups, security, fixes</td></tr>
</tbody></table></div>
<p>WordPress looks cheaper per month, but maintenance time and plugin licences add up. Framer costs more per month and usually less per year for a marketing site.</p>
"""),
('fw-editing', 'Editing day to day', """
<ul>
<li><b>Framer:</b> edit text and images directly on the page, add CMS items such as blog posts in a simple panel. Very easy for designers and marketers.</li>
<li><b>WordPress:</b> the block editor or a page builder. Flexible, but layouts can drift as more people edit, and updates sometimes break things.</li>
</ul>
"""),
('fw-switch', 'Moving from WordPress to Framer', """
<ol>
<li>List the pages and posts that bring traffic and links.</li>
<li>Design the new site in Figma and rebuild it in Framer.</li>
<li>Import blog content into the Framer CMS.</li>
<li>Set up 301 redirects for every changed URL.</li>
<li>Check Search Console for a few weeks after launch.</li>
</ol>
<p>The same checklist as in our <a href="../blog/migrate-wordpress-to-webflow-without-losing-seo.html">WordPress to Webflow guide</a> applies.</p>
"""),
('fw-seo', 'Framer or WordPress for SEO?', """
<p>This is the question we hear most, and the honest answer is that <b>both can rank well</b>. Google does not prefer one platform. It ranks pages that load fast, answer the search and have a clean structure. The difference is in how much work it takes to get there.</p>
<div class="post-table" role="region" aria-label="Framer and WordPress SEO compared" tabindex="0"><table>
<thead><tr><th>SEO task</th><th>Framer</th><th>WordPress</th></tr></thead>
<tbody>
<tr><td><b>Titles and meta descriptions</b></td><td>Built in, per page and per CMS item</td><td>Usually through a plugin such as Yoast or Rank Math</td></tr>
<tr><td><b>Sitemap and robots.txt</b></td><td>Generated automatically</td><td>Generated by core or an SEO plugin</td></tr>
<tr><td><b>301 redirects</b></td><td>Set in site settings</td><td>Plugin or server rules</td></tr>
<tr><td><b>Structured data (schema)</b></td><td>Added as custom code per page</td><td>Plugins generate most of it automatically</td></tr>
<tr><td><b>Page speed</b></td><td>Fast out of the box, served from a CDN</td><td>Depends on hosting, theme, plugins and caching</td></tr>
<tr><td><b>Large content sites</b></td><td>Fine for a normal blog</td><td>More control over taxonomies, archives and filters</td></tr>
</tbody></table></div>
<p><b>Framer is the easier choice</b> for a company site with a blog: speed and clean markup come by default, and there is no plugin stack to slow pages down. <b>WordPress gives more control</b> when SEO depends on thousands of pages, complex categories, faceted filters or programmatic pages.</p>
<div class="post-note"><b>What actually moves rankings</b><p>On either platform, rankings come from useful content, a clear page structure, internal links and links from other sites. The platform only decides how easy the technical part is. A fast Framer page with thin content will not beat a slower WordPress page that answers the question better.</p></div>
"""),
('fw-security', 'Security: is Framer safer than WordPress?', """
<p>For a typical marketing site, <b>Framer carries far less security risk</b>, mostly because there is much less for you to manage.</p>
<ul>
<li><b>Framer</b> is a hosted platform. Framer runs the servers, SSL certificates and updates. There are no plugins or themes on your side to patch, and no admin login on your domain for bots to attack.</li>
<li><b>WordPress</b> core is well maintained, but most real-world problems come from outdated plugins, themes and weak admin passwords. Security depends on regular updates, backups, a good host and often a security plugin.</li>
</ul>
<p>That does not make WordPress unsafe. It means WordPress security is a job someone has to do every month. If nobody on your team owns that job, Framer or Webflow removes the risk instead of managing it.</p>
<p>One thing to weigh on the other side: with Framer your site lives on Framer's platform. You cannot move the code to your own server. WordPress is open source, so you can host it anywhere and take everything with you.</p>
"""),
('fw-speed', 'Speed and Core Web Vitals', """
<p>Framer publishes pre-built pages to a global CDN, compresses images and handles caching for you, so a well-built Framer site usually scores well on Core Web Vitals without extra work. Heavy animations and very large images can still slow it down, so they need the same care as anywhere else.</p>
<p>WordPress can be just as fast, but it takes deliberate choices: good managed hosting, a light theme, few plugins, a caching layer and optimised images. Many slow WordPress sites are slow because plugins were added over the years and never removed.</p>
"""),
('fw-languages', 'Multilingual sites', """
<ul>
<li><b>Framer</b> has built-in localization: you translate pages and CMS items inside the editor, and each language gets its own URL for search engines.</li>
<li><b>WordPress</b> uses plugins such as WPML or Polylang. They are powerful and handle complex setups, but they add another plugin to keep updated and can slow the editor down on big sites.</li>
</ul>
<p>For two to five languages on a company site, Framer is simpler. For many languages with different content per market, WordPress or Webflow give more room.</p>
"""),
('fw-design', 'Design freedom and animations', """
<p>Framer was built by people who make design tools, and it shows. Layouts, hover effects, scroll animations and page transitions are set visually, very close to how a designer works in Figma. What you approve in the design is what goes live.</p>
<p>On WordPress the result depends on the theme or page builder and on the developer. Anything is possible with custom code, but advanced motion takes more development time, and page builders often add extra code that slows the page down.</p>
"""),
('fw-choose', 'A quick way to decide', """
<p>Answer these five questions. If most answers point one way, that is your platform.</p>
<ol>
<li><b>Do you sell many products online?</b> Yes: WordPress with WooCommerce, or Shopify. No: Framer works.</li>
<li><b>Do you need logins, memberships, courses or bookings?</b> Yes: WordPress. No: Framer.</li>
<li><b>Will you publish more than a few hundred articles with complex categories?</b> Yes: WordPress or Webflow. No: Framer is enough.</li>
<li><b>Is there someone to update plugins and watch security every month?</b> No: Framer.</li>
<li><b>Is design and first impression the main goal of the site?</b> Yes: Framer.</li>
</ol>
<p>Still not sure? Send us a short brief and we will tell you which platform fits, even if the answer is the one we do not build on.</p>
"""),
  ],
  faq=[("Is Framer or WordPress better for SEO?", "Both can rank well. Framer is faster to set up correctly and fast by default; WordPress gives more control for very large content sites with complex categories."),
       ("Is a Framer website secure?", "Yes. Framer hosts the site and handles servers, SSL and updates, so there are no plugins or admin logins on your domain to attack. WordPress can be secure too, but it needs regular updates and backups."),
       ("Can I export my Framer site and host it myself?", "No. Framer sites are hosted by Framer. If owning and moving the code matters to you, WordPress or a custom build is the better fit."),
       ("Does Framer support multiple languages?", "Yes. Framer has built-in localization for pages and CMS content, with a separate URL for each language."),
       ("Is Framer good for SEO?", "Yes for most marketing sites: clean pages, fast loading, editable meta tags and sitemaps. Very large content sites get more control on Webflow or WordPress."),
       ("Is Framer cheaper than WordPress?", "Framer has a monthly plan but no maintenance costs. WordPress hosting is cheap, but updates, plugins and fixes add up over a year."),
       ("Can I move from WordPress to Framer?", "Yes. Pages are rebuilt in Framer, blog content is imported and old URLs get 301 redirects to keep rankings."),
       ("Do you build on both?", "Yes. We design in Figma and build in Framer, Webflow or WordPress depending on what the site needs."),
       ('How much does a Framer website cost?', 'Usually $3,000 to $15,000 with a professional team; see our Framer website cost guide for the breakdown.'),
       ('Is WordPress better for large blogs?', 'For very large content libraries with custom logic, yes. For a normal company blog, Framer or Webflow is enough.'),
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

<p>Planning a hospitality project? Our <a href="../blog/restaurant-website-design.html">restaurant website design guide</a> covers menu editing, reservations and the scope to agree before hiring.</p>
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
('rd-takeaways', 'Summary', """
<div class="post-note"><b>In one minute</b><p>A redesign costs more when the structure, message or platform changes, and less when only the look changes. Protect your SEO with redirects and kept metadata. Measure the current site first, so you know what the redesign must improve.</p></div>
"""),
('rd-breakdown', 'Where a redesign budget goes', """
<div class="post-table" role="region" aria-label="Redesign cost breakdown" tabindex="0"><table>
<thead><tr><th>Part</th><th>Typical share</th><th>Includes</th></tr></thead>
<tbody>
<tr><td><b>Audit and strategy</b></td><td>10 to 15%</td><td>Analytics review, content audit, goals</td></tr>
<tr><td><b>Structure and messaging</b></td><td>10 to 15%</td><td>Sitemap, page outlines, key messages</td></tr>
<tr><td><b>Design</b></td><td>30 to 35%</td><td>Desktop and mobile in Figma, components</td></tr>
<tr><td><b>Build</b></td><td>25 to 35%</td><td>Pages, CMS, integrations</td></tr>
<tr><td><b>SEO protection and launch</b></td><td>5 to 10%</td><td>Redirects, metadata, QA, monitoring</td></tr>
</tbody></table></div>
"""),
('rd-process', 'How a redesign runs', """
<ol>
<li><b>Audit:</b> what works today, what does not, and which pages bring traffic.</li>
<li><b>Plan:</b> structure, messaging and the scope, with a fixed price.</li>
<li><b>Design:</b> key pages first, then the rest on the same components.</li>
<li><b>Build:</b> on the same platform or a new one.</li>
<li><b>Launch:</b> redirects, checks and a few weeks of monitoring.</li>
</ol>
"""),
('rd-measure', 'How to measure success', """
<ul>
<li>Conversion rate on key pages: demo requests, inquiries, sales.</li>
<li>Organic traffic and rankings before and after.</li>
<li>Page speed and Core Web Vitals.</li>
<li>Time your team spends on updates.</li>
</ul>
"""),
  ],
  faq=[("How long does a website redesign take?", "Usually 3 to 8 weeks, depending on the number of layouts, content readiness and whether the platform changes."),
       ("Will a redesign hurt my SEO?", "Not if URLs are kept or redirected, metadata is carried over and indexing is checked after launch."),
       ("Should I redesign or just refresh?", "Refresh if the structure and message still work. Redesign if visitors do not convert or the site no longer fits the business."),
       ("Can you redesign my site on the same platform?", "Yes. We redesign on Webflow, Framer or WordPress, or move you to a better fit if it makes sense."),
       ('Should we redesign and change platform at the same time?', 'Often yes, as it saves building twice. Plan SEO carefully if URLs change.'),
       ('Can we redesign in stages?', 'Yes. Start with the homepage and key landing pages, then the rest on the same design system.'),
  ],
),
dict(
  slug="website-design-for-ai-startups",
  title="Website Design for AI Startups in 2026: What Converts | Sorvel",
  h1="Website design for AI startups: what actually works in 2026",
  card="How AI startups explain the product, show it working and earn trust on the website, with page structure, costs and timelines.",
  desc="Website design for AI startups in 2026: how to explain an AI product in seconds, show it working, answer data and trust questions, which pages you need, platform choice and costs.",
  cat="Niches", date="2026-11-01", svc=("saas-website-design", "SaaS website design"),
  cover=("c-website-design-for-ai-startups", "A developer working with two monitors in a startup office"),
  lead="Every AI startup says it saves time with AI. Buyers have heard it hundreds of times. The websites that convert make the product concrete in the first few seconds and answer the trust questions before anyone asks. Here is how to do that.",
  sections=[
("ai-short", "The short answer", """
<p>A strong AI startup website does three things: it names the job your product does in plain words, it shows the product doing that job with real screens or a short demo, and it answers questions about data, accuracy and security on the page.</p>
<p>With our studio an AI startup website starts <b>from $6,900</b> and takes <b>3 to 6 weeks</b>. A single launch or waitlist page starts <b>from $2,400</b> and takes 1 to 2 weeks.</p>
<div class="post-note"><b>Key takeaways</b><p>Lead with the outcome, not the model. Show a real input becoming a real output. Give security and data handling their own section. Pick Framer for a fast launch and Webflow when you will publish a lot.</p></div>
"""),
("ai-message", "Lead with the job, not the technology", """
<p>Visitors decide in a few seconds whether a site is for them. "AI-powered platform" tells them nothing. A headline that names the job and the audience does:</p>
<div class="post-table" role="region" aria-label="AI startup headline examples" tabindex="0"><table>
<thead><tr><th>Vague</th><th>Clear</th></tr></thead>
<tbody>
<tr><td>AI-powered customer experience platform</td><td>Answer support tickets in seconds, in your brand's voice</td></tr>
<tr><td>Next-generation AI for finance teams</td><td>Close the books three days faster with automatic reconciliation</td></tr>
<tr><td>Revolutionary AI assistant</td><td>Find the subscriptions you forgot you pay for</td></tr>
</tbody></table></div>
<p>Then support the headline with one line on how it works and one clear action: start a trial, book a demo or join the waitlist.</p>
"""),
("ai-show", "Show the product working", """
<p>AI products are hard to picture, so visitors trust what they can see. The strongest options, in order:</p>
<ol>
<li><b>A short looping demo</b> of an input turning into an output: a document into a summary, a question into an answer.</li>
<li><b>Real interface screens</b>, cropped to the part that matters, with short captions.</li>
<li><b>Before and after</b> examples that show the result, not the process.</li>
</ol>
<p>Avoid glowing brains, robots and abstract particles. They say "AI" without saying what your AI does. On the Skyli pre-launch site we showed a live subscription list with the monthly total and a "Skyli suggests" card, so the value was visible before anyone read a word.</p>
[[cta]]
"""),
("ai-trust", "Answer trust questions on the page", """
<p>Buyers of AI products worry about data, accuracy and control. Answer those concerns openly:</p>
<ul>
<li><b>Data:</b> where it goes, how long it is kept and whether it trains the model.</li>
<li><b>Security and compliance:</b> SOC 2, GDPR or ISO, if you have them, with a link to details.</li>
<li><b>Accuracy:</b> how the output is checked and how a human stays in control.</li>
<li><b>Integrations:</b> the tools the buyer already uses, shown as logos.</li>
</ul>
<p>A dedicated "Security" or "How it works" section often does more for demo requests than another feature grid. For German-speaking buyers we placed GDPR compliance and local partnership right under the hero of an AI agency site, because that is the first question they ask.</p>
"""),
("ai-pages", "Pages an AI startup website needs", """
<div class="post-table" role="region" aria-label="AI startup website pages" tabindex="0"><table>
<thead><tr><th>Page</th><th>Purpose</th><th>When</th></tr></thead>
<tbody>
<tr><td><b>Home</b></td><td>The job, the proof, one action</td><td>Always</td></tr>
<tr><td><b>Product or How it works</b></td><td>Show the workflow step by step</td><td>Always</td></tr>
<tr><td><b>Use cases</b></td><td>One page per audience or job</td><td>Once you sell to more than one segment</td></tr>
<tr><td><b>Pricing</b></td><td>Plans or "talk to us" with clear starting points</td><td>When you charge</td></tr>
<tr><td><b>Security</b></td><td>Data handling and compliance</td><td>Selling to companies</td></tr>
<tr><td><b>Changelog and blog</b></td><td>Show momentum, bring search traffic</td><td>After launch</td></tr>
</tbody></table></div>
"""),
("ai-stage", "What to build at each stage", """
<ul>
<li><b>Pre-launch:</b> one landing page with the problem, a preview of the product and a waitlist. Fast and cheap to change.</li>
<li><b>Seed:</b> 5 to 8 pages: home, product, use cases, pricing, about, contact, blog.</li>
<li><b>Series A and later:</b> a CMS for use cases, integrations, customer stories and a changelog, built so marketing can publish without developers.</li>
</ul>
"""),
("ai-platform", "Webflow or Framer for an AI startup", """
<p>Pre-seed and seed teams with a handful of pages usually launch faster on Framer, and it handles motion-rich product scenes well. Teams that publish a changelog, docs links, integrations or a blog are better served by Webflow's CMS. See <a href="../blog/webflow-vs-framer.html">Webflow vs Framer</a> and <a href="../blog/framer-website-cost.html">what a Framer website costs</a>.</p>
"""),
("ai-mistakes", "Common mistakes", """
<ul>
<li>Leading with the model or the tech stack instead of the outcome.</li>
<li>Abstract AI visuals instead of the real product.</li>
<li>No answer to "what happens to my data?"</li>
<li>Five different calls to action on the homepage.</li>
<li>Claims like "10x productivity" with nothing behind them.</li>
</ul>
"""),
  ],
  faq=[("How long does an AI startup website take?", "Usually 3 to 6 weeks for 5 to 10 pages, or 1 to 2 weeks for a single launch page."),
       ("How much does an AI startup website cost?", "With a professional team usually $5,000 to $20,000; with our studio from $6,900, or from $2,400 for one page."),
       ("Should an AI startup use a template?", "Before product-market fit a template can be enough. Once you raise or sell to larger companies, a custom site that shows your real product usually converts better."),
       ("How do we show the product before it is finished?", "With designed product scenes based on your real flows. They can be updated as the product changes."),
       ("Do you design product UI as well?", "Yes. We design the product interface in Figma, so the website and the app look like one product."),
       ("Can the site be in several languages?", "Yes, in Webflow or Framer, with layouts checked for each language."),
  ],
),
dict(
  slug="b2b-website-design",
  title="B2B Website Design in 2026: How to Build a Site That Generates Leads | Sorvel",
  h1="B2B website design: how to build a site that generates leads",
  card="What B2B buyers look for, the pages every B2B site needs, proof that works and lead capture that turns visits into qualified leads.",
  desc="B2B website design guide for 2026: how B2B buyers decide, the pages and proof every B2B site needs, messaging, lead capture that works, platform choice, costs and timelines.",
  cat="Niches", date="2026-11-01", svc=("websites", "website design and development"),
  cover=("c-b2b-website-design", "A professional working at a computer in a busy office"),
  lead="B2B buyers rarely buy on their first visit. They come back several times, often with colleagues, and each time the website has to answer a different question. A good B2B site is built for that whole journey, not just the first impression.",
  sections=[
("b2b-short", "The short answer", """
<p>A B2B website that generates leads makes clear who you help and with what, proves it with case studies and named clients, and gives every type of visitor a next step, from a guide to download to a quote request.</p>
<p>A professional B2B website usually costs <b>$5,000 to $20,000</b> and takes <b>4 to 8 weeks</b>. With our studio it starts <b>from $6,900</b>.</p>
<div class="post-note"><b>Key takeaways</b><p>Write for the buying committee, not one person. Make proof specific. Offer two kinds of action: one for buyers who are ready and one for those still researching. Connect every form to your CRM.</p></div>
"""),
("b2b-buyers", "How B2B buyers actually decide", """
<p>A typical B2B purchase involves several people: a user who feels the problem, a manager who owns the budget and often someone from finance, IT or legal. Each of them visits your site with a different question:</p>
<div class="post-table" role="region" aria-label="B2B buyer questions" tabindex="0"><table>
<thead><tr><th>Who</th><th>Their question</th><th>Page that answers it</th></tr></thead>
<tbody>
<tr><td><b>User</b></td><td>Will this make my job easier?</td><td>Product and use cases</td></tr>
<tr><td><b>Manager</b></td><td>Will it pay off, and who else uses it?</td><td>Case studies, pricing</td></tr>
<tr><td><b>Finance or procurement</b></td><td>What does it cost and what are the terms?</td><td>Pricing, how we work</td></tr>
<tr><td><b>IT or legal</b></td><td>Is it secure and compliant?</td><td>Security, FAQ</td></tr>
</tbody></table></div>
"""),
("b2b-pages", "Pages every B2B website needs", """
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
<p>On a recruitment firm's site we led with the firm's hiring numbers and gave founders and engineers separate paths through the same site, because they arrive with completely different goals.</p>
"""),
("b2b-message", "Messaging that works for B2B", """
<ul>
<li><b>Name the customer.</b> "For logistics companies with 50 to 500 drivers" beats "for businesses of all sizes".</li>
<li><b>Name the outcome.</b> Fewer violations, faster hiring, lower cost per lead.</li>
<li><b>Use their words.</b> The terms your buyers use in sales calls, not internal jargon.</li>
<li><b>Show, then tell.</b> A product screen or a process diagram before the paragraph.</li>
</ul>
[[cta]]
"""),
("b2b-proof", "Proof beats promises", """
<ul>
<li><b>Case studies with specifics:</b> the problem, what was done and what changed.</li>
<li><b>Named logos and quotes</b> from real people with their role and company.</li>
<li><b>Numbers you can stand behind,</b> such as clients served, years in business or response time.</li>
<li><b>Certifications and partners</b> that matter in your industry.</li>
</ul>
<p>Generic testimonials like "Great team, highly recommended" do little. A quote that mentions a specific result or moment is far more convincing.</p>
"""),
("b2b-leads", "Lead capture that works", """
<ul>
<li><b>A short contact form:</b> name, email, company and one question. Every extra field costs leads.</li>
<li><b>A softer option</b> for early researchers: a guide, checklist or pricing sheet.</li>
<li><b>A clear response time,</b> for example "reply within one business day".</li>
<li><b>CRM integration,</b> so no lead sits unseen in an inbox.</li>
<li><b>Analytics on every form,</b> so you know which pages bring qualified leads.</li>
</ul>
"""),
("b2b-platform", "Which platform for a B2B website", """
<p>Webflow is a strong default for marketing teams that publish case studies and articles often and want to edit without developers. WordPress fits when you need complex functionality or many integrations. For a fast, smaller site, Framer works well. See <a href="../blog/webflow-vs-wordpress.html">Webflow vs WordPress</a>.</p>
"""),
("b2b-mistakes", "Common B2B website mistakes", """
<ul>
<li>A homepage that talks about the company instead of the customer.</li>
<li>No case studies, or case studies with no details.</li>
<li>Only one call to action: "Book a demo", with nothing for early researchers.</li>
<li>Forms that ask for budget, company size and phone before saying hello.</li>
<li>No clear prices or starting points, so buyers go to a competitor that has them.</li>
</ul>
"""),
  ],
  faq=[("How many pages does a B2B website need?", "Most start with 6 to 12 pages and grow through case studies, industry pages and articles."),
       ("How much does a B2B website cost?", "Usually $5,000 to $20,000 with a professional team; with our studio from $6,900."),
       ("Which platform is best for a B2B website?", "Webflow is a strong default for marketing teams; WordPress fits complex functionality."),
       ("How long does a B2B website take?", "Usually 4 to 8 weeks, depending on the number of layouts and content readiness."),
       ("Should we show prices on a B2B website?", "Starting prices or ranges help qualify leads and build trust, even if final pricing is custom."),
       ("Can you connect forms to our CRM?", "Yes: HubSpot, Salesforce, Pipedrive and most email tools."),
  ],
),
dict(
  slug="law-firm-website-design",
  title="Law Firm Website Design in 2026: What Clients Look For | Sorvel",
  h1="Law firm website design: what clients look for before they call",
  card="Trust signals, practice area pages, call-first design, local SEO and costs for law firm websites that turn visitors into consultations.",
  desc="Law firm website design guide for 2026: the trust signals clients look for, practice area pages, call-first mobile design, bilingual sites, local SEO and what a law firm website costs.",
  cat="Niches", date="2026-11-01", svc=("websites", "website design and development"),
  cover=("c-law-firm-website-design", "A lawyer on the phone working on a laptop"),
  lead="People looking for a lawyer are often stressed and in a hurry. They compare a few firms on their phone and call the one that feels most trustworthy and easiest to reach. A good law firm website is built for exactly that moment.",
  sections=[
("law-short", "The short answer", """
<p>A law firm website that brings in consultations shows who you help and where, proves experience early, and puts a way to call or book on every screen, especially on mobile. Practice area pages and local SEO bring most of the search traffic.</p>
<p>A custom law firm website usually costs <b>$5,000 to $20,000</b>. With our studio it starts <b>from $6,900</b>, and a single call-first landing page for ads starts <b>from $2,400</b>.</p>
<div class="post-note"><b>Key takeaways</b><p>Calm the visitor, then make calling easy. Give every practice area its own page. Show real attorneys and real credentials. Design for phones first, because that is where most legal searches happen.</p></div>
"""),
("law-trust", "Trust signals clients look for", """
<ul>
<li><b>Real photos of the attorneys</b> with bar admissions, years of practice and education.</li>
<li><b>Results and reviews,</b> presented within the advertising rules of your bar.</li>
<li><b>Languages spoken,</b> if you serve more than one community.</li>
<li><b>Clear, calm language.</b> No legal jargon in the headlines.</li>
<li><b>Free consultation details:</b> how it works, how long it takes and that it is confidential.</li>
</ul>
"""),
("law-pages", "Practice area pages: the backbone of the site", """
<p>Each practice area deserves its own page. These pages rank for searches like "DUI lawyer in Houston" and give visitors confidence that you handle their exact situation. A strong practice area page includes:</p>
<ol>
<li>What the area covers, in plain words.</li>
<li>Typical situations clients come with.</li>
<li>How the process works and what happens next.</li>
<li>Relevant results or experience.</li>
<li>An FAQ with the questions clients ask on the first call.</li>
<li>A call or booking button, repeated.</li>
</ol>
[[cta]]
"""),
("law-mobile", "Call-first design on mobile", """
<p>Most people search for a lawyer on their phone, often in a stressful moment. A sticky call button, click-to-call numbers and a short contact form matter more than any animation. For a Houston criminal defense firm we designed a bilingual landing page with proof above the fold and a way to call from every single section, built in Webflow.</p>
"""),
("law-bilingual", "Bilingual and multilingual law firm sites", """
<p>If you serve Spanish-speaking or other communities, a real second-language version, not an automatic translation widget, builds far more trust. Plan for a language switcher, translated practice pages and staff who answer in that language. Medical and dental practices have similar needs; see our <a href="../blog/dental-website-design.html">dental website design guide</a>.</p>
"""),
("law-seo", "Local SEO for law firms", """
<ul>
<li>A Google Business Profile with the same name, address and phone as the website.</li>
<li>Practice area pages that mention the city or region you serve.</li>
<li>Reviews on Google and legal directories.</li>
<li>Structured data for your firm, attorneys and locations.</li>
<li>Helpful articles that answer common legal questions in your area.</li>
</ul>
"""),
("law-pages-list", "Pages a law firm website needs", """
<div class="post-table" role="region" aria-label="Law firm website pages" tabindex="0"><table>
<thead><tr><th>Page</th><th>Purpose</th></tr></thead>
<tbody>
<tr><td><b>Home</b></td><td>Who you help, where, and how to reach you now</td></tr>
<tr><td><b>Practice areas</b></td><td>One page per area, for search and trust</td></tr>
<tr><td><b>Attorneys</b></td><td>Real people, credentials and experience</td></tr>
<tr><td><b>Results and reviews</b></td><td>Proof, within your bar's rules</td></tr>
<tr><td><b>Contact or free consultation</b></td><td>Short form, phone, map, hours</td></tr>
<tr><td><b>Blog or FAQ</b></td><td>Answers to common questions, for search traffic</td></tr>
</tbody></table></div>
"""),
("law-mistakes", "Common law firm website mistakes", """
<ul>
<li>Stock photos of gavels and handshakes instead of the real team.</li>
<li>One "Services" page for every practice area.</li>
<li>Phone numbers that are not clickable on mobile.</li>
<li>Long contact forms that ask for the whole story up front.</li>
<li>Slow pages, which hurt both rankings and patience.</li>
</ul>
"""),
  ],
  faq=[("How much does a law firm website cost?", "A custom site with a professional team usually costs $5,000 to $20,000; with our studio from $6,900, or from $2,400 for one landing page."),
       ("Which platform is best for a law firm?", "Webflow or WordPress. Both handle practice area pages, blogs and local SEO well."),
       ("How long does a law firm website take?", "Usually 4 to 6 weeks, depending on the number of practice areas and content."),
       ("Can the site be bilingual?", "Yes. We design and build sites in two or more languages."),
       ("Can you build a landing page for Google Ads?", "Yes. A call-first landing page for one practice area is often the fastest way to get calls from ads."),
       ("Do you write the legal content?", "We structure and design the pages. Legal content should come from or be reviewed by your attorneys."),
  ],
),
dict(
  slug="travel-website-design",
  title="Travel and Tourism Website Design in 2026: A Practical Guide | Sorvel",
  h1="Travel and tourism website design: a practical guide",
  card="How destination and tour websites inspire visitors, help them plan and turn interest into bookings and inquiries, with structure, platform and costs.",
  desc="Travel and tourism website design guide for 2026: inspiring imagery, experience finders, itineraries, booking and inquiry flows, mobile planning, platform choice and typical costs.",
  cat="Niches", date="2026-11-01", svc=("websites", "website design and development"),
  cover=("c-travel-website-design", "A person browsing a travel agency website on a laptop"),
  lead="Travel websites sell a feeling first and a plan second. The best ones move visitors from 'that looks amazing' to 'send me a quote' without friction. Here is how to design that journey for a destination, a tour operator or a travel brand.",
  sections=[
("tr-short", "The short answer", """
<p>A travel or tourism website needs big, honest imagery, a quick way to find the right experience, ready-made itineraries or tours with dates and prices, and a short inquiry or booking form. Most visitors plan on a phone, so mobile comes first.</p>
<p>A custom travel website usually costs <b>$5,000 to $20,000</b> with a professional team. With our studio it starts <b>from $6,900</b>.</p>
<div class="post-note"><b>Key takeaways</b><p>Inspire, then help people plan. Show dates, duration and price on every tour. Keep the inquiry form short. Use real photos of the place, and design for phones first.</p></div>
"""),
("tr-flow", "From inspiration to inquiry", """
<ol>
<li><b>Inspire:</b> a strong hero with a real photo or video, the place's story and a few key facts.</li>
<li><b>Explore:</b> filters by interest, such as diving, culture, family, adventure or wellness.</li>
<li><b>Plan:</b> itineraries or tours with duration, level, season and price.</li>
<li><b>Act:</b> a short inquiry or booking form with a clear reply time.</li>
</ol>
<p>For Visit Pemba, the travel guide to Pemba Island in Zanzibar, we built exactly this path: an aerial hero with four island facts, arched story cards inspired by Swahili doorways, an experience finder by interest and ready-made itineraries leading to a trip inquiry. It was designed in Figma and built in WordPress.</p>
"""),
("tr-pages", "Pages a travel website needs", """
<div class="post-table" role="region" aria-label="Travel website pages" tabindex="0"><table>
<thead><tr><th>Page</th><th>Purpose</th></tr></thead>
<tbody>
<tr><td><b>Home</b></td><td>Inspire and route visitors to experiences</td></tr>
<tr><td><b>Experiences or tours</b></td><td>Browse and filter by interest</td></tr>
<tr><td><b>Itineraries</b></td><td>Ready-made trips with duration and price</td></tr>
<tr><td><b>Stay and eat</b></td><td>Accommodation and food options</td></tr>
<tr><td><b>Travel info</b></td><td>Best time to visit, how to get there, practical tips</td></tr>
<tr><td><b>Plan your trip</b></td><td>Inquiry or booking form</td></tr>
</tbody></table></div>
[[cta]]
"""),
("tr-details", "Details that build confidence", """
<ul>
<li>Best time to visit and what each season is like.</li>
<li>How to get there, with travel times.</li>
<li>Named reviews with the trip and date.</li>
<li>Clear cancellation and payment terms.</li>
<li>Responsible travel and local partners, if they matter to your audience.</li>
</ul>
"""),
("tr-booking", "Booking or inquiry?", """
<div class="post-table" role="region" aria-label="Booking vs inquiry" tabindex="0"><table>
<thead><tr><th></th><th>Online booking</th><th>Inquiry form</th></tr></thead>
<tbody>
<tr><td><b>Best for</b></td><td>Fixed-date tours, day trips, activities</td><td>Tailor-made trips, groups, premium travel</td></tr>
<tr><td><b>Setup</b></td><td>Booking system integration</td><td>Simple form connected to email or CRM</td></tr>
<tr><td><b>Conversion</b></td><td>Instant, but needs exact availability</td><td>Starts a conversation, higher value per lead</td></tr>
</tbody></table></div>
"""),
("tr-mobile", "Design for planning on a phone", """
<p>Travellers browse on their phones, often in short sessions. Use large images that load fast, swipeable cards for tours, sticky "Plan your trip" buttons and forms with as few fields as possible. Save details like dates and group size for a second step.</p>
"""),
("tr-platform", "Which platform", """
<p>WordPress suits content-rich destination sites with many pages, tours and booking plugins. Webflow suits design-led tour operators that want an easy CMS without plugin maintenance. Framer works for smaller, highly visual brands. See <a href="../blog/webflow-vs-wordpress.html">Webflow vs WordPress</a>.</p>
"""),
("tr-mistakes", "Common travel website mistakes", """
<ul>
<li>Stock beach photos that could be anywhere.</li>
<li>Tours without dates, duration or price.</li>
<li>Long inquiry forms on mobile.</li>
<li>Heavy images that make pages slow on mobile networks.</li>
<li>No practical information, so visitors leave to find it elsewhere.</li>
</ul>
"""),
  ],
  faq=[("How much does a travel website cost?", "A custom design and build usually costs $5,000 to $20,000 with a professional team; with our studio from $6,900."),
       ("How long does a travel website take?", "Usually 4 to 8 weeks, depending on the number of tours, pages and integrations."),
       ("Can you add online booking?", "Yes, through booking integrations or a simple inquiry flow, depending on how you sell trips."),
       ("Should a tour operator show prices?", "Yes. Starting prices help visitors self-qualify and increase inquiries from the right travellers."),
       ("Can the site be multilingual?", "Yes, with real translated pages rather than an automatic widget."),
       ("Do you design for mobile first?", "Yes. Every page is designed for phones in Figma, not squeezed afterwards."),
  ],
),
dict(
  slug="landing-page-cost",
  title="How Much Does a Landing Page Cost in 2026? Full Price Guide | Sorvel",
  h1="How much a landing page costs in 2026",
  card="Price ranges for landing pages from templates to studios, a line-by-line cost breakdown, hidden costs and how to get a fixed quote.",
  desc="How much a landing page costs in 2026: price ranges from DIY to studios, a cost breakdown by task, what drives the price, hidden costs, timelines and how to get a fixed quote.",
  cat="Pricing", date="2026-11-03", svc=("websites", "website design and development"),
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
("rates", "Hourly rates vs a fixed price", """
<p>Many people search for landing page setup rates, because some designers quote by the hour. Typical rates in 2026 look like this:</p>
<div class="post-table" role="region" aria-label="Hourly rates for landing page work" tabindex="0"><table>
<thead><tr><th>Who</th><th>Typical hourly rate</th><th>Hours for one landing page</th></tr></thead>
<tbody>
<tr><td><b>Junior freelancer</b></td><td>$20 to $50</td><td>15 to 40</td></tr>
<tr><td><b>Senior freelancer</b></td><td>$50 to $120</td><td>20 to 40</td></tr>
<tr><td><b>Studio or agency</b></td><td>$90 to $200</td><td>25 to 60, including strategy and QA</td></tr>
</tbody></table></div>
<p>Hourly pricing looks flexible, but the final bill is hard to predict, and every round of changes adds hours. A <b>fixed price</b> agreed after the brief is easier to plan: you know the total, the scope and the timeline before work starts. That is how we quote every landing page.</p>
"""),
("setup", "What a landing page setup includes", """
<p>The design is only part of the job. A page that is ready for traffic also needs a technical setup. Check that your quote covers it:</p>
<ul>
<li><b>Domain or subdomain</b> connected, with SSL.</li>
<li><b>Hosting</b> on the platform plan, Webflow, Framer or WordPress.</li>
<li><b>Form</b> connected to your CRM, email tool or booking calendar.</li>
<li><b>Analytics and conversion tracking</b>: Google Analytics, Google Ads or Meta pixel, and events on every button that matters.</li>
<li><b>SEO basics</b>: title, description, social sharing image and a clean URL.</li>
<li><b>Speed and mobile checks</b> before launch, because most ad clicks come from phones.</li>
<li><b>Cookie banner</b> if you run ads to visitors in the EU or the UK.</li>
</ul>
<p>Setup on its own usually takes <b>half a day to two days</b>, so it adds a few hundred dollars when it is quoted separately. Ours is included in the price.</p>
"""),
("bytype", "Landing page cost by type", """
<div class="post-table" role="region" aria-label="Landing page cost by type" tabindex="0"><table>
<thead><tr><th>Type of page</th><th>Typical cost with a professional team</th><th>What makes it cost more</th></tr></thead>
<tbody>
<tr><td><b>Lead generation for a service</b></td><td>$1,500 to $4,000</td><td>Several forms, booking, CRM routing</td></tr>
<tr><td><b>SaaS sign-up or demo page</b></td><td>$2,500 to $6,000</td><td>Product visuals, pricing table, integrations</td></tr>
<tr><td><b>Product launch or waitlist</b></td><td>$2,000 to $5,000</td><td>Animation, video, referral mechanics</td></tr>
<tr><td><b>Event or webinar</b></td><td>$1,000 to $3,000</td><td>Registration tools, reusable templates</td></tr>
<tr><td><b>E-commerce product page</b></td><td>$1,500 to $5,000</td><td>Checkout, reviews, upsells, store integration</td></tr>
</tbody></table></div>
<p>If you plan several campaigns, ask for a reusable template. The first page costs more, and every next page on the same system costs a fraction of it.</p>
"""),
("diy", "Should you build it yourself?", """
<p>A template is fine to test an idea for a week. It stops being cheap when real ad money goes to it. If you spend $2,000 a month on ads and a better page lifts conversion from 2% to 3%, you get <b>50% more leads</b> for the same spend. Over a few months that pays for a professional page many times over.</p>
<p>Build it yourself when the budget is very small, the offer is still changing every week, or you only need a page for a short test. Hire help when the page carries real traffic, the brand matters or you need tracking you can trust.</p>
"""),
  ],
  faq=[("What are typical landing page setup rates?", "Freelancers usually charge $20 to $120 an hour and studios $90 to $200. A landing page takes 15 to 60 hours, which is why many teams prefer a fixed price agreed upfront."),
       ("What is included in a landing page setup?", "Domain and SSL, hosting, a connected form, analytics and conversion tracking, SEO basics, a cookie banner where needed, and speed and mobile checks before launch."),
       ("How much does a landing page cost?", "Usually $1,500 to $6,000 with a professional team in 2026. With our studio from $2,400, extra pages on the same design from $600."),
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
('wx-takeaways', 'Summary', """
<div class="post-note"><b>In one minute</b><p>Wix is the quicker start for a small site you build yourself. Webflow is the better base for a custom, professional site that has to grow, rank and be edited by a team. Most businesses outgrow Wix when content, SEO and brand start to matter.</p></div>
"""),
('wx-cost', 'Cost over the first year', """
<div class="post-table" role="region" aria-label="Webflow and Wix first-year cost" tabindex="0"><table>
<thead><tr><th></th><th>Webflow</th><th>Wix</th></tr></thead>
<tbody>
<tr><td><b>Build</b></td><td>Usually a professional build, from a few thousand dollars</td><td>Often DIY, or a low-cost freelancer</td></tr>
<tr><td><b>Monthly plan</b></td><td>Site plan, plus editor seats if needed</td><td>Premium plan</td></tr>
<tr><td><b>Maintenance</b></td><td>None, hosting included</td><td>None, hosting included</td></tr>
<tr><td><b>Cost to grow</b></td><td>Low: new pages on existing components</td><td>Higher once the template limits you</td></tr>
</tbody></table></div>
<p>Plan prices change, so check both platforms' pricing pages. The bigger difference is what happens when the business grows: a custom Webflow site scales with you, while many Wix sites end up rebuilt.</p>
"""),
('wx-seo', 'SEO and speed compared', """
<ul>
<li><b>Webflow</b> gives full control over page titles, meta descriptions, Open Graph, schema markup, 301 redirects, canonical URLs and clean HTML structure.</li>
<li><b>Wix</b> covers the basics well for small sites, with guided SEO settings, but offers less control over structure and code.</li>
<li><b>Speed</b> depends mostly on the build. A clean Webflow build with optimised images usually reaches good Core Web Vitals; template-heavy Wix sites can be slower.</li>
</ul>
"""),
('wx-who', 'Which one fits your business', """
<div class="post-table" role="region" aria-label="Who should choose Webflow or Wix" tabindex="0"><table>
<thead><tr><th>You are</th><th>Better fit</th></tr></thead>
<tbody>
<tr><td>A sole trader building a simple site yourself</td><td>Wix</td></tr>
<tr><td>A startup or SaaS company that needs to look established</td><td>Webflow</td></tr>
<tr><td>A business that publishes articles, case studies or resources</td><td>Webflow</td></tr>
<tr><td>A marketing team that runs campaigns and landing pages</td><td>Webflow</td></tr>
<tr><td>Testing an idea for a few weeks</td><td>Wix</td></tr>
</tbody></table></div>
"""),
  ],
  faq=[("Is Webflow better than Wix for SEO?", "Webflow gives more control over structure, schema and redirects, which matters as a site grows."),
       ("Is Webflow more expensive than Wix?", "Plans cost more and a professional build is usually needed, but you get a custom site that scales."),
       ("Can you move my Wix site to Webflow?", "Yes, with a content import and redirect map to keep rankings."),
       ('How long does it take to move from Wix to Webflow?', 'Usually 2 to 5 weeks, depending on the number of pages and whether you redesign at the same time.'),
       ('Will I lose my Google rankings when moving from Wix?', 'Not if every changed URL gets a 301 redirect, metadata is carried over and indexing is checked after launch.'),
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
('bt-takeaways', 'Summary', """
<div class="post-note"><b>In one minute</b><p>A brief does not need to be long. Answer the eight questions in the template, attach two or three reference sites and give a budget range. That is enough for any good team to give you an accurate fixed quote.</p></div>
"""),
('bt-example', 'A filled-in example', """
<ol>
<li><b>About us:</b> B2B software that helps restaurants track licences and staff training.</li>
<li><b>Audience:</b> owners and operations managers of restaurant groups in the US.</li>
<li><b>Goal:</b> demo requests.</li>
<li><b>Pages:</b> home, features, pricing, about, contact, blog.</li>
<li><b>Content:</b> logo and product screenshots ready; homepage copy needs help.</li>
<li><b>References:</b> two SaaS sites we like for their clear product screens.</li>
<li><b>Platform:</b> Webflow; HubSpot forms.</li>
<li><b>Budget and timeline:</b> $7,000 to $10,000; launch in six weeks.</li>
</ol>
"""),
('bt-content', 'What content to prepare', """
<ul>
<li>Logo files and brand colours, if you have them.</li>
<li>Product screenshots or photos.</li>
<li>Team photos and short bios.</li>
<li>Client logos, testimonials and case study notes.</li>
<li>Any existing copy, even rough, and the questions customers ask most.</li>
</ul>
"""),
('bt-next', 'What happens after you send a brief', """
<p>A good team replies with questions, then a written plan: scope, pages, timeline, price and what they need from you. With us you get that plan within 24 hours, with a fixed price. If the scope changes later, the price changes only with your approval.</p>
"""),
  ],
  faq=[("How long should a website brief be?", "One or two pages is plenty if it answers the key questions."),
       ("Should I include a budget?", "Yes. A range helps agencies suggest the right scope instead of guessing."),
       ("Can I send a brief to Sorvel?", "Yes. Use the brief form on the contact page and you get a written plan with a fixed price within 24 hours."),
       ("What if I don't know which pages I need?", 'List your goals and audience; a good team will suggest the pages.'),
       ('Do I need a sitemap before the brief?', 'No. A rough list of page types is enough.'),
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
("same-brief", "Make it easy to compare: send the same brief", """
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
dict(
  slug="webflow-pricing",
  title="Webflow Pricing 2026: Plans, Seats, Hosting and Real Costs | Sorvel",
  h1="Webflow pricing in 2026: plans, seats and what you will really pay",
  card="Every Webflow plan after the 2026 price change, how site plans and seats add up, and real yearly costs for five typical sites.",
  desc="Webflow pricing in 2026 explained: Starter, Basic and Premium site plans, workspace seats, ecommerce, Localize and bandwidth, with real yearly costs and how to pay less.",
  cat="Pricing", date="2026-11-04", svc=("webflow-agency", "Webflow design and development"),
  cover=("c-webflow-pricing", "An open laptop with a notebook, pencil and calculator on a wooden desk"),
  lead="Webflow changed its pricing in 2026: the CMS and Business plans are gone, there is a new Premium plan, and seats are billed separately. Here is what each plan costs, what you actually need, and what a real Webflow site costs per year.",
  sections=[
("wfp-short", "The short answer", """
<p>For most businesses, <b>Webflow costs $15 to $25 per month per site</b> when billed yearly. A site without a blog runs on the <b>Basic</b> plan at $15 a month; a site with a blog or any CMS content needs <b>Premium</b> at $25 a month. Paying month to month costs more: $25 and $39.</p>
<p>On top of the site plan you may pay for <b>seats</b> if several people edit the site ($15 to $39 per person per month), for <b>Localize</b> if the site has more than one language, and for <b>ecommerce</b> if you sell online. The design and build of the site is a separate, one-off cost.</p>
<div class="post-note"><b>Key takeaways</b><p>Basic for sites without a CMS, Premium for anything with a blog or collections. Always pay yearly if you plan to keep the site. A typical company site with a blog and one extra editor costs about $480 a year in Webflow fees. Prices below are in US dollars, before tax, as of November 2026.</p></div>
"""),
("wfp-plans", "Webflow site plans and prices in 2026", """
<p>A site plan pays for hosting, the custom domain, bandwidth and the CMS for one website. Every live site needs its own plan.</p>
<div class="post-table" role="region" aria-label="Webflow site plans 2026" tabindex="0"><table>
<thead><tr><th>Plan</th><th>Billed yearly</th><th>Billed monthly</th><th>What you get</th></tr></thead>
<tbody>
<tr><td><b>Starter</b></td><td>Free</td><td>Free</td><td>webflow.io address only, 2 pages, 50 CMS items, 1 GB bandwidth. For learning and drafts.</td></tr>
<tr><td><b>Basic</b></td><td>$15/mo</td><td>$25/mo</td><td>Custom domain, up to 300 static pages, 10 GB bandwidth, no CMS.</td></tr>
<tr><td><b>Premium</b></td><td>$25/mo</td><td>$39/mo</td><td>20,000 CMS items in 40 collections, 50 GB bandwidth that can be expanded.</td></tr>
<tr><td><b>Team</b></td><td>$2,500/mo</td><td>Yearly contract only</td><td>Premium limits and more, plus seats and Localize for larger marketing teams.</td></tr>
<tr><td><b>Enterprise</b></td><td>Custom</td><td>Custom</td><td>SSO, custom roles, uptime agreement and custom limits.</td></tr>
</tbody></table></div>
<p>The only real question for most companies is <b>Basic or Premium</b>. If the site has a blog, case studies, team profiles, job listings or anything else you add as items, you need Premium.</p>
"""),
("wfp-changes", "What changed in Webflow pricing in 2026", """
<p>Webflow reworked its plans in 2026. If you read an older guide, these are the differences:</p>
<ul>
<li><b>The CMS plan and the Business plan were retired.</b> Both were replaced by one plan, <b>Premium</b>.</li>
<li><b>CMS limits went up</b> to 20,000 items, and CMS item add-ons were removed.</li>
<li><b>Included bandwidth on the top plan went down</b>: Premium includes 50 GB, while the old Business plan included 100 GB. High-traffic sites buy bandwidth add-ons.</li>
<li><b>Basic went up slightly</b>, to $15 a month billed yearly.</li>
<li><b>A Team plan</b> was added for in-house marketing teams.</li>
</ul>
<p>New purchases moved to the new plans in May 2026. Most existing sites switch at their next renewal from 29 June 2026, and sites in Freelancer and Agency workspaces or on older legacy pricing from <b>16 November 2026</b>. If your site is still on a CMS or Business plan, check your billing page to see when your price changes.</p>
[[cta]]
"""),
("wfp-twice", "Site plans vs workspace plans: why you may pay twice", """
<p>Webflow has two kinds of plans, and they confuse almost everyone:</p>
<ul>
<li><b>Site plan</b>: pays for one live website. This is the plan above.</li>
<li><b>Workspace plan</b>: pays for the place where people design and manage sites, with seats, staging sites and team features.</li>
</ul>
<div class="post-table" role="region" aria-label="Webflow workspace plans 2026" tabindex="0"><table>
<thead><tr><th>Workspace</th><th>Billed yearly</th><th>Who it is for</th></tr></thead>
<tbody>
<tr><td><b>Starter</b></td><td>Free</td><td>Owners of one or two sites. Includes one Full seat.</td></tr>
<tr><td><b>Core</b></td><td>$19/mo</td><td>In-house teams: 10 staging sites, code export, shared libraries.</td></tr>
<tr><td><b>Growth</b></td><td>$49/mo</td><td>Bigger teams: unlimited staging sites, site-level roles.</td></tr>
<tr><td><b>Freelancer</b></td><td>$16/mo</td><td>Freelancers who build sites for clients.</td></tr>
<tr><td><b>Agency</b></td><td>$35/mo</td><td>Studios: unlimited staging, free client seats per site.</td></tr>
</tbody></table></div>
<p>If a studio builds your site and you just run it, you often need <b>only a site plan</b> and the free Starter workspace. The studio pays for its own workspace.</p>
"""),
("wfp-seats", "Webflow seats explained", """
<p>Seats decide who can do what inside the workspace. They are billed per person, per month:</p>
<div class="post-table" role="region" aria-label="Webflow seat prices 2026" tabindex="0"><table>
<thead><tr><th>Seat</th><th>Billed yearly</th><th>What the person can do</th></tr></thead>
<tbody>
<tr><td><b>Full</b></td><td>$39/mo</td><td>Design and build in the Webflow Designer, manage settings and publish.</td></tr>
<tr><td><b>Limited</b></td><td>$15/mo</td><td>Edit content and CMS items, publish changes. Typical for marketers and writers.</td></tr>
<tr><td><b>Free</b></td><td>$0</td><td>Review and comment only.</td></tr>
</tbody></table></div>
<p>Most small teams need one Full seat (often included) and one or two Limited seats for the people who update the blog. Monthly billing for seats costs a little more.</p>
"""),
("wfp-ecom", "Webflow ecommerce pricing", """
<div class="post-table" role="region" aria-label="Webflow ecommerce plans 2026" tabindex="0"><table>
<thead><tr><th>Plan</th><th>Billed yearly</th><th>Products</th><th>Webflow transaction fee</th></tr></thead>
<tbody>
<tr><td><b>Standard</b></td><td>$29/mo</td><td>500</td><td>2%</td></tr>
<tr><td><b>Plus</b></td><td>$74/mo</td><td>5,000</td><td>0%</td></tr>
<tr><td><b>Advanced</b></td><td>$212/mo</td><td>15,000</td><td>0%</td></tr>
</tbody></table></div>
<p>Card fees from Stripe or PayPal come on top. The 2% fee on Standard means Plus becomes cheaper once you sell more than about $2,250 a month. For large catalogues, subscriptions or complex checkout rules, Shopify is usually the better platform. See our <a href="../blog/shopify-store-design.html">Shopify store design guide</a>.</p>
"""),
("wfp-addons", "Add-ons: languages, bandwidth and more", """
<ul>
<li><b>Localize</b> (multilingual sites): Essential from $9 a month per extra language, up to 3 languages; Advanced from $29 a month per language, with translated URLs and more words. Your main language is free.</li>
<li><b>Bandwidth</b>: extra blocks from $20 a month for 50 GB on yearly billing. Most company sites never need them; video-heavy or high-traffic sites do.</li>
<li><b>Optimize and Analyze</b>: Webflow's own A/B testing and analytics, priced by traffic. Useful for high-traffic marketing teams, not needed for a typical company site.</li>
</ul>
"""),
("wfp-real", "What a Webflow site really costs per year", """
<p>Here is what five typical sites pay Webflow per year on yearly billing, not counting design and build:</p>
<div class="post-table" role="region" aria-label="Real yearly Webflow costs" tabindex="0"><table>
<thead><tr><th>Site</th><th>What it needs</th><th>Webflow cost per year</th></tr></thead>
<tbody>
<tr><td><b>Landing page or small site</b></td><td>Basic plan</td><td>$180</td></tr>
<tr><td><b>Company site with a blog</b></td><td>Premium plan</td><td>$300</td></tr>
<tr><td><b>Company site with a blog and one editor</b></td><td>Premium plus one Limited seat</td><td>$480</td></tr>
<tr><td><b>Bilingual company site</b></td><td>Premium, one Limited seat, Localize Essential for one extra language</td><td>About $590</td></tr>
<tr><td><b>Small online shop</b></td><td>Ecommerce Standard</td><td>$348 plus 2% of sales</td></tr>
</tbody></table></div>
<p>Compared with WordPress, there is no separate hosting, security plugin or maintenance contract to add. That is why Webflow often costs less per year even though the monthly fee looks higher. See <a href="../blog/webflow-vs-wordpress.html">Webflow vs WordPress</a>.</p>
"""),
("wfp-build", "Webflow plan price vs the cost of building the site", """
<p>The plan is the small part. The design and build is the main investment, and it is a one-off cost:</p>
<ul>
<li><b>Landing page</b>: usually $1,500 to $6,000 with a professional team. With us from $2,400.</li>
<li><b>Company website</b> of 5 to 10 pages with a CMS: with us from $6,900.</li>
<li><b>WordPress to Webflow migration</b>: with us from $2,900.</li>
</ul>
<p>For full ranges and what drives them, read <a href="../blog/webflow-website-cost.html">how much a Webflow website costs</a>.</p>
"""),
("wfp-owner", "Who should pay for the plan: you or your agency?", """
<p>Put the site plan on <b>your own company account and card</b>, even when a studio builds the site. Then the domain, the hosting and the content stay yours if you ever change agency, and nobody can switch the site off over an unpaid invoice.</p>
<p>The usual setup looks like this: the studio designs and builds in its own workspace, then transfers the finished site to your workspace, and you buy the site plan there. On Agency and Freelancer workspaces the studio can also invite you as a free client, so you can edit content without buying a seat. Ask about this before the project starts, so there are no surprise seat costs after launch.</p>
"""),
("wfp-limits", "What happens when you hit a limit", """
<ul>
<li><b>Too many CMS items or pages</b>: you cannot add more until you move up a plan or clean up old items. 20,000 items on Premium is plenty for almost every company blog.</li>
<li><b>Too much bandwidth</b>: Webflow lets you go over for a short time, then asks you to buy a larger bandwidth block. Heavy images and self-hosted video are the usual cause.</li>
<li><b>Too many editors</b>: each extra person who edits needs a seat, or a free client seat if your agency's workspace includes them.</li>
</ul>
<p>Check your usage in the site settings every few months. It takes a minute and avoids an unexpected upgrade.</p>
"""),
("wfp-choose", "Which Webflow plan do you need?", """
<ol>
<li><b>Only a few pages, no blog?</b> Basic.</li>
<li><b>A blog, case studies, careers or any repeated content?</b> Premium.</li>
<li><b>More than one language?</b> Premium plus Localize.</li>
<li><b>Selling products?</b> An ecommerce plan, or Shopify for bigger stores.</li>
<li><b>A marketing team of five or more people editing every week?</b> Look at Team or Enterprise.</li>
</ol>
"""),
("wfp-save", "How to pay less for Webflow", """
<ul>
<li><b>Pay yearly.</b> Monthly billing costs 56 to 67% more on Premium and Basic.</li>
<li><b>Do not buy Premium for a site without a CMS.</b> Basic is enough.</li>
<li><b>Give writers Limited seats</b>, not Full seats.</li>
<li><b>Compress images and host long videos elsewhere</b> to stay inside your bandwidth.</li>
<li><b>Keep drafts on staging.</b> A site needs a paid plan only when it goes live on your domain.</li>
</ul>
<p>Prices change often. Always confirm the current numbers on Webflow's own pricing page before you buy.</p>
"""),
  ],
  faq=[("How much does Webflow cost per month?", "$15 a month for Basic and $25 a month for Premium when billed yearly, or $25 and $39 billed monthly. Seats, ecommerce and Localize are extra."),
       ("Is Webflow free?", "You can build on the free Starter plan, but it only publishes to a webflow.io address with 2 pages. A site on your own domain needs a paid site plan."),
       ("What happened to the Webflow CMS and Business plans?", "They were retired in 2026 and replaced by one Premium plan with 20,000 CMS items. Existing sites move to the new plans at renewal."),
       ("What is the difference between a site plan and a workspace plan?", "A site plan pays for one live website: hosting, domain, CMS. A workspace plan pays for the team space where people design and manage sites, including seats."),
       ("What is a Webflow seat?", "A paid place for one person in the workspace. A Full seat ($39 a month yearly) can design and publish; a Limited seat ($15) can edit content; a Free seat can only comment."),
       ("Does Webflow charge transaction fees?", "Only on the Standard ecommerce plan, at 2%. Plus and Advanced have no Webflow fee. Card processing fees from Stripe or PayPal apply on every plan."),
       ("Is Webflow more expensive than WordPress?", "Per month, usually yes. Per year, often not, because hosting, security and maintenance are included."),
       ("How much does it cost to build a Webflow website?", "A landing page usually costs $1,500 to $6,000 with a professional team, and a 5 to 10 page company site more. With Sorvel, websites start from $6,900 and landing pages from $2,400."),
  ],
),

dict(
  slug="restaurant-website-design",
  title="Restaurant Website Design: Scope, Menus & Booking | Sorvel",
  h1="Restaurant website design: what to include before you hire",
  card="A buying guide for restaurant owners: menus, reservations, local search and the scope to agree before a website redesign.",
  desc="Plan a restaurant website redesign with readable menus, clear booking paths and local search basics. Compare agency proposals and prepare a clear project brief.",
  cat="Hospitality", date="2026-11-06", svc=("websites", "website design and development"),
  cover=("c-restaurant-website-design", "A waiter carrying plates of salad and appetizers in a restaurant"),
  cover_credit=("Pixabay / Pexels", "https://www.pexels.com/photo/people-inside-restaurant-262978/"),
  lead="Commission a restaurant website around the decisions guests need to make: what to eat, where to go and how to book. This guide explains what to put in your brief and how to compare redesign proposals.",
  sections=[
("rwd-short", "The short answer", """
<p>A restaurant website design project should give guests a readable menu, accurate location details and a clear route to reservations or ordering. Before hiring an agency, agree who supplies the content, which booking system stays, what staff can edit and how launch will be checked.</p>
<div class="post-note"><b>Key takeaways</b><ul>
<li>Start with guest tasks, then choose the page structure and visual direction.</li>
<li>Ask for an editable text menu, with a downloadable version only as an extra.</li>
<li>Separate website work from booking subscriptions, photography and ongoing support.</li>
<li>Compare written deliverables rather than a homepage mockup or an unsupported promise of more bookings.</li>
</ul></div>
"""),
("rwd-scope", "What should a restaurant website include?", """
<p>Write down what you want guests to do before discussing colours. A neighbourhood restaurant might prioritise walk-ins and directions. A destination venue might need reservations and private dining enquiries. A takeaway business might make ordering its main action. Choose the main task for your venue and make the supporting information easy to find.</p>
<p>Use this example structure as a starting brief, then remove anything your team cannot keep current. These are suggested deliverables, not a required page count.</p>
<div class="post-table" role="region" aria-label="Suggested restaurant website scope" tabindex="0"><table>
<thead><tr><th>Page or section</th><th>Guest question</th><th>Ask the agency to deliver</th></tr></thead>
<tbody>
<tr><td>Home</td><td>Is this the right place?</td><td>Cuisine, atmosphere, location and the main action</td></tr>
<tr><td>Menus</td><td>What can I eat?</td><td>Editable dishes, descriptions, prices and menu categories</td></tr>
<tr><td>Reservations</td><td>Can I get a table?</td><td>Booking route, group policy and a contact fallback</td></tr>
<tr><td>Visit</td><td>How do I get there?</td><td>Address, service hours, directions and verified access details</td></tr>
<tr><td>Private dining</td><td>Can you host our event?</td><td>Approved room information and a routed enquiry form</td></tr>
</tbody></table></div>
<p>Keep your story and photography, but give them a job. Show the room to explain the atmosphere. Show dishes you actually serve. Stock photography can illustrate an editorial guide like this one; for your restaurant's sales pages, commission or supply photographs of the venue itself.</p>
<p>For example, brief a neighbourhood bistro around dinner menus, table reservations and finding the entrance. For a venue with an event room, add a separate enquiry route and approved room photographs. Treat these as planning examples, not a standard package: the right structure is the one your guests need and your staff can maintain.</p>
"""),
("rwd-menu", "Should your restaurant menu be a PDF or a web page?", """
<p>We recommend a text-based web menu as the main version. Let guests browse categories, read descriptions and check prices without interpreting a photograph of a printed sheet. Offer a PDF alongside it if guests need a download. Ask the designer to demonstrate the longest dish name and description on a narrow screen.</p>
<p>This recommendation follows two accessibility sources: the <a href="https://www.w3.org/WAI/tutorials/images/" target="_blank" rel="noopener">W3C Images Tutorial</a> and <a href="https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html" target="_blank" rel="noopener">WCAG guidance on non-text content</a>. Both explain that informative images need an equivalent text alternative. Do not make an image the only way to understand what you serve.</p>
<p>Agree a publishing process with the person who runs service. Who changes a dish, who approves its description, and who updates the printed menu? Ask for a demonstration using your content. Keep dietary statements under restaurant approval; a designer should never infer ingredients or make assurances about allergens.</p>
[[cta]]
"""),
("rwd-booking", "How should reservations and ordering work?", """
<p>Choose the booking or ordering workflow before approving the layout. Tell the agency which provider you already use and whether the project includes a link, an embedded widget or additional integration work. Ask the provider to confirm what your account supports. We would keep a working operational system unless there is a clear reason to replace it.</p>
<p>Make the handoff explicit. A reservation button should say what happens next. A private dining form should explain whether it sends an enquiry or confirms a booking. Decide how to handle large parties, unavailable dates and requests outside service hours. Do not present an enquiry receipt as a confirmed table.</p>
<p>Test a complete journey before launch: choose the venue, follow the booking route and check the confirmation. Include a visible phone or contact fallback when the external service is unavailable. Ask who owns troubleshooting after launch, especially where responsibility passes from the website team to the booking provider.</p>
"""),
("rwd-budget", "What changes the cost of restaurant website design?", """
<p>Ask for a quote against an agreed brief rather than a price for “a restaurant website.” We have not included market price ranges here because an unsupported benchmark would make different scopes look comparable. Use the <a href="../blog/website-redesign-cost.html">website redesign cost guide</a> to organise the discussion, then confirm the actual deliverables in your proposal.</p>
<div class="post-table" role="region" aria-label="Restaurant website proposal comparison" tabindex="0"><table>
<thead><tr><th>Scope item</th><th>Define in the quote</th><th>Confirm separately</th></tr></thead>
<tbody>
<tr><td>Menu management</td><td>Content entry, categories and staff editing</td><td>Who supplies and approves future changes</td></tr>
<tr><td>Reservations</td><td>Link, widget or agreed integration</td><td>Provider subscriptions and transaction terms</td></tr>
<tr><td>Photography and copy</td><td>Existing assets or commissioned content</td><td>Usage rights and approval responsibilities</td></tr>
<tr><td>Multiple locations</td><td>Shared templates and venue-specific content</td><td>Different hours, menus and booking accounts</td></tr>
<tr><td>Launch and support</td><td>Redirects, testing, training and handover</td><td>Hosting, maintenance and later changes</td></tr>
</tbody></table></div>
<p>Request the same scope from each supplier. Mark exclusions, revision arrangements, content responsibilities and recurring fees beside the project total. Ask what happens if the booking requirement changes after design approval. A useful quote should make that decision understandable before work starts.</p>
<p>Ask suppliers to identify optional work explicitly. A seasonal campaign page, translated menu or new location can become a later phase if it is not needed for launch. Have the agency explain what can reuse the agreed design and what would require a new layout. Keep those assumptions beside the quote so a lower total does not conceal a missing requirement.</p>
"""),
("rwd-platform", "Which platform should you ask the agency to use?", """
<p>Start with an editing test rather than a platform preference. Ask the proposed team to show how your manager would change opening hours, replace a menu and publish a new photograph. Decide who will hold the account and who can recover access if the original supplier is unavailable.</p>
<p>We would choose between a custom build and a template by testing your actual content and booking workflow. A template proposal should identify its limits and the changes included. A custom proposal should explain what the extra design work solves. Neither label replaces a practical demonstration.</p>
<p>Ask for ownership and handover terms in writing: domain access, site administration, content files, image rights and any continuing maintenance arrangement. Discuss portability before signing. Keep your restaurant's operational accounts under your control, with the agency given the access it needs to do the work.</p>
"""),
("rwd-search", "What should the brief say about local search and AI answers?", """
<p>Give each location a clear identity and keep its name, address, hours and menu information consistent. Ask for restaurant structured data that describes the visible content. <a href="https://developers.google.com/search/docs/appearance/structured-data/local-business" target="_blank" rel="noopener">Google's Local Business documentation</a> and the <a href="https://schema.org/Restaurant" target="_blank" rel="noopener">Schema.org Restaurant definition</a> both document restaurant information such as address, opening hours and menu URLs.</p>
<p>Write direct answers to real guest questions: where to park, how to request a group booking and which menu is served at lunch. Publish only details the restaurant can confirm. Put the answer beside the relevant menu or visit information, rather than hiding everything inside promotional copy.</p>
<p>Keep expectations realistic. Google's <a href="https://developers.google.com/search/docs/appearance/ai-features" target="_blank" rel="noopener">AI search guidance</a> and <a href="https://developers.google.com/search/docs/appearance/structured-data/sd-policies" target="_blank" rel="noopener">structured data policies</a> do not guarantee search appearances. We would commission clear content and correct implementation, and reject a promise of guaranteed AI citations or rankings.</p>
"""),
("rwd-redesign", "How do you protect existing pages during a redesign?", """
<p>Give the agency a list of your existing pages before it proposes replacements. Identify menu links, location pages, event pages and campaign destinations that still matter. Decide which URLs should stay and which need a replacement. Include old PDF menus if guests or other websites still link to them.</p>
<p>When a URL permanently changes, ask for a direct permanent redirect to the relevant replacement. Google documents HTTP <b>301</b> and <b>308</b> for this purpose in both its <a href="https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes" target="_blank" rel="noopener">site move guide</a> and <a href="https://developers.google.com/search/docs/crawling-indexing/301-redirects" target="_blank" rel="noopener">redirect documentation</a>. Request a URL map and test it; do not accept “SEO included” as the whole handover.</p>
<p>Keep the current site available until the replacement is approved. Assign someone to verify menus and hours immediately before launch. After the switch, check representative old links, booking routes and contact messages again. A successful design review is only part of accepting the finished website.</p>
"""),
("rwd-checklist", "What should you check before accepting the website?", """
<p>Put acceptance checks in the brief so both sides know what “finished” means. Our suggested checklist is:</p>
<ol>
<li>Read the menu on a phone without sideways page scrolling.</li>
<li>Change a dish and opening hours using the staff account.</li>
<li>Complete a reservation through the agreed provider's test process.</li>
<li>Send an event enquiry and confirm the right person receives it.</li>
<li>Open the navigation and booking controls using a keyboard.</li>
<li>Check venue details, image descriptions and approved dietary wording.</li>
<li>Follow old links and confirm the agreed redirects.</li>
<li>Receive account access, training notes and support contacts.</li>
</ol>
<p>Agree how test bookings will be identified and removed. Use test details in forms, and ask staff to confirm receipt without creating real reservations or service work. Record issues in a shared list with an owner, then repeat affected checks after fixes. Keep that record with the handover.</p>
<p>Include the person who handles daily updates in the final review. Give them an ordinary task without talking them through each click. If the task needs a developer or an undocumented workaround, resolve that before accepting the handover. Training should use your real menu structure and the actual staff permissions.</p>
"""),
("rwd-hire", "How do you choose a restaurant website design agency?", """
<p>Ask each candidate to walk through a menu update, a mobile booking journey and a launch checklist. Discuss who will build the site and who will answer questions after handover. Use our <a href="../blog/how-to-choose-a-web-design-agency.html">agency selection questions</a> to compare the answers.</p>
<p>Send a brief with your current address, location list, menu files, booking provider, photographs and the staff member responsible for updates. Add what must stay and what is failing today. The <a href="../blog/website-brief-template.html">website brief template</a> can help organise those inputs.</p>
<p>For our <a href="../services/websites.html">website design and development service</a>, we would turn that brief into an agreed structure, design direction and build scope. Ask us to separate essentials from later additions. You should be able to explain what you are buying, who supplies each input and how you will know it is ready to launch.</p>
"""),
  ],
  faq=[
    ("What should a restaurant website include?", "We recommend an editable menu, accurate visit information and a clear reservation or ordering route. Add private dining and other sections when they support a real service your team can maintain."),
    ("How much does restaurant website design cost?", "Request a written quote against your menu, locations, booking workflow and content requirements. Compare recurring provider fees and support separately from the design and build."),
    ("Can we keep our existing reservation system?", "Ask the agency to scope a link, widget or integration with your current provider. Confirm the exact account capabilities with the provider before approving the work."),
    ("Should we use a PDF menu?", "We recommend a readable text menu as the main version, with a PDF download as an extra. Do not rely on a photograph as the only way to understand the menu."),
    ("Do different restaurant locations need separate pages?", "We recommend separate location pages when menus, hours, directions or booking routes differ. Ask for shared templates so each venue can publish accurate details without rebuilding the layout."),
    ("Can restaurant staff update the website?", "Make a staff editing demonstration an acceptance requirement. Ask the agency to show a menu change and an hours update using the permissions your team will actually receive."),
    ("Will a redesign guarantee more reservations?", "Do not treat a booking increase as a guaranteed outcome. Define the guest journeys you want to improve, agree the checks and evaluate results using your actual booking data."),
    ("What should we send an agency for a quote?", "Send your current website, menus, locations, booking provider and available content, together with the problems you need to solve. Identify who approves content and who will manage updates."),
  ],
),
dict(
  slug="dental-website-design",
  title="Dental Website Design 2026: Cost, Must-Haves and HIPAA | Sorvel",
  h1="Dental website design in 2026: what it costs and what it needs",
  card="What a dental practice website costs in 2026, the pages and features that bring in new patients, and how to handle forms and booking safely.",
  desc="Dental website design in 2026: real price ranges, the pages that win new patients, online booking, HIPAA-safe forms, local SEO and how to choose a designer.",
  cat="Healthcare", date="2026-11-08", svc=("websites", "website design and development"),
  cover=("c-dental-website-design", "A bright modern dental clinic with glass treatment rooms"),
  lead="A dental website has one job: turn a local search into a booked appointment. Here is what a good one costs in 2026, what it must include, and the mistakes that quietly cost practices new patients.",
  sections=[
("dw-short", "The short answer", """
<p>A professional dental website usually costs <b>$2,000 to $8,000</b> on a template from a dental marketing company, and <b>$10,000 to $30,000</b> for a custom design for one location. Multi-location groups often spend more. Running costs for hosting, forms, booking and updates add a monthly fee on top.</p>
<p>Whatever you spend, the site needs the same core: clear treatment pages, real photos of the practice and team, visible prices or insurance information, online booking, fast mobile pages, and forms that keep patient data safe.</p>
<div class="post-note"><b>Key takeaways</b><p>Patients choose a dentist on their phone in a few minutes, so mobile speed and a visible "Book" button matter more than effects. Never collect health information through a standard website form. A custom site pays off when you compete for high-value treatments such as implants, Invisalign or cosmetic work.</p></div>
"""),
("dw-cost", "How much does a dental website cost?", """
<div class="post-table" role="region" aria-label="Dental website cost by type" tabindex="0"><table>
<thead><tr><th>Option</th><th>Upfront cost</th><th>Good for</th><th>Watch out for</th></tr></thead>
<tbody>
<tr><td><b>DIY builder</b></td><td>$0 to $500</td><td>A brand-new practice on a tight budget</td><td>Looks like every other DIY site; slow; no strategy</td></tr>
<tr><td><b>Dental marketing company template</b></td><td>$2,000 to $8,000</td><td>Single practices that want something fast</td><td>Monthly contracts, and often you do not own the site</td></tr>
<tr><td><b>Custom design, one location</b></td><td>$10,000 to $30,000</td><td>Practices growing implants, ortho or cosmetic work</td><td>Needs a clear brief and real photos</td></tr>
<tr><td><b>Multi-location or group</b></td><td>$30,000 and up</td><td>DSOs and groups with several clinics</td><td>Location pages, booking per clinic, many editors</td></tr>
</tbody></table></div>
<p>These are typical market ranges in 2026. With Sorvel, a custom practice website starts from $6,900, and a single landing page for one treatment, for example implants, starts from $2,400. You get a written plan and a fixed price within 24 hours.</p>
<p>Before you sign with a dental marketing company, ask one question: <b>who owns the website if we leave?</b> Many template packages are rented. When the contract ends, the site goes with it.</p>
[[cta]]
"""),
("dw-pages", "The pages a dental website needs", """
<ul>
<li><b>Home</b>: who you are, where you are, what you treat, and a booking button in the first screen.</li>
<li><b>One page per treatment</b>: cleaning and check-ups, whitening, implants, Invisalign or braces, veneers, emergency dentistry, children's dentistry. Separate pages rank for separate searches; one "Services" page with a list ranks for nothing.</li>
<li><b>Team</b>: real photos of each dentist with qualifications. People book with a person, not a logo.</li>
<li><b>Prices, insurance and finance</b>: even "from" prices or the insurers you accept remove the biggest doubt.</li>
<li><b>New patients</b>: what the first visit looks like, how long it takes, what to bring.</li>
<li><b>Location and contact</b>: map, parking, opening hours, phone number that can be tapped on mobile.</li>
<li><b>Reviews</b>: real patient reviews, ideally pulled from Google so they stay current.</li>
<li><b>Emergency page</b>: one of the most searched dental terms. Show same-day availability and a phone number.</li>
</ul>
"""),
("dw-booking", "Online booking: the feature that pays for the site", """
<p>Many patients look for a dentist in the evening, when the practice is closed. If the site only says "call us", a good share of them will book with the next practice that lets them pick a time online.</p>
<ul>
<li>Use the booking tool that connects to your practice management software, so the front desk does not retype appointments.</li>
<li>Put a "Book online" button in the header on every page, and repeat it at the end of each treatment page.</li>
<li>Let new patients choose the reason for the visit, so the right slot length is booked.</li>
<li>Keep a phone number next to the button. Older patients and emergencies still call.</li>
</ul>
"""),
("dw-hipaa", "Forms, patient data and HIPAA", """
<p>This is where many dental websites get it wrong. In the US, health information sent through your website is protected under HIPAA, and every vendor that handles it on your behalf needs a Business Associate Agreement (BAA) with you. Similar rules apply in other countries, such as GDPR in the EU and UK.</p>
<div class="post-table" role="region" aria-label="Which website forms are safe for patient data" tabindex="0"><table>
<thead><tr><th>Form</th><th>Safe for health details?</th><th>What to do</th></tr></thead>
<tbody>
<tr><td><b>Standard website form</b> (Webflow, Framer, basic WordPress plugins)</td><td>No</td><td>Use only for general questions; ask people not to share health details</td></tr>
<tr><td><b>HIPAA-ready form tool with a signed BAA</b></td><td>Yes, if set up correctly</td><td>Embed or link it for new-patient forms and medical history</td></tr>
<tr><td><b>Patient portal or booking system</b></td><td>Yes, if the vendor signs a BAA</td><td>Best place for records, documents and anything clinical</td></tr>
</tbody></table></div>
<p>Webflow's own terms say its platform should not be used for protected health information, so on a Webflow dental site we keep the marketing pages on Webflow and send intake forms and booking to a specialised tool. The same approach works on Framer and WordPress. Also check analytics and ad tracking scripts: they should not run on pages where patients enter health details.</p>
<p>This is not legal advice. Ask your compliance adviser to confirm your setup.</p>
"""),
("dw-local", "Local SEO: how patients find you", """
<p>Most dental searches are local: "dentist near me", "emergency dentist" plus a city, "Invisalign" plus a neighbourhood. To show up:</p>
<ol>
<li><b>Complete your Google Business Profile</b>: categories, hours, photos, booking link, and replies to every review.</li>
<li><b>Use the same name, address and phone number</b> on the website, Google and directories.</li>
<li><b>Write real treatment pages</b> that answer what patients ask: cost, pain, recovery time, how many visits.</li>
<li><b>Add a page per location</b> if you have more than one clinic, with its own address, team and photos.</li>
<li><b>Add structured data</b> for your practice (Dentist schema), opening hours and FAQs, so Google and AI assistants can read the key facts.</li>
</ol>
<p>Patients now also ask ChatGPT and Google's AI answers which dentist to choose. Clear, factual pages with prices, treatments and reviews are what those tools quote.</p>
"""),
("dw-design", "Design that builds trust", """
<ul>
<li><b>Real photography</b> of the clinic, team and equipment. Stock photos of perfect smiles make every practice look the same.</li>
<li><b>Calm, clean layouts</b> with plenty of space. Many patients feel anxious about the dentist; the site should feel reassuring, not loud.</li>
<li><b>Before and after galleries</b> for cosmetic treatments, with patient consent.</li>
<li><b>Accessible design</b>: readable text sizes, good contrast, keyboard-friendly forms. Aim for WCAG 2.1 AA, which also helps older patients.</li>
<li><b>Fast mobile pages</b>: compress photos and keep heavy video off the first screen.</li>
</ul>
"""),
("dw-platform", "Which platform: WordPress, Webflow or Framer?", """
<div class="post-table" role="region" aria-label="Platforms for dental websites" tabindex="0"><table>
<thead><tr><th>Platform</th><th>Best for</th><th>Keep in mind</th></tr></thead>
<tbody>
<tr><td><b>Webflow</b></td><td>A polished custom site the team can edit easily</td><td>Use external tools for intake forms and booking</td></tr>
<tr><td><b>WordPress</b></td><td>Large content sites and many plugins</td><td>Needs regular updates and security work</td></tr>
<tr><td><b>Framer</b></td><td>A fast, design-led site for one practice</td><td>Simpler CMS; external tools for forms</td></tr>
<tr><td><b>Dental marketing platforms</b></td><td>All-in-one packages</td><td>Usually rented, with long contracts</td></tr>
</tbody></table></div>
<p>More detail: <a href="../blog/webflow-vs-wordpress.html">Webflow vs WordPress</a> and <a href="../blog/webflow-pricing.html">Webflow pricing in 2026</a>.</p>
"""),
("dw-running", "Running costs after launch", """
<p>Plan for a monthly budget as well as the build. The usual items are hosting (on Webflow, for example, $25 a month for a site with a CMS on yearly billing), a HIPAA-ready form or intake tool, the online booking tool, a review tool if you use one, and some design or content time for new treatments and offers. Template packages from dental marketing companies bundle these into one monthly fee, which is simpler but usually costs more over a few years.</p>
<p>Ask every vendor for the full yearly cost, not only the monthly price, and check what happens to your site, domain and content if you cancel.</p>
"""),
("dw-mistakes", "Common mistakes on dental websites", """
<ul>
<li>One "Services" page instead of a page per treatment.</li>
<li>No prices, no insurance information, no finance options.</li>
<li>A booking button hidden at the bottom of the contact page.</li>
<li>Collecting medical history through a normal contact form.</li>
<li>Stock photos instead of the real team.</li>
<li>A site rented from an agency, so the practice cannot move it or edit it.</li>
</ul>
"""),
("dw-hire", "How to brief a designer for a dental website", """
<p>Send a short brief with: the treatments that matter most to the business, your locations, the booking and practice software you use, the insurers you accept, three websites you like and why, and who will update the site. Our <a href="../blog/website-brief-template.html">website brief template</a> covers the rest. If your current site is the problem, read <a href="../blog/website-redesign-cost.html">what a website redesign costs</a>.</p>
<p>Legal and medical practices share many of the same needs, so our <a href="../blog/law-firm-website-design.html">law firm website guide</a> is useful too.</p>
"""),
  ],
  faq=[("How much does a dental website cost?", "Typically $2,000 to $8,000 for a template from a dental marketing company and $10,000 to $30,000 for a custom site for one location, plus monthly costs for hosting, booking and forms. With Sorvel, custom websites start from $6,900."),
       ("What pages should a dental website have?", "Home, one page per treatment, team, prices or insurance, new patients, emergency dentistry, reviews, and location and contact."),
       ("Can I use a normal contact form on a dental website?", "Only for general questions. Health details and medical history should go through a HIPAA-ready form or patient portal whose vendor signs a Business Associate Agreement."),
       ("Is Webflow HIPAA compliant?", "Webflow's terms say it should not be used for protected health information. Use Webflow for the public pages and an external HIPAA-ready tool for intake forms and booking."),
       ("Should a dental website show prices?", "Yes, at least starting prices or the insurers you accept. Price is one of the main questions patients have, and clear answers bring more bookings."),
       ("How long does it take to build a dental website?", "Usually 3 to 6 weeks for a custom single-location site, depending on content, photos and the booking setup."),
       ("Do I need online booking on my dental website?", "It is strongly recommended. Many patients search outside office hours and book with the first practice that lets them choose a time online."),
       ("How do dental practices rank on Google?", "A complete Google Business Profile, consistent name, address and phone number, a page per treatment and location, reviews, and fast mobile pages."),
  ],
),
]
