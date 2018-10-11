# factorial.py

# Base case: 1! = 1 = 1

# IMPORTS
import sys

# SIMPLIFYING SYS.ARGV
def commandCall(argNum):
    return sys.argv[int(argNum)]

def fact(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 6
    else:
        return n*fact(n-1)

if len(sys.argv) >= 2:
    if type(commandCall(1)) == int:
        print("\nAnswer is:",fact(int(commandCall(1))),"\n")