# Encapsulamineto

class Cuenta:
    def __init__(self, numero, titular, saldo, agencia, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__agencia = agencia
        self.__limite = limite

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
        
        
    def __str__(self):
        print(
            f'Número: {self.__numero} \nTitular: {self.__titular} \nSaldo: {self.__saldo} \nAgencia: {self.__agencia} \nLímite: {self.__limite}')


cuenta = Cuenta(777111, 'Juan', 20000000, 'BNA', 20000000)
cuenta1 = Cuenta(666111, 'Pam', 10000000, 'BNA', 20000000)
cuenta2 = Cuenta(555111, 'Teo', 15000000, 'BNA', 20000000)
print(" ")
print('-----Cuenta-----')
print(" ")
cuenta.__str__()
print(" ")
cuenta1.__str__()
print(" ")
cuenta2.__str__()
print(" ")
# ---------------------------------
print(" ")
cuenta.retira(500000)
print(" ")
cuenta.extracto()
print(" ")
cuenta1.retira(500000)
print(" ")
cuenta1.extracto()
print(" ")
cuenta2.retira(500000)
print(" ")
cuenta2.extracto()
print(" ")
# ---------------------------------
print(" ")
cuenta.__str__()
print(" ")
cuenta1.__str__()
print(" ")
cuenta2.__str__()
print(" ")
# -----------------------------------
print(" ")
cuenta.deposita(3000000)
print(" ")
cuenta.extracto()
print(" ")
cuenta1.deposita(3000000)
print(" ")
cuenta1.extracto()
print(" ")
cuenta2.deposita(3000000)
print(" ")
cuenta2.extracto()
print(" ")
# ---------------------------------
print(" ")
cuenta.__str__()
print(" ")
cuenta1.__str__()
print(" ")
cuenta2.__str__()
print(" ")
# ------------------------------------
print('Valor extráe, deposita----------')
print(" ")
cuenta1.transfiere(100, cuenta, cuenta1)
print(" ")
cuenta.extracto()
print(" ")
cuenta1.extracto()
print(" ")
# ------------------------------------


print('Debajo de las primeras instancias----------')
cuenta = Cuenta(777111, 'Juan', 20000000, 'BNA', 20000000)
cuenta1 = Cuenta(666111, 'Pam', 10000000, 'BNA', 20000000)
cuenta2 = Cuenta(555111, 'Teo', 15000000, 'BNA', 20000000)

# print(" ")
# cuenta.__str__()
# print(" ")
# cuenta1.__str__()
# print(" ")
# cuenta2.__str__()
# print(" ")
print(f'''
    Número: {cuenta1._Cuenta__numero}
    Titular:{cuenta1._Cuenta__titular}
    Saldo{cuenta1._Cuenta__saldo}
    Agencia{cuenta1._Cuenta__agencia}
    Límite{cuenta1._Cuenta__limite}
      ''')
print(" ")
print(f'''
    Número: {cuenta2._Cuenta__numero}
    Titular:{cuenta2._Cuenta__titular}
    Saldo{cuenta2._Cuenta__saldo}
    Agencia{cuenta2._Cuenta__agencia}
    Límite{cuenta2._Cuenta__limite}
      ''')

# Lo que aprendimos en esta aula:

# Atributos privados.
# Encapsulamiento del código.
# Encapsulamiento de la manipulación de atributos en los métodos.
# Cohesión del código.