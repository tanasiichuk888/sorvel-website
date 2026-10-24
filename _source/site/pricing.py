import sys; sys.path.insert(0, "SOURCE_DIR/site")
from common import *

PX_ICON = {
  "cursor": '<path d="M5 3.5l13 6.2-5.6 1.7-2.2 5.6L5 3.5z"/><path d="M12.4 11.4 18 17"/>',
}
ICON.update(PX_ICON)

ROLES = {
  "LD": ("Design lead", "Owns the direction and signs off every screen before you see it."),
  "WD": ("Web designer", "Pages, layouts and motion in Figma."),
  "PD": ("Product designer", "Flows, product UI and the design system."),
  "BD": ("Brand designer", "Identity, guidelines, decks and assets."),
  "WF": ("Webflow developer", "Clean native builds with a CMS your team can edit."),
  "FR": ("Framer developer", "Fast, motion-rich builds and quick launches."),
  "WP": ("WordPress developer", "Custom themes, plugins and complex content."),
  "SE": ("SEO specialist", "Redirect maps, meta, schema and indexing."),
  "CR": ("CRO specialist", "Hypotheses, tests, tracking and reports."),
}

def it(t, d): return (t, d)

# id, icon, name, list price, unit (list), from?, big price, big unit, desc, note, how[], get[], roles[], cta label, need, foot, badge
PROJECTS = [
 dict(id="website", ic="cursor", name="Website design &amp; build", frm=True, price="$6,900", unit="project",
  desc="A marketing site designed in Figma and built in Webflow, Framer or WordPress by one team, with a CMS your people can edit.",
  note="Fixed scope and price, agreed in writing before anything starts.", badge="Most booked",
  how=[it("Typical timeline: 3 to 6 weeks", "For 5 to 10 pages, from brief to launch, depending on content and feedback speed."),
       it("Paid in two milestones", "The first when we start, the second before launch."),
       it("Progress every 24 to 48 hours", "Written updates and live previews. Nothing ships until you approve it.")],
  get=[it("Sitemap and messaging", "What each page says, in which order, before anything is drawn."),
       it("Wireframes and design", "High-fidelity pages on your brand, desktop to mobile."),
       it("Built on the right platform", "Webflow, Framer or WordPress, chosen around how your team works."),
       it("CMS set up", "Blog, case studies, careers or news, editable without us."),
       it("Motion and interactions", "So the site feels considered, not templated."),
       it("SEO-ready structure", "Meta, schema, redirects and speed from day one."),
       it("Launch and handover", "Domain, QA and a short video guide for your team.")],
  roles=["LD", "WD", "WF"], cta="Get a website quote", need="Website",
  foot="Bigger sites and web apps are quoted from your brief."),
 dict(id="landing", ic="target", name="Landing page", frm=True, price="$2,400", unit="page",
  desc="One page with one job: demos, sign-ups or sales. Designed and built for paid traffic, launches and lead generation.",
  note="Fixed price per page, agreed in writing before we start.",
  how=[it("Typical timeline: 1 to 2 weeks", "From brief to a live, tracked page."),
       it("One revision round included", "Most pages need only one, because the offer is agreed first."),
       it("Ready for your ad accounts", "Fast loading, matched to the campaign and tracked from the first click.")],
  get=[it("Offer and page structure", "Who it's for, what you promise and the order of proof."),
       it("Conversion copy", "Headlines, sections and calls to action written for one action."),
       it("Figma design", "Desktop and mobile, with the main action always in reach."),
       it("Build and integrations", "Forms wired to your CRM, email tool or webhook."),
       it("Analytics events", "Every button and form tracked, so you see what works.")],
  roles=["LD", "WD", "FR"], cta="Get a landing page quote", need="Landing page",
  foot="Each extra page in the same set from $600."),
 dict(id="product", ic="layout", name="Product UI design", frm=True, price="$4,800", unit="project",
  desc="Dashboards, web apps and mobile apps people understand on the first try, with a design system your engineers can build from.",
  note="Priced by the number of flows and screens, agreed before we start.",
  how=[it("Typical timeline: 3 to 6 weeks", "Depending on the number of flows and screens."),
       it("Structure before style", "Wireframes are agreed first, so the UI round is fast."),
       it("Support while they build", "We answer your engineers' questions after handoff.")],
  get=[it("UX review", "A ranked list of what confuses users today and why."),
       it("User flows and wireframes", "Onboarding, core tasks and settings mapped out."),
       it("UI design", "Web, desktop or mobile, in light and dark if needed."),
       it("Design system", "Components and tokens so every new screen is faster."),
       it("Clickable prototype", "To test with users or show to investors."),
       it("Dev-ready handoff", "States, edge cases and specs, organised for engineers.")],
  roles=["LD", "PD"], cta="Get a product design quote", need="Product design",
  foot="Ongoing product work usually runs best on the monthly Design plan."),
 dict(id="brand", ic="brand", name="Brand identity", frm=True, price="$3,900", unit="project",
  desc="An identity that makes a young company look established: logo, colour, type and the rules that keep everything consistent.",
  note="Fixed scope and price, agreed in writing before we start.",
  how=[it("Typical timeline: 2 to 4 weeks", "From direction to a full brand kit."),
       it("Two clear directions", "Fewer options, more thought behind each. You pick one, we refine it."),
       it("Designed for real use", "Tested on your site, deck and social before we call it done.")],
  get=[it("Direction", "A short look at your market and where you can stand apart."),
       it("Logo and wordmark", "A mark that works from a favicon to a billboard."),
       it("Colour and type system", "A palette and type scale with clear roles."),
       it("Brand guidelines", "Simple rules anyone on your team can follow."),
       it("Templates", "Pitch deck, social posts and documents, ready to use.")],
  roles=["LD", "BD"], cta="Get a brand quote", need="Brand identity",
  foot="Pair it with a website and the two are designed together."),
 dict(id="migration", ic="move", name="Website migration", frm=True, price="$2,900", unit="project",
  desc="Move from WordPress to Webflow or Framer, or back, without losing rankings, links or content on the way.",
  note="Priced by pages and CMS items, agreed before we start.",
  how=[it("Typical timeline: 1 to 3 weeks", "Built in parallel, so your current site stays live the whole time."),
       it("Every URL accounted for", "Nothing is switched over until each redirect is tested."),
       it("30 days of monitoring", "We watch Search Console after launch and fix anything that slips.")],
  get=[it("Content and SEO audit", "Every page, post and ranking keyword listed first."),
       it("CMS rebuild", "Collections designed for how your team publishes."),
       it("Content import", "Posts, images and metadata moved automatically."),
       it("301 redirect map", "Every old URL sent to the right new one."),
       it("Launch checks", "Broken links, speed and indexing, before and after.")],
  roles=["WF", "WP", "SE"], cta="Get a migration quote", need="Migration",
  foot="Redesign and migrate at once? We quote both together."),
 dict(id="audit", ic="eye", name="UX audit", frm=False, price="$750", unit="one time",
  desc="An expert review of your site or product before you commit to anything bigger. Clear, ranked and ready to act on.",
  note="The full fee is credited if you continue with a project.", badge="Start here",
  how=[it("Delivered in 3 to 5 days", "As a written report you can share with your team."),
       it("No commitment", "Use it with us, with your own team or with anyone else.")],
  get=[it("Review of key pages or flows", "Where people hesitate, get lost or leave."),
       it("Issues ranked by impact", "So you know what to fix first."),
       it("Annotated screenshots", "Every issue shown, not just described."),
       it("One section redesigned", "A concrete example of the fix."),
       it("Quick wins", "Changes you can ship this week.")],
  roles=["LD"], cta="Book a UX audit", need="UX audit",
  foot="Most clients use it to plan a redesign with confidence."),
]

