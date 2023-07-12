class Cuenta():
    def __init__(self,nombre,monto):
        self.nombre=nombre
        self.monto=monto
class CajaAhorro(Cuenta):
    def __init__(self,nombre,monto):
        super().__init__(nombre,monto)
        print("titular de la cuenta",self.nombre)
        print("dinero de la cuenta",self.monto)
class PlazoFijo(Cuenta):
    def __init__(self,nombre,monto):
        super().__init__(nombre,monto)
        self.montop=(self.monto*7)/100
        print("titular de la cuenta",self.nombre)
        print("el plazo fijo mensual es 7% mensual",self.montop)
admi=CajaAhorro("lucas",100000)

admi=PlazoFijo("lucas",100000)