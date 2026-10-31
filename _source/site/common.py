import os, html
ROOT = "WEBSITE_DIR/"

ARROW = '<svg viewBox="0 0 20 20"><path d="M4 10h11m-4.5-4.5L15 10l-4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>'
DIAG = '<svg viewBox="0 0 20 20"><path d="M5 15 15 5M7 5h8v8" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>'
PLANE = '<svg class="btn__plane" viewBox="0 0 20 20" aria-hidden="true"><path d="M17.5 3 2.8 8.9l4.9 1.7m9.8-7.6-3 13.6-5.2-4.3m8.2-9.3-8.2 9.3m0 0v3.9l2.4-2.1" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>'
FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%230B0C0F'/%3E%3Cpath d='M8 24 16 7l8 17' fill='none' stroke='%23F2EFEA' stroke-width='3.2' stroke-linejoin='round'/%3E%3Ccircle cx='16' cy='19.5' r='2.6' fill='%233B6BFF'/%3E%3C/svg%3E"

# simple line icons (24x24, stroke)
ICON = {
  "web": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M7 6.5h.01M10 6.5h.01"/>',
  "target": '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4"/><path d="M12 12l6-6m0 0h-3m3 0v3"/>',
  "layout": '<rect x="3" y="3" width="7" height="18" rx="1.5"/><rect x="13" y="3" width="8" height="8" rx="1.5"/><rect x="13" y="14" width="8" height="7" rx="1.5"/>',
  "brand": '<path d="M5 19 12 4l7 15"/><circle cx="12" cy="14.5" r="2"/>',
  "move": '<path d="M4 8h12m0 0-3-3m3 3-3 3M20 16H8m0 0 3-3m-3 3 3 3"/>',
  "code": '<path d="M8 7l-5 5 5 5M16 7l5 5-5 5"/>',
  "pen": '<path d="M4 20l4-1 11-11-3-3L5 16l-1 4z"/><path d="M14 6l3 3"/>',
  "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
  "search": '<circle cx="11" cy="11" r="6.5"/><path d="M20 20l-4.2-4.2"/>',
  "bolt": '<path d="M13 3 5 14h6l-1 7 8-11h-6l1-7z"/>',
  "shield": '<path d="M12 3l7 3v6c0 4.4-3 7.6-7 9-4-1.4-7-4.6-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/>',
  "doc": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h6"/>',
  "chat": '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 10h8"/>',
  "figma": '<rect x="7" y="3" width="10" height="6" rx="3"/><rect x="7" y="9" width="10" height="6" rx="3"/><circle cx="14" cy="18" r="3"/><path d="M10 15h-.01"/>',
  "clock": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
  "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.8-3.4 3.3-5 6.5-5s5.7 1.6 6.5 5"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 15c2 .6 3.1 2.3 3.5 5"/>',
  "key": '<circle cx="8" cy="15" r="4.5"/><path d="M11.5 12 20 3.5M17 6.5l2.5 2.5M15 8.5l2 2"/>',
  "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/>',
  "check": '<circle cx="12" cy="12" r="8.5"/><path d="M8 12.5l2.5 2.5L16 9.5"/>',
  "grid": '<rect x="3" y="3" width="8" height="8" rx="1.5"/><rect x="13" y="3" width="8" height="8" rx="1.5"/><rect x="3" y="13" width="8" height="8" rx="1.5"/><rect x="13" y="13" width="8" height="8" rx="1.5"/>',
  "flask": '<path d="M9 3h6M10 3v6L4.5 19a1.5 1.5 0 0 0 1.3 2h12.4a1.5 1.5 0 0 0 1.3-2L14 9V3"/><path d="M7 15h10"/>',
  "link": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
  "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5 12 13l8.5-6.5"/>',
  "heart": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
  "eye": '<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
  "cut": '<circle cx="6" cy="7" r="3"/><circle cx="6" cy="17" r="3"/><path d="M8.5 8.5 20 18M8.5 15.5 20 6"/>',
}
def ico(name, cls="cs-ico"):
    return f'<span class="{cls}"><svg viewBox="0 0 24 24">{ICON[name]}</svg></span>'

