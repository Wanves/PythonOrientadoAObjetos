# Propiedades

# class Cuenta:
#     def __init__(self, numero, titular, saldo, agencia, limite):
#         self.__numero = numero
#         self.__titular = titular
#         self.__saldo = saldo
#         self.__agencia = agencia
#         self.__limite = limite
#     # --------------------------------

#     def get_saldo(self):
#         return self.__saldo

#     def get_titular(self):
#         return self.__titular

#     def get_limite(self):
#         return self.__limite
#     # --------------------------------

#     def set_limite(self, limite):
#         self.__limite = limite
#     # --------------------------------

#     def retira(self, valor):
#         self.__saldo -= valor

#     def deposita(self, valor):
#         self.__saldo += valor

#     def extracto(self):
#         print(
#             f'El saldo de la cuenta de: {self.__titular} es: {self.__saldo} ')

#     def transfiere(self, valor, origen, destino):
#         self.retira(valor)
#         self.deposita(valor)

#     # --------------------------------

#     def __str__(self):
#         print(f'Número: {self.__numero} \nTitular: {self.get_titular()} \nSaldo: {self.get_saldo()} \nAgencia: {self.__agencia} \nLímite: {self.get_limite()}')


# cuenta = Cuenta(777111, 'Juan', 20000000, 'BNA', 20000000)
# cuenta1 = Cuenta(666111, 'Pam', 10000000, 'BNA', 20000000)
# cuenta2 = Cuenta(555111, 'Teo', 15000000, 'BNA', 20000000)
# print(" ")
# print(f'Saldo: {cuenta.get_saldo()}')
# print(" ")
# print(f'Titular: {cuenta.get_titular()}')
# print(" ")
# print(f'Límite actúal: {cuenta.get_limite()}')
# print(" ")
# cuenta.set_limite(50000000)
# print(" ")
# cuenta.__str__()
# print(" ")
# print(f'Límite nuevo: {cuenta.get_limite()}')
# print(" ")

class Cliente:
    def __init__(self, nombre) -> None:
        self.__nombre = nombre
    

    def get_nombre(self):
        return self.__nombre.title()
        
cliente = Cliente('Juan Wanvestrant')
print("")
print(f'Cliente: {cliente.get_nombre()}')
print("")

class Cliente:
    def __init__(self, nombre) -> None:
        self.__nombre = nombre
    
    @property
    def nombre(self):
        return self.__nombre.title()
        
cliente = Cliente('Juan Wanvestrant')
print("")
print(f'Cliente: {cliente.nombre}')
print("")

class Cliente:
    def __init__(self, nombre, limite) -> None:
        self.__nombre = nombre
        self.__limite = limite
    @property
    def nombre(self):
        return self.__nombre.title()
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        
        
cliente = Cliente('Juan Wanvestrant', 50000000)
print("")
print(f'Cliente: {cliente.nombre}')
print("")
cliente.nombre = 'Neo'
print("")
print(f'Cliente: {cliente.nombre}')
print("")
print(f'Cliente: {cliente.limite}')
print("")
cliente.limite = '100000000'
print("")
print(f'Cliente: {cliente.limite}')
print("")

# Lo que aprendimos en esta aula:

# Métodos de lectura para los atributos: Getters.
# Métodos de modificación para los atributos, Setters.
# Propiedades.