# GuessingGame.py

import random as ra
import math as ma
import sys

def isInteger(value):
  try:
    int(value)
    return True
  except ValueError:
    return False

def guessSequence():
    x = ra.randint(1, 5)
    c = input("Guess a number between one and five! See if you're right! \n> ")
    if isInteger(c) == True:
        if 1 <= int(c) <= 5:
            c = int(c)
            if x == c:
                print("Woo-hoo! You got it - that was my number! Good for you! \n Phew. I'm tired from all this guessing. Cya later!\n")
                quit()
            else:
                print("Not quite! \nMy number was",str(x),". Try again!\n")
                guessSequence()
        else:
            print("Nope - that's not a number between one and five! Try again!\n")
            guessSequence()
    else: 
        print("That's not a valid integer! Try again!\n")
        guessSequence()

guessSequence()
