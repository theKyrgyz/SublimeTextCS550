# finalproject.py

# An element and periodic table manipulator by Lucas Eggers
# DATE: November 3, 2018
# DESCRIPTION: This project uses two Python code files and a csv file to create two object classes [Element and PeriodicTable] which can then be manipulated and used to calculate things,
#              like the weight of a given molecule.
# SOURCES: https://docs.python.org/3/library/csv.html for importing csv files into Python
#          https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python for string-to-float checks

import element, csv, re, string
from element import Element

element.importTest()

class PeriodicTable:
    kind = 'periodic table'
    def __init__(self, inputFile):
        global elementList
        elementList = []
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
                f = elemTest
                return f
        return None
        # print("I don't see any element with that symbol.")

    def WeightMolec(self,inputMol):
        # print(inputMol)
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
            if (y != "None") and (self.ElemBySymbol(str(y)) != None):
                molWeight += float((self.ElemBySymbol(str(y))).weight) * float(z)
            if self.ElemBySymbol(str(y)) == None:
                print("NOTE TO USER: In your molecule you've inputted \na symbol which doesn't have a corresponding element. \nThis means your result won't be accurate. \nBe advised.")
        return molWeight

# VARIOUS NON-CLASS FUNCTIONS - the MAIN LOOP (beginRequest) and the STRING MANIPULATOR (splitter)

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

def beginRequest(p):
    choice = input("What would you like to do in the wonderful world of chemistry today?\n1  Find an element by atomic number.\n2  Find an element by name.\n3  Find an element by atomic weight [precision required].\n4  Find an element by symbol.\nM  Find the weight of a molecule. [COOL FEATURE!]\nQ  Quit.\n\n>> ")
    if choice == "1":
        i = input("\nPlease input the number of the element you wish to find.\n>> ")
        try:
            float(i)
            p.ElemByNumber(i)
        except ValueError:
            print("\n")
    elif choice == "2":
        i = input("\nPlease input the name of the element you wish to find. \nCapitalization and spelling are key.\n>> ")
        p.ElemByName(i)
    elif choice == "3":
        i = input("\nPlease input the weight of the element you wish to find. \nNote: must be exactly what is on file.\n>> ")
        try:
            float(i)
            p.ElemByWeight(i)
        except ValueError:
            print("\n")
    elif choice == "4":
        i = input("\nPlease input the symbol of the element you wish to find. \nCapitalization and spelling are key.\n>> ")
        (p.ElemBySymbol(i)).show()
        print("\n")
    elif choice == "M":
        i = input("\nPlease input the chemical formula of the molecule \nwhose molecular weight you want to find.\n>> ")
        print("\nThe weight of this molecule,",i,", is:",round(p.WeightMolec(splitter(i)), 4),"\n")
    elif choice.upper() == "Q":
        print("\n")
        quit()
    else:
        print("I don't understand.\n")

P1 = PeriodicTable("elements.csv")

print("\nNOW ENTERING... CAMERON'S CRAZY and CONCIEVABLY CRIMINAL CHEMICAL CACHE!!!\n")
while True:
    beginRequest(P1)

