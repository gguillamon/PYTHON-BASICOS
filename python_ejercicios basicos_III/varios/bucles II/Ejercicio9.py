# 9.- Escribir un programa para calcular superficies. Constará de un menú que solicitará la figura a
# la que se va a calcular la superficie, pedirá los datos (lado, base y altura, radio ...) según la figura
# de la que se trate y visualizará el resultado. El programa deberá calcular superficies de las
# siguientes figuras: cuadrados, triángulos y círculos. Ejemplo:
# Cálculo de superficies:
# 1.- Cuadrados
# 2.- Triángulos
# 3.- Círculos
# 4.- Salir
# Elija opción (1-4): 1
# Lado: 8
# La superficie es de 64 cm²
# (mostramos de nuevo el menú...)
#Gabriel Guillamon

import math

salir = False
while not salir:
    area = None
    print('1.- Cuadrados')
    print('2.- Triángulos')
    print('3.- Círculos')
    print('4.- Salir')

    opcion = int(input('Elija la opcion (1-4): o pulse cualquier otra tecla para salir '))
    if opcion == 1:
        lado = float(input('Introduza el lado: '))
        area = lado * lado
    elif opcion == 2:
        base = float(input('Introduza base: '))
        altura = float(input('Introduza altura: '))
        area = base * altura / 2
    elif opcion == 3:
        radio = float(input('Radio: '))
        area = math.pi * (radio ** 2)
    else:
        salir = True

    if area:
        print(f'El area es: {area} cm²')
