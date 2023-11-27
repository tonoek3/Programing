class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre 
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido,  numero_cuenta, saldo=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
    
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}, numero de cuenta: {self.numero_cuenta} con un saldo de {self.saldo}"
    
    def depositar(self, deposito):
        self.saldo += deposito
        print("Deposito exitoso.")

    def retirar(self, retiro):
        if self.saldo >= retiro:
            self.saldo -= retiro
            print("Retiro exitoso")
        elif self.saldo < retiro:
            print("No tienes saldo suficiente para retirar")       
       
def crear_cliente():
    nombre = input("Introduce tu primer nombre: ")
    apellido = input("\nIntroduce tu primer apellido: ")
    numero_cuenta = input("\nIntroduce tu numero de cuenta: ")
    cliente = Cliente(nombre, apellido, numero_cuenta)   
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion= 0

    while opcion != range(1,3):
        print("""[1] Depositar \n[2] Retirar \n[3] Salir""")
        opcion = int(input("Que accion desea realizar"))

        if opcion == 1:
            monto = int(input("Cuanto deseas depositar: "))
            mi_cliente.depositar(monto)
        
        elif opcion == 2:
            monto_retiro = int(input("Cuanto deseas retirar: "))
            mi_cliente.retirar(monto_retiro)
        
        elif opcion == 3:
            break
        print(mi_cliente)

    print("Gracias poe operar en banco Python")

inicio()
