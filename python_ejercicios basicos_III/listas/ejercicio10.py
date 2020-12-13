
# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
# Carga la tabla con valores numéricos enteros.
# Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

s = 0
filas=5
columnas=5
tabla=[]

for i in range(filas):
    tabla.append([int(input("Introduzca valores enteros para las filas: "))])
    sumafilas=0
    sumacolumnas=0
    for j in range(columnas):
        tabla[i].append(int(input("Introduzca valores enteros para las columnas: ")))
        sumacolumnas=sumacolumnas+tabla[i][j]*filas
        sumafilas=sumafilas+tabla[i][j]
        

print(str(tabla),str(sumacolumnas),str(sumafilas))