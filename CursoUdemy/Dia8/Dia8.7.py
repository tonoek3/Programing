def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adios")
    return otra_funcion


def mayus(texto):
    print(texto.upper())

saludo_mayus =  decorar_saludo(mayus)

mayus("joto")

