def prueba (n1,n2,*args,**kwargs):
    print(f"{n1} es tu primer valor")
    print(f"{n2} es tu segundo valor")

    for cosa in args:
        print(f"los argumentos son {cosa}")

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
    return 

numeros=[10,20,30,40]
perros={"enzo":"pastor aleman","toreto":"snausher"}
prueba(23,14,*numeros,**perros)