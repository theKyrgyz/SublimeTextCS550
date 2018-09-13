import sys

def commandCall(argNum):
	return sys.argv[int(argNum)]
	

if len(sys.argv) == 4:
	x = float(commandCall(1))
	y = float(commandCall(2))
	z = float(commandCall(3))

	if x < y < z:
		print("True");
	elif z < y < x:
		print("True");
	else:
		print("False");
else:
	print("Length incorrect.")