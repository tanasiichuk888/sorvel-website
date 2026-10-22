"""Rebuild the Sorvel website pages.

Usage (from this folder):  python3 build.py
Needs Python 3 + Pillow (pip install pillow).

The scripts contain two placeholders, SOURCE_DIR and WEBSITE_DIR.
This runner copies them to a temp folder, swaps in the real paths
(this folder and ../website) and runs them in the right order.
"""
import os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
WEBSITE = os.path.abspath(os.path.join(HERE, "..", "website"))
tmp = tempfile.mkdtemp(prefix="sorvel-build-")

for root, _, files in os.walk(HERE):
    for f in files:
        src = os.path.join(root, f)
        dst = os.path.join(tmp, os.path.relpath(src, HERE))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if f.endswith((".py", ".html")):
            s = open(src, encoding="utf-8").read().replace("SOURCE_DIR", tmp).replace("WEBSITE_DIR", WEBSITE)
            open(dst, "w", encoding="utf-8").write(s)
        else:
            shutil.copy(src, dst)

def run(script, cwd):
    print("→", script)
    subprocess.run([sys.executable, script], cwd=cwd, check=True)

site = os.path.join(tmp, "site")
# 1. inner pages (work, process, contact, pricing, about, reviews, legal, 404, services)
for s in ["main_pages.py", "rest.py", "services.py", "pricing.py"]:
    run(s, site)
# 2. case studies
for s in ["cc_page.py", "wa_page.py", "vc_page.py", "ci_page.py", "as_page.py", "vb_page.py"]:
    run(s, tmp)
# 3. "More work" block on every case page
run("remore_all.py", tmp)
# 4. SEO tags, structured data, sitemap.xml, robots.txt
subprocess.run([sys.executable, os.path.join(HERE, "seo.py")], check=True)
print("Done. Pages written to", WEBSITE)
