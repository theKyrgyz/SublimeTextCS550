# minesweeper.py
# DATE: September 27 through October 2, 2018
# DESCRIPTION: A WIP playable Minesweeper game. Currently the board is fully uncovered and there is no user interaction.
# SOURCES: Nothing online, but Anan in my class helped me out tremedously with simplifying my code - from if statements checking for bombs post-placement, to a method that immediately adds to the count of squares surrounding the bomb, directly after its placement.

import sys
import random as ra
print("\n")
try:
    w = int(sys.argv[1])
    h = int(sys.argv[2])
    b = int(sys.argv[3])
    if (((b >= (w*h)) or (w==0)) or ((h==0) or (b==0))):
        print("You want me to put more bombs than spots available, or the board includes a dimension of 0. Too bad.\n")
    else:
        board = [[0]*(w+2) for i in range(h+2)]
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

except ValueError:
    print("You haven't provided the correct number of arguments. Too bad.\n")
    quit()

# cut the board

for l in board:
    l.pop(0)
    l.pop(-1)
board.pop(0)
board.pop(-1)
print("Cut board:")
for l in board:
    print(*l)
print("\n")

# start the actual game

playerBoard = [["?"]*(w) for i in range(h)]
for pbr in playerBoard:
    print(*pbr)
print("\n")
