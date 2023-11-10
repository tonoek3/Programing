#Proyecto dia 3
print("Te dire cunatas veces sale una letra, cuatas palabras tiene el texto, cual es la primera letra y la ultima del texto, el texto al reves, te dire si existe la palabra python")
texto=input("Ingresa el texto que quieras que estudie: ").lower()
letra1= input("Ingresa una letra: ").lower()
letra2= input("ingresa la letra 2: ").lower()
letra3= input("Ingresa la letra 3: ").lower()

print(f"La letra {letra1} se repite "+str(texto.count(letra1)),"veces",f"la letra {letra2} se repite "+str(texto.count(letra2)),"veces",f"la letra {letra3} se repite "+str(texto.count(letra3)),"veces")

texto=list(texto.split(" "))
numPalabras=texto.__len__()
print(f"En el texto hay {numPalabras} palabras")

separador= " "
texto=separador.join(texto)

primeraLetra=texto[0]
ultimaLetra=texto[-1]
print(f"La primera letra del texto es {primeraLetra} y la ultima letra del texto es {ultimaLetra}")

texto=list(texto.split(" "))
numPalabras=texto.__len__()

alReves=list(reversed(texto))

separador= " "
alReves=separador.join(alReves)

print(alReves)

siEsta="python" in texto

print(f"La palabra python se encuentra en el texto: {siEsta}.")






