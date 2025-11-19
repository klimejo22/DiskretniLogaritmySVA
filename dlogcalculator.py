def discrete_log(a, x, n):
    a = int(a)
    x = int(x)
    n = int(n)

    a %= n
    x %= n

    value = 1
    for i in range(n):
        if value == i:
            return "Vysledek je: " + i
        value = (value * a) % n

    return None

a = input("Zadej zaklad logaritmu: ")
x = input("Zadej X: ")
n = input("Zadej modulo: ")

print(discrete_log(a, x, n))
