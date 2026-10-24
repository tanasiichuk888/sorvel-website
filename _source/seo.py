"""SEO pass — run after every build (build.py calls it last).

Adds to every page: canonical, robots, Open Graph + Twitter tags, JSON-LD
structured data, lazy-loading for below-the-fold images.
Writes sitemap.xml, robots.txt and _headers (Cloudflare Pages cache rules).

When the domain is final, change SITE below and run build.py again.
"""
import os, re, json, glob, html, datetime, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "site"))
from common import mnav as _mnav  # full-screen phone menu

SITE = "https://sorvel.agency"          # <- final domain, no trailing slash
BRAND = "Sorvel Studio"
LINKEDIN = "https://www.linkedin.com/company/sorvel"
HERE = os.path.dirname(os.path.abspath(__file__))
W = os.path.abspath(os.path.join(HERE, "..", "website"))
TODAY = datetime.date.today().isoformat()
NOINDEX = {"404.html"}
START, END = "<!-- seo -->", "<!-- /seo -->"
GLASS_V = 5  # bump after editing css/glass.css or js/glass.js
CASE_V = 16  # bump after editing css/case.css
PAGES_V = 30
MOBILE_V = 5  # bump after editing css/mobile.css
BRAND_V = 2  # bump after replacing logo / favicon files
# other assets that change: bump the number after editing the file
ASSET_V = {"css/style.css": 9, "js/main.js": 26, "css/xp.css": 6, "js/scenes.js": 20, "js/xp.js": 5, "js/dots.js": 2, "css/hero.css": 2, "js/case.js": 13, "js/fx.js": 17, "js/svc.js": 17}

# Search titles (aim for under ~60 characters). Case studies are generated from the page.
POPULAR = [("saas-website-design", "SaaS website design"), ("fintech-website-design", "Fintech website design"),
           ("webflow-agency", "Webflow agency"), ("wordpress-to-webflow-migration", "WordPress to Webflow migration")]

TITLES = {
    "about.html": "About Sorvel | Senior design and development studio",
    "contact.html": "Start a project | Fixed quote in 24 hours | Sorvel",
    "pricing.html": "Pricing | Website and product design | Sorvel",
    "process.html": "Our process | From brief to launch | Sorvel",
    "reviews.html": "Client reviews | Sorvel Studio",
    "work.html": "Work | Website and product design case studies | Sorvel",
    "services/websites.html": "Website design and development | Sorvel Studio",
    "services/brand-identity.html": "Brand identity design | Sorvel Studio",
    "services/landing-pages.html": "Landing page design and CRO | Sorvel Studio",
    "services/migrations.html": "Website migration services | Sorvel Studio",
    "services/product-design.html": "SaaS product and UI/UX design | Sorvel Studio",
}

def clean_url(rel):
    if rel == "index.html": return SITE + "/"
    return SITE + "/" + rel[:-5]

def text(s): return html.unescape(re.sub(r"<[^>]+>", " ", s)).replace("  ", " ").strip()

ORG = {"@type": "Organization", "@id": SITE + "/#org", "name": BRAND, "alternateName": ["Sorvel", "Sorvel Agency", "sorvel.agency"], "url": SITE + "/",
       "logo": {"@type": "ImageObject", "url": SITE + "/img/brand/logo-512.png", "width": 512, "height": 512},
       "image": SITE + "/img/og/default.jpg",
       "description": "Design and development studio for SaaS, fintech, AI and B2B companies. Websites, product UI and brand identity, built in Webflow, Framer, WordPress and Shopify.",
       "founder": {"@id": SITE + "/#founder"}, "sameAs": [LINKEDIN],
       "knowsAbout": ["Web design", "UI/UX design", "Product design", "Brand identity", "Webflow", "Framer", "WordPress", "Shopify", "Figma"],
       "areaServed": "Worldwide"}
PERSON = {"@type": "Person", "@id": SITE + "/#founder", "name": "Mykola Tanasiichuk", "jobTitle": "Founder, Design Lead",
          "image": SITE + "/img/team/mykola.webp", "worksFor": {"@id": SITE + "/#org"},
          "sameAs": ["https://www.behance.net/tanasiichuk8", "https://dribbble.com/koliafree11"]}
