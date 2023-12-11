def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    print(n1 + n2)

try:
    suma()
except ValueError:
    print("Valor no valido")
except:
    print("hubo un problema")
else:
    print("Gracias por hacer bien tu trabajo")



"""
try:
    # Codigo que queremos probar
except:
    # Codigo a ejecutar si hay un error
else:
    # Codigo a ejecutar si no hay un error
finally:
    # Codigo que se va a ejecutar de todos modos
"""