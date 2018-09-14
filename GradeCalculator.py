# GradeCalculator.py

# Date:
# Description:
# Sources:

import sys
import math as ma

# SIMPLIFYING SYS.ARGV
def commandCall(argNum):
    return sys.argv[int(argNum)]

# WHEN THE CORRECT THRESHHOLD IS MET, i.e. the FINISHING SECTION
def finished():
    listLetters = ["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"]
    print("Your letter grade is "+str(listLetters[listSpot])+".")
    print("Diagnostics: listSpot is "+str(listSpot)+". threshVal is "+str(threshVal)+".")

# IF-THEN STATEMENTS
if len(sys.argv) == 2:
    if 0.0 <= float(commandCall(1)) <= 5.0:
       grade = float(commandCall(1))
       print("Grade as a float: ",str(grade))
       listThresh = [0.0, 1.0, 1.5, 2.0, 2.5, 2.85, 3.2, 3.5, 3.85, 4.2, 4.5, 4.7, 4.85, 5.01]
       print("ListThresh Length: ",str(len(listThresh)))
       listSpot = 1
       checking = True
       cycles = 0
       while (checking and (cycles < 25)):
         threshVal = float(listThresh[listSpot])
         if threshVal <= grade:
            checking = True
            listSpot = listSpot + 1
            cycles = cycles + 1
         else:
            print("Stopping list at spot "+str(listSpot)+".")
            checking = False
            listSpot = listSpot - 1
            finished()
           

    else:
       print("You have provided a number outside the required range. Please try again with a number between 0 and 5, inclusive.")
    quit()
else:
    print("You have provided an unsuitable number of arguments. Please try again with one float number.")
    quit()