WEBSITE = {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": BRAND, "publisher": {"@id": SITE + "/#org"}, "inLanguage": "en"}

def section_name(rel):
    if rel.startswith("work/"): return ("Work", SITE + "/work")
    if rel.startswith("services/"): return ("Services", SITE + "/#services")
    return None

def _div_block(s, start):
    """Return the end index of the <div> that opens at `start` (simple depth count)."""
    depth, i = 0, start
    for m in re.finditer(r'<div\b|</div>', s[start:]):
        depth += 1 if m.group(0) != "</div>" else -1
        if depth == 0:
            return start + m.end()
    raise ValueError("unclosed div")

def _svc_mobile(s):
    st = s.index('<div class="svc__stage" aria-hidden="true">')
    stage = s[st:_div_block(s, st)]
    vis = []
    for m in re.finditer(r'<div class="vis[ "]', stage):
        vis.append(stage[m.start():_div_block(stage, m.start())])
    def clone(i):
        v = vis[i]
        if "is-on" not in v.split(">", 1)[0]:
            v = v.replace('class="vis ', 'class="vis is-on ', 1)
        v = re.sub(r'id="([^"]+)"', lambda m: f'id="{m.group(1)}-m{i}"', v)
        v = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#{m.group(1)}-m{i})', v)
        v = re.sub(r'href="#([^"]+)"', lambda m: f'href="#{m.group(1)}-m{i}"', v)
        return f'<div class="svc__stage svc__stage--m" aria-hidden="true">{v}</div>'
    n = [0]
    def put(m):
        i = n[0]; n[0] += 1
        return m.group(0) + (clone(i) if i < len(vis) else "")
    return re.sub(r'<div class="svc__body"><div>', put, s)

def process(path):
    rel = os.path.relpath(path, W).replace(os.sep, "/")
    s = open(path, encoding="utf-8").read()
    s = re.sub(r"[ \t]*" + re.escape(START) + r".*?" + re.escape(END) + r"\n?", "", s, flags=re.S)
    if rel in TITLES:
        s = re.sub(r"<title>.*?</title>", "<title>" + html.escape(TITLES[rel], quote=False) + "</title>", s, count=1, flags=re.S)
    elif rel.startswith("work/"):
        nm = re.search(r"<title>([^:|]*?)(?: case study|:)", s)
        ey = re.search(r'class="eyebrow"[^>]*>(.*?)</p>', s)
        if nm and ey:
            ind = text(ey.group(1)).split("·")[0].strip()
            s = re.sub(r"<title>.*?</title>", f"<title>{nm.group(1)}: {ind.lower() if ind[:1].isupper() and not ind.isupper() else ind} website case study | Sorvel</title>", s, count=1, flags=re.S)
    title = text(re.search(r"<title>(.*?)</title>", s, re.S).group(1))
    dm = re.search(r'<meta name="description" content="(.*?)"', s)
    desc = html.unescape(dm.group(1)) if dm else ""
    h1m = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S); h1 = text(h1m.group(1)) if h1m else title
    url = clean_url(rel)
    is_case = rel.startswith("work/"); is_service = rel.startswith("services/")
    slug = os.path.basename(rel)[:-5]
    og = f"{SITE}/img/og/{slug}.jpg" if is_case and os.path.exists(f"{W}/img/og/{slug}.jpg") else f"{SITE}/img/og/default.jpg"
    E = lambda v: html.escape(v, quote=True)

    tags = []
    if rel in NOINDEX:
        tags.append('<meta name="robots" content="noindex, follow" />')
    else:
        tags += [f'<link rel="canonical" href="{url}" />',
                 '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1" />']
    if '<meta name="theme-color"' not in s:
        tags.append('<meta name="theme-color" content="#0B0C0F" />')
    tags += ['<meta name="author" content="Mykola Tanasiichuk" />',
             f'<meta property="og:type" content="{"article" if is_case else "website"}" />',
             f'<meta property="og:site_name" content="{BRAND}" />', '<meta property="og:locale" content="en_US" />',
             f'<meta property="og:title" content="{E(title)}" />', f'<meta property="og:description" content="{E(desc)}" />',
             f'<meta property="og:url" content="{url}" />', f'<meta property="og:image" content="{og}" />',
             '<meta property="og:image:width" content="1200" />', '<meta property="og:image:height" content="630" />',
             f'<meta property="og:image:alt" content="{E(h1)}" />',
             '<meta name="twitter:card" content="summary_large_image" />', f'<meta name="twitter:title" content="{E(title)}" />',
             f'<meta name="twitter:description" content="{E(desc)}" />', f'<meta name="twitter:image" content="{og}" />']

    graph = [ORG, WEBSITE]
    if rel not in NOINDEX:
        page = {"@type": "AboutPage" if rel == "about.html" else ("ContactPage" if rel == "contact.html" else "WebPage"),
                "@id": url + "#webpage", "url": url, "name": title, "description": desc, "isPartOf": {"@id": SITE + "/#website"},
                "inLanguage": "en", "primaryImageOfPage": og}
        if rel != "index.html":
            crumbs = [("Home", SITE + "/")]
            sec = section_name(rel)
            if sec: crumbs.append(sec)
            crumbs.append((h1 if len(h1) < 70 else title.split("|")[0].strip(), url))
            bc = {"@type": "BreadcrumbList", "@id": url + "#breadcrumb",
                  "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]}
            page["breadcrumb"] = {"@id": url + "#breadcrumb"}; graph.append(bc)
        else:
            page["about"] = {"@id": SITE + "/#org"}
        graph.append(page)
        if rel in ("index.html", "about.html"): graph.append(PERSON)
        if is_service:
            graph.append({"@type": "Service", "@id": url + "#service", "name": h1, "serviceType": title.split("|")[0].strip(),
                          "description": desc, "provider": {"@id": SITE + "/#org"}, "areaServed": "Worldwide", "url": url})
        if is_case:
            graph.append({"@type": "CreativeWork", "@id": url + "#work", "name": h1, "headline": title.split("|")[0].strip(),
                          "description": desc, "image": og, "url": url, "creator": {"@id": SITE + "/#org"},
                          "author": {"@id": SITE + "/#org"}, "inLanguage": "en"})
        qa = re.findall(r'<details class="acc__item"[^>]*><summary>(.*?)</summary><div class="acc__a">(.*?)</div></details>', s, re.S)
        if qa:
            graph.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
                {"@type": "Question", "name": text(q), "acceptedAnswer": {"@type": "Answer", "text": text(a)}} for q, a in qa]})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    tags.append(f'<script type="application/ld+json">{ld}</script>')
    block = START + "\n  " + "\n  ".join(tags) + "\n  " + END + "\n"
    anchor = dm.group(0) if dm else "<title>"
    i = s.index(anchor); j = s.index("\n", i) + 1 if dm else i
    s = s[:j] + "  " + block + s[j:]
    s = re.sub(r'(<!-- /seo -->\n)[ \t]+', r'\1  ', s)

    pre = "../" * rel.count("/")
    # self-hosted fonts instead of Google Fonts (privacy + speed)
    s = re.sub(r'[ \t]*<link[^>]*fonts\.(googleapis|gstatic)\.com[^>]*>\n', '', s)
    if "css/fonts.css" not in s:
        k = s.index('<link rel="stylesheet"')
        s = s[:k] + (f'<link rel="preload" href="{pre}fonts/inter-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin />\n'
                     f'  <link rel="preload" href="{pre}fonts/hanken-grotesk-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin />\n'
                     f'  <link rel="stylesheet" href="{pre}css/fonts.css?v=1" />\n  ') + s[k:]

    # phone menu: new button + full-screen panel on every page (index and case pages have hand-built headers)
    NEW_BURGER = '<button class="nav__burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mnav"><span class="nav__bl" aria-hidden="true"><b>Menu</b><b>Close</b></span><span class="nav__ic" aria-hidden="true"><i></i><i></i></span></button>'
    s = re.sub(r'<button class="nav__burger"[^>]*><span></span><span></span></button>\s*<a class="btn btn--primary nav__mcta"[^>]*>.*?</a>(?:</span>)*', NEW_BURGER, s, flags=re.S)
    if 'id="mnav"' not in s and 'class="nav__burger"' in s:
        act = "work" if rel.startswith("work/") else ""
        s = s.replace("  </header>\n", "  </header>\n" + _mnav(pre, act), 1)

    # services list on phones: each row carries its own copy of its preview, so opening a row never moves the rows above it
    if 'class="svc__list"' in s and "svc__stage--m" not in s:
        s = _svc_mobile(s)

    # footer "Popular" row: links to the niche service pages on every page (helps them get found and indexed)
    if 'class="foot__pop"' not in s and '<div class="foot__bottom">' in s:
        pop = "".join(f'<a href="{pre}services/{a}.html">{b}</a>' for a, b in POPULAR)
        s = s.replace('<div class="foot__bottom">', f'<nav class="foot__pop" aria-label="Popular"><span>Popular</span>{pop}</nav>\n      <div class="foot__bottom">', 1)

    # liquid-glass layer on every page (css + ambient background + pointer highlight)
    if "css/glass.css" not in s:
        links = list(re.finditer(r'<link rel="stylesheet" href="[^"]+" />\n', s))
        k = links[-1].end()
        s = s[:k] + f'  <link rel="stylesheet" href="{pre}css/glass.css?v={GLASS_V}" />\n' + s[k:]
    s = re.sub(r'css/glass\.css\?v=\d+', f'css/glass.css?v={GLASS_V}', s)
    # phone typography pass, always the last stylesheet
    s = re.sub(r'[ \t]*<link rel="stylesheet" href="[^"]*css/mobile\.css[^"]*" />\n', '', s)
    k = s.index("</head>")
    s = s[:k] + f'  <link rel="stylesheet" href="{pre}css/mobile.css?v={MOBILE_V}" />\n' + s[k:]
    if 'class="amb"' not in s:
        s = re.sub(r"(<body[^>]*>)", r'\1\n  <div class="amb" aria-hidden="true"><i></i><i></i><i></i></div>', s, count=1)
    if "js/glass.js" not in s:
        s = s.replace("</body>", f'  <script src="{pre}js/glass.js?v={GLASS_V}"></script>\n</body>', 1)
    s = re.sub(r'js/glass\.js\?v=\d+', f'js/glass.js?v={GLASS_V}', s)
    s = re.sub(r'css/case\.css(\?v=\d+)?"', f'css/case.css?v={CASE_V}"', s)
    s = re.sub(r'css/pages\.css(\?v=\d+)?"', f'css/pages.css?v={PAGES_V}"', s)
    s = re.sub(r'img/brand/(logo\.svg|favicon\.svg|favicon-32\.png|apple-touch-icon\.png)(\?v=\d+)?"', lambda m: f'img/brand/{m.group(1)}?v={BRAND_V}"', s)

    for _a, _v in ASSET_V.items():
        s = re.sub(re.escape(_a) + r'(\?v=\d+)?"', f'{_a}?v={_v}"', s)
    # big cover screenshots: lower priority than the headline text
    s = re.sub(r'(<div class="cs-cover[^"]*"[^>]*>.*?</section>)', lambda m: re.sub(r'<img(?![^>]*fetchpriority)', '<img fetchpriority="low"', m.group(1)), s, count=1, flags=re.S)
    # decorative image walls load after the page (keeps first paint fast on phones)
    def _wall(m):
        blk = m.group(0)
        blk = re.sub(r'<img src="([^"]+)"', r'<img data-src="\1" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="', blk)
        return re.sub(r' loading="(eager|lazy)"', '', blk)
    s = re.sub(r'<div class="sx-wall".*?</div>\n</div>', _wall, s, flags=re.S)
    # defer page scripts: text paints before animations start
    s = re.sub(r'<script src="([^"]+)"(?![^>]*\bdefer)', r'<script defer src="\1"', s)
    # accessibility fixes flagged by Lighthouse
    s = s.replace(' role="tablist"', '')
    s = re.sub(r' role="tab" aria-selected="(true|false)"', r' aria-expanded="\1"', s)
    s = re.sub(r'(class="(?:score__stars|rcard__stars)")(?! role=)', r'\1 role="img"', s)
    s = re.sub(r'(<a class="case__media[^"]*"[^>]*?) aria-label="[^"]*"', r'\1', s)
    # client logos: real width/height so the browser reserves the right space
    def _logo(m):
        tag, src, hpx = m.group(0), m.group(1), int(m.group(2))
        if " width=" in tag: return tag
        try:
            from PIL import Image
            w, h = Image.open(os.path.join(W, src.lstrip("./").replace("../", ""))).size
        except Exception:
            return tag
        return tag.replace("<img ", f'<img width="{round(w * hpx / h)}" height="{hpx}" ', 1)
    s = re.sub(r'<img[^>]*src="((?:\.\./)?img/logos/[^"]+)"[^>]*style="height:(\d+)px"[^>]*>', _logo, s)
    s = re.sub(r'(<img[^>]*img/logos/[^>]*?)style="height:(\d+)px"', r'\1style="--h:\2px"', s)

    # lazy-load images below the first section
    body_start = s.find("</section>")
    if body_start > 0:
        head, tail = s[:body_start], s[body_start:]
        tail = re.sub(r"<img(?![^>]*\bloading=)", '<img loading="lazy"', tail)
        tail = re.sub(r"<img(?![^>]*\bdecoding=)", '<img decoding="async"', tail)
        s = head + tail
    open(path, "w", encoding="utf-8").write(s)
    return None if rel in NOINDEX else (url, rel)

pages = [process(p) for p in sorted(glob.glob(W + "/**/*.html", recursive=True))]
pages = [p for p in pages if p]
def prio(rel):
    if rel == "index.html": return "1.0"
    if rel in ("work.html", "contact.html", "pricing.html") or rel.startswith("services/"): return "0.9"
    if rel.startswith("work/"): return "0.8"
    if rel in ("privacy.html", "terms.html"): return "0.3"
    return "0.7"
urls = "\n".join(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod><priority>{prio(r)}</priority></url>"
                 for u, r in sorted(pages, key=lambda x: (-float(prio(x[1])), x[0])))
open(W + "/sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
open(W + "/robots.txt", "w").write(f"User-agent: *\nAllow: /\nDisallow: /404\n\nSitemap: {SITE}/sitemap.xml\n")
open(W + "/_headers", "w").write("""/img/*
  Cache-Control: public, max-age=604800
/css/*
  Cache-Control: public, max-age=31536000, immutable
/fonts/*
  Cache-Control: public, max-age=31536000, immutable
/js/*
  Cache-Control: public, max-age=31536000, immutable
/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN
""")
print(f"SEO: {len(pages)} pages in sitemap, domain {SITE}")
