def ejemplo1():

    def suma(num1,num2):
    
        try:
            print(num1+num2)
        except:
            print("Error inesperado")

def ejemplo2():
    def cociente(num1,num2):
        try:
            print(num1/num2)
        except TypeError:
            print("Los argumentos a ingresar deben ser números")
        except ZeroDivisionError:
            print("El segundo argumento no debe ser cero")

def ejemplo3():
    def abrir_archivo(nombre_archivo):
        try:
            archivo = open(nombre_archivo)
        except FileNotFoundError:
            print("El archivo no fue encontrado")
        except:
            print("Error desconocido")
        else:
            print("Abriendo exitosamente")
        finally:
            print("Finalizando ejecución")