SERVICES = [
  ("websites", "Websites", "Webflow, Framer, WordPress", "web"),
  ("landing-pages", "Landing pages & CRO", "One page, one goal", "target"),
  ("product-design", "Product design", "SaaS, dashboards, apps", "layout"),
  ("brand-identity", "Brand identity", "Logo, system, guidelines", "brand"),
  ("migrations", "Website migrations", "Move without losing SEO", "move"),
]

CASES = {
  "valhalla-capital": dict(name="Valhalla Capital", tag="Private credit · Figma + Webflow", img="valhalla/hero.webp", kind=["websites"], chips=["Fintech", "Webflow", "Design system"]),
  "serverscamp": dict(name="ServersCamp", tag="Cloud infrastructure · Site + panel UI", img="serverscamp/hero.webp", kind=["websites", "product"], chips=["SaaS", "Product UI", "Development"]),
  "arlowe-baxter": dict(name="Arlowe Baxter", tag="Property tech · Figma + Webflow", img="arlowe-baxter/hero.webp", kind=["websites"], chips=["Property tech", "Webflow", "Redesign"]),
  "salinas-defense": dict(name="Salinas Defense", tag="Legal · Landing page + Webflow", img="salinas/hero.webp", kind=["landing"], chips=["Legal", "Landing page", "Bilingual"]),
  "awswrap": dict(name="AWS Wrap", tag="Automotive · Design + WordPress", img="awswrap/hero.webp", kind=["websites"], chips=["Local business", "WordPress", "Calculator"]),
  "college-classics": dict(name="College Classics", tag="Fashion · Shopify design + build", img="college-classics/hero.webp", kind=["websites", "ecommerce"], chips=["E-commerce", "Shopify", "Fashion"]),
  "vibz": dict(name="Vibz", tag="Video marketing · Website design", img="vibz/hero.webp", kind=["websites"], chips=["Agency", "Figma", "Desktop + mobile"]),
  "alma-secret": dict(name="Alma Secret Tunisie", tag="Beauty · Shopify design + build", img="alma-secret/hero.webp", kind=["websites", "ecommerce"], chips=["E-commerce", "Shopify", "Cash on delivery"]),
  "ci-isac": dict(name="CI-ISAC Australia", tag="Cyber security · Figma + Webflow", img="ci-isac/hero.webp", kind=["websites"], chips=["Cyber security", "Webflow", "Not-for-profit"]),
  "varsity-city": dict(name="Varsity City", tag="Apparel · Shopify redesign", img="varsity-city/hero.webp", kind=["websites", "ecommerce"], chips=["E-commerce", "Shopify", "Redesign"]),
  "noir": dict(name="NOIR Properties", tag="Real estate · Website design", img="noir/hero.webp", kind=['websites'], chips=['Real estate', 'Spain', 'Desktop + mobile']),
  "skyli": dict(name="Skyli", tag="Fintech · AI expense tracker", img="skyli/hero.webp", kind=['websites', 'landing'], chips=['Fintech', 'AI', 'Pre-launch']),
  "open-select": dict(name="Open Select", tag="Recruitment · B2B website", img="open-select/hero.webp", kind=['websites'], chips=['B2B', 'Recruitment', 'Desktop + mobile']),
  "copliancy": dict(name="Copliancy", tag="SaaS · Compliance platform", img="copliancy/hero.webp", kind=['websites', 'product'], chips=['SaaS', 'Product UI', 'Marketing site']),
  "visit-pemba": dict(name="Visit Pemba", tag="Tourism · Figma + WordPress", img="visit-pemba/hero.webp", kind=['websites'], chips=['Tourism', 'WordPress', 'Live site']),
  "agentur": dict(name="KI-Agentur", tag="AI agency · Website design (DE)", img="agentur/hero.webp", kind=['websites'], chips=['AI', 'German', 'Agency']),
  "mutmachbuch": dict(name="Mutmachbuch", tag="E-commerce · Shopify store design", img="mutmachbuch/hero.webp", kind=['websites', 'ecommerce'], chips=['E-commerce', 'Shopify', 'Live store']),
  "wehike": dict(name="WeHike", tag="Travel · Website design", img="wehike/hero.webp", kind=['websites'], chips=['Travel', 'Booking', 'Desktop + mobile']),
  "waveads": dict(name="AdVoyage", tag="Boat advertising · Figma + Framer", img="waveads/hero.webp", kind=["landing"], chips=["Landing page", "Framer", "Miami"]),
}

