# Date: September 13, 2018. 
# Description: A function that evaluates whether three given integer arguments are sorted in ascending, descending, or arbitrary order. 
# Sources: Other than Esther An introducing me to the "elif" statement, none specifically, aside from those given in the assignment.

import sys

def argCall(argNum):
	return sys.argv[int(argNum)]
	

if len(sys.argv) == 4:
	x = float(argCall(1))
	y = float(argCall(2))
	z = float(argCall(3))

	if x < y < z:
		print("True");
	elif z < y < x:
		print("True");
	else:
		print("False");
else:
	print("Length incorrect.")