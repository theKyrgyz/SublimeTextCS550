import string

userElem = "2H2O2SSe10Bbbbb178Two2J"

def splitter(s):
    # global l,resultList,vPrev,v
    l = list(s)
    v = 0
    resultList = []
    vPrev = 0
    while v < len(l):
        if (s[v] in string.ascii_uppercase) and (v != 0):
            resultList.append(s[vPrev:v])
            vPrev = v
        if v == len(l)-1:
            resultList.append(s[vPrev:v+1])
            vPrev = v
        v += 1
    return resultList

print(splitter(userElem))