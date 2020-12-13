unidades = {'0': 'cero', '1': 'uno', '2': 'dos', '3': 'tres', '4': 'cuatro', '5': 'cinco', '6': 'seis',
            '7': 'siete', '8': 'ocho', '9': 'nueve'}
decenas={'10': 'diez', '11': 'once', '12': 'doce', '13': 'trece', '14': 'catorce', '15': 'quince', '16': 'dieciseis',
         '17': 'diecisiete', '18': 'dieciocho', '19': 'diecinueve', '20': 'veinte'}
conectores={'2': 'veinti', '3': 'treinta', '4': 'cuarenta', '5': 'cincuenta', '6': 'sesenta', '7': 'setenta',
        '8':'ochenta', '9': 'noventa'}

numero = input("Introduzca un numero entre 0 y 100: ")
if int(numero) >= 0 or numero <= int(100):
    aux = ''
    if numero in unidades: # 0 a 9
        aux = unidades[numero]
    elif numero in decenas: # 10 a 20
        aux = decenas[numero]
    elif numero[0] in conectores and numero[1] == "0":
        aux = conectores[numero]
    elif numero[0] in conectores and numero[1] in unidades:
        aux = conectores[numero[0]]
        aux += ' y ' + unidades[numero[1]]
    else:
        aux = 'cien'

if len(aux) > 0:
    print(f'El numero introducido es el {aux}')
else:
    print('Numero fuera de rango')
