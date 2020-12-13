# Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero
# , o un mensaje de aviso en caso contrario.

num1=float(input("Introduzca el primer numero"))

num2=float(input("Introduzca el segundo numero"))

while num2 != 0:
    print("El resultado es ",num1/num2,)
    num1=float(input("Introduzca el primer numero"))

    num2=float(input("Introduzca el segundo numero"))
print("Ha introducido un cero el programa ha terminado")