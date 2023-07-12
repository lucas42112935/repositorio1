def cantidad():

 for i in range(n):
    n=int(input("cantidad de triangulos:"))
    lado1=int(input("ingrese primer lado:"))
    lado2=int(input("ingrese segund olado:"))
    lado3=int(input("ingrese tercer lado:"))
    triangulos(lado1==lado2==lado3)
def triangulos():
    if lado1==lado2==lado3:
        print("triangulo equilatero")
        equilatero+=1
    elif lado1==lado2 or lado1==lado3 or lado2==lado3:
        print("triangulo isosceles")
    isosceles+=1
    equilatero=0
    isosceles=0
    escaleno=0
contador_equilatero=0
contador_isosceles=0
contador_escaleno=0

print("cantidad de triangulos equilatero",contador_equilatero)
print("cantidad de triangulos isosceles",contador_isosceles)
print("cantidad de triangulos escalenos",contador_escaleno)

triangulos()
cantidad()