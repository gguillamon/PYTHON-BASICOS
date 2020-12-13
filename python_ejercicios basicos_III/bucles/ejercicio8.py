# Escribe un programa que pida el limite inferior y superior de un intervalo.
#  Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
# A continuación se van introduciendo números hasta que introduzcamos el 0. 
# Cuando termine el programa dará las siguientes informaciones:
# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuantos números están fuera del intervalo.
# He informa si hemos introducido algún número igual a los límites del intervalo.

limiteInferior=int(input("Introduzca el limite inferior: "))
limiteSuperior=int(input("Introduzca el limiete superior: "))
acumulador=0
fuera=0

while True:
    if limiteInferior > limiteSuperior:
        print("El limite inferior debe ser mas bajo")
        limiteInferior=int(input("Introduzca el limite inferior: "))
    valor=int(input("Introduzca numeros:")) 
    if valor == limiteInferior: 
        print("ha introducido el valor igual al limite inferior")  
    elif valor == limiteSuperior:   
        print("ha introducido el valor igual al limite superior")  
    if valor == 0:
        break
    elif valor >= limiteInferior and valor <= limiteSuperior:
        acumulador+=1 
    else:
        fuera+=1
        
print("Ha conseguido ",acumulador,"numeros dentro del intervalo y ",fuera,"numeros están fuera")                
