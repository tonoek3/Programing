#Recetario 
from pathlib import Path
from os import system
import glob

ruta_recetario = Path(Path.home(),"Recetas")

def contar_recetas(ruta_recetario):
    contador = 0
    for txt in Path(ruta_recetario).glob("**/*.txt"):
        contador += 1
    return contador

def inicio ():
    system("cls")
    print("*"*50) 
    print("\t    Recetario de recetas xd") 
    print("*"*50)
    nombre = input("Cual es tu nombre: ")
    system("cls")
    print(f"Hola {nombre} bienvenido al recetario\n")
    print(f"La ruta del recetario es {ruta_recetario}")
    print(f"Existen {contar_recetas(ruta_recetario)} recetas en el recetario")

    eleccion = "x"

    while not eleccion.isnumeric() or int(eleccion) not in range(1,7):
        print("Elige una opcion")
        print("""
        [1] Leer receta
        [2] Crear receta
        [3] Crear categoria
        [4] Eliminar receta
        [5] Eliminar categoria
        [6] Finalizar programa""")
        eleccion = input("- ")
    return eleccion

def mostrar_categorias(ruta_recetario):
    print("Categorias")
    ruta_categorias = Path(ruta_recetario)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1

    return lista_categorias
    
mostrar_categorias(ruta_recetario)




opcion = 0
fin = False

if opcion == 1:
    #Mostrar categorias 
    #Elegir categoria
    #Mostrar recetas
    #Elegir receta
    #Leer receta
    #Regresar al inicio
    pass
elif opcion == 2:
    #Mostrar categorias
    #Elegir categoria
    #Escribir receta nueva
    #Crear receta
    #Regresar al inicio
    pass 
elif opcion == 3:
    #Crear categoria 
    #Generar categoria
    #Regresar al inicio
    pass
elif opcion == 4:
    #Mostrar categorias
    #Elegir categoria
    #Mostrar recetas
    #Elegir receta
    #Eliminar receta
    #Regresar al inicio
    pass
elif opcion == 5:
    #Mostrar categorias
    #Elegir categoria
    #Eliminar categoria
    #Regresar al inicio
    pass
elif opcion == 6:
    #Finalizar proceso
    pass





