#class Persona():
 #   def inicializar(self, nom):
  #      self.nombre= nom
   # def imprimir(self):
    #    print("nombre:",self.nombre)
##objeto 1
#persona1 = Persona()
#persona1.inicializar("eliam")
#persona1.imprimir()
##objeto 2
#persona2 = Persona
#persona2.inicializar("lucas")
#persona2.imprimir()




#class Persona():
 #   def inicializar(self, nom, nota):
  #      self.nombre= nom
   #     self.nota= nota
    #def imprimir(self):
     #   print("nombre:",self.nombre)
      #  print("nota:",self.nota)
#persona1 = Persona()
#persona1.inicializar("eliam", 10)
#persona1.imprimir()        




#class Persona():
 #   def inicializar(self, nom, edad):
  #      self.nombre= nom
   #     self.edad= edad
    #def imprimir(self):
     #   print("nombre:",self.nombre)
      #  print("edad:",self.edad)
    #def año_edad(self):
     #   if self.edad < 4:
      #      print("es menor de edad")
       # else:
        #    print("es mayor de 18")
#persona1 = Persona()
#persona1.inicializar("eliam", 20)
#persona1.imprimir()
#persona1.año_edad()        



#class Triangulos():
#    def inicializador(self):
 #       self.lado1 = int(input("ingrese primer lado:"))
  #      self.lado2 = int(input("ingrese segundo lado:"))
   #     self.lado3 = int(input("ingrese tercer lado:"))
    #def imprimir(self):
     #   print("primer lado:", self.lado1)
      #  print("segundo lado:",self.lado2)
       # print("tercer lado:",self.lado3)

    #def lado_mayor(self):
     #   if self.lado1 >1 and self.lado1 <=20:
      #      print("el lado mayor es:",self.lado1)
       # if self.lado1 >2 and self.lado2 <=4:
        #    print("el lado mayor es:",self.lado2)
        #else:
         #   print("el lado mayor es:",self.lado3)



   # def es_equiliatero(self):
    #    if self.lado1==self.lado2 and self.lado1==self.lado3:
     #       print("el triangulo es equilatero:",self.lado1)
#triangulo = Triangulos()
#triangulo.inicializador()
#triangulo.imprimir()
#triangulo.lado_mayor()
#triangulo.es_equiliatero()



class Matematica():
    
    def __init__(self):
        self.valor1 = int(input("ingrese primer numero:"))
        self.valor2 = int(input("ingrese segundo numero:"))
        self.sum_1()
        self.res_1()
        self.multiplicacion()
        self.division()
    def sum_1(self):
        suma=self.valor1+self.valor2
        print("la suma de los numero es:",suma)
    def res_1(self):
        resta=self.valor1-self.valor2
        print("la resta de los dos numero es:",resta)
    def multiplicacion(self):
        multi=self.valor1*self.valor2
        print("la multiplicacion es:",multi) 
    def division(self):
        promedio=(self.valor1+self.valor2)/2
        print("la division es:",promedio)    
        
numeros = Matematica()