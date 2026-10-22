import re, html
W = "WEBSITE_DIR/work/"
src = open(W + "awswrap.html").read()
src = src.replace('<img fetchpriority="low" ', '<img ')  # undo the SEO pass tweak so templates match
src = re.sub(r'<title>AWS Wrap[^<]*</title>', '<title>AWS Wrap case study | Sorvel Studio</title>', src)  # restore the template title
I = "../img/work/ci-isac/"

def shot(img, alt):
    return f'<div class="cs-stage" data-reveal><div class="vwin cs-shot" data-parallax=".03"><div class="win__bar"><i></i><i></i><i></i></div><img src="{I}{img}" alt="{alt}" loading="lazy" width="1600" height="1000"></div></div>'

def row(flip, eb, h, p, img, alt):
    return f'''        <article class="cs-row{" cs-row--flip" if flip else ""}">
          <div class="cs-row__text" data-reveal>
            <p class="eyebrow">{eb}</p>
            <h3>{h}</h3>
            <p>{p}</p>
          </div>
          {shot(img, alt)}
        </article>
'''

PILLARS = [
    ("Intelligence Sharing", "The heart of the platform. Members receive human-triaged intelligence and share their own, so everyone gets early visibility.",
     ["Threat Intelligence Forums", "Human and machine-to-machine sharing", "Supply Chain Working Group"]),
    ("Managed Threat Intelligence", "Human-triaged, Australian-specific intelligence from analysts. Members act on real threats instead of disproving fakes.",
     ["Vulnerability Advisories", "Threat Advisories", "Strategic Advisories", "Knowledge base", "Detections", "TriageBot", "Automated Threat Feeds"]),
    ("Cyber Defensive Capabilities", "Services that lift a member's defences from day one, all included in membership.",
     ["Attack Surface Monitoring", "Software Bill of Materials (SBOM)", "Crawler", "Leaked Credential Monitoring", "Vulnerability Database", "Australian Honeypots", "Heretic", "Defacement Monitor", "MS Patch Tuesday Dashboard"]),
]
tabs = "".join(f'<button type="button" class="cip__tab{" is-on" if i == 0 else ""}" data-i="{i}" aria-pressed="{"true" if i == 0 else "false"}"><b>{len(p)}</b><span>{n}</span></button>' for i, (n, d, p) in enumerate(PILLARS))
panels = "".join(f'<div class="cip__panel{" is-on" if i == 0 else ""}" data-i="{i}"><p>{d}</p><ul>{"".join(f"<li style=\"--k:{k}\">{x}</li>" for k, x in enumerate(p))}</ul></div>' for i, (n, d, p) in enumerate(PILLARS))

main = f'''  <main class="cs cs--ci">
    <div class="cs-progress" aria-hidden="true"><i></i></div>
    <!-- ============ CASE HERO ============ -->
    <section class="cs-hero">
      <canvas class="hero__dots" aria-hidden="true"></canvas>
      <div class="wrap">
        <nav class="cs-crumbs" data-intro style="--d:.05s"><a href="../work.html">Work</a><span>/</span><span>CI-ISAC Australia</span></nav>
        <p class="eyebrow" data-intro style="--d:.1s">Cyber security · Not-for-profit · Australia</p>
        <h1 class="cs-title">
          <span class="line"><span class="line__in" style="--d:.15s">Threat intelligence,</span></span>
          <span class="line"><span class="line__in" style="--d:.25s">sold like a <span class="accent">product</span>.</span></span>
        </h1>
        <p class="cs-lead" data-intro style="--d:.4s">CI-ISAC Australia is the not-for-profit intelligence sharing community for Australia's critical infrastructure and essential services, with 160+ member organisations from national telcos to regional GPs. We redesigned their WordPress site as a lighter, product-led website: nine page designs in Figma that turn a complex membership into one clear offer, with the Webflow build now under way.</p>

        <dl class="cs-facts" data-intro style="--d:.5s">
          <div><dt>Client</dt><dd>CI-ISAC Australia</dd></div>
          <div><dt>Scope</dt><dd>Website redesign, Webflow build, icon set</dd></div>
          <div><dt>Platform</dt><dd>WordPress → Figma → Webflow</dd></div>
          <div><dt>Status</dt><dd>Design done, Webflow build in progress</dd></div>
        </dl>
      </div>

      <div class="wrap cs-cover" data-intro style="--d:.6s">
        <div class="vwin cs-win" data-parallax=".06">
          <div class="win__bar"><i></i><i></i><i></i><span class="win__url">ci-isac.org.au</span></div>
          <img src="{I}hero.webp" alt="CI-ISAC homepage hero: Human analysis. More actionable intelligence." width="1600" height="1000">
        </div>
      </div>
    </section>

    <!-- ============ CHALLENGE ============ -->
    <section data-chapter="Challenge" class="sec cs-brief">
      <div class="wrap cs-split">
        <div data-reveal>
          <p class="eyebrow">The challenge</p>
          <h2 class="h2">A serious service, <span class="dim">hidden behind an old site.</span></h2>
        </div>
        <div class="cs-text" data-reveal style="--d:.08s">
          <p>CI-ISAC works much like a SaaS platform: members get an intelligence sharing network, human-triaged advisories and a suite of defensive tools. The old WordPress site presented it like an association, with long pages and no clear picture of what a member actually gets.</p>
          <p>The team wanted a lighter, cleaner site in the style of modern SaaS products, streamlined to around ten pages, with a CMS for analysis and news. The people reading it are busy: a single IT lead at a regional clinic, a security team at a utility, a SOC at a national telco.</p>
          <ul class="cs-goals">
            <li>Explain membership in one scroll</li>
            <li>Show that every member gets the same 19 products</li>
            <li>Make analysis and policy work easy to find</li>
          </ul>
        </div>
      </div>
      <div class="wrap">
        <div class="cs-problems">
          <article data-reveal style="--d:0.00s"><h3>19 products, no structure</h3><p>Advisories, monitoring, honeypots, feeds and forums were described in different places with no order a buyer could follow.</p></article>
          <article data-reveal style="--d:0.06s"><h3>Members of every size</h3><p>A one-person IT team and an established SOC need different reasons to join, but get exactly the same membership.</p></article>
          <article data-reveal style="--d:0.12s"><h3>Expert content, buried</h3><p>Advisories, position papers and the SOCI Act response are the best proof of expertise, and they were hard to find.</p></article>
        </div>
      </div>
    </section>

    <!-- ============ HOW WE WORKED ============ -->
    <section data-chapter="Process" class="sec cs-chapter">
      <div class="wrap">
        <header class="sec__head sec__head--row" data-reveal>
          <div>
            <p class="eyebrow">How we work</p>
            <h2 class="h2">Homepage first, <span class="dim">then the whole system.</span></h2>
          </div>
          <p class="sec__lead">The client's own wireframes were the starting point, with nothing treated as fixed. The homepage set the style, revisions came in as comments right on the Figma frames, and the other pages followed in the same system.</p>
        </header>
        <div class="cs-process" data-reveal>
          <div class="cs-phase" style="--i:0"><p class="cs-phase__when">Structure</p><h3>From wireframes to a site map</h3><p>We took the team's wireframes and site map, cut the old site down to about ten pages and planned a CMS for analysis and news.</p><ul><li>Wireframe review</li><li>New site map</li><li>Content plan</li></ul></div>
          <div class="cs-phase" style="--i:1"><p class="cs-phase__when">Homepage</p><h3>Light SaaS, dark navy</h3><p>Deep navy, a signal orange for actions and night photos of real Australian infrastructure instead of hooded-hacker stock art.</p><ul><li>Homepage design</li><li>Revisions in Figma</li><li>Colour and type system</li></ul></div>
          <div class="cs-phase" style="--i:2"><p class="cs-phase__when">All pages</p><h3>Nine page designs</h3><p>About, Sectors, Membership, Resources, an article template, the SOCI Act review, TLP designations and Contact, plus a custom icon set.</p><ul><li>8 inner page designs</li><li>Article template</li><li>Custom icon set</li></ul></div>
          <div class="cs-phase" style="--i:3"><p class="cs-phase__when">Build</p><h3>Webflow, in progress</h3><p>A native Webflow build with CMS collections for resources and events, and the existing posts moved over from WordPress.</p><ul><li>Webflow build</li><li>CMS and filters</li><li>Post migration</li></ul></div>
        </div>
      </div>
    </section>

    <!-- ============ NUMBERS ============ -->
    <section class="cs-numbers" aria-label="CI-ISAC in numbers">
      <div class="wrap">
        <p class="eyebrow" data-reveal>At a glance</p>
        <div class="cs-bench">
          <div data-reveal><b><span data-count="160">0</span>+</b><span>Member organisations</span><em>From national telcos to regional GPs</em></div>
          <div data-reveal style="--d:.06s"><b><span data-count="19">0</span></b><span>Products in every membership</span><em>Across 3 pillars, no add-ons</em></div>
          <div data-reveal style="--d:.12s"><b><span data-count="9">0</span></b><span>Page designs in Figma</span><em>One system, ready for Webflow</em></div>
          <div data-reveal style="--d:.18s"><b><span data-count="4">0</span> <small>hours</small></b><span>Saved per actionable advisory</span><em>As reported by members</em></div>
        </div>
      </div>
    </section>

    <!-- ============ PILLAR DEMO ============ -->
    <section data-chapter="Idea" class="sec cs-demo">
      <div class="wrap cs-split">
        <div data-reveal>
          <p class="eyebrow">The idea</p>
          <h2 class="h2">One membership, <span class="dim">three pillars.</span></h2>
          <p class="cs-demo__lead">Nineteen products are too many to list one by one. So the site groups them into three pillars with a count on each: intelligence sharing, managed threat intelligence and cyber defensive capabilities. 3 + 7 + 9, every member, no add-ons. The same structure runs from the homepage to the membership page.</p>
          <p class="cs-demo__try">Try it. Switch between the pillars.</p>
        </div>
        <div class="cip" data-reveal style="--d:.1s">
          <div class="cip__top"><span class="cip__label">Included in every membership</span><b class="cip__count" aria-live="polite"><span>3</span> of 19 products</b></div>
          <div class="cip__tabs">{tabs}</div>
          <div class="cip__panels">{panels}</div>
          <p class="cip__foot">All 19 products. Every member. No add-ons.</p>
        </div>
      </div>
    </section>

    <!-- ============ GALLERY / STORY ============ -->
    <section data-chapter="Details" class="sec cs-story">
      <div class="wrap">
{row(False, "Homepage", "The offer in three cards.", "Right after the hero and the key numbers, three dark cards show the pillars with their product counts and the top products in each. One line under them closes the argument: all 19 products, every member, no add-ons.", "pillars.webp", "One membership, 3 pillars of support")}
{row(True, "Member size", "Same access, whatever the size.", "The team asked for a block that speaks to each kind of member. A small switcher picks single IT lead, small security team or established SOC, and shows what members of that size value most, from clear advisories to Attack Surface Monitoring.", "sizes.webp", "Members vary by size, access to the capabilities does not")}
{row(False, "Sectors", "Every sector the SOCI Act covers.", "Twelve sectors in a clean grid, each with a line on its threat picture, from energy and water to space technology and local government. Health gets its own block for the Health Cyber Sharing Network: 60+ organisations, 600+ facilities, a $6.4m Commonwealth grant.", "hcsn.webp", "Health Cyber Sharing Network with key numbers and a chart")}
{row(True, "Membership", "All 19 products, described properly.", "The membership page lists every product under its pillar as a short, specific card: what it does and why it matters to an Australian operator. Fees are explained in plain words, with a briefing form instead of a price table.", "products.webp", "A suite of cyber defence products and services")}
{row(False, "About", "Credentials that build trust.", "The about page explains how the platform works in short, then introduces the management board: former intelligence leads, a Brigadier, an Air Commodore and a former ICANN CEO, each with a short bio.", "board.webp", "Management board on the About page")}
{row(True, "Resources", "Analysis people can actually find.", "A filterable hub for announcements, education, governance and partnerships, plus a reading-friendly article template and dedicated pages for the SOCI Act review and TLP designations.", "resources.webp", "CI-ISAC Resources hub with category filters")}
      </div>
    </section>

    <!-- ============ FULL PAGE ============ -->
    <section class="sec cs-duo">
      <div class="wrap cs-duo__grid">
        <div class="cs-duo__code" data-reveal>
          <p class="eyebrow">The whole system</p>
          <h3>Nine pages, one design language.</h3>
          <p>Home, About, Sectors, Membership, Resources, an article, the SOCI Act review, TLP designations and Contact. The same navy, orange and card system across all of them, so the Webflow build can reuse every component.</p>
          <div class="vwin cs-shot"><div class="win__bar"><i></i><i></i><i></i></div><img src="{I}pages.webp" alt="All nine CI-ISAC page designs side by side" loading="lazy" width="1600" height="1000"></div>
        </div>
        <div class="wa-scroll" data-reveal style="--d:.1s">
          <div class="vwin"><div class="win__bar"><i></i><i></i><i></i><span class="win__url">Homepage design</span></div>
            <div class="wa-scroll__vp"><img src="{I}full.webp" alt="Full CI-ISAC homepage design, top to bottom" loading="lazy" width="1000" height="5521"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ REEL ============ -->
    <section class="cs-reel" aria-hidden="true">
      <div class="cs-reel__track">{"".join(f'<img src="{I}{x}" alt="" loading="lazy" width="1600" height="1000">' for x in ["news.webp", "dayone.webp", "sectors.webp", "finance.webp", "article.webp", "soci.webp", "contact.webp", "tlp.webp", "fees.webp"] * 2)}</div>
    </section>

    <!-- ============ KEY DECISIONS ============ -->
    <section data-chapter="Decisions" class="sec cs-chapter">
      <div class="wrap">
        <header class="sec__head" data-reveal>
          <p class="eyebrow">Key decisions</p>
          <h2 class="h2">Choices that make a complex service <span class="dim">easy to say yes to.</span></h2>
        </header>
        <div class="cs-dec">
          <div class="cs-dec__row" data-reveal style="--d:0.00s">
            <h3 class="cs-dec__q">How do you show what members get?</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>A long feature list on one page.</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>Three pillars with product counts, 3 + 7 + 9, and a card for every product.</p></div>
          </div>
          <div class="cs-dec__row" data-reveal style="--d:0.04s">
            <h3 class="cs-dec__q">How do you price for every size?</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>Bronze, silver and gold packages.</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>One product set for all, a size switcher, and fees explained in a short conversation.</p></div>
          </div>
          <div class="cs-dec__row" data-reveal style="--d:0.08s">
            <h3 class="cs-dec__q">What does cyber security look like?</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>Hooded hackers, padlocks and green code.</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>Night photos of real infrastructure, a calm navy palette and a custom icon set.</p></div>
          </div>
          <div class="cs-dec__row" data-reveal style="--d:0.12s">
            <h3 class="cs-dec__q">Where does the expertise live?</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>A blog link in the footer.</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>Latest analysis on the homepage, a filterable resources hub and dedicated policy pages.</p></div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ RESULT ============ -->
    <section data-chapter="Result" class="sec cs-result">
      <div class="wrap">
        <header class="sec__head" data-reveal>
          <p class="eyebrow">The result</p>
          <h2 class="h2">A cyber defence network <span class="dim">that reads like a product.</span></h2>
        </header>
        <div class="cs-outcomes">
          <div data-reveal><b>9 designs</b><span>a complete page system in Figma, reviewed through comments on the frames</span></div>
          <div data-reveal style="--d:.06s"><b>19 products</b><span>grouped into three clear pillars</span></div>
          <div data-reveal style="--d:.12s"><b>CMS-ready</b><span>resources, events and articles planned as collections</span></div>
          <div data-reveal style="--d:.18s"><b>Webflow</b><span>build in progress, posts moving over from WordPress</span></div>
        </div>
        <div class="cs-got" data-reveal>
          <h3>What CI-ISAC <br>gets from the project</h3>
          <ul>
            <li>Homepage and 8 inner page designs</li>
            <li>A membership page for all 19 products</li>
            <li>Sector pages with health and finance networks</li>
            <li>A filterable resources hub and article template</li>
            <li>SOCI Act review and TLP pages</li>
            <li>A briefing and trial request form</li>
            <li>A custom icon set</li>
            <li>A Webflow build with CMS</li>
          </ul>
        </div>
      </div>
    </section>

MOREWORK
  </main>'''

a = src.index("    <!-- ============ MORE WORK ============ -->")
b = src.index("  </main>")
main = main.replace("MOREWORK\n", src[a:b])
h0 = src.index('  <main class="cs cs--aw">')
h1 = src.index("  </main>") + len("  </main>")
out = src[:h0] + main + src[h1:]
out = out.replace("<title>AWS Wrap case study | Sorvel Studio</title>", "<title>CI-ISAC Australia case study | Sorvel Studio</title>")
out = re.sub(r'<meta name="description" content="[^"]*" />', '<meta name="description" content="How Sorvel redesigned the CI-ISAC Australia website: nine page designs in Figma that turn a cyber threat intelligence membership into one clear offer, built in Webflow." />', out, count=1)
out = re.sub(r'href="../css/case.css(\?v=\d+)?"', 'href="../css/case.css?v=12"', out)
out = re.sub(r'<script src="../js/case.js\?v=\d+"></script>', '<script src="../js/case.js?v=12"></script>', out)
open(W + "ci-isac.html", "w").write(out)
print("ok", len(out))
