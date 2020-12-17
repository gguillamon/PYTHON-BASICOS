# 5.- Escribe un programa que dado un número, muestre todos los múltiplos de 11 desde el cero
# hasta el número.
# 1
# Introduzca un número: 125
# Los múltiplos son: 0 , 11 , 22 , 33 , 44 , 55 , 66 , 77 , 88 , 99 , 110 ,
# 121
# Gabriel Guillamon
numero=int(input("Introduzca un numero:"))
resultado=0
while resultado != numero:
    resultado+=1
    if resultado % 11 == 0:
        print(f"{resultado}",end=" ,")
