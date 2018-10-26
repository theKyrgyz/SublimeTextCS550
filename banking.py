# banking.py
# Account management

import random

def askName():
    NameSelection = input("Please input the name you want associated with your account.\n>> ")
    return NameSelection

def askPin():
    while True:
        PinSelection = input("Please input the 4-digit pin you want associated with your account.\n>> ")
        if len(PinSelection) == 4:
            return int(PinSelection)

def genID():
        y = "0"
        for i in range(0,4):
            z = str(random.randint(0,9))
            y += z
        return str(y)

class Account:
    kind = 'bank account'
    # constructor:
    # initializes properties, sets up the animal object
    def __init__(self):
        #, number, name, wild, location
        self.ID = genID()
        self.holdername = askName()
        self.PIN = askPin()
        self.amount = 0

    # methods / functions

    def stats(self):
        print("\n")
        print("ACCOUNT NAME: "+self.holdername)
        print("ACCOUNT BALANCE: $"+str(self.amount))
        print("\n")

    def deposit(self, amtToAdd):
        self.amount += amtToAdd
        print("Deposit was successful. Current balance is: $"+str(self.amount)+"\n")

    def withdraw(self, amtToRemove):
        self.amount -= amtToRemove
        print("Withdrawal was successful. Grab your cash and go! Current balance is: $"+str(self.amount)+"\n")

    def checkPin(self, guess):
        if str(g) == str(self.PIN):
            return True
        else:
            return False

listAccounts = []

listAccounts.append(Account())

print(listAccounts[0].__dict__)

def inputLoop():
    while True:
        listAccounts[vCurr].stats()
        choice = input("(1) Make a deposit.\n(2) Make a withdrawl.\n(3) Change PIN.\n(4) Close account.\n>> ")
        if choice == "1":
            global g
            g = input("Please input your PIN.")
            if listAccounts[vCurr].checkPin(g) == True:
                x = input("Please state how much of the revenue from your exploited labor you'd like to deposit.\n>> ")
                if int(x) != ValueError:
                    listAccounts[vCurr].deposit(int(x))
                else:
                    print("That's not a number.")
            else:
                print("\nIncorrect PIN. I'm calling the police.\n")
        elif choice == "2":
            g = input("Please input your PIN.")
            if listAccounts[vCurr].checkPin(g) == True:
                x = input("Please state how much moolah you'd like to withdraw.\n>> ")
                if int(x) != ValueError:
                    listAccounts[vCurr].withdraw(int(x))
                else:
                    print("That's not a number.")
            else:
                print("\nIncorrect PIN. I'm calling the police.\n")
        else:
            print("I don't quite understand that.")

vCurr = 0
inputLoop()
