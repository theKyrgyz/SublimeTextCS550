# Class2
# doing Mandelbrot together. SO MUCH MORE EFFICIENT.
from PIL import Image, ImageFilter
import random, getpass
from datetime import date, datetime

print(datetime.now().month, datetime.now().day)
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
blueLetters = [180,102,70,47,0,185,222,100,0,112,150,94,63,100,0,50,0,25,135,208,37,205,213,74,74,12]

xmin, xmax = -0.725935500641975308344, -0.725860250864197530669
ymin, ymax = 0.240865921580246913788, 0.240922415407407407538
imgx, imgy = 1000,1000
maxIt = 256

username = list(getpass.getuser().lower())

def mandelbrot(specify,VALCOL):
    for y in range(imgy):
        cy = ((ymax-ymin)/(imgy-1))*y + ymin 
        # only doing it once per row... smart
        for x in range(imgx):
            cx = ((xmax-xmin)/(imgx-1))*x + xmin
            # complex numbers:
            c = complex(cx,cy)
            z = 0
            for i in range(maxIt):
                global iCon
                iCon = i
                if abs(z) > 2.0:
                    break
                z = z**2 + c
            if VALCOL == "M2":
                r = (iCon%30)*7
                g = abs(iCon-5)
                b = int(iCon**(1/2))*2
            else:
                r = iCon
                g = (iCon*10)%3
                b = int(iCon+((datetime.now().day)%7))
            specify.putpixel((x,y),(r,g,b))

def julia(specify,cval,VALCOL):
    for y in range(imgy):
        yJ = ((ymax-ymin)/(imgy-1))*y + ymin 
        # only doing it once per row... smart
        for x in range(imgx):
            xJ = ((xmax-xmin)/(imgx-1))*x + xmin
            # complex numbers:
            z = complex(xJ,yJ)
            for i in range(maxIt):
                global iCon
                iCon = i
                if abs(z) > 2.0:
                    break
                z = z**2 + cval
                # print(iCon)
                # print(z)
            if VALCOL == "J1":
                r = ((iCon%30)*7)+40
                g = abs(iCon-5)
                if username[0] in letters:
                    for s in range(len(letters)):
                        if username[0] == letters[s]:
                            b = abs(blueLetters[s])
                else:
                    b = abs(150-iCon)
                #print(r,g,b)
            if VALCOL == "J2":
                r = ((iCon%30)*7)+40
                g = ((int(xJ*100)%15)*3)+120
                if username[0] in letters:
                    for s in range(len(letters)):
                        if username[0] == letters[s]:
                            b = abs(blueLetters[s])
                else:
                    b = abs(150-iCon)
                #print(r,g,b)
            else:
                r = iCon
                g = (iCon*10)%3
                b = 256-iCon
            specify.putpixel((x,y),(r,g,b))

ImgC1 = Image.new("RGBA",(imgx,imgy))
ImgC1.paste((0,0,0), (0,0,imgx,imgy))
ImgC1.save("ImgC1.png","PNG")
VALCOL = "M1"
mandelbrot(ImgC1,"M1")
ImgC1.save("ImgC1.png","PNG")
ImgC1.show()

"""
xmin, xmax = -1.786400592936561140507, -1.786395803871461587019
ymin, ymax = -0.000002098513044253179, 0.000001493285780411937
ImgC3 = Image.new("RGBA",(imgx,imgy))
ImgC3.paste((0,0,0), (0,0,imgx,imgy))
ImgC3.save("ImgC3.png","PNG")
VALCOL = "M2"
mandelbrot(ImgC3,"M2")
ImgC3.save("ImgC3.png","PNG")
ImgC3.show()


xmin, xmax = 0.2, 0.25
ymin, ymax = -0.60, -0.55
imgx, imgy = 1500,1500
maxIt = 200
ImgC4 = Image.new("RGBA",(imgx,imgy))
ImgC4.paste((0,0,0), (0,0,imgx,imgy))
julia(ImgC4,complex(0.5,-0.3),"J1")
ImgC41 = ImgC4.filter(ImageFilter.EDGE_ENHANCE_MORE)
ImgC42 = ImgC4.filter(ImageFilter.CONTOUR)
ImgC4F = Image.blend(ImgC41, ImgC42, 0.05)
ImgC4F.save("ImgC4.png","PNG")
ImgC4F.show()
"""

xmin, xmax = 0.6, 0.7
ymin, ymax = 0.05, 0.15
imgx, imgy = 1000,1000
maxIt = 200
ImgC5 = Image.new("RGBA",(imgx,imgy))
julia(ImgC5,complex(-0.5,0.55),"J2")
ImgC5.save("ImgC5.png","PNG")
ImgC5.show()


