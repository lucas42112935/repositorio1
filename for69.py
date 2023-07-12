def inicio(mensaje):
    print(mensaje)




def triangulos_n(v1, v2, v3):
    if (v1 ==3):
        print("equilatero")
    else:
        if (v2 ==2):
            print("isosceles")
        else:
            print(v3)
            print("escaleno")

def ingres_valor():
    valor1=int(input("ingresar valor"))
    valor2=int(input("ingresar valor"))
    valor3=int(input("ingresar valor"))
    triangulos_n(valor1, valor2, valor3)

def finalizacion(mensaje1):
    print(mensaje1)


inicio("inicio del programa")
ingres_valor()
finalizacion("final del programa")
