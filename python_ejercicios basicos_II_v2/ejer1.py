
numeros = []
numeros.append(int(input('Introduzca el primer numero: ')))
numeros.append(int(input('Introduzca el segundo numero: ')))
numeros.append(int(input('Introduzca el tercer numero: ')))
mayor = -99999999999
for num in numeros:
    if num > mayor:
        mayor = num
menor = 99999999999
for num in numeros:
    if num < menor:
        menor = num
print(f'Mayor numero: {mayor}')
print(f'Menor numero: {menor}')