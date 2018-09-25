# capedyerClass.py

"""

An adventure game by Lucas Eggers. Let's do this.

DATE: 24 September 2018
DESCRIPTION: 
SOURCES: http://usingpython.com/python-rpg-game/ for the proper syntax when using dictionaries for moving between rooms.
           https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row for clean nice list printing. (minor)
           https://thispointer.com/python-how-to-find-keys-by-value-in-dictionary/ for getting a list of the keys which carry a certain value.

This code's organized a bit weirdly, just because of how Python runs through its code sequentially. First, the room layout is defined.
Then, movement between rooms is laid down, plus a quit command. After that, an inventory system is created, and rooms are checked for items.
Next, "cutscenes" are laid down - I define cutscenes as any player-code interaction that isn't done through the lens of room movement and travel.
Then the main travelling() loop is placed, which is what the player will almost always be using. It calls the functions listed above.
FINALLY, the code that kicks off the game is found. Way at the bottom.

"""

import random as random

class RoomClass:

    kind = 'room'

    def __init__(self, number, name, descrip, north, east, south, west, atatuq, ramona, nathan, rope, shovel, button, woodenplanes, mapBaffin, fridge):
        self.number = number
        self.name = name
        self.descrip = descrip
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.atatuq = atatuq
        self.ramona = ramona
        self.nathan = nathan
        self.rope = rope
        self.shovel = shovel
        self.button = button
        self.woodenplanes = woodenplanes
        self.map = mapBaffin
        self.fridge = fridge


CommandCenter = RoomClass(1, "Command Center", "This is where the magic happens. Glittering buttons do terrifying things. \nBest not to push them.\nTo the south is the general's office, to the north, the Comms Room. \nThe living quarters are east of here, and to the west is the Strategy Room.", "Communications Room", "The Skyway", "Confrontation Room", "Strategy Room", False, True, False, False, False, None, None, None, None)
CommunicationsRoom = RoomClass(2, "Communications Room", "You look out through the glass, over the icy waters.", "Hillside Steps", None, "Command Center", None, False, False, True, False, True, None, None, None, None)
StrategyRoom = RoomClass(3, "Strategy Room", "The westernmost room of the facility. A table stands in the center, with a map of Baffin Island taped across its entire length.", None, "Command Center", None, None, False, False, False, False, False, None, None, None, None)
ConfrontationRoom = RoomClass(4, "Confrontation Room", "The general's office. Oof.", "Command Center", None, None, None, True, False, False, False, False, None, None, None, None)
HillsideSteps = RoomClass(5, "Hillside Steps", "A series of rugged stairs leading from the facility down to the ocean.", "The Harbor", None, "Communications Room", None, False, False, False, False, False, None, None, None, None)
TheHarbor = RoomClass(6, "The Harbor", "Boats, seaplanes, and icebreakers alike are lined up next to a rusty metal dock.", None, None, "Hillside Steps", None, False, False, False, False, False, None, None, None, None)
TheSkyway = RoomClass(7, "The Skyway", "A see-through tunnel connecting the command and living centers of the base.", None, "Living Quarters", None, "Command Center", False, False, False, False, False, None, None, None, None)
LivingQuarters = RoomClass(8, "Living Quarters", "A humble kitchen,  fit for the half-dozen inhabitants of this forsaken place.\nBut truly, why have that fridge when you could just stick the spaghetti in ice outside?", "Radar Array", None, None, "The Skyway", False, False, False, False, False, None, None, None, None)
RadarArray = RoomClass(9, "Radar Array", "Cross-stitched metal rebar has been wrought towards the sky, \ncatching any plane in the area for two hundred miles.", None, "Survey Area 118", "Living Quarters", None, False, False, False, False, False, None, None, None, None)
SurveyArea118 = RoomClass(10, "Survey Area 118", "A barren expense of tundra, which Command seems to think guards something special.", None, None, None, "Radar Array", False, False, False, False, False, None, None, None, None)

listRooms = [CommandCenter, CommunicationsRoom, StrategyRoom, ConfrontationRoom, HillsideSteps, TheHarbor, TheSkyway, LivingQuarters, RadarArray, SurveyArea118]