def btn_primary(href, label, lg=True, extra=""):
    return (f'<a class="btn btn--primary{" btn--lg" if lg else ""}" href="{href}"{extra}>'
            f'<span class="btn__roll"><span data-text="{label}">{label}</span></span>'
            f'<span class="btn__arrow" aria-hidden="true">{ARROW}{ARROW}</span></a>')
def btn_ghost(href, label, tg=False, lg=True):
    ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
    return (f'<a class="btn btn--ghost{" btn--lg" if lg else ""}" href="{href}"{ext}><span class="btn__fill" aria-hidden="true"></span>'
            f'{PLANE if tg else ""}<span class="btn__roll"><span data-text="{label}">{label}</span></span></a>')

def head(title, desc, p, extra_fonts=""):
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="theme-color" content="#0B0C0F" />
  <link rel="icon" href="{p}img/brand/favicon.svg" type="image/svg+xml" />
  <link rel="icon" href="{p}img/brand/favicon-32.png" sizes="32x32" type="image/png" />
  <link rel="apple-touch-icon" href="{p}img/brand/apple-touch-icon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@500;600&family=Inter:wght@400;500;600{extra_fonts}&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{p}css/style.css" />
  <link rel="stylesheet" href="{p}css/case.css" />
  <link rel="stylesheet" href="{p}css/pages.css?v=21" />\n  <link rel="stylesheet" href="{p}css/svc.css?v=3" />\n  <link rel="stylesheet" href="{p}css/scenes.css?v=9" />
</head>
'''

def mnav(p, active=""):
    def cur(k): return ' aria-current="page"' if k == active else ""
    svc = "".join(f'<a href="{p}services/{s}.html"><i><svg viewBox="0 0 24 24">{ICON[ic]}</svg></i><b>{t.replace("&", "&amp;")}</b><small>{d}</small></a>' for s, t, d, ic in SERVICES)
    links = [("work", "work.html", "Work"), ("pricing", "pricing.html", "Pricing"), ("process", "process.html", "Process"), ("about", "about.html", "About"), ("reviews", "reviews.html", "Reviews")]
    rows = "".join(f'<li style="--i:{n + 2}"><a class="mnav__link" href="{p}{h}"{cur(k)}><span class="mnav__n">0{n + 2}</span><span class="mnav__t">{t}</span></a></li>' for n, (k, h, t) in enumerate(links))
    return f'''  <div class="mnav" id="mnav" aria-label="Menu" inert>
    <div class="mnav__bg" aria-hidden="true"></div>
    <div class="mnav__in">
      <ul class="mnav__list">
        <li style="--i:1"><button class="mnav__link mnav__acc" type="button" aria-expanded="false" aria-controls="mnav-svc"><span class="mnav__n">01</span><span class="mnav__t">Services</span><span class="mnav__pm" aria-hidden="true"></span></button>
          <div class="mnav__sub" id="mnav-svc"><div><div class="mnav__svc">{svc}</div></div></div></li>
        {rows}
      </ul>
      <div class="mnav__foot" style="--i:8">
        <p class="mnav__status"><span class="status__dot" aria-hidden="true"></span> Replies in about 10 minutes</p>
        <a class="btn btn--primary btn--lg mnav__cta" href="{p}contact.html"><span class="btn__roll"><span data-text="Start a project">Start a project</span></span><span class="btn__arrow" aria-hidden="true"><svg viewBox="0 0 20 20"><path d="M4 10h11m-4.5-4.5L15 10l-4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8"/></svg><svg viewBox="0 0 20 20"><path d="M4 10h11m-4.5-4.5L15 10l-4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8"/></svg></span></a>
        <div class="mnav__contact"><a href="https://t.me/tanasiychuk8" target="_blank" rel="noopener">Telegram</a><a href="mailto:hello@sorvel.agency">hello@sorvel.agency</a></div>
      </div>
    </div>
  </div>
