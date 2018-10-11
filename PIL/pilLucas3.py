# pilLucas3.py

from PIL import Image, ImageDraw, ImageFont, ImageOps
import random

imgx = 2853
imgy = 2024

a = Image.new("RGBA",(imgx,imgy))
a.paste((255,0,0), (0,0,imgx,imgy))
a.save("a.png","PNG")

b = Image.open("Pisca.png")

comp = Image.blend(a, b, 0.7)
print("\nZeroeth phase complete.")

d = comp.histogram()

e, f, g, h = comp.split()

i = ImageDraw.Draw(comp)

i.line(((0, 0) + (150, comp.size[1]+500)), fill="grey", width=300)
i.line((comp.size[0], comp.size[1], comp.size[0]-150, -400), fill="grey", width=700)
comp.save("GrayCross.png", "PNG")

if (Image.open("bitmapNoise.png") == FileNotFoundError):
    k = Image.new("RGBA",(imgx,imgy))

    for kx in range(0,imgx):
        for ky in range(0,imgy):
            kr = random.randint(0,255)
            k.putpixel((kx,ky),(kr,kr,kr))

    k.save("bitmapNoise.png","PNG")
    k.show()
else:
    k = Image.open("bitmapNoise.png")

compTwo = comp
print("First phase complete.")

m = ImageDraw.Draw(compTwo)

airAmer = ImageFont.truetype("Air Americana.ttf", 400)

m.text(((imgx/2)-600, (imgy/2)-300), "WE ARE \nWATCHING.", fill="white", font=airAmer)

compTwo.save("NoiseAndMessage.png", "PNG")
print("Second phase complete.")

compThree = Image.blend(compTwo, k, 0.30)
print("Third phase complete.")

compFour = ImageOps.expand(compThree, border=45, fill="black")
compFour = compFour.resize((512,512), resample=Image.NEAREST)
print("Fourth phase complete.\n")
compFour.show()
compFour.save("WeAreWatching.png", "PNG")
