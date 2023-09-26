# Mejorando el juego con siclos While
# Mientras se cumpla una condición el ciclo seguirá siendo ejecutado

def run():

    try:
        print("-----------------------")
        print('   Adivina el número   ')
        print("-----------------------")
        print('   Tienes tres intentos   ')
        print("-----------------------")
        numero_secreto = 55
        total_intentos = 3
        intento = 1
        while total_intentos >= intento:
            print(f"Intento {intento} de {total_intentos}")
            print(" ")
            print(" ")
            entrada = int(input('Ingresa un número: '))
            print(" ")
            print(f'El número ingresado es: {entrada}')
            print(" ")
            acierto = entrada == numero_secreto
            mayor = entrada > numero_secreto
            menor = entrada < numero_secreto

            if acierto:
                print('Genial! haz acertado el número secreto.😃')
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
                print(" ")
            intento += 1
        print("Fin del juego✅")
        print(" ")
    except:
        print(" ")
        print('Haz ingresado un valor no requerido')
        print(" ")

if __name__ == '__main__':
    run()

# Lo que aprendimos en esta aula:

# Qué son y cómo funcionan los ciclos de lazo.
# El ciclo de lazo con la cláusula WHILE en Python.
# La función format().