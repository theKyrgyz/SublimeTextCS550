# ListProblem4.py

# For a list with random values, if any value in the list is divisible by the first value in the list, delete that value.

i = 0
k = 48
fibList = [1,1]
oddList = [1,1]
while k > i:
    c = fibList[-1] + fibList[-2]
    fibList.append(c)
    if c%2 != 0:
        oddList.append(c)
        i = i+1
print(*oddList[:10],"\n",*oddList[10:20],"\n",*oddList[20:30],"\n",*oddList[30:35],"\n",*oddList[35:40],"\n",*oddList[40:45],"\n",*oddList[45:],"\n")


