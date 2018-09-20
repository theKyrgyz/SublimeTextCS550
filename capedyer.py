"""
# capedyer.py

# An adventure game by Lucas Eggers. Let's do this.

# SOURCES: http://usingpython.com/python-rpg-game/ for the proper syntax when using dictionaries for moving between rooms.
           https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row for clean nice list printing. (minor)
           https://thispointer.com/python-how-to-find-keys-by-value-in-dictionary/ for getting a list of the keys which carry a certain value.

This code's organized a bit weirdly, just because of how Python runs through its code sequentially. First, the room layout is defined.
Then, movement between rooms is laid down, plus a quit command. After that, an inventory system is created, and rooms are checked for items.
Next, "cutscenes" are laid down - I define cutscenes as any player-code interaction that isn't done through the lens of room movement and travel.
Then the main travelling() loop is placed, which is what the player will almost always be using. It calls the functions listed above.
FINALLY, the code that kicks off the game is found. Way at the bottom.

"""
### NON-TRAVELLING DICTIONARIES AND FUNCTIONS:
## MOVING FROM ROOM TO ROOM, PLUS THE ITEMS IN EACH ROOM.

roomDictionary = {
        1 : {"name":"Command Center", "descrip":"There are many buttons here.", "north" : 2, "west" : 3, "south" : 4, "east":7, "rope":"f", "shovel":"f"},
        2 : {"name":"Apex Room", "descrip":"You look out through the glass, over the icy waters.", "south":1, "north":5, "rope":"f", "shovel":"f"},
        3 : {"name":"Strategy Room", "descrip":"The western flank of the facility.", "east":1, "rope":"f", "shovel":"f"},
        4 : {"name":"Confrontation Room", "decsrip":"The general's office. Oof.", "north":1, "rope":"f", "shovel":"f"},
        5 : {"name":"Hillside Steps", "descrip":"A series of rugged stairs leading from the facility down to the ocean.", "south":2, "north":6, "rope":"f", "shovel":"f"},
        6 : {"name":"The Harbor", "descrip":"Boats, seaplanes, and icebreakers alike are lined up next to a rusty metal dock.", "south":5, "rope":"f", "shovel":"f"},
        7 : {"name":"The Skyway", "descrip":"A see-through tunnel connecting the command and living centers of the base.", "west":1, "rope":"f", "shovel":"f"}


}




#####      DEFINING A CRAP-TON OF FUNCTIONS:



## DEFINES THE 'GO' FUNCTION, allowing players to move between rooms.
def goDirection():
    global mainloopInput
    global currentRoom
    global newRoom
    if mainloopInput[1] in roomDictionary[currentRoom]:
        currentRoom = roomDictionary[currentRoom][mainloopInput[1]]
        newRoom = True
    else:
        print("\nWhoops! That's not a viable direction.\n")
        newRoom = False

## Defining the QUIT function, with a check (are you sure?).
def quitSure():
    if input("Quit? y/n ") == "y":
        quit()
    else:
        travelling()

## Defining the INVENTORY functions - check inventory, drop items, etc.

inventory = ["rope", "shovel"]

def inventoryCheck():
    print("You have: ", end="")
    print(*inventory, sep=", ", end="")
    print(".")

def inventoryDrop():
    global WantToDrop
    ## WantToDrop is the item the user wishes to drop.
    if WantToDrop in inventory:
        inventory.remove(WantToDrop)
        if WantToDrop in roomDictionary[currentRoom]:
            print("You successfully drop the "+WantToDrop+".")
            roomDictionary[currentRoom][WantToDrop] = "t"
        else:
            print("It is thrown into the void, never to be seen again. \n(It appears you've dropped something that can't be dropped in this room. \nTry dropping it somewhere else.)")
            roomDictionary[currentRoom][WantToDrop] = "f"
    else:
        print("You rummage through your backpack, but can't seem to find that item.")

def inventoryTake():
    global WantToTake
    ## WantToTake is the item the user wants to take. Pretty self-explanatory.
    if WantToTake in roomDictionary[currentRoom]:
        if roomDictionary[currentRoom][WantToTake] == "t":
            print("You swipe the heck out of that"+WantToTake+".")
            roomDictionary[currentRoom][WantToTake] = "f"
            inventory.add(WantToTake)
        else: 
            print("Seems like the item you want isn't here. \nIt might be in another room, or you might not have typed it correctly.\n")
    else:
        print("I don't think that's a thing you can take. \nSomething went wrong, anyway. Try again.\n")

# Checking for items in rooms. THIS IS A MEAN PART

