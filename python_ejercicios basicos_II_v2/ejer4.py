
from math import sqrt, pow

a = float(input('Introduzca a: '))
b = float(input('Introduzca b: '))
c = float(input('Introduzca c: '))
if a == 0:
    if b != 0:
        x = -c / b
        print(f'Solucion: x={x}')
    else:
        if c != 0:
            print('La ecuacion no tiene solucion.')
else:
    x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print(f'Soluciones: x1={x1} y x2={x2}')

