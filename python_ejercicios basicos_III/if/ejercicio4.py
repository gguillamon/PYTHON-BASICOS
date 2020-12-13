#Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero,
# o un mensaje de aviso en caso contrario.

num1=int(input("Introduzca el primer numero:"))
num2=int(input("Introduzca el segundo numero:"))

if num2 > 0:
    print(num1/num2)
else:
    print("El segundo numero debe ser mayor que 0")    