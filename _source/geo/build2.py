import json, math
import numpy as np
from matplotlib.path import Path
g50=json.load(open("countries.json")); g=json.load(open("c110.json"))
# land dots from 50m (any country), Spain flagged
polys=[]
for f in g50["features"]:
    geom=f["geometry"]
    if not geom: continue
    ps=geom["coordinates"] if geom["type"]=="MultiPolygon" else [geom["coordinates"]]
    for poly in ps:
        r=np.array(poly[0]); polys.append((Path(r),r[:,0].min(),r[:,0].max(),r[:,1].min(),r[:,1].max(),1 if f["properties"]["name"]=="Spain" else 0))
N=26000; pts=[]; ga=math.pi*(3-math.sqrt(5))
for i in range(N):
    y=1-2*(i+.5)/N; lat=math.degrees(math.asin(y)); lon=math.degrees((i*ga)%(2*math.pi))-180
    if lat<-60: continue
    for p,x0,x1,y0,y1,c in polys:
        if x0<=lon<=x1 and y0<=lat<=y1 and p.contains_point((lon,lat)):
            pts+=[round(lat*10),round(lon*10),c]; break
# borders + centroids from 110m, all countries
C=[]
for f in g["features"]:
    n=f["properties"]["name"]; geom=f["geometry"]
    if not geom or n=="Antarctica": continue
    ps=geom["coordinates"] if geom["type"]=="MultiPolygon" else [geom["coordinates"]]
    rings=[]; best=None; ba=0
    for poly in ps:
        r=np.array(poly[0]); a=(r[:,0].max()-r[:,0].min())*(r[:,1].max()-r[:,1].min())
        if a<0.6: continue
        step=max(1,len(r)//90); rr=r[::step]
        rings.append([[round(float(y),1),round(float(x),1)] for x,y in rr])
        if a>ba: ba=a; best=r
    if not rings: continue
    # centroid: polygon area centroid of largest ring
    x=best[:,0]; y=best[:,1]; cr=x*np.roll(y,-1)-np.roll(x,-1)*y; A=cr.sum()/2
    cx=((x+np.roll(x,-1))*cr).sum()/(6*A) if A else x.mean(); cy=((y+np.roll(y,-1))*cr).sum()/(6*A) if A else y.mean()
    C.append([n.replace("United States of America","United States").replace("Dem. Rep.","DR").replace("Bosnia and Herz.","Bosnia"),round(float(cy),1),round(float(cx),1),rings,round(ba,1)])
print(len(pts)//3,len(C))
js="window.GEO="+json.dumps({"p":pts,"c":C},separators=(",",":"))+";"
open("WEBSITE_DIR/js/geo.js","w").write(js); print(len(js))
