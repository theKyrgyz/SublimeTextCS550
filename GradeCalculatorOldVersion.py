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
        dictionaryThresh = {0.0:"F", 1.0:"D-", 1.5:"D", 2.0:"D+", 2.5:"C-", 2.85:"C", 3.2:"C+", 3.5:"B-", 3.85:"B", 4.2:"B+", 4.5:"A-", 4.7:"A", 4.85:"A+", 5.01}
        print("dictionaryThresh Length: ",str(len(dictionaryThresh)))
        for element in list(dictionaryThresh):
        if grade >= element:
            print("Your grade: " + dictionaryThresh[element])
            stop()
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



