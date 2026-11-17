# Inline SVG product illustrations for the service pages (no photos, no fake numbers).
# Each returns a responsive <svg> drawn on a 560 x 420 canvas; colours come from CSS classes (.il-*).

def _bar(x, y, w, h=8, c="il-l2", r=4): return f'<rect class="{c}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/>'
def _btn(x, y, w, label, h=30): return f'<rect class="il-acc" x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}"/><text class="il-tb" x="{x + w/2}" y="{y + h/2 + 4}" text-anchor="middle">{label}</text>'
def _chip(x, y, label, cls="il-chip"):
    w = 14 + len(label) * 6.4
    return f'<g class="{cls}"><rect x="{x}" y="{y}" width="{w}" height="24" rx="12"/><text x="{x + w/2}" y="{y + 16}" text-anchor="middle">{label}</text></g>'
def _win(x, y, w, h, url=""):
    u = f'<rect class="il-l1" x="{x + 70}" y="{y + 9}" width="{w - 140}" height="14" rx="7"/><text class="il-tm" x="{x + w/2}" y="{y + 20}" text-anchor="middle">{url}</text>' if url else ""
    return (f'<rect class="il-card" x="{x}" y="{y}" width="{w}" height="{h}" rx="14"/><path class="il-line" d="M{x} {y + 32}h{w}"/>'
            f'<circle class="il-dot" cx="{x + 16}" cy="{y + 16}" r="4"/><circle class="il-dot" cx="{x + 30}" cy="{y + 16}" r="4"/><circle class="il-dot" cx="{x + 44}" cy="{y + 16}" r="4"/>{u}')
def _wrap(body, label):
    return (f'<svg class="illus" viewBox="0 0 560 420" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg">'
            f'<defs><linearGradient id="ilg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3B6BFF"/><stop offset="1" stop-color="#7C9BFF"/></linearGradient>'
            f'<linearGradient id="ilf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3B6BFF" stop-opacity=".35"/><stop offset="1" stop-color="#3B6BFF" stop-opacity="0"/></linearGradient></defs>'
            f'{body}</svg>')

def phone(label="Mobile app screens"):
    def ph(x, y, scr):
        return (f'<g class="il-float"><rect class="il-card" x="{x}" y="{y}" width="190" height="370" rx="30"/><rect class="il-l1" x="{x + 70}" y="{y + 12}" width="50" height="8" rx="4"/>{scr}'
                f'<rect class="il-l1" x="{x + 12}" y="{y + 322}" width="166" height="36" rx="12"/>'
                + "".join(f'<circle class="{"il-acc" if i == 0 else "il-dot"}" cx="{x + 38 + i * 38}" cy="{y + 340}" r="6"/>' for i in range(4)) + '</g>')
    a = (f'<text class="il-th" x="54" y="102">Good morning</text>{_bar(54, 114, 90, 7)}'
         f'<rect fill="url(#ilg)" x="54" y="136" width="150" height="86" rx="16"/><text class="il-tw" x="68" y="166">Your plan</text><rect class="il-wb" x="68" y="180" width="80" height="7" rx="3.5"/><rect class="il-wb" x="68" y="196" width="110" height="10" rx="5"/>'
         + "".join(f'<rect class="il-l1" x="54" y="{236 + i * 40}" width="150" height="32" rx="10"/><circle class="il-acc2" cx="72" cy="{252 + i * 40}" r="8"/>{_bar(88, 248 + i * 40, 70 - i * 12, 7)}' for i in range(2)))
    b = (f'<text class="il-th" x="324" y="102">Checkout</text>{_bar(324, 114, 70, 7)}'
         + "".join(f'<rect class="il-l1" x="324" y="{134 + i * 52}" width="150" height="44" rx="12"/><rect class="il-l2" x="334" y="{142 + i * 52}" width="28" height="28" rx="8"/>{_bar(372, 148 + i * 52, 70, 7)}{_bar(372, 160 + i * 52, 40, 6, "il-l1b")}' for i in range(2))
         + f'<path class="il-line" d="M324 252h150"/><text class="il-tm" x="324" y="276">Total</text>{_bar(424, 268, 50, 9, "il-l2")}{_btn(324, 292, 150, "Pay now", 34)}')
    return _wrap(ph(40, 30, a) + f'<g class="il-float il-d2">{ph(310, 30, b)}</g>', label)

