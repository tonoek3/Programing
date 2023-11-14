from random import*

palabras=["paraguas","mazatlan","perpendicular","parangaricutirimicuaro"]
letras_correctas=[]
letras_incorrectas=[]
intentos=6
aciertos=0
juego_terminado=False

#elegir palabra
def palabra(palabras):
    return choice(palabras)

#pedir letra
def pedir_letra():
    letra_elegida=""
    es_valida=False
    abecedario="abcdefghijklmnopqrstuvwxyz"
    
    while not es_valida:
        letra_elegida= input("Introduce una letra: ")
        if letra_elegida in abecedario and len(letra_elegida)==1:
            es_valida=True
        else:
            print("Digita un valor valido.")

print(palabra(palabras))

pedir_letra()
