lista_numeros=[1,2,3,4,5,6,7]

def cantidad_pares(lista_numeros):
    numeros_pares=[]
    for n in lista_numeros:
        if n%2 ==0:
            numeros_pares.append(n)
        else:
            pass
    return numeros_pares.__len__()

resultado = cantidad_pares(lista_numeros)

print(resultado)

