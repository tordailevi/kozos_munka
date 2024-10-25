
def simbolprint(linelength:int=30, symbol:str=" ", border:bool=False):
    if(border == False):
        print(symbol*linelength)
    else:
        print(f"|{(symbol)*(linelength-2)}|")

def itemprint(linelength:int=30, symbol:str=" ", itemName:str="", itemPrice:int=0, border:bool=False):
    itemPriceText = f"{itemPrice}"
    if(border == False):
        print(f"{itemName}{(symbol)*(linelength-(len(itemName)+len(itemPriceText)+2))}{itemPrice}Ft")
    else:
        print(f"|{itemName}{(symbol)*(linelength-(len(itemName)+len(itemPriceText)+4))}{itemPrice}Ft|")

def header_print(linelength:int=30, text:str=""):
    simbolprint(linelength,"*")
    print("*", end="")
    print(" " * (linelength//2-(len(text)//2+1)), end="")
    print(text, end="")
    print(" " * (linelength//2-(len(text)//2+1)), end="")
    print("*")
    simbolprint(linelength,"*")