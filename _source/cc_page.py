import re, sys
sys.path.insert(0, "SOURCE_DIR")
W = "WEBSITE_DIR/work/"
src = open(W + "awswrap.html").read()
src = src.replace('<img fetchpriority="low" ', '<img ')  # undo the SEO pass tweak so templates match
src = re.sub(r'<title>AWS Wrap[^<]*</title>', '<title>AWS Wrap case study | Sorvel Studio</title>', src)  # restore the template title

# reuse the iPhone frame markup from the AWS page
phone_tpl = re.search(r'(<div class="cs-cover__phone iphone".*?<img src=")[^"]+(" alt="" width="393" height="852"></span></span></span></div>)', src, re.S)
def phone(cls, img, alt, par, lazy=True):
    a, b = phone_tpl.group(1), phone_tpl.group(2)
    a = a.replace('class="cs-cover__phone iphone" data-parallax="-.1"', f'class="{cls} iphone" data-parallax="{par}"').replace("--sb:#020202;--sbc:#fff", "--sb:#000;--sbc:#fff")
    b = b.replace('alt=""', f'alt="{alt}"' + (' loading="lazy"' if lazy else ""))
    return a + img + b

I = "../img/work/college-classics/"
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

BODIES = [("Royal", "#1f48a6"), ("Navy", "#1b2547"), ("Black", "#151515"), ("Maroon", "#5a1d29"),
          ("Bottle green", "#1d4631"), ("Purple", "#43215c"), ("Red", "#a3212c"), ("Gold", "#c3922e")]
