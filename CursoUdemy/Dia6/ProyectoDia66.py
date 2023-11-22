#Recetario 
from pathlib import Path
from os import system
import glob
import os

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
        eleccion = input()
    return int(eleccion)

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
    
def elegir_categoria(lista_categoria):
    eleccion_correcta = "x"

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista_categoria) + 1):
        eleccion_correcta = input("\nElije una categoria: ")
    return lista_categoria[int(eleccion_correcta) - 1]

def mostrar_recetas(mi_categoria):
    print("Recetas: ")
    ruta_recetas = Path(mi_categoria)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob("*.txt"):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        contador += 1
    return lista_recetas

def elegir_receta(lista_recetas):
    eleccion_correcta = "x"
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista_recetas) + 1):
        eleccion_correcta = input("\nElije una receta: ")
    return lista_recetas[int(eleccion_correcta) - 1]

def leer_receta(mi_receta):
    print(Path.read_text(mi_receta))

def crear_receta(ruta_recetario):
    existe = False
    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + ".txt"
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta_recetario, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva,contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa receta ya fue creada")
        
def crear_categoria(ruta_recetario):
    existe = False
    while not existe:
        print("Escribe el nombre de tu nueva categoria: ")
        nombre_categoria = input() 
        ruta_nueva = Path(ruta_recetario, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa categoria ya fue creada")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} ha sido eliminado")

def volver_inicio():
    eleccion_regresar = "x"
    while eleccion_regresar.lower() != "v":
        eleccion_regresar = input("Preciona V para volver al menu: ")

finalizar_programa = False
opcion = 0

while not finalizar_programa:
    opcion = inicio()

    if opcion == 1:
        lista_categorias = mostrar_categorias(ruta_recetario) 
        mi_categoria = elegir_categoria(lista_categorias)
        lista_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_receta(lista_recetas)
        leer_receta(mi_receta)
        volver_inicio()
    elif opcion == 2:
        lista_categorias = mostrar_categorias(ruta_recetario) 
        mi_categoria = elegir_categoria(lista_categorias)
        crear_receta(mi_categoria)
        volver_inicio()
    elif opcion == 3:
        crear_categoria(ruta_recetario)
        volver_inicio()
    elif opcion == 4:
        lista_categorias = mostrar_categorias(ruta_recetario) 
        mi_categoria = elegir_categoria(lista_categorias)
        lista_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_receta(lista_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()
    elif opcion == 5:
        lista_categorias = mostrar_categorias(ruta_recetario) 
        mi_categoria = elegir_categoria(lista_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()
    elif opcion == 6:
        finalizar_programa = True





