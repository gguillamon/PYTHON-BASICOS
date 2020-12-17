# 8.- Escribir un programa que “dibuje” un mes del calendario. El programa recibirá como entrada el
# número de días del mes y el día de la semana del primer día del mes. Ejemplo:
# Número de días del mes: 31
# Día 1 es (0 lunes, 6 domingo): 4
#  L M X J V S D
#  1 2 3
#  4 5 6 7 8 9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31
dias = int(input("Número de días del mes:"))
primer_dia = int(input("Día 1 es (0 lunes, 6 domingo):"))

# preparamos impresion
mes = [[], [], [], [], []]
dia_mes = 1
for i in mes: #i = semana
    for ds in range(0, 7):#rango semana
        if ds < primer_dia and i == mes[0] or dia_mes > dias:
            i.append('  ')#agrega dos espacios por cada posicion
        else:
            if len(str(dia_mes)) == 1: #cuadra el dia cuando solo tiene 1 caracter
                aux = ' ' + str(dia_mes)
            else:
                aux = str(dia_mes)
            i.append(aux)
            dia_mes += 1

# imprimimos
print(' L  M  X  J  V  S  D')
for i in mes:
    for j in i:
        print(j+' ', end='')#imprime x semana
    print()#hace el salto