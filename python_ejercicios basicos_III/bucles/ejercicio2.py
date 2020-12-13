#Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100.
#A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,
#a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número
#(además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado. 
import random
intentos=0
aleatorio=random.randint(1,100)
num=int(input("Ingrese un numero, 0 para salir: "))
while intentos < 10:
    intentos+=1
    if num < aleatorio:
        print("Ingrese un numero mayor:")
    else:
        print("Ingrese un numero menor:") 
    if num == aleatorio:
        print(" Enhorabuena, has acertado!!")
    else:
        num=int(input("Ingrese un numero, 0 para salir: "))  
    if intentos == 10:
        print("Numero de intento superado, pruebe otra vez PAlOYAS")    
print("PROGRAMA TERMINADO")      