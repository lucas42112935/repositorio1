lista = [10,20,30,150,1000,6000,101,250]
cantidad=0
x=0
while x<len(lista):
     if len(lista[x])>100:
        cantidad=cantidad+1
     x=x+1
print("valores de la lista:",lista)
print("valores maximo a 100:",cantidad)