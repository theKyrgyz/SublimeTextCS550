"""
capedyer.py

An adventure game by Lucas Eggers. Let's do this.

DATE:
DESCRIPTION: 
SOURCES: http://usingpython.com/python-rpg-game/ for the proper syntax when using dictionaries for moving between rooms.
           https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row for clean nice list printing. (minor)
           https://thispointer.com/python-how-to-find-keys-by-value-in-dictionary/ for getting a list of the keys which carry a certain value.

This code's organized a bit weirdly, just because of how Python runs through its code sequentially. First, the room layout is defined.
Then, movement between rooms is laid down, plus a quit command. After that, an inventory system is created, and rooms are checked for items.
Next, "cutscenes" are laid down - I define cutscenes as any player-code interaction that isn't done through the lens of room movement and travel.
Then the main travelling() loop is placed, which is what the player will almost always be using. It calls the functions listed above.
FINALLY, the code that kicks off the game is found. Way at the bottom.

lockedDoor
goDirection / goDirections
quitSure
inventory: check, drop, take
getKeysByValue?


"""

import random as random

### NON-TRAVELLING DICTIONARIES AND FUNCTIONS:
## MOVING FROM ROOM TO ROOM, PLUS THE ITEMS IN EACH ROOM.

roomDictionary = {
        1 : {"name":"Command Center", "descrip":"There are many buttons here.", "north" : 2, "west" : 3, "south" : 4, "east":7, "rope":"f", "shovel":"f", "button":"Buttons, mostly blue dot the control panel of the complicated machines. \nSome say things like 'contact', 'ignition', 'anaylze'. One gigantic red button says 'WARN'"},
        2 : {"name":"Apex Room", "descrip":"You look out through the glass, over the icy waters.", "south":1, "north":5, "rope":"f", "shovel":"f"},
        3 : {"name":"Strategy Room", "descrip":"The westernmost room of the facility. A table stands in the center, with a map of Baffin Island taped across its entire length.", "east":1, "rope":"f", "shovel":"f", "table":"The table is little more than a couple 2x4s nailed together. \nSpare no expense, heh.", "map":"The map appears to be from American aviation agencies. \nIt shows criss-crossing vector, local airstrips, and - oh! \nThere's Cape Dyer. Home sweet home. \nWooden planes track real-time locations of aircraft.", "woodenplanes":"Most are bush planes doing local service to Inuit towns, \nbut some are intencontinental jetliners doing circumpolar trips. \nHot stuff."},
        4 : {"name":"Confrontation Room", "descrip":"The general's office. Oof.", "north":1, "rope":"f", "shovel":"f"},
        5 : {"name":"Hillside Steps", "descrip":"A series of rugged stairs leading from the facility down to the ocean.", "south":2, "north":6, "rope":"f", "shovel":"f"},
        6 : {"name":"The Harbor", "descrip":"Boats, seaplanes, and icebreakers alike are lined up next to a rusty metal dock.", "south":5, "rope":"f", "shovel":"f"},
        7 : {"name":"The Skyway", "descrip":"A see-through tunnel connecting the command and living centers of the base.", "west":1, "east":8, "rope":"f", "shovel":"f"},
        8 : {"name":"Living Quarters", "descrip":"A humble kitchen,  fit for the half-dozen inhabitants of this forsaken place.\nBut truly, why have that fridge when you could just stick the spaghetti in ice outside?", "west":7, "north":9, "rope":"f", "shovel":"f", "fridge":"A prized amenities, if redundant at times. You open it slowly, eyeing Nathan's spaghetti. \nYou love spaghetti.", "door":"The door is old and rusty, but reinforced with newer hinges. You'll need a key to get past it."},
        9 : {"name":"Radar Arrays", "descrip":"Gigantic lattice-pattern metal towers sit, perched on the plateau above the cape, taking information from hundreds of miles around.", "south":8, "rope":"f", "shovel":"f"},

}

# Locked doors:
# The one from 8 to 9:
lockedDoorNortheast = "f"

def lockedDoorNortheastPassage():
    if lockedDoorNortheast == "t":
        return True
    else:
        return False


#####      DEFINING A CRAP-TON OF FUNCTIONS:



## DEFINES THE 'GO' FUNCTION, allowing players to move between rooms.
def goDirection():
    global mainloopInput
    global currentRoom
    global newRoom
    if ((currentRoom == 8) and (mainloopInput == ["go", "north"])) or ((currentRoom == 9) and (mainloopInput == ["go", "south"])):
        if lockedDoorNortheastPassage() == False:
            print("Hmm. Looks like this door has been locked. You're gonna need to find a key.")
        else:
            print("This door is no match for you and your mighty key-finding skillz!")
            currentRoom = 9
            newRoom = True
            travelling()
    else:
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

global inventory
inventory = ["rope", "shovel"]

def inventoryCheck():
    if inventory != []:
        print("You have: ", end="")
        print(', '.join(inventory), end=".\n")
    else:
        print("You've got absolutely nothing.\n")

def inventoryDrop():
    global WantToDrop
    ## WantToDrop is the item the user wishes to drop.
    if WantToDrop in inventory:
        if WantToDrop in roomDictionary[currentRoom]:
            inventory.remove(WantToDrop)
            print("You successfully "+mainloopInput[0]+" the "+WantToDrop+".")
            roomDictionary[currentRoom][WantToDrop] = "t"
        else:
            print("It is thrown into the void, never to be seen again. \nJust kidding. \n(It appears you've dropped something that can't be dropped in this room. \nTry dropping it somewhere else.)")
            roomDictionary[currentRoom][WantToDrop] = "f"
    else:
        print("You rummage through your backpack, but can't seem to find that item.")

def inventoryTake():
    global WantToTake
    ## WantToTake is the item the user wants to take. Pretty self-explanatory.
    if WantToTake in roomDictionary[currentRoom]:
        if roomDictionary[currentRoom][WantToTake] == "t":
            print("You "+mainloopInput[0]+" the heck out of that "+WantToTake+".")
            roomDictionary[currentRoom][WantToTake] = "f"
            inventory.append(WantToTake)
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

# Examining items in the room.

def examineItem():
    global WantToExamine
    if WantToExamine in buttonExamination:
        WantToExamine = "button"
        examineCompletion()
    if WantToExamine in woodenExamination:
        WantToExamine = "woodenplanes"
        examineCompletion()
    if WantToExamine == ("map" or "mapofBaffinIsland"):
        WantToExamine = "map"
        examineCompletion()
    if WantToExamine == ("fridge" or "refrigerator"):
        WantToExamine = "fridge"
        examineCompletion()
    else:
        examineCompletion()

def examineCompletion():
    global WantToExamine
    print("Examining:",WantToExamine)
    if WantToExamine in roomDictionary[currentRoom]:
        print(roomDictionary[currentRoom][WantToExamine])
    else:
        print("Sorry, I couldn't find that in this room.")
    travelling()

# A simple HELP screen.
def provideHelp():
    h = input("\n1) I need help with understanding how a text adventure / interactive fiction work functions.\n2) I need help with specific commands.\n> ")
    if h == "1":
        print("Well, I guess you need to tell Lucas to actually write all this out.")
    elif h == "2":
        print("A list of the current commands available:\n'go [direction]' moves the player in the direction specified. Current supported directions are north, south, east, and west.")
        print("'n', 's', 'e', and 'w' all function as shorthand for the 'go' command.\n'i' returns your entire inventory.\n'drop [thing]' drops an item, if it's in your inventory.")
        print("'q' quits the game. 'h' provides help.")
    else:
        print("I don't quite understand that. Please put in 1 or 2. I'm returning you to the main game now.")
        travelling()

## STUPID COMMANDS - SKIP. Eat function, purge function, moo function. I don't even know why I put this in.

def eatFunction():
    global WantToEat
    if WantToEat in inventory:
        inventory.remove(WantToEat)
        print("Consuming the "+WantToEat+", you suddenly have a profound feeling...\n...that you won't be able to recover this item once it recedes from your intestinal tracts.")
    print("OM NOM NOM NOM NOM. How nutritious of a "+WantToEat+". You feel so utterly "+random.choice(adjectivesEat)+".")
    WantToEat = WantToEat.strip('"\'')
    thingsYouHaveEaten.append(WantToEat.strip('"\''))

def purge():
    global thingsYouHaveEaten
    thingsYouHaveEaten = str(thingsYouHaveEaten)[1:-1]
    thingsYouHaveEaten = thingsYouHaveEaten.strip('"\'')
    inventory.append(thingsYouHaveEaten.strip('"\''))
    thingsYouHaveEaten = []
    print("Bleh. You decide that your index finger will do the job well enough.\nSticking it far down your esophagus, you feel the rising in your digestive tract.\nSoon enough, you ralph outwards the entire contents of your stomach.\nSwiftly, you add them to your inventory.")

def moo():
    global cow
    global inventory
    if cow == False:
        print("Thou art now a bovine. Unfortunately, bovines are unable to posses any items. You eat them all.")
        cow = True
        thingsYouHaveEaten.append(inventory)
        inventory = []
    else:
        print("Thou art already a hooved creature, wanderer.")

