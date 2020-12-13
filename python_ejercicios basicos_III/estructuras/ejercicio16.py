#ejercicio que calcula el tiempo que tardarán dos puntos a diferentes
#velocidades en encontrarse

distancia=int(input("Introduzca la distancia en km:"))
velCoche1=int(input("Introduzca la velocidad del primer coche(km/h):"))
velCoche2=int(input("Introduzca la velocidad del segundo coche(km/h):"))
tiempo=distancia/(velCoche2-velCoche1)*60
print("El coche tardará en alcanzarlo",tiempo,"minutos")
