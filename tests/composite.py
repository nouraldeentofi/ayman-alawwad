from PIL import Image, ImageDraw, ImageFilter
S="tests/shots/"
BG=(232,225,214)
def rounded(im, r):
    m=Image.new('L', im.size, 0); ImageDraw.Draw(m).rounded_rectangle([0,0,im.size[0]-1,im.size[1]-1], r, fill=255)
    out=Image.new('RGBA', im.size); out.paste(im, (0,0), m); return out
def place(canvas, im, xy, r):
    im=rounded(im.convert('RGB'), r)
    sh=Image.new('RGBA', (im.size[0]+80, im.size[1]+80), (0,0,0,0))
    ImageDraw.Draw(sh).rounded_rectangle([40,52,40+im.size[0],52+im.size[1]], r, fill=(60,40,30,70))
    sh=sh.filter(ImageFilter.GaussianBlur(22))
    canvas.alpha_composite(sh, (xy[0]-40, xy[1]-40)); canvas.alpha_composite(im, xy)
# phones
files=["vp-p1-light","vp-p3-light","vp-p4-light","vp-p5-light","vp-p6-light","vp-p7-light","vp-p1-dark","vp-p2-dark"]
pw,ph=390,844; gap=56; pad=80
W=pad*2+4*pw+3*gap; H=pad*2+2*ph+gap
c=Image.new('RGBA',(W,H),BG+(255,))
for i,f in enumerate(files):
    im=Image.open(S+f+".png").resize((pw,ph), Image.LANCZOS)
    place(c, im, (pad+(i%4)*(pw+gap), pad+(i//4)*(ph+gap)), 38)
c.convert('RGB').save("preview/ayman-phone-preview.png", optimize=True)
# desktop
files=["vd-d1-light","vd-d1-dark","vd-d2-light","vd-d3-light","vd-d4-light","vd-d6-light"]
dw,dh=960,600; gap=56; pad=80
W=pad*2+2*dw+gap; H=pad*2+3*dh+2*gap
c=Image.new('RGBA',(W,H),BG+(255,))
for i,f in enumerate(files):
    im=Image.open(S+f+".png").resize((dw,dh), Image.LANCZOS)
    place(c, im, (pad+(i%2)*(dw+gap), pad+(i//2)*(dh+gap)), 18)
c.convert('RGB').save("preview/ayman-desktop-preview.png", optimize=True)
print("ok")
