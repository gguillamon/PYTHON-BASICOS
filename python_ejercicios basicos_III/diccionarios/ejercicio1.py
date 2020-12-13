# Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas claves
#  sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves. 

numero=int(input("Introduzca un numero"))
diccionario={}

for clave in range(1,numero+1):
    diccionario[clave]= clave ** 2
for clave,valor in diccionario.items():
    print("%d --> %d " % (clave,valor))
    