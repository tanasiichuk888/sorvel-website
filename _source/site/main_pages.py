import sys; sys.path.insert(0, "SOURCE_DIR/site")
from common import *
import scenes

# ======================= WORK =======================
WALL = [
    [("ci-isac/hero.webp", "CI-ISAC Australia", "Cyber security", "ci-isac"), ("valhalla/hero.webp", "Valhalla Capital", "Fintech", "valhalla-capital"), ("college-classics/colours.webp", "College Classics", "Shopify", "college-classics"),
     ("varsity-city/segments.webp", "Varsity City", "Shopify", "varsity-city"), ("serverscamp/panel.webp", "ServersCamp", "Product UI", "serverscamp"), ("waveads/who.webp", "AdVoyage", "Framer", "waveads"), ("vibz/hero.webp", "Vibz", "Figma", "vibz"), ("vibz/hero.webp", "Vibz", "Figma", "vibz"), ("arlowe-baxter/dashboard.webp", "Arlowe Baxter", "Webflow", "arlowe-baxter")],
    [("college-classics/hero.webp", "College Classics", "Shopify", "college-classics"), ("awswrap/calculator.webp", "AWS Wrap", "WordPress", "awswrap"), ("alma-secret/bestsellers.webp", "Alma Secret", "Shopify", "alma-secret"),
     ("waveads/hero.webp", "AdVoyage", "Framer", "waveads"), ("ci-isac/pillars.webp", "CI-ISAC Australia", "Webflow", "ci-isac"), ("varsity-city/hero.webp", "Varsity City", "Apparel", "varsity-city"), ("salinas/hero.webp", "Salinas Defense", "Landing page", "salinas-defense"), ("valhalla/fund.webp", "Valhalla Capital", "Webflow", "valhalla-capital")],
    [("serverscamp/hero.webp", "ServersCamp", "Cloud", "serverscamp"), ("arlowe-baxter/hero.webp", "Arlowe Baxter", "Property tech", "arlowe-baxter"), ("alma-secret/signature.webp", "Alma Secret", "Beauty", "alma-secret"),
     ("awswrap/hero.webp", "AWS Wrap", "Automotive", "awswrap"), ("college-classics/why.webp", "College Classics", "Fashion", "college-classics"), ("varsity-city/portfolio.webp", "Varsity City", "Portfolio", "varsity-city"), ("salinas/why.webp", "Salinas Defense", "Legal", "salinas-defense")],
]

