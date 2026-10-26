import sys; sys.path.insert(0, "SOURCE_DIR/site")
from common import *
import scenes

# Niche landing pages for search. They live next to the service pages (services/<slug>.html)
# but are not in the main menu; the footer "Popular" row and related pages link to them.
SOL = [
  ("saas-website-design", "SaaS website design"),
  ("fintech-website-design", "Fintech website design"),
  ("webflow-agency", "Webflow agency"),
  ("wordpress-to-webflow-migration", "WordPress to Webflow"),
]

D = {
"saas-website-design": dict(
  title="SaaS Website Design Agency | Webflow and Framer | Sorvel",
  desc="SaaS website design and development: clear messaging, real product visuals and a Webflow or Framer build your marketing team can edit. Fixed quote in 24 hours.",
  eyebrow="SaaS website design", visual="product-design", need="website",
  lines=["SaaS websites", "that make the", 'product <span class="accent">obvious</span>.'],
  lead="Your site has a few seconds to explain what the product does, who it is for and why it beats what they use today. We design the story, the product visuals and the pages around demos and sign-ups, then build it in Webflow or Framer so your team ships changes without a developer.",
  who=[("The product outgrew the site", "You have shipped a lot since launch. The homepage still describes version one, and sales explains the rest on calls."),
       ("Visitors don't get it", "Abstract headlines and stock illustrations leave people guessing. They leave before they see what the product actually does."),
       ("Marketing waits on engineering", "Every new landing page or pricing change sits in the dev backlog behind product work.")],
  incl=[("pen", "Positioning and messaging", "What you do, for whom, and the proof, in the order a buyer needs it."),
        ("layout", "Product visuals", "Clean UI shots and simplified product scenes instead of generic illustrations."),
        ("target", "Pages that convert", "Home, product, pricing, integrations, use cases and a demo or sign-up path."),
        ("code", "Webflow or Framer build", "A native, fast build with components your team reuses for new pages."),
        ("grid", "CMS for growth", "Blog, changelog, customers and integrations set up as collections."),
        ("search", "SEO and tracking", "Technical SEO, schema, and events on every demo and sign-up button.")],
  phases=[("Week 1", "Story and structure", "What the site must say, and to whom.", ["Positioning", "Sitemap", "Wireframes"]),
          ("Weeks 1 to 3", "Design", "Desktop and mobile in Figma.", ["Home page first", "Product visuals", "Inner pages"]),
          ("Weeks 2 to 5", "Build", "Webflow or Framer, with CMS.", ["Components", "CMS collections", "Forms and events"]),
          ("Launch", "QA and handover", "Live, tested and documented.", ["Cross-device QA", "Redirects", "Video guide"])],
  plat=[("Seed to Series B", "A first proper site, or the redesign after a raise."), ("Product-led growth", "Sign-up flows, pricing pages and a clean handoff to onboarding."),
        ("Sales-led", "Demo booking, use cases and proof for each type of buyer."), ("Dev tools and infrastructure", "Technical audiences who want specs and benchmarks, not fluff.")],
  cases=["serverscamp", "valhalla-capital", "ci-isac"],
  faq=[("Webflow or Framer for a SaaS site?", "Webflow if marketing publishes a lot (blog, changelog, many landing pages) and needs a strong CMS. Framer if you want a fast, motion-rich site with fewer content types. We recommend one in the written plan."),
       ("Can you show our product if the UI keeps changing?", "Yes. We build simplified product scenes from your real interface, so they stay accurate longer and are quick to update when features change."),
       ("Do you write the copy?", "We shape the structure and messaging of every page and polish your text. Full copywriting from scratch can be added to the scope."),
       ("Can you design the product itself too?", 'Yes. We also design SaaS dashboards and web apps, so the site and the product feel like one company. See <a href="product-design.html">product design</a>.'),
       ("How long does a SaaS website take?", "Usually 3 to 6 weeks for 5 to 10 pages, depending on content and feedback speed.")],
  related=["websites", "product-design", "landing-pages"]),

"fintech-website-design": dict(
  title="Fintech Website Design | Trust-first Webflow sites | Sorvel",
  desc="Website design for fintech, investment and financial services firms: clear products, visible trust signals and gated flows, designed in Figma and built in Webflow.",
  eyebrow="Fintech website design", visual="websites", need="website",
  lines=["Fintech websites", 'people <span class="accent">trust</span> with money.'],
  lead="Money products live or die on trust. We design fintech and financial services sites that explain complex products in plain words, show the proof early and handle the gated or regulated parts properly, from investor eligibility to risk disclosures.",
  who=[("It looks less serious than you are", "A template site makes a regulated, well-funded business look like a side project. Investors and partners notice."),
       ("The product is hard to explain", "Fees, eligibility, risk and returns end up in long paragraphs that nobody reads."),
       ("Compliance slows every change", "Disclosures, jurisdictions and gated content make each edit risky, so the site never improves.")],
  incl=[("shield", "Trust-first design", "Calm typography, real data and visible credentials instead of stock photos of handshakes."),
        ("layout", "Complex products made simple", "Tables, calculators and step-by-step explainers for fees, returns and eligibility."),
        ("key", "Gated and qualified flows", "Investor eligibility checks, gated data rooms and request-access forms."),
        ("doc", "Disclosures in the right place", "Risk and legal text where it is needed, readable and easy for compliance to update."),
        ("code", "Webflow build", "A fast build with no plugins to patch, and a CMS for news, insights and fund updates."),
        ("search", "SEO and speed", "Clean structure and schema so you rank for what you actually offer.")],
  phases=[("Week 1", "Products and rules", "What you offer and what must be said.", ["Audience and products", "Compliance notes", "Sitemap"]),
          ("Weeks 1 to 3", "Design", "Desktop and mobile in Figma.", ["Home page first", "Product pages", "Gated flows"]),
          ("Weeks 3 to 5", "Build", "Native Webflow with CMS.", ["Forms and checks", "Disclosures", "Analytics"]),
          ("Launch", "Review and go live", "Signed off by your team.", ["Compliance review", "Cross-device QA", "Video guide"])],
  plat=[("Investment and private credit", "Fund sites, investor eligibility and gated data rooms."), ("Payments and banking", "Product pages, pricing and onboarding for business or consumer finance."),
        ("Wealth and advisory", "Credibility first, with clear services and a simple way to get in touch."), ("Proptech and lending", "Calculators, income estimates and lead capture for property finance.")],
  cases=["valhalla-capital", "arlowe-baxter"],
  faq=[("Can you build an investor eligibility check?", "Yes. For Valhalla Capital we built a three-step check that routes qualified investors to a request-access form, using native Webflow forms and no paid third-party tools."),
       ("Do you handle compliance?", "We design and place disclosures, consents and gated content to your counsel's requirements. Your legal team approves the wording; we make it readable and easy to update."),
       ("Is Webflow secure enough for a financial company?", "For a marketing site, yes: managed hosting, SSL, no plugins to patch and role-based editor access. Client data and transactions stay in your own systems."),
       ("Can you show numbers without exposing real data?", "Yes. We design charts and calculators that use illustrative or approved figures and are easy to update."),
       ("How long does a fintech website take?", "Usually 4 to 6 weeks for 5 to 8 pages, plus time for your compliance review.")],
  related=["websites", "brand-identity", "landing-pages"]),

"webflow-agency": dict(
  title="Webflow Agency | Webflow design and development | Sorvel",
  desc="Webflow design and development for SaaS, fintech and B2B: custom Figma design, clean Webflow builds, a CMS your team can edit and technical SEO. Fixed quote in 24 hours.",
  eyebrow="Webflow agency", visual="landing-pages", need="website",
  lines=["Webflow sites,", 'designed and built <span class="accent">properly</span>.'],
  lead="Custom design in Figma, then a clean native Webflow build: a tidy class system, CMS collections that make sense and interactions that stay fast. Your marketing team gets a site they can edit on day one without breaking the layout.",
  who=[("Your Webflow site is hard to edit", "Classes named div-block-37, nested combos and one-off styles mean every change risks breaking something."),
       ("You outgrew your template", "It got you live, but it looks like hundreds of other sites and no longer fits your story."),
       ("You're moving to Webflow", "From WordPress, Squarespace or custom code, and you don't want to lose rankings on the way.")],
  incl=[("figma", "Custom Figma design", "Desktop, tablet and mobile, designed for your content, not a template."),
        ("grid", "Clean class system", "A tidy, documented structure so new pages are quick and safe to build."),
        ("move", "CMS collections", "Blog, case studies, team, careers and resources, modelled around how you publish."),
        ("bolt", "Interactions", "Scroll and hover motion with Webflow interactions, light enough to keep the site fast."),
        ("search", "Technical SEO", "Meta, schema, sitemap, redirects and Core Web Vitals checked before launch."),
        ("check", "Handover", "A video walkthrough and editor access your team can use without us.")],
  phases=[("Week 1", "Structure", "Pages, content and CMS model.", ["Sitemap", "CMS model", "Wireframes"]),
          ("Weeks 1 to 3", "Design", "Custom design in Figma.", ["Home page first", "Inner pages", "Mobile"]),
          ("Weeks 2 to 5", "Webflow build", "Native and pixel-accurate.", ["Class system", "CMS and forms", "Interactions"]),
          ("Launch", "QA and handover", "Live, tested and yours.", ["Cross-device QA", "Domain and redirects", "Video guide"])],
  plat=[("New Webflow site", "Designed and built from scratch."), ("Redesign in Webflow", "Keep your CMS content, replace the design."),
        ("Migration to Webflow", "From WordPress or another platform, with every URL redirected."), ("Webflow cleanup", "Untangle classes and CMS on a site that grew messy.")],
  cases=["valhalla-capital", "arlowe-baxter", "ci-isac"],
  faq=[("Do you use templates?", "No. Every site is designed in Figma for your content and built from scratch in Webflow with a clean class system."),
       ("Can you take over an existing Webflow site?", "Yes. We audit the structure first, then clean it up or rebuild the parts that slow your team down."),
       ("Who owns the Webflow site?", "You do. We build in your workspace or transfer the site to you at launch, together with the Figma files."),
       ("Which Webflow plan do we need?", "Usually the CMS site plan for a marketing site with a blog or case studies. We confirm it in the plan based on your pages and traffic."),
       ("How long does a Webflow website take?", "Usually 3 to 6 weeks for 5 to 10 pages, design and build included.")],
  related=["websites", "migrations", "landing-pages"]),

"wordpress-to-webflow-migration": dict(
  title="WordPress to Webflow Migration | Keep your SEO | Sorvel",
  desc="Move your site from WordPress to Webflow without losing rankings: content import, a 301 redirect map, meta and schema kept, and 30 days of Search Console checks.",
  eyebrow="WordPress to Webflow migration", visual="migrations", need="migration",
  lines=["Leave WordPress.", 'Keep your <span class="accent">rankings</span>.'],
  lead="We move your pages, posts and media from WordPress to Webflow, map every old URL to its new home and keep your titles, descriptions and structured data. Then we watch Search Console for 30 days so nothing slips.",
  who=[("Plugin updates break things", "Every update is a gamble, and security patches eat time your team doesn't have."),
       ("Marketing can't edit without help", "Page builders and custom themes make simple edits slow and risky."),
       ("The site is slow", "Heavy themes and plugins drag down Core Web Vitals and conversions.")],
  incl=[("doc", "Content audit", "Every page, post and template listed, with the ones that bring traffic marked."),
        ("move", "Content import", "Posts, images, authors and categories moved as CMS items, not copy-pasted."),
        ("key", "Redirect map", "Every old URL sent to the right new one with 301 redirects."),
        ("search", "Meta and schema", "Titles, descriptions and structured data kept or improved."),
        ("figma", "Optional redesign", "Move and refresh the design in one project, or keep today's look."),
        ("check", "Launch checks", "Broken links, speed and indexing checked before and after launch.")],
  phases=[("Week 1", "Audit", "Know exactly what you have.", ["Page inventory", "Top keywords", "Redirect plan"]),
          ("Weeks 1 to 2", "Rebuild", "Webflow, same content.", ["CMS structure", "Templates", "Content import"]),
          ("Weeks 2 to 3", "Check", "Nothing left behind.", ["Redirects tested", "Meta compared", "Speed tested"]),
          ("Launch + 30 days", "Watch", "Make sure rankings hold.", ["Search Console", "Fix 404s", "Report"])],
  plat=[("Blogs and content sites", "Hundreds or thousands of posts imported automatically."), ("Company sites", "Pages rebuilt cleanly, forms and integrations reconnected."),
        ("WooCommerce shops", "We'll tell you honestly whether Webflow or Shopify fits better."), ("Redesign and move", "A new design and a new platform in one project.")],
  cases=["ci-isac", "arlowe-baxter"],
  faq=[("Will we lose our Google rankings?", "Not if it's done properly. We map every old URL to a new one, keep your meta and structure, and watch Search Console for 30 days after launch."),
       ("How many posts can you move?", "From a 10 page site to thousands of posts. Larger content sets are imported automatically, not by hand."),
       ("Will the site be down during the move?", "No. We build in Webflow in parallel and switch the domain only when everything is checked."),
       ("What happens to forms and integrations?", "We list them all in the audit and reconnect each one in Webflow, or suggest a simpler option where a plugin did the job."),
       ("How much does a migration cost?", "From $2,900 for a typical company site. Big blogs or a redesign on top are quoted after the audit, in writing, within 24 hours.")],
  related=["migrations", "websites", "webflow-agency"]),
}

