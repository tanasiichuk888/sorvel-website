import re, os
from PIL import Image
W = "WEBSITE_DIR/work/"
ROOT = "WEBSITE_DIR/"
ICONS = ('<svg viewBox="0 0 18 12" class="iphone__sig"><rect x="0" y="8" width="3" height="4" rx="1"/><rect x="5" y="5.5" width="3" height="6.5" rx="1"/><rect x="10" y="3" width="3" height="9" rx="1"/><rect x="15" y="0" width="3" height="12" rx="1"/></svg>'
         '<svg viewBox="0 0 16 12" class="iphone__wifi"><path d="M8 11.5 5.6 9a3.4 3.4 0 0 1 4.8 0zM3.5 6.9a6.4 6.4 0 0 1 9 0l-1.4 1.4a4.4 4.4 0 0 0-6.2 0zM1.3 4.7a9.5 9.5 0 0 1 13.4 0l-1.4 1.4a7.5 7.5 0 0 0-10.6 0z"/></svg>'
         '<span class="iphone__bat"><i></i></span>')
def bar_colors(src):
    im = Image.open(ROOT + src.replace("../", "")).convert("RGB")
    w, h = im.size
    px = im.crop((0, 0, w, max(4, h // 60))).resize((1, 1), Image.LANCZOS).getpixel((0, 0))
    lum = 0.2126 * px[0] + 0.7152 * px[1] + 0.0722 * px[2]
    return "#%02x%02x%02x" % px, ("#fff" if lum < 150 else "#0b0c0f")
def repl(m):
    cls, attrs, src, imgattrs = m.group(1), m.group(2), m.group(3), m.group(4)
    sb, sbc = bar_colors(src)
    imgattrs = re.sub(r'width="\d+" height="\d+"', 'width="393" height="852"', imgattrs)
    return (f'<div class="{cls} iphone"{attrs} style="--sb:{sb};--sbc:{sbc}">'
            f'<span class="iphone__key iphone__key--action"></span><span class="iphone__key iphone__key--up"></span><span class="iphone__key iphone__key--down"></span><span class="iphone__key iphone__key--power"></span><span class="iphone__key iphone__key--cam"></span>'
            f'<span class="iphone__rim"><span class="iphone__bezel"><span class="iphone__screen">'
            f'<span class="iphone__bar"><b>9:41</b><span class="iphone__island"></span><span class="iphone__icons">{ICONS}</span></span>'
            f'<img src="{src}"{imgattrs}></span></span></span></div>')
for f in sorted(os.listdir(W)):
    p = W + f; s = open(p).read()
    s2, n = re.subn(r'<div class="(cs-phone(?: cs-phone--2)?|cs-cover__phone)"([^>]*)><img src="([^"]+)"([^>]*)></div>', repl, s)
    open(p, "w").write(s2); print(f, n)
