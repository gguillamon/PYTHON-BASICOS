# 17.- Escribir un programa que haga que el usuario piense un número entero de 1 a 100, el
# programa deberá adivinarlo en el menor número de intentos posible. Al final debe decir en
# cuántos intentos lo ha conseguido, un “posible” simulacro (no óptimo) del juego podría ser:
# Piense un número del 0 al 100 (no me engañe ni cambie de número)
# ENTER para comenzar
# -- El usuario piensa el número 15
# ¿es el 30? (m-mayor, n-menor, i-igual)
# n
# ¿es el 5?
# m
# ¿es el 12?
# m
# ¿es el 15?
# i
# ¡¡¡Qué bueno soy, lo he acertado en tan sólo 4 intentos!!!
# ¿Desea jugar otra vez (S/N)? N
# Mejorar el programa para que detecte si el usuario cambia de número a mitad de la partida y
# también para que el ordenador cambie de mensaje según el número de intentos que haga.

#Gabriel Guillamon


import random

Detecta_trampa = False
salir = False
while not salir and not Detecta_trampa:
    acertado = False
    intentos = 1
    input('Piense un número del 0 al 100 (no me engañe ni cambie de número)\n Pulse ENTER para comenzar')
    resultado = input('¿Es el 50? (m-mayor, n-menor, i-igual): ')
    if resultado == 'm':
        max = 100
        min = 50 + 1
    elif resultado == 'n':
        max = 50 - 1
        min = 0
    elif resultado == 'i':
        acertado = True
    while not acertado and not Detecta_trampa:
        intentos += 1
        num = random.randint(min, max)
        resultado = input(f'¿Es el {num}?: ')
        if resultado == 'm':
            if len(range(min, max)) == 0:
                Detecta_trampa = True
            min = num+1
        elif resultado == 'n':
            if len(range(min, max)) == 0:
                Detecta_trampa = True
            max = num-1
        elif resultado == 'i':
            acertado = True

    if not Detecta_trampa:
        if intentos < 10:
            print(f'QUE BUENO SOY. He acertado en SOLO {intentos} intentos!!!')
        else:
            print(f'He acertado en {intentos} intentos... :(')

        jugar = input('¿Desea volver a jugar?: (y/*)')
        if jugar != 'y':
            salir = True
    else:
        print('Estás haciendo trampa...')

print('Fin del juego, hasta la proxima!!')
