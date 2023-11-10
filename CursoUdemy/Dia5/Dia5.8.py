from random import*

# lista inicial
palitos=["-","--","---","----"]

# mezclar palitos 
def mezclar(lista):
    shuffle(lista)
    return lista


# pedirle intento
def probar_suerte():
    intento=""
    while intento not in ["1","2","3","4"]:
        intento = input("Elige un numero del 1 al 4: ")
    
    return int(intento)


# comprobar el intento
def chequear_intento(lista,intento):
    if lista [intento - 1] =="-":
        print("A lavar los platos")
    else:
        print("te salvaste perro")
    
    print(f"te ha tocado{lista[intento-1]}")


palitoss_mezclados = mezclar(palitos)
seleccion = probar_suerte()
resultado=chequear_intento(palitoss_mezclados,seleccion)

