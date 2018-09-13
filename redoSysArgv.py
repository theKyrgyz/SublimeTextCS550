import sys

def commandCall(argNum):
	return sys.argv[int(argNum)]
	

v = commandCall(1)
w = commandCall(0)

print(str(v))
print(str(w))
