# hanoi.py

listA = []
global counter
counter = 0

def moves(n, l):
    global counter
    if n == 0:
        return 
    moves(n-1, not l)
    if l:
        print(str(n)+', left')
        counter += 1
    else:
        print(str(n) +', right')
        counter += 1
    moves(n-1, not l)



for a in range(0,6):
    moves(a, True)
    print(counter)
    counter = 0