n = int(input("cuantos triangulos procesara"))
cantidad = 0
for x in range(n):
    altura =int(input("ingrese altura"))
    base = int(input("ingrese base"))
    superficie=altura*base/2
    print("la superficie es")
    print(superficie)
    if superficie>12:
        cantidad=cantidad+1
print("superficie superior a 12 son:", cantidad)
