from PIL import Image, ImageOps
src=Image.open('/root/.claude/uploads/9cac7207-2d1b-5bf4-969e-62974606aff5/2ea6720d-image.png').convert('RGB')
W,H=src.size; TH=round(W*290/214); extra=TH-H; top=extra//2; bot=extra-top
def fill(strip,n):
    out=Image.new('RGB',(W,n)); y=0; flip=False
    while y<n:
        s=ImageOps.flip(strip) if flip else strip
        out.paste(s,(0,y)); y+=strip.height; flip=not flip
    return out
ts=src.crop((0,4,W,64)); bs=src.crop((0,1278,W,1326))
canvas=Image.new('RGB',(W,TH))
t=fill(ts,top); canvas.paste(ImageOps.flip(t),(0,0))
canvas.paste(src,(0,top))
canvas.paste(fill(ImageOps.flip(bs),bot),(0,top+H))
# crop off any strip of the original 1-2px edges
canvas=canvas.resize((900,round(900*TH/W)),Image.LANCZOS)
d='/home/claude/site/beer-passport/'
canvas.save(d+'cover.webp',quality=82,method=6); canvas.save(d+'cover.jpg',quality=84,optimize=True,progressive=True)
canvas.resize((428,580),Image.LANCZOS).save(d+'cover-sm.webp',quality=82,method=6)
canvas.save('/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/cover_preview.png')
print(canvas.size)
