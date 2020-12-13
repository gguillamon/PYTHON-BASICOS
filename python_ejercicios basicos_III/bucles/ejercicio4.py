# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).
# El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

num=input("Introduzca numeros o 's' para salir:")

contador1=0
contador2=0
contador3=0

sumacontadores=contador1+contador2+contador3
while num != 's':
    if int(num) > 0:
        contador1+=1
    elif int(num) < 0:
        contador2+=1
    elif int(num) == 0:
        contador3+=1   
    else:
        print("Introduzca un valor valido.")                
    num=input("Introduzca numeros o enter para salir:")
       

print("Hay",contador1,"numeros mayores de 0,",contador2,"menores de cero, y",contador3, "ceros.")        