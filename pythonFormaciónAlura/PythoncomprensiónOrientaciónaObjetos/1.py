# Programación orientada a objetos

# numero, titular, saldo, limite

# numero = 123
# titular = 'Juan'
# saldo = 55.0
# limite = 1000.0

# print(" ")
# print(numero)
# print(" ")

# numero1 = 321
# titular1 = 'Zoe'
# saldo1 = 100.0
# limite1 = 1000.0

# print(" ")
# print(numero1)
# print(" ")

cuenta = {
    'numero': 123,
    'titular': 'Juan',
    'saldo': 55.0,
    'limite': 1000.0
}
cuenta2 = {
    'numero': 321,
    'titular': 'Zoe',
    'saldo': 100.0,
    'limite': 1000.0
}

# print(" ")
# print(cuenta['titular'])
# print(" ")
# print(cuenta2['titular'])
# print(" ")


def cuenta(numero, titular, saldo, limite):
    cuenta = {
        'numero': numero,
        'titular': titular,
        'saldo': saldo,
        'limite': limite
    }
    return cuenta

cuenta1 = cuenta(777,'Neo',1000000,1000000000)
cuenta2 = cuenta(666,'Zoe',2000000,2000000000)
print(" ")
print(cuenta1)
print(" ")
print(cuenta2)
print(" ")


def retira(cuenta,valor):
    cuenta['saldo'] -= valor
    
def deposita(cuenta,valor):
    cuenta['saldo']+= valor
    
def extracto(cuenta):
    print(f'El saldo de la cuenta de: {cuenta["titular"]} es: {cuenta["saldo"]} ')
    
retira(cuenta1, 40)
extracto(cuenta1)
print(" ")
deposita(cuenta1,1000000.0)
print(" ")
extracto(cuenta1)

# Lo que aprendimos en esta aula:

# Diccionarios.
# Funciones.
# Encapsulamiento de código.