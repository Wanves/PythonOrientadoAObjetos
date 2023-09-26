# Ciclo for
# Juego con el siclo for

def run():

    try:
        print("-----------------------")
        print('   Adivina el número   ')
        print("-----------------------")
        print('   Tienes tres intentos   ')
        print("-----------------------")
        numero_secreto = 55
        
        intento = 1
        for intento in range(1,4):
            print(f"Intento {intento}")
            print(" ")
            print(" ")
            entrada = int(input('Ingresa un número: '))
            print(" ")
            print(f'El número ingresado es: {entrada}')
            print(" ")
            if entrada < 1 or entrada > 100:
                print('Ingresa un número mayor que 0 y menor o igual a 100')
                continue
            elif intento ==4:
                break
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
        print("Fin del juego✅")
        print(" ")
    except:
        print(" ")
        print('Haz ingresado un valor no requerido')
        print(" ")

if __name__ == '__main__':
    run()
    
# Lo que aprendimos en esta aula:

# El ciclo de lazo con la cláusula FOR en Python.
# Las cláusulas CONTINUE y BREAK en Python.