# a couple non-direction functions

def quitSure():
    if input("Quit? y/n ") == "y":
        quit()
    else:
        travelling()

global isLockedRadar
isLockedRadar = False

# Help system

def provideHelp():
    h = input("\n1) I need help with understanding how a text adventure / interactive fiction work functions.\n2) I need help with specific commands.\n> ")
    if h == "1":
        print("Well, I guess you need to tell Lucas to actually write all this out.")
    elif h == "2":
        print("A list of the current commands available:\n'go [direction]' moves the player in the direction specified. Current supported directions are north, south, east, and west.")
        print("'n', 's', 'e', and 'w' all function as shorthand for the 'go' command.\n'i' returns your entire inventory.\n'drop [thing]' drops an item, if it's in your inventory; 'take [thing]' picks it up.")
        print("Inputting 'o' or 'objectives' provides the list of objectives you're currently working on.")
        print("'q' quits the game. 'h' provides help.")
    else:
        print("I don't quite understand that. Please put in 1 or 2. I'm returning you to the main game now.")
        travelling()

# inventory system

global inventory
inventory = ["rope"]

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
        if currentRoom.WantToDrop == False:
            inventory.remove(WantToDrop)
            print("You successfully "+mainloopInput[0]+" the "+WantToDrop+".")
            currentRoom.WantToDrop = True
        else:
            print("It is thrown into the void, never to be seen again. \nJust kidding. \n(It appears you've dropped something that can't be dropped in this room. \nTry dropping it somewhere else.)")
            currentRoom.WantToDrop = False
    else:
        print("You rummage through your backpack, but can't seem to find that item.")

def inventoryTake():
    global WantToTake
    ## WantToTake is the item the user wants to take. Pretty self-explanatory.
    if getattr(currentRoom,WantToTake) != ValueError:
        if getattr(currentRoom,WantToTake) == True:
            print("You "+mainloopInput[0]+" the heck out of that "+WantToTake+".")
            currentRoom.WantToTake = False
            inventory.append(WantToTake)
        else: 
            print("Seems like the item you want isn't here. \nIt might be in another room, or you might not have typed it correctly.\n")
    else:
        print("I don't think that's a thing you can take. \nSomething went wrong, anyway. Try again.\n")


def getItemsFromRoom(inputCurrentRoom, valuetoFind):
    global thingsInRoom
    global itemToGet
    thingsInRoom = list()
    for itemToGet in availableItemsList:
        if getattr(inputCurrentRoom, itemToGet) == valuetoFind:
            thingsInRoom.append(itemToGet)
            # print("Appending",itemToGet)
    return thingsInRoom

# examining objects

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
    if getattr(currentRoom,WantToExamine) != None:
        print(getattr(currentRoom,WantToExamine))
    else:
        print("Sorry, I couldn't find that in this room.")
    travelling()

# lists defined

takeList = ["take","grab","pickup","pick up","swipe","pick"]
dropList = ["drop","leave","yeet"]

eatList = ["consume","eat","devour","cronch","inhale"]

possibleDirections = ["west","north","south","east"]

global examineList
examineList = ["x", "examine", "investigate", "look"]
buttonExamination = ["button","buttons","redbutton","bluebutton"]
woodenExamination = ["woodenaircraft","woodenpieces","woodplanes","woodpieces","woodaircraft","aircraft","pieces"]

availableItemsList = ["rope", "shovel"]

AtatuqList = ["atatuq", "general atatuq", "general"]
RamonaList = ["ramona", "ramona butchers", "butchers"]
NathanList = ["nathan", "nate", "nathaniel", "nathaniel dessner", "dessner", "comms officer"]

AtatuqFlavor = ["is sitting and stroking his beard.","is puffing on his cigar.","is scowling at you.","is punching figures into a calculator.","is slumped in his chair."]
RamonaFlavor = ["is sulking in the corner.","is headbanging to punk music.","is tinkering with a cassette tape.","is observing a succulent.","is tracing a detailed map of the area."]
NathanFlavor = ["is spinning in his chair.","is practicing yodeling.","is sleeping.","is eating an MRE.","isn't doing any work anytime soon."]

