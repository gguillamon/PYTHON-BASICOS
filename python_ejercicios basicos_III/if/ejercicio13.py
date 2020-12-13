#Escribir un programa que lea un año indicar si es bisiesto. 
#Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, 
# excepto que también sea divisible por 400.

ANIO=int(input("Introduzca el año: "))
if ANIO % 4 == 0:
    print("es bisiesto")
elif ANIO % 4 == 0 and ANIO % 100 != 0:
    print("No es bisiesto")
elif ANIO % 4 == 0 and ANIO % 100 == 0 and ANIO % 400 == 0:
    print(" Es bisiesto")
else:
    print("No es bisiesto")    