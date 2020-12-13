# Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
# La temperatura media de cada día
# Los días con menos temperatura
# Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella.
#  si no existe ningún día se muestra un mensaje de información.
total=0
dia=1
dias=[]
temperaturas=[]
while len(dias) < 5:
    temperaturas=int(input("Introduzca la tempreratura : "))
    dias.append(temperaturas)
    dia+=1
    total+=temperaturas
print("La temperatura media es de ",total/5)
print("La temperatura máxima alcanzada ha sido de %d grados y el día con menos temperatura ha sido de %d grados" % (max(dias),min(dias)))
temp=int(input("Introduzca la temperatura de comprobacion de datos: "))
if temp == max(dias):
    print("la temperatura de %d coincide con la registrada de %d en el dia %d " % (temp,max(dias),dia))
else:
    print("No existe ningun dia donde se haya registrado esa temperatura.")