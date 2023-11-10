


def chequear_3_cifras(lista):
    lista_3_cifras =[]

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

resultado=chequear_3_cifras([333,22,310])

print(resultado)