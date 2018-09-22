# capedyerClass.py

class RoomClass:

    kind = 'room'

    def __init__(self, number, name, descrip, north, east, south, west, rope, shovel):
        self.number = number
        self.name = name
        self.descrip = descrip
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.rope = rope
        self.shovel = shovel


CommandCenter = RoomClass(1, "Command Center", "This is where the magic happens.", "Apex Room", "The Skyway", "Confrontation Room", "Strategy Room", False, False)
ApexRoom = RoomClass(2, "Apex Room", "You look out through the glass, over the icy waters.", "Hillside Steps", None, "Command Center", None, False, True)
StrategyRoom = RoomClass(3, "Strategy Room", "The westernmost room of the facility. A table stands in the center, with a map of Baffin Island taped across its entire length.", None, "Command Center", None, None, False, False)
ConfrontationRoom = RoomClass(4, "Confrontation Room", "The general's office. Oof.", "Command Center", None, None, None, False, False)
HillsideSteps = RoomClass(5, "Hillside Steps", "A series of rugged stairs leading from the facility down to the ocean.", "The Harbor", None, "Apex Room", None, False, False)
TheHarbor = RoomClass(6, "The Harbor", "Boats, seaplanes, and icebreakers alike are lined up next to a rusty metal dock.", None, None, "Hillside Steps", None, False, False)
TheSkyway = RoomClass(7, "The Skyway", "A see-through tunnel connecting the command and living centers of the base.", None, "Living Quarters", None, "Command Room", False, False)
LivingQuarters = RoomClass(8, "Living Quarters", "A humble kitchen,  fit for the half-dozen inhabitants of this forsaken place.\nBut truly, why have that fridge when you could just stick the spaghetti in ice outside?", "Radar Array", None, None, "The Skyway", False, False)
RadarArray = RoomClass(9, "Radar Array", "Cross-stitched metal rebar has been wrought towards the sky, \ncatching any plane in the area for two hundred miles.", None, None, "Living Quarters", None, False, False)

listRooms = [CommandCenter, ApexRoom, StrategyRoom, ConfrontationRoom, HillsideSteps, TheHarbor, TheSkyway, LivingQuarters, RadarArray]



global Cutscene
global newRoom
global currentRoom
Cutscene = True
newRoom = True
currentRoom = CommandCenter

NorthList = ["go north","north","n","go n"]
WestList = ["go west","west","w","go w"]
SouthList = ["go south","south","s","go s"]
EastList = ["go east","east","e","go e"]

def goingNorth():
    global currentRoom
    global newRoom
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

"""
def goingDirection(direc):
    direcUsed = direc
    global currentRoom
    global newRoom
    print("Going",direc)
    for entry in listRooms:
        if entry.name == currentRoom.direcUsed:
            currentRoom = entry
    print("Entering",currentRoom.name)
    newRoom = True
    return
"""

def travelling():
    global newRoom
    while Cutscene == False:
        global currentRoom
        if newRoom == True:
            print("\n\nYou are now in: ", end="")
            print(currentRoom.name)
            print(currentRoom.descrip)
        global mainloopInput
        global rawCommandInput
        newRoom = False
        rawCommandInput = input("\n>> ")
        mainloopInput = rawCommandInput.lower().split()
        if mainloopInput == []:
            travelling()
        elif rawCommandInput in NorthList:
            if currentRoom.north != None:
                goingNorth()
                print(newRoom)
            else:
                print("You can't go north from here.")
        elif rawCommandInput in SouthList:
            if currentRoom.south != None:
                goingSouth()
                print(newRoom)
            else:
                print("You can't go south from here.")
        elif rawCommandInput in WestList:
            if currentRoom.west != None:
                goingWest()
                print(newRoom)
            else:
                print("You can't go west from here.")
        elif rawCommandInput in EastList:
            if currentRoom.east != None:
                goingEast()
                print(newRoom)
            else:
                print("You can't go east from here.")
        elif rawCommandInput == "q":
            quit()
        else:
            print("Whoops! I don't quite understand that.")

print("\n\n\n\tCAPE DYER. A THRILLING TALE OF NUCLEAR WAR, RADIOACTIVE COWS, AND BIG RED BUTTONS. \n")
# NOTE TO SELF: INSERT INSTRUCTIONS TO PLAYER HERE
Cutscene = False
newRoom = True
travelling()