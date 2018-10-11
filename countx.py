userinput = input("\nMr. X. Avier demands you input a string! Best not to anger him.\n> ")
XList = ["x","X"]
global count
count = 0
def countx(n):
    global count
    if type(n) == str:
        n = list(n)
    if len(n) > 0:
        if n.pop(0) in XList:
            count += 1
        countx(n)
    else:
        print("\n"+str(count)+"\n")
countx(userinput)