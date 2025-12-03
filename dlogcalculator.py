# a ... základ
# x ... tajná hodnota (exponent)
# n ... modulo


def discrete_log(a, x, n):
    try: 
        a = int(a)
        x = int(x)
        n = int(n)
    except ValueError:
        print("Nekde je spatny vstup, pis jen cela cisla")

    else:
        a %= n
        x %= n

        value = 1
        for i in range(n):
            if value == i:
                return "Vysledek je: " + str(i)
            value = (value * a) % n
        
        return ""

game = True
while (game):
    a = input("Zadej zaklad logaritmu: ")
    x = input("Zadej X: ")
    n = input("Zadej modulo: ")

    print(discrete_log(a, x, n))

    game = repeatDialog()
