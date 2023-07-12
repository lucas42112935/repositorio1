def numero_mayor(v1, v2, v3):
    if (v1 > v2 and v1 > v3):
        print(v1)
    else:
        if (v2>v3):
            print(v2)
        else:
            print(v3)

def ingreso_num():

    valor1= int(input("ingrese un valor:"))
    valor2= int(input("ingrese un valor:"))
    valor3= int(input("ingrese un valor:"))
    numero_mayor(valor1, valor2, valor3)

#bloque
ingreso_num()
