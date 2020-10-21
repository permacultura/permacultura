
rendimientos={}
f = open("rendimientos.txt", "r")
for x in f:
    a=x.split(",")
    rendimientos[a[0]]=a[1]
class Ingrediente():
    def __init__(self,nombre,cantidad):
        self.nombre=nombre
        self.cantidad=cantidad

class Receta(Ingrediente):
    def __init__(self,nombre,Ingrediente,wh,aceite,vecesSemana):
        self.Ingrediente=Ingrediente
        self.nombre=nombre
        self.wh=wh
        self.aceite=aceite
        self.vecesSemana=vecesSemana

class Comidas(Receta):
    def m2PorIngrediente():
        return "x"
    def gastoAceite():
        return "aceite"
    def gastoElectricidad():
        return "wh"

I1 = Ingrediente("tomate", "0.2")
print (I1.cantidad)
