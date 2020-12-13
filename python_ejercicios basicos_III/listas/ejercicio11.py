# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’.
# Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones o elementos que delimitan la tabla,
#  es decir, las más externas, mientras que el resto de los elementos contendrán el valor 0. 
#   111111111111111
#   100000000000001
#   100000000000001
#   100000000000001
#   111111111111111
num_filas=5
num_colum=15

marco=[]
for i in range(0,num_filas):
    fila=[]
    for j in range(0,num_colum):
        if i == 0 or i == num_filas - 1 or j == 0 or j == num_colum - 1 :
            fila.append(1)
        else:
            fila.append(0)
    marco.append(fila)        
for fila in marco:
	for elemento in fila:
		print(elemento," ",end="")
	print()
