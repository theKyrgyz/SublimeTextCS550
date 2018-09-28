# ListProblem2.py
# Used official Python data structure documentation for this one: https://docs.python.org/3.7/tutorial/datastructures.html

# Prints the numbers one through one hundred, ordered randomly (shuffled)

import random as ra
thatList = [x for x in range(1,101)]
ra.shuffle(thatList)
print(*thatList[:20],"\n",*thatList[20:40],"\n",*thatList[40:60],"\n",*thatList[60:80],"\n",*thatList[80:],"\n",)

