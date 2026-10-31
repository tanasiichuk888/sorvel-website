from PIL import Image, ImageFilter
import os
T="/root/.claude/projects/-home-claude/bc3cd58f-2f95-5613-8857-c615c999697d/tool-results/mcp-Figma-blob-%s.png"
W="/mnt/user-data/outputs/site/website/img/work/"
P={
"noir":("1793447703062-ce4k1w","1793448392169-xs2klr",[888,1543,2634,3594]),
"skyli":("1793447713263-z7jf28","1793449171511-y3x46r",[909,2626,5494,1555]),
"open-select":("1793447720845-ivctiz","1793449199079-ghpum3",[1369,6813,8895,5355]),
"copliancy":("1793447845552-u1fmqk","1793449202209-b4700e",[793,1483,2534,3110]),
"visit-pemba":("1793448225807-kaqlt6","1793449184361-677b39",[1058,1575,2048,3060]),
"agentur":("1793448235609-nv34ms","1793449181874-nelvw3",[574,1058,1845,3746]),
"mutmachbuch":("1793448245533-cqtqiq","1793449191149-bdh346",[1035,1635,3045,3585]),
"wehike":("1793448379931-o60mcb","1793449193083-ezwfl5",[1100,1780,3000,690]),
}
def save(im,path,w=1600):
    if im.width!=w: im=im.resize((w,round(im.height*w/im.width)),Image.LANCZOS)
    im.save(path,quality=84,method=6)
for k,(d,m,ys) in P.items():
    os.makedirs(W+k,exist_ok=True)
    D=Image.open(T%d).convert("RGB"); w=D.width; h=round(w*.625)
    save(D.crop((0,0,w,h)),W+k+"/hero.webp")
    for i,y in enumerate(ys,1):
        y=min(y,D.height-h); save(D.crop((0,y,w,y+h)),W+k+f"/s{i}.webp")
    M=Image.open(T%m).convert("RGB")
    mw=M.width; mh=round(mw/0.4613)
    if M.height>=mh: M2=M.crop((0,0,mw,mh))
    else:
        M2=Image.new("RGB",(mw,mh),M.getpixel((mw//2,M.height-2))); M2.paste(M,(0,0))
    save(M2,W+k+"/m-hero.webp",786)
    # figma canvas: full desktop + mobile column on dark board
    C=Image.new("RGB",(1600,1113),(30,30,30))
    dh=1033; dw=round(D.width*dh/D.height)
    if dw>1100: dw=1100; dh=round(D.height*dw/D.width)
    C.paste(D.resize((dw,dh),Image.LANCZOS),(40,40))
    mm=M2.resize((round(M2.width*600/M2.height),600),Image.LANCZOS)
    C.paste(mm,(40+dw+60,40))
    C.save(W+k+"/figma.webp",quality=82)
print("ok")
