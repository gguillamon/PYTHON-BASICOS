# 2.- Estás en un largo viaje en coche, la distancia a la próxima gasolinera es de 200 Km. Escribe un
# programa que preguntando el tamaño del depósito, el % del combustible restante y el consumo,
# muestre si puedes o no llegar a la gasolinera.
# Ejemplo:
# Tamaño del depósito (litros): 50
# % de combustible: 50
# Consumo (l/100 Km): 10
# Puedes recorrer 250 Km más.
# Espera a la próxima gasolinera.

size=int(input("Tamaño del deposito(litros): "))
fuel=int(input(" % de combustible: "))
consumo=int(input("Consumo l/100: "))
recorrer=(size*fuel/100)*consumo
if(recorrer > 200):
    print("Puedes recorrer %d Km mas" % (recorrer))
else:
    print("Echa gasolina!! solo puedes recorrer %d Km mas" % (recorrer))
    