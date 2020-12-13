#ejercicio que da como resultado la hora de llegada tomando como
#parametros hora de salida y tiempo de tardanza

horapartida = int(input("Hora de salida:"))
minpartida = int(input("Minutos de salida:"))
segpartida = int(input("Segundos de salida:"))
segviaje = int(input("Tiempo que has tardado en segundos:"))
# Convierto la hora de salida a segundos
seginicial = horapartida * 3600 + minpartida*60 + segpartida
# Le sumo los segundos que he tardado
segfinal = seginicial + segviaje
# Convierto los segundos totales a hora, minúto y segundos
horallegada = segfinal // 3600
minllegada = (segfinal % 3600) // 60
segllegada = (segfinal % 3600) % 60
# Muestro la hora de llegada
print("Hora de llegada")
print(horallegada,":",minllegada,":",segllegada)