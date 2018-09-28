# ListProblem3.py
# This is the one my group came up with. Don't judge it, skip to number 4.

x = 1
y = 101
urList = []
for i in range(x,y):
    if (i%6 != 0) and ((i%2 == 0) or (i%3 == 0)):
        urList.append(i)
print(*urList[:20],"\n",*urList[20:40],"\n",*urList[40:])

