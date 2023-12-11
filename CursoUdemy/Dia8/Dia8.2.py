def pedir_numero():
    while True:
        try:
            numero = int(input("Introduce un numero: "))
        except:
            print("Digito no valido")
        else:
            print(f"Tu numero es {numero}")
            break
    print("Gracias por todo tontin")

pedir_numero()