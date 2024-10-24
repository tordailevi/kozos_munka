# what is the length of the line
# what simbol should be printed in the line
# should there be a border?

def simbolprint(linelength:int=10, symbol:str=" ", border:bool=False):
    if(border == False):
        print(symbol*linelength)
    else:
        print(f"|{(symbol)*(linelength-2)}|")



# what is the length of the line
# what simbol should be printed in the line
# name of the item
# price of the item
# should there be a border?

def itemprint(linelength:int=10, symbol:str=" ", itemName:str="", itemPrice:int=0, border:bool=False):
    if(border == False):
        print(f"{itemName}{(symbol)*(linelength-(len(itemName)+len({itemPrice})+2))}{itemPrice}Ft")
    else:
        print(f"|{itemName}{(symbol)*(linelength-(len(itemName)+len({itemPrice})+4))}{itemPrice}Ft|")