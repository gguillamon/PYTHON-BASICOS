#Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar 
# un dado de seis caras y muestre por pantalla el número en letras (dato cadena) 
# de la cara opuesta al resultado obtenido.
#Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
#Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje:
#“ERROR: número incorrecto.”.

num=int(input("Introduzca un numero entre 6 para mostrar cara opuesta: "))

if num == 1:
    print("seis")
elif num == 6:
    print("uno")
elif num == 2:
    print("cinco")
elif num == 5:
    print("dos")
elif num == 3:
    print("cuatro")
elif num == 4:
    print("tres") 
else:
    print("ERROR: número incorrecto.")                       