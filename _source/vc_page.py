import re
W = "WEBSITE_DIR/work/"
src = open(W + "awswrap.html").read()
src = src.replace('<img fetchpriority="low" ', '<img ')  # undo the SEO pass tweak so templates match
src = re.sub(r'<title>AWS Wrap[^<]*</title>', '<title>AWS Wrap case study | Sorvel Studio</title>', src)  # restore the template title
I = "../img/work/varsity-city/"

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

BODIES = [("Forest", "#1f4a32"), ("Scarlet", "#b51f2e"), ("Navy", "#1b2547"), ("Black", "#151515"),
          ("Orange", "#d9661f"), ("Royal", "#1f48a6"), ("Gold", "#c3922e"), ("Purple", "#43215c")]
SLEEVES = [("White", "#f1eee7"), ("Cream", "#c8a978"), ("Black", "#171717"), ("Grey", "#a1a4a5"), ("Scarlet", "#b51f2e")]
RIBS = [("Black", "#151515"), ("Navy", "#1b2547"), ("Scarlet", "#b51f2e"), ("Forest", "#1f4a32"), ("White", "#f1eee7")]
def sw(group, items, on):
    return "".join(f'<button type="button" class="ccp__sw{" is-on" if n == on else ""}" style="--c:{c}" data-g="{group}" data-c="{c}" data-n="{n}" aria-label="{n} {group}" aria-pressed="{"true" if n == on else "false"}"></button>' for n, c in items)

JACKET = '''<svg class="ccp__svg" viewBox="0 0 400 380" aria-hidden="true">
              <path class="ccp__hook" d="M200 14c10 0 15 6 15 12s-6 10-15 14M200 40v8M150 64l50-16 50 16" />
              <path class="ccp__sl" d="M140 66C96 76 78 112 72 150L54 286l40 7 18-118 10-92z"/>
              <path class="ccp__sl" d="M260 66c44 10 62 46 68 84l18 136-40 7-18-118-10-92z"/>
              <path class="ccp__bd" d="M140 66q60 26 120 0l20 12 4 224q-84 14-168 0l4-224z"/>
              <path class="ccp__rib" d="M54 286l40 7-3 26-40-7zM306 293l40-7 3 26-40 7zM116 302q84 14 168 0v26q-84 14-168 0z"/>
              <path class="ccp__st" d="M53 296l40 7M52 305l40 7M307 303l40-7M308 312l40-7M116 312q84 14 168 0M116 320q84 14 168 0"/>
              <path class="ccp__rib" d="M148 62q52 34 104 0l-12-12q-40 26-80 0z"/>
              <path class="ccp__st" d="M153 58q47 30 94 0M157 54q43 27 86 0"/>
              <path class="ccp__line" d="M200 86v222"/>
              <g class="ccp__snap"><circle cx="200" cy="110" r="4"/><circle cx="200" cy="150" r="4"/><circle cx="200" cy="190" r="4"/><circle cx="200" cy="230" r="4"/><circle cx="200" cy="270" r="4"/></g>
              <path class="ccp__welt" d="M146 214l24 40M254 214l-24 40"/>
              <text class="ccp__let" x="244" y="170" text-anchor="middle">M</text>
            </svg>'''

