# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno
#  (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, 
# la nota más alta que ha sacado y la menor.

notas=[]
while len(notas) != 5:
    valor=int(input("Introduzca la nota: "))
    if int(valor) > 0 and int(valor) < 10:
        notas.append(valor)
    else:
        print("valor erroneo, puntacion de 0 a 10")
        
print("Las notas son ", notas,"y la media es ",sum(notas)/len(notas),"la nota mas alta es ",max(notas),"y la menor es ",min(notas))