# 5.- Los empleados de una fábrica trabajan en dos turnos: diurno y nocturno. Escribir un programa
# que calcule el sueldo bruto mensual en euros a partir de los siguientes datos:
# • Días trabajados.
# • Días festivos trabajados.
# • Turno: mañana, tarde, noche.
# ... con las siguientes restricciones:
# • Un día tiene 8 horas laborales.
# • Las horas de un día normal se pagan a 12 €, las horas de un día festivo se pagan a 24€.
# • Un trabajador en un mes, sólo puede trabajar en un turno y 8 horas al día.
# • Los meses son de 30 días.
# • El turno de noche se paga un 20% más que los turnos de mañana y tarde.
# Ejemplo:
# Días trabajados: 22
# Días festivos trabajados: 5
# Turno (M-mañana, T-tarde, N-noche): M
# Sueldo: 3072 euros

DiasTrabajados=int(input("Dias trabajados: "))
DiasFestivos=int(input("Dias festivos trabajados: "))
Turno=input("Introduce Turno de trabajo: (M-mañana, T-tarde, N-noche) :")

diastotales=DiasTrabajados-DiasFestivos
horas=DiasTrabajados*8*12
horasFes=DiasFestivos*8*24
if Turno=="N":
    sueldo=(horas*2.4)+horasFes
    
else:
    sueldo=horas+horasFes
    

print("Días trabajados: %d\nDías festivos trabajados: %d\nTurno (M-mañana, T-tarde, N-noche): %s\nSueldo: %.2f euros" %(DiasTrabajados,DiasFestivos,Turno, sueldo))



