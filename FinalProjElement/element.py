# element.py
# part of the Periodic Table project by Lucas Eggers
# main file is finalproject.py

# IMPORTS
import random
from random import shuffle
import csv

def importTest():
    print("\nnote: element.py import successful.")

# CREATING THE Element CLASS with basic display features
class Element:
    kind = 'element'
    def __init__(self, element, number, symbol, weight):
        self.element = element
        self.number = number
        self.symbol = symbol
        self.weight = weight

    def show(self):
        print("\nElement: ",str(self.element),"\nAtomic Number: ",str(self.number),"\nSymbol: ",str(self.symbol),"\nAtomic Weight: ",str(self.weight))