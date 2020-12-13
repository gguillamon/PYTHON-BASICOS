dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre",
         "Diciembre"]

fecha = input("Introduzca la fecha (dd/mm/yyyy): ")
dia, mes, anio = fecha.split("/")
diaInt = int(dia)
mesInt = int(mes)
mesInt -= 1
anioInt = int(anio)
correcta = False

if (anioInt % 4 == 0 and anioInt % 100 != 0) or anioInt % 400 == 0:
    dias_meses[1] += 1
    correcta = True
elif mesInt < 0 or mesInt > 12:
    print("La fecha es incorrecta")
elif diaInt <= 0 or diaInt > dias_meses[mesInt]:
    print("La fecha es incorrecta")

if correcta:
    print(f"La fecha es {diaInt} de {meses[mesInt]} de {anioInt}")
