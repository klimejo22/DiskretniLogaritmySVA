# g ... základ
# x ... tajná hodnota (exponent)
# n ... modulo

g = int(input("Zadej spolecny zaklad: "))
x = int(input("Zadej tajnou hodnotu: "))
n = int(input("Zadej spolecne modulo: "))

# rychlá modulární exponenciace
r = pow(g, x, n)

print("Vrsledek je: ", r)
