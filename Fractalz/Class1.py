# Class1.py for Fractalz - making a standard Mandelbrot fractal image
# DATE: October 18, 2018
# DESCRIPTION: A quick [bodged] code that creates a Mandelbrot fractal in a specified resolution.
# SOURCES: Just the assignment pdf with instructions.
# want: 512x512 image

from PIL import Image, ImageDraw
global cx,cy,ZcurrX,ZcurrY,boundLeft,boundRight,boundUp,boundDown,zNext,escape,iterationNumber

def escapeFunc():
    global iterationNumber,escape
    if ((zNext[0]**2) + (zNext[1]**2)) >= 4:
        # print("It's escaped at step",iterationNumber,"with coords",zNext)
        escape = True
    if iterationNumber > 254:
        # print("After 254 tries it hasn't escaped.")
        escape = True

def mandelbrot():
    global cx,cy,ZcurrX,ZcurrY,boundLeft,boundRight,boundUp,boundDown,zNext,escape,iterationNumber
    while escape == False:
        zNext = [(ZcurrX**2 - ZcurrY**2),(2*ZcurrX*ZcurrY)]
        zNext[0] = zNext[0] + cx
        zNext[1] = zNext[1] + cy
        ZcurrX = zNext[0]
        ZcurrY = zNext[1]
        iterationNumber += 1
        escapeFunc()

def iterationColor():
    global iterationNumber,colorToPrint
    if iterationNumber > 254:
        colorToPrint = (255,0,0)
    else:
        colorToPrint = (iterationNumber,0,0)

cx = 2
cy = 2
ZcurrX = 0
ZcurrY = 0
escape = False
iterationNumber = 0

# image creation: assigning pixel 
# square - 256, then divide by 128

imgx = 512
imgy = 512

ImgA = Image.new("RGBA",(imgx,imgy))
ImgA.paste((0,0,0), (0,0,imgx,imgy))
ImgA.save("ImgA.png","PNG")

for kx in range(0,imgx):
        for ky in range(0,imgy):
            if kx != 0:
                cx = (kx/(imgx/4)) - 2
            if ky != 0:
                cy = (ky/(imgy/4)) - 2
            # print("Original pixel:",kx,ky,"Converted number:",cx,cy)
            ZcurrX = 0
            ZcurrY = 0
            escape = False
            iterationNumber = 0
            mandelbrot()
            iterationColor()
            ImgA.putpixel((kx,ky),(colorToPrint))

ImgA.show()
ImgA.save("CalculatedA.png","PNG")
