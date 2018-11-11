# finalproject.py

# An element and periodic table manipulator by Lucas Eggers
# DATE: November 3, 2018
# DESCRIPTION: This project uses two Python code files and a csv file to create two object classes [Element and PeriodicTable] which can then be manipulated and used to calculate things,
#              like the weight of a given molecule.
# SOURCES: https://docs.python.org/3/library/csv.html for importing csv files into Python
#          https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python for string-to-float checks

# IMPORTS
import element, csv, re, string, types
from element import Element

element.importTest()

# CREATING THE PERIODIC TABLE CLASS
class PeriodicTable:
    kind = 'periodic table'
    # INIT takes inputFile attribute - this is the csv file in the folder we want to turn into our table
    def __init__(self, inputFile):
        global elementList
        elementList = []
        self.inputFile = inputFile
        self.create()
        # self.FL is the 'Full List' of inputted elements in that periodic table.
        self.FL = elementList

    # The main table creation function
    def create(self):
        with open(self.inputFile, newline='') as csvfile:
            elementreaderA = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in elementreaderA:
                ATS = ', '.join(row)
                # ATS stands for Attributes to Separate. It's a single element row's attributes, which will then be separated and put inside an Element object.
                ATS = ATS.split(',')
                elementList.append(Element(ATS[0],ATS[1],ATS[2],ATS[3]))

    # Printing the entire table neatly. Isn't used in this program, though. 
    def printEntireTable(self):
        if elementList == []:
            print("This table empty, yeet.")
        else:
            for i in elementList:
                if i != None:
                    i.show()
            print("\n")

    # The next four functions are calling the table and searching through it for an element, based on one of its attributes.
    def ElemByNumber(self,number):
        for elemTest in self.FL:
            if int(elemTest.number) == int(number):
                elemTest.show()
                print("\n")
                f = elemTest
                return
        print("\nI don't see any element with that number.")

    def ElemByWeight(self,wgt):
        for elemTest in self.FL:
            if float(elemTest.weight) == float(wgt):
                elemTest.show()
                print("\n")
                f = elemTest
                return
        print("\nI don't see any element with that weight.\n")

    def ElemByName(self,name):
        name = name.capitalize()
        for elemTest in self.FL:
            if str(elemTest.element) == str(name):
                elemTest.show()
                print("\n")
                f = elemTest
                return f
        print("\nI don't see any element with that name.")

    # This one in particular is used in the molecular weight function to call the weight of element based on its symbol.
    def ElemBySymbol(self,sym):
        for elemTest in self.FL:
            if str(elemTest.symbol) == str(sym):
                f = elemTest
                return f
        return None
        print("\n")

    # The function which determines the weight of the molecule, inputted by user.
    def WeightMolec(self,inputMol):
        # At this stage inputMol is a list of the different elements w/ coefficients, like ['H2','Se10']
        molWeight = 0.0
        # At the beginning the molecular weight is 0, of course. Now, for each item in the list...
        for chunk in inputMol:
            y, z = "None", "0"
            SOLE = True
            m = list(chunk)
            # Checking... is this item without a coefficient? Well, that's an implied '1'. So treat it as such. Add that weight.
            for x in m:
                if x.isdigit() == True:
                    SOLE = False
            if (SOLE == True) and ((self.ElemBySymbol(str(chunk)) != None)):
                # molWeight += float((self.ElemBySymbol(str(chunk))).weight)
                y = chunk
                z = 1
            # If the chunk has a coefficient at the end, split it into two parts: the letters/element and the number/coefficient
            for x in range(0,len(chunk)):
                if (chunk[x] in string.digits) and (chunk[x-1] in string.ascii_letters):
                    y = chunk[:x]
                    z = chunk[x:]
            if (y != "None") and (self.ElemBySymbol(str(y)) != None):
                # Essentially, "If you *can* (without breaking the code), multiply the weight of the element by the coefficient"
                molWeight += float((self.ElemBySymbol(str(y))).weight) * float(z)
            if self.ElemBySymbol(str(y)) == None:
                # This is printed if the user inputs an elemental symbol that simply isn't associated with an actual element
                print("NOTE TO USER: In your molecule you've inputted \na symbol which doesn't have a corresponding element. \nThis means your result won't be accurate. \nBe advised.")
        return molWeight

    # checking ionic bond stability based on the number of electrons in the combined molecule
    def ionicStability(self,a,b):
        ionicList = [2,4,12,20,28,36,44,52,60,68,76,84,90,118]
        print("\nBased on the number of electrons in each element...")
        if ((a+b) in ionicList):
            print("\nThat would work very well as an ionic bond. Stability would be high.")
        elif ((a+b)-1 in ionicList) or ((a+b)+1 in ionicList):
            print("\nThat would combine to form a poor ionic bond. \nStability would be low, and the resulting compound would be highly reactive.")
        else:
            print("\nIonic bond stability uncertain. \nThe bond would not be entirely stable, but not entirely reactive either.")
        print("\nNumber of electrons in the molecule with the ionic bond would be:",(a+b),".\n")



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
    choice = input("What would you like to do in the wonderful world of chemistry today?\nFIN  Find an element by name, number, or symbol.\nWGT  Find an element by atomic weight [precision required].\nION  Check the stability of an ionic bond between two given elements.\nMOL  Find the weight of a molecule. [COOL FEATURE!]\nQ  Quit.\n\nOTHERWISE, just input the name, number, or symbol of an element for info.\n\n>> ")
    if choice.upper() == "FIN":
        i = input("\nPlease input the number, name, or symbol of the element you wish to find.\n>> ")
        try:
            int(float(i))
            if str(int(float(i))+0.0) != str(float(i)):
                print("\nThe number you've put in isn't an integer. \nRounding down...\n")
            p.ElemByNumber(int(float(i)))
        except ValueError:
            if len(i) < 3:
                if (p.ElemBySymbol(i)) != None:
                    (p.ElemBySymbol(i)).show()
                    print("\n")
                else:
                    print("\nSorry, I don't see an element with that symbol.")
            else:
                p.ElemByName(i)
        print("\n")
    elif choice.upper() == "WGT":
        i = input("\nPlease input the weight of the element you wish to find. \nNote: must be exactly what is on file.\n>> ")
        try:
            float(i)
            p.ElemByWeight(i)
        except ValueError:
            print("\n")
    elif choice.upper() == "ION":
        a = input("\nPlease input the symbol or the name of the first element in the bond.\n>> ")
        if len(a) < 3:
            if (p.ElemBySymbol(a)) != None:
                a = p.ElemBySymbol(a)
                a.show()
            else:
                print("\nSorry, I don't see an element with that symbol.")
        else:
            a = p.ElemByName(a)
        b = input("\nPlease input the symbol or the name of the second element in the bond.\n>> ")
        if len(b) < 3:
            if (p.ElemBySymbol(b)) != None:
                b = p.ElemBySymbol(b)
                b.show()
            else:
                print("\nSorry, I don't see an element with that symbol.")
        else:
            b = p.ElemByName(b)
        if (type(a) == element.Element) and (type(b) == element.Element):
            p.ionicStability(int((a).number),int((b).number))
        else:
            print("\nSorry, it seems like somewhere along the line you didn't input an element.\n")
    elif choice.upper() == "MOL":
        i = input("\nPlease input the chemical formula of the molecule \nwhose molecular weight you want to find.\n>> ")
        print("\n")
        print("\nThe weight of this molecule,",i,", is:",round(p.WeightMolec(splitter(i)), 4),"\n")
    elif choice.upper() == "Q":
        print("\n")
        quit()
    else:
        # if no option is clearly chosen, run it through the general info-search intelligence function
        i = choice
        try:
            int(float(i))
            if str(int(float(i))+0.0) != str(float(i)):
                print("\nThe number you've put in isn't an integer. \nRounding down...\n")
            p.ElemByNumber(int(float(i)))
        except ValueError:
            if len(i) < 3:
                if (p.ElemBySymbol(i)) != None:
                    (p.ElemBySymbol(i)).show()
                    print("\n")
                else:
                    print("\nSorry, I don't see an element with that symbol.")
            else:
                p.ElemByName(i)

# CREATING THE PERIODIC TABLE
P1 = PeriodicTable("elements.csv")

# BEGINNING THE ACTUAL INTERFACE
print("\nNOW ENTERING... CAMERON'S CRAZY and CONCIEVABLY CRIMINAL CHEMICAL CACHE!!!\n")
while True:
    beginRequest(P1)