def deck(label="Pitch deck slides"):
    back = '<rect class="il-card il-o5" x="96" y="40" width="400" height="240" rx="14"/><rect class="il-card il-o7" x="78" y="60" width="400" height="240" rx="14"/>'
    bars = "".join(f'<rect fill="url(#ilg)" class="il-grow" style="--i:{i}" x="{300 + i * 34}" y="{250 - h}" width="22" height="{h}" rx="5"/>' for i, h in enumerate([34, 52, 74, 104, 140]))
    front = (f'<g class="il-float"><rect class="il-card" x="60" y="82" width="400" height="240" rx="14"/><text class="il-tm" x="84" y="116">TRACTION</text>'
             f'<text class="il-th il-big" x="84" y="150">Growing every</text><text class="il-th il-big" x="84" y="178">month since launch</text>{_bar(84, 196, 150, 7)}{_bar(84, 210, 120, 7)}'
             f'{bars}<path class="il-line" d="M292 251h170"/><text class="il-tm" x="84" y="300">06 / 14</text></g>')
    strip = "".join(f'<rect class="il-card{" il-sel" if i == 2 else ""}" x="{70 + i * 84}" y="{344}" width="72" height="44" rx="8"/>{_bar(80 + i * 84, 356, 34, 5)}{_bar(80 + i * 84, 366, 50, 5, "il-l1b")}' for i in range(5))
    return _wrap(back + front + strip, label)

def site(label="Website build", tool="Webflow"):
    hero = (_win(30, 30, 380, 330, "yourcompany.com") + f'<text class="il-tm" x="54" y="70">LOGO</text>' + "".join(_bar(250 + i * 36, 64, 26, 6) for i in range(4))
            + f'<text class="il-th il-big" x="54" y="118">Websites that</text><text class="il-th il-big" x="54" y="146">turn visits into leads</text>{_bar(54, 162, 210, 7)}{_bar(54, 176, 170, 7)}{_btn(54, 196, 112, "Get a quote")}'
            + f'<rect fill="url(#ilf)" x="54" y="244" width="332" height="96" rx="12"/><path class="il-acc-line" d="M62 320c40-8 60-34 98-40s66 12 100-10 70-38 118-44"/>'
            + "".join(f'<rect class="il-l1" x="{54 + i * 112}" y="{350 - 6}" width="100" height="0" rx="0"/>' for i in range(3)))
    panel = (f'<g class="il-float il-d2"><rect class="il-card" x="350" y="120" width="180" height="220" rx="14"/><text class="il-tm" x="368" y="148">{tool.upper()} CMS</text>'
             + "".join(f'<rect class="il-l1" x="366" y="{162 + i * 40}" width="148" height="32" rx="8"/><rect class="{"il-acc" if i == 0 else "il-l2"}" x="374" y="{170 + i * 40}" width="16" height="16" rx="4"/>{_bar(398, 174 + i * 40, 80 - i * 14, 7)}' for i in range(4))
             + '</g>')
    badge = _chip(54, 376, "Lighthouse 95+", "il-chip il-ok") + _chip(186, 376, "Schema + SEO") + _chip(300, 376, "Editable CMS")
    return _wrap(hero + panel + badge, label)

def store(label="Shopify store product page"):
    w = (_win(30, 30, 500, 330, "yourstore.com/products/classic") + '<rect class="il-l1" x="54" y="62" width="210" height="270" rx="12"/><rect fill="url(#ilg)" opacity=".55" x="94" y="112" width="130" height="160" rx="60"/>'
         + "".join(f'<rect class="{"il-sel" if i == 0 else "il-l2"}" x="{58 + i * 52}" y="{296 - 0}" width="0" height="0"/>' for i in range(4))
         + f'<text class="il-tm" x="288" y="82">NEW SEASON</text><text class="il-th il-big" x="288" y="112">Classic Jacket</text>{_bar(288, 126, 70, 9, "il-l2")}'
         + "".join(f'<rect class="{"il-acc" if i == 1 else "il-l1"}" x="{288 + i * 44}" y="150" width="36" height="28" rx="8"/>' for i in range(4))
         + f'{_bar(288, 194, 200, 7)}{_bar(288, 208, 170, 7)}{_btn(288, 230, 216, "Add to cart", 38)}'
         + "".join(f'<circle class="il-acc2" cx="{296 + i * 70}" cy="{298}" r="7"/>{_bar(308 + i * 70, 294, 46, 7, "il-l1b")}' for i in range(3)))
    cart = f'<g class="il-float il-d2"><rect class="il-card" x="380" y="300" width="150" height="80" rx="14"/><circle class="il-acc" cx="408" cy="340" r="14"/><text class="il-tb" x="408" y="345" text-anchor="middle">2</text>{_bar(432, 330, 70, 7)}{_bar(432, 344, 50, 7, "il-l1b")}</g>'
    return _wrap(w + cart, label)

