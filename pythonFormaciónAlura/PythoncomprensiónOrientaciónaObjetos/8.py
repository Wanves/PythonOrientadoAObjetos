# Getters y setters

class Cuenta:
    def __init__(self, numero, titular, saldo, agencia, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__agencia = agencia
        self.__limite = limite
        self.__codigo_banco = '1001'
    # --------------------------------
    @property
    def saldo(self):
        return self.__saldo
    @property    
    def titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite
    # --------------------------------

    def set_limite(self, limite):
        self.__limite = limite
    # --------------------------------

    def retira(self, valor):
        if self.__puede_retirar(valor):
         self.__saldo -= valor
        else:
            print(f'El valor {valor} exedió el límite permitido')
            
    def __puede_retirar(self, valor_a_retirar):        
        valor_disponible = self.__saldo + self.__limite
        return valor_a_retirar <= valor_disponible
    
    def deposita(self, valor):
        self.__saldo += valor

    def extracto(self):
        print(
            f'El saldo de la cuenta de: {self.__titular} es: {self.__saldo} ')

    def transfiere(self, valor, origen, destino):
        self.retira(valor)
        self.deposita(valor)
    
    @staticmethod
    def codigo_banco():
        return '1001'
    @staticmethod
    def codigo_bancos():
        return {'BR':'1001','BNA':'1002','ITAU':'1003'}

    # --------------------------------

    def __str__(self):
        print(f'Número: {self.__numero} \nTitular: {self.__titular} \nSaldo: {self.__saldo} \nAgencia: {self.__agencia} \nLímite: {self.get_limite()}')


cuenta = Cuenta(777111, 'Juan', 20000000, 'BNA', 20000000)
cuenta1 = Cuenta(666111, 'Pam', 10000000, 'BNA', 20000000)
print(" ")
cuenta.retira(3000000)
print(" ")
cuenta.extracto()
print(" ")
cuenta.retira(1000000)
print(" ")
cuenta.extracto()
print(" ")
cuenta.extracto()
print(" ")
cuenta.retira(200000)
print(" ")
cuenta.extracto()
print(" ")
print(cuenta.codigo_banco())
print(" ")
codigos = cuenta.codigo_bancos()
print(" ")
print(codigos['BNA'])
print(" ")

# Lo que aprendimos en esta aula:

# Métodos privados.
# Métodos de clase y métodos estáticos.