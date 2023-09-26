# pais = 'Brasil'
# titulos = 4

# print(" ")
# print('Argentina', 'tiene', '3', 'titulos', 'mundiales', 'de', 'futbol', sep='-')
# print(" ")
# print('Argentina', 'tiene', '3', 'titulos', 'mundiales', 'de', 'futbol', end=' ')
# print(" ")
# print(" ")
# print(f'{pais} tiene {titulos} titulos')
# print(" ")


# def adivina_numero():
#     numero_secreto = 42
#     print(" ")
#     entrada = int(input("Digita un número: "))
#     print(" ")
#     print("Digitaste el número ", entrada)
#     print(" ")
#     if entrada == numero_secreto:
#         print("Acertaste!")
#         print(" ")
#     else:
#         print("El número no corresponde.")
#         print(" ")
        
# adivina_numero()

print("**********************")
print("  Adivina el numero")
print("**********************")

numero_secreto = 55
entrada_str = input("Digita un número: ")
entrada = int(entrada_str)
print("El número que digitaste: ",entrada)

if (numero_secreto == entrada):
    print("¡Acertaste!")
else:
    print("El número no corresponde.")

print('El juego ha concluído!')