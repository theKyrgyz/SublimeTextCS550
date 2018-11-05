# finalproject.py

# An element manipulator by Lucas Eggers
# DATE: November 3, 2018
# DESCRIPTION: 
# SOURCES: https://docs.python.org/3/library/csv.html for importing csv files into Python
#          https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python for string-to-float checks

""" 
Assignment:
Compose  a  data  type  Element  for  entries  in  the  periodic  table  of 
elements.  Include  data  type  values  for  element,  atomic  number, symbol, 
and  atomic  weight  and  accessor  methods  for  each  of  these  values. 
Then,  create  a  data  type  PeriodicTable  that  reads  values  from a  file  to 
create  a  list  of  Element  objects  and  responds  to  queries  on  input  so  that 
a  user  can  type  a  molecular  equation  like  H2O  and  the  program 
responds  by  printing  the  molecular  weight.  What  other  kinds  of 
interactions  can  you  create  within  this  class? 
The  file  here: 
https://introcs.cs.princeton.edu/python/32class/elements.csv 
contains the  data  that  the program  should  read.  
Include  fields  for element, atomic  number, symbol,  and  atomic  weight.
"""

import element
from element import Element
import csv, re, string

element.importTest()

elementList = []

class PeriodicTable:
    kind = 'periodic table'
    def __init__(self, inputFile):
        self.inputFile = inputFile
        self.create()
        # self.FL is the 'Full List' of inputted elements in that periodic table.
        self.FL = elementList

    def create(self):
        with open(self.inputFile, newline='') as csvfile:
            elementreaderA = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in elementreaderA:
                ATS = ', '.join(row)
                # ATS stands for Attributes to Separate. It's a single element row's attributes, which will then be separated and put inside an Element object.
                ATS = ATS.split(',')
                elementList.append(Element(ATS[0],ATS[1],ATS[2],ATS[3]))

    def printEntireTable(self):
        if elementList == []:
            print("This table empty, yeet.")
        else:
            for i in elementList:
                if i != None:
                    i.show()
            print("\n")

    def ElemByNumber(self,number):
        for elemTest in self.FL:
            if int(elemTest.number) == int(number):
                elemTest.show()
                print("\n")
                f = elemTest

    def ElemByWeight(self,wgt):
        for elemTest in self.FL:
            if float(elemTest.weight) == float(wgt):
                elemTest.show()
                print("\n")
                f = elemTest
                return
        print("I don't see any element with that number.")

    def ElemByName(self,name):
        for elemTest in self.FL:
            if str(elemTest.element) == str(name):
                elemTest.show()
                print("\n")
                f = elemTest
                return
        print("I don't see any element with that number.")

    def ElemBySymbol(self,sym):
        for elemTest in self.FL:
            if str(elemTest.symbol) == str(sym):
                print("\n")
                f = elemTest
                return f
        print("I don't see any element with that symbol.")

    def WeightMolec(self,inputMol):
        print(inputMol)
        molWeight = 0.0
        for chunk in inputMol:
            y, z = "None", "0"
            SOLE = True
            m = list(chunk)
            for x in m:
                if x.isdigit() == True:
                    SOLE = False
            if SOLE == True:
                molWeight += float((self.ElemBySymbol(str(chunk))).weight)
            for x in range(0,len(chunk)):
                # print(chunk,x,chunk[x],chunk[x-1])
                if (chunk[x] in string.digits) and (chunk[x-1] in string.ascii_letters):
                    y = chunk[:x]
                    z = chunk[x:]
                    # print("Yes!")
            if y != "None":
                molWeight += float((self.ElemBySymbol(str(y))).weight) * float(z)
        return molWeight

def splitter(s):
    l = list(s)
    v, vPrev = 0, 0
    resultList = []
    while v < len(l):
        if (s[v] in string.ascii_uppercase) and (v != 0):
            resultList.append(s[vPrev:v])
            vPrev = v
        if v == len(l)-1:
            resultList.append(s[vPrev:v+1])
            vPrev = v
        v += 1
    return resultList

def BeginRequest(p):
    choice = input("What would you like to do in the wonderful world of chemistry today?\n1  Find an element by atomic number.\n2  Find an element by name.\n3  Find an element by atomic weight [precision required].\n4  Find an element by symbol.\nM  Find the weight of a molecule. [COOL FEATURE!]\nQ  Quit.\n\n>> ")
    if choice == "1":
        i = input("\nPlease input the number of the element you wish to find.\n>> ")
        try:
            float(i)
            p.ElemByNumber(i)
        except ValueError:
            print("\n")
    elif choice == "2":
        i = input("\nPlease input the name of the element you wish to find. Capitalization and spelling are key.\n>> ")
        p.ElemByName(i)
    elif choice == "3":
        i = input("\nPlease input the weight of the element you wish to find. Note: must be exactly what is on file.\n>> ")
        try:
            float(i)
            p.ElemByWeight(i)
        except ValueError:
            print("\n")
    elif choice == "4":
        i = input("\nPlease input the symbol of the element you wish to find. Capitalization and spelling are key.\n>> ")
        (p.ElemBySymbol(i)).show()
        print("\n")
    elif choice == "M":
        i = input("\nPlease input the chemical formula of the molecule whose atomic weight you want to find.\n>> ")
        print("\nThe weight of this molecule,",i,", is:",round(p.WeightMolec(splitter(i)), 4),"\n")
    elif choice.upper() == "Q":
        print("\n")
        quit()
    else:
        print("I don't understand.\n")

P1 = PeriodicTable("elements.csv")

while True:
    BeginRequest(P1)

