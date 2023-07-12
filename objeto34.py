class Alumnos():
    def __init__(self):
        self.nombres=[]
        self.notas=[]

    def cargar_alumnos(self):
        for i in range(1):
             nom=input("ingrese nombre:")
             notas=int(input("ingrese nota:"))
             self.nombres.append(nom)
             self.notas.append(notas)

    def listar_alumno(self):
        print("alumnos listados:",self.nombres)
        print("notas de alumnos:",self.notas)

    def mostrar_alumnos(self):
         for i in range(len(self.nombres)):
              if self.notas[i]>=7:
                   print("alumno con nota mayor a 7:",self.nombres)
                   print("nota:",self.notas)

    def menu_alumnos(self):
         while True:
              print("---menu---")
              print("casilla 1 cargar alumnos")
              print("casilla 2 listar alumnos")
              print("casilla 3 mostrar alumnos con notas mayores a 7")
              print("casilla 4 fin del programa")
              opcion=int(input("ingrese casilla:"))
              if opcion==1:
                   self.cargar_alumnos()
              else:
                   if opcion==2:
                        self.listar_alumno()
                   else:
                        if opcion==3:
                             self.mostrar_alumnos()
                        else:
                             if opcion==4:
                                  print("fin del programa")
                                  break
administrador=Alumnos()
administrador.menu_alumnos()