def work():
    p = ""
    ORDER_W = ["valhalla-capital", "visit-pemba", "skyli", "ci-isac", "open-select", "mutmachbuch", "serverscamp", "arlowe-baxter", "copliancy", "agentur", "college-classics", "alma-secret", "noir", "wehike",
               "varsity-city", "vibz", "awswrap", "salinas-defense", "waveads"]
    cards = [pcard(x, p, kind=1) for x in ORDER_W if x not in HIDDEN]
    _vis = [x for x in ORDER_W if x not in HIDDEN]; _n = lambda k: sum(k in CASES[x]["kind"] for x in _vis)
    varsity = f'''          <a class="pcard pcard--cta" href="contact.html" data-kind="all-kinds" data-reveal>
            <div class="pcta">
              <p class="eyebrow">Your project</p>
              <h3>This spot is <span class="accent">yours</span>.</h3>
              <p class="pcta__lead">Send a short brief. You get a written plan, timeline and fixed price within 24 hours.</p>
              <span class="pcta__btn">Start a project <span aria-hidden="true">→</span></span>
              <span class="pcta__ghost" aria-hidden="true"><i></i><i></i><i></i></span>
            </div>
          </a>'''
    body = hero('<span>Work</span>', "Selected work", ["Work that had", 'a <span class="accent">job</span> to do.'],
                "Every project here started with a business problem: investors who didn't trust the site, engineers who couldn't see the benchmarks, landlords who never reached the form. Here's how each one was solved.",
                btn_primary("contact.html", "Start a project") + btn_ghost("https://t.me/tanasiychuk8", "Write on Telegram", tg=True), p=p, visual=scenes.wall(p, [[t for t in col if t[3] not in HIDDEN] for col in WALL]))
    body += f'''
    <section class="cs-numbers" aria-label="Studio in numbers">
      <div class="wrap">
        <div class="cs-bench">
          <div data-reveal><b><span data-count="600">0</span>+</b><span>Projects shipped</span><em>Websites, products and brands</em></div>
          <div data-reveal style="--d:.06s"><b><span data-count="11">0</span>+</b><span>Years in design</span><em>Web, product and brand</em></div>
          <div data-reveal style="--d:.12s"><b><span data-count="5" data-dec="1">0</span></b><span>Average client rating</span><em>Across every review we share</em></div>
          <div data-reveal style="--d:.18s"><b><span data-count="24">0</span>h</b><span>To a written plan</span><em>After you send a brief</em></div>
        </div>
      </div>
    </section>

    <section class="sec" data-chapter="Projects">
      <div class="wrap">
{sec_head("Case studies", 'Real projects, <span class="dim">explained start to finish.</span>', "Each case shows the problem, the decisions we made and what the client walked away with. Filter by the kind of work you need.")}
        <div class="filters" role="tablist" aria-label="Filter projects" data-reveal>
          <button class="is-on" data-f="all">All<sup>{len(_vis)}</sup></button>
          <button data-f="websites">Websites<sup>{_n("websites")}</sup></button>
          <button data-f="ecommerce">E-commerce<sup>{_n("ecommerce")}</sup></button>
          <button data-f="landing">Landing pages<sup>{_n("landing")}</sup></button>
          <button data-f="product">Product UI<sup>{_n("product")}</sup></button>
        </div>
        <div class="pcards">
{chr(10).join(cards)}
{varsity}
        </div>
        <div class="pnote" data-reveal><span>Many projects run under NDA, so they never make it to a public page. <b>Need an example in your industry?</b></span><a href="mailto:hello@sorvel.agency?subject=Examples%20in%20my%20industry">Ask for private examples →</a></div>
      </div>
    </section>

    <section class="cs-reel" aria-hidden="true">
      <div class="cs-reel__track">{"".join(f'<img src="img/work/{x}" alt="" loading="lazy" width="1600" height="1000">' for x in ["valhalla/webinar.webp","arlowe-baxter/services.webp","salinas/about.webp","awswrap/work.webp","college-classics/colours.webp","waveads/who.webp","valhalla/fund.webp","arlowe-baxter/dashboard.webp","salinas/why.webp","awswrap/calculator.webp","college-classics/why.webp"]*2)}</div>
    </section>
'''
    body += cta(p, "Your project next", "Let's make yours <br>the next case study.")
    page("work.html", "Work | Sorvel Studio", "Case studies from Sorvel: websites, landing pages and product UI for fintech, SaaS, property tech and local businesses.", "work", body, p)

