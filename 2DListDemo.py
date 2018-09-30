# 2DListDemo.py

i = [[1,2,3],[4,5,6],[7,8,9]]

print(i[0]) # <--- returns a list
print(i[1][0]) # <---- returns a number, here, 4

i = []
for k in range(10):
    i.append(0)

print(i)

i = [0]*10 # <---- SAME AS THE FOR LOOP ABOVE. Good for doing repetetive appends.
print(i)

i = [[0]*10 for x in range(10)] # <----  10x10 grid
print(i, sep="\n")

for x in range(10):
    k = [0]*10
    i.append(k)