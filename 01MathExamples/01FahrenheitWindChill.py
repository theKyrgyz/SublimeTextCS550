# Fahrenheit to Celsius

import sys
import random

t = float(sys.argv[1])
v = float(sys.argv[2])

print("Temperature: ",str(t))

print("Wind speed: ",str(v))

# now the work at home begins!

# w  =  35.74  +  0.6215  t  +  (0.4275  t  -  35.75)(v**0.16)

x = 35.74 + 0.6215*t
print("x: ",str(x))
y = (0.4275*t - 35.75)
print("y: ",str(y))
z = v**0.16
print("z: ",str(z))

w = x + y*z

print("Wind chill: ",str(w),"! Brr...")
