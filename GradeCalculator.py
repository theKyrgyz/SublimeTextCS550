# GradeCalculator.py by Lucas Eggers

# Date: Saturday, September 16, 2018
# Description: A simple grade calculator, taking a command lime argument (float between 0 and 5) and outputting its corresponding letter grade. 
#              Additionally - returns specific error messages if there are a different number of arguments or the number isn't compatible.
# Sources: Huge thanks to Benjamin Cillie who showed me how dictionaries work in Python. I would not have been able to simplify this 
#          code as much as I have without his pointing me in the right direction,
#          namely in the direction of parts of official Python documentation. Lines 25 to 29 are partially his work, largely tweaked by me
#          to fit certain parameters. 

# IMPORTS
import sys
import math as ma

# SIMPLIFYING SYS.ARGV
def commandCall(argNum):
    return sys.argv[int(argNum)]

print("\n")

# IF-THEN STATEMENTS
if len(sys.argv) == 2:
    if 0.0 <= float(commandCall(1)) <= 5.0:
        grade = float(commandCall(1))
        dictionaryThresh = {0.0:"F", 1.0:"D-", 1.5:"D", 2.0:"D+", 2.5:"C-", 2.85:"C", 3.2:"C+", 3.5:"B-", 3.85:"B", 4.2:"B+", 4.5:"A-", 4.7:"A", 4.85:"A+", 5.01:"A+"}
        for element in list(dictionaryThresh):
            if grade <= element:
                print("Congratulations! Your calculated grade is: "+dictionaryThresh[element]+". \n")
                break
    else:
       print("You have provided a number outside the required range. Please try again with a number between 0 and 5, inclusive.")
    quit()
else:
    print("You have provided an unsuitable number of arguments. Please try again with one float number.")
    quit()



