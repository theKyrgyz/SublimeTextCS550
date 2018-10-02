# minesweeper.py
import sys
import random as ra 
def commandCall(argNum):
    return sys.argv[int(argNum)]
print("\n")
if len(sys.argv) != 4:
    print("You haven't provided the correct number of arguments.\n")
    quit()

w = int(commandCall(1))
h = int(commandCall(2))
b = int(commandCall(3))
if ((b >= (w*h)) or (w==0) or (h==0)):
    print("You want me to put more bombs than spots available. Too bad. \n")
    quit()

board = [[0]*(w+2) for i in range(h+2)]

global numberBombsPlaced
numberBombsPlaced = 0
while numberBombsPlaced < b:
    bx = ra.randint(1,(w))
    by = ra.randint(1,(h))
    if board[by][bx] != "*":
        board[by][bx] = "*"
        for x in range (-1,2):
            for y in range (-1,2):
                if board[by+y][bx+x] != "*":
                    board[by+y][bx+x] += 1
        numberBombsPlaced += 1

for each in board[1:h+1]:
    print(*each[1:w+1])
print("\n")