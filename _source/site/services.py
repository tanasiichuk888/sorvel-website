import sys; sys.path.insert(0, "SOURCE_DIR/site")
from common import *
import scenes

S = {
"websites": dict(
  title="Websites | Sorvel Studio", desc="Marketing websites designed in Figma and built in Webflow, Framer or WordPress for SaaS, fintech and B2B companies.",
  eyebrow="Service · Websites", lines=["Websites that", 'explain fast and <span class="accent">sell</span>.'],
  lead="A marketing site that says what you do in five seconds and makes the next step obvious. Designed in Figma, built in Webflow, Framer or WordPress, and handed over so your team can run it.",
  price="$6,900", price_note="3 to 6 weeks for a typical 5 to 10 page site", need="Website",
  who=[("Your site no longer matches your product", "The company grew, the product changed, but the website still pitches last year's version. Visitors leave before they understand what you sell."),
       ("Leads arrive, then vanish", "Traffic is fine, but few people book a demo or send a form."),
       ("Every change needs a developer", "Simple text edits wait days in a dev queue.")],
  incl=[("pen", "Messaging and sitemap", "We shape what each page says and in which order, before anything is drawn."),
        ("figma", "Figma design", "Desktop, tablet and mobile, on a component system that keeps every page consistent."),
        ("code", "Webflow, Framer or WordPress", "A clean native build, no bloated templates or page builders."),
        ("grid", "CMS you can edit", "Blog, case studies, careers or news, set up so your team updates them alone."),
        ("bolt", "Motion that feels expensive", "Scroll reveals, hover states and interactions that stay fast."),
        ("search", "Technical SEO", "Clean structure, meta, schema, redirects and speed, ready for search on day one.")],
  phases=[("Week 1", "Strategy and structure", "Goals, audience and the sitemap.", ["Sitemap", "Messaging per page", "Wireframes"]),
          ("Weeks 1 to 3", "Design", "The look, on desktop and mobile.", ["Home page first", "Inner pages", "Prototype"]),
          ("Weeks 2 to 5", "Build", "Native build with CMS and motion.", ["Pixel-accurate", "CMS set up", "Forms and analytics"]),
          ("Launch", "QA and handover", "Tested, live and documented.", ["Cross-device QA", "Domain and redirects", "Video guide"])],
  plat=[("Webflow", "Best for marketing teams who want to edit everything visually."), ("Framer", "Best for fast, motion-rich sites and quick launches."),
        ("WordPress", "Best when you need plugins, complex content or an existing setup."), ("Not sure?", "Tell us how your team works and we'll recommend one.")],
  cases=["valhalla-capital", "serverscamp", "arlowe-baxter", "awswrap"],
  faq=[("Which platform should we choose?", "Webflow if your marketing team edits often, Framer for speed and motion, WordPress if you rely on plugins or already run it. We'll recommend one in the plan."),
       ("Can you redesign our existing site?", "Yes. Most of our website projects are redesigns. We keep what works, fix what doesn't and protect your SEO along the way."),
       ("Do you write the copy?", "We shape the structure and messaging of every page and polish your text. Full copywriting from scratch can be added to the scope."),
       ("Can we edit the site ourselves after launch?", "Yes. Everything is set up in a CMS, and you get a short video guide. Most clients never need us for small edits."),
       ("How long does a website take?", "Usually 3 to 6 weeks for 5 to 10 pages, depending on content and feedback speed.")]),
"landing-pages": dict(
  title="Landing pages and CRO | Sorvel Studio", desc="High-converting landing pages for ads and launches, plus monthly conversion testing. Designed in Figma and built in Webflow, Framer or WordPress.",
  eyebrow="Service · Landing pages & CRO", lines=["One page.", 'One <span class="accent">goal</span>.', "Measured."],
  lead="Landing pages built around a single action: a demo, a sign-up, a call or a sale. Then we keep testing the offer, the layout and the copy, and keep what moves the number.",
  price="$2,400", price_note="1 to 2 weeks per page, CRO from $1,500 a month", need="Landing page",
  who=[("You're paying for clicks that don't convert", "Ads send traffic to a generic home page, and most of it leaves without doing anything."),
       ("You're launching something new", "A product, a feature or an event that needs its own page this month."),
       ("You never know what works", "Changes are made on gut feeling, and nobody measures the result.")],
  incl=[("target", "Offer and structure", "What you promise, to whom, and the order of proof that makes it believable."),
        ("pen", "Conversion copy", "Headlines, sections and calls to action written for the action you want."),
        ("figma", "Figma design", "Desktop and mobile, with the main action always in reach."),
        ("code", "Fast build", "Webflow, Framer or WordPress, with forms and integrations wired up."),
        ("chart", "Tracking", "Analytics events on every button and form, so you see what happens."),
        ("flask", "A/B testing", "Variants of the headline, offer or layout, tested on real traffic.")],
  phases=[("Days 1 to 2", "Offer and outline", "Who it's for and what they need to see.", ["Audience and offer", "Page outline", "Copy draft"]),
          ("Days 2 to 6", "Design", "Desktop and mobile in Figma.", ["First design", "One revision round", "Final"]),
          ("Days 5 to 10", "Build and tracking", "Live page with events.", ["Build", "Forms and CRM", "Analytics events"]),
          ("Every month", "Test and improve", "Optional CRO plan.", ["Heatmaps", "One A/B test", "Written results"])],
  plat=[("Paid ads", "Pages matched to each campaign and keyword."), ("Product launches", "A page that tells one story and drives one action."),
        ("Lead generation", "Forms, calculators and quizzes that qualify as they convert."), ("Local services", "Call-first pages built for people in a hurry.")],
  cases=["salinas-defense", "arlowe-baxter"],
  faq=[("How is a landing page different from a website?", "A website serves many visitors with many questions. A landing page serves one audience with one offer and one action, so it converts far better for ads and launches."),
       ("Can you connect it to our CRM?", "Yes. HubSpot, Pipedrive, Mailchimp, Zapier or a webhook into your own system."),
       ("Do you run the ads too?", "No, we focus on the page. We'll happily work alongside your ads team or agency."),
       ("How does the CRO plan work?", "Each month we review the data, write a hypothesis, design and build one test, then report the result. Winners stay, losers go."),
       ("How fast can a page go live?", "Usually 1 to 2 weeks from brief to launch. Urgent launches can be faster.")]),
"product-design": dict(
  title="Product design | Sorvel Studio", desc="UI and UX design for SaaS products, dashboards, web apps and mobile apps, with design systems your developers can build from.",
  eyebrow="Service · Product design", lines=["Products people get", 'on the <span class="accent">first try</span>.'],
  lead="Dashboards, web apps and mobile apps designed around how people actually use them. Clear flows, a solid design system and Figma files your engineers can build from without guessing.",
  price="$4,800", price_note="3 to 6 weeks, priced by flows and screens", need="Product design",
  who=[("Users get lost in your product", "Support tickets keep asking where things are, and new users drop off during setup."),
       ("The UI grew without a plan", "Five shades of blue, three button styles, and every new screen takes longer to design."),
       ("Your developers are guessing", "Designs arrive without states, edge cases or specs, so the build never matches.")],
  incl=[("eye", "UX review", "A ranked list of what confuses users today and why."),
        ("move", "User flows", "Onboarding, core tasks and settings mapped before any pixels."),
        ("layout", "UI design", "Clean, calm screens for web, desktop and mobile, light and dark."),
        ("grid", "Design system", "Components, tokens and rules so every new screen is faster."),
        ("spark", "Prototypes", "Clickable flows to test with users or show investors."),
        ("code", "Dev-ready handoff", "States, edge cases and specs, organised for your engineers.")],
  phases=[("Week 1", "Review and flows", "What works, what doesn't.", ["UX review", "User flows", "Priorities"]),
          ("Weeks 1 to 2", "Wireframes", "Structure before style.", ["Key screens", "Edge cases", "Feedback round"]),
          ("Weeks 2 to 4", "UI and system", "The look and the parts.", ["Final screens", "Components", "Prototype"]),
          ("Handoff", "Ready to build", "Everything engineers need.", ["Specs and states", "Tokens", "Q&A while they build"])],
  plat=[("SaaS dashboards", "Analytics, admin panels and complex tables made readable."), ("Web apps", "Booking, marketplaces, internal tools and portals."),
        ("Mobile apps", "iOS and Android screens that follow platform patterns."), ("Design systems", "From a few components to a full library with tokens.")],
  cases=["serverscamp"],
  faq=[("Do you build the product too?", "We design the product and hand it to your engineers with everything they need. For marketing sites around the product, we design and build."),
       ("Can you work with our existing design system?", "Yes. We extend what you have, or clean it up first if it has grown messy."),
       ("Do you do user research?", "We start with a UX review of your product and data. Interviews and usability tests can be added to the scope."),
       ("Light and dark mode?", "Yes, when it makes sense for your users. We set up tokens so both stay in sync."),
       ("How do you price product work?", "By the number of flows and screens. Ongoing product work usually runs best on a monthly design plan.")]),
"brand-identity": dict(
  title="Brand identity | Sorvel Studio", desc="Brand identity for young companies: logo, colour, type, guidelines and templates that make you look established from day one.",
  eyebrow="Service · Brand identity", lines=["Look established", 'from <span class="accent">day one</span>.'],
  lead="An identity that makes a young company look like it's been around for years. Logo, colour, type and the simple rules that keep every page, deck and post consistent.",
  price="$3,900", price_note="2 to 4 weeks", need="Brand identity",
  who=[("You look smaller than you are", "The product is serious, but the logo was a weekend job and it shows in every investor meeting."),
       ("Nothing matches", "The site, the deck and the social posts all look like different companies."),
       ("You're about to launch or raise", "You need a brand that holds up in front of customers and investors, quickly.")],
  incl=[("search", "Direction", "A short look at your market, competitors and where you can stand apart."),
        ("brand", "Logo and wordmark", "A mark that works from a favicon to a billboard."),
        ("pen", "Colour and type", "A palette and type system with clear roles for each."),
        ("doc", "Brand guidelines", "Simple rules anyone on your team can follow."),
        ("grid", "Templates", "Social posts, pitch deck and documents, ready to use."),
        ("key", "Organised files", "Every asset exported and named, in your own Figma.")],
  phases=[("Week 1", "Direction", "Where the brand should sit.", ["Market look", "Moodboards", "Two directions"]),
          ("Weeks 1 to 2", "Identity", "The chosen direction, refined.", ["Logo", "Colour and type", "Applications"]),
          ("Weeks 2 to 3", "System", "Rules and templates.", ["Guidelines", "Deck and social", "Website styles"]),
          ("Handover", "Ready to use", "Everything exported.", ["Logo pack", "Figma library", "Short guide"])],
  plat=[("Startups", "A brand ready for launch, customers and investors."), ("Rebrands", "A fresh look that keeps what people already recognise."),
        ("Brand plus website", "Identity and site designed together, so they match perfectly."), ("Pitch decks", "Investor decks in your new brand, structured to tell the story.")],
  cases=["valhalla-capital", "serverscamp"], cases_title='Design systems <span class="dim">we built.</span>',
  faq=[("How many logo options do we get?", "We present two clear directions, then refine the one you choose. Fewer options, more thought behind each."),
       ("Can you refresh our brand instead of starting over?", "Yes. Often a stronger type system, cleaner colours and better rules are enough."),
       ("Can you design the website at the same time?", "Yes, and it's the best way to do it. The site then becomes the first real test of the brand."),
       ("Do we get the source files?", "Yes. All files are yours, organised in your own Figma, with exports for every use."),
       ("Do you name companies?", "Naming isn't part of our standard scope, but we can suggest options as part of the direction phase.")]),
"migrations": dict(
  title="Website migrations | Sorvel Studio", desc="Move your website from WordPress to Webflow or Framer, or the other way round, without losing rankings, links or content.",
  eyebrow="Service · Website migrations", lines=["Move platforms.", 'Keep your <span class="accent">rankings</span>.'],
  lead="Moving from WordPress to Webflow or Framer, or the other way round, without losing traffic, links or content on the way. Every old URL accounted for, every page checked before launch.",
  price="$2,900", price_note="1 to 3 weeks, depending on pages and CMS items", need="Migration",
  who=[("Your current platform slows you down", "Plugin updates break things, edits need a developer and the site keeps getting slower."),
       ("You're scared of losing traffic", "Years of SEO work sit on your current URLs, and one bad move could wipe it out."),
       ("Content is everywhere", "Hundreds of posts and pages with no clear map of what's where.")],
  incl=[("search", "Content and SEO audit", "Every page, post and ranking keyword listed before anything moves."),
        ("grid", "CMS rebuild", "Collections designed for how your team really publishes."),
        ("move", "Content import", "Posts, images and metadata moved cleanly, not copy-pasted."),
        ("link", "Redirect map", "Every old URL sent to the right new one with 301 redirects."),
        ("code", "Meta and schema", "Titles, descriptions and structured data kept or improved."),
        ("check", "Launch checks", "Broken links, speed and indexing checked before and after launch.")],
  phases=[("Week 1", "Audit", "Know exactly what you have.", ["Page inventory", "Top keywords", "Redirect plan"]),
          ("Weeks 1 to 2", "Rebuild", "New platform, same content.", ["CMS structure", "Templates", "Content import"]),
          ("Week 2 to 3", "Check", "Nothing left behind.", ["Redirects tested", "Meta compared", "Speed tested"]),
          ("Launch + 30 days", "Watch", "Make sure rankings hold.", ["Search Console", "Fix 404s", "Report"])],
  plat=[("WordPress to Webflow", "The most common move, for teams who want visual editing."), ("WordPress to Framer", "For smaller, faster, motion-rich marketing sites."),
        ("Webflow to WordPress", "When you need plugins, membership or complex content."), ("Redesign + migrate", "A new design and a new platform in one project.")],
  cases=["valhalla-capital", "arlowe-baxter"], cases_title='Rebuilds <span class="dim">we have shipped.</span>',
  faq=[("Will we lose our Google rankings?", "Not if it's done properly. We map every old URL to a new one, keep your meta and structure, and watch Search Console for 30 days after launch."),
       ("Can you migrate and redesign at once?", "Yes, and it often saves time. We'd still keep URLs and content structure stable where rankings depend on them."),
       ("How many pages can you move?", "From a 10 page site to thousands of blog posts. Larger content sets are imported automatically, not by hand."),
       ("Will the site be down during the move?", "No. We build on the new platform in parallel and switch the domain only when everything is checked."),
       ("What about forms, integrations and analytics?", "We list them all in the audit and reconnect each one on the new platform.")]),
}

