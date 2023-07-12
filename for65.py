def inicio():
    print("***********************")

def carga_suma():
    valor1=int(input("ingrese primer valor:"))
    valor2=int(input("ingrese segundo valor:"))
    suma=valor1+valor2
    print("el valor ingresado es")

def finalizacion():
    print("**********************")

def separador():
    print("_______________________________________")
    
#programa principal

inicio()
for i in range(5):
    carga_suma()
    separador()   
finalizacion()