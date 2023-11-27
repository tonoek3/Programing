class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + "dice muuu")

class Obeja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + "dice beee")


mi_vaca =  Vaca("ayuwoki")
mi_obeja = Obeja("perrilla")

def hablar_animal(animal):
    animal.hablar()


hablar_animal(mi_obeja)
