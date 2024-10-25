def get_order(orderedItems:list, menuItems:list):
    a:int=1
    while a !=0:
        c:int=0
        try:
            a:int=int(input("Kérem adja meg a választott étel sorszámát! (ha már nem szeretne rendelni, írjon be 0-át): "))
            if ((a == 0) or (6 < a) or (0 > a)):
                continue
            else:
                b:int=int(input("Kérem adja meg, hogy a megadott ételből hány tételt szeretne rendelni!: "))
            while b-1 >= c:
                orderedItems.append(a-1)
                c+=1
        except ValueError:
            print("Hiba, kérem számadatot adjon meg adjon meg!")
    return(orderedItems)

            
        
