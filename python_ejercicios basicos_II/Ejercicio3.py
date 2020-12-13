# 3.- Escribe un programa que dada una nota numérica entre 0 y 10 con dos decimales, diga la nota
# literal que tiene el alumno. Suponiendo:
# Sobresaliente: nota en el intervalo [9, 10]
# Notable: nota en el intervalo [7, 9)
# Bien: nota en el intervalo [6, 7)
# Suficiente: nota en el intervalo [5, 6)
# Suspenso: nota en el intervalo [0, 5)
# Introduzca la nota: 8.35

nota=float(input("Introduzca la nota: "))
if nota > 0 < 10:
    if nota < 10:
        print("sobresaliente:",nota)
    elif nota < 9:
        print("notable:",nota)
    elif nota <7:
        print("bien : ",nota)
    elif nota <6:
        print("suficiente",nota)
else:
    print("Debe introducir una nota entre 0 y 10")