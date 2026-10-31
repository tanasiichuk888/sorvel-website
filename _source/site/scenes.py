"""Animated illustrations for inner-page heroes (styled by css/scenes.css + css/svc.css, driven by js/scenes.js + js/svc.js)."""
import re

_SVC = open("SOURCE_DIR/svc_markup.html").read()
_CHUNKS = re.split(r"\n\s*<!-- \d [^>]*-->\n", _SVC)[1:]
_CHUNKS[-1] = _CHUNKS[-1].rsplit("          </div>", 1)[0]
SVC_KEYS = ["websites", "product-design", "brand-identity", "landing-pages", "migrations"]


def svc(slug):
    html = _CHUNKS[SVC_KEYS.index(slug)].strip()
    if "is-on" not in html.split(">", 1)[0]:
        html = html.replace('class="vis ', 'class="vis is-on ', 1)
    return f'<div class="svc__stage sx-stage" aria-hidden="true">\n{html}\n</div>'


def flow():
    return '''<div class="sx sx-flow" data-scene="flow" data-loop="11000" aria-hidden="true">
  <div class="fl-line"><i></i></div>
  <div class="fl-step fl-1"><span class="fl-when">Day 0</span>
    <div class="fl-card fl-msg"><span class="fl-ava">J</span><div><b>Jane · Acme</b><p class="fl-type" data-text="Hi! We need a new site for our SaaS. Launch is in May.">&nbsp;</p></div><span class="fl-time">09:12</span></div></div>
  <div class="fl-step fl-2"><span class="fl-when">Within 24h</span>
    <div class="fl-card fl-doc"><div class="fl-doc__ic"></div><div class="fl-doc__body"><b>Project plan.pdf</b><i></i><i></i><i></i>
      <div class="fl-doc__meta"><span>Fixed price <b>$6,900</b></span><span>Timeline <b>4 weeks</b></span></div></div></div></div>
  <div class="fl-step fl-3"><span class="fl-when">Weeks 1–3</span>
    <div class="fl-card fl-fig"><div class="fl-fig__frame"><b></b><i></i><i></i><u></u><s></s>
      <span class="fl-pin p1">1</span><span class="fl-pin p2">2</span></div>
      <div class="fl-cmt"><span class="fl-ava">J</span><p>Love it. Approved ✓</p></div></div></div>
  <div class="fl-step fl-4"><span class="fl-when">Launch</span>
    <div class="fl-card fl-live"><span class="fl-check"></span><div><b>acme.com is live</b><small>Design ✓ · Build ✓ · QA ✓</small></div></div></div>
</div>'''


def inbox():
    return '''<div class="sx sx-inbox" data-scene="inbox" data-loop="11000" aria-hidden="true">
  <div class="ib-win">
    <div class="ib-head"><span class="ib-ava">AC</span><div><b>Sorvel Studio</b><small><i></i>Usually replies in 10 minutes</small></div></div>
    <div class="ib-body">
      <div class="ib-msg ib-me"><p class="ib-type" data-text="Hi! We're a fintech startup and need a new marketing site in Webflow. Can you help?">&nbsp;</p><span class="ib-tick">Delivered ✓✓</span></div>
      <div class="ib-typing"><i></i><i></i><i></i></div>
      <div class="ib-msg ib-them"><p>Absolutely. Here's a written plan, timeline and fixed price for your review.</p>
        <div class="ib-files"><span><i class="f1"></i>Plan.pdf</span><span><i class="f2"></i>Timeline</span><span><i class="f3"></i>$6,900 fixed</span></div></div>
    </div>
    <div class="ib-input"><span>Write a message…</span><b></b></div>
  </div>
  <div class="ib-clock"><svg viewBox="0 0 44 44"><circle cx="22" cy="22" r="19"/><circle class="g" cx="22" cy="22" r="19"/></svg><div><b><span data-to="3">0</span>h <span data-to="12">0</span>m</b><small>to a written reply</small></div></div>
</div>'''


def globe():
    return '''<script src="js/geo.js?v=2"></script>
<div class="sx sx-globe" data-scene="globe" data-loop="0" aria-hidden="true">
  <canvas class="gl-c"></canvas>
</div>'''


def rate(quotes):
    q = "".join(f'<figure class="rt-q" style="--i:{i}"><div class="rt-stars"><i></i><i></i><i></i><i></i><i></i></div><p>{t}</p><figcaption>{w}</figcaption></figure>' for i, (t, w) in enumerate(quotes))
    return f'''<div class="sx sx-rate" data-scene="rate" data-loop="12000" aria-hidden="true">
  <div class="rt-score"><b><span data-to="5" data-dec="1">0</span></b><div class="rt-big"><i></i><i></i><i></i><i></i><i></i></div><small>Average across every client review</small>
    <div class="rt-dist"><span>5★</span><i><u></u></i><em>100%</em></div></div>
  <div class="rt-stack">{q}</div>
  <div class="rt-foot"><span class="rt-avas"><i>V</i><i>R</i><i>S</i><i>B</i><i>A</i><i>M</i></span><span><b>600+</b> five-star reviews on Upwork and Fiverr Pro</span></div>
</div>'''


def fan(p, cases):
    cards = "".join(f'<figure class="fn-card" style="--i:{i}"><img src="{p}img/work/{img}" alt="" loading="lazy" width="1600" height="1000"><figcaption><b>{n}</b><span>{t}</span></figcaption></figure>' for i, (img, n, t) in enumerate(cases))
    return f'''<div class="sx sx-fan" data-scene="fan" data-loop="0" aria-hidden="true">
  <div class="fn-deck">{cards}</div>
  <div class="fn-dots">{"".join("<i></i>" for _ in cases)}</div>
</div>'''


def wall(p, cols):
    """Tilted wall of real project screens, 3 columns looping vertically (pure CSS)."""
    out = []
    for ci, col in enumerate(cols):
        tiles = "".join(
            f'<a class="wl-tile" href="{p}work/{href}.html" tabindex="-1"><img src="{p}img/work/{img}" alt="" loading="{"eager" if k < 2 else "lazy"}" width="1600" height="1000"><span><b>{name}</b>{tag}</span></a>'
            for k, (img, name, tag, href) in enumerate(col + col))
        out.append(f'<div class="wl-col" style="--i:{ci}"><div class="wl-track">{tiles}</div></div>')
    return f'''<div class="sx-wall" aria-hidden="true">
  <div class="wl-plane">{"".join(out)}</div>
</div>'''
