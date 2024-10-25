from fprint_lib import simbolprint,itemprint

def receipt_print(linelength:int=30, menuItems:list=[], menuItemPrices:list=[], orderedItems:list=[]):
    
    szum:int = 0
    i:int = 0
    
    print("")
    simbolprint(linelength,"*")
    print("*", end="")
    print(" " * (linelength//2-4), end="")
    print("NYUGTA", end="")
    print(" " * (linelength//2-4), end="")
    print("*")
    simbolprint(linelength,"*")
    
    while(i<len(orderedItems)):
        itemprint(linelength, " ", menuItems[orderedItems[i]], menuItemPrices[orderedItems[i]])
        szum += menuItemPrices[orderedItems[i]]
        i+=1

    simbolprint(linelength,"=")

    itemprint(linelength, " ", "Összeg:", szum)
    itemprint(linelength, " ", "Szervízdíj:", szum*0.1)

    simbolprint(linelength,"=")

    itemprint(linelength, " ", "Fizetendő:", szum+szum*0.1)

    simbolprint(linelength,"*")
    print("*", end="")
    print(" " * (linelength//2-4), end="")
    print("NYUGTA", end="")
    print(" " * (linelength//2-4), end="")
    print("*")
    simbolprint(linelength,"*")
