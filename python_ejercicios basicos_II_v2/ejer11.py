nota1 = float(input('Nota del alumno 1: '))
nota2 = float(input('Nota del alumno 2: '))
nota3 = float(input('Nota del alumno 3: '))
nota4 = float(input('Nota del alumno 4: '))
nota5 = float(input('Nota del alumno 5: '))
aprobados = 0
suspensos = 0
if nota1 >= 5:
    aprobados += 1
else:
    suspensos += 1
if nota2 >= 5:
    aprobados += 1
else:
    suspensos += 1
if nota3 >= 5:
    aprobados += 1
else:
    suspensos += 1
if nota4 >= 5:
    aprobados += 1
else:
    suspensos += 1
if nota5 >= 5:
    aprobados += 1
else:
    suspensos += 1


media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print(f'Aprobados: {aprobados}')
print(f'Suspensos: {suspensos}')
print(f'Nota media: {media}')