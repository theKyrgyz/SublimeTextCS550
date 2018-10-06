# minesweeper.py
# DATE: September 27 through October 2, 2018
# DESCRIPTION: A WIP playable Minesweeper game. Currently the board is fully uncovered and there is no user interaction.
# SOURCES: Online: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console for clearing console, and https://stackoverflow.com/questions/287871/print-in-terminal-with-colors for colors. Anan in my class helped me out tremedously with simplifying my code - from if statements checking for bombs post-placement, to a method that immediately adds to the count of squares surrounding the bomb, directly after its placement.

import sys
import random as ra
import copy
import os
print("\n")


# clearing the screen
def clsc():
    os.system('cls' if os.name=='nt' else 'clear')

# colors! so purty
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# starting to create the board
try:
    w = int(sys.argv[1])
    h = int(sys.argv[2])
    b = int(sys.argv[3])
    if (((b >= (w*h)) or (w==0)) or ((h==0) or (b==0))):
        print("You want me to put more bombs than spots available, or the board includes a dimension of 0. Too bad.\n")
    else:
        global board
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

for l in range(0,h+1):
    board[l][0] = '|'
    board[l][-1] = "|"
board[0] = "-"*(w+2)
board[0-1] = "-"*(w+2)

# start the actual game

playerBoard = copy.deepcopy(board)

for m in range(1,h+1):
    for n in range(1,w+1):
        playerBoard[m][n] = (bcolors.WARNING+"?"+bcolors.ENDC)
clsc()
"""
for pbr in playerBoard:
    print(*pbr)
print("\n")
"""
Game = True

CascadableNot = ["*","_","-","|"]
uncoveredZeroes = []
CascadableList = []
currentCascade = []


# functions for loops, etc.
def cascadingZero():
    currentCascade = []
    global ix
    global iy
    playerBoard[iy][ix] = 0
    CascadableList.append(str(ix)+","+str(iy))
    while len(CascadableList) != 0:
        currentCascade = CascadableList[0].split(",")
        ix = int(currentCascade[0])
        iy = int(currentCascade[1])
        CascadableList.pop(0)
        for x in range(-1,2):
            for y in range(-1,2):
                # print(ix,iy)
                if (not (str(board[iy+y][ix+x]) in CascadableNot)) and (str(playerBoard[iy+y][ix+x]) != "0"): #((not (str(board[iy+y][ix+x]) in CascadableNot)) and (playerBoard[iy+y][ix+x] != 0)):
                    playerBoard[iy+y][ix+x] = copy.deepcopy(int(board[iy+y][ix+x]))
                    if board[iy+y][ix+x] == 0:
                        CascadableList.append(str(ix+x)+","+str(iy+y))
    print("You have uncovered a whole bunch of zeroes.")

def uncover():
    # xyinput = input("Which square would you like to uncover? Please input your choice as 'x,y' with 1,1 being the top left corner.\n>> ").split(",")
    if (len(turnBasedInput) == 3) and ((int(turnBasedInput[1]) <= w) and (int(turnBasedInput[2]) <= h)):
        global ix
        global iy
        ix = int(turnBasedInput[1])
        iy = int(turnBasedInput[2])
        clsc()
        if board[iy][ix] == "*":
            print("\n\nKA BOOM!\n\nYou have been explode. Great job.\n\n")
            Game == False
            quit()
        elif board[iy][ix] == 0:
            cascadingZero()
        else:
            print("\nYou have uncovered a "+str(board[iy][ix])+".\n")
            playerBoard[iy][ix] = board[iy][ix]
    else:
        print("You have provided an unsuitable number of arguments, or your coordinates are too large.")
    return

def flag():
    if (len(turnBasedInput) == 3) and ((int(turnBasedInput[1]) <= w) and (int(turnBasedInput[2]) <= h)):
        ix = (int(turnBasedInput[1]))
        iy = (int(turnBasedInput[2]))
        if playerBoard[iy][ix] != (bcolors.FAIL + "F" + bcolors.ENDC):
            playerBoard[iy][ix] = bcolors.FAIL + "F" + bcolors.ENDC
            print("\nFlag successful. Be careful out there.\n")
        else:
            playerBoard[iy][ix] = bcolors.WARNING+"?"+bcolors.ENDC
            print("Unflag successful.")
        clsc()
    else:
        print("You have provided an unsuitable number of arguments, or your coordinates are too large.")
    return

def WinState():
    global bombsFlagged
    questionMark = False
    bombsFlagged = 0
    for wy in range(1,h+1):
        for wh in range(1,w+1):
            if (playerBoard[wy][wh] == (bcolors.WARNING + "?" + bcolors.ENDC)) and (board[wy][wh] != "*"):
                # print("i found a ?")
                questionMark = True
            """ if (board[wy][wh] == "*") and (playerBoard[wy][wh] == bcolors.FAIL + "F" + bcolors.ENDC):
                bombsFlagged = bombsFlagged + 1 """
    if questionMark == False:
        print("You win! \033[1m YAYAYAYA \033[0m \n")
        quit()

# repeatedly asking input
while Game == True:
    print("\n")
    for pbr in playerBoard:
        print(*pbr)
    print("\n")
    WinState()
    turnBasedInput = input("To uncover a square, put in 'u'. To flag a square, put in 'f'. \nAdd a space. Put in coordinates as 'x y' where '1 1' is the top left corner.\n>> ").split()
    print("\n\n")
    if len(turnBasedInput) == 3:
        if turnBasedInput[0] == "u":
            uncover()
        elif turnBasedInput[0] == "f":
            flag()
    elif len(turnBasedInput) == 1:
        if turnBasedInput[0] == "q":
            quit()
