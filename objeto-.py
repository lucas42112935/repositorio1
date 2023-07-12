#crear una clase que administre una agenda personal 
#se debe almacenar el nombre de la persona , telefono y mail
#debe mostrar un menu con las siguientes opciones 
#1-carga de un contacto en la agenda
#2-listado completo de la agenda 
#3- consulta ingresando el nombre de la persona
#4-modificacion de su telefono y mail
#finalizar programa


class Agenda():


    def __init__(self):
        self.nombre=[]
        self.mail=[]
        self.telefono=[]

    def agenda_12(self):
        for i in range(1):
            n=input("ingrese nombre:")
            t=int(input("ingrese telefono:"))
            e=input("ingrese correo:")
            self.nombre.append(n)
            self.mail.append(e)
            self.telefono.append(t)

    def consulta_1(self):
        for i in range(len(self.nombre)):
            print("consulta de usuario")
            consulta=input("ingrese nombre:")
            if self.nombre[i]==consulta:
                print(self.nombre[i])
                print(self.telefono[i])
                print(self.mail[i])



    def modificador_1(self):
        print("modificar datos")
        modificar=input("ingrese nombre a modificar")
        for i in range(len(self.nombre)):
            if self.nombre==modificar:
                self.nombre[i]=input("ingrese nuevo nombre")
                self.telefono[i]=int(input("ingrese nuevo telefono"))
                self.mail[i]=input("ingrese nuevo mail")
                print(self.nombre[i],self.telefono[i],self.mail[i])



    def listado_1(self):
        print("listado de la agenda completo")
        print("nombre:",self.nombre)
        print("telefono:",self.telefono)
        print("email:",self.mail)

    def menu_1(self):
        while True:
            print("casilla 1 carga un contacto en la agenda")
            print("casilla 2 listado completo de la agenda")
            print("casilla 3 consulta ingresando el nombre de la persona")
            print("casilla 4 modificacion de su telefono y email")
            print("casilla 5 fin del programa")

            opcion=int(input("ingrese casilla:"))

            if opcion==1:
                self.agenda_12()
            else:
                if opcion==2:
                    self.listado_1()
                else:
                    if opcion==3:
                        self.consulta_1()
                    else:
                        if opcion==4:
                            self.modificador_1()
                        else:
                            if opcion==5:
                                print("fin del programa")
                                break


administrador=Agenda()
administrador.menu_1()