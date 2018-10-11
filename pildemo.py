# pildemo.py

from PIL import Image

imgx = 512
imgy = 512

myImage = Image.new("RGB",(imgx,imgy))

myImage.putpixel((0,0),(255,0,0))
myImage.putpixel((10,0),(255))

myImage.save("demo.png","PNG")