PLANS = [
 ("Build", [
  dict(id="plan-full", ic="layout", name="Design + Development", frm=False, price="$4,500", unit="mo", bunit="month",
   desc="Senior design and build on one monthly plan. Two requests at once, so approved designs turn into live pages without a hand-off.",
   note="Billed monthly. Pause for a month or cancel anytime.", badge="Best value",
   how=[it("2 active requests", "One in design and one in build, with an unlimited backlog."),
        it("Updates every 24 to 48 hours", "Written progress and live previews as the work moves."),
        it("Weekly written report", "What shipped, what's next and anything we need from you.")],
   get=[it("Website and landing pages", "New pages, sections and campaigns."),
        it("Product UI", "Flows, screens and design systems."),
        it("Brand and pitch decks", "Assets, guidelines and decks for the raise."),
        it("Webflow, Framer and WordPress", "Builds, CMS changes, integrations and fixes."),
        it("Design and build in one loop", "Approved designs go straight to the build.")],
   roles=["LD", "PD", "WD", "WF", "WP"], cta="Start this plan", need="Monthly plan: Design + Development",
   foot="Heavy month? Add a second build request any time."),
  dict(id="plan-design", ic="pen", name="Design", frm=False, price="$2,900", unit="mo", bunit="month",
   desc="Ongoing senior design for product, website and brand, for teams with their own developers.",
   note="Billed monthly. Pause for a month or cancel anytime.",
   how=[it("1 active request", "Worked one at a time from an unlimited backlog."),
        it("Updates every 24 to 48 hours", "Written progress and Figma links as the work moves."),
        it("Weekly written report", "What shipped and what's next.")],
   get=[it("Product design", "Flows, product UI and the design system."),
        it("Website design", "Pages that explain the product and convert."),
        it("Brand and decks", "Assets, social, pitch decks and guidelines."),
        it("Dev-ready files", "Specs and states your developers can build from.")],
   roles=["LD", "PD", "WD", "BD"], cta="Start this plan", need="Monthly plan: Design",
   foot="Need builds too? Design + Development covers both."),
  dict(id="plan-dev", ic="code", name="Development", frm=False, price="$2,900", unit="mo", bunit="month",
   desc="Ongoing builds, changes and fixes on Webflow, Framer or WordPress, for teams who already have designs.",
   note="Billed monthly. Pause for a month or cancel anytime.",
   how=[it("1 active request", "Worked one at a time from an unlimited backlog."),
        it("Updates every 24 to 48 hours", "Staging links so you can check before it goes live."),
        it("Weekly written report", "What shipped and what's next.")],
   get=[it("New pages and sections", "Built pixel-accurate from your Figma."),
        it("CMS work", "New collections, templates and content changes."),
        it("Speed and SEO fixes", "Core Web Vitals, meta, schema and redirects."),
        it("Integrations", "Forms, CRMs, analytics and third-party tools.")],
   roles=["WF", "FR", "WP"], cta="Start this plan", need="Monthly plan: Development",
   foot="Your platform decides who's on the plan."),
 ]),
 ("Grow", [
  dict(id="cro", ic="chart", name="Conversion optimisation", frm=True, price="$1,500", unit="mo", bunit="month",
   desc="One tested improvement a month on the page that matters most. Works on its own or alongside any plan.",
   note="Billed monthly. Cancel anytime.",
   how=[it("One test a month", "Most tests need 2 to 4 weeks of traffic to read clearly."),
        it("Monthly written report", "What we tested, what happened and what's next.")],
   get=[it("Funnel and heatmap review", "Where people drop off and why."),
        it("Written hypothesis", "One clear idea per month, tied to a metric."),
        it("Test designed and built", "The variant, ready to run on real traffic."),
        it("Tracking checks", "So the numbers can be trusted."),
        it("Experiment log", "Every test and result in one place.")],
   roles=["CR", "WD"], cta="Start CRO", need="CRO",
   foot="Best for pages with steady traffic."),
 ]),
 ("Hourly", [
  dict(id="hours", ic="clock", name="25-hour pack", frm=False, price="$2,250", unit="", bunit="25 hours",
   desc="For smaller or irregular tasks. Use the hours on any design or development work within a month.",
   note="Valid for one month. Unused hours don't roll over.",
   how=[it("Live hours log", "See exactly where every hour went."),
        it("Buy again anytime", "No commitment and no contract.")],
   get=[it("Any design task", "Pages, screens, assets or decks."),
        it("Any build task", "Fixes, new sections and CMS changes."),
        it("Senior people only", "The same team that runs our plans.")],
   roles=["LD", "WD", "WF"], cta="Buy hours", need="Hours pack",
   foot="Using it every month? A plan costs less."),
 ]),
]

