#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente.
#Pueden ocurrir tres cosas:
#El exponente sea positivo, sólo tienes que imprimir la potencia.
#El exponente sea 0, el resultado es 1.
#El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

base=int(input("Introduzca un numero de base: "))
exp=int(input("Introduzca un numero como exponente: "))

potencia= base ** exp

if exp > 0:
    print("la potencia es", potencia)
elif exp == 0:
    potencia = 1
    print("la potencia es",potencia)
elif exp < 0:
    potencia= 1//potencia
    print("La potencia es",potencia)        