AtatuqState = ['A', 0, 0]
RamonaState = ['R', 0, 0]
NathanState = ['N', 0, 0]


# goDirection and the variables it uses <------ STARTING ROOMS

global Cutscene
global newRoom
global currentRoom
Cutscene = True
newRoom = True
currentRoom = LivingQuarters # *****

NorthList = ["go north","north","n","go n"]
WestList = ["go west","west","w","go w"]
SouthList = ["go south","south","s","go s"]
EastList = ["go east","east","e","go e"]
AllDirectionList = ["go north","north","n","go n","go west","west","w","go w","go south","south","s","go s","go east","east","e","go e"]

def goingNorth():
    global currentRoom
    global newRoom
    global isLockedRadar
    if currentRoom == LivingQuarters:
        if (isLockedRadar == False) and ("key" not in inventory):
            print("It seems this door has been locked. \nGuess you'll have to find another way through, or get a key.")
            newRoom = False
            return
    print("Going north...")
    for entry in listRooms:
        if entry.name == currentRoom.north:
            currentRoom = entry
            break
    print("Entering",currentRoom.name)
    newRoom = True
    return

def goingSouth():
    global currentRoom
    global newRoom
    print("Going south...")
    for entry in listRooms:
        if entry.name == currentRoom.south:
            currentRoom = entry
            break
    print("Entering",currentRoom.name)
    newRoom = True
    return

def goingWest():
    global currentRoom
    global newRoom
    print("Going west...")
    for entry in listRooms:
        if entry.name == currentRoom.west:
            currentRoom = entry
            break
    print("Entering",currentRoom.name)
    newRoom = True
    return

def goingEast():
    global currentRoom
    global newRoom
    print("Going east...")
    for entry in listRooms:
        if entry.name == currentRoom.east:
            currentRoom = entry
            break
    print("Entering",currentRoom.name)
    newRoom = True
    return

## OBJECTIVES
UnspecObjectives = ["* Go find General Atatuq and receive his orders."]
AtatuqObjectives = []
RamonaObjectives = []
NathanObjectives = []

global AtatuqGameState
AtatuqGameState = 0

def printObjectives():
    if UnspecObjectives != []:
        print("\nMisc. Objectives:")
        print(*UnspecObjectives, sep="\n")
    if AtatuqObjectives != []:
        print("\nGeneral Atatuq Objectives:")
        print(*AtatuqObjectives, sep="\n")
    if RamonaObjectives != []:
        print("\nRamona Butchers Objectives:")
        print(*RamonaObjectives, sep="\n")
    if NathanObjectives != []:
        print("\nNathaniel Dessner Objectives:")
        print(*NathanObjectives, sep="\n")
    return


## doing TALK TO

def talkTo():
    """
    print("talkTo received", end=" ")
    print(*mainloopInput)
    print(rawCommandInput)
    """
    if currentRoom.atatuq == True:
        if mainloopInput[-1] in AtatuqList:
            AtatuqTalkTo()
    if currentRoom.ramona == True:
        if mainloopInput[-1] in RamonaList:
            RamonaTalkTo()
    if currentRoom.nathan == True: 
        if mainloopInput[-1] in NathanList:
            NathanTalkTo()
    print("Either the person isn't in the room, or I don't quite understand who you're trying to talk to. Try again.\nBe sure to use all LOWERCASE for names!")
    
def AtatuqTalkTo():
    if AtatuqState[1:] == [0,0]:
        beginCutsceneAtatuqOne()
    if AtatuqState[1:] == [0,1]:
        print("'Are you done?' he yells. 'No? Then go!'")
    if AtatuqState[1:] == [0,2]:
        beginCutsceneAtatuqFresnelFinish()
    else:
        print("Atatuq waves you away.")
    travelling()

def RamonaTalkTo():
    print("Ramona glares at you. 'Can't you tell I'm busy?'")
    travelling()

def NathanTalkTo():
    if NathanState[1:] == [0,0]:
        beginCutsceneNathanOne()
    if NathanState[1:] == [1,0]:
        beginCutsceneNathanFresnel()
    if NathanState[2] == [2,0]:
        beginCutsceneNathanBoat()
    else:
        print("Nathan thumps his hackeysack against a terminal. 'Hey! I'm workin' here!'")
    travelling()


