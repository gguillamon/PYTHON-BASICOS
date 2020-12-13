nota = float(input('Introduce la nota: '))
if 0 <= nota <= 10:
    if nota <5:
        print("Suspenso")
    elif nota <6:
        print("Suficiente")
    elif nota <7:
        print("Bien")
    elif nota < 9:
        print("Notable")
    elif nota < 10:
        print("Sobresaliente")
else:
    print("No es una nota válida...")