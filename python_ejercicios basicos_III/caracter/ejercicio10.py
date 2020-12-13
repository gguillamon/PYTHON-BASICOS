# Introducir una cadena de caracteres e indicar si es un palíndromo.
#  Una palabra palíndroma es aquella
#  que se lee igual adelante que atrás.

PALABRA=input("Introduzca una palabra:")
vuelta=PALABRA[::-1]
if PALABRA == vuelta:
    print("Es un palíndromo")
    print(PALABRA,vuelta)
else:
    print("No es un palíndromo")