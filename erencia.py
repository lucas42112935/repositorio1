#class Persona():
    #def __init__(self):
     #   self.nombre=input("ingrese nombre:")
    #    self.edad=int(input("ingrese edad:"))

   # def imprimir(self):
  #      print("nombre:",self.nombre)
 #       print("edad:",self.edad)


#class Empleado(Persona):
    #def __init__(self):
        #super().__init__()
       # self.sueldo=float(input("ingrese sueldo:"))
      #  self.imprimir()
     #   self.verificar()

    #def imprimir(self):
   #     super().imprimir()
  #      print("sueldo:",self.sueldo)

 #   def verificar(self):
       # if self.sueldo>300000:
           # print("paga impuesto",self.sueldo)

#admi=Empleado()

#class Operaciones():
 #   def __init__(self):
        #class Persona():
    #def __init__(self):
     #   self.nombre=input("ingrese nombre:")
    #    self.edad=int(input("ingrese edad:"))

   # def imprimir(self):
  #      print("nombre:",self.nombre)
 #       print("edad:",self.edad)


#class Empleado(Persona):
    #def __init__(self):
        #super().__init__()
       # self.sueldo=float(input("ingrese sueldo:"))
      #  self.imprimir()
     #   self.verificar()

    #def imprimir(self):
   #     super().imprimir()
  #      print("sueldo:",self.sueldo)

 #   def verificar(self):
       # if self.sueldo>300000:
           # print("paga impuesto",self.sueldo)

#admi=Empleado()


class Operaciones():

    def __init__(self):
        self.v1 = 0
        self.v2 = 0
        self.total= 0

    def carga1(self):
        self.v1=int(input("ingrese numero:"))

    def carga2(self):
        self.v2=int(input("ingrese numero:"))

    def resultado1(self):
        print("resultado:",self.total)
    

    def operar(self):
        pass

class Sum(Operaciones):
    def operar(self):
        self.total=self.v1+self.v2


class Resta(Operaciones):
    def operar(self):
        self.total=self.v1-self.v2

admi=Sum()
admi.carga1()
admi.carga2()
admi.operar()
admi.resultado1()

admi=Resta()
admi.carga1()
admi.carga2()
admi.operar()
admi.resultado1()