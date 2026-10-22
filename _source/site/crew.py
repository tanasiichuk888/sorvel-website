# Team block: founder card + discipline tiles with live micro-illustrations (no stock faces).
VIS = {
 "ui": '<div class="cw cw--ui"><i class="s"></i><div class="m"><i class="h"></i><div class="k"><i></i><i></i><i></i></div><div class="ch"><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div></div><svg class="cur" viewBox="0 0 20 20"><path d="M3 2l13 6.5-5.6 1.6L8 16 3 2z"/></svg></div>',
 "brand": '<div class="cw cw--brand"><div class="mk"><i></i><i></i></div><b>Aa</b><div class="sw"><i></i><i></i><i></i><i></i></div></div>',
 "webflow": '<div class="cw cw--wf"><div class="tr"><p style="--i:0"><i></i>Body</p><p style="--i:1" class="l1"><i></i>Hero</p><p style="--i:2" class="l2"><i></i>Heading</p><p style="--i:3" class="l2"><i></i>Button</p><p style="--i:4" class="l1"><i></i>CMS · Cases</p></div><div class="cm"><i></i><i></i><i></i></div></div>',
 "framer": '<div class="cw cw--fr"><svg viewBox="0 0 200 110" preserveAspectRatio="none"><path d="M10 100 H190 M10 10 H190" fill="none" stroke="rgba(169,190,255,.18)" stroke-dasharray="3 4" vector-effect="non-scaling-stroke"/><path class="cv-curve" d="M10 100 C 90 100, 80 10, 190 10" fill="none" stroke="#3B6BFF" stroke-width="2" vector-effect="non-scaling-stroke"/></svg><i class="dot"></i><span>ease · spring</span></div>',
 "wp": '<div class="cw cw--wp"><i style="--i:0"></i><i style="--i:1" class="t"></i><i style="--i:2" class="i"></i><i style="--i:3" class="b"></i></div>',
 "shop": '<div class="cw cw--sh"><div class="pc"><i class="im"></i><i class="t"></i><i class="p"></i><span>Add to cart</span></div><b class="bd">1</b></div>',
}
ROLES = [
 ("ui", "Product &amp; UI design", "SaaS apps, dashboards and design systems that stay consistent.", "Figma"),
 ("brand", "Brand identity", "Logos, type and colour systems that hold up everywhere.", "Figma · Illustrator"),
 ("webflow", "Webflow development", "Clean classes, a CMS your team can edit, smooth interactions.", "Webflow"),
 ("framer", "Framer &amp; motion", "Fast marketing sites with motion that feels intentional.", "Framer"),
 ("wp", "WordPress development", "Custom themes and blocks, no bloated page builders.", "WordPress"),
 ("shop", "Shopify design", "Store UX and product pages designed to sell.", "Shopify"),
]

def crew(indent="        ", p=""):
    tiles = "\n".join(
        f'{indent}    <article class="crew__tile" data-reveal style="--d:{.05 + i*.05:.2f}s"><div class="crew__vis">{VIS[k]}</div>'
        f'<div class="crew__txt"><span class="crew__n">{i+1:02d}</span><h3>{t}</h3><p>{d}</p><em>{tag}</em></div></article>'
        for i, (k, t, d, tag) in enumerate(ROLES))
    return f'''{indent}<div class="crew">
{indent}  <article class="crew__lead" data-reveal>
{indent}    <div class="crew__ph"><i class="crew__ring r1"></i><i class="crew__ring r2"><b></b></i><i class="crew__ring r3"><b></b></i><img class="crew__av" src="{p}img/team/mykola.webp" width="211" height="211" alt="Mykola Tanasiichuk" loading="lazy" decoding="async"><span class="crew__badge"><i></i>Founder</span></div>
{indent}    <div class="crew__who"><h3>Mykola Tanasiichuk</h3><p>Founder · Design lead</p></div>
{indent}    <blockquote>"I lead every project from the first brief to launch, and bring in the right senior specialist for each part of the build."</blockquote>
{indent}    <div class="crew__tools"><span>Figma</span><span>Webflow</span><span>Framer</span><span>WordPress</span><span>Shopify</span></div>
{indent}  </article>
{indent}  <div class="crew__grid">
{tiles}
{indent}  </div>
{indent}</div>'''

SIGN = '<svg class="sign" viewBox="0 0 220 60" aria-label="Mykola"><path d="M6 44c10-22 18-34 22-30s-6 30-2 30 14-30 18-30-4 26 0 28 10-16 16-16-2 14 4 14 8-12 12-12-2 10 2 10c6 0 10-18 16-18s-6 20-2 20c6 0 12-26 18-26s-8 28-2 28c5 0 9-10 14-10s-2 8 2 8 10-6 16-6 20-2 30-4"/></svg>'

def note(eyebrow, subject, title, paras, p=""):
    av = f'{p}img/team/mykola.webp'
    txt = "\n".join(f'            <p>{x}</p>' for x in paras)
    return f'''    <section class="sec note">
      <div class="wrap">
        <article class="letter" data-reveal>
          <i class="letter__q" aria-hidden="true">&ldquo;</i>
          <div class="letter__meta">
            <p class="eyebrow">{eyebrow}</p>
            <dl>
              <div><dt>From</dt><dd><img src="{av}" width="24" height="24" alt="" loading="lazy">Mykola Tanasiichuk</dd></div>
              <div><dt>Subject</dt><dd>{subject}</dd></div>
            </dl>
          </div>
          <h2 class="letter__title">{title}</h2>
          <div class="letter__text">
{txt}
          </div>
          <footer class="letter__foot">
            <div class="letter__me"><span class="letter__av"><img src="{av}" width="64" height="64" alt="Mykola Tanasiichuk" loading="lazy"></span><p><b>Mykola Tanasiichuk</b><span>Founder, Sorvel</span></p></div>
            {SIGN}
          </footer>
        </article>
      </div>
    </section>'''
