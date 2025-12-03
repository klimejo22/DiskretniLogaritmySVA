# g ... základ
# x ... tajná hodnota (exponent)
# n ... modulo

game = True
while game:
    try:
        g = int(input("Zadej spolecny zaklad: "))
        x = int(input("Zadej tajnou hodnotu: "))
        n = int(input("Zadej spolecne modulo: "))

        # rychlá modulární exponenciace
        r = pow(g, x, n)
        
        print("Vysledek je: ", r)

    except ValueError:
        print("Nekde je spatny vstup, pis jen cela cisla")

    if (input("Pro pokracovani 1: ") == "2"):
        game = False
