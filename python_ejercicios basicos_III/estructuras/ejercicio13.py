#Ejercicio que muestra la raiz cuadrada y cubica de un numero
import math
numero=int(input("Introduzca un numero entero:"))
resultado=math.sqrt(numero)
resultado2=numero**(1/3)
print("La raiz cuadrada es:",resultado)
print("La raiz cúbica es: %.2f" % resultado2)

