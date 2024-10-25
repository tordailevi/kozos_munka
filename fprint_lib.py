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

def itemprint(linelength:int=10, symbol:str=" ", itemName:str="", itemPrice:int=0, border:bool=True):
    itemPriceText = f"{itemPrice}"
    if(border == False):
        print(f"{itemName}{(symbol)*(linelength-(len(itemName)+len(itemPriceText)+2))}{itemPrice}Ft")
    else:
        print(f"|{itemName}{(symbol)*(linelength-(len(itemName)+len(itemPriceText)+4))}{itemPrice}Ft|")


def jelek(jel:str, hanyszor:int=1):
    print(jel*hanyszor)

def nyugta_kiiras(szo:str = "",hossz:int=24, jel:str="*",):
    hossz=hossz-2
    szo=szo.upper()
    print(f"{jel}{szo:^{hossz}}{jel}" )
def lec(szo:str="",hossz:int=24,jel:str="*"):
    jelek(jel,hossz)
    nyugta_kiiras(szo,hossz,jel)
    jelek(jel,hossz)

def tetelkiiras(tetel:str="", t1:float=0, hossz:int=24):
    hossz=hossz-len(tetel)
    print(f"{tetel}{t1:>{hossz}}")