import sys, glob
from PIL import Image
T = "/root/.claude/projects/-home-claude/bc3cd58f-2f95-5613-8857-c615c999697d/tool-results/"
out = sys.argv[1]
for a in sys.argv[2:]:
    n, k = a.split("=")
    f = glob.glob(T + "*" + k + ".*")[0]
    im = Image.open(f).convert("RGB"); im.save(f"{out}/{n}.webp", "WEBP", quality=90, method=6); print(n, im.size)
