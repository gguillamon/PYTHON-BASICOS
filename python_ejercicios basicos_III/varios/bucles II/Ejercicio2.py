# 2.- Escribir un programa que imprima las 10 tablas de multiplicar.

for i in range(1,11) :
    print ("Tabla de multiplicar: ",i)
    for j in range(11):
        print(" %d x %d = %d" % (i,j,i*j) )
        
      