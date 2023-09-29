

# palabra ='banana'
# print(" ")
# print(palabra.startswith('b'))
# print(palabra.endswith('a'))
# intento = 'a'
# indice = 0


# print(" ")
# print(palabra.find('a'))
# print(" ")

# for letra in palabra:
#     if intento == letra:
#         print(f'Encontré la letra {letra} en la posición {indice}')
#     else:
#         print('La letra no se encuentra en ésta posición')
#     indice = indice + 1
# print(f'La cantidad de letras que contiene la palabra es: {len(palabra)}')
    
# intento = 'a'
# for letra in palabra:
#     if intento == letra:
#         print(f'Encontré la letra {letra} en la posición {indice}')
#     indice = indice + 1


# palabra = "aluracursos"



# palabra.find("a") # el resultado es 4


# print(palabra.find("a")) # el resultado es 4

# print(palabra.find("b")) # el resultado es -1

# print(palabra.find('s')) # el resultado es 9

# print(palabra.find("l")) # el resultado es 1

# a = "Caballo"
# b = "Vaca"
# print("{} y {}".format(b, a))

# palabra = "alura"
# palabra.upper()
# print(palabra) # ¿cuál es el resultado?

# import numpy as np

# # Generar una lista de 1000 números aleatorios
# lista_de_numeros = np.random.rand(1000)

# # Imprimir los primeros 10 números
# print(lista_de_numeros[:])



# # Crear una lista de 1000 ceros
# lista_de_ceros = np.zeros(1000)

# print(lista_de_ceros)


# precios = [1525,1120,1464,1200,1330,1356,1312,1531,1232, 1234,1250,1114,1553,1147,1303,1296,1309,1404,1479,1376,1152,1440,1038,1018,1291,1388,1577,1115,1488,1494,1254,1230,1122,1396,1208,1356,1549,1116,1443,1075,1536,1542,1036,1015,1020,1217,1484,1032,1390,1026]

# print(min(precios))

# valores = [0, 0, 0, 1, 2, 3, 4]
# print(valores.count(0))

# letras_acertadas = ['', '', '', '', '', '']
# letras_faltando = str(letras_acertadas.count('_'))
# print('Aún faltan acertar {} letras'.format(letras_faltando))

# frutas = ['Banana', 'Fresa', 'Manzana', 'Uva', 'Manzana', 'Uva']
# print(frutas.index('Uva'))

# # frutas = ['Banana', 'Fresa', 'Manzana', 'Uva']
# # print(frutas.index('Sandia'))


# frutas = ['Banana', 'Fresa', 'Manzana', 'Uva']
# fruta_buscada = 'Sandia'
# if fruta_buscada in frutas:
#   print(frutas.index(fruta_buscada))
# else:
#   print('Lo siento, {} no está en la lista de frutas'.format(fruta_buscada))


# instructor = ('Alvaro',38)
# instructor2 = ('José',48)

# instructores = [instructor, instructor2]
# print(instructores[1][0])
# print(instructores[1][1])


# nombres = ("Nico", "Douglas", "Flavio", "Daniel")

# nombres = []
# nombres.append("Fabio") 

# print(nombres)

# nombres = nombres[0]

# nombres = list(nombres)

# nombres = tuple(nombres)

# nombres = (nombres)


# total = 0
# frase = "python rocks!"
# acabo = False
# while (not acabo):
#     acabo = ( total == len(frase) )
#     total = total + 1
# print(total - 1)

# pasos = 0
# while (pasos <= 10):
#   pasos += 1
# print(pasos)


# enteros = [1,3,4,5,7,8]
# cuadrados = [n*n for n in enteros]
# print(cuadrados)

# cuadrados = [2 for n in enteros]



# archivo = open('palabras.txt', 'w')
# archivo.write('uva\n')
# archivo.write('banana\n')
# archivo.close()

# archivo = open('palabras.txt', 'a')
# archivo.write('fresa\n')
# archivo.write('manzana\n')
# archivo.close()

# archivo = open('palabras.txt', 'r')
# linea = archivo.readline()
# for linea in archivo:
#     print(linea.strip())

# def suma_dos_numeros(primer_numero, segundo_numero):
#     print(primer_numero + segundo_numero)

# def resta_dos_numeros(primer_numero, segundo_numero)
#     print(primer_numero - segundo_numero)

# def multiplica_dos_numeros(primer_numero, segundo_numero):
#     print(primer_numero * segundo_numero)

# def divide_dos_numeros(primer_numero, segundo_numero):
#     print(primer_numero / segundo_numero)
