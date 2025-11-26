from libs import repeatDialog
from libs.discreteLog import discrete_log




game = True
while (game):
    a = input("Zadej zaklad logaritmu: ")
    x = input("Zadej X: ")
    n = input("Zadej modulo: ")

    print(discrete_log(a, x, n))

    game = repeatDialog()
