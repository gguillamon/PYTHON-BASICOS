#Algoritmo que pida números hasta que se introduzca un cero.
#Debe imprimir la suma y la media de todos los números introducidos.

num=int(input("Introduzca un numero, para salir pulse 0: "))
contador=0
acumulador=0
while num != 0:
    acumulador=acumulador+num
    contador+=1
    media=acumulador/contador
    num=int(input("Introduzca un numero, para salir pulse 0: "))
print("La suma de los numeros introducidos es",acumulador,", y la media es",media,)       
    