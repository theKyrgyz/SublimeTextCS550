import random as r
import math as m 

theta = r.random()
# convert to radians
theta = theta * m.pi * 2

s = pow(m.sin(theta), 2)
print(str(s))

c = pow(m.cos(theta), 2)
print(str(c))

end = (c + s)

end = round(end, 2)

print(str(end))