def getKeysByValue(dictOfElements, valueToFind):
    global roomKeys
    roomKeys = list()
    roomItems = dictOfElements.items()
    # print("We are looking for", valueToFind)
    for item in roomItems:
        if item[1] == valueToFind:
            if item[1] != 1:
                roomKeys.append(item[0])
                # print("Appending",item)
    return roomKeys

# A simple help screen.
def provideHelp():
    h = input("\n1) I need help with understanding how a text adventure / interactive fiction work functions.\n2) I need help with specific commands.\n> ")
    if h == "1":
        print()
    elif h == "2":
        print("A list of the current commands available:\n'go [direction]' moves the player in the direction specified. Current supported directions are north, south, east, and west.")
        print("'n', 's', 'e', and 'w' all function as shorthand for the 'go' command.\n'i' returns your entire inventory.\n'drop [thing]' drops an item, if it's in your inventory.")
        print("'q' quits the game. 'h' provides help.")
    else:
        print("I don't quite understand that. Please put in 1 or 2. I'm returning you to the main game now.")
        travelling()

## STARTING CUTSCENES, stopping the travelling() loop.

def beginCutscene(CutNum):
    Cutscene = True
    print("Your location:",roomDictionary[currentRoom]["name"]+".")
    print(roomDictionary[currentRoom]["descrip"])
    if CutNum == 4:
        cutsceneGeneralAnatuq()
    else:
        return

## CUTSCENE 'GENERAL' PATHS

def cutsceneGeneralAnatuq():
    choiceOne = input("General Anatuq walks up to you. Uh oh. Do you: \n\n1) snatch his cigarette right out of his mouth, or \n\n2) try to greet him in a friendly manner?\n\n>> ")
    if choiceOne == "1":
        print("\n\nGeneral Anatuq is most displeased. \nWhen you regain consciousness, you find yourself abandoned in the frigid wastes outside the base.\n\n")
        exit()
    if choiceOne == "2":
        print("General Anatuq smirks and says, 'Go back out there, boy. You still have work to do.'\n")
        currentRoom = 1
        Cutscene = False
        travelling()


### MAIN VERB COMMAND INPUT LOOP

def travelling():
    while Cutscene == False:
        global currentRoom
        global newRoom
        if newRoom == True:
            print("\n\nYou are now in :",roomDictionary[currentRoom]["name"])
            print(roomDictionary[currentRoom]["descrip"])
            getKeysByValue(roomDictionary[currentRoom], "t")
            if roomKeys != []:
                print("\nHere, you notice: ", sep=", ")
            print(*roomKeys, sep=", ")
        newRoom = False
        global mainloopInput
        mainloopInput = input("\n>> ").lower().split()
        if len(mainloopInput) == 2: # IF THE COMMAND IS TWO WORDS
            if mainloopInput[0] == "go":
                goDirection() # THIS IS IMPORTANT! IT CALLS THE GO FUNCTION FROM BEFORE. I do this in order to increase adaptability. And to make it less ugly.
            elif mainloopInput[0] == "drop":
                global WantToDrop
                WantToDrop = mainloopInput[1]
                inventoryDrop()
            elif mainloopInput[0] == "take":
                global WantToTake
                WantToTake = mainloopInput[1]
                inventoryTake()
            else:
                print("\nI don't understand that verb. Try 'go [direction]' or 'use [item]'.\n")
            if currentRoom == 4: # CHECKING FOR CUTSCENE TRIGGERS.
                beginCutscene(4)
        # IF THE COMMAND IS ONE WORD
        elif mainloopInput[0] == "i":
            inventoryCheck()
        elif mainloopInput[0] == "q":
            quitSure()
        elif mainloopInput[0] == "n":
            mainloopInput = ["go", "north"]
            goDirection()
        elif mainloopInput[0] == "e":
            mainloopInput = ["go", "east"]
            goDirection()
        elif mainloopInput[0] == "s":
            mainloopInput = ["go", "south"]
            goDirection()
        elif mainloopInput[0] == "w":
            mainloopInput = ["go", "west"]
            goDirection()
        elif mainloopInput[0] == "h":
            provideHelp()
        else:
            print("Whoops! You need to provide at least two arguments for a command like 'go'. \nIf your command is one word, I just don't understand it.")

### FORMALLY BEGINNING THE GAME. Initiate sequence, codename: BOOGALOO.

print("\n\n\n\tCAPE DYER. A THRILLING TALE OF NUCLEAR WAR AND BIG RED BUTTONS. \n")
print("If you're not familiar with standard interactive fiction nomenclature, enter 'h' for help.\n")
# NOTE TO SELF: INSERT INSTRUCTIONS TO PLAYER HERE
currentRoom = 1
Cutscene = False
newRoom = True
travelling()

