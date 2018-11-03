# element.py

import random
from random import shuffle
import csv

def importTest():
    print("\nelement.py import successful.\n")

class Element:
    kind = 'element'
    def __init__(self, element, number, symbol, weight):
        self.element = element
        self.number = number
        self.symbol = symbol
        self.weight = weight

    def show(self):
        print("\nElement: ",str(self.element),"\nAtomic Number: ",str(self.number),"\nSymbol: ",str(self.symbol),"\nAtomic Weight: ",str(self.weight))

"""
E1 = Element("Hydrogen",1,"H",1.01)
E1.show()
"""

"""
elementList = []
with open('elements.csv', newline='') as csvfile:
    elementreaderA = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in elementreaderA:
        print(', '.join(row))
        ATS = ', '.join(row)
        # ATS stands for Attributes to Separate. It's a single element row's attributes, which will then be separated and put inside an Element object.
        ATS = ATS.split(',')
        print(ATS)
        elementList.append(Element(ATS[0],ATS[1],ATS[2],ATS[3]))

if elementList == []:
    print("This table empty, yeet.")
else:
    for i in elementList:
        if i != None:
            i.show()
    print("\n")
"""


