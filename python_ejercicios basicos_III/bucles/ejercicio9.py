# Escribe un programa que dados dos números, uno real (base) y un entero positivo
#  (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.

base=int(input("Introduza la base: "))
exponente=int(input("Introduzca el exponente: "))
potencia=1

for i in range(1,exponente+1):
    potencia*=base
print(potencia)


