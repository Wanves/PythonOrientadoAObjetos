import random

def jugar():
  imprime_presentacion()

  palabra_secreta = cargar_palabra()

  letras_acertadas = inicializa_lista(palabra_secreta)
  print(letras_acertadas)  
  ahorco = False
  acerto = False
  errores = 0

  while (not ahorco and not acerto):  
    intento = pide_intento()
    if intento in palabra_secreta:  
      marca_intento_correcto(intento,letras_acertadas,palabra_secreta)
    else:
      errores += 1   
    dibuja_horca(errores)
    ahorco = errores == 7 
    acerto = "_" not in letras_acertadas 
    print(letras_acertadas)
    if ahorco:
      imprime_mensage_perdedor(palabra_secreta)
    elif acerto:
      imprime_mensage_vencedor()  
  print("\nFin del juego!")

def imprime_presentacion():
  print("****************************************")
  print("**************El Ahorcado***************")
  print("****************************************")
  print("Bienvenido al juego del ahorcado\n")

def cargar_palabra():
  archivo = open('palabras.txt','r')
  palabras = [linea.strip() for linea in archivo]
  archivo.close()
  i = random.randrange(0,len(palabras))
  palabra_secreta = palabras[i].strip().upper()
  return palabra_secreta

def inicializa_lista(palabra_secreta):
  return ['_' for letra in palabra_secreta]

def pide_intento():
  intento = input("\nDigita una letra: ")
  intento = intento.strip().upper()
  return intento

def marca_intento_correcto(intento,letras_acertadas,palabra_secreta):
  indice = 0      
  for letra in palabra_secreta:
    if intento == letra:
      letras_acertadas[indice] = letra       
      # print(f"Encontré la letra '{letra}' en la posición {indice}")         
    indice += 1 
  
def dibuja_horca(errores):
    print("  _______     ")
    print(" |/      |    ")

    if(errores == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errores == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errores == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errores == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errores == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errores == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errores == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensage_perdedor(palabra_secreta):
    print("¡Qué lástima! Te has ahorcado")
    print("La palabra era {}".format(palabra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensage_vencedor():
    print("Felicidades, ¡Has ganado!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")  

if (__name__=="__main__"):
  jugar()



# Lo que aprendimos en esta aula:

# La secuencia del juego El Ahorcado.
# Cómo iterar en cadenas de texto.
# Algunas funciones de string.

# Lo que aprendimos en esta aula:

# Qué son las listas en Python.
# Diversos métodos de listas.
# Qué son las tuplas en Python.
# Algunas aplicaciones de las tuplas.

# Lo que aprendimos en esta aula:

# Cómo finalizar ciclos de lazo con while.
# Qué son las comprensiones de lista en Python.
# Cómo usar la comprensión de listas.

# Lo que aprendimos en esta aula:

# Cómo crear un archivo de texto usando Python.
# Cómo iterar en un archivo de texto.
# Cómo añadir texto a un archivo previamente creado.
# Cómo leer un archivo de texto.
# Almacenar el contenido de un archivo de texto en una estructura secuencial de Python.

# Lo que aprendimos en esta aula:

# Pasos para la refactorización del código.
# Creación de funciones para mejorar la legibilidad y la claridad del código.
# Mejorar la presentación visual del código.