PLAN_ID = {'Website': 'website', 'Landing page': 'landing', 'Product design': 'product', 'Brand identity': 'brand', 'Migration': 'migration'}

def service(slug):
    d = S[slug]; p = "../"
    nm = [t for s, t, *_ in SERVICES if s == slug][0].replace("&", "&amp;")
    probs = "\n".join(f'          <article data-reveal style="--d:{i*.06:.2f}s"><h3>{t}</h3><p>{x}</p></article>' for i, (t, x) in enumerate(d["who"]))
    incl = "\n".join(f'          <div data-reveal style="--d:{(i%3)*.05:.2f}s">{ico(ic)}<h3>{t}</h3><p>{x}</p></div>' for i, (ic, t, x) in enumerate(d["incl"]))
    ph = ""
    for i, (when, h, x, lis) in enumerate(d["phases"]):
        li = "".join(f"<li>{a}</li>" for a in lis)
        ph += f'          <div class="cs-phase" style="--i:{i}"><p class="cs-phase__when">{when}</p><h3>{h}</h3><p>{x}</p><ul>{li}</ul></div>\n'
    plat = "\n".join(f'          <div data-reveal style="--d:{i*.05:.2f}s"><b>{a}</b><span>{b}</span></div>' for i, (a, b) in enumerate(d["plat"]))
    cs = d["cases"]; cards = "\n".join(pcard(c, p, wide=(len(cs) % 2 == 1 and i == 0)) for i, c in enumerate(cs))
    other = "".join(f'<a class="cs-more__row" href="{s}.html" data-reveal style="--d:{i*.05:.2f}s"><span class="cs-more__name">{t.replace("&","&amp;")}</span><span class="cs-more__tag">{dd}</span><span class="cs-more__go" aria-hidden="true">{DIAG}</span></a>'
                    for i, (s, t, dd, ic) in enumerate([x for x in SERVICES if x[0] != slug]))
    body = hero(f'<a href="../index.html#services">Services</a><span>/</span><span>{nm}</span>', d["eyebrow"], d["lines"], d["lead"],
                btn_primary(f"../contact.html?plan={PLAN_ID[d['need']]}#brief", "Get a quote") + btn_ghost("../pricing.html", "See pricing"), p=p, visual=scenes.svc(slug))
    body += f'''
    <section class="sec cs-brief" data-chapter="Who it's for">
      <div class="wrap">
{sec_head("Sound familiar?", 'Who this is <span class="dim">built for.</span>')}
        <div class="cs-problems" style="margin-top:0">
{probs}
        </div>
      </div>
    </section>

    <section class="sec" data-chapter="Included">
      <div class="wrap">
{sec_head("What's included", 'Everything it takes, <span class="dim">nothing padded.</span>', "One senior team covers it end to end, so nothing gets lost between agencies or freelancers.")}
        <div class="incl">
{incl}
        </div>
      </div>
    </section>

    <section class="sec cs-chapter" data-chapter="Process">
      <div class="wrap">
{sec_head("How it runs", 'Clear steps, <span class="dim">written updates.</span>', "You review on your own time. We send progress every 24 to 48 hours, no meetings needed.")}
        <div class="cs-process" data-reveal>
{ph}        </div>
      </div>
    </section>

    <section class="sec" data-chapter="Fit">
      <div class="wrap">
{sec_head("Where it fits", 'Made for <span class="dim">your situation.</span>')}
        <div class="plat">
{plat}
        </div>
      </div>
    </section>

    <section class="sec" data-chapter="Work">
      <div class="wrap">
{sec_head("Related work", d.get("cases_title", 'Projects <span class="dim">like yours.</span>'), "", row=False)}
        <div class="pcards">
{cards}
        </div>
      </div>
    </section>

    <section class="sec" data-chapter="Pricing">
      <div class="wrap">
        <div class="sprice" data-reveal>
          <div class="sprice__main">
            <p class="sprice__tag">Pricing</p>
            <h2 class="sprice__title">{nm}</h2>
            <p class="sprice__note">{d["price_note"]}. Exact fixed quote in writing within 24 hours.</p>
          </div>
          <div class="sprice__side">
            <div class="sprice__num"><small>from</small><b>{d["price"]}</b><span>fixed price</span></div>
            <div class="sprice__btns">
              {btn_primary(f"../contact.html?plan={PLAN_ID[d['need']]}#brief", "Get an exact quote", lg=False)}
              {btn_ghost("../pricing.html", "Compare all prices", lg=False)}
            </div>
          </div>
        </div>
      </div>
    </section>
'''
    body += faq(d["faq"])
    body += f'''    <section class="cs-more">
      <div class="wrap">
        <header class="cs-more__head" data-reveal><p class="eyebrow">Other services</p><a class="cs-more__all" href="../pricing.html">All prices <span aria-hidden="true">→</span></a></header>
        <div class="cs-more__list">{other}</div>
      </div>
    </section>
'''
    body += cta(p)
    page(f"services/{slug}.html", d["title"], d["desc"], "services", body, p)

if __name__ == "__main__":
    for s in S: service(s)
