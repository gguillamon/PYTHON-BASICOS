# Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido.
# Cada alumno puede tener distinta cantidad de notas. 
# Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.
# El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo.
# Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos.
# Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.

listaNombres=[]
listaNotas=[]
numalumnos=int(input("Introduzca el numero de alumnos: "))
notas=0
dicnombres={}

for num in range(numalumnos):
    nombre=input("Introduzca nombre")
    while nombre in dicnombres:
        print("El alumno ya existe")
        nombre=input("Introduzca nombre")
    notas=int(input("Introduzca notas del alumno o numero negativo para salir: "))
    while notas > 0:
        listaNotas.append(notas)
        dicnombres[nombre] = str(notas.copy())
        notamedia=sum(notas)/len(listaNotas)
        

for nombres,valores in dicnombres.items():
    print("El alumno %s tiene la nota media de %2f " % nombre,notamedia)
