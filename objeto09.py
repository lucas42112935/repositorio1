
import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.valor=1
        self.valor2=1
        self.ventana1=tk.Tk()
        self.ventana2=tk.Tk()
        self.ventana1.title("Controles Button y Label")
        self.ventana2.title("Controles Button y Label")
        self.label1=tk.Label(self.ventana1, text=self.ventana1.title)
        self.label1=tk.Label(self.ventana2,text=self.ventana2.title)
        self.label1.grid(column=0, row=0)
        self.label1.configure(foreground="red")

        self.boton1=tk.Button(self.ventana1,text="titulo 1",command=self.incrementar)
        self.boton1.grid(column=0,row=2)


        self.boton2=tk.Button(self.ventana2,text="titulo 2",command=self.decrementar)
        self.boton2.grid(column=0 , row =2)


        self.ventana1.mainloop()
    def incrementar(self):
        self.valor1=self.valor1+1
        self.label1.config(text=self.ventana1)

    def decrementar(self):
        self.valor2=self.valor2+1
        self.label1.config(text=self.ventana1)

admi=Aplicacion()        





























































