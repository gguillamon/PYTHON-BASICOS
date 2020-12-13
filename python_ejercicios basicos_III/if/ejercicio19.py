# #Escribe un programa que pida un número entero entre uno y doce e imprima el número de días
# #que tiene el mes correspondiente.
# Podemos hacer la siguiente división para memorizar cuántos días tiene cada mes del año:
#  Meses con 30 días: Abril, Junio, Septiembre y Noviembre. Meses con 31 días: Enero, Marzo,
# Mayo, Julio, Agosto, Octubre y Diciembre. Meses con 28 días: Febrero
# (Menos cuando es bisiesto que tiene 29 días).

num=int(input("Introduzca el numero de mes para saber sus dias: "))

if num == 1 or num == 3 or num == 5 or num == 7 or num == 8 or num == 10 or num == 12:
    print("ESTE MES TIENE 31 DIAS")
elif num == 4 or num == 6 or num == 9 or num == 11:
    print("ESTE MES TIENE 30 DIAS")
elif num == 2:
    print("ESTE MES TIENE 28 DIAS, MENOS CUANDO ES BISIESTO QUE TIENE 29 DIAS") 
else:
    print("Introduzca un numero correcto")           