'''

def nav(p, active=""):
    def cur(k): return ' class="is-current"' if k == active else ""
    menu = "".join(f'<a href="{p}services/{s}.html"><i><svg viewBox="0 0 24 24">{ICON[ic]}</svg></i><b>{t.replace("&", "&amp;")}</b><small>{d}</small></a>' for s, t, d, ic in SERVICES)
    return f'''  <header class="nav" data-intro style="--d:0s">
    <div class="nav__inner">
      <a class="nav__logo" href="{p}index.html" aria-label="Sorvel Studio home">
        <img src="{p}img/brand/logo.svg" alt="Sorvel" width="296" height="94">
      </a>
      <nav class="nav__links" aria-label="Main">
        <div class="nav__dd"><a href="{p}index.html#services"{cur("services")}>Services <svg viewBox="0 0 10 10" aria-hidden="true"><path d="M1.5 3.5 5 7l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.4"/></svg></a><div class="nav__menu">{menu}</div></div>
        <a href="{p}work.html"{cur("work")}>Work</a>
        <a href="{p}pricing.html"{cur("pricing")}>Pricing</a>
        <a href="{p}process.html"{cur("process")}>Process</a>
        <a href="{p}about.html"{cur("about")}>About</a>
      </nav>
      <a class="btn btn--primary btn--small nav__cta" href="{p}contact.html">
        <span class="btn__roll"><span data-text="Start a project">Start a project</span></span>
      </a>
      <button class="nav__burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mnav"><span class="nav__bl" aria-hidden="true"><b>Menu</b><b>Close</b></span><span class="nav__ic" aria-hidden="true"><i></i><i></i></span></button>
    </div>
  </header>
{mnav(p, active)}'''

def footer(p):
    svc = "".join(f'<a href="{p}services/{s}.html">{t.replace("&", "&amp;")}</a>' for s, t, d, ic in SERVICES)
    return f'''  <footer class="foot">
    <div class="wrap">
      <div class="foot__top">
        <div class="foot__brand">
          <a class="foot__logo" href="{p}index.html" aria-label="Sorvel Studio home"><img src="{p}img/brand/logo.svg" alt="Sorvel" width="296" height="94" loading="lazy"></a>
          <p class="foot__tag">Design, build and grow <br>with one senior team.</p>
          <p class="foot__time"><span class="status__dot" aria-hidden="true"></span> Our time <b class="clock">--:--</b> CET · replies in ~10 min</p>
        </div>
        <nav class="foot__cols" aria-label="Footer">
          <div><h4>Services</h4>{svc}</div>
          <div><h4>Studio</h4><a href="{p}work.html">Work</a><a href="{p}pricing.html">Pricing</a><a href="{p}process.html">Process</a><a href="{p}about.html">About</a><a href="{p}reviews.html">Reviews</a></div>
          <div><h4>Contact</h4><a href="mailto:hello@sorvel.agency">hello@sorvel.agency</a><a href="https://t.me/tanasiychuk8" target="_blank" rel="noopener">Telegram</a><a href="{p}contact.html">Start a project</a></div>
          <div><h4>Follow</h4><a href="https://www.linkedin.com/company/sorvel" target="_blank" rel="noopener">LinkedIn</a><a href="https://www.behance.net/tanasiichuk8" target="_blank" rel="noopener">Behance</a><a href="https://dribbble.com/koliafree11" target="_blank" rel="noopener">Dribbble</a></div>
        </nav>
      </div>
      <div class="foot__bottom"><span>© <span class="year">2026</span> Sorvel Studio</span><span class="foot__legal"><a href="{p}privacy.html">Privacy</a><a href="{p}terms.html">Terms</a></span><a href="#top">Back to top ↑</a></div>
    </div>
  </footer>
