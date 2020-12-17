# 10.- Escribir un programa que tome 100 números aleatorios entre 0 y 99. A continuación debe
# mostrar cuántos números están comprendidos en los intervalos [0-19], [20-39], [40-59], [60-79] y
# [80-99]. Ejemplo:
# [ 0-19]: 12
# [20-39]: 34
# [40-59]: 20
# [60-79]: 15
# [80-99]: 19
# Total: 100
#Gabriel Guillamon

import random
rango1 = 0  # 0-19
rango2 = 0  # 20-39
rango3 = 0  # 40-59
rango4 = 0  # 60-79
rango5 = 0  # 80-99

for j in range(0, 100):
    i = random.randint(0, 99)
    if i in range(0, 20):
        rango1 += 1
    elif i in range(20, 40):
        rango2 += 1
    elif i in range(40, 60):
        rango3 += 1
    elif i in range(60, 80):
        rango4 += 1
    else:
        rango5 += 1

print(f'[ 0-19]: {rango1}')
print(f'[20-39]: {rango2}')
print(f'[40-59]: {rango3}')
print(f'[60-79]: {rango4}')
print(f'[80-99]: {rango5}')
print(f'Total: {rango1 + rango2 + rango3 + rango4 + rango5}')
