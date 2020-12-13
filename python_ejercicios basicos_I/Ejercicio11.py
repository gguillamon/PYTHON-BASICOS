#11-Ejercicio que calcule la longitud de la cincunferencia pudiendo importar la libreria Math
import math
print("Vamos a calcular la longitud de una circunferencia...")
radio=int(input("Introduzca el radio en cm, por favor: "))
longitud=2*math.pi*radio
print("La longitud de la circunferecia es: %.2f cm"% longitud)