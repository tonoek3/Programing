class Animal:
    def __init__(self,crecer, reproducir, morir):
        self.crecer = crecer
        self.reproducir = reproducir
        self.morir = morir
        
        

    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass


piolin = Pajaro("10 semanas","3 hijos","2 anios")

print(piolin.morir)
