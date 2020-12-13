# Realizar una algoritmo que muestre la tabla de multiplicar de un número 
# introducido por teclado.
num=int(input("Introduzca un numero: "))

for i in range(1,10):
    print(num,"x",i,"=",num*i)