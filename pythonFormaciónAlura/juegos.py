import horca, adivinanza

def run():

    try:
        print(" ")
        print("-----------------------")
        print('   Juegos Python   ')
        print("-----------------------")
        print('  Tienes tres intentos   ')
        print("-----------------------")
        print('(1) Horca (2) Adivinanza')
        juego = int(input("Selecciona el juego que deseas: "))
        if juego == 1:
            print(f'Juego de la Horca')
            horca.jugar()
        elif juego == 2:
            print(f'Juego de adivinar el número {adivinanza}')
            adivinanza.jugar()
        
        
    except:
        print(" ")
        print('Haz ingresado un valor no requerido')
        print(" ")


if __name__=='__main__':
    run()



# Lo que aprendimos en esta aula:

# A generar archivos .py en Google Colab.
# A ejecutar archivos .py en el Command Prompt.
# A definir y ejecutar funciones en Python.