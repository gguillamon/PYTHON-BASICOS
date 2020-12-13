# Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, 
# pida valores para ‘lista1’ y ‘lista2
# ’ y calcule lista3=lista1+lista2.
lista1=[]
lista2=[]
lista3=[]
for i in range(5):
    i=lista1.append(int(input("Introduzca los valores de la lista 1: ")))
for j in range(5):
    j=lista2.append(int(input("Introduzca los valores de la lista 2: ")))
lista3=lista1+lista2
print(lista3)
