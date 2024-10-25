from fprint_lib import simbolprint,itemprint,header_print

def menu_print(linelength:int=30, menuItems:list=[],menuItemPrices:list=[]):

    print()
    header_print(linelength, "MENÜ")

    simbolprint(linelength, "_")

    i:int = 0
    while(i<len(menuItems)):
        itemprint(linelength, ".", f"{menuItems[i]}", menuItemPrices[i], True)
        if(i<len(menuItems)-1):
            simbolprint(linelength, "=", True)
        i+=1
    
    simbolprint(linelength, "_", True)
    print()