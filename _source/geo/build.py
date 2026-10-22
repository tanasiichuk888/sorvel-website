import json, math
import numpy as np
from matplotlib.path import Path
g=json.load(open("countries.json"))
HL={"Spain":0,"United States of America":1,"Canada":2,"Uruguay":3,"Austria":4,"Iceland":5,"Saudi Arabia":6,"Zimbabwe":7,"United Kingdom":8,"Germany":9,"Belgium":10}
polys=[]  # (path,bbox,code)
outlines={}
for f in g["features"]:
    n=f["properties"]["name"]; geom=f["geometry"]
    if not geom: continue
    ps=geom["coordinates"] if geom["type"]=="MultiPolygon" else [geom["coordinates"]]
    code=HL.get(n,-1)+1
    for poly in ps:
        ring=np.array(poly[0])
        polys.append((Path(ring),ring[:,0].min(),ring[:,0].max(),ring[:,1].min(),ring[:,1].max(),code))
        if code and len(ring)>=12 and not (n=="United States of America" and ring[:,1].max()<30 and ring[:,0].min()<-150 and False):
            area=(ring[:,0].max()-ring[:,0].min())*(ring[:,1].max()-ring[:,1].min())
            if area<1.5 and n not in("Belgium",): continue
            step=max(1,len(ring)//160)
            r=ring[::step]
            outlines.setdefault(code,[]).append([[round(float(y),1),round(float(x),1)] for x,y in r])
N=26000; pts=[]
ga=math.pi*(3-math.sqrt(5))
for i in range(N):
    y=1-2*(i+.5)/N; lat=math.degrees(math.asin(y)); lon=math.degrees((i*ga)%(2*math.pi))-180
    if lat<-60: continue
    c=None
    for p,x0,x1,y0,y1,code in polys:
        if x0<=lon<=x1 and y0<=lat<=y1 and p.contains_point((lon,lat)):
            c=code; break
    if c is not None: pts+= [round(lat*10), round(lon*10), c]
print(len(pts)//3, {k:len(v) for k,v in outlines.items()})
js="window.GEO={p:"+json.dumps(pts,separators=(",",":"))+",o:"+json.dumps({str(k):v for k,v in outlines.items()},separators=(",",":"))+"};"
open("WEBSITE_DIR/js/geo.js","w").write(js)
print(len(js))
