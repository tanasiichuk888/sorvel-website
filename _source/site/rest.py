import sys, re, html as H; sys.path.insert(0, "SOURCE_DIR/site")
from common import *
from crew import crew, note as crew_note
import scenes

# ---------------- ABOUT ----------------
def about():
    note_html = crew_note("Why no calls", "How we work together", 'Respect for <br>your <span class="accent">calendar.</span>', [
        "Most of our clients run companies. Their days are already full of meetings, and a design project shouldn't add more.",
        "So we work in writing. You get a plan you can forward to your team, updates you can read in two minutes, and a place to leave feedback whenever it suits you. Decisions are recorded, so nothing is &quot;I thought we said&quot;.",
        "It sounds small. In practice it's the reason projects move faster and end with fewer surprises."]).replace('<section class="sec note">', '<section class="sec note" data-chapter="Founder">')
    p = ""
    vals = [("eye", "Taste over trends", "We design what fits your business and your buyers, not what's popular on Dribbble this month."),
            ("doc", "Written, not spoken", "Plans, updates and decisions arrive in writing. You review on your own schedule and nothing gets lost in a call."),
            ("users", "Seniors only", "The people you meet in the plan are the people who design and build. No juniors learning on your budget."),
            ("clock", "A dedicated team per project", "Every project has its own designer and developer from start to finish, so it moves fast and nothing slips."),
            ("check", "Fixed scope, fixed price", "You know what you get and what it costs before we start. No surprise invoices."),
            ("heart", "Built to be handed over", "Clean files, a tidy CMS and a short video guide. You should never feel locked in.")]
    v = "\n".join(f'          <div data-reveal style="--d:{(i%2)*.06:.2f}s">{ico(ic)}<h3>{t}</h3><p>{x}</p></div>' for i, (ic, t, x) in enumerate(vals))
    people = [("Mykola Tanasiichuk", "Founder, Design Lead", True), ("Team member", "Senior Product Designer", False), ("Team member", "Webflow Developer", False),
              ("Team member", "Framer Developer", False), ("Team member", "WordPress Developer", False), ("Team member", "Brand Designer", False)]
    pp = "\n".join(f'          <article class="person{" person--lead" if lead else ""}" data-reveal style="--d:{i*.05:.2f}s"><div class="person__ph">{"<span>MT</span>" if lead else ""}</div><h3>{n}</h3><p>{r}</p></article>' for i, (n, r, lead) in enumerate(people))
    body = hero('<span>About</span>', "About the studio", ["A senior team", 'with <span class="accent">a lot of reps</span>.'],
                "Sorvel is a design and development studio for startups and growing businesses, mostly in SaaS, fintech and AI. We started as one designer taking on projects from around the world, and grew into a team that covers design and build end to end.",
                btn_primary("contact.html", "Start a project") + btn_ghost("work.html", "See our work"), p=p, visual=scenes.globe())
    body += f'''
    <section class="sec" data-chapter="Story">
      <div class="wrap pg-split">
        <div data-reveal>
          <p class="eyebrow">Our story</p>
          <h2 class="h2">From one designer <span class="dim">to a senior team.</span></h2>
        </div>
        <div class="pg-prose" data-reveal>
          <p>It began with Mykola designing websites for clients he never met in person, in time zones he had to look up. Teams from all over the world kept coming back, and kept sending their friends.</p>
          <p>Over the years the projects grew, from single landing pages to full websites, product interfaces and brand systems. To keep up without lowering the bar, we built a team of senior designers and developers who share the same standards.</p>
          <p>Today we design in Figma and build in Webflow, Framer and WordPress. The way we work has stayed the same: a clear plan in writing, fast progress you can see, and a result you're proud to send to customers.</p>
        </div>
      </div>
    </section>

    <section class="sec" data-chapter="Numbers" style="padding-top:0;border-top:0">
      <div class="wrap">
        <div class="tstats" data-reveal style="margin-bottom:0">
          <div><b><span data-count="11">0</span>+</b><span>years designing for the web</span></div>
          <div><b><span data-count="600">0</span>+</b><span>projects shipped</span></div>
          <div><b><span data-count="24">0</span>h</b><span>to a written plan and quote</span></div>
        </div>
      </div>
    </section>

    <section class="sec" data-chapter="Belief">
      <div class="wrap">
        <p class="eyebrow" data-reveal>What we believe</p>
        <blockquote class="big-quote" data-reveal>Anyone can make a page look busy. <span class="dim">The work is deciding what to leave out.</span></blockquote>
      </div>
    </section>

    <section class="sec" data-chapter="Values">
      <div class="wrap">
{sec_head("How we work", 'Six things we <span class="dim">don\'t compromise on.</span>')}
        <div class="vals">
{v}
        </div>
      </div>
    </section>

    <section class="sec" data-chapter="Team">
      <div class="wrap">
{sec_head("The team", 'People who <span class="dim">do the work.</span>', "No account managers in the middle. You talk to the designers and developers who build your project.")}
{crew()}
      </div>
    </section>

{note_html}
'''
    body += cta(p)
    page("about.html", "About | Sorvel Studio", "Sorvel is a senior design and development studio for startups and growing businesses, mostly in SaaS, fintech and AI. 11 years, 600+ projects.", "about", body, p)

