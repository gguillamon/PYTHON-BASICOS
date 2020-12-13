# """ Realiza un programa que pida el día de la semana (del 1 al 7)
#  y escriba el día correspondiente.
#  Si introducimos otro número nos da un error. """

dia=int(input("Introduzca un dia de la semana en numero: "))

if dia == 1:
    print("LUNES")
elif dia == 2:
    print("MARTES")
elif dia == 3:
    print("MIERCOLES")
elif dia == 4:
    print("JUEVES")
elif dia == 5:
    print("VIERNES")
elif dia == 6:
    print("SABADO")
elif dia == 7:
    print("DOMINGO")
else:
    print("ERROR, INTRODUZCA UN NUMERO DEL 1-7")                      