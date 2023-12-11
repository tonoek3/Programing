## Ejemplo de como usar funciones dentro de otras funciones
## Las funciones se pueden almacenar en variables

def cambiar_letras(tipo):
    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula
    
operacion = cambiar_letras('may')

operacion("joto")



