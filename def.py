def lados():
 n=int(input("cantidad de triangulos:"))
 contador_equilatero=0
 contador_isosceles=0
 contador_escaleno=0
 for i in range(n):
    lado1=int(input("ingresar lado 1"))
    lado2=int(input("ingresar lado 2"))
    lado3=int(input("ingresar lado 3"))
 if lado1==lado2==lado3:
    print("el triangulo es:",i+1,",equilatero")
    contador_equilatero+=1
 elif lado1==lado2 or lado1==lado3 or lado2==lado3:
    print("el triangulo es",i+1,"isosceles")
    contador_isosceles+=1
 else:
    contador_escaleno+=1
    print("cantidad de triangulos equilatero:",contador_equilatero+1)
    print("cantidad de triangulos isosceles:",contador_isosceles+1)
    print("cantidad de triangulos escaleno:",contador_escaleno+1)

lados()