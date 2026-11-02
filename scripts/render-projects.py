from PIL import Image,ImageDraw,ImageFont,ImageFilter
from pathlib import Path
import math
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/freebox'
F='/usr/share/fonts/truetype/dejavu/DejaVuSans'
def font(n,b=False):return ImageFont.truetype(F+('-Bold' if b else '')+'.ttf',n)
specs=[('termux-agent','TERMUX AGENT','LOCAL AI / ANDROID','#1BC2A8','01'),('xnode-osint','XNODE OSINT','RESEARCH / PYTHON','#4FB0D6','02'),('vibe-chat','VIBE CHAT','TERMINAL / WEB UI','#F6B93B','03'),('netmon','NETMON','NETWORK / WINDOWS','#FF8A5C','04'),('wifi-audit','WIFI AUDIT','LOCAL PASSWORD AUDIT','#1BC2A8','05'),('lab-web','LAB / WEB','RED TEAM LAB','#4FB0D6','06')]
for name,title,sub,color,num in specs:
 frames=[]
 for k in range(48):
  im=Image.new('RGB',(520,160),'#0E1A1E');d=ImageDraw.Draw(im)
  d.rounded_rectangle((5,8,514,151),radius=24,fill='#102126',outline='#28413F',width=2)
  d.rounded_rectangle((17,20,502,139),radius=17,outline=color,width=1)
  # Moving perimeter pulse, continuous around the squircle-like outline.
  per=2*(485+119);pos=(k/48*per)
  def point(t):
   t%=per
   if t<485:return (17+t,20)
   t-=485
   if t<119:return (502,20+t)
   t-=119
   if t<485:return (502-t,139)
   return (17,139-(t-485))
  glow=Image.new('RGB',im.size);gd=ImageDraw.Draw(glow)
  pts=[point(pos-j) for j in range(50)]
  gd.line(pts,fill=color,width=5)
  glow=glow.filter(ImageFilter.GaussianBlur(5))
  from PIL import ImageChops
  im=ImageChops.add(im,glow);d=ImageDraw.Draw(im)
  d.line(pts[:18],fill=color,width=3)
  # Independent logo motion within a stationary icon tile.
  d.rounded_rectangle((33,44,99,111),18,fill='#16272B',outline=color,width=2)
  cx=66;cy=77
  if name=='telegram':
   a=math.sin(k*math.pi/24)*3
   d.polygon([(44,cy+a),(88,cy-17+a),(76,cy+21+a),(65,cy+7+a),(58,cy+17+a),(59,cy+3+a)],outline=color,width=2)
   d.line([(59,cy+3+a),(81,cy-12+a),(65,cy+7+a)],fill=color,width=2)
  elif name=='site':
   d.ellipse((45,56,87,98),outline=color,width=2);d.ellipse((57,56,75,98),outline=color,width=1)
   d.line((45,77,87,77),fill=color,width=1)
   dot=45+(k%24)*42/24;d.ellipse((dot-2,74,dot+2,78),fill='#EAF3F1')
  elif name not in ['site','support']:
   shift=int(math.sin(k*math.pi/24)*3)
   d.line([(57+shift,65),(45+shift,77),(57+shift,89)],fill=color,width=3)
   d.line([(75-shift,65),(87-shift,77),(75-shift,89)],fill=color,width=3)
   d.line((71,61,62,94),fill=color,width=2)
  else:
   r=1+0.08*math.sin(k*math.pi/12)
   pts=[(66+r*20*math.sin(t)**3,79-r*(16*math.cos(t)-6*math.cos(2*t)-3*math.cos(3*t)-math.cos(4*t))) for t in [i*math.pi/40 for i in range(81)]]
   d.line(pts,fill=color,width=2)
  d.text((121,43),title,font=font(25,True),fill='#EAF3F1')
  d.text((122,84),sub,font=font(13),fill=color)
  d.text((475,28),num,font=font(10),fill=color)
  # Three trailing arrowheads: each illuminates in sequence, with a gentle drift.
  for j in range(3):
   active=(k//5)%3==j
   c=color if active else '#28413F';x=425+j*18+3*math.sin(k*math.pi/24)
   d.line([(x,65),(x+10,77),(x,89)],fill=c,width=4 if active else 2)
  frames.append(im)
 path=OUT/('project-'+name+'.gif')
 frames[0].save(path,save_all=True,append_images=frames[1:],loop=0,duration=60,optimize=True)
 with Image.open(path) as test:
  assert test.n_frames==48 and test.info['loop']==0
 print(path.name,path.stat().st_size)