'''

def scripts(p, extra=("pages", "fx", "svc", "scenes")):
    s = f'  <script src="{p}js/dots.js"></script>\n  <script src="{p}js/main.js?v=16"></script>\n  <script src="{p}js/case.js"></script>\n'
    for e in extra: s += f'  <script src="{p}js/{e}.js?v=16"></script>\n'
    return s

def hero(crumb, eyebrow, lines, lead, actions="", center=False, p="", visual=""):
    ls = "\n".join(f'          <span class="line"><span class="line__in" style="--d:{.15 + i * .1:.2f}s">{l}</span></span>' for i, l in enumerate(lines))
    crumbs = f'<nav class="cs-crumbs" data-intro style="--d:.05s"><a href="{p}index.html">Home</a><span>/</span>{crumb}</nav>'
    body = (f'<div class="pg-hero__grid"><p class="cs-lead" data-intro style="--d:.45s">{lead}</p>'
            f'<div class="pg-hero__actions" data-intro style="--d:.55s">{actions}</div></div>') if not center else \
           f'<p class="cs-lead" data-intro style="--d:.45s">{lead}</p>' + (f'<div class="pg-hero__actions" data-intro style="--d:.55s;justify-content:center;margin-top:36px;justify-self:auto">{actions}</div>' if actions else "")
    copy = f'''{crumbs}
        <p class="eyebrow" data-intro style="--d:.1s">{eyebrow}</p>
        <h1 class="cs-title">
{ls}
        </h1>
        {body}'''
    if visual:
        inner = f'<div class="pg-hero__split"><div class="pg-hero__copy">{copy}</div><div class="pg-hero__vis" data-intro style="--d:.35s">{visual}</div></div>'
    else:
        inner = copy
    return f'''    <section class="pg-hero{" pg-hero--center" if center else ""}{" pg-hero--vis" if visual else ""}" id="top">
      <canvas class="hero__dots" aria-hidden="true"></canvas>
      <div class="wrap">
        {inner}
      </div>
    </section>
'''

def sec_head(eyebrow, title, lead="", row=True, chapter=""):
    if row and lead:
        return f'''        <header class="sec__head sec__head--row" data-reveal>
          <div><p class="eyebrow">{eyebrow}</p><h2 class="h2">{title}</h2></div>
          <p class="sec__lead">{lead}</p>
        </header>'''
    return f'''        <header class="sec__head" data-reveal>
          <p class="eyebrow">{eyebrow}</p><h2 class="h2">{title}</h2>{f'<p class="sec__lead">{lead}</p>' if lead else ""}
        </header>'''

def faq(items, title="Questions, answered", eyebrow="FAQ"):
    acc = "\n".join(f'          <details class="acc__item"{" open" if i == 0 else ""}><summary>{q}</summary><div class="acc__a"><p>{a}</p></div></details>' for i, (q, a) in enumerate(items))
    return f'''    <section class="sec faq" data-chapter="FAQ">
      <div class="wrap faq__grid">
        <div class="faq__side" data-reveal>
          <p class="eyebrow">{eyebrow}</p>
          <h2 class="h2">{title}</h2>
          <div class="ask">
            <p>Something else on your mind? Write to us and get a reply in about 10 minutes.</p>
            <a href="mailto:hello@sorvel.agency">hello@sorvel.agency <span aria-hidden="true">→</span></a>
            <a href="https://t.me/tanasiychuk8" target="_blank" rel="noopener">Telegram: @tanasiychuk8 <span aria-hidden="true">→</span></a>
          </div>
        </div>
        <div class="acc" data-reveal>
{acc}
        </div>
      </div>
    </section>
'''

def cta(p, eyebrow="Your project next", title="Tell us what <br>you're building.", lead=""):
    return f'''    <section class="cs-next pg-cta">
      <div class="wrap" data-reveal>
        <p class="eyebrow">{eyebrow}</p>
        <h2 class="cta__title">{title}</h2>
        {f'<p class="cta__lead">{lead}</p>' if lead else ""}
        <div class="pg-cta__row">
          <div class="pg-cta__btns">
            {btn_primary(p + "contact.html", "Start a project")}
            {btn_ghost("https://t.me/tanasiychuk8", "Write on Telegram", tg=True)}
          </div>
          <div class="pg-cta__mail"><span>Or write directly</span><a href="mailto:hello@sorvel.agency">hello@sorvel.agency</a><a href="https://t.me/tanasiychuk8" target="_blank" rel="noopener">@tanasiychuk8</a></div>
        </div>
      </div>
    </section>
