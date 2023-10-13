
class Cuenta:
    def __init__(self, numero, titular, saldo, agencia, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.agencia = agencia
        self.limite = limite

    def retira(self, valor):
        self.saldo -= valor


    def deposita(self, valor):
        self.saldo += valor


    def extracto(self):
        print(f'El saldo de la cuenta de: {self.titular} es: {self.saldo} ')

    def __str__(self):
        print(
            f'Número: {self.numero} \nTitular: {self.titular} \nSaldo: {self.saldo} \nAgencia: {self.agencia} \nLímite: {self.limite}')


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
# -----------------------------------
# Lo que aprendimos en esta aula:

# Clases.
# Objetos.
# Función constructora.
# Dirección y referencia de objetos.
# Atributos de clase.
# Acceso a los atributos a través del objeto.
# Lo que aprendimos en esta aula:

# Métodos que definen el comportamiento de una clase.
# Creación de métodos.
# Cómo llamar métodos a través del objeto.
# Acceso a los atributos a través de self.
# Colector de basura.
# El tipo None.