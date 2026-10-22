import re
W = "WEBSITE_DIR/work/"
src = open(W + "awswrap.html").read()
src = src.replace('<img fetchpriority="low" ', '<img ')  # undo the SEO pass tweak so templates match
src = re.sub(r'<title>AWS Wrap[^<]*</title>', '<title>AWS Wrap case study | Sorvel Studio</title>', src)  # restore the template title
I = "../img/work/waveads/"
LIVE = "https://minimal-pages-060778.framer.app"

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

COLORS = [("Ocean", "#3B6BFF", "#fff"), ("Night", "#111216", "#fff"), ("Coral", "#ff6b5b", "#fff"), ("Sand", "#f3ead8", "#14161b"), ("Lime", "#c8f560", "#14161b")]
chips = "".join(f'<button type="button" class="wad__c{" is-on" if i == 0 else ""}" style="--c:{c}" data-bg="{c}" data-fg="{f}" aria-label="{n} banner" aria-pressed="{"true" if i == 0 else "false"}"></button>' for i, (n, c, f) in enumerate(COLORS))

main = f'''  <main class="cs cs--wa">
    <div class="cs-progress" aria-hidden="true"><i></i></div>
    <!-- ============ CASE HERO ============ -->
    <section class="cs-hero">
      <canvas class="hero__dots" aria-hidden="true"></canvas>
      <div class="wrap">
        <nav class="cs-crumbs" data-intro style="--d:.05s"><a href="../work.html">Work</a><span>/</span><span>AdVoyage</span></nav>
        <p class="eyebrow" data-intro style="--d:.1s">Outdoor advertising · Boat billboards · Miami Beach</p>
        <h1 class="cs-title">
          <span class="line"><span class="line__in" style="--d:.15s">A billboard that</span></span>
          <span class="line"><span class="line__in" style="--d:.25s"><span class="accent">floats</span>.</span></span>
        </h1>
        <p class="cs-lead" data-intro style="--d:.4s">AdVoyage puts brands on boats that cruise along Miami Beach, in front of millions of people lying on the sand with nothing else to look at. We replaced a free starter site with a landing page that sells the idea in one scroll: designed in Figma, then built in Framer with a looping hero of the boat on the water.</p>

        <dl class="cs-facts" data-intro style="--d:.5s">
          <div><dt>Client</dt><dd>AdVoyage</dd></div>
          <div><dt>Scope</dt><dd>Landing page design, Framer build</dd></div>
          <div><dt>Platform</dt><dd>Figma + Framer</dd></div>
          <div><dt>Live site</dt><dd><a href="{LIVE}" target="_blank" rel="noopener">View the Framer build ↗</a></dd></div>
        </dl>
      </div>

      <div class="wrap cs-cover" data-intro style="--d:.6s">
        <div class="vwin cs-win" data-parallax=".06">
          <div class="win__bar"><i></i><i></i><i></i><span class="win__url">advoyage · Miami Beach</span></div>
          <img src="{I}hero.webp" alt="AdVoyage hero: Float your brand on water, Miami is our canvas" width="1600" height="1000">
        </div>
      </div>
    </section>

    <!-- ============ CHALLENGE ============ -->
    <section data-chapter="Challenge" class="sec cs-brief">
      <div class="wrap cs-split">
        <div data-reveal>
          <p class="eyebrow">The challenge</p>
          <h2 class="h2">A new kind of ad <span class="dim">needs to be seen to be believed.</span></h2>
        </div>
        <div class="cs-text" data-reveal style="--d:.08s">
          <p>Most marketing managers have never bought a boat billboard. They know highway billboards, social ads and influencers. AdVoyage had to explain a new format, prove it works and get a quote request, all on one page.</p>
          <p>The first site was a free build by a friend. It had the idea but not the polish a brand manager expects before spending real budget. The founder's one firm request: the boat itself, with an ad on it, has to be the first thing people see.</p>
          <ul class="cs-goals">
            <li>Show the boat in the first second</li>
            <li>Prove it beats a billboard</li>
            <li>Turn interest into a quote request</li>
          </ul>
        </div>
      </div>
      <div class="wrap">
        <div class="cs-problems">
          <article data-reveal style="--d:0.00s"><h3>An unfamiliar format</h3><p>People can't picture a floating billboard until they see one. Text alone doesn't sell it.</p></article>
          <article data-reveal style="--d:0.06s"><h3>No proof yet</h3><p>A young company with no long client list. The numbers about Miami Beach had to do the convincing.</p></article>
          <article data-reveal style="--d:0.12s"><h3>Many kinds of buyers</h3><p>Clubs, retail brands, event promoters and real estate all buy differently, and each needed to see itself on the page.</p></article>
        </div>
      </div>
    </section>

    <!-- ============ HOW WE WORKED ============ -->
    <section data-chapter="Process" class="sec cs-chapter">
      <div class="wrap">
        <header class="sec__head sec__head--row" data-reveal>
          <div>
            <p class="eyebrow">How we worked</p>
            <h2 class="h2">From a free starter site <span class="dim">to a sales page.</span></h2>
          </div>
          <p class="sec__lead">Design first, build second. The full page was approved in Figma before a single Framer frame was made, so the build had no surprises.</p>
        </header>
        <div class="cs-process" data-reveal>
          <div class="cs-phase" style="--i:0"><p class="cs-phase__when">Discovery</p><h3>What a buyer needs to hear</h3><p>We reviewed the old site and the founder's references, and listed the questions a brand manager asks before booking a new ad format.</p><ul><li>Old site review</li><li>References and competitors</li><li>Buyer questions</li></ul></div>
          <div class="cs-phase" style="--i:1"><p class="cs-phase__when">Hero</p><h3>The boat comes first</h3><p>A generated scene of a AdVoyage boat sailing past the beach with "Display your ad" on its side, turned into a looping video for the hero.</p><ul><li>Boat concept</li><li>Looping hero video</li><li>Headline and stats</li></ul></div>
          <div class="cs-phase" style="--i:2"><p class="cs-phase__when">Design</p><h3>A calm, numbered grid</h3><p>Thin lines, numbered columns and lots of white space, so the photos and numbers carry the page. Every section designed in Figma.</p><ul><li>Full landing page</li><li>Audience blocks</li><li>Numbered quote form</li></ul></div>
          <div class="cs-phase" style="--i:3"><p class="cs-phase__when">Build</p><h3>Framer, ready to edit</h3><p>Built in Framer from the approved design, with smooth scroll reveals and a working form, so the founder can update copy himself.</p><ul><li>Framer build</li><li>Form and anchors</li><li>Responsive layouts</li></ul></div>
        </div>
      </div>
    </section>

    <!-- ============ NUMBERS ============ -->
    <section class="cs-numbers" aria-label="Key facts on the new page">
      <div class="wrap">
        <p class="eyebrow" data-reveal>At a glance</p>
        <div class="cs-bench">
          <div data-reveal><b><span data-count="1">0</span> <small>page</small></b><span>That explains, proves and sells</span><em>Single-scroll landing page</em></div>
          <div data-reveal style="--d:.06s"><b><span data-count="28.2" data-dec="1">0</span>M+</b><span>Yearly Miami visitors, in the first screen</span><em>Numbers before claims</em></div>
          <div data-reveal style="--d:.12s"><b><span data-count="4">0</span></b><span>Audience blocks</span><em>Nightlife, retail, events, real estate</em></div>
          <div data-reveal style="--d:.18s"><b><span data-count="7">0</span></b><span>Numbered fields in the quote form</span><em>Dates and budget included</em></div>
        </div>
      </div>
    </section>

    <!-- ============ AD DEMO ============ -->
    <section data-chapter="Idea" class="sec cs-demo">
      <div class="wrap cs-split">
        <div data-reveal>
          <p class="eyebrow">The idea</p>
          <h2 class="h2">Let them see <span class="dim">their own brand on the water.</span></h2>
          <p class="cs-demo__lead">The hero boat carries a placeholder ad that says "Display your ad." It does one job: lets a brand manager picture their logo sailing past South Beach. Once they can see it, the format stops being strange and starts being a campaign. Right after, the numbers explain why it works: people on the sand look at the boat for up to a minute, with no other ad in sight.</p>
        </div>
        <div class="wvs" data-reveal style="--d:.1s">
          <div class="wvs__photo"><img src="{I}boat.webp" alt="AdVoyage boat with a Display your ad banner off Miami Beach" loading="lazy" width="1200" height="560"></div>
          <div class="wvs__body">
            <p class="wvs__label">Why a boat beats a billboard</p>
            <div class="wvs__row"><span>View time</span>
              <div class="wvs__bar"><i style="--w:6%"></i><em>Road billboard · 2–3 sec</em></div>
              <div class="wvs__bar is-on"><i style="--w:100%"></i><em>AdVoyage boat · 10–60+ sec</em></div></div>
            <div class="wvs__row"><span>Competing ads</span>
              <div class="wvs__bar"><i style="--w:100%"></i><em>Road billboard · 10+ around it</em></div>
              <div class="wvs__bar is-on"><i style="--w:3%"></i><em>AdVoyage boat · none</em></div></div>
            <ul class="wvs__facts"><li><b>28.2M+</b>Miami visitors a year</li><li><b>7+ mi</b>of beachfront</li><li><b>$22B</b>spent by visitors</li></ul>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ GALLERY / STORY ============ -->
    <section data-chapter="Details" class="sec cs-story">
      <div class="wrap">
{row(False, "Proof", "Numbers first, then the comparison.", "Four big numbers sit right under the hero: 28.2M visitors, 10M on South Beach, 76% engagement, 7+ miles of sand. Then a plain side-by-side shows why a boat beats a road billboard.", "compare.webp", "Stats row and Why Boat Advertising Wins comparison")}
{row(True, "Audience", "Every buyer finds their column.", "Four numbered columns for hospitality, retail, events and real estate. Hover one and it opens with a photo and a line on how that kind of brand uses the boats.", "who.webp", "Who we sail for: four numbered audience columns")}
{row(False, "Advantage", "Three reasons, one photo of Miami.", "A relaxed audience with nowhere else to look, a $22B tourism economy and free reach when people photograph the boat. Numbered cards next to the city skyline at sunset.", "advantage.webp", "The Unfair Advantage section with Miami skyline")}
{row(True, "Contact", "A quote form that reads like a brief.", "Seven numbered fields ask what a quote really needs: company, dates, budget and what you're advertising. Next to it, the email, the waters they sail and a promise of a reply in one business day.", "form.webp", "Start a campaign quote form")}
      </div>
    </section>

    <!-- ============ FULL PAGE ============ -->
    <section class="sec cs-duo">
      <div class="wrap cs-duo__grid">
        <div class="cs-duo__code" data-reveal>
          <p class="eyebrow">The whole page</p>
          <h3>One scroll, from boat to brief.</h3>
          <p>Hero, numbers, comparison, audiences, advantages and the form. Each section answers the next question a buyer has, so by the end the only step left is sending the brief.</p>
          <div class="vwin cs-shot"><div class="win__bar"><i></i><i></i><i></i></div><img src="{I}hero.webp" alt="AdVoyage hero on desktop" loading="lazy" width="1600" height="1000"></div>
        </div>
        <div class="wa-scroll" data-reveal style="--d:.1s">
          <div class="vwin"><div class="win__bar"><i></i><i></i><i></i><span class="win__url">Full page design</span></div>
            <div class="wa-scroll__vp"><img src="{I}full.webp" alt="Full AdVoyage landing page design, top to bottom" loading="lazy" width="1200" height="4271"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ REEL ============ -->
    <section class="cs-reel" aria-hidden="true">
      <div class="cs-reel__track">{"".join(f'<img src="{I}{x}" alt="" loading="lazy" width="1600" height="1000">' for x in ["compare.webp", "who.webp", "advantage.webp", "form.webp", "hero.webp"] * 2)}</div>
    </section>

    <!-- ============ KEY DECISIONS ============ -->
    <section data-chapter="Decisions" class="sec cs-chapter">
      <div class="wrap">
        <header class="sec__head" data-reveal>
          <p class="eyebrow">Key decisions</p>
          <h2 class="h2">Choices that make a new format <span class="dim">feel like a safe buy.</span></h2>
        </header>
        <div class="cs-dec">
          <div class="cs-dec__row" data-reveal style="--d:0.00s">
            <h3 class="cs-dec__q">What goes in the hero?</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>A stock beach photo and a slogan.</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>The boat itself, ad on its side, sailing past the beach in a looping video.</p></div>
          </div>
          <div class="cs-dec__row" data-reveal style="--d:0.04s">
            <h3 class="cs-dec__q">How do you prove a new format?</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>Adjectives like "unforgettable" and "unique".</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>Visitor numbers up front and a direct comparison with road billboards.</p></div>
          </div>
          <div class="cs-dec__row" data-reveal style="--d:0.08s">
            <h3 class="cs-dec__q">Who is it for?</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>"Any brand that wants attention."</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>Four named audiences, each with its own column and use case.</p></div>
          </div>
          <div class="cs-dec__row" data-reveal style="--d:0.12s">
            <h3 class="cs-dec__q">How do you ask for the lead?</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>Name, email and an empty message box.</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>A short brief with dates and budget, so the first reply can be a real quote.</p></div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ RESULT ============ -->
    <section data-chapter="Result" class="sec cs-result">
      <div class="wrap">
        <header class="sec__head" data-reveal>
          <p class="eyebrow">The result</p>
          <h2 class="h2">A page that sells <span class="dim">the sea view.</span></h2>
        </header>
        <div class="cs-outcomes">
          <div data-reveal><b>Boat first</b><span>the product is visible in the first second, not explained in the third paragraph</span></div>
          <div data-reveal style="--d:.06s"><b>Proof</b><span>real Miami numbers and a billboard comparison</span></div>
          <div data-reveal style="--d:.12s"><b>Better leads</b><span>quote requests arrive with dates and budget</span></div>
          <div data-reveal style="--d:.18s"><b>Framer</b><span>the founder edits copy and photos himself</span></div>
        </div>
        <div class="cs-got" data-reveal>
          <h3>What AdVoyage <br>walked away with</h3>
          <ul>
            <li>A full landing page design in Figma</li>
            <li>A Framer build of the approved design</li>
            <li>A looping hero video of the ad boat</li>
            <li>Stats and billboard comparison blocks</li>
            <li>Four audience blocks with hover photos</li>
            <li>A numbered "Unfair advantage" section</li>
            <li>A quote form with dates and budget</li>
            <li>Responsive layouts for every screen</li>
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
out = out.replace("<title>AWS Wrap case study | Sorvel Studio</title>", "<title>AdVoyage case study | Sorvel Studio</title>")
out = re.sub(r'<meta name="description" content="[^"]*" />', '<meta name="description" content="How Sorvel designed a landing page in Figma and built it in Framer for AdVoyage, a boat billboard advertising company on Miami Beach." />', out, count=1)
out = out.replace('href="../css/case.css"', 'href="../css/case.css?v=13"').replace('href="../css/case.css?v=9"', 'href="../css/case.css?v=10"')
out = re.sub(r'<script src="../js/case.js\?v=\d+"></script>', '<script src="../js/case.js?v=10"></script>', out)
open(W + "waveads.html", "w").write(out)
print("ok", len(out))
