
# Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores),
#  y posterior ordene los elementos de menor a mayor.
import random

lista=[random.randint(0,100)for x in range(10)]

print(sorted(lista))
