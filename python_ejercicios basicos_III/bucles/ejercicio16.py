# Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

import os
import time
for horas in range(0,24):
    for minutos in range(0,60):
        for segundos in range(0,60):
            os.system("clear")
            print(horas,":",minutos,":",segundos)
		    time.sleep(1)