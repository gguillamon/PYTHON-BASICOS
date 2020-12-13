#programa que muestra cantidad de horas y minutos dado un numero de minutos

minutos=float(input("Introduzca el numero de minutos"))
h, minutos = divmod(minutos, 60)
print ("%d horas y %02d minutos" % (h, minutos))