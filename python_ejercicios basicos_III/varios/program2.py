# 2. Crear un programa que lea por teclado una cadena y un carácter, 
# y reemplace todos los dígitos en la cadena por el carácter. Ej: su clave es:
#  1540 y X debería devolver su clave es: XXXX

cadena=input("Introduzca una cadena: ")
caracter=input("Introduzca un caracter: ")
cadena=cadena.split()
re=cadena.split(cadena,caracter)
print(re)


