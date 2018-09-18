# capedyer.py

# An adventure game by Lucas Eggers. Let's do this.

# SOURCES: http://usingpython.com/python-rpg-game/ for the proper syntax when using dictionaries.

## Class Work today (9.18.18)

def hi():
    print("hello!")


## MOVING FROM ROOM TO ROOM

roomDictionary = {
        1 : {"name":"Command Center", "north" : 2, "west" : 3, "south" : 4},
        2 : {"name":"Apex Room", "south":1},
        3 : {"name":"Western Front", "east":1},
        4 : {"name":"Confrontation Room", "north":1}


}

currentRoom = 1
Cutscene = False

## FUNCTION DEFINITIONS: STARTING A NON-TRAVEL "CUTSCENE" SEQUENCE

def beginCutscene(int):
    Cutscene = True
    print("Your location:",roomDictionary[currentRoom]["name"]+".")
    cutsceneOne()

## CUTSCENE ONE PATHS

def cutsceneOne():
    choice == input("General Anatuq walks up to you. Uh oh. Do you: \n\n1) snatch his cigarette right out of his mouth, or \n\n2) try to greet him in a friendly manner?\n\n>> ")
    if choice == "1":
        print("\n\nGeneral Anatuq is most displeased. When you regain consciousness, you find yourself abandoned in the frigid wastes outside the base.\n\n")
        exit()
    if choice == "2":
        print("General Anatuq smirks and says, 'Go back out there, boy. You still have work to do.'")
        currentRoom = 1
        Cutscene = False
        travel()
        return


### MAIN TRAVEL LOOP

def travelling():
    while Cutscene == False:
        print("Your location: ",roomDictionary[currentRoom]["name"],".")
        mainloopInput = input("\n>> ").lower().split()
        if len(mainloopInput) == 2:
            if mainloopInput[0] == "go":
                if mainloopInput[1] in rooms[currentRoom]:
                    currentRoom = rooms[currentRoom][move[1]]
                else:
                    print("\nWhoops! That's not a viable direction.\n")
            else:
                print("\nI don't understand that verb. Try 'go [direction]' or 'use [item]'.\n")

            if currentRoom == 4:
                beginCutscene(4)
        else:
            print("Whoops! You need to provide at least two arguments for a command like 'go'.")

### BEGINNING THE GAME

print("\n \n \n CAPE DYER. A THRILLING TALE OF NUCLEAR WAR AND BIG RED BUTTONS. \n")
currentRoom = 1
travelling()

