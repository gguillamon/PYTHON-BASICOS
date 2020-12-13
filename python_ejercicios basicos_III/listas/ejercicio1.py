# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) 
# y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

lista1=[1,3,5,2,8,4,9,6,7,0]

for cuen in lista1:
    lista1.sort()
    print(cuen,cuen ** 2, cuen ** 3)
    