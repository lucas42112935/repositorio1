cantidad = 0
n = int(input("ingrese cantidad de valores"))
for x in range (n):
    valor = int(input("ingrese valor:"))
    if valor >= 1000:
        cantidad = cantidad +1
print("cantidad de valores mayores a mil:", cantidad)