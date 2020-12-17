# 15.- Escribir un programa que dándole un número (entre 2 y 40) imprima un rombo como el de la
# figura. Ejemplo:
# Nivel: 4
# XXXX XXXX
# XXX   XXX
# XX     XX
# X       X
# X       X
# XX     XX
# XXX   XXX
# XXXX XXXX
#Gabriel Guillamon

num = int(input('Nivel: '))

if num not in range(2, 41):
    print('Error: el numero debe de estar en el intervalo 2-40')
else:
    
    espacios = 0

    simbolos = 'X' * num

    for i in range(0, num):#bucle para espacios
        espacios = (' ' * i) * 2
        print(f'{simbolos}{espacios}{simbolos}')
        simbolos = simbolos[:len(simbolos) - 1]

    for i in range(0, num):#bucle para simbolos
        simbolos += 'X'
        print(f'{simbolos}{espacios}{simbolos}')
        espacios = espacios[:len(espacios) - 2]


