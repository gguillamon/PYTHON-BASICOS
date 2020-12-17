# 3.- Programa que lee notas de los alumnos y dice cuántos están aprobados y cuál es la nota
# media. El programa dejará de pedir notas, cuando se pulse la tecla ENTER.
# Introduzca las notas, ENTER para terminar:
# Nota del alumno 1: 5.60
# Nota del alumno 2: 4.20
# Nota del alumno 3: 8.35
# Nota del alumno 4: 7.23
# Nota del alumno 5: 5.01
# Nota del alumno 6: (pulsamos ENTER)
# Número de alumnos: 5
# Aprobados: 4
# Suspensos: 1
# # Nota media: 6.08
#Gabriel Guillamon
print('Introduzca las notas, ENTER para terminar')

suma=0
aprobados = 0
suspensos = 0
i=0
salir = False
while not salir:
    i+=1
    nota = input(f'Nota del alumno {i}: ')
    if nota != '':
        notaInteger = float(nota)
        suma += notaInteger
        if notaInteger >= 5:
            aprobados += 1
        else:
            suspensos += 1
    else:
        salir = True



print(f"Numero de alumnos:{i-1}\nAprobados:{aprobados}\nSuspensos:{suspensos}\nNota media:{(suma)/i}")    