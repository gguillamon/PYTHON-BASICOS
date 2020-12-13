# Una empresa tiene el registro de las horas que trabaja diariamente
# un empleado durante la semana (seis días) y requiere determinar el total de éstas,
# así como el sueldo que recibirá por las horas trabajadas. 

precioHora=float(input("Introduzca el precio por hora: "))
totalHoras=0
SumaSueldo=0
for dia in range(1,7):
    horas=int(input("Introduzca las horas del dia %d : " % dia))
    totalHoras+=horas
    sueldo=horas*precioHora
    SumaSueldo+=sueldo
    print("Usted cobrará %.2f €  por trabajar %.2f horas en el dia %d con un total de %.2f horas y un sueldo de %.2f euros" % (sueldo,horas,dia,totalHoras,SumaSueldo))
if horas == 0:
    print("dato erroneo") 