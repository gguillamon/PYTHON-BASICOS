# Si tenemos una cadena con un nombre y apellidos,
# realizar un programa que muestre las iniciales en mayúsculas.

Nombre=input("Introduce tu nombre y apellidos: ")

division=Nombre.split()



print(division[0][0].upper(),division[1][0].upper(), division[2][0].upper(), end=" ")
