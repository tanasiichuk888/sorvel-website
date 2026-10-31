import re, sys, html
W = "WEBSITE_DIR/work/"

CASES = {
  "valhalla-capital": ("Valhalla Capital Partners", "Private credit · Figma + Webflow", "../img/work/valhalla/hero.webp"),
  "serverscamp": ("ServersCamp", "Cloud infrastructure · Site + panel", "../img/work/serverscamp/hero.webp"),
  "arlowe-baxter": ("Arlowe Baxter", "Property tech · Figma + Webflow", "../img/work/arlowe-baxter/hero.webp"),
  "salinas-defense": ("Salinas Defense", "Legal · Landing page + Webflow", "../img/work/salinas/hero.webp"),
  "awswrap": ("AWS Wrap", "Automotive · Design + WordPress", "../img/work/awswrap/hero.webp"),
  "college-classics": ("College Classics", "Fashion · Shopify design + build", "../img/work/college-classics/hero.webp"),
  "vibz": ("Vibz", "Video marketing · Website design", "../img/work/vibz/hero.webp"),
  "alma-secret": ("Alma Secret Tunisie", "Beauty · Shopify design + build", "../img/work/alma-secret/hero.webp"),
  "ci-isac": ("CI-ISAC Australia", "Cyber security · Figma + Webflow", "../img/work/ci-isac/hero.webp"),
  "varsity-city": ("Varsity City", "Apparel · Shopify redesign", "../img/work/varsity-city/hero.webp"),
  "noir": ("NOIR Properties", "Real estate · Website design", "../img/work/noir/hero.webp"),
  "skyli": ("Skyli", "Fintech · AI expense tracker", "../img/work/skyli/hero.webp"),
  "open-select": ("Open Select", "Recruitment · B2B website", "../img/work/open-select/hero.webp"),
  "copliancy": ("Copliancy", "SaaS · Compliance platform", "../img/work/copliancy/hero.webp"),
  "visit-pemba": ("Visit Pemba", "Tourism · Figma + WordPress", "../img/work/visit-pemba/hero.webp"),
  "agentur": ("KI-Agentur", "AI agency · Website design (DE)", "../img/work/agentur/hero.webp"),
  "mutmachbuch": ("Mutmachbuch", "E-commerce · Shopify store design", "../img/work/mutmachbuch/hero.webp"),
  "wehike": ("WeHike", "Travel · Website design", "../img/work/wehike/hero.webp"),
  "waveads": ("AdVoyage", "Boat advertising · Figma + Framer", "../img/work/waveads/hero.webp"),
}
ORDER = ["visit-pemba", "skyli", "open-select", "mutmachbuch", "copliancy", "agentur", "noir", "wehike", "vibz", "alma-secret", "ci-isac", "varsity-city", "waveads", "college-classics", "valhalla-capital", "serverscamp", "arlowe-baxter", "salinas-defense", "awswrap"]

def problems(items):
    cards = "\n".join(f'          <article data-reveal style="--d:{i*.06:.2f}s"><h3>{t}</h3><p>{p}</p></article>' for i, (t, p) in enumerate(items))
    return f'''      <div class="wrap">
        <div class="cs-problems">
{cards}
        </div>
      </div>
'''

def process(title, lead, phases):
    ph = []
    for i, (when, h, p, lis) in enumerate(phases):
        li = "".join(f"<li>{x}</li>" for x in lis)
        ph.append(f'          <div class="cs-phase" style="--i:{i}"><p class="cs-phase__when">{when}</p><h3>{h}</h3><p>{p}</p><ul>{li}</ul></div>')
    body = "\n".join(ph)
    return f'''
    <!-- ============ HOW WE WORKED ============ -->
    <section class="sec cs-chapter">
      <div class="wrap">
        <header class="sec__head sec__head--row" data-reveal>
          <div>
            <p class="eyebrow">How we worked</p>
            <h2 class="h2">{title}</h2>
          </div>
          <p class="sec__lead">{lead}</p>
        </header>
        <div class="cs-process" data-reveal>
{body}
        </div>
      </div>
    </section>
'''

def decisions(title, rows):
    r = []
    for i, (q, no, yes) in enumerate(rows):
        r.append(f'''          <div class="cs-dec__row" data-reveal style="--d:{i*.04:.2f}s">
            <h3 class="cs-dec__q">{q}</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>{no}</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>{yes}</p></div>
          </div>''')
    body = "\n".join(r)
    return f'''
    <!-- ============ KEY DECISIONS ============ -->
    <section class="sec cs-chapter">
      <div class="wrap">
        <header class="sec__head" data-reveal>
          <p class="eyebrow">Key decisions</p>
          <h2 class="h2">{title}</h2>
        </header>
        <div class="cs-dec">
{body}
        </div>
      </div>
    </section>
'''

def got(title, items):
    li = "\n".join(f"            <li>{x}</li>" for x in items)
    return f'''        <div class="cs-got" data-reveal>
          <h3>{title}</h3>
          <ul>
{li}
          </ul>
        </div>
'''

ARROW = '<svg viewBox="0 0 20 20"><path d="M4 10h11m-4.5-4.5L15 10l-4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>'

def more(slug):
    cards = []
    for i, s in enumerate([ORDER[(ORDER.index(slug) + n) % len(ORDER)] for n in (1, 2, 3)]):
        name, tag, img = CASES[s]
        cards.append(f'''          <a class="cs-more__card" href="{s}.html" data-reveal style="--d:{i*.06:.2f}s">
            <div class="cs-more__img"><img src="{img}" alt="{name} website" loading="lazy" width="800" height="500"></div>
            <div class="cs-more__body"><div><h3>{name}</h3><p>{tag}</p></div><span aria-hidden="true">→</span></div>
          </a>''')
    body = "\n".join(cards)
    return f'''    <!-- ============ MORE WORK ============ -->
    <section class="cs-more">
      <div class="wrap">
        <header class="sec__head sec__head--row" data-reveal>
          <div>
            <p class="eyebrow">More work</p>
            <h2 class="h2">Other projects <br>we're proud of.</h2>
          </div>
        </header>
        <div class="cs-more__grid">
{body}
        </div>
      </div>
    </section>

    <!-- ============ NEXT ============ -->
    <section class="cs-next">
      <div class="wrap cs-next__inner" data-reveal>
        <div>
          <p class="eyebrow">Your project next</p>
          <h2 class="cta__title">Let's make yours <br>the next case study.</h2>
        </div>
        <div class="hero__actions">
          <a class="btn btn--primary btn--lg" href="../index.html#contact">
            <span class="btn__roll"><span data-text="Start a project">Start a project</span></span>
            <span class="btn__arrow" aria-hidden="true">{ARROW}{ARROW}</span>
          </a>
          <a class="btn btn--ghost btn--lg" href="https://t.me/tanasiychuk8" target="_blank" rel="noopener">
            <span class="btn__fill" aria-hidden="true"></span>
            <span class="btn__roll"><span data-text="Write on Telegram">Write on Telegram</span></span>
          </a>
        </div>
      </div>
    </section>
  </main>'''

def apply(slug, D):
    p = W + slug + ".html"
    s = open(p).read()
    # 1. problems inside the challenge section (after the split wrap)
    i = s.index('<section class="sec cs-brief">')
    j = s.index("    </section>", i)
    s = s[:j] + problems(D["problems"]) + s[j:]
    # 2. process right after the challenge section
    j = s.index("    </section>", i) + len("    </section>\n")
    s = s[:j] + process(*D["process"]) + s[j:]
    # 3. decisions before the quote (if any) or the result
    anchor = "    <!-- ============ QUOTE" if "<!-- ============ QUOTE" in s else "    <!-- ============ RESULT"
    k = s.index(anchor)
    s = s[:k] + decisions(*D["decisions"]).lstrip("\n") + "\n" + s[k:]
    # 4. what the client got, inside the result section
    k = s.index('<section class="sec cs-result">')
    k2 = s.index("      </div>\n    </section>", k)
    s = s[:k2] + got(*D["got"]) + s[k2:]
    # 5. replace next-case with more work + CTA
    a = s.index("    <!-- ============ NEXT ============ -->")
    b = s.index("  </main>") + len("  </main>")
    s = s[:a] + more(slug) + s[b:]
    open(p, "w").write(s)
    print("ok", slug)

def remore(slug):
    p = W + slug + ".html"; s = open(p).read()
    a = s.index("    <!-- ============ MORE WORK ============ -->")
    b = s.index("  </main>") + len("  </main>")
    s = s[:a] + more(slug) + s[b:]
    open(p, "w").write(s); print("more", slug)

IMGDIR = {"valhalla-capital": "valhalla", "serverscamp": "serverscamp", "arlowe-baxter": "arlowe-baxter", "salinas-defense": "salinas", "awswrap": "awswrap"}

HIDDEN = {"serverscamp"}  # keep in sync with site/common.py

def more_list(slug):
    rows = []
    vis = [x for x in ORDER if x not in HIDDEN or x == slug]
    for i, s in enumerate([vis[(vis.index(slug) + n) % len(vis)] for n in (1, 2, 3)]):
        name, tag, img = CASES[s]
        rows.append(f'''          <a class="cs-more__row" href="{s}.html" data-img="{img}" data-reveal style="--d:{i*.06:.2f}s">
            <span class="cs-more__thumb"><img src="{img}" alt="" loading="lazy" width="800" height="500"></span>
            <span class="cs-more__name">{name}</span>
            <span class="cs-more__tag">{tag}</span>
            <span class="cs-more__go" aria-hidden="true"><svg viewBox="0 0 20 20"><path d="M5 15 15 5M7 5h8v8" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></span>
          </a>''')
    body = "\n".join(rows)
    return f'''    <!-- ============ MORE WORK ============ -->
    <section class="cs-more">
      <div class="wrap">
        <header class="cs-more__head" data-reveal>
          <p class="eyebrow">More work</p>
          <a class="cs-more__all" href="../work.html">All projects <span aria-hidden="true">→</span></a>
        </header>
        <div class="cs-more__list">
{body}
        </div>
      </div>
      <div class="cs-more__float" aria-hidden="true"><img alt=""></div>
    </section>

'''
