#La política de cobro de una compañía telefónica es:
#cuando se realiza una llamada, el cobro es por el tiempo que ésta dura,
#de tal forma que los primeros cinco minutos cuestan 1 euro
#, los siguientes tres, 80 céntimos, los siguientes dos minutos, 
#70 céntimos, y a partir del décimo minuto, 50 céntimos.
#Además, se carga un impuesto de 3 % cuando es domingo,
#y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %.
#Realice un algoritmo para determinar cuánto debe pagar por cada concepto
#una persona que realiza una llamada. 

llamada=float(input("Introduzca el tiempo de duracion de la llamada en minutos: "))
turno=input("Introduzca \"m\" para indicar mañana o \"t\" para indicar tarde: ")
dia=input("Introduzca el dia de la semana: ") 
precio=1

if llamada <= 5:
        precio
elif llamada > 5 and llamada <= 8:
        precio=precio+0.80
elif llamada > 8 and llamada <= 10:
        precio=precio+0.50
else:
        print("datos introducidos erroneos")
if dia == "Domingo":
        porcentaje=precio+(precio*0.03)
elif dia != "Domingo" and turno == "m":
        porcentaje=precio+(precio*0.15)
elif dia != "Domingo" and turno == "t":
        porcentaje=precio+(precio*0.10)                        

print("Deberá pagar %.2f por esta llamada" % porcentaje)

#NO da el resultado correcto repasar 