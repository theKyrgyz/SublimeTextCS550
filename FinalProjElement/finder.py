# finder.py

def beginRequest(p):
    choice = input("What would you like to do in the wonderful world of chemistry today?\nF  Find an element by name, number, or symbol.\nW  Find an element by atomic weight [precision required].\nM  Find the weight of a molecule. [COOL FEATURE!]\nQ  Quit.\n\n>> ")
    if choice == "F":
        i = input("\nPlease input the number, name, or symbol of the element you wish to find.\n>> ")
        try:
            int(i)
            p.ElemByNumber(i)
        except ValueError:
            if len(i) < 3:
                p.ElemBySymbol(i)
            else:
                p.ElemByName(i)
        print("\n")
    elif choice == "W":
        i = input("\nPlease input the weight of the element you wish to find. \nNote: must be exactly what is on file.\n>> ")
        try:
            float(i)
            p.ElemByWeight(i)
        except ValueError:
            print("\n")
    elif choice.upper() == "M":
        i = input("\nPlease input the chemical formula of the molecule \nwhose molecular weight you want to find.\n>> ")
        print("\nThe weight of this molecule,",i,", is:",round(p.WeightMolec(splitter(i)), 4),"\n")
    elif choice.upper() == "Q":
        print("\n")
        quit()
    else:
        print("I don't understand.\n")