'''

# preview styling per project: (tint colour, address-bar label, phone screenshot or None)
PREVIEW = {
  "valhalla-capital": ("#b08d4a", "valhallacap.com", "valhalla/m-hero.webp"),
  "serverscamp": ("#2fbf71", "serverscamp.com", "serverscamp/m-hero.webp"),
  "arlowe-baxter": ("#4f7cff", "arlowebaxter.com", "arlowe-baxter/m-hero.webp"),
  "salinas-defense": ("#c9a24a", "salinasdefense.com", "salinas/m-hero.webp"),
  "awswrap": ("#e0352b", "awswrap.com", "awswrap/m-hero.webp"),
  "college-classics": ("#2a55c9", "College Classics · Shopify", "college-classics/m-hero.webp"),
  "vibz": ("#b23cff", "Vibz · Figma", "vibz/m-home.webp"),
  "alma-secret": ("#3f8fa8", "almasecret.tn", "alma-secret/m-product.webp"),
  "ci-isac": ("#e07a1f", "ci-isac.org.au · Figma", None),
  "varsity-city": ("#2f7a4f", "Varsity City · Figma", None),
  "noir": ("#1c1f4a", "NOIR · Figma", "noir/m-card.webp"),
  "skyli": ("#e86a5e", "Skyli · Figma", "skyli/m-card.webp"),
  "open-select": ("#0f9480", "Open Select · Figma", "open-select/m-card.webp"),
  "copliancy": ("#2e9e5b", "Copliancy · Figma", "copliancy/m-card.webp"),
  "visit-pemba": ("#1a8a8a", "visitpemba.tz", "visit-pemba/m-card.webp"),
  "agentur": ("#5b5bf0", "KI-Agentur · Figma", "agentur/m-card.webp"),
  "mutmachbuch": ("#6d3ad6", "mutmachbuch.com", "mutmachbuch/m-card.webp"),
  "wehike": ("#ef5a24", "WeHike · Figma", "wehike/m-card.webp"),
  "waveads": ("#2aa7c9", "advoyage · Miami Beach", None),
}

HIDDEN = {"serverscamp"}  # case studies hidden from the site for now (pages still exist, just not linked)

def pcard(slug, p, wide=False, kind=None):
    if slug in HIDDEN: return ""
    c = CASES[slug]
    tint, url, phone = PREVIEW.get(slug, ("#3B6BFF", c["name"], None))
    chips = "".join(f"<span>{x}</span>" for x in c["chips"])
    k = f' data-kind="{" ".join(c["kind"])}"' if kind else ""
    ph = (f'<div class="pv-phone"><div class="pv-phone__scr"><img src="{p}img/work/{phone}" alt="" loading="lazy" width="393" height="852"></div><span class="pv-phone__isl"></span></div>') if phone else ""
    return f'''          <a class="pcard{" pcard--wide" if wide else ""}{" has-phone" if phone else ""}" href="{p}work/{slug}.html"{k} style="--tint:{tint}" data-reveal>
            <div class="pcard__media">
              <div class="pv-win"><div class="pv-bar"><i></i><i></i><i></i><span>{url}</span></div><div class="pv-shot"><img src="{p}img/work/{c["img"]}" alt="{c["name"]} website" loading="lazy" width="1600" height="1000"></div></div>
              {ph}
            </div>
            <div class="pcard__body"><h3>{c["name"]}</h3><p>{c["tag"]}</p><span class="pcard__go" aria-hidden="true">{DIAG}</span><div class="pcard__tags">{chips}</div></div>
          </a>'''

def page(path, title, desc, active, body, p, extra_js=("pages", "fx", "svc", "scenes"), main_cls="cs inner", dock=True):
    out = head(title, desc, p) + '<body class="case-page">\n' + nav(p, active)
    out += f'  <main class="{main_cls}">\n    <div class="cs-progress" aria-hidden="true"><i></i></div>\n'
    pass  # section dock removed
    out += body + "  </main>\n\n" + footer(p) + "\n" + scripts(p, extra_js) + "</body>\n</html>\n"
    full = ROOT + path
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(out)
    print("wrote", path, len(out))