# ======================= PRICING =======================
def plan(tag, name, desc, price_small, price, unit, meta, items, cta_label, cta_href, note="", hero=False, badge=""):
    lis = "".join(f"<li>{i}</li>" for i in items)
    m = "".join(f"<span>{x}</span>" for x in meta)
    b = f"<b>{badge}</b>" if badge else ""
    return f'''        <article class="plan{" plan--hero" if hero else ""}" data-reveal>
          <div>
            <p class="plan__tag">{tag}{b}</p>
            <h3>{name}</h3>
            <p class="plan__desc">{desc}</p>
            <div class="plan__price"><small>{price_small}</small><b>{price}</b><span>{unit}</span></div>
            <div class="plan__meta">{m}</div>
          </div>
          <div class="plan__side">
            <ul class="plan__list">{lis}</ul>
            <div class="plan__foot">{btn_primary(cta_href, cta_label, lg=False)}<p>{note}</p></div>
          </div>
        </article>
'''
def pricing():
    p = ""
    projects = (
      plan("One-time project", "Website design &amp; build", "A complete marketing site, designed in Figma and built in Webflow, Framer or WordPress. Fixed scope and fixed price, agreed before we start.",
           "from", "$2,900", "per project", ["3 to 6 weeks", "5 to 10 pages", "2 milestones"],
           ["Sitemap and messaging", "Wireframes and Figma design", "Desktop, tablet and mobile", "Webflow, Framer or WordPress build", "CMS for blog, cases or news", "Motion and interactions", "Technical SEO setup", "Launch, handover and a short guide"],
           "Get a quote", "contact.html?need=Website", "Bigger sites are quoted from your brief.", hero=True, badge="Most booked")
      + plan("One-time project", "Landing page", "One page with one job: sign-ups, demos, calls or sales. Built for paid traffic and launches, with the copy structure to back it.",
           "from", "$1,200", "per page", ["1 to 2 weeks", "Design + build", "Ready for ads"],
           ["Offer and copy structure", "Figma design, desktop and mobile", "Webflow, Framer or WordPress build", "Forms and integrations", "Analytics events", "Speed and SEO basics"],
           "Get a quote", "contact.html?need=Landing%20page", "Extra pages from $350 each.")
      + plan("One-time project", "Product UI design", "Screens for a SaaS product, dashboard or app that people understand on the first try, with a design system your developers can build from.",
           "from", "$2,400", "per project", ["2 to 5 weeks", "Figma only", "Dev-ready handoff"],
           ["UX review of what exists", "User flows", "Wireframes and prototypes", "UI for web or mobile", "Component library", "Handoff notes for engineers"],
           "Get a quote", "contact.html?need=Product%20design", "Priced by number of flows and screens.")
      + '        <div class="plans-duo">\n'
      + plan("One-time project", "Brand identity", "Logo, colour, type and the rules that keep every page, deck and post consistent.",
           "from", "$1,900", "per project", ["2 to 3 weeks"],
           ["Brand direction options", "Logo and wordmark", "Colour and type system", "Brand guidelines", "Social and deck templates"],
           "Get a quote", "contact.html?need=Brand%20identity")
      + plan("One-time project", "Website migration", "Move from WordPress to Webflow or Framer, or the other way round, without losing rankings or content.",
           "from", "$1,500", "per project", ["1 to 3 weeks"],
           ["Content and SEO audit", "CMS rebuild and import", "301 redirect map", "Meta and schema kept", "Launch checks"],
           "Get a quote", "contact.html?need=Migration")
      + '        </div>\n'
      + f'''        <div class="pnote" data-reveal><span><b>Not sure where to start?</b> A UX audit of your site or product: ranked issues, annotated screens and one redesigned section, in 3 to 5 days. <b>$390</b>, credited if you continue with us.</span>{btn_ghost("contact.html?need=UX%20audit", "Book an audit", lg=False)}</div>
''')
    subs = (
      plan("Monthly plan", "Design + Development", "Your senior design and build team on tap. Two requests in progress at a time, one in design and one in build, with an unlimited backlog.",
           "", "$3,900", "/ month", ["2 active requests", "Updates every 24 to 48h", "Pause or cancel anytime"],
           ["Website and landing pages", "Product UI and design systems", "Webflow, Framer, WordPress builds", "Front-end development", "Brand assets and decks", "Shared board with every request", "Weekly written report", "Senior designer and developer"],
           "Start a plan", "contact.html?need=Monthly%20plan", "Billed monthly. No long contract.", hero=True, badge="Best value")
      + '        <div class="plans-duo">\n'
      + plan("Monthly plan", "Design", "Ongoing design for product, website and brand. One request in progress at a time.",
           "", "$2,400", "/ month", ["1 active request", "Pause anytime"],
           ["Product and website design", "Design systems in Figma", "Marketing and launch assets", "Updates every 24 to 48h", "Weekly written report"],
           "Start a plan", "contact.html?need=Monthly%20plan")
      + plan("Monthly plan", "Development", "Ongoing builds, fixes and new pages on Webflow, Framer or WordPress. One request at a time.",
           "", "$2,400", "/ month", ["1 active request", "Pause anytime"],
           ["New pages and sections", "CMS setup and changes", "Speed and SEO fixes", "Integrations and forms", "Weekly written report"],
           "Start a plan", "contact.html?need=Monthly%20plan")
      + '        </div>\n        <div class="plans-duo">\n'
      + plan("Growth add-on", "Conversion optimisation", "Works alone or with any plan. One tested improvement a month on the page that matters most.",
           "from", "$990", "/ month", ["Monthly test"],
           ["Funnel and heatmap review", "One A/B test designed and built", "Written hypotheses and results", "Tracking checks", "Monthly report"],
           "Start CRO", "contact.html?need=CRO")
      + plan("Flexible", "20-hour pack", "For smaller or irregular tasks. Use the hours on any design or development work within a month.",
           "", "$1,100", "for 20 hours", ["Valid 1 month"],
           ["Any design or build task", "Senior people only", "Visible hours log", "Buy again anytime", "No commitment"],
           "Buy hours", "contact.html?need=Hours%20pack")
      + '        </div>\n')
    body = hero('<span>Pricing</span>', "Pricing", ["Senior work,", 'priced <span class="accent">clearly</span>.'],
                "Pick a fixed-price project or a monthly plan. You know the cost before anything starts, and every price below is a starting point we confirm in writing within 24 hours.",
                btn_primary("contact.html", "Get a quote") + btn_ghost("https://t.me/tanasiychuk8", "Ask on Telegram", tg=True), p=p)
    body += f'''
    <section class="sec" data-chapter="Plans" style="padding-top:0;border-top:0">
      <div class="wrap">
        <div style="display:flex;justify-content:center;margin-bottom:40px" data-reveal>
          <div class="ptoggle" role="tablist" aria-label="Pricing type">
            <button class="is-on" role="tab" aria-selected="true" data-p="projects">One-time projects</button>
            <button role="tab" aria-selected="false" data-p="plans">Monthly plans <small>Flexible</small></button>
          </div>
        </div>
        <div class="ppanel" data-panel="projects">
{projects}        </div>
        <div class="ppanel" data-panel="plans" hidden>
{subs}        </div>
      </div>
    </section>

    <section class="sec" data-chapter="Compare">
      <div class="wrap">
{sec_head("Project or plan?", 'Two ways to work, <span class="dim">same senior team.</span>', "Most clients start with a project, then stay on a plan for new pages and improvements.")}
        <div class="vs" data-reveal>
          <div><h3>One-time project</h3><p>Best when you know what you need.</p><ul><li>A new website, landing page, product UI or brand</li><li>Fixed scope and fixed price, agreed upfront</li><li>Paid in two milestones</li><li>Clear start and finish date</li></ul></div>
          <div><h3>Monthly plan</h3><p>Best when the work never really stops.</p><ul><li>A steady flow of pages, features and fixes</li><li>One flat monthly price, no hourly maths</li><li>Unlimited backlog, worked through in order</li><li>Pause or cancel anytime</li></ul></div>
        </div>
      </div>
    </section>

    <section class="sec" data-chapter="Included">
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
      ("Why do projects show a “from” price?", "Because two websites are never the same size. The price on this page is where a typical project starts. Send a brief and you'll get an exact fixed price in writing within 24 hours."),
      ("How do payments work?", "Projects are split into two milestones: the first when we start, the second before launch. Monthly plans are billed at the start of each month."),
      ("What is an active request?", "A single task we are working on right now, like a new page, a feature screen or a set of fixes. When one is done, the next one from your backlog starts."),
      ("Can I pause or cancel a monthly plan?", "Yes. Pause for a month or cancel anytime, with no notice period and no fee."),
      ("What if the scope changes halfway?", "On a project, we write up the change and its price, and you decide. On a monthly plan, it simply goes into the backlog."),
      ("Can we start small?", "Yes. The $390 UX audit or a single landing page are both good ways to see how we work before a bigger project."),
      ("Do you offer discounts?", "Monthly plans already cost less than the same work as separate projects. For non-profits and early-stage teams, ask and we'll see what we can do."),
    ])
    body += cta(p, "Ready when you are", "Get an exact quote <br>in 24 hours.")
    page("pricing.html", "Pricing | Sorvel Studio", "Clear pricing for websites, landing pages, product UI and brand, as fixed-price projects or flexible monthly plans.", "pricing", body, p)

# ======================= PROCESS =======================
def process():
    p = ""
    steps = [
      ("Day 0", "You send a brief", "A few lines through the form, by email or on Telegram. What you're building, what the site should do, any links or deadlines. No call needed.",
       [("Short brief form", "5 min"), ("Links to examples you like", "optional"), ("NDA first, if you need one", "optional")]),
      ("Within 24h", "You get a written plan", "We read everything, look at your current site and competitors, then reply with a clear plan: what we'll make, in what order, how long it takes and the fixed price.",
       [("Scope and page list", ""), ("Timeline with milestones", ""), ("Fixed price, split in two", ""), ("Questions we need answered", "")]),
      ("Days 1 to 3", "Kickoff", "Once you approve, we set up a shared board and folder. You send content and access, we send a short questionnaire about your audience, voice and goals.",
       [("Shared board with every task", ""), ("Brand, content and access checklist", ""), ("Sitemap and messaging draft", "")]),
      ("Weeks 1 to 3", "Design in Figma", "We start with structure and copy, then the look. You review on your own time, leave comments right on the design and see changes within 24 to 48 hours.",
       [("Wireframes and copy structure", ""), ("Desktop and mobile design", ""), ("Interactive prototype", ""), ("Two rounds of revisions per page", "")]),
      ("Weeks 2 to 5", "Build", "The approved design becomes a real site in Webflow, Framer or WordPress, with CMS, animations and forms. You get a private link and watch it come together.",
       [("Pixel-accurate build", ""), ("CMS you can edit yourself", ""), ("Animations and interactions", ""), ("Speed, SEO and accessibility checks", "")]),
      ("Launch +30 days", "Launch and aftercare", "We test on real devices, connect your domain and go live. For 30 days after launch, fixes are on us. After that, you can stay on a monthly plan.",
       [("Cross-device QA", ""), ("Domain, redirects and analytics", ""), ("Video guide to edit your site", ""), ("30 days of free fixes", "")]),
    ]
    st = ""
    for i, (when, h, desc, lis) in enumerate(steps):
        li = "".join(f"<li>{a}{f'<em>{b}</em>' if b else ''}</li>" for a, b in lis)
        st += f'          <div class="step" data-reveal><p class="step__when">{when}</p><div><h3>{h}</h3><p>{desc}</p></div><ul>{li}</ul></div>\n'
    body = hero('<span>Process</span>', "How we work", ["Calm, written,", '<span class="accent">predictable</span>.'],
                "No sales calls and no meetings for the sake of meetings. You send a brief, get a plan in writing and see real progress every few days, all on your own schedule.",
                btn_primary("contact.html", "Send a brief") + btn_ghost("https://t.me/tanasiychuk8", "Write on Telegram", tg=True), p=p, visual=scenes.flow())
    body += f'''
    <section class="sec cs-brief" data-chapter="Why">
      <div class="wrap pg-split">
        <div data-reveal><p class="eyebrow">Why it works this way</p><h2 class="h2">Every decision <span class="dim">on record.</span></h2></div>
        <div class="pg-prose" data-reveal style="--d:.08s">
          <p>Calls feel productive, but half of what's said is forgotten by Friday. Writing things down is slower for an hour and faster for the whole project.</p>
          <p>You review designs when it suits you, not when a meeting is booked. Feedback lands right on the screen it's about. And when someone new joins your team, the full history is already there.</p>
          <p>It also means you never wait for us. Updates arrive every 24 to 48 hours, whether you asked or not.</p>
        </div>
      </div>
    </section>

    <section class="sec" data-chapter="Steps">
      <div class="wrap">
{sec_head("Step by step", 'From brief <span class="dim">to live site.</span>', "A typical website takes 3 to 6 weeks. A landing page, 1 to 2. Here's what happens in between.")}
        <div class="steps">
{st}        </div>
      </div>
    </section>

    <section class="sec" data-chapter="Tools">
      <div class="wrap">
{sec_head("How we stay in touch", 'Simple tools, <span class="dim">no extra logins.</span>')}
        <div class="tools">
          <div data-reveal>{ico("figma")}<h3>Comments right on the design</h3><p>Click any spot in Figma and leave a note. We reply in the same thread, so nothing gets lost in long emails.</p></div>
          <div data-reveal style="--d:.05s">{ico("grid")}<h3>Shared board</h3><p>Every task, its status and what's next, visible anytime.</p></div>
          <div data-reveal style="--d:.1s">{ico("chat")}<h3>Telegram or email</h3><p>Quick questions get quick answers, during your working day.</p></div>
          <div data-reveal style="--d:.15s">{ico("eye")}<h3>Short video walkthroughs</h3><p>For bigger milestones, a 3 minute recorded tour of what changed and why.</p></div>
          <div data-reveal style="--d:.2s">{ico("doc")}<h3>Weekly written report</h3><p>What's done, what's next and anything we need from you.</p></div>
          <div data-reveal style="--d:.25s">{ico("link")}<h3>Live preview link</h3><p>Watch the real site take shape, on any device.</p></div>
          <div data-reveal style="--d:.3s">{ico("key")}<h3>Your accounts</h3><p>Figma, CMS and hosting live in your name from day one.</p></div>
        </div>
      </div>
    </section>

    <section class="sec" data-chapter="Promises">
      <div class="wrap">
{sec_head("Our promises", 'What you can <span class="dim">hold us to.</span>')}
        <div class="vals">
          <div data-reveal>{ico("clock")}<h3>A reply in about 10 minutes</h3><p>On working days, every message gets an answer the same or next day.</p></div>
          <div data-reveal style="--d:.05s">{ico("shield")}<h3>The price doesn't move</h3><p>The fixed price you approved is the price you pay, unless you add scope.</p></div>
          <div data-reveal>{ico("users")}<h3>Senior people only</h3><p>The designer and developer on your project are the ones who do the work.</p></div>
          <div data-reveal style="--d:.05s">{ico("eye")}<h3>Progress you can see</h3><p>Real updates every 24 to 48 hours, never a silent week.</p></div>
          <div data-reveal>{ico("check")}<h3>Done means done</h3><p>Tested on real devices, fast, accessible and ready for search before launch.</p></div>
          <div data-reveal style="--d:.05s">{ico("heart")}<h3>30 days of free fixes</h3><p>If something breaks after launch, we fix it, no questions asked.</p></div>
        </div>
      </div>
    </section>