def row(o, on):
    unit = f'<small>/{o["unit"]}</small>' if o["unit"] in ("mo",) else ""
    frm = "<small>from</small> " if o["frm"] else ""
    badge = f'<em>{o["badge"]}</em>' if o.get("badge") else ""
    return (f'            <button class="px__row{" is-on" if on else ""}" type="button" role="tab" aria-selected="{str(on).lower()}" aria-controls="px-{o["id"]}" id="pxr-{o["id"]}" data-id="{o["id"]}">'
            f'{ico(o["ic"], "px__ic")}<span class="px__name">{o["name"]}{badge}</span><span class="px__price">{frm}{o["price"]}{unit}</span></button>\n')

def panel(o, group, on):
    unit = o.get("bunit") or o["unit"]
    frm = "<small>from</small>" if o["frm"] else ""
    lst = lambda xs: "".join(f'<li><b>{t}</b><span>{d}</span></li>' for t, d in xs)
    roles = "".join(f'<li><i>{k}</i><b>{ROLES[k][0]}</b><span>{ROLES[k][1]}</span></li>' for k in o["roles"])
    href = "contact.html?plan=" + o["id"] + "#brief"
    return f'''          <article class="px__panel" id="px-{o["id"]}" role="tabpanel" aria-labelledby="pxr-{o["id"]}"{"" if on else " hidden"}>
            <div class="px__top">
            <h3>{o["name"]}</h3>
            <p class="px__desc">{o["desc"]}</p>
            <div class="px__big">{frm}<b>{o["price"]}</b><span>/ {unit}</span></div>
            <p class="px__note">{o["note"]}</p>
            <a class="btn btn--primary px__cta" href="{href}"><span class="btn__roll"><span data-text="{o["cta"]}">{o["cta"]}</span></span><span class="btn__arrow" aria-hidden="true">{ARROW}{ARROW}</span></a>
            <p class="px__alt">or <a href="https://t.me/tanasiychuk8" target="_blank" rel="noopener">ask a question on Telegram</a>, reply in about 10 minutes</p>
            </div>
            <div class="px__scroll">
            <p class="px__lbl">What you get</p>
            <ul class="px__list">{lst(o["get"])}</ul>
            <button class="px__more" type="button" aria-expanded="false">Timeline and team <span aria-hidden="true"></span></button>
            <div class="px__extra">
              <p class="px__lbl">How it works</p>
              <ul class="px__list">{lst(o["how"])}</ul>
              <p class="px__lbl">Who works on it</p>
              <ul class="px__team">{roles}</ul>
            </div>
            <p class="px__foot">{o["foot"]}</p>
            </div>
          </article>
'''