PRICE = {"website": ("$6,900", "3 to 6 weeks for a typical 5 to 10 page site"), "migration": ("$2,900", "1 to 3 weeks, depending on pages and CMS items")}
SVC_NAME = {s: t for s, t, d, ic in SERVICES}
SOL_NAME = dict(SOL)

def solution(slug):
    d = D[slug]; p = "../"
    nm = SOL_NAME[slug]
    probs = "\n".join(f'          <article data-reveal style="--d:{i*.06:.2f}s"><h3>{t}</h3><p>{x}</p></article>' for i, (t, x) in enumerate(d["who"]))
    incl = "\n".join(f'          <div data-reveal style="--d:{(i%3)*.05:.2f}s">{ico(ic)}<h3>{t}</h3><p>{x}</p></div>' for i, (ic, t, x) in enumerate(d["incl"]))
    ph = ""
    for i, (when, h, x, lis) in enumerate(d["phases"]):
        li = "".join(f"<li>{a}</li>" for a in lis)
        ph += f'          <div class="cs-phase" style="--i:{i}"><p class="cs-phase__when">{when}</p><h3>{h}</h3><p>{x}</p><ul>{li}</ul></div>\n'
    plat = "\n".join(f'          <div data-reveal style="--d:{i*.05:.2f}s"><b>{a}</b><span>{b}</span></div>' for i, (a, b) in enumerate(d["plat"]))
    cs = [c for c in d["cases"] if c not in HIDDEN] or ["ci-isac", "vibz"]; cards = "\n".join(pcard(c, p, wide=(len(cs) % 2 == 1 and i == 0)) for i, c in enumerate(cs))
    rel = [(s, SVC_NAME.get(s) or SOL_NAME.get(s)) for s in d["related"]] + [(s, t) for s, t in SOL if s != slug and s not in d["related"]]
    other = "".join(f'<a class="cs-more__row" href="{s}.html" data-reveal style="--d:{i*.05:.2f}s"><span class="cs-more__name">{t.replace("&","&amp;")}</span><span class="cs-more__go" aria-hidden="true">{DIAG}</span></a>'
                    for i, (s, t) in enumerate(rel[:5]))
    price, note = PRICE[d["need"]]
    quote = f"../contact.html?plan={d['need']}#brief"
    body = hero(f'<a href="../index.html#services">Services</a><span>/</span><span>{nm}</span>', d["eyebrow"], d["lines"], d["lead"],
                btn_primary(quote, "Get a quote") + btn_ghost("../work.html", "See our work"), p=p, visual=scenes.svc(d["visual"]))
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

    <section class="sec" data-chapter="Work">
      <div class="wrap">
{sec_head("Related work", 'Projects <span class="dim">like yours.</span>', "", row=False)}
        <div class="pcards">
{cards}
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

    <section class="sec" data-chapter="Pricing">
      <div class="wrap">
        <div class="sprice" data-reveal>
          <div class="sprice__main">
            <p class="sprice__tag">Pricing</p>
            <h2 class="sprice__title">{nm}</h2>
            <p class="sprice__note">{note}. Exact fixed quote in writing within 24 hours.</p>
          </div>
          <div class="sprice__side">
            <div class="sprice__num"><small>from</small><b>{price}</b><span>fixed price</span></div>
            <div class="sprice__btns">
              {btn_primary(quote, "Get an exact quote", lg=False)}
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
        <header class="cs-more__head" data-reveal><p class="eyebrow">Related</p><a class="cs-more__all" href="../pricing.html">All prices <span aria-hidden="true">→</span></a></header>
        <div class="cs-more__list">{other}</div>
      </div>
    </section>
'''
    body += cta(p)
    page(f"services/{slug}.html", d["title"], d["desc"], "services", body, p)

if __name__ == "__main__":
    for s, _ in SOL: solution(s)
