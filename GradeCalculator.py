# GradeCalculator.py

# Date:
# Description:
# Sources:

import sys
import math as ma

def commandCall(argNum):
	return sys.argv[int(argNum)]

if len(sys.argv) == 2:
	if 0.0 <= float(commandCall(1)) <= 5.0:
		grade = float(commandCall(1))
		print("Grade as a float: ",str(grade))

		listThresh = [0.0, 1.0, 1.5, 2.0, 2.5, 2.85, 3.2, 3.5, 3.85, 4.2, 4.5, 4.7, 4.85, 5.1]
		print("ListThresh Length: ",str(len(listThresh)))

		listSpot = 1
		checking = True
		while checking:
			threshVal = float(listThresh[listSpot])
			if threshVal >= grade:
    			print ("Stopping list at spot ", str(listSpot))
    			checking = False
			else:
    			print("Running through list again.")
    			checking = True
    			listSpot = listSpot + 1


		print("It was ", listLetters[VALUE], " on that day.")








	else:
		print("You have provided a number outside the required range. Please try again with a number.")
	quit()
else:
	print("You have provided an unsuitable number of arguments. Please try again with one float number.")
	quit()
