# Escribe un programa que diga si un número introducido por teclado es o no primo. 
# Un número primo es aquel que sólo es divisible entre él mismo y la unidad.
#  Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.

num=input("Introduzca un numero o enter para salir: ")

while num != 0:
    for i in range(2,int(num)):
        if int(num) % i == 0:
            print("No es primo")
        else:
            print("es primo")
        num=input("Introduzca un numero: ")

           
    