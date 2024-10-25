from menu_print import menu_print
from getorder import get_order
from receipt_print import receipt_print

menuItems:list=["1) Palacsinta", "2) Pörkölt", "3) Rántotthús", "4) Húsleves", "5) Bableves", "6) Frankfurti leves"]
orderedItems:list=[]
menuItemPrices:list=[800, 2500, 3000, 1500, 1300, 1900]

menu_print(30,menuItems,menuItemPrices)

get_order(orderedItems)

receipt_print(30, menuItems, menuItemPrices, orderedItems)