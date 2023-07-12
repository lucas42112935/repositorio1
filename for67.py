def inicio(mensaje):
    print(mensaje)
    print("***************************")


def valores_enteros():
    valor1=int(input("ingrese primer valor"))
    valor2=int(input("ingrese segundo valor"))
    valor3=int(input("ingrese tercer valor"))

    if valor1>valor2:
        print("el numero mayor es",valor1)
    
    if valor2>valor3:
        print("el numero mayor es",valor2)
    if valor2<valor1:
        print("el numero menor es",valor2)

def finalizacion(mensaje1):
    print(mensaje1)
    print("*****************************")
# bloque
inicio("hola mundo")
for i in range(5):
    valores_enteros()
finalizacion("fin del mundo")