import sys, glob
from PIL import Image
T="/root/.claude/projects/-home-claude/bc3cd58f-2f95-5613-8857-c615c999697d/tool-results/"
out=sys.argv[1]; keys=sys.argv[2:]
t=[Image.open(glob.glob(T+'*'+k+'.*')[0]).convert('RGB') for k in keys]; im=Image.new('RGB',(1600,1000))
for i,ti in enumerate(t): im.paste(ti,((i%2)*800,(i//2)*500))
im.save(out,'WEBP',quality=90,method=6); print(out)
