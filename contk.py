#confeccionar un programa que perimita ingresar
#dos numeros en controles de tipo entry
#luego sumar los dos valores ingresados
#y mostrar la suma en un label al presionar un boton
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()

        self.dato1=tk.StringVar()
        self.dato2=tk.StringVar()
        self.entryTritle=tk.Label(self.ventana1, text="ingrese numero")
        self.entryTritle.grid(column=1, row=0)
        self.ventana=tk.Entry(self.ventana1, width=10, textvariable=self.dato1)
        self.ventana.grid(column=0, row=0)
        self.ventana0=tk.Entry(self.ventana1, width=10, textvariable=self.dato2,)
        self.ventana0.grid(column=0, row=1)
        self.entritilte=tk.Label(self.ventana1,text="ingrese numero")
        self.entritilte.grid(column=1, row=1)

        self.boton1=tk.Button(self.ventana1, text="sumar", command=self.sumar)
        self.boton1.grid(column=0, row=2)

        self.label1=tk.Label(self.ventana1, text="")
        self.label1.grid(column=0, row=3)

        self.ventana1.mainloop()


    def sumar(self):
        valor1=int(self.dato1.get())
        valor2=int(self.dato2.get())
        total= valor1+valor2
        self.ventana1.title(valor1+valor2)
        self.label1.config(text="resultado :" + ""+ str(total))
aplicacion=Aplicacion()