def dash(label="Web app dashboard"):
    w = _win(20, 30, 520, 340, "app.yourproduct.com")
    side = '<rect class="il-l1" x="20" y="62" width="110" height="308"/>' + "".join(f'<rect class="{"il-acc" if i == 0 else "il-l2"}" x="36" y="{84 + i * 30}" width="{70 if i else 78}" height="{14}" rx="7"/>' for i in range(6))
    kpi = "".join(f'<rect class="il-l1" x="{148 + i * 128}" y="78" width="116" height="64" rx="10"/>{_bar(160 + i * 128, 92, 50, 6, "il-l1b")}{_bar(160 + i * 128, 108, 70, 12, "il-l2")}' for i in range(3))
    chart = ('<rect class="il-l1" x="148" y="156" width="372" height="120" rx="10"/><path fill="url(#ilf)" d="M160 262 L210 236 L260 244 L310 214 L360 222 L410 190 L460 196 L508 170 L508 268 L160 268Z"/>'
             '<path class="il-acc-line il-draw" d="M160 262 L210 236 L260 244 L310 214 L360 222 L410 190 L460 196 L508 170"/>')
    rows = "".join(f'<path class="il-line" d="M148 {300 + i * 22}h372"/>{_bar(160, 292 + i * 22, 90, 6)}{_bar(300, 292 + i * 22, 60, 6, "il-l1b")}<rect class="{"il-ok-b" if i % 2 == 0 else "il-warn-b"}" x="440" y="{289 + i * 22}" width="56" height="12" rx="6"/>' for i in range(3))
    return _wrap(w + side + kpi + chart + rows, label)

def cleanup(label="AI MVP cleanup review"):
    w = _win(20, 30, 330, 340, "src/app/page.tsx")
    code = "".join(f'<text class="il-tm" x="34" y="{80 + i * 22}">{i + 1}</text><rect class="{c}" x="56" y="{72 + i * 22}" width="{wd}" height="8" rx="4"/>'
                   for i, (wd, c) in enumerate([(120, "il-l2"), (200, "il-l1b"), (150, "il-bad-b"), (230, "il-l1b"), (90, "il-l2"), (180, "il-ok-b"), (210, "il-l1b"), (140, "il-l1b"), (170, "il-ok-b"), (100, "il-l2"), (220, "il-l1b"), (130, "il-l1b")]))
    items = [("il-bad", "API key exposed", "Moved to server"), ("il-warn", "No access rules", "Row-level security on"), ("il-warn", "6 button styles", "One design system"), ("il-ok", "Slow first load", "Images and queries fixed")]
    cards = "".join(f'<g class="il-float" style="--i:{i}"><rect class="il-card" x="300" y="{48 + i * 82}" width="240" height="68" rx="12"/><circle class="{c}" cx="322" cy="{70 + i * 82}" r="6"/>'
                    f'<text class="il-ts il-strike" x="336" y="{74 + i * 82}">{a}</text><path class="il-ok-line" d="M318 {94 + i * 82} l5 5 9-10"/><text class="il-tb2" x="340" y="{102 + i * 82}">{b}</text></g>'
                    for i, (c, a, b) in enumerate(items))
    return _wrap(w + code + cards, label)

