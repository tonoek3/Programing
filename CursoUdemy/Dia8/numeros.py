def numeros_perfume():
    n = 0
    while True:
        n += 1
        yield print("A-"+str(n))
        
def numeros_farmacia():
    n = 0
    while True:
        n += 1
        yield print("B-"+str(n))

def numeros_cosme():
    n = 0
    while True:
        n += 1
        yield print("C-"+str(n))

def mensaje(turno):
    print("Tu turno es el numero:")
    print(turno)
    print("Porfavor, espere. xd ")



mi_turno = next(numeros_perfume())




