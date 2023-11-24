def ejemplo1():
    class Casa:
        def __init__(self,color,cantidad_pisos):
            self.color = color 
            self.cantidad_pisos = cantidad_pisos

    casa_blanca = Casa("blanco",4)

    print(casa_blanca.color,casa_blanca.cantidad_pisos)

def ejemplo2():
    class Cubo:
        caras = 6

        def __init__(self,color):
            self.color = color

    cubo_rojo = Cubo("rojo")

    print(cubo_rojo.color, cubo_rojo.caras)        


class Personaje:
    real = False

    def __init__(self,especie,magico,edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry = Personaje("Humano",True,17)

print(f"Tu personaje es real = {harry.real}, es de especie: {harry.especie}, es magico = {harry.magico} y tiene la edad de {harry.edad} años")