def promo(kind):
    if kind == "projects":
        return f'''          <a class="px__promo" href="#audit" data-pick="audit">
            <span class="px__promo-tag">Not ready to commit?</span>
            <b>Start with a $750 UX audit.</b>
            <span>Ranked issues and one redesigned section in 3 to 5 days. The full fee is credited if you continue.</span>
            <span class="px__promo-go">See the audit <span aria-hidden="true">→</span></span>
          </a>
'''
    return f'''          <a class="px__promo" href="#hours" data-pick="hours">
            <span class="px__promo-tag">Not sure about a plan?</span>
            <b>Try us with 25 hours first.</b>
            <span>Same senior team, no contract. If you stay on a plan, it costs less per hour than the pack.</span>
            <span class="px__promo-go">See the hours pack <span aria-hidden="true">→</span></span>
          </a>
'''

def pricing():
    p = ""
    # projects tab
    prj_rows = '            <p class="px__group">Projects</p>\n            <div class="px__box">\n' + "".join(row(o, i == 0) for i, o in enumerate(PROJECTS)) + "            </div>\n"
    pln_rows = ""
    for g, items in PLANS:
        pln_rows += f'            <p class="px__group">{g}</p>\n            <div class="px__box">\n' + "".join(row(o, False) for o in items) + "            </div>\n"
    panels = "".join(panel(o, "Projects", i == 0) for i, o in enumerate(PROJECTS))
    panels += "".join(panel(o, g, False) for g, items in PLANS for o in items)

    trs_rows = [("Active requests at a time", "1 design", "2: design + build", "1 build"),
                ("Product, website and brand design", "yes", "yes", "no"),
                ("Webflow, Framer, WordPress builds", "no", "yes", "yes"),
                ("Updates every 24 to 48 hours", "yes", "yes", "yes"),
                ("Unlimited backlog", "yes", "yes", "yes"),
                ("Weekly written report", "yes", "yes", "yes"),
                ("Pause or cancel anytime", "yes", "yes", "yes")]
    def cell(v):
        if v == "yes": return f'<td><span aria-label="Included">{ico("check", "ct-ico")}</span></td>'
        if v == "no": return '<td><span class="ct-n" aria-label="Not included">—</span></td>'
        return f"<td>{v}</td>"
    trs = "".join(f'<tr><th scope="row">{r[0]}</th>{cell(r[1])}{cell(r[2])}{cell(r[3])}</tr>' for r in trs_rows)

    body = f'''    <section class="pg-hero pg-hero--center px-hero" id="top">
      <canvas class="hero__dots" aria-hidden="true"></canvas>
      <div class="wrap">
        <nav class="cs-crumbs" data-intro style="--d:.05s"><a href="index.html">Home</a><span>/</span><span>Pricing</span></nav>
        <h1 class="cs-title">
          <span class="line"><span class="line__in" style="--d:.15s">A senior team,</span></span>
          <span class="line"><span class="line__in" style="--d:.25s">priced <span class="accent">upfront</span>.</span></span>
        </h1>
        <p class="cs-lead" data-intro style="--d:.4s">A fixed-price project or a monthly plan. Pick one and see exactly what you get.</p>
        <div class="ptabs" role="tablist" aria-label="Pricing type" data-intro style="--d:.5s">
          <button class="is-on" role="tab" aria-selected="true" data-tab="projects">One-time projects</button>
          <button role="tab" aria-selected="false" data-tab="plans">Monthly plans <em>Flexible</em></button>
          <i class="ptabs__pill" aria-hidden="true"></i>
        </div>
      </div>
    </section>

    <section class="sec px-sec" style="padding-top:0;border-top:0">
      <div class="wrap">
        <div class="px">
          <div class="px__menu" role="tablist" aria-label="Pricing options">
            <div class="px__set" data-set="projects">
{prj_rows}{promo("projects")}            </div>
            <div class="px__set" data-set="plans" hidden>
{pln_rows}{promo("plans")}            </div>
          </div>
          <div class="px__stage">
{panels}          </div>
        </div>
      </div>
    </section>

    <section class="sec">
      <div class="wrap">
{sec_head("Why “from”", 'What moves <span class="dim">the final price.</span>', "Two projects are never the same size. These are the things that change a quote, so there are no surprises later.")}
        <div class="moves">
          <div data-reveal>{ico("layout")}<h3>Number of pages</h3><p>The base price covers a typical scope. Extra unique page templates are added at a fixed rate per page.</p></div>
          <div data-reveal style="--d:.05s">{ico("pen")}<h3>Copy and content</h3><p>We polish your text as standard. Writing every page from scratch is quoted separately.</p></div>
          <div data-reveal style="--d:.1s">{ico("link")}<h3>Integrations</h3><p>Forms and analytics are included. CRMs, payments, memberships or custom code add to the scope.</p></div>
          <div data-reveal style="--d:.15s">{ico("chat")}<h3>Languages</h3><p>A second language adds layouts to check and content to set up, so it's priced per language.</p></div>
        </div>
      </div>
    </section>

    <section class="sec">
      <div class="wrap">
{sec_head("In every engagement", 'What you can <span class="dim">count on.</span>')}
        <div class="trust">
          <div data-reveal>{ico("shield")}<h3>Fixed price before we start. No surprise invoices.</h3><p>Scope, timeline and price are written down and approved by you before any work begins.</p></div>
          <div data-reveal style="--d:.05s">{ico("key")}<h3>You own everything</h3><p>Figma files, code, CMS and assets are yours, set up in your own accounts.</p></div>
          <div data-reveal style="--d:.1s">{ico("doc")}<h3>NDA on request</h3><p>We sign yours or ours before you share anything sensitive.</p></div>
          <div data-reveal style="--d:.15s">{ico("eye")}<h3>Nothing ships unapproved</h3><p>Every page and screen goes live only after your sign-off.</p></div>
          <div data-reveal style="--d:.2s">{ico("chat")}<h3>Written updates</h3><p>Progress every 24 to 48 hours, no meetings needed.</p></div>
          <div data-reveal style="--d:.25s">{ico("clock")}<h3>EU and US overlap</h3><p>Based in Europe, with hours that overlap US mornings.</p></div>
        </div>
      </div>
    </section>
'''
    body += faq([
      ("Why do prices show “from”?", "Because two websites are never the same size. The price is where a typical project starts. Send a brief and you'll get an exact fixed price in writing within 24 hours."),
      ("How do payments work?", "Projects are split into two milestones: the first when we start, the second before launch. Monthly plans are billed at the start of each month."),
      ("What is an active request?", "A single task we're working on right now, like a new page, a feature screen or a set of fixes. When one is done, the next one from your backlog starts."),
      ("Project or monthly plan?", "Choose a project when you know exactly what you need, like a new website. Choose a plan when work keeps coming: new pages, features, tests and fixes every month."),
      ("Can I pause or cancel a monthly plan?", "Yes. Pause for a month or cancel anytime, with no notice period and no fee."),
      ("What if the scope changes halfway?", "On a project, we write up the change and its price, and you decide. On a monthly plan, it simply goes into the backlog."),
      ("Can we start small?", "Yes. The $750 UX audit is the easiest way to see how we work, and the full fee is credited if you continue."),
    ])
    body += cta(p, "Ready when you are", "Get an exact quote <br>in 24 hours.")
    page("pricing.html", "Pricing | Sorvel Studio", "Clear pricing for websites, landing pages, product UI, brand and migrations, as fixed-price projects or monthly plans.", "pricing", body, p, dock=False)

if __name__ == "__main__":
    pricing()
