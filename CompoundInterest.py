import sys
import math as ma

def argCall(argNum):
	return sys.argv[int(argNum)]

if len(sys.argv) == 4:
	p = float(argCall(1))
	r = float(argCall(2))
	t = float(argCall(3))
	ert = ma.exp(r*t)
	result = round(p*(ert), 2)
	print("You'll have $"+str(result)+".")
else: print("Wrong number of arguments. Please input Principal (dollars), Rate (in decimal value), and Time (number of years), respectively.")