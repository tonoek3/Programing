from numeros import *

def eleccion():
    print("""""""""""""""""""""""")
    print("     Bienvenido xd     ")
    print("""""""""""""""""""""""")
    
    while True:
        print("Sacar turno en: ")
        print("[1] Perfumes")
        print("[2] Farmacia")
        print("[3] Cosmeticos")
        print("[4] Salir")
        elegir = int(input("Que deseas realizar: "))
        if elegir == 1:
            texto = next(numeros_perfume())
            mensaje(texto)

        elif elegir ==2:
            texto = numeros_farmacia()
            mensaje(texto)

        elif elegir == 3:
            texto = numeros_cosme()
            mensaje(texto)
            
        elif elegir>4 or elegir<1:
            print("Digito no valido\n")
            
        elif elegir == 4:
            print("Gracias por su visita :) ")
            break

eleccion()