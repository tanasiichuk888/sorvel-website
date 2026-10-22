import re, sys
sys.path.insert(0, ".")
from common import *
def patch(rel, p, active=""):
    f = ROOT + rel; s = open(f).read()
    a = s.index('  <header class="nav"'); b = s.index("  </header>\n", a) + len("  </header>\n")
    s = s[:a] + nav(p, active) + s[b:]
    a = s.index('  <footer class="foot">'); b = s.index("  </footer>\n", a) + len("  </footer>\n")
    s = s[:a] + footer(p) + s[b:]
    if "pages.css" not in s:
        anchor = f'  <link rel="stylesheet" href="{p}css/case.css" />\n' if "case.css" in s else f'  <link rel="stylesheet" href="{p}css/style.css" />\n'
        s = s.replace(anchor, anchor + f'  <link rel="stylesheet" href="{p}css/pages.css" />\n')
    s = s.replace('href="../index.html#contact"', 'href="../contact.html"').replace('href="../index.html#work-list"', 'href="../work.html"')
    import re as _re
    s = _re.sub(r'  <link rel="icon" href="data:[^"]*" />\n', f'  <link rel="icon" href="{p}img/brand/favicon.svg" type="image/svg+xml" />\n  <link rel="icon" href="{p}img/brand/favicon-32.png" sizes="32x32" type="image/png" />\n  <link rel="apple-touch-icon" href="{p}img/brand/apple-touch-icon.png" />\n', s)
    open(f, "w").write(s); print("patched", rel)
for c in ["valhalla-capital", "serverscamp", "arlowe-baxter", "salinas-defense", "awswrap"]:
    patch(f"work/{c}.html", "../", "work")
patch("index.html", "")
# home: link each service accordion item to its page
f = ROOT + "index.html"; s = open(f).read()
order = ["websites", "product-design", "brand-identity", "landing-pages", "migrations"]
names = {"websites": "websites", "product-design": "product design", "brand-identity": "brand identity", "landing-pages": "landing pages", "migrations": "migrations"}
if "svc__more" not in s:
    parts = s.split('</ul>\n              </div></div>\n            </li>')
    assert len(parts) == 6, len(parts)
    out = parts[0]
    for i, slug in enumerate(order):
        out += f'</ul>\n                <a class="svc__more" href="services/{slug}.html">More about {names[slug]} <span aria-hidden="true">→</span></a>\n              </div></div>\n            </li>' + parts[i + 1]
    s = out
open(f, "w").write(s)
