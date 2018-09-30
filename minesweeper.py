# minesweeper.py

# IMPORTS
import sys
import math as ma # costs $0.02 to import math
import random as ra 

# SIMPLIFYING SYS.ARGV
def commandCall(argNum):
    return sys.argv[int(argNum)]

print("\n")

if len(sys.argv) != 4:
    print("You haven't provided the correct number of arguments.")
    quit()

w = int(commandCall(1))
h = int(commandCall(2))
b = int(commandCall(3))

if b >= (w*h):
    print("You want me to put more bombs than spots available. Too bad.")
    quit()

board = [[0]*w for x in range(h)]

# placing the bombs

def runBombPlacement():
    bx = ra.randint(0,(w-1))
    by = ra.randint(0,(h-1))
    # print("x+1:",bx+1,"y+1:",by+1)
    if board[by][bx] == "*":
        runBombPlacement()
    else:
        board[by][bx] = "*"
    return

for z in range(b):
    runBombPlacement()

# printing the updated board

for each in board:
    print(*each)

# number placement function

summationList = []
global minesNumberDisplay
minesNumberDisplay = 0

def CheckComplete():
    summationList = []
    if y != 0:
        if board[y-1][x] == "*":
            summationList.append(1)
            # print("current square sum:",sum(summationList))
            # print(x,",",y,"got the one above it.")
        if x != 0:
            if board[y-1][x-1] == "*":
                summationList.append(1)
                # print("current square sum:",sum(summationList))
                # print(x,",",y,"got the one above and to the left of it.")
        if not (x >= (w-1)):
            if board[y-1][x+1] == "*":
                summationList.append(1)
                # print("current square sum:",sum(summationList))
                # print(x,",",y,"got the one above and to the right of it.")
    if not (y >= (h-1)):
        if board[y+1][x] == "*":
            summationList.append(1)
            # print("current square sum:",sum(summationList))
            # print(x,",",y,"got the one below it.")
        if x != 0:
            if board[y+1][x-1] == "*":
                summationList.append(1)
                # print("current square sum:",sum(summationList))
                # print(x,",",y,"got the one below and to the left of it.")
        if x < (w-1):
            if board[y+1][x+1] == "*":
                summationList.append(1)
                # print("current square sum:",sum(summationList))
                # print(x,",",y,"got the one below and to the right of it.")
    if x != 0:
        if board[y][x-1] == "*":
                summationList.append(1)
                # print("current square sum:",sum(summationList))
                # print(x,",",y,"got the one to the left of it.")
    if not (x >= w-1):
        if board[y][x+1] == "*":
                summationList.append(1)
                # print("current square sum:",sum(summationList))
                # print(x,",",y,"got the one to the right of it.")
    board[y][x] = sum(summationList)


# begin the process

for y in range(h):
    for x in range(w):
        # print("x:",x,"y:",y,"val:",board[y][x])
        if board[y][x] != "*":
            CheckComplete()

print("\n\n\nFinished board: \n")
# print updated "finished product" board
for each in board:
    print(*each)


print("\n")