SLEEVES = [("White", "#f1eee7"), ("Cream", "#c8a978"), ("Grey", "#a1a4a5"), ("Black", "#171717")]
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
              <rect class="ccp__tag" x="190" y="72" width="20" height="12" rx="1.5"/>
            </svg>'''

main = f'''  <main class="cs cs--cc">
    <div class="cs-progress" aria-hidden="true"><i></i></div>
    <!-- ============ CASE HERO ============ -->
    <section class="cs-hero">
      <canvas class="hero__dots" aria-hidden="true"></canvas>
      <div class="wrap">
        <nav class="cs-crumbs" data-intro style="--d:.05s"><a href="../work.html">Work</a><span>/</span><span>College Classics</span></nav>
        <p class="eyebrow" data-intro style="--d:.1s">Fashion · Varsity jackets · Made in England</p>
        <h1 class="cs-title">
          <span class="line"><span class="line__in" style="--d:.15s">Forty-four jackets,</span></span>
          <span class="line"><span class="line__in" style="--d:.25s"><span class="accent">one</span> fit.</span></span>
        </h1>
        <p class="cs-lead" data-intro style="--d:.4s">College Classics is the ready-to-wear line of an English workshop that has made custom varsity jackets since 2011. We designed the store in Figma and built it on Shopify in 28 days: an editorial look that sells a £245 jacket without a sales call, and a colourway system that keeps 44 combinations easy to browse.</p>

        <dl class="cs-facts" data-intro style="--d:.5s">
          <div><dt>Client</dt><dd>College Classics</dd></div>
          <div><dt>Scope</dt><dd>E-commerce design, Shopify development</dd></div>
          <div><dt>Timeline</dt><dd>28 days</dd></div>
          <div><dt>Live store</dt><dd><a href="https://7d00zu-0i.myshopify.com/" target="_blank" rel="noopener">View the store ↗</a></dd></div>
        </dl>
      </div>

      <div class="wrap cs-cover" data-intro style="--d:.6s">
        {phone("cs-cover__phone", I + "m-hero.webp", "", "-.1", lazy=False)}
        <div class="vwin cs-win" data-parallax=".06">
          <div class="win__bar"><i></i><i></i><i></i><span class="win__url">College Classics · Shopify</span></div>
          <img src="{I}hero.webp" alt="College Classics homepage hero: Wool body. Leather sleeves." width="1600" height="1000">
        </div>
      </div>
    </section>

    <!-- ============ CHALLENGE ============ -->
    <section data-chapter="Challenge" class="sec cs-brief">
      <div class="wrap cs-split">
        <div data-reveal>
          <p class="eyebrow">The challenge</p>
          <h2 class="h2">A maker since 2011. <span class="dim">A shop from day one.</span></h2>
        </div>
        <div class="cs-text" data-reveal style="--d:.08s">
          <p>For fourteen years the workshop made varsity jackets to order for universities, clubs and companies. Every sale started with a conversation. College Classics is the first jacket with their own name in the collar: finished, boxed and ready to ship.</p>
          <p>That meant a store that had to do the selling on its own. It needed to show 44 colourways without turning into a wall of thumbnails, explain why a jacket costs £245, and feel like a heritage brand on the first visit, not a new shop nobody has heard of.</p>
          <ul class="cs-goals">
            <li>Sell online with no sales call</li>
            <li>Make 44 colourways easy to browse</li>
            <li>Earn trust for a brand-new name</li>
          </ul>
        </div>
      </div>
      <div class="wrap">
        <div class="cs-problems">
          <article data-reveal style="--d:0.00s"><h3>44 colourways</h3><p>Eight body colours and a choice of sleeves. Shown the usual way, that's a dropdown nobody opens or a grid nobody finishes.</p></article>
          <article data-reveal style="--d:0.06s"><h3>A price to explain</h3><p>£245 is fair for 24oz melton and full-grain leather. But the quality doesn't show in a thumbnail, so the page has to explain it.</p></article>
          <article data-reveal style="--d:0.12s"><h3>From custom to ready-made</h3><p>Fourteen years of reputation sat with the custom business. The new brand needed to borrow that trust without confusing the two.</p></article>
        </div>
      </div>
    </section>

    <!-- ============ HOW WE WORKED ============ -->
    <section data-chapter="Process" class="sec cs-chapter">
      <div class="wrap">
        <header class="sec__head sec__head--row" data-reveal>
          <div>
            <p class="eyebrow">How we worked</p>
            <h2 class="h2">28 days, three milestones, <span class="dim">one launch.</span></h2>
          </div>
          <p class="sec__lead">The project ran in three fixed milestones. Each one ended with something the client could open, click through and approve before the next began.</p>
        </header>
        <div class="cs-process" data-reveal>
          <div class="cs-phase" style="--i:0"><p class="cs-phase__when">Direction</p><h3>Heritage menswear, not streetwear</h3><p>We agreed on a look before drawing a single page: cream and black, a heavy slab serif and calm product photography, closer to a classic outfitter than a hype drop.</p><ul><li>Mood and references</li><li>Store structure review</li><li>Type and colour</li></ul></div>
          <div class="cs-phase" style="--i:1"><p class="cs-phase__when">Milestone 1</p><h3>Homepage in Figma</h3><p>Hero, colourway grid, featured jacket, reviews, "why it costs", the story and the service strip. Desktop and mobile.</p><ul><li>Homepage desktop</li><li>Homepage mobile</li><li>Component set</li></ul></div>
          <div class="cs-phase" style="--i:2"><p class="cs-phase__when">Milestone 2</p><h3>Inner pages in Figma</h3><p>Collection with colour filters, product page with swatches and size guide, our story, delivery and returns, FAQ.</p><ul><li>Collection and filters</li><li>Product page</li><li>Content pages</li></ul></div>
          <div class="cs-phase" style="--i:3"><p class="cs-phase__when">Milestone 3</p><h3>Shopify build and QA</h3><p>A custom theme built from the Figma files, 44 products linked by colour, then a full QA pass on real phones before launch.</p><ul><li>Custom Shopify theme</li><li>Swatches and filters</li><li>16-point QA fix list</li></ul></div>
        </div>
      </div>
    </section>

    <!-- ============ NUMBERS ============ -->
    <section class="cs-numbers" aria-label="Key facts on the new store">
      <div class="wrap">
        <p class="eyebrow" data-reveal>At a glance</p>
        <div class="cs-bench">
          <div data-reveal><b><span data-count="44">0</span></b><span>Colourways, each its own product</span><em>Linked by swatches</em></div>
          <div data-reveal style="--d:.06s"><b><span data-count="28">0</span> <small>days</small></b><span>From first design to launch</span><em>Figma and Shopify</em></div>
          <div data-reveal style="--d:.12s"><b><span data-count="11">0</span></b><span>Sizes, from XXS to 6XL</span><em>One size guide for all</em></div>
          <div data-reveal style="--d:.18s"><b><span data-count="16">0</span></b><span>Fixes found and closed in QA</span><em>Before the store went live</em></div>
        </div>
      </div>
    </section>

    <!-- ============ COLOURWAY DEMO ============ -->
    <section data-chapter="Idea" class="sec cs-demo">
      <div class="wrap cs-split">
        <div data-reveal>
          <p class="eyebrow">The idea</p>
          <h2 class="h2">Pick a body, <span class="dim">pick a sleeve.</span></h2>
          <p class="cs-demo__lead">Every colourway is a separate Shopify product with its own photos, URL and stock. On the page they act like one: swatches jump between them instantly, and the collection can be filtered by body or sleeve colour. Shoppers get a simple choice, Google gets 44 indexable pages.</p>
          <p class="cs-demo__try">Try it. This is a simplified version of the swatch picker.</p>
        </div>
        <div class="ccp" data-reveal style="--d:.1s;--body:#1f48a6;--sleeve:#f1eee7">
          <div class="ccp__top"><span class="ccp__label">The Varsity Jacket</span><b class="ccp__name" aria-live="polite">Royal / White</b><span class="ccp__price">£245 · one fit, every colour</span></div>
          <div class="ccp__stage">
            {JACKET}
          </div>
          <div class="ccp__grp"><span>Body</span><div class="ccp__row">{sw("body", BODIES, "Royal")}</div></div>
          <div class="ccp__grp"><span>Sleeves</span><div class="ccp__row">{sw("sleeve", SLEEVES, "White")}</div></div>
        </div>
      </div>
    </section>

    <!-- ============ FIGMA ============ -->
    <section data-chapter="System" class="sec cs-figma">
      <div class="wrap">
        <header class="sec__head sec__head--row" data-reveal>
          <div><p class="eyebrow">Design first</p><h2 class="h2">Every page of the store, <span class="dim">desktop and mobile.</span></h2></div>
          <p class="sec__lead">Home, product, catalogue, our story, size and fit, contact, FAQ, returns, delivery, search and cart, all designed in Figma before a line of Shopify code.</p>
        </header>
        <div class="figma figma--solo" data-reveal>
          <div class="vwin figma__canvas" data-parallax=".03"><div class="win__bar"><i></i><i></i><i></i><span class="win__url">Figma · College Classics</span></div><img src="../img/work/college-classics/figma.webp" alt="Figma canvas with every College Classics page for desktop and mobile" width="1600" height="700" loading="lazy" decoding="async"></div>
        </div>
      </div>
    </section>

    <!-- ============ GALLERY / STORY ============ -->
    <section data-chapter="Details" class="sec cs-story">
      <div class="wrap">
{row(False, "Colourways", "The whole range, on one screen.", "Right under the hero, every colourway sits in a single swatch grid, split body and sleeve like the real jacket. One tap opens that exact product, so people who know what they want skip the browsing.", "colours.webp", "See all of our colour-ways swatch grid")}
{row(True, "Product", "Built like the ones they don't make any more.", "The featured jacket gets a full spec table: body, sleeves, lining, trims and where it's made. One price for all 44 colourways, and delivery, returns and sizes repeated right under the buttons.", "featured.webp", "Featured varsity jacket with photo gallery and spec table")}
{row(False, "Price", "Why it costs what it costs.", "Instead of discount banners, three plain cards explain the price: the 24oz wool, the full-grain leather and the in-house making. Things that never show in a photo, said out loud.", "why.webp", "Why it costs what it costs: the wool, the leather, the making")}
{row(True, "Story", "Fourteen years of borrowed trust.", "A new name needs a history. The story block tells how the workshop spent fourteen years making jackets for other people, next to the bear mascot drawn for the brand, so the shop feels established from day one.", "story.webp", "Our story section with the College Classics bear mascot")}
      </div>
    </section>

    <!-- ============ MOBILE ============ -->
    <section class="sec cs-duo">
      <div class="wrap cs-duo__grid">
        <div class="cs-duo__code" data-reveal>
          <p class="eyebrow">Mobile</p>
          <h3>Most orders start on a phone.</h3>
          <p>Product photo first, headline second, two full-width buttons and the key facts in one row. The swatch grid scrolls sideways, so all 44 colourways stay one thumb away.</p>
          <div class="vwin cs-shot"><div class="win__bar"><i></i><i></i><i></i></div><img src="{I}featured.webp" alt="Featured jacket section on desktop" loading="lazy" width="1600" height="1000"></div>
        </div>
        <div class="cs-phones" data-reveal style="--d:.1s">
          {phone("cs-phone", I + "m-hero.webp", "College Classics mobile homepage", ".08")}
          {phone("cs-phone cs-phone--2", I + "m-colours.webp", "College Classics colourways on mobile", "-.04").replace("--sb:#000;--sbc:#fff", "--sb:#fff;--sbc:#0b0c0f")}
        </div>
      </div>
    </section>

    <!-- ============ REEL ============ -->
    <section class="cs-reel" aria-hidden="true">
      <div class="cs-reel__track">{"".join(f'<img src="{I}{x}" alt="" loading="lazy" width="1600" height="1000">' for x in ["colours.webp", "featured.webp", "why.webp", "story.webp", "hero.webp"] * 2)}</div>
    </section>

    <!-- ============ KEY DECISIONS ============ -->
    <section data-chapter="Decisions" class="sec cs-chapter">
      <div class="wrap">
        <header class="sec__head" data-reveal>
          <p class="eyebrow">Key decisions</p>
          <h2 class="h2">Choices that sell a £245 jacket <span class="dim">without a salesperson.</span></h2>
        </header>
        <div class="cs-dec">
          <div class="cs-dec__row" data-reveal style="--d:0.00s">
            <h3 class="cs-dec__q">How do you show 44 colourways?</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>One product with a long colour dropdown.</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>44 products linked by swatches, plus body and sleeve colour filters on the collection.</p></div>
          </div>
          <div class="cs-dec__row" data-reveal style="--d:0.04s">
            <h3 class="cs-dec__q">How do you defend the price?</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>Sale badges and countdown timers.</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>One honest price and a section that explains the wool, the leather and the making.</p></div>
          </div>
          <div class="cs-dec__row" data-reveal style="--d:0.08s">
            <h3 class="cs-dec__q">What should it look like?</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>A stock streetwear theme with loud banners.</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>An editorial layout in cream and black, a heavy slab serif and lots of air around the product.</p></div>
          </div>
          <div class="cs-dec__row" data-reveal style="--d:0.12s">
            <h3 class="cs-dec__q">How does a new brand earn trust?</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>Launch and wait for reviews.</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>Lead with the 14-year maker story, Google reviews and "made in England" in the first screen.</p></div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ RESULT ============ -->
    <section data-chapter="Result" class="sec cs-result">
      <div class="wrap">
        <header class="sec__head" data-reveal>
          <p class="eyebrow">The result</p>
          <h2 class="h2">A heritage store <span class="dim">on day one.</span></h2>
        </header>
        <div class="cs-outcomes">
          <div data-reveal><b>28 days</b><span>from the first Figma frame to a live Shopify store</span></div>
          <div data-reveal style="--d:.06s"><b>44 pages</b><span>one indexable product page for every colourway</span></div>
          <div data-reveal style="--d:.12s"><b>One price</b><span>explained on the page instead of discounted</span></div>
          <div data-reveal style="--d:.18s"><b>Editable</b><span>products, colours and content managed in Shopify by the team</span></div>
        </div>
        <div class="cs-got" data-reveal>
          <h3>What College Classics <br>walked away with</h3>
          <ul>
            <li>A store design in Figma, desktop and mobile</li>
            <li>A custom Shopify theme built from it</li>
            <li>44 colourway products linked by swatches</li>
            <li>Body and sleeve colour filters</li>
            <li>A product page with spec table and size guide</li>
            <li>Story, delivery, returns and FAQ pages</li>
            <li>A 16-point QA pass before launch</li>
            <li>Newsletter sign-up for the next drop</li>
          </ul>
        </div>
      </div>
    </section>

MOREWORK
  </main>'''

# fill MORE WORK + CTA from the AWS page (more list is regenerated afterwards)
a = src.index("    <!-- ============ MORE WORK ============ -->")
b = src.index("  </main>")
main = main.replace("MOREWORK\n", src[a:b])

h0 = src.index('  <main class="cs cs--aw">')
h1 = src.index("  </main>") + len("  </main>")
out = src[:h0] + main + src[h1:]
out = out.replace("<title>AWS Wrap case study | Sorvel Studio</title>", "<title>College Classics case study | Sorvel Studio</title>")
out = re.sub(r'<meta name="description" content="[^"]*" />', '<meta name="description" content="How Sorvel designed and built the College Classics Shopify store in 28 days: an editorial varsity jacket shop with 44 colourways linked by swatches." />', out, 1)
out = out.replace('href="../css/case.css"', 'href="../css/case.css?v=9"')
out = out.replace('<script src="../js/case.js?v=8"></script>', '<script src="../js/case.js?v=9"></script>')
open(W + "college-classics.html", "w").write(out)
print("ok", len(out))
