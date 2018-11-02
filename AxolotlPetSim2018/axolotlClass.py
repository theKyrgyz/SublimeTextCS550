# axolotlClass.py - class file for the axolotl pet

# plan out your code
"""
PROPERTIES: (ex. dog):
breed, size, color, name, home, food/diet, owner, skills/tricks, energy level, hunger/needs, captivity/no
Needs: energy, hunger, thirst, happiness

METHODS: (things it can do):
walk, eat, sleep, play, fetch, roll over, bark, pee

NOW: create the dog class - the general plan for the object
"""
import random

class axolotl:
    kind = 'axolotl pet'
    # constructor:
    # initializes properties, sets up the animal object
    def __init__(self, number, name="John", wild=False, loc="Minneapolis", hunger=4, energy=4):
        #, number, name, wild, location
        self.number = number
        self.name = name
        self.wild = wild
        self.loc = loc
        self.hunger = hunger
        self.energy = energy

    # methods / functions

    def eat(self, amt):
        status = ""
        if amt == 0:
            print("You didn't pick anything that "+self.name+" could eat.")
            mainLoop()
        if self.hunger > 0:
            self.hunger -= int(2*amt)
            self.energy += int(1*amt)
            if self.hunger < 0:
                self.hunger = 0
            if self.energy > 10:
                self.energy = 10
            status = self.name+" just gobbled that sweet sweet yum yum."
        else:
            status = self.name+" wouldn't take a single bite."

    def sleep(self):
        status = ""
        if self.energy > 0:
            self.hunger += 2
            self.energy += 5
            if self.hunger > 10:
                self.hunger = 10
            if self.energy < 0:
                self.energy = 0
            status = self.name+" slept soundly for the day."
        else:
            status = self.name+" is too restless! They won't sleep now."

    def checkWild(self):
        if self.wild == True:
            return "In the wild"
        else:
            return "In captivity"

    def stats(self):
        return "\nYOUR PET AXOLOTL:\n"+"Name: "+self.name+"\nCaptivity Status: "+self.checkWild()+"\nLocation: "+self.loc+"\nHunger: "+str(self.hunger)+"\nEnergy: "+str(self.energy)

"""
def showStats(pet):
    print("\nYOUR PET AXOLOTL:\n"+"Name: "+pet.name+"\nCaptivity Status: "+checkWild(pet.wild)+"\nLocation: "+pet.loc+"\nHunger: "+pet.hunger+"\nEnergy: "+pet.energy)
"""

def howMuchEat():
    foodInput = input("What would you like to feed your axolotl? \n(1) A food pellet. \n(2) A squirmy worm. \n(3) A whole freakin' fish.\n>> ")
    if foodInput < 4:
        return int(foodInput)
    else:
        return 0

PetNames = ["Xochitl","Benny","Tizoc","Tlaco","Yaotl","Ruben","Jacobin"]
CaptiveLocs = ["El Paso","Dallas","Washington","Bordeaux","Shreveport","Galveston","Phoenix"]
WildLocs = ["Xochimilco","Chalco","Mexico City","Tlaxcala"]

A1 = axolotl(1, "Xochitl", False, "El Paso", 5, 5)

def creationProcess():
    isWild = random.choice([True, False])
    if isWild == True:
        P1 = axolotl(2, random.choice(PetNames), True, random.choice(WildLocs), random.randint(2,6), random.randint(3,7))
    else:
        P1 = axolotl(2, random.choice(PetNames), False, random.choice(CaptiveLocs), random.randint(3,7), random.randint(2,6))

creationProcess()

print(P1.__dict__)

def mainLoop(): 
    while True:
        print(P1.stats()+"\n")
        choice = input("Choose how you'd like to care for your pet.\n>> ")
        if choice == "eat":
            P1.eat(howMuchEat())
        elif choice == "sleep":
            P1.sleep()
        else:
            print("I don't quite understand that.")
mainLoop()
