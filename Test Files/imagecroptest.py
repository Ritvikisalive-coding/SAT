from PIL import Image , ImageDraw, ImageOps

def make_circle(im):
    mask = Image.new("L", im.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0,0) + im.size, fill= 255)

    out = ImageOps.fit(im, mask.size, centering=(0.5,0.5))
    out.putalpha(mask)
    return out

with Image.open("Lego.jpeg") as im:
    im = im.convert("RGBA")
    circular_im = make_circle(im)
    circular_im.save("Cropped/Lego.png")
    print("cropped")