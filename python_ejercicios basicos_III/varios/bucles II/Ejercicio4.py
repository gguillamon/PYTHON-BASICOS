# 4.- Escribir un programa que solicite un número positivo, acto seguido debe calcular la suma de
# todos los números pares comprendidos entre 0 y el numero solicitado. Ejemplo:
# Introduzca un número: 341
# La suma es: 29070
# Gabriel Guillamon

suma=0

numero=int(input("Introduzca un número:"))
if numero>0:
    for i in range(numero):
        if i % 2 == 0:
            suma+=i
else:
    print ("Introduzca un numero mayor que 0")  

print (f"La suma es {suma}")  