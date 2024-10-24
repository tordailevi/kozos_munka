import fprint_lib

menuItems:list=["Palacsinta", "Pörkölt", "Rántotthús", "Húsleves", "Bableves", "Frankfurti leves"]
orderedItems:list=[]
menuItemPrices:list=[800, 2500, 3000, 1500, 1300, 1900]
#printMenu(menuItems)

#getorder(orderedItems, menuItemPrices)







fprint_lib.simbolprint(30, "*")
fprint_lib.itemprint(30, "_", f"{menuItems[0]}", 800)
fprint_lib.simbolprint(30, "=")
fprint_lib.itemprint(30, "_", f"{menuItems[1]}", 2500)
fprint_lib.simbolprint(30, "=")
fprint_lib.itemprint(30, "_", f"{menuItems[2]}", 3000)
fprint_lib.simbolprint(30, "=")
fprint_lib.itemprint(26, "_", f"{menuItems[3]}", 1500)
fprint_lib.simbolprint(30, "=")
fprint_lib.itemprint(26, "_", f"{menuItems[4]}", 1300)
fprint_lib.simbolprint(30, "=")
fprint_lib.itemprint(26, "_", f"{menuItems[5]}", 1900)
fprint_lib.simbolprint(30, "*")