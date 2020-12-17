# 14.- Escribir un programa que dándole un número (entre 2 y 40) imprima un triángulo como el de la figura.
# Nivel: 4
#  XX
#  XXXX
#  XXXXXX
# XXXXXXXX
# Nivel: 3
#  X
# XXX
# XXXXX
# Nivel: 2
#  XX
# XXXX

nivel = int(input('Nivel: '))

if nivel not in range(2, 41):
    print('Error: el nivel erróneo, debe estar en el intervalo 2 - 40')
else:
   
    espacios = nivel - 1

    if nivel % 2 == 0:
        simbolo = 'XX'
    else:
        simbolo = 'X'

    for i in range(0, nivel):
        espacios = ' ' * espacios
        print(f'{espacios}{simbolo}')

        simbolo += 'X' * 2
        espacios -= 1
