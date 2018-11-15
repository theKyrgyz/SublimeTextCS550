# filter.py
# https://stackoverflow.com/questions/9701515/filter-part-of-image-using-pil-python

# IMPORTS
import sys, imghdr, colorsys
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter

# SIMPLIFYING SYS.ARGV
def commandCall(argNum):
    return sys.argv[int(argNum)]

baseImg = Image.open(commandCall(1))
baseStr = commandCall(1)
acceptList = ["png","jpeg","jpg"]

if not ( (imghdr.what(baseStr)) in acceptList):
    print("Invalid image format.")
    quit()
else:
    print("Acceptable image format. Continuing...")

baseImg.save('basePNG.png','PNG')
basePNG = Image.open('basePNG.png')

# basePNG.show()

modifyA = basePNG.filter(ImageFilter.MedianFilter(5))
# modifyA.show()

width, height = basePNG.size

"""
baseForCrop = Image.open('basePNG.png')
box = (0,0,int(width*(2/3)),int(height*(2/3)))
Bcrop1 = basePNG.crop(box)
BcropEd = Bcrop1.filter(ImageFilter.MedianFilter(15))
baseForCrop.paste(BcropEd, box)
modifyB = baseForCrop
# modifyB.show()
"""

baseHSV = basePNG.convert('HSV')
# baseHSV.show()



modifyC = baseHSV
modifyD = modifyC

baseLoaded = basePNG.load()

"""
for y in range(basePNG.size[1]):
    for x in range(basePNG.size[0]):
        color = tuple(baseLoaded[x, y])
        h, s, v = colorsys.rgb_to_hsv(color[0],color[1],color[2])
        h = h
        s = s * 0.8
        v = v * 0.9
        r, g, b = colorsys.hsv_to_rgb(h,s,v)
        modifyD.putpixel( (x,y), (int(r+200),int(g),int(b+200)) )

modifyD = modifyD.filter(ImageFilter.SMOOTH)
modifyD.show()
"""


for y in range(basePNG.size[1]):
    for x in range(basePNG.size[0]):
        color = tuple(baseLoaded[x, y])
        h, s, v = colorsys.rgb_to_hsv(color[0],color[1],color[2])
        h = h
        s = s * 0.8
        v = v * 0.9
        r, g, b = colorsys.hsv_to_rgb(h,s,v)
        modifyC.putpixel( (x,y), (int(r),int(abs(g-10)),int(b)) )

modifyC = modifyC.filter(ImageFilter.SMOOTH)
modifyC = modifyC.convert('RGB')
modifyC.save('finalFiltered.png','PNG')
modifyC.show()