# ---------------- REVIEWS ----------------
def reviews():
    import json
    p = ""
    src = open(ROOT + "js/main.js").read()
    data = json.loads(src[src.index("/*REVIEWS*/") + 11:src.index("/*/REVIEWS*/")])
    def nm(r):
        if r.get("n"):
            return r["n"]
        c = r.get("c", "")
        return "Client from " + ("the " if c.startswith(("United", "Netherlands")) else "") + c
    cards = []
    items = data
    for r in data:
        sub = " · ".join(x for x in [r.get("role", ""), r.get("c", "") if r.get("n") else "", r.get("d", "")] if x)
        tags = (f'<span class="rcard__src rcard__src--ok">✓ {r["src"]}</span>' if r.get("src") else "") + ('<span class="rcard__src">Repeat client</span>' if r.get("rep") else "")
        tr = f'<small class="rcard__tr">Translated from {r["tr"]}</small>' if r.get("tr") else ""
        cards.append(f'''          <figure class="rcard" data-reveal><div class="rcard__top"><span class="rcard__ava">{H.escape(r["ini"])}</span><span class="rcard__who"><b>{H.escape(nm(r))}</b><span>{H.escape(sub)}</span></span><span class="rcard__tags">{tags}</span></div><div class="rcard__stars" aria-label="5 out of 5"><i></i><i></i><i></i><i></i><i></i></div><p>{H.escape(r["t"], quote=False)}</p>{tr}</figure>''')
    reps = len({nm(r) for r in data if r.get("rep") and r.get("n")}) or sum(1 for r in data if r.get("rep"))
    body = hero('<span>Reviews</span>', "Client reviews", ["What it's like", 'to <span class="accent">work with us</span>.'],
                "Real reviews from Upwork and Fiverr Pro projects, quoted word for word under the name each client uses on the platform. A selection from more than 600 five-star reviews.",
                btn_primary("contact.html", "Start a project") + btn_ghost("work.html", "See the work"), p=p, visual=scenes.rate([("Our agency has hired him for 20+ different projects… We continue to work with Mykola on a monthly basis.","Mark R. · Agency owner · Upwork"),("The biggest reason I would recommend working with Mykola, is that the design process with him feels just right.","Andrei B. · Owner · Upwork"),("He even recorded personalized video tutorials so we could manage our site ourselves — that was a game-changer!","alexandrzakiyan · United States · Fiverr Pro"),("I worked with great designers before, and highly recommend Mykola.","theborodin · United States · Fiverr Pro")]))
    body += f'''
    <section class="sec" data-chapter="Score" style="padding-top:0;border-top:0">
      <div class="wrap">
        <div class="rbig" data-reveal>
          <div class="rbig__score"><b>5.0</b><div class="score__stars" aria-label="5 out of 5"><i></i><i></i><i></i><i></i><i></i></div></div>
          <div class="rbig__stats">
            <div><b>600+</b><span>five-star client reviews</span></div>
            <div><b>100%</b><span>Job Success on Upwork</span></div>
            <div><b><span data-count="600">0</span>+</b><span>projects shipped</span></div>
          </div>
        </div>
      </div>
    </section>

    <section class="sec" data-chapter="Reviews">
      <div class="wrap">
{sec_head("In their words", 'Fast, clear, <span class="dim">and on point.</span>', "The same three things come up again and again: quick replies, few revision rounds and a result that matches what they had in mind.")}
        <div class="rgrid" data-cols>
{chr(10).join(cards)}
        </div>
      </div>
    </section>

    <section class="sec" data-chapter="Work">
      <div class="wrap">
{sec_head("Behind the reviews", 'See the projects <span class="dim">in detail.</span>', "", row=False)}
        <div class="pcards">
{pcard("valhalla-capital", p)}
{pcard("ci-isac", p)}
        </div>
      </div>
    </section>
'''
    body += cta(p, title="Let's make you <br>the next review.")
    page("reviews.html", "Reviews | Sorvel Studio", "Real client reviews for Sorvel Studio, quoted word for word. 5.0 from clients all over the world.", "reviews", body, p)

# ---------------- LEGAL ----------------
def legal(path, title, eyebrow, lines, lead, sections, desc):
    p = ""
    toc = "".join(f'<a href="#{sid}">{h}</a>' for sid, h, _ in sections)
    secs = "\n".join(f'          <h2 id="{sid}">{h}</h2>\n          {b}' for sid, h, b in sections)
    body = hero(f'<span>{eyebrow}</span>', eyebrow, lines, lead, p=p)
    body += f'''
    <section class="sec" style="padding-top:0;border-top:0">
      <div class="wrap legal">
        <nav class="legal__toc" aria-label="On this page">{toc}</nav>
        <div class="legal__body">
          <p class="legal__meta">Last updated: 23 October 2026. Questions? Write to <a href="mailto:hello@sorvel.agency">hello@sorvel.agency</a>.</p>
{secs}
        </div>
      </div>
    </section>
'''
    page(path, title, desc, "", body, p, dock=False)

PRIVACY = [
  ("summary", "In short", "<p>We collect only what you send us, use it only to reply and run your project, and never sell it. This website uses no tracking or advertising cookies; we only keep anonymous statistics about how the site is used.</p>"),
  ("who", "Who we are", "<p>This website and the Sorvel Studio brand are run by Mykola Tanasiichuk, a sole proprietor (FOP) registered in Ukraine, who is responsible for the personal data described in this policy. For anything about your data, write to <a href=\"mailto:hello@sorvel.agency\">hello@sorvel.agency</a>.</p>"),
  ("collect", "What we collect", "<p>When you fill in the project form or write to us, we receive what you choose to share:</p><ul><li>your name and email address;</li><li>your company name, if given;</li><li>details about your project, timeline, platform and budget;</li><li>anything else you write in your message or attach.</li></ul><p>When you message us on Telegram, we also see your Telegram name and username.</p>"),
  ("use", "How we use it", "<p>We use your information to reply to your enquiry, prepare a plan and quote, and run the project if we work together. We may keep your contact details to send project-related messages. We do not send newsletters or marketing emails unless you ask for them.</p>"),
  ("basis", "Why we're allowed to use it", "<p>We use what you send us to answer your enquiry and to prepare or carry out a project with you. The anonymous site statistics rely on our legitimate interest in understanding which pages are useful and keeping the site working well; they can't be used to identify you.</p>"),
  ("share", "Who we share it with", "<p>We never sell or rent your information. We share it only with services we need to run the studio, such as Cloudflare, which hosts this website, Web3Forms, which delivers the briefs sent through our form, our email provider, and the design and hosting tools used for your project. Each one handles data under its own privacy terms. Some of these providers are based outside the EU, for example in the United States; where that happens, the transfer is covered by the safeguards they offer, such as the EU-US Data Privacy Framework or the European Commission's standard contractual clauses.</p><p>We may also disclose information if required by law.</p>"),
  ("cookies", "Cookies and analytics", "<p>This website doesn't set tracking or advertising cookies, and all fonts and files are served from our own domain, so your browser doesn't contact third-party font or ad services. We count visits with Cloudflare Web Analytics, which works without cookies and doesn't track you across other websites. We also keep simple, anonymous statistics of our own, without cookies: which pages are viewed and in what order, how far down a page people scroll, how long a page stays open, which links and buttons are clicked, and whether the project form was started or sent. Each visit gets a random number that lives only in your browser tab and is deleted when you close it; we store it with the page, the website you came from and your country, never your name, email, IP address or anything that identifies you. This tells us which pages help people and which ones lose them.</p>"),
  ("keep", "How long we keep it", "<p>We keep enquiries that don't turn into projects for up to 12 months. Project correspondence and files are kept for as long as needed to support you and meet legal and accounting obligations, then deleted. Anonymous site statistics are deleted automatically after 13 months.</p>"),
  ("rights", "Your rights", "<p>You can ask us at any time to see the information we hold about you, correct it, or delete it. You can also object to how we use it. Write to <a href=\"mailto:hello@sorvel.agency\">hello@sorvel.agency</a> and we'll reply within 30 days. If you're in the EU or UK, you also have the right to complain to your local data protection authority.</p>"),
  ("security", "Security", "<p>We use reputable providers, keep access to client data limited to the people working on your project, and use strong passwords and two-factor authentication on our accounts. No method of sending data over the internet is completely secure, so please don't send passwords or payment details through the form.</p>"),
  ("changes", "Changes to this policy", "<p>If we change this policy, we'll update the date at the top of this page. Significant changes will be highlighted here.</p>"),
]
TERMS = [
  ("about", "About these terms", "<p>These terms cover the use of this website and the design and development services provided by Sorvel Studio (\"we\", \"us\"). Each project also has its own written proposal. If the proposal and these terms differ, the proposal wins.</p>"),
  ("site", "Using this website", "<p>You may browse this website and share links to it. You may not copy its design, text or images for your own use without our permission. Project images and case studies are shown with our clients' permission and remain the property of their owners.</p>"),
  ("projects", "Proposals and scope", "<p>Before a project starts, we send a written proposal with the scope, timeline, price and number of revision rounds. Work starts once you accept it in writing and the first payment is received. Anything outside the agreed scope is quoted separately before we do it.</p>"),
  ("payment", "Payment", "<p>Fixed-price projects are usually paid in two milestones: 50% to start and 50% before launch or handover. Monthly plans are paid in advance each month. Prices are in US dollars and exclude any taxes or fees charged by your bank or payment provider. Paid plan months and completed milestones are non-refundable.</p>"),
  ("feedback", "Feedback and timelines", "<p>Timelines assume feedback within two business days of each delivery. Delays in feedback or content may move the launch date. If a project is paused for more than 30 days, we may need to reschedule it around other work.</p>"),
  ("ownership", "Ownership", "<p>Once the project is paid in full, you own the final designs, code and files we create for you. We keep the right to show the work in our portfolio, unless you ask us not to in writing. Third-party fonts, plugins, stock images and platforms remain under their own licences.</p>"),
  ("plans", "Monthly plans", "<p>Plans renew each month until cancelled. You can pause or cancel at any time with notice before the next billing date. Unused time does not roll over unless agreed in writing.</p>"),
  ("liability", "Liability", "<p>We work carefully and test before launch, but we can't guarantee that a website will be free of all errors or that it will achieve specific business results. Our total liability for any project is limited to the amount you paid for it. We are not responsible for issues caused by hosting providers, platforms or third-party services.</p>"),
  ("changes", "Changes and contact", "<p>We may update these terms from time to time. The version in force when you accept a proposal applies to that project. Questions? Write to <a href=\"mailto:hello@sorvel.agency\">hello@sorvel.agency</a>.</p>"),
]

