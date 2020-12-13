dTrabajados = int(input("Dias trabajados: "))
dFestivos = int(input("Dias festivos trabajados: "))
turno = input("Turno de trabajo: (M-mañana, T-tarde, N-noche) :")

diastotales = dTrabajados - dFestivos

horasNormalesEuros = dTrabajados * 8 * 12
horasFestivasEuros = dFestivos * 8 * 24
sueldo = horasFestivasEuros + horasNormalesEuros
if turno == "N":
    sueldo *= 1.2

print(f'Sueldo: {sueldo} euros.')
