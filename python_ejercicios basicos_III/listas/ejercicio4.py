# Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo.
#  Entonces se debe imprimir el vector (sólo los elementos introducidos).
lista=[]
valores=0
while True:
    valores=int(input("Introduzca valores: "))
    if valores > 0 :
        lista.append(valores)
    else:
        break
print(lista)

    
