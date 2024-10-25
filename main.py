import fprint_lib
from getorder import get_order
from receipt_print import receipt_print

menuItems:list=["1) Palacsinta", "2) Pörkölt", "3) Rántotthús", "4) Húsleves", "5) Bableves", "6) Frankfurti leves"]
orderedItems:list=[]
menuItemPrices:list=[800, 2500, 3000, 1500, 1300, 1900]


fprint_lib.lec("Étlap", 30, "*")
fprint_lib.itemprint(30, ".", f"{menuItems[0]}", 800, "*")
fprint_lib.simbolprint(30, "=", "*")
fprint_lib.itemprint(30, ".", f"{menuItems[1]}", 2500, "*")
fprint_lib.simbolprint(30, "=", "*")
fprint_lib.itemprint(30, ".", f"{menuItems[2]}", 3000, "*")
fprint_lib.simbolprint(30, "=", "*")
fprint_lib.itemprint(30, ".", f"{menuItems[3]}", 1500, "*")
fprint_lib.simbolprint(30, "=", "*")
fprint_lib.itemprint(30, ".", f"{menuItems[4]}", 1300, "*")
fprint_lib.simbolprint(30, "=", "*")
fprint_lib.itemprint(30, ".", f"{menuItems[5]}", 1900, "*")
fprint_lib.simbolprint(30, "-", "*")
fprint_lib.simbolprint(30, "*", "*")

get_order(orderedItems)

receipt_print(30, menuItems, menuItemPrices, orderedItems)