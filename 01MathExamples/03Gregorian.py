# 03Gregorian.py

# Date: September 13, 2018. 
# Description: A day-of-the-week calculator, provided one inputs the month, day, and year in the command terminal as arguments. 
# Sources: Official Python documentation for lists and printing specific items from lists, as well as the assignment instructions and equations.

"""
COPY AND PASTED FORMULAS
y0  =  y  -  (14  -  m)  /  12
x  =  y0  +  y0/4  -  y0/100  +  y0/400  
m0  =  m  +  12  *  ((14  -  m)  /  12)  -  2 
d0  =  (d  +  x  +  (31*m0)/  12)  mod  7 

"""

import sys

def argCall(argNum):
	return sys.argv[int(argNum)]

y = int(argCall(3))
d = int(argCall(2))
m = int(argCall(1))

print("\n Day entered: ",str(m),str(d),str(y))

print("Begin operations. \n Diagnostic test results:")

""" SKIP THIS PART. IT WAS A FAILED ATTEMPT.
yzero = round(y - ((12 - m)/12), 0)
print(str(yzero))
x = round((yzero + yzero/4 - yzero/100 + yzero/400), 0)
print(str(x))
mzero = float(m + (int(12*((12-m)/12) - 2)) - 2)

print(str(mzero))

dhalfway = (d + x + ((31*mzero)/12))
print("Dhalfway = ",str(dhalfway))

dzero = (d + x + ((31*mzero)/12)) % 7

print(str(dzero))
"""

yzero = y - (14-m)//12
print(str(yzero))
x = yzero + (yzero//4) - (yzero//100) + (yzero//400)
print(str(x))
mzero = m + 12*((14-m)//12) - 2
print(str(mzero))
dhalfway = d + x + ((31*mzero)//12)
print(str(dhalfway))
dfinal = (dhalfway)%7
print(str(dfinal), "\n")

listDays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print("It was ", listDays[dfinal], " on that day.")




