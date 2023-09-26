# La condición Si No Si

def run():
    try:
        print("-----------------------")
        print('   Adivina el número   ')
        print("-----------------------")

        numero_secreto = 55

        # introducir un número
        print(" ")
        entrada = int(input('Ingresa un número: '))
        print(" ")
        print(f'El número ingresado es: {entrada}')
        print(" ")
        acierto = entrada == numero_secreto
        mayor = entrada > numero_secreto
        menor = entrada < numero_secreto
        # si es el número que se almacenó en entrada es igual al número secrtedo: Acierto
        if acierto:
            print('Genial! haz acertado el número secreto.')
            print(" ")
        # si no se cumple la condición anterior , será: Error
        else:
            # si el usuario ingresa un número mayor especificarlo
            if mayor:
                print(
                    'No haz acertado el número secreto. El número ingresado es mayor al número secreto')
            elif menor:
                print(
                    'No haz acertado el número secreto. El número ingresado es menor al número secreto')
            print('No haz acertado el número secreto')
            print(" ")

        print(type(numero_secreto))
        print(" ")
        print(type(entrada))
        print(" ")
        print(type(acierto))
        print(" ")
    except:
        print(" ")
        print('Haz ingresado un valor no requerido')
        print(" ")


if __name__ == '__main__':
    run()


# Lo que aprendimos en esta aula:

# A realizar comparaciones entre variables.
# El control de flujo con las cláusulas IF, ELSE y ELIF en Python.
