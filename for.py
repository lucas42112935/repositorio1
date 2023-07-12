multi3 = 3
multi5 = 5

for x in range (10):
    valor = int(input("ingrese los valores"))
    if valor %3 ==0:
        multi3 = multi3 + 1
    if valor %5 ==0:
        multi5 = multi5 + 1
        # concatenador.
print("multiplos de tres:", multi3)
print("multiplos de cinco:", multi5)