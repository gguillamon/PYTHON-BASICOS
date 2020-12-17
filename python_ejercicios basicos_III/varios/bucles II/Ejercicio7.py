# 7.- Escribir un programa que solicite números (enteros o reales), el programa terminará cuando
# se introduzca el cero. A continuación debe mostrar el mayor número. Ejemplo:
# Introduzca un número (cero para terminar): 1230
# Introduzca un número (cero para terminar): 0.023
# Introduzca un número (cero para terminar): 12.23
# Introduzca un número (cero para terminar): 3.1415
# Introduzca un número (cero para terminar): 280
# Introduzca un número (cero para terminar): 4234.6
# Introduzca un número (cero para terminar): 0
# Mayor: 4234.6
# # Gabriel Guillamon

mayor =0
numero=-1
while numero != 0:
    numero = float(input('Introduce un numero positivo (cero para terminar): '))
    if numero > mayor:
        mayor = numero
print("El mayor es:", mayor)        
