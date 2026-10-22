import re
W = "WEBSITE_DIR/work/"
src = open(W + "awswrap.html").read()
src = src.replace('<img fetchpriority="low" ', '<img ')  # undo the SEO pass tweak so templates match
src = re.sub(r'<title>AWS Wrap[^<]*</title>', '<title>AWS Wrap case study | Sorvel Studio</title>', src)  # restore the template title
I = "../img/work/alma-secret/"
phone_tpl = re.search(r'(<div class="cs-cover__phone iphone".*?<img src=")[^"]+(" alt="" width="393" height="852"></span></span></span></div>)', src, re.S)
def phone(cls, img, alt, par, lazy=True, sb="#3f7d99", sbc="#fff"):
    a, b = phone_tpl.group(1), phone_tpl.group(2)
    a = re.sub(r'class="cs-cover__phone iphone" data-parallax="[^"]*"', f'class="{cls} iphone" data-parallax="{par}"', a)
    a = re.sub(r'--sb:[^;]+;--sbc:[^"]+"', f'--sb:{sb};--sbc:{sbc}"', a)
    b = b.replace('alt=""', f'alt="{alt}"' + (' loading="lazy"' if lazy else ""))
    return a + img + b
LIVE = "https://almasecret.tn"

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

main = f'''  <main class="cs cs--as">
    <div class="cs-progress" aria-hidden="true"><i></i></div>
    <!-- ============ CASE HERO ============ -->
    <section class="cs-hero">
      <canvas class="hero__dots" aria-hidden="true"></canvas>
      <div class="wrap">
        <nav class="cs-crumbs" data-intro style="--d:.05s"><a href="../work.html">Work</a><span>/</span><span>Alma Secret Tunisie</span></nav>
        <p class="eyebrow" data-intro style="--d:.1s">Beauty · Natural cosmetics · Tunisia</p>
        <h1 class="cs-title">
          <span class="line"><span class="line__in" style="--d:.15s">A beauty store built</span></span>
          <span class="line"><span class="line__in" style="--d:.25s">for <span class="accent">cash on delivery</span>.</span></span>
        </h1>
        <p class="cs-lead" data-intro style="--d:.4s">Alma Secret is a Spanish brand of certified natural cosmetics. Its Tunisian distributor needed an online store that works the way Tunisians actually shop: in French, in dinars, paid in cash at the door. We designed the full store and built it on Shopify, from a shop-by-concern homepage to a one-page checkout with no card fields at all.</p>

        <dl class="cs-facts" data-intro style="--d:.5s">
          <div><dt>Client</dt><dd>Alma Secret Tunisie</dd></div>
          <div><dt>Scope</dt><dd>UX and UI design, Shopify development</dd></div>
          <div><dt>Market</dt><dd>Tunisia · French · TND</dd></div>
          <div><dt>Live store</dt><dd><a href="{LIVE}" target="_blank" rel="noopener">almasecret.tn ↗</a></dd></div>
        </dl>
      </div>

      <div class="wrap cs-cover" data-intro style="--d:.6s">
        {phone("cs-cover__phone", I + "m-product.webp", "", "-.1", lazy=False)}
        <div class="vwin cs-win" data-parallax=".06">
          <div class="win__bar"><i></i><i></i><i></i><span class="win__url">almasecret.tn</span></div>
          <img src="{I}hero.webp" alt="Alma Secret Tunisie homepage hero with the anti-aging eye cream" width="1600" height="1000">
        </div>
      </div>
    </section>

    <!-- ============ CHALLENGE ============ -->
    <section data-chapter="Challenge" class="sec cs-brief">
      <div class="wrap cs-split">
        <div data-reveal>
          <p class="eyebrow">The challenge</p>
          <h2 class="h2">Premium skincare, <span class="dim">paid in cash at the door.</span></h2>
        </div>
        <div class="cs-text" data-reveal style="--d:.08s">
          <p>In Tunisia most online orders are paid on delivery, and many shoppers never enter a card online. A standard Shopify checkout asks for exactly what they don't want to give, and a courier needs an exact locality to deliver.</p>
          <p>At the same time Alma Secret is a premium brand: Ecocert-certified, made in Spain, sold in 24+ countries. The store had to feel as calm and clean as the products, and help people pick the right cream without a beauty advisor next to them.</p>
          <ul class="cs-goals">
            <li>A checkout built for cash on delivery</li>
            <li>Help people find the right product fast</li>
            <li>Look like the premium brand it is</li>
          </ul>
        </div>
      </div>
      <div class="wrap">
        <div class="cs-problems">
          <article data-reveal style="--d:0.00s"><h3>No cards, no problem</h3><p>Card fields scare off shoppers who only pay in cash. The checkout had to drop them completely.</p></article>
          <article data-reveal style="--d:0.06s"><h3>Delivery to a locality</h3><p>The courier only delivers to an exact locality from its own directory, so the address form had to match it.</p></article>
          <article data-reveal style="--d:0.12s"><h3>Too many choices</h3><p>Face, body, hair, pregnancy-safe care and packs. Without guidance, people leave before they find their product.</p></article>
        </div>
      </div>
    </section>

    <!-- ============ HOW WE WORKED ============ -->
    <section data-chapter="Process" class="sec cs-chapter">
      <div class="wrap">
        <header class="sec__head sec__head--row" data-reveal>
          <div>
            <p class="eyebrow">How we worked</p>
            <h2 class="h2">Design every screen, <span class="dim">then build it on Shopify.</span></h2>
          </div>
          <p class="sec__lead">Two clear stages. First every page and state was designed on desktop and mobile, then the store was built on Shopify and checked page by page before launch.</p>
        </header>
        <div class="cs-process" data-reveal>
          <div class="cs-phase" style="--i:0"><p class="cs-phase__when">Discovery</p><h3>How Tunisians buy online</h3><p>Payment habits, delivery rules and the courier's address directory shaped the store before any design started.</p><ul><li>Market and payment review</li><li>Courier requirements</li><li>Site map</li></ul></div>
          <div class="cs-phase" style="--i:1"><p class="cs-phase__when">Design</p><h3>Every page and state</h3><p>Homepage, collection with a filter drawer, product page, cart drawer, checkout, FAQ, contact, brand story and newsletter popup.</p><ul><li>Desktop and mobile</li><li>Filter drawer and cart</li><li>COD checkout</li></ul></div>
          <div class="cs-phase" style="--i:2"><p class="cs-phase__when">Build</p><h3>Shopify, no Plus plan</h3><p>Instead of the expensive Shopify Plus plan, a cash-on-delivery form app gives the custom checkout on the standard plan.</p><ul><li>Shopify theme</li><li>COD order form</li><li>Courier locality list</li></ul></div>
          <div class="cs-phase" style="--i:3"><p class="cs-phase__when">Launch</p><h3>QA, page by page</h3><p>Every page, filter and order flow tested on real phones, with fixes closed before the store went live.</p><ul><li>Mobile QA</li><li>Order flow tests</li><li>SEO basics</li></ul></div>
        </div>
      </div>
    </section>

    <!-- ============ NUMBERS ============ -->
    <section class="cs-numbers" aria-label="Alma Secret in numbers">
      <div class="wrap">
        <p class="eyebrow" data-reveal>At a glance</p>
        <div class="cs-bench">
          <div data-reveal><b><span data-count="30000">0</span>+</b><span>Positive reviews of the brand</span><em>From 24+ countries</em></div>
          <div data-reveal style="--d:.06s"><b><span data-count="7">0</span></b><span>Skin and hair concerns to shop by</span><em>Right on the homepage</em></div>
          <div data-reveal style="--d:.12s"><b><span data-count="0">0</span></b><span>Card fields at checkout</span><em>Cash on delivery only</em></div>
          <div data-reveal style="--d:.18s"><b><span data-count="24">0</span>–72h</b><span>Delivery anywhere in Tunisia</span><em>Free from 150 DT</em></div>
        </div>
      </div>
    </section>

    <!-- ============ CHECKOUT ============ -->
    <section data-chapter="Idea" class="sec cs-demo">
      <div class="wrap cs-split">
        <div data-reveal>
          <p class="eyebrow">The idea</p>
          <h2 class="h2">A checkout <span class="dim">people trust.</span></h2>
          <p class="cs-demo__lead">The order form asks only what a courier needs: name, phone, governorate, locality and address. No account, no card, no second step. The total is shown before the button, and the button says exactly what happens next: you pay when the parcel arrives.</p>
        </div>
        <div class="asc" data-reveal style="--d:.1s">
          <p class="asc__title">Finaliser ma commande</p>
          <div class="asc__item"><span class="asc__img"></span><div><b>Crème contour des yeux anti-âge</b><small>Soins visage · 1</small></div><em>76 DT</em></div>
          <div class="asc__grid">
            <div class="asc__f"><span>Nom complet</span><i>Amira Ben Salah</i></div>
            <div class="asc__f"><span>Téléphone</span><i>•• ••• •••</i></div>
            <div class="asc__f"><span>Gouvernorat</span><i>Sousse <u>⌄</u></i></div>
            <div class="asc__f"><span>Localité</span><i>Sahloul <u>⌄</u></i></div>
            <div class="asc__f asc__f--w"><span>Adresse</span><i>Rue, numéro, étage</i></div>
          </div>
          <div class="asc__pay"><span class="asc__dot"></span><div><b>Paiement à la livraison</b><small>Vous payez en espèces à la réception</small></div></div>
          <div class="asc__tot"><span>Livraison</span><b>Offerte dès 150 DT</b></div>
          <div class="asc__btn">Confirmer ma commande · 76 DT</div>
        </div>
      </div>
    </section>

    <!-- ============ GALLERY / STORY ============ -->
    <section data-chapter="Details" class="sec cs-story">
      <div class="wrap">
{row(False, "Shop by concern", "Start from the problem, not the catalogue.", "Right under the hero, a swipeable row of concerns: dry skin, oily skin, anti-aging, damaged hair and more. Each card shows a real face and opens only the products that solve it.", "concern.webp", "Selon vos besoins: shop by skin and hair concern")}
{row(True, "Best-sellers", "Proof on every product card.", "Each card shows the category, star rating with the number of reviews, price in dinars and a quick add-to-cart button, so people can buy straight from the homepage.", "bestsellers.webp", "Nos best-sellers product grid with ratings and prices")}
{row(False, "Signature range", "Tell the story behind the jar.", "The Cleopatra range gets its own block: donkey milk, thermal water, argan and green tea, shown as ingredient chips next to a bright product photo, with one clear link to the whole range.", "signature.webp", "Notre gamme signature: the Cleopatra range")}
{row(True, "Trust", "Real customers from real cities.", "Verified reviews signed with a first name, city and age, from La Marsa to Sousse, followed by the brand's big facts: 30,000+ positive reviews, Ecocert certified and 100% made in Spain.", "reviews.webp", "Customer reviews and brand facts")}
      </div>
    </section>

    <!-- ============ MOBILE ============ -->
    <section class="sec cs-duo">
      <div class="wrap cs-duo__grid">
        <div class="cs-duo__code" data-reveal>
          <p class="eyebrow">Mobile</p>
          <h3>Most orders come from a phone.</h3>
          <p>Swipeable rows instead of long grids, a product page with the price, stock and both buttons in the first scroll, and a cart that says it plainly: two minutes, no bank card, you pay the courier.</p>
          <div class="vwin cs-shot"><div class="win__bar"><i></i><i></i><i></i></div><img src="{I}bestsellers.webp" alt="Best-sellers grid on desktop" loading="lazy" width="1600" height="1000"></div>
        </div>
        <div class="cs-phones" data-reveal style="--d:.1s">
          {phone("cs-phone", I + "m-hero.webp", "Alma Secret mobile homepage", ".08")}
          {phone("cs-phone cs-phone--2", I + "m-cart.webp", "Cash-on-delivery cart on mobile", "-.04")}
        </div>
      </div>
    </section>

    <!-- ============ REEL ============ -->
    <section class="cs-reel" aria-hidden="true">
      <div class="cs-reel__track">{"".join(f'<img src="{I}{x}" alt="" loading="lazy" width="1600" height="1000">' for x in ["concern.webp", "bestsellers.webp", "signature.webp", "reviews.webp", "hero.webp"] * 2)}</div>
    </section>

    <!-- ============ KEY DECISIONS ============ -->
    <section data-chapter="Decisions" class="sec cs-chapter">
      <div class="wrap">
        <header class="sec__head" data-reveal>
          <p class="eyebrow">Key decisions</p>
          <h2 class="h2">Choices made for the market, <span class="dim">not a template.</span></h2>
        </header>
        <div class="cs-dec">
          <div class="cs-dec__row" data-reveal style="--d:0.00s">
            <h3 class="cs-dec__q">How do people pay?</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>The default card checkout.</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>A one-page cash-on-delivery form, on the standard Shopify plan.</p></div>
          </div>
          <div class="cs-dec__row" data-reveal style="--d:0.04s">
            <h3 class="cs-dec__q">How does the address work?</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>Free text fields and a postcode.</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>Governorate and locality picked from the courier's own list, so every parcel can be delivered.</p></div>
          </div>
          <div class="cs-dec__row" data-reveal style="--d:0.08s">
            <h3 class="cs-dec__q">How do shoppers choose?</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>A menu of product types.</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>Shop by concern on the homepage, plus a filter drawer on every collection.</p></div>
          </div>
          <div class="cs-dec__row" data-reveal style="--d:0.12s">
            <h3 class="cs-dec__q">What about delivery options?</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>Several shipping methods to compare.</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>One option, 24–72 hours anywhere in Tunisia, free from 150 DT.</p></div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ RESULT ============ -->
    <section data-chapter="Result" class="sec cs-result">
      <div class="wrap">
        <header class="sec__head" data-reveal>
          <p class="eyebrow">The result</p>
          <h2 class="h2">A premium brand, <span class="dim">bought the local way.</span></h2>
        </header>
        <div class="cs-outcomes">
          <div data-reveal><b>COD only</b><span>a checkout with no card fields and no account to create</span></div>
          <div data-reveal style="--d:.06s"><b>Deliverable</b><span>every order arrives with a locality the courier knows</span></div>
          <div data-reveal style="--d:.12s"><b>Guided</b><span>shoppers start from their concern, not the catalogue</span></div>
          <div data-reveal style="--d:.18s"><b>Standard plan</b><span>a custom checkout without paying for Shopify Plus</span></div>
        </div>
        <div class="cs-got" data-reveal>
          <h3>What Alma Secret <br>walked away with</h3>
          <ul>
            <li>A full store design, desktop and mobile</li>
            <li>A Shopify build in French and dinars</li>
            <li>A one-page cash-on-delivery checkout</li>
            <li>Courier locality selection</li>
            <li>Collection filter drawer and cart drawer</li>
            <li>Product pages with a sticky buy bar on mobile</li>
            <li>FAQ, contact and brand story pages</li>
            <li>Newsletter popup with a first-order discount</li>
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
out = out.replace("<title>AWS Wrap case study | Sorvel Studio</title>", "<title>Alma Secret Tunisie case study | Sorvel Studio</title>")
out = re.sub(r'<meta name="description" content="[^"]*" />', '<meta name="description" content="How Sorvel designed and built the Alma Secret Tunisie Shopify store: natural cosmetics sold in French and dinars, with a cash-on-delivery checkout." />', out, count=1)
out = re.sub(r'href="../css/case.css(\?v=\d+)?"', 'href="../css/case.css?v=15"', out)
out = re.sub(r'<script src="../js/case.js\?v=\d+"></script>', '<script src="../js/case.js?v=12"></script>', out)
open(W + "alma-secret.html", "w").write(out)
print("ok", len(out))
