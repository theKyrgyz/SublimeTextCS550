# weather.py

import sys
import math as ma

def commandCall(argNum):
	return sys.argv[int(argNum)]

if input("Is it raining outside? y/n ") == "y":
	print("Be sure to bring an umbrella! :)")
else:
	print("Too bad. If it is, make sure to respond with the letter y.")