def notfound():
    p = ""
    links = "".join(f'<a href="{h}">{t}</a>' for h, t in [("work.html", "Our work"), ("services/websites.html", "Websites"), ("pricing.html", "Pricing"), ("contact.html", "Contact")])
    body = f'''    <section class="nf">
      <canvas class="hero__dots" aria-hidden="true"></canvas>
      <div class="wrap">
        <div class="nf__code" data-intro>4<span>0</span>4</div>
        <h1 data-intro style="--d:.1s">This page took a different route.</h1>
        <p data-intro style="--d:.2s">The link may be old or mistyped. Here are a few places worth going instead.</p>
        <div class="nf__links" data-intro style="--d:.3s">{btn_primary("index.html", "Back to home")}{btn_ghost("contact.html", "Start a project")}</div>
        <div class="nf__more" data-intro style="--d:.4s">{links}</div>
      </div>
    </section>
'''
    page("404.html", "Page not found | Sorvel Studio", "This page doesn't exist.", "", body, p, dock=False)

if __name__ == "__main__":
    about(); reviews(); notfound()
    legal("privacy.html", "Privacy policy | Sorvel Studio", "Privacy policy", ["Your data,", 'kept <span class="accent">simple</span>.'],
          "What we collect when you contact us, why, and what you can ask us to do with it. Written in plain English.", PRIVACY,
          "How Sorvel Studio collects, uses and protects the information you send us.")
    legal("terms.html", "Terms | Sorvel Studio", "Terms", ["Clear terms,", 'no <span class="accent">fine print</span>.'],
          "How proposals, payments, ownership and timelines work when you hire us. Each project also gets its own written proposal.", TERMS,
          "Terms for using the Sorvel Studio website and hiring us for design and development.")
