# Getters y setters

class Cuenta:
    def __init__(self, numero, titular, saldo, agencia, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__agencia = agencia
        self.__limite = limite
    # --------------------------------

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite
    # --------------------------------

    def set_limite(self, limite):
        self.__limite = limite
    # --------------------------------

    def retira(self, valor):
        self.__saldo -= valor

    def deposita(self, valor):
        self.__saldo += valor

    def extracto(self):
        print(
            f'El saldo de la cuenta de: {self.__titular} es: {self.__saldo} ')

    def transfiere(self, valor, origen, destino):
        self.retira(valor)
        self.deposita(valor)

    # --------------------------------

    def __str__(self):
        print(f'Número: {self.__numero} \nTitular: {self.get_titular()} \nSaldo: {self.get_saldo()} \nAgencia: {self.__agencia} \nLímite: {self.get_limite()}')


cuenta = Cuenta(777111, 'Juan', 20000000, 'BNA', 20000000)
cuenta1 = Cuenta(666111, 'Pam', 10000000, 'BNA', 20000000)
cuenta2 = Cuenta(555111, 'Teo', 15000000, 'BNA', 20000000)
print(" ")
print(f'Saldo: {cuenta.get_saldo()}')
print(" ")
print(f'Titular: {cuenta.get_titular()}')
print(" ")
print(f'Límite actúal: {cuenta.get_limite()}')
print(" ")
cuenta.set_limite(50000000)
print(" ")
cuenta.__str__()
print(" ")
print(f'Límite nuevo: {cuenta.get_limite()}')
print(" ")
