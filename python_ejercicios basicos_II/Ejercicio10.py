# 11.- Programa que lee la nota de 5 alumnos y dice cuántos están aprobados y cuál es la nota
# media. Para este ejercicio no se pueden utilizar bucles.
# Nota del alumno 01: 5.60
# Nota del alumno 02: 4.20
# Nota del alumno 03: 8.35
# Nota del alumno 04: 7.23
# Nota del alumno 05: 5.01
# Aprobados: 4
# Suspensos: 1
# Nota media: 6.08
contadorA=0
contadorS=0
sumaCant=0
notas=[]
alu1=float(input("Nota del alumno 01:"))
notas.append(alu1)
sumaCant+=alu1
alu2=float(input("Nota del alumno 02:"))
notas.append(alu2)
sumaCant+=alu2
alu3=float(input("Nota del alumno 03:"))
notas.append(alu3)
sumaCant+=alu3
alu4=float(input("Nota del alumno 04:"))
notas.append(alu4)
sumaCant+=alu4
alu5=float(input("Nota del alumno 05:"))
notas.append(alu5)
sumaCant+=alu5

for nota in notas:
    if nota < 5:
        contadorS+=1
    else:
        contadorA+=1
        
print("Aprobados: %d\nSuspensos: %d\nNota media: %.2f" % (contadorA,contadorS,sumaCant/5))
