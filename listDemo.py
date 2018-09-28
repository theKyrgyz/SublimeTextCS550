# listDemo.py
# empty list
a = []

print(a)

a.append(5)
a.append(3)
a.append(8)
a.append(8)

print(a)

# ADDING STUFF MORE EFFICIENTLY
a += [1,2,3,4,5]

# will return [5, 3, 8, 8, 1, 2, 3, 4, 5]

a.insert(0,7)

print(a)

# a way to insert multiple values at the left-most point:

a = [1,2,3,4,5] + a

if a.pop() == 5:
    # every time this if statement is checked/run, pop() will delete stuff from the list. this is UNSAFE.

# SWAPPING VARS EASILY

y,z = 5,10
y,z = z,y