# funciones incorporadas
import random as r


def jugar():
    print(" ")
    print("-----------------------")
    print('   Adivina el número   ')
    print("-----------------------")
    print('  Tienes tres intentos   ')
    print({__name__})
    print("-----------------------")
    print("Elige el nivel de dificultad: ")
    print(" ")
    print(f' (1)Novato (2)Intermedio (3)Avanzado')
    print(" ")

    nivel = int(input('Nivel: '))
    if nivel == 1:
            total_intentos = 20
    elif nivel == 2:
            total_intentos = 10
    else:
            total_intentos = 5

    numero_secreto = r.randint(1, 100)
    puntos = 1000
        # print(f'El numero secreto es: {numero_secreto}')
    intento = 1

    for intento in range(1, total_intentos+1):
            print(f"Intento {intento} de {total_intentos}")
            print(" ")
            print(" ")
            entrada = int(input('Ingresa un número: '))
            print(" ")
            print(f'El número ingresado es: {entrada}')
            print(" ")
            if entrada < 1 or entrada > 100:
                if intento == total_intentos:
                    break
                print('Ingresa un número mayor que 0 y menor o igual a 100')
                continue
            elif intento == total_intentos:
                break
            acierto = entrada == numero_secreto
            mayor = entrada > numero_secreto
            menor = entrada < numero_secreto

            if acierto:
                print(
                    f'Genial! haz acertado el número secreto.😃 Tu puntajes es {puntos}')
                print(" ")
                print(" ")
                break
            else:
                if mayor:
                    print(
                        'No haz acertado el número secreto. El número ingresado es mayor al número secreto')
                elif menor:
                    print(
                        'No haz acertado el número secreto. El número ingresado es menor al número secreto')
                puntos_perdidos = abs(numero_secreto - entrada)
                puntos = puntos - puntos_perdidos
                print(" ")
    print("Fin del juego✅")
    print(" ")
if __name__=='__main__':
    jugar()


# Lo que aprendimos en esta aula:

# Trabajar con el módulo random.
# A definir intervalos de números y aplicarlos a la función randint().

# Lo que aprendimos en esta aula:

# A utilizar funciones incorporadas de Python.
