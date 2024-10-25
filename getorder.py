def get_order(orderedItems:list):
    itemNumber:int=1
    while itemNumber !=0:
        i:int=0
        try:
            itemNumber:int=int(input("Kérem adja meg a választott étel sorszámát! (ha már nem szeretne rendelni, írjon be 0-át): "))
            if ((itemNumber == 0) or (6 < itemNumber) or (0 > itemNumber)):
                continue
            else:
                itemAmount:int=int(input("Kérem adja meg, hogy a megadott ételből hány tételt szeretne rendelni!: "))
            while itemAmount-1 >= i:
                orderedItems.append(itemNumber-1)
                i+=1
        except ValueError:
            print("Hiba, kérem számadatot adjon meg adjon meg!")
