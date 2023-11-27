class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("pio, mi color es {}".format(self.color))
    
    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()


    def pintar_negro(self):
        self.color = "black"
        print(f"ahora el pajaro es {self.color}")

    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = 21
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print("joto")



piolin = Pajaro("marron", "domestico")
piolin.mirar()

