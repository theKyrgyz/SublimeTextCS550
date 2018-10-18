# pilClassLucas4.py

""" objectives:
1. do a red/black checkerboard
2. thunderbolts down the screen

"""
import random
from PIL import Image, ImageDraw, ImageFont, ImageOps

imgx = 50*8
imgy = 50*8

checker = Image.new("RGBA",(imgx,imgy))

red = False

for sy in range(0,7):
    for sx in range(0,7):
        for cy in range(0,50):
            for cx in range(0,50):
                if red == False:
                    checker.putpixel((cx+(sx*50),cy+(sy*50)),(0,0,0))
                else:
                    checker.putpixel((cx+(sx*50),cy+(sy*50)),(255,0,0))
        red = not red

# checker.show()

# PYTHON IMAGE 2: ELECTRIC BOOGALOO

imgx = 200
imgy = 200

thunderbolt = Image.new("RGBA",(imgx,imgy))
thunderbolt.paste((0,0,0), (0,0,imgx,imgy))

LinesWanted = 40
for l in range(0,LinesWanted-1):
    touch = False
    a = random.randint(10,255)
    b = random.randint(10,255)
    c = random.randint(10,255)
    currentx = random.randint(1,imgx)
    currenty = 0
    while touch == False:
        thunderbolt.putpixel((currentx,currenty),(a,b,c))
        supervisor = random.randint(0,100)
        if (supervisor < 15) and (currentx > 0):
            currentx -= 1
        elif (supervisor > 85) and (currentx < imgx-1):
            currentx += 1
        else:
            currenty += 1
        if currenty == imgy:
            touch = True
thunderbolt.show()


