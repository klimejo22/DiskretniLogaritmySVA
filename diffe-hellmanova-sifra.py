# g ... základ
# x ... tajná hodnota (exponent)
# n ... modulo

from libs import repeatDialog


game = True
while game:
    g = int(input("Zadej spolecny zaklad: "))
    x = int(input("Zadej tajnou hodnotu: "))
    n = int(input("Zadej spolecne modulo: "))

    # rychlá modulární exponenciace
    r = pow(g, x, n)

    print("Vysledek je: ", r)

    game = repeatDialog()