'''
    body += faq([
      ("Do we ever need a call?", "No. Everything works in writing. If you'd still prefer a quick call at some point, just say so, but most clients never need one."),
      ("How much of my time does it take?", "About an hour at kickoff for content and access, then 15 to 30 minutes per review round. Everything else is on us."),
      ("What do you need from me to start?", "A short brief, your logo and brand files if you have them, and any content you already have. We help write or polish the rest."),
      ("How many revisions are included?", "Two rounds per page in design, plus fixes during the build. In practice most pages are approved after the first round."),
      ("What happens after the 30 days?", "You can edit the site yourself in the CMS, order small tasks as needed, or stay on a monthly plan for ongoing work."),
    ])
    body += cta(p, "Start with a brief", "A few lines <br>is all it takes.")
    page("process.html", "Process | Sorvel Studio", "How Sorvel works: a written brief, a plan in 24 hours, design in Figma, build, launch and 30 days of free fixes. No calls needed.", "process", body, p)

# ======================= CONTACT =======================
def plans_json():
    import json, pricing as P
    NEED = {"website":"Website","landing":"Landing page","product":"Product design","brand":"Brand identity","migration":"Migration","audit":"UX audit",
            "plan-full":"Monthly plan","plan-design":"Monthly plan","plan-dev":"Monthly plan","cro":"Monthly plan","hours":""}
    out = {}
    def add(o, group):
        unit = o.get("bunit") or o["unit"]
        price = ("from " if o["frm"] else "") + o["price"] + (" / " + unit if unit and unit != "one time" else "")
        out[o["id"]] = {"name": o["name"].replace("&amp;", "&"), "group": group, "price": price, "need": NEED.get(o["id"], ""), "monthly": o["unit"] == "mo"}
    for o in P.PROJECTS: add(o, "One-time project")
    for g, items in P.PLANS:
        for o in items: add(o, "Monthly plan" if g in ("Build", "Grow") else "Hours pack")
    return '<script type="application/json" id="plans-data">' + json.dumps(out) + '</script>\n'

def contact():
    p = ""
    body = hero('<span>Contact</span>', "Start a project", ["Tell us what", "you're <span class=\"accent\">building</span>."],
                "A few lines are enough. You'll get a clear plan, timeline and fixed price in writing within 24 hours. No sales calls.", "", p=p, visual=scenes.inbox())
    body += f'''
    <section class="sec" style="padding-top:0;border-top:0">
      <div class="wrap contact-grid">
        <aside class="contact-side" data-reveal>
          <a class="cbox cbox--glow" href="mailto:hello@sorvel.agency?subject=New%20project"><small>Email</small><b>hello@sorvel.agency <span>→</span></b><p>Best for longer briefs and attachments.</p></a>
          <a class="cbox" href="https://t.me/tanasiychuk8" target="_blank" rel="noopener"><small>Telegram</small><b>@tanasiychuk8 <span>→</span></b><p>Best for quick questions.</p></a>
          <div class="cbox"><small>Our time</small><b><span class="clock" style="color:var(--text);font-weight:600">--:--</span> CET</b><p>We usually reply within 10 minutes during working hours.</p></div>
          <div class="cbox">
            <small>What happens next</small>
            <ol class="next-steps" style="margin-top:14px">
              <li><b>Today</b><span>We read your brief and look at your current site.</span></li>
              <li><b>Within 24h</b><span>You get a written plan, timeline and fixed price.</span></li>
              <li><b>Days 1 to 3</b><span>Approve it and we start.</span></li>
            </ol>
          </div>
        </aside>

        <form class="brief brief--page" id="brief" data-reveal style="--d:.1s" novalidate>
          <input type="hidden" name="plan" value="">
          {plans_json()}          <div class="picked" hidden>
            <span class="picked__ic" aria-hidden="true"></span>
            <div class="picked__txt"><small>You picked</small><b class="picked__name"></b><span class="picked__price"></span></div>
            <a class="picked__change" href="pricing.html">Change</a>
            <button class="picked__x" type="button" aria-label="Remove selected option">×</button>
          </div>
          <div class="brief__row">
            <label class="field"><span>Your name</span><input name="name" autocomplete="name" required placeholder="Jane Cooper"></label>
            <label class="field"><span>Work email</span><input name="email" type="email" autocomplete="email" required placeholder="jane@company.com"></label>
          </div>
          <label class="field"><span>Company or website <em>optional</em></span><input name="company" autocomplete="url" placeholder="company.com"></label>

          <fieldset class="choose">
            <legend>What do you need?</legend>
            <label><input type="checkbox" name="need" value="Website"><span>Website</span></label>
            <label><input type="checkbox" name="need" value="Landing page"><span>Landing page</span></label>
            <label><input type="checkbox" name="need" value="Product design"><span>Product design</span></label>
            <label><input type="checkbox" name="need" value="Brand identity"><span>Brand identity</span></label>
            <label><input type="checkbox" name="need" value="Migration"><span>Migration</span></label>
            <label><input type="checkbox" name="need" value="Monthly plan"><span>Monthly plan</span></label>
            <label><input type="checkbox" name="need" value="UX audit"><span>UX audit</span></label>
          </fieldset>

          <div class="brief__row">
            <label class="field"><span>Platform <em>optional</em></span><select name="platform"><option value="">Not sure yet</option><option>Webflow</option><option>Framer</option><option>WordPress</option><option>Figma only</option></select></label>
            <label class="field"><span>Budget <em>optional</em></span><select name="budget"><option value="">Prefer not to say</option><option>Under $3,000</option><option>$3,000 to $6,000</option><option>$6,000 to $12,000</option><option>$12,000+</option><option>Monthly plan</option></select></label>
          </div>

          <fieldset class="choose choose--one">
            <legend>When do you want to start?</legend>
            <label><input type="radio" name="timeline" value="As soon as possible"><span>As soon as possible</span></label>
            <label><input type="radio" name="timeline" value="Within a month"><span>Within a month</span></label>
            <label><input type="radio" name="timeline" value="Just exploring"><span>Just exploring</span></label>
          </fieldset>

          <label class="field"><span>About the project</span><textarea name="details" rows="5" required placeholder="What are you building, what should the site or product do, any links or deadlines."></textarea></label>
          <input type="text" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">

          <div class="brief__foot">
            <button class="btn btn--primary btn--lg" type="submit">
              <span class="btn__roll"><span data-text="Send brief">Send brief</span></span>
              <span class="btn__arrow" aria-hidden="true">{ARROW}{ARROW}</span>
            </button>
            <p class="brief__note">Reply in about 10 minutes. No sales calls.</p>
          </div>
          <p class="brief__msg" role="status" aria-live="polite"></p>

          <div class="brief__done" hidden>
            <span class="brief__check" aria-hidden="true"></span>
            <h3>Brief received.</h3>
            <p>Thanks! You'll get a written plan and quote within 24 hours. Keep an eye on your inbox.</p>
          </div>
        </form>
      </div>
    </section>
'''
    body += faq([
      ("Do I need a detailed brief?", "No. A few lines about what you're building and a link to your current site is enough. We'll ask for anything else we need."),
      ("Can you sign an NDA first?", "Yes. Send yours or ask for ours and we'll sign it before you share details."),
      ("Will you try to sell me on a call?", "No. You'll get everything in writing, and you can decide in your own time."),
      ("What if I only have a rough idea?", "That's fine. Tell us the goal and we'll suggest the simplest way to get there, with a price for each option."),
    ], title="Before you write")
    page("contact.html", "Start a project | Sorvel Studio", "Send a short brief and get a written plan, timeline and fixed price within 24 hours. Email, Telegram or the form. No sales calls.", "contact", body, p)

if __name__ == "__main__":
    work(); process(); contact()
    import pricing as _p; _p.pricing()
