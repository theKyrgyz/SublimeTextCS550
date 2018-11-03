# finalproject.py

""" Compose  a  data  type  Element  for  entries  in  the  periodic  table  of 
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
Include  fields  for element, atomic  number,  
symbol,  and  atomic  weight.
"""



import element
from element import Element
import csv

element.importTest()

elementList = []

class PeriodicTable:
    kind = 'periodic table'
    def __init__(self, inputFile):
        self.inputFile = inputFile
        self.create()
        self.FL = elementList

    def create(self):
        with open(self.inputFile, newline='') as csvfile:
            elementreaderA = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in elementreaderA:
                # print(', '.join(row))
                ATS = ', '.join(row)
                # ATS stands for Attributes to Separate. It's a single element row's attributes, which will then be separated and put inside an Element object.
                ATS = ATS.split(',')
                # print(ATS)
                elementList.append(Element(ATS[0],ATS[1],ATS[2],ATS[3]))

    def printEntireTable(self):
        if elementList == []:
            print("This table empty, yeet.")
        else:
            for i in elementList:
                if i != None:
                    i.show()
            print("\n")

P1 = PeriodicTable("elements.csv")
# P1.printEntireTable()

