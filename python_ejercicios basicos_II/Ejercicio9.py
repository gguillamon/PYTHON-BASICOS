# 9.- Escribir un programa que pida cuatro números enteros por teclado y determine el mayor y el
# 2
# menor de los cuatro números. Ejemplo:
# Introduzca 4 números enteros: 20 34 10 -18
# Mayor número: 34
# Menor número: -18
mayor=1
menor=0
numeros=[]
for i in range(4):
    elementos=int(input("Introduzca un numero: "))
    numeros.append(elementos)
    if numeros[i]>mayor:
        mayor=numeros[i]
    elif numeros[i]<menor:
        menor=numeros[i]
print("El mayor es %s y el menor es %s " %(mayor,menor))    
    

    