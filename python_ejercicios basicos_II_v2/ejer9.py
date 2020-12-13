entrada = input("Introduzca 4 numero separados por espacios: ")
a, b, c, d = entrada.split(' ')
n1 = int(a)
n2 = int(b)
n3 = int(c)
n4 = int(d)
menor = 9999999999
mayor = -9999999999
numeros = [n1, n2, n3, n4]
for i in numeros:
    if i > mayor:
        mayor = i
    elif i < menor:
        menor = i

print(f'El mayor es {mayor} y el menor es {menor}')