def search(label="Google result and AI answer citing your site"):
    serp = (_win(20, 30, 300, 260, "google.com/search")
            + '<rect class="il-l1" x="38" y="54" width="264" height="26" rx="13"/>'
            + "".join(f'<text class="il-tm" x="40" y="{108 + i * 62}">{u}</text><text class="{"il-tlink" if i == 0 else "il-ts"}" x="40" y="{126 + i * 62}">{t}</text>{_bar(40, 134 + i * 62, 220, 6, "il-l1b")}'
                      for i, (u, t) in enumerate([("yourcompany.com", "Your service, explained clearly"), ("competitor.com", "Another result"), ("directory.com", "Top 10 list")])))
    ai = (f'<g class="il-float il-d2"><rect class="il-card il-glow" x="250" y="150" width="290" height="230" rx="16"/><circle fill="url(#ilg)" cx="276" cy="178" r="11"/><text class="il-th" x="296" y="183">AI answer</text>'
          + "".join(_bar(268, 204 + i * 16, [250, 230, 244, 180][i], 7, "il-l2" if i < 3 else "il-l1b") for i in range(4))
          + _chip(268, 278, "1  yourcompany.com", "il-chip il-cite") + _chip(268, 310, "2  guide") + _chip(352, 310, "3  docs")
          + f'{_bar(268, 350, 200, 6, "il-l1b")}</g>')
    return _wrap(serp + ai, label)

def funnel(label="Conversion funnel with an A/B test"):
    st = [("Visitors", 300), ("Viewed offer", 236), ("Started form", 160), ("Became leads", 104)]
    f = "".join(f'<g class="il-grow-x" style="--i:{i}"><rect fill="url(#ilg)" opacity="{1 - i * .16:.2f}" x="{170 - w / 2 + 60}" y="{50 + i * 62}" width="{w}" height="46" rx="10"/>'
                f'<text class="il-tw" x="{230}" y="{78 + i * 62}" text-anchor="middle">{n}</text></g>' for i, (n, w) in enumerate(st))
    ab = (f'<g class="il-float il-d2"><rect class="il-card" x="390" y="60" width="150" height="130" rx="14"/><text class="il-tm" x="406" y="86">VARIANT A</text>{_bar(406, 98, 110, 7)}{_bar(406, 112, 80, 7, "il-l1b")}<rect class="il-l2" x="406" y="132" width="70" height="22" rx="11"/></g>'
          f'<g class="il-float"><rect class="il-card il-glow" x="390" y="206" width="150" height="130" rx="14"/><text class="il-tm" x="406" y="232">VARIANT B</text>{_bar(406, 244, 110, 7)}{_bar(406, 258, 80, 7, "il-l1b")}{_btn(406, 276, 90, "Winner", 24)}</g>')
    return _wrap(f + ab + _chip(60, 372, "Heatmaps") + _chip(150, 372, "Recordings") + _chip(256, 372, "A/B tests"), label)

def audit(label="UX audit with annotated issues"):
    w = (_win(20, 30, 320, 340, "yourcompany.com") + f'<text class="il-th il-big" x="44" y="100">Headline that</text><text class="il-th il-big" x="44" y="126">says too little</text>{_bar(44, 144, 200, 7)}{_bar(44, 158, 160, 7)}'
         f'<rect class="il-l2" x="44" y="180" width="96" height="28" rx="14"/><rect class="il-l1" x="44" y="226" width="272" height="120" rx="10"/>')
    pins = "".join(f'<circle class="{c} il-pulse" style="--i:{i}" cx="{x}" cy="{y}" r="12"/><text class="il-tb" x="{x}" y="{y + 4}" text-anchor="middle">{i + 1}</text>' for i, (x, y, c) in enumerate([(262, 112, "il-bad"), (152, 194, "il-warn"), (300, 288, "il-warn")]))
    notes = [("il-bad", "High impact", "Value is unclear"), ("il-warn", "Medium", "CTA has low contrast"), ("il-warn", "Medium", "Proof is too far down")]
    cards = "".join(f'<g class="il-float" style="--i:{i}"><rect class="il-card" x="330" y="{60 + i * 100}" width="210" height="84" rx="12"/><circle class="{c}" cx="352" cy="{84 + i * 100}" r="10"/>'
                    f'<text class="il-tb" x="352" y="{88 + i * 100}" text-anchor="middle">{i + 1}</text><text class="il-tm" x="370" y="{88 + i * 100}">{a.upper()}</text><text class="il-ts" x="348" y="{116 + i * 100}">{b}</text>{_bar(348, 126 + i * 100, 120, 6, "il-l1b")}</g>'
                    for i, (c, a, b) in enumerate(notes))
    return _wrap(w + pins + cards, label)

KINDS = {"audit": audit,"phone": phone, "deck": deck, "site": site, "store": store, "dash": dash, "cleanup": cleanup, "search": search, "funnel": funnel}

def illus(kind, **kw):
    return KINDS[kind](**kw)
