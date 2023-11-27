class Animal:
    def __init__(self,edad, color):
        self.edad = edad
        self.color = color 

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")


class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        self.edad = edad
        self.color = color
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("pio")
    
    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")


piolin = Pajaro(3, "rojo", 30)
mi_animal = Animal(4,"negro")


piolin.volar(40)
mi_animal.nacer()
