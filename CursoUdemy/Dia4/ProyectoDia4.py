from random import *
print("¡Juego adivinador de numero!")
nombre=input("Introduce tu nombre: ")

print("\n")
print(f"Muy bien {nombre}, el juego es muy simple, tienes 8 intentos para adividar el numero entre 1 y 100.")

respuesta=randint(1,100)
INTENTOS=0
while INTENTOS<8:
    intento = int(input("Introduce un numero: "))
    if intento>101 or intento<0:
        print("Digito no valido joto")
    elif intento>respuesta:
        print("la respuesta es menor.")
        INTENTOS+=1
        continue
    elif intento<respuesta:
        print("la respuesta es mayor.")
        INTENTOS+=1
        continue
    elif intento==respuesta:
        print(f"¡¡Felicidades {nombre} acertaste el numero!!")
        exit()

print("GAME OVER")

    