## STARTING CUTSCENES, stopping the travelling() loop.

## ATATUQ

def beginCutsceneAtatuqOne():
    print("Atatuq grimaces. 'Good morning, Lieutenant,' he barks. \n'The plan is simple today. Do your work and I won't shove my walking stick so far up your-'\n'What do you need me to do, sir?' you ask. \n'Get Nathaniel Dessner out of his chair and into the lighthouse. \nHe needs to fix the Fresnel lens by 1100 hours or that flashing light will be the last thing he sees.\nYou can find him in the Comms Room, north of here. If he isn't sleeping.'")
    AtatuqState[2] = 1
    NathanState[1] = 1
    choice = input("Do you say: \n1. 'Of course, sir.'\n2. 'I'm sure he'd be more than happy to.'\n>> ")
    if choice == "1":
        print("'Mmph,' he grunts. What a jag. Best get to work.")
        travelling()
    elif choice == "2":
        print("'That slacker would love nothing more, I'm sure.' Man, Nathaniel can be a jag sometimes. Best get to work.")
        travelling()
    else:
        beginCutsceneAtatuqOne()

def beginCutsceneAtatuqFresnelFinish():
    choice = input("\nThe old general smiles. 'Did ya do it?' As you nod, he grins and pats you on the back. \n'Good work. Now, are you ready for your next task?' \n1. 'Yes, General.'\n2. 'Please, give me a moment to get ready.'\n>> ")
    if choice == "1":
        print("'Good,' he snaps. 'Talk to Ramona. \nI want you to work with her on collecting samples out in the Northeast Quadrant, east of the Radar Array.'")
        AtatuqState = ["A",1,0]
        RamonaState = ["R",1,0]
        travelling()
    elif choice == "2":
        print("'Alright. But get back to me as soon as you can.'")
        travelling()
    else:
        beginCutsceneAtatuqFresnelFinish()

## NATHAN

def beginCutsceneNathanOne():
    choice = input("Nathan shrugs. 'Whaddaya want?'\n1. You seen the general? \n2. Not much. What's up?\n>> ")
    if choice == "1":
        print("'He's probably in his hidey-hole at the south end of the station. Pft.' You leave Nathan to it.")
    elif choice == "2":
        print("'Whatever it is, it's very important.' Nathan apparently thinks he's said enough.")
    else:
        beginCutsceneNathanOne()
    travelling()

def beginCutsceneNathanFresnel():
    choice = input("Nathan shrugs. 'Whaddaya want?'\n1. 'Weren't you supposed to fix the Fresnel yesterday?' \n2. 'General's on my case again about the lens. You know what to do.'\n>> ")
    if choice == "1":
        print("\n'Like you're such a saint. I'll do it later.' It's a wonder Nate wasn't fired months ago.")
    elif choice == "2":
        print("\n'Doing things isn't my strong suit.' You both chuckle, but he doesn't seem to get the hint.")
    else:
        beginCutsceneNathanFresnel()
    choice = input("Listen. If you're so intent on this, why don't you do it yourself?\n1. 'Is that whiff of insubordination I detect?' \n2. 'Because you're gonna do it.'\n>> ")
    if choice == "1":
        print("\nNathan smirks. 'Alright, alright. Consider it done.'")
        AtatuqState[2] = 2
        NathanState[1] = 2
    elif choice == "2":
        print("\nNathan scoffs. 'Or what? You're hopeless.' \nGuess you're gonna have to try and get through to him some other way.")
    else:
        beginCutsceneNathanFresnel()
    travelling()
    


"""
def beginCutscene(CutNum):
    Cutscene = True
    if CutNum == 1:
        # print("WE PAST THE ONE CHECK")
        cutsceneGeneralAnatuq()
    else:
        return
"""

## CUTSCENE 'GENERAL' PATHS




