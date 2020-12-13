# Realizar un programa que comprueba si una cadena leída por teclado comienza 
# por una subcadena introducida por teclado.

cadena=input("Introduzca la primera cadena: ")
subcadena=input("Introduzca la palabra de comienzo: ")

if cadena.startswith(subcadena) == True:
    print("correcto, empieza con la cadena especificada.")
else:
    print("La cadena no comienza por el texto introducido.")