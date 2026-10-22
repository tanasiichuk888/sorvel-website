import re
W = "WEBSITE_DIR/work/"
src = open(W + "awswrap.html").read()
src = src.replace('<img fetchpriority="low" ', '<img ')  # undo the SEO pass tweak so templates match
src = re.sub(r'<title>AWS Wrap[^<]*</title>', '<title>AWS Wrap case study | Sorvel Studio</title>', src)  # restore the template title
I = "../img/work/vibz/"
phone_tpl = re.search(r'(<div class="cs-cover__phone iphone".*?<img src=")[^"]+(" alt="" width="393" height="852"></span></span></span></div>)', src, re.S)
def phone(cls, img, alt, par, lazy=True, sb="#3f7d99", sbc="#fff"):
    a, b = phone_tpl.group(1), phone_tpl.group(2)
    a = re.sub(r'class="cs-cover__phone iphone" data-parallax="[^"]*"', f'class="{cls} iphone" data-parallax="{par}"', a)
    a = re.sub(r'--sb:[^;]+;--sbc:[^"]+"', f'--sb:{sb};--sbc:{sbc}"', a)
    b = b.replace('alt=""', f'alt="{alt}"' + (' loading="lazy"' if lazy else ""))
    return a + img + b

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

main = f'''  <main class="cs cs--vb">
    <div class="cs-progress" aria-hidden="true"><i></i></div>
    <section class="cs-hero">
      <canvas class="hero__dots" aria-hidden="true"></canvas>
      <div class="wrap">
        <nav class="cs-crumbs" data-intro style="--d:.05s"><a href="../work.html">Work</a><span>/</span><span>Vibz</span></nav>
        <p class="eyebrow" data-intro style="--d:.1s">Marketing agency · Short-form video · Switzerland</p>
        <h1 class="cs-title">
          <span class="line"><span class="line__in" style="--d:.15s">Short videos,</span></span>
          <span class="line"><span class="line__in" style="--d:.25s">a site with <span class="accent">vibe</span>.</span></span>
        </h1>
        <p class="cs-lead" data-intro style="--d:.4s">Vibz is a Swiss agency that makes short-form videos for brands: script, filming, editing and posting, all from one team. We designed their German-language website in Figma: seven pages on desktop and mobile, built around one action, booking a free consultation.</p>
        <dl class="cs-facts" data-intro style="--d:.5s">
          <div><dt>Client</dt><dd>Vibz</dd></div>
          <div><dt>Scope</dt><dd>Website design, desktop and mobile</dd></div>
          <div><dt>Platform</dt><dd>Figma</dd></div>
          <div><dt>Pages</dt><dd>7 pages, 13 layouts</dd></div>
        </dl>
      </div>
      <div class="wrap cs-cover" data-intro style="--d:.6s">
        {phone("cs-cover__phone", I + "m-home.webp", "", "-.1", lazy=False, sb="#ffffff", sbc="#0b0c0f")}
        <div class="vwin cs-win" data-parallax=".06">
          <div class="win__bar"><i></i><i></i><i></i><span class="win__url">Vibz · Homepage</span></div>
          <img src="{I}hero.webp" alt="Vibz homepage hero: Mehr Reichweite? Easy!" width="1600" height="1000">
        </div>
      </div>
    </section>

    <section data-chapter="Challenge" class="sec cs-brief">
      <div class="wrap cs-split">
        <div data-reveal>
          <p class="eyebrow">The challenge</p>
          <h2 class="h2">An agency for TikTok <span class="dim">can't look like a law firm.</span></h2>
        </div>
        <div class="cs-text" data-reveal style="--d:.08s">
          <p>Vibz sells short, catchy videos for Instagram, TikTok and YouTube. Their buyers are Swiss business owners and HR teams who still think in print ads and job boards, and need to be convinced that 30-second videos actually bring customers and candidates.</p>
          <p>The site had to feel as fast and energetic as the videos, explain three services without long text, back the claims with numbers, and lead every visitor to the same next step: a free consultation.</p>
          <ul class="cs-goals">
            <li>Energy of social media, clarity of a business site</li>
            <li>Proof that short video works</li>
            <li>One clear action on every page</li>
          </ul>
        </div>
      </div>
      <div class="wrap">
        <div class="cs-problems">
          <article data-reveal style="--d:0.00s"><h3>A sceptical buyer</h3><p>Many clients still trust traditional marketing. The site has to show why short video wins, not just say it.</p></article>
          <article data-reveal style="--d:0.06s"><h3>Three services</h3><p>Short video marketing, social recruiting and corporate video, each with its own buyer and questions.</p></article>
          <article data-reveal style="--d:0.12s"><h3>Mobile first</h3><p>Their audience lives on phones, so every page needed a mobile layout designed, not squeezed.</p></article>
        </div>
      </div>
    </section>

    <section data-chapter="Process" class="sec cs-chapter">
      <div class="wrap">
        <header class="sec__head sec__head--row" data-reveal>
          <div>
            <p class="eyebrow">How we worked</p>
            <h2 class="h2">Homepage first, <span class="dim">then every page on two screens.</span></h2>
          </div>
          <p class="sec__lead">The homepage set the visual language, then the inner pages followed in the same system, each one designed separately for desktop and mobile.</p>
        </header>
        <div class="cs-process" data-reveal>
          <div class="cs-phase" style="--i:0"><p class="cs-phase__when">Structure</p><h3>What a buyer needs to hear</h3><p>Problems, services, proof, process, comparison, team and FAQ, in the order a sceptical buyer asks.</p><ul><li>Site map</li><li>Homepage story</li><li>German copy structure</li></ul></div>
          <div class="cs-phase" style="--i:1"><p class="cs-phase__when">Style</p><h3>Purple to pink, bold type</h3><p>A violet-to-magenta gradient from the logo, heavy rounded headlines and soft glows, so the site feels like the feed it sells.</p><ul><li>Colour and type</li><li>Gradient system</li><li>Components</li></ul></div>
          <div class="cs-phase" style="--i:2"><p class="cs-phase__when">Desktop</p><h3>Six page designs</h3><p>Home, About, Portfolio, Blog, an article template and Contact, all with the same consultation banner and footer.</p><ul><li>Homepage</li><li>Inner pages</li><li>Article template</li></ul></div>
          <div class="cs-phase" style="--i:3"><p class="cs-phase__when">Mobile</p><h3>Every page, again</h3><p>A separate mobile layout for each page plus the full-screen menu, with thumb-sized buttons and swipeable rows.</p><ul><li>Mobile pages</li><li>Mobile menu</li><li>Handoff in Figma</li></ul></div>
        </div>
      </div>
    </section>

    <section class="cs-numbers" aria-label="Project in numbers">
      <div class="wrap">
        <p class="eyebrow" data-reveal>At a glance</p>
        <div class="cs-bench">
          <div data-reveal><b><span data-count="7">0</span></b><span>Pages designed</span><em>Home, about, portfolio, blog, article, contact, menu</em></div>
          <div data-reveal style="--d:.06s"><b><span data-count="13">0</span></b><span>Layouts in Figma</span><em>Desktop and mobile</em></div>
          <div data-reveal style="--d:.12s"><b><span data-count="3">0</span></b><span>Services explained</span><em>Video, recruiting, corporate</em></div>
          <div data-reveal style="--d:.18s"><b><span data-count="1">0</span></b><span>Main action everywhere</span><em>Free consultation</em></div>
        </div>
      </div>
    </section>

    <section data-chapter="Details" class="sec cs-story">
      <div class="wrap">
{row(False, "Hero", "Mehr Reichweite? Easy!", "A big two-colour headline, one line on what Vibz does, the free consultation button and a Google rating. A real person on the right and a growth badge make the promise concrete from the first second.", "hero.webp", "Vibz homepage hero")}
{row(True, "Problems", "Your problems, our solution.", "A toggle switches the same three cards between the buyer's problems and how Vibz solves them: low visibility, hard-to-reach audiences and weak engagement. One click turns pain into an offer.", "challenges.webp", "Aktuelle Herausforderungen with problem and solution toggle")}
{row(False, "Services", "Three services, one panel.", "Short video marketing, social recruiting and corporate video sit as tabs. Each shows its key benefits and what Vibz does differently, from full-service production to 7-day delivery.", "expertise.webp", "Entdecke unsere Expertise service tabs")}
{row(True, "Proof", "Data instead of adjectives.", "A chart of monthly users and hours per platform, plus three stat cards on short-form video growth, shows the buyer why the format matters before asking for a meeting.", "social.webp", "Die Macht der Sozialen Medien chart")}
{row(False, "Comparison", "Short video vs. traditional marketing.", "A side-by-side list in the brand gradient against a plain white card: cost, engagement, reach, targeting and speed. The difference is visible before you read a word.", "compare.webp", "Vibz: Dein Game-Changer im Marketing comparison")}
{row(True, "Inner pages", "The same energy, every page.", "About with mission and core values, a portfolio of video case studies, a blog with an article template and a contact page with three ways to reach the team, all ending with the same consultation banner.", "about.webp", "We are Vibz about page")}
      </div>
    </section>

    <section class="sec cs-duo">
      <div class="wrap cs-duo__grid">
        <div class="cs-duo__code" data-reveal>
          <p class="eyebrow">Mobile</p>
          <h3>Designed for the thumb.</h3>
          <p>Each page has its own mobile layout: stacked hero with the button in reach, swipeable service and team rows, and a full-screen menu with the consultation button always at the bottom.</p>
          <div class="vwin cs-shot"><div class="win__bar"><i></i><i></i><i></i></div><img src="{I}faq.webp" alt="FAQ section on desktop" loading="lazy" width="1600" height="1000"></div>
        </div>
        <div class="cs-phones" data-reveal style="--d:.1s">
          {phone("cs-phone", I + "m-home_menu.webp", "Vibz mobile menu", ".08", sb="#ffffff", sbc="#0b0c0f")}
          {phone("cs-phone cs-phone--2", I + "m-about_us.webp", "Vibz about page on mobile", "-.04", sb="#ffffff", sbc="#0b0c0f")}
        </div>
      </div>
    </section>

    <section class="sec cs-duo">
      <div class="wrap cs-duo__grid">
        <div class="cs-duo__code" data-reveal>
          <p class="eyebrow">The whole homepage</p>
          <h3>One scroll, from hook to consultation.</h3>
          <p>Hero, logos, testimonial, problems, services, social media data, process, comparison, team, FAQ, insights and the final call to action. Every section answers the next doubt a buyer has.</p>
          <div class="vwin cs-shot"><div class="win__bar"><i></i><i></i><i></i></div><img src="{I}team.webp" alt="Das Vibz Experten Team" loading="lazy" width="1600" height="1000"></div>
        </div>
        <div class="wa-scroll" data-reveal style="--d:.1s">
          <div class="vwin"><div class="win__bar"><i></i><i></i><i></i><span class="win__url">Homepage design</span></div>
            <div class="wa-scroll__vp"><img src="{I}full.webp" alt="Full Vibz homepage design, top to bottom" loading="lazy" width="1000" height="7971"></div>
          </div>
        </div>
      </div>
    </section>

    <section class="cs-reel" aria-hidden="true">
      <div class="cs-reel__track">{"".join(f'<img src="{I}{x}" alt="" loading="lazy" width="1600" height="1000">' for x in ["process.webp", "values.webp", "portfolio.webp", "blog.webp", "article.webp", "contact.webp", "insights.webp"] * 2)}</div>
    </section>

    <section data-chapter="Decisions" class="sec cs-chapter">
      <div class="wrap">
        <header class="sec__head" data-reveal>
          <p class="eyebrow">Key decisions</p>
          <h2 class="h2">Choices that turn a scroll <span class="dim">into a consultation.</span></h2>
        </header>
        <div class="cs-dec">
          <div class="cs-dec__row" data-reveal style="--d:0.00s"><h3 class="cs-dec__q">How do you open?</h3><div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>A showreel and a slogan.</p></div><div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>A question the buyer already asks, "Mehr Reichweite?", and a free consultation button.</p></div></div>
          <div class="cs-dec__row" data-reveal style="--d:0.04s"><h3 class="cs-dec__q">How do you sell the format?</h3><div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>"Video is the future."</p></div><div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>Platform data, research quotes and a direct comparison with traditional marketing.</p></div></div>
          <div class="cs-dec__row" data-reveal style="--d:0.08s"><h3 class="cs-dec__q">How do you show three services?</h3><div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>Three long service pages.</p></div><div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>One tabbed panel with benefits and what makes Vibz different.</p></div></div>
          <div class="cs-dec__row" data-reveal style="--d:0.12s"><h3 class="cs-dec__q">What about mobile?</h3><div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>Let the desktop layout stack itself.</p></div><div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>A designed mobile version of every page, plus the menu.</p></div></div>
        </div>
      </div>
    </section>

    <section data-chapter="Result" class="sec cs-result">
      <div class="wrap">
        <header class="sec__head" data-reveal>
          <p class="eyebrow">The result</p>
          <h2 class="h2">A website that moves <span class="dim">like the videos.</span></h2>
        </header>
        <div class="cs-outcomes">
          <div data-reveal><b>7 pages</b><span>a complete site design in one visual system</span></div>
          <div data-reveal style="--d:.06s"><b>13 layouts</b><span>every page designed for desktop and mobile</span></div>
          <div data-reveal style="--d:.12s"><b>One action</b><span>free consultation on every page and in the menu</span></div>
          <div data-reveal style="--d:.18s"><b>Ready to build</b><span>components and styles organised in Figma</span></div>
        </div>
        <div class="cs-got" data-reveal>
          <h3>What Vibz <br>walked away with</h3>
          <ul>
            <li>Homepage design, desktop and mobile</li>
            <li>About page with mission and values</li>
            <li>Portfolio with video case studies</li>
            <li>Blog and article template</li>
            <li>Contact page</li>
            <li>Full-screen mobile menu</li>
            <li>Gradient brand system and components</li>
            <li>Figma file ready for development</li>
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
out = out.replace("<title>AWS Wrap case study | Sorvel Studio</title>", "<title>Vibz case study | Sorvel Studio</title>")
out = re.sub(r'<meta name="description" content="[^"]*" />', '<meta name="description" content="How Sorvel designed the Vibz website in Figma: a bold, bilingual-ready site for a Swiss short-form video agency, desktop and mobile, seven pages." />', out, count=1)
out = re.sub(r'href="../css/case.css(\?v=\d+)?"', 'href="../css/case.css?v=15"', out)
out = re.sub(r'<script src="../js/case.js\?v=\d+"></script>', '<script src="../js/case.js?v=12"></script>', out)
open(W + "vibz.html", "w").write(out)
print("ok", len(out))
