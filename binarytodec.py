# binarytodec.py

# IMPORTS
import sys
import math as ma # costs $0.02 to import math

# SIMPLIFYING SYS.ARGV
def commandCall(argNum):
    return sys.argv[int(argNum)]

if len(sys.argv) < 2:
    print("You haven't provided enough arguments.")
    quit()

rawInput = commandCall(1)
rawList = list(rawInput)

intList = []

def binaryToDec(BinaryList):
    for p in range(0,len(BinaryList)):
        s = (p+1)*(-1)
        a = 2**p
        if (BinaryList[s] != '0') and (BinaryList[s] != '1'):
            print("Whoops! You didn't enter only zeroes and ones. Sorry.")
            quit()
        if BinaryList[s] == '1':
            intList.append(a)
    global dec
    dec = sum(intList)
    return dec

print(binaryToDec(rawList))