## COMMAND ALTERNATIVE LISTS because Abraham Goodman doesn't know how words work, plus LISTS FOR INTERPRETING EXAMINING THINGS.

takeList = ["take","grab","pickup","pick up","swipe","pick"]
dropList = ["drop","leave","yeet"]

eatList = ["consume","eat","devour","cronch","inhale"]

possibleDirections = ["west","north","south","east"]

global thingsYouHaveEaten
thingsYouHaveEaten = []
adjectivesEat = ["invigorated","rejuvenated","defenestrated","like God","revitalized","reborn","satanic","full of yummy bits inside"]

global examineList
examineList = ["x", "examine", "investigate", "look"]
buttonExamination = ["button","buttons","redbutton","bluebutton"]
woodenExamination = ["woodenaircraft","woodenpieces","woodplanes","woodpieces","woodaircraft","aircraft","pieces"]

## STARTING CUTSCENES, stopping the travelling() loop.

def beginCutscene(CutNum):
    Cutscene = True
    print("Your location:",roomDictionary[currentRoom]["name"]+".")
    print(roomDictionary[currentRoom]["descrip"])
    if CutNum == 4:
        # print("WE GOT TO THE FOUR CHECK")
        cutsceneGeneralAnatuq()
    else:
        return

## CUTSCENE 'GENERAL' PATHS

def cutsceneGeneralAnatuq():
    # print("CAN YOU READ THIS?")
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
        # Giving the player about the room they just moved to.
        if newRoom == True:
            print("\n\nYou are now in: ",roomDictionary[currentRoom]["name"])
            print(roomDictionary[currentRoom]["descrip"])
            getKeysByValue(roomDictionary[currentRoom], "t")
            if roomKeys != []:
                print("\nHere, you notice: ", sep=", ")
            print(*roomKeys, sep=", ")
            print("The possible exits are: ")
            for direction in possibleDirections:
                if direction in roomDictionary[currentRoom]:
                    print(direction)
        newRoom = False
        global mainloopInput
        global rawCommandInput
        rawCommandInput = input("\n>> ")
        mainloopInput = rawCommandInput.lower().split()
        if mainloopInput == []:
            travelling()
        # If the player is attempting to examine something:
        if mainloopInput[0] in examineList:
            if len(mainloopInput) == 1:
                print(roomDictionary[currentRoom]["descrip"])
            else: # If the player wants to examine an object and not the room in general
                mainloopInput.pop(0)
                global WantToExamine
                WantToExamine = "".join(mainloopInput)
                examineItem()
                travelling()
        if len(mainloopInput) == 2: # IF THE COMMAND IS TWO WORDS
            if mainloopInput[0] == "go":
                goDirection() # THIS IS IMPORTANT! IT CALLS THE GO FUNCTION FROM BEFORE. I do this in order to increase adaptability. And to make it less ugly.
            elif mainloopInput[0] in dropList:
                global WantToDrop
                WantToDrop = mainloopInput[1]
                inventoryDrop()
            elif mainloopInput[0] in takeList:
                global WantToTake
                WantToTake = mainloopInput[1]
                inventoryTake()
            elif mainloopInput[0] in eatList:
                global WantToEat
                WantToEat = mainloopInput[1]
                eatFunction()
            else:
                print("\nI don't understand that verb. Try 'go [direction]' or 'take [item]'.\n")
        # IF THE COMMAND IS ONE WORD
        elif mainloopInput[0] == "i":
            inventoryCheck()
        elif mainloopInput[0] == "qy":
            quit()
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
        elif mainloopInput[0] == "sudo":
            quit()
        elif mainloopInput[0] == "purge":
            purge()
        elif mainloopInput[0] == "moo":
            global cow
            moo()
        elif mainloopInput[0] == "x":
            print()
        else:
            print("Whoops! You need to provide at least two arguments for a command like 'go'. \nIf your command is one word, I just don't understand it.")
        if (currentRoom == 4) and (newRoom == True): 
            # CHECKING FOR CUTSCENE TRIGGERS.
            # print("We got to the currentRoom 4 check.")
            beginCutscene(4)

### FORMALLY BEGINNING THE GAME. Initiate sequence, codename: BOOGALOO.

print("\n\n\n\tCAPE DYER. A THRILLING TALE OF NUCLEAR WAR, RADIOACTIVE COWS, AND BIG RED BUTTONS. \n")
print("If you're not familiar with standard interactive fiction nomenclature, enter 'h' for help.\n")
# NOTE TO SELF: INSERT INSTRUCTIONS TO PLAYER HERE
currentRoom = 1
Cutscene = False
newRoom = True
cow = False
travelling()

