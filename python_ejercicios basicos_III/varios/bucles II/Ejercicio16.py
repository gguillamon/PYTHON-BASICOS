# 16.- Escribir un programa para que dada una cantidad de euros la devuelva en el menor número
# de billetes y monedas de curso legal posible (billetes: 500 €, 200 €, 100 €, 50 €, 20 €, 10 € y 5€.
# Monedas: 2 €, 1 €. Ejemplo:
# Introduzca una cantidad: 2343
# 3
# 4 billetes de 500
# 1 billete de 200
# 1 billete de 100
# 2 billetes de 20
# 1 moneda de 2
# 1 moneda de 1
#Gabriel Guillamon

cantidad = int(input('Introduzca una cantidad: '))
euros = {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

for valor in euros.keys():
    euros[valor] = cantidad // valor
    cantidad = euros % valor

for valor in euros.keys():
    if euros[valor] != 0:
        if valor >= 5:
            texto = 'billete'
        else:
            texto = 'moneda'
        if euros[valor] > 1:
            texto += 's'
        print(f'{euros[valor]} {texto} de {valor}')