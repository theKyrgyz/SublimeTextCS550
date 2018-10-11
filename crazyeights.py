userinput = input("\nYour classmate Ai Tuh demands you input a string! Best not to anger her.\n> ")
def reset():
    global count
    count = 0
    global spot
    spot = -1
def crazy_eights(n):
    global count
    global spot
    spot += 1
    if spot < len(n):
        if spot != 0:
            if n[spot] == v:
                count += 1
                if n[spot-1] == v:
                    count += 1
        else:
            if n[spot] == v:
                count += 1
        crazy_eights(n)
    else:
        print("\n"+str(count)+"\n")
reset()
v = "8"
crazy_eights(list(userinput))