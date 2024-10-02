"""class Usuario:
    def __init__(self):
        self.nombre = "Nariyoshi"
        self.apellido = "Miyagi"
        self.email = "miyagi@codingdojo.la"
        self.limite_credito = 30000
        self.saldo_pagar = 0

miyagi = Usuario()
daniel = Usuario()

#Accedemos a los atributos de la instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Nariyoshi

daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
print(daniel.nombre) #Imprime: Daniel
print()
class Usuariov1:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

miyagi = Usuariov1("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuariov1("Daniel", "Larusso", "daniel@codingdojo.la")

print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel

clases de Métodos

class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido

miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

miyagi.hacer_compra(150)
miyagi.hacer_compra(300)
daniel.hacer_compra(45)

print(miyagi.saldo_pagar) #Imprime: 450
print(daniel.saldo_pagar) #Imprime: 45
"""
"""
clases de Métodos Practica
"""
print("------------Practica-----------")
class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido

    def pagar_tarjeta(self, monto):
        self.saldo_pagar = self.saldo_pagar - monto

    def mostrar_saldo_usuario(self):
         return print("Usuario:",self.nombre, self.apellido, "Saldo de Pago", "$",self.saldo_pagar)

miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

miyagi.hacer_compra(150)
miyagi.hacer_compra(300)
miyagi.pagar_tarjeta(100)

print(miyagi.saldo_pagar)
print(miyagi.mostrar_saldo_usuario())