main = f'''  <main class="cs cs--vc">
    <div class="cs-progress" aria-hidden="true"><i></i></div>
    <!-- ============ CASE HERO ============ -->
    <section class="cs-hero">
      <canvas class="hero__dots" aria-hidden="true"></canvas>
      <div class="wrap">
        <nav class="cs-crumbs" data-intro style="--d:.05s"><a href="../work.html">Work</a><span>/</span><span>Varsity City</span></nav>
        <p class="eyebrow" data-intro style="--d:.1s">Apparel · Custom varsity jackets · UK since 2011</p>
        <h1 class="cs-title">
          <span class="line"><span class="line__in" style="--d:.15s">One maker, four kinds</span></span>
          <span class="line"><span class="line__in" style="--d:.25s">of <span class="accent">buyer</span>.</span></span>
        </h1>
        <p class="cs-lead" data-intro style="--d:.4s">Varsity City has hand-made custom varsity and letterman jackets in the UK since 2011, for Netflix, the NFL, Warner Bros, universities and school leavers. We redesigned their Shopify store around that mix: a bold new homepage that gives brands, teams, universities and schools their own path, and puts the online jacket designer front and centre.</p>

        <dl class="cs-facts" data-intro style="--d:.5s">
          <div><dt>Client</dt><dd>Varsity City</dd></div>
          <div><dt>Scope</dt><dd>UX and UI redesign, Shopify</dd></div>
          <div><dt>Platform</dt><dd>Figma + Shopify</dd></div>
          <div><dt>Full redesign</dt><dd>About 13 pages</dd></div>
        </dl>
      </div>

      <div class="wrap cs-cover" data-intro style="--d:.6s">
        <div class="vwin cs-win" data-parallax=".06">
          <div class="win__bar"><i></i><i></i><i></i><span class="win__url">Varsity City · Homepage</span></div>
          <img src="{I}hero.webp" alt="Varsity City homepage hero: UK and EU's leading varsity jacket supplier" width="1600" height="1000">
        </div>
      </div>
    </section>

    <!-- ============ CHALLENGE ============ -->
    <section data-chapter="Challenge" class="sec cs-brief">
      <div class="wrap cs-split">
        <div data-reveal>
          <p class="eyebrow">The challenge</p>
          <h2 class="h2">One jacket or a thousand. <span class="dim">Same site for both.</span></h2>
        </div>
        <div class="cs-text" data-reveal style="--d:.08s">
          <p>Varsity City sells to very different people. A student wants one jacket with their initial. A film studio needs a hero piece for a character. A university society orders sixty, a corporate client wants three hundred for an event.</p>
          <p>The old store mixed all of them on the same pages, with repeated content, small bugs and a bare page around the jacket designer, the tool that brings most custom orders in. The goal: simpler, up-to-date UX, more enquiries and better SEO, without touching the designer tool itself.</p>
          <ul class="cs-goals">
            <li>A clear path for every kind of buyer</li>
            <li>More bulk quote enquiries</li>
            <li>No duplicate content, better SEO</li>
          </ul>
        </div>
      </div>
      <div class="wrap">
        <div class="cs-problems">
          <article data-reveal style="--d:0.00s"><h3>Mixed audiences</h3><p>Single orders and 100+ corporate commissions shared the same pages, so neither got the answers it needed.</p></article>
          <article data-reveal style="--d:0.06s"><h3>A hidden designer</h3><p>The jacket designer brings in custom orders, but it sat on a bare page with no sizing, details or steps around it.</p></article>
          <article data-reveal style="--d:0.12s"><h3>Repeated content</h3><p>The same text on several pages confused visitors and competed with itself in search.</p></article>
        </div>
      </div>
    </section>

    <!-- ============ HOW WE WORKED ============ -->
    <section data-chapter="Process" class="sec cs-chapter">
      <div class="wrap">
        <header class="sec__head sec__head--row" data-reveal>
          <div>
            <p class="eyebrow">How we work</p>
            <h2 class="h2">Homepage first, <span class="dim">then a page for every buyer.</span></h2>
          </div>
          <p class="sec__lead">The redesign runs in clear milestones. The homepage sets the look and the structure, then each audience gets its own page before the Shopify build.</p>
        </header>
        <div class="cs-process" data-reveal>
          <div class="cs-phase" style="--i:0"><p class="cs-phase__when">Audit</p><h3>What to keep, what to cut</h3><p>We went through the current store page by page: duplicate content, broken bits, and which pages actually bring enquiries.</p><ul><li>Content and SEO audit</li><li>Bug list</li><li>New site map</li></ul></div>
          <div class="cs-phase" style="--i:1"><p class="cs-phase__when">Homepage</p><h3>Bold, sporty, trusted</h3><p>Deep green, scarlet and cream with a tall condensed headline, real photos of people in the jackets, and proof from big brands everywhere.</p><ul><li>Homepage desktop</li><li>Audience cards</li><li>Bulk quote form</li></ul></div>
          <div class="cs-phase" style="--i:2"><p class="cs-phase__when">Audience pages</p><h3>Four buyers, four pages</h3><p>Corporate and brands, sports teams, universities and societies, schools and leavers. Each with its own copy, proof and quote form.</p><ul><li>Four segment pages</li><li>Copy for each</li><li>Remaining pages</li></ul></div>
          <div class="cs-phase" style="--i:3"><p class="cs-phase__when">Build</p><h3>Shopify, designer untouched</h3><p>A clean Shopify build around the existing jacket designer, with sizing and details added to its page.</p><ul><li>Shopify theme</li><li>Designer page rebuilt</li><li>Redirects and SEO</li></ul></div>
        </div>
      </div>
    </section>

    <!-- ============ NUMBERS ============ -->
    <section class="cs-numbers" aria-label="Varsity City in numbers">
      <div class="wrap">
        <p class="eyebrow" data-reveal>At a glance</p>
        <div class="cs-bench">
          <div data-reveal><b>2011</b><span>Hand-crafting jackets since</span><em>15+ years of experience</em></div>
          <div data-reveal style="--d:.06s"><b><span data-count="8000">0</span>+</b><span>Jackets delivered worldwide</span><em>From one-offs to 100+ orders</em></div>
          <div data-reveal style="--d:.12s"><b><span data-count="17">0</span>+</b><span>Major brands and corporates</span><em>Netflix, NFL, Spotify, Bolt</em></div>
          <div data-reveal style="--d:.18s"><b><span data-count="25">0</span>+</b><span>Colour combinations in the designer</span><em>Body, sleeves, ribbing</em></div>
        </div>
      </div>
    </section>

    <!-- ============ DESIGNER DEMO ============ -->
    <section data-chapter="Idea" class="sec cs-demo">
      <div class="wrap cs-split">
        <div data-reveal>
          <p class="eyebrow">The idea</p>
          <h2 class="h2">Put the designer <span class="dim">in the spotlight.</span></h2>
          <p class="cs-demo__lead">The jacket designer is how most custom orders start, so the new homepage leads with it: "Design my jacket" is the first button in the hero, a whole section walks through body colour, sleeve leather, ribbing and letters, and four simple steps explain what happens next.</p>
          <p class="cs-demo__try">Try it. Pick the colours and add your letter.</p>
        </div>
        <div class="ccp ccp--vc" data-reveal style="--d:.1s;--body:#1f4a32;--sleeve:#f1eee7;--rib:#151515">
          <div class="ccp__top"><span class="ccp__label">Your custom varsity jacket</span><b class="ccp__name" aria-live="polite">Forest / White</b><span class="ccp__price">Made to order in 4–6 weeks</span></div>
          <div class="ccp__stage">
            {JACKET}
          </div>
          <div class="ccp__grp"><span>Body</span><div class="ccp__row">{sw("body", BODIES, "Forest")}</div></div>
          <div class="ccp__grp"><span>Sleeves</span><div class="ccp__row">{sw("sleeve", SLEEVES, "White")}</div></div>
          <div class="ccp__grp"><span>Ribbing</span><div class="ccp__row">{sw("rib", RIBS, "Black")}</div></div>
          <div class="ccp__grp"><span>Letter</span><div class="ccp__row"><input class="ccp__letter" type="text" maxlength="1" value="M" aria-label="Chest letter"></div></div>
        </div>
      </div>
    </section>

    <!-- ============ GALLERY / STORY ============ -->
    <section data-chapter="Details" class="sec cs-story">
      <div class="wrap">
{row(False, "Audiences", "Four doors, right after the hero.", "Corporate and brands, sports teams, universities and societies, schools and leavers. Each gets a big photo card with what they usually order, and leads to its own page. Above them, a row of real client names from the NFL to SOAS University.", "segments.webp", "For brands, schools, universities and teams: four audience cards")}
{row(True, "Collection", "Every kind of jacket, one grid.", "Custom varsity, letterman, women's, baseball, men's and personalised jackets, each as a photo card with a one-line description and a shop link. Real people in real jackets, no flat product shots.", "collection.webp", "Crafted for style, identity and comfort: the collection grid")}
{row(False, "Ready to ship", "For people who can't wait six weeks.", "Next to the made-to-order service sits a stock line: “Own your look” shows ready-to-ship jackets at £199, in stock and dispatched straight away.", "ownlook.webp", "Own your look: ready-to-ship varsity jackets at £199")}
{row(True, "Process", "Four steps, from colours to doorstep.", "Design it online, pick your base, add the detail, production and delivery in 4–6 weeks. A dark, numbered section that answers “what happens after I order?” before anyone has to ask.", "steps.webp", "Your custom jacket in 4 simple steps")}
{row(False, "Portfolio", "You've seen us before.", "Jackets made for Sex Education, Justice League, Venom and Kingsman 2, listed like film credits next to a still from the show. For a custom maker, nothing builds trust faster.", "portfolio.webp", "Portfolio: jackets made for Netflix, DC Films, Marvel and Kingsman")}
{row(True, "Bulk orders", "A quote form that sells the service.", "The bulk form lives on the homepage, with category, estimated quantity and project details, next to the promises that matter to a buyer: a reply within 4 business hours, no minimum order, sample and fitting days, a dedicated account manager.", "form.webp", "Bulk and wholesale pricing quote form")}
      </div>
    </section>

    <!-- ============ FULL PAGE ============ -->
    <section class="sec cs-duo">
      <div class="wrap cs-duo__grid">
        <div class="cs-duo__code" data-reveal>
          <p class="eyebrow">The whole homepage</p>
          <h3>Proof on every scroll.</h3>
          <p>Brand names in the top bar, client logos, film credits, materials and FAQs. Each section answers a doubt before it turns into a reason to leave, and every one ends with a way to design or quote.</p>
          <div class="vwin cs-shot"><div class="win__bar"><i></i><i></i><i></i></div><img src="{I}materials.webp" alt="Premium materials, no compromises" loading="lazy" width="1600" height="1000"></div>
        </div>
        <div class="wa-scroll" data-reveal style="--d:.1s">
          <div class="vwin"><div class="win__bar"><i></i><i></i><i></i><span class="win__url">Full homepage design</span></div>
            <div class="wa-scroll__vp"><img src="{I}full.webp" alt="Full Varsity City homepage design, top to bottom" loading="lazy" width="1000" height="8543"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ REEL ============ -->
    <section class="cs-reel" aria-hidden="true">
      <div class="cs-reel__track">{"".join(f'<img src="{I}{x}" alt="" loading="lazy" width="1600" height="1000">' for x in ["trusted.webp", "design.webp", "materials.webp", "faq.webp", "gallery.webp", "segments.webp"] * 2)}</div>
    </section>

    <!-- ============ KEY DECISIONS ============ -->
    <section data-chapter="Decisions" class="sec cs-chapter">
      <div class="wrap">
        <header class="sec__head" data-reveal>
          <p class="eyebrow">Key decisions</p>
          <h2 class="h2">Choices that turn visitors <span class="dim">into orders and quotes.</span></h2>
        </header>
        <div class="cs-dec">
          <div class="cs-dec__row" data-reveal style="--d:0.00s">
            <h3 class="cs-dec__q">Who is the homepage for?</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>Everyone at once, in one long product grid.</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>Four audience cards right after the hero, each leading to its own page.</p></div>
          </div>
          <div class="cs-dec__row" data-reveal style="--d:0.04s">
            <h3 class="cs-dec__q">Where does the designer live?</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>One link in the menu.</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>The first hero button, its own section and a four-step explainer.</p></div>
          </div>
          <div class="cs-dec__row" data-reveal style="--d:0.08s">
            <h3 class="cs-dec__q">How do you show the big names?</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>A small logo strip near the footer.</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>Names in the top bar, a logo row, client chips and a film portfolio.</p></div>
          </div>
          <div class="cs-dec__row" data-reveal style="--d:0.12s">
            <h3 class="cs-dec__q">How do you get bulk enquiries?</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>A generic contact page.</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>A bulk quote form on the homepage with quantity, category and a 4-hour reply promise.</p></div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ RESULT ============ -->
    <section data-chapter="Result" class="sec cs-result">
      <div class="wrap">
        <header class="sec__head" data-reveal>
          <p class="eyebrow">The result</p>
          <h2 class="h2">A store that knows <span class="dim">who it's talking to.</span></h2>
        </header>
        <div class="cs-outcomes">
          <div data-reveal><b>4 paths</b><span>brands, teams, universities and schools each get their own page</span></div>
          <div data-reveal style="--d:.06s"><b>Designer first</b><span>the tool that brings custom orders is the hero's main action</span></div>
          <div data-reveal style="--d:.12s"><b>Bulk form</b><span>quote requests arrive with category, quantity and details</span></div>
          <div data-reveal style="--d:.18s"><b>Cleaner SEO</b><span>one topic per page, no repeated content</span></div>
        </div>
        <div class="cs-got" data-reveal>
          <h3>What Varsity City <br>gets from the redesign</h3>
          <ul>
            <li>A new homepage design in Figma</li>
            <li>Four audience pages with new copy</li>
            <li>A rebuilt jacket designer page</li>
            <li>Collection and ready-to-ship blocks</li>
            <li>A film and brand portfolio section</li>
            <li>A bulk and wholesale quote form</li>
            <li>Materials and FAQ sections</li>
            <li>A clean Shopify build of about 13 pages</li>
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
out = out.replace("<title>AWS Wrap case study | Sorvel Studio</title>", "<title>Varsity City case study | Sorvel Studio</title>")
out = re.sub(r'<meta name="description" content="[^"]*" />', '<meta name="description" content="How Sorvel is redesigning the Varsity City Shopify store: a homepage with a clear path for brands, teams, universities and schools, built around the jacket designer." />', out, count=1)
out = re.sub(r'href="../css/case.css(\?v=\d+)?"', 'href="../css/case.css?v=11"', out)
out = re.sub(r'<script src="../js/case.js\?v=\d+"></script>', '<script src="../js/case.js?v=11"></script>', out)
open(W + "varsity-city.html", "w").write(out)
print("ok", len(out))
