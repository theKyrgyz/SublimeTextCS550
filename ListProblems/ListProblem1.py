# ListProblem1.py

# produces 10 numbers, between 1 and 100, ordered by size

import random as ra
TheList = []
def doIt():
    a = ra.randint(1,100)
    if ((a%3) == 0) or (a in TheList):
        doIt()
    else:
        TheList.append(a)
        return
for i in range(0,9):
    doIt()
TheList.sort()
print(*TheList)