def travelling():
    global newRoom
    while Cutscene == False:
        global currentRoom
        print("\n=============", end="")
        if newRoom == True:
            print("\n\nYou are now in: ", end="")
            print(currentRoom.name)
            print(currentRoom.descrip)
            getItemsFromRoom(currentRoom, True)
            if thingsInRoom != []:
                print("\nHere, you notice: ", sep=", ")
            print(*thingsInRoom, sep=", ")
            print("\n")
            if currentRoom.atatuq == True:
                r = random.choice(AtatuqFlavor)
                print("General Atatuq",r)
            if currentRoom.ramona == True:
                r = random.choice(RamonaFlavor)
                print("Ramona",r)
            if currentRoom.nathan == True:
                r = random.choice(NathanFlavor)
                print("Nathan",r)
            print("\nThe possible exits are: ")
            for direction in possibleDirections:
                if getattr(currentRoom,direction) != None:
                    print(direction)
        global mainloopInput
        global rawCommandInput
        newRoom = False
        rawCommandInput = input("\n>> ")
        mainloopInput = rawCommandInput.lower().split()
        if mainloopInput == []:
            travelling()
        if mainloopInput[0] in examineList:
            if len(mainloopInput) == 1:
                print(currentRoom.descrip)
            else: # If the player wants to examine an object and not the room in general
                mainloopInput.pop(0)
                global WantToExamine
                WantToExamine = "".join(mainloopInput)
                examineItem()
                travelling()
        if (mainloopInput[0] == "talk") or (mainloopInput[0:1] == ["talk","to"]):
            if mainloopInput[1] != "to":
                mainloopInput.pop(0)
                mainloopInput.insert(0,'talk')
                mainloopInput.insert(1, 'to')
            talkTo()
            travelling()
        if len(mainloopInput) == 2: # IF THE COMMAND IS TWO WORDS
            if mainloopInput[0] == "go":
                break
            elif mainloopInput[0] in dropList:
                global WantToDrop
                WantToDrop = mainloopInput[1]
                inventoryDrop()
            elif mainloopInput[0] in takeList:
                global WantToTake
                WantToTake = mainloopInput[1]
                inventoryTake()
            elif not (rawCommandInput in AllDirectionList):
                print("\nI don't understand that verb and object. Try 'go [direction]' or 'take [item]'.\n")
        elif rawCommandInput in NorthList:
            if currentRoom.north != None:
                goingNorth()
            else:
                print("You can't go north from here.")
        elif rawCommandInput in SouthList:
            if currentRoom.south != None:
                goingSouth()
            else:
                print("You can't go south from here.")
        elif rawCommandInput in WestList:
            if currentRoom.west != None:
                goingWest()
            else:
                print("You can't go west from here.")
        elif rawCommandInput in EastList:
            if currentRoom.east != None:
                goingEast()
            else:
                print("You can't go east from here.")
        elif mainloopInput[0] == "i":
            inventoryCheck()
        elif rawCommandInput == "q":
            quitSure()
        elif mainloopInput[0] == "h":
            provideHelp()
        elif (rawCommandInput == "o") or (rawCommandInput == "objectives"):
            printObjectives()
        elif rawCommandInput == "qy":
            quit()
        else:
            print("Whoops! I don't quite understand that input.")


# Starting the game, plus early description.

print("\n\n\n\tCAPE DYER. A THRILLING TALE OF NUCLEAR WAR, RADIOACTIVE COWS, AND BIG RED BUTTONS. \n")
print("If you're not familiar with standard interactive fiction nomenclature, enter 'h' for help.\n\n")
print("JUNE 24, 1984, CAPE DYER, NORTHWEST TERRITORIES, CANADA.")
print("You are ALICE WHITE, the lieutenant presiding officer at Cape Dyer, a nuclear-strike early-warning station in the frigid wastes of the Canadian northern islands. Of course, that sounds exciting. Edge-of-your-seat kind of stuff. But most days, it's incredibly dull, and cold. You huddle in your base and do contract work for Environmental Canada Services. But all that is going to change today, and your decisions will shape the future of the entire planet.\n")
print("For now, however, you've just woken up in the kitchen. Must've fallen asleep during a midnight snack again - thank goodness the General didn't catch you. Every day, your first task is to go receive his orders. Better get on that.\n\n")

Cutscene = False
newRoom = True
travelling()