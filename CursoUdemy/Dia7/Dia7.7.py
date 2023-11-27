class Padre:
    def hablar(self):
        print("hola")

class Madre:
    def hablar(self):
        print("Puto")

    def reir(self):
        print("Ja Ja")

class Hijo(Madre,Padre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.hablar()