# 1.- Escribir un programa que pida tres números enteros por teclado y determine el mayor y el
# menor de los tres números. Ejemplo:
# Introduzca el primer número: 20
# Introduzca el segundo número: 34
# Introduzca el tercer número: -18
# Mayor número: 34
# Menor número: -18

num=[2]
mayor=0
menor=0
for i in range(3):
    valor=int(input("Ingrese un numero: "))
    num.append(valor)
    if num[i]>mayor:
        mayor=num[i]
    elif num[i]<menor:
        menor=num[i]
    else:
        print("Son iguales")
print("El mayor es %d y el menor es %d " % (mayor,menor))