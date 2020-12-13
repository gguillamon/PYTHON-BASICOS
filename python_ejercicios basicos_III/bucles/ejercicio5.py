# Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario,
#  el programa termina cuando se introduce un espacio.

vocal=input("Introduzca un caracter en minusculas: ")
while True:
    if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
        print("VOCAL")
    elif vocal == " ":
        print("Programa terminado")    
    else:
        print("NO VOCAL")
vocal=input("Introduzca un caracter en minusculas: ")      