tamanio = int(input('Tamaño del depósito (litros): '))
porcentajeConbustible = int(input('% de combustible: '))
consumo = float(input('Consumo (l/100 Km): '))


autonomia = tamanio * porcentajeConbustible / 100 / consumo * 100

print(f'Puedes recorrer {autonomia} km más ')
if autonomia > 200:
    print('Espera a la proxima gasolinera')
else:
    print('La gasolinera está a 200km, ¡echa gasolina!!!')
