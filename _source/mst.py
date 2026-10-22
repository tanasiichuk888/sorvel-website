import sys, glob
from PIL import Image
T = "/root/.claude/projects/-home-claude/bc3cd58f-2f95-5613-8857-c615c999697d/tool-results/"
S = 2.8
out, ks = sys.argv[1], sys.argv[2:]
t = [Image.open(glob.glob(T+"*"+k+".*")[0]).convert("RGB") for k in ks]
im = Image.new("RGB", (round(393*S), round(852*S)), "white")
pos = [(0,0),(157,0),(0,341),(157,341)]
for ti,(x,y) in zip(t,pos): im.paste(ti, (round(x*S), round(y*S)))
im = im.resize((786, 1704), Image.LANCZOS)
im.save(out, "WEBP", quality=90, method=6)
im.save("SOURCE_DIR/mprev.png"); print(out, im.size)
