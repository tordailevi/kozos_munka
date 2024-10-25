from fprint_lib import simbolprint,itemprint,header_print

def receipt_print(linelength:int=30, menuItems:list=[], menuItemPrices:list=[], orderedItems:list=[]):
    
    szum:int = 0
    i:int = 0
    
    print("")
    header_print(linelength, "NYUGTA")
    
    while(i<len(orderedItems)):
        itemprint(linelength, " ", menuItems[orderedItems[i]], menuItemPrices[orderedItems[i]])
        szum += menuItemPrices[orderedItems[i]]
        i+=1

    simbolprint(linelength,"=")

    itemprint(linelength, " ", "Összeg:", szum)
    itemprint(linelength, " ", "Szervízdíj:", szum*0.1)

    simbolprint(linelength,"=")

    itemprint(linelength, " ", "Fizetendő:", szum+szum*0.1)

    header_print(linelength, "NYUGTA")
