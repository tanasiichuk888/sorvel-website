import sys, re, datetime; sys.path.insert(0, "SOURCE_DIR/site")
from common import *
from blog_posts import POSTS

PLAN = {"wordpress-to-webflow-migration": "migration", "saas-website-design": "website"}

def nice_date(d):
    return datetime.date.fromisoformat(d).strftime("%-d %B %Y")

def read_min(post):
    words = len(re.sub(r"<[^>]+>", " ", " ".join(b for _, _, b in post["sections"]) + post["lead"]).split())
    return max(3, round(words / 220))

def author(p, post):
    return (f'<div class="post-by"><img src="{p}img/team/mykola.webp" alt="" width="44" height="44">'
            f'<span><b>Mykola Tanasiichuk</b><small>Founder, Sorvel · <time datetime="{post["date"]}">{nice_date(post["date"])}</time></small></span></div>')

def inline_cta(p, post):
    svc, name = post["svc"]
    quote = f"{p}contact.html?plan={PLAN[svc]}#brief"
    if PLAN[svc] == "migration":
        t, x = "Planning a move to Webflow?", "Send us your site address. You get a written plan with scope, timeline and a fixed price within 24 hours, no call needed."
    else:
        t, x = "Want a number for your own site?", "Tell us about your product and the pages you need. You get a written plan with scope, timeline and a fixed price within 24 hours."
    return f'''<aside class="post-cta" data-reveal>
  <div><p class="post-cta__t">{t}</p><p>{x}</p></div>
  <div class="post-cta__btns">{btn_primary(quote, "Get a fixed quote", lg=False)}{btn_ghost("https://t.me/tanasiychuk8", "Ask on Telegram", tg=True, lg=False)}</div>
</aside>'''

def bcard(p, post, big=False):
    return (f'<a class="bcard{" bcard--big" if big else ""}" href="{p}blog/{post["slug"]}.html" data-reveal>'
            f'<span class="bcard__meta"><span class="bcard__cat">{post["cat"]}</span><span>{read_min(post)} min read</span></span>'
            f'<h3>{post["h1"]}</h3><p>{post["card"]}</p>'
            f'<span class="bcard__foot"><time datetime="{post["date"]}">{nice_date(post["date"])}</time><span class="bcard__go" aria-hidden="true">{DIAG}</span></span></a>')

def post_page(post):
    p = "../"
    svc, name = post["svc"]
    strip = lambda h: re.sub(r"^\d+\. ", "", h)
    toc = "".join(f'<a href="#{sid}">{strip(h)}</a>' for sid, h, _ in post["sections"])
    secs = "\n".join(f'          <h2 id="{sid}">{h}</h2>\n{b.strip()}' for sid, h, b in post["sections"]).replace("[[cta]]", inline_cta(p, post))
    short = post["h1"] if len(post["h1"]) < 48 else post["h1"][:46].rsplit(" ", 1)[0] + "…"
    body = hero(f'<a href="../blog.html">Blog</a><span>/</span><span>{short}</span>', f'{post["cat"]} · {read_min(post)} min read',
                [post["h1"]], post["lead"], actions=author(p, post), p=p)
    others = [x for x in POSTS if x["slug"] != post["slug"]]
    rel = "".join(bcard(p, x) for x in others[:2])
    body += f'''
    <section class="sec post-sec">
      <div class="wrap legal post">
        <nav class="legal__toc post__toc" aria-label="In this article"><p>In this article</p>{toc}</nav>
        <article class="legal__body post__body">
{secs}
          <div class="post-end" data-reveal>
            <p class="post-end__k">Next step</p>
            <h2>Get a fixed quote in 24 hours.</h2>
            <p>Send a short brief or your site address. You get a written plan with the scope, the timeline and a fixed price. See how we handle <a href="{p}services/{svc}.html">{name}</a>.</p>
            <div class="post-end__btns">{btn_primary(f"{p}contact.html?plan={PLAN[svc]}#brief", "Start a project", lg=False)}{btn_ghost(f"{p}services/{svc}.html", "See the service", lg=False)}</div>
          </div>
        </article>
      </div>
    </section>
'''
    body += faq(post["faq"], title='Quick <span class="dim">answers.</span>', eyebrow="FAQ")
    body += f'''    <section class="sec" data-chapter="More">
      <div class="wrap">
{sec_head("Keep reading", 'More from <span class="dim">the blog.</span>', "", row=False)}
        <div class="bgrid bgrid--2">{rel}</div>
      </div>
    </section>
'''
    body += cta(p)
    page(f'blog/{post["slug"]}.html', post["title"], post["desc"], "", body, p, dock=False)

def index():
    p = ""
    cards = "".join(bcard(p, x, big=(i == 0)) for i, x in enumerate(POSTS))
    body = hero("<span>Blog</span>", "Blog", ['Notes on websites', 'that <span class="accent">sell</span>.'],
                "Straight answers about website costs, platforms, migrations and design, from the team that designs and builds them every week.", p=p)
    body += f'''
    <section class="sec post-sec">
      <div class="wrap">
        <div class="bgrid">{cards}</div>
      </div>
    </section>
'''
    body += cta(p)
    page("blog.html", "Blog | Website design, Webflow and SaaS guides | Sorvel",
         "Guides on website costs, WordPress to Webflow migrations, SaaS websites and design, from the Sorvel team.", "", body, p, dock=False)

if __name__ == "__main__":
    index()
    for x in POSTS: post_page(x)
