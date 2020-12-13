#12-EJERCICIO- Escribe un programa que calcule lo que se tarda en llegar a un sitio dada la velocidad y distancia
print("PROGRAMA--¿Cuanto tardo en llegar?")
destino=input("¿A donde vamos?")
v=int(input("a la velocidad en km/h de :"))
e=float(input("¿Te sabes la distancia en km? "))
tiempo=e/v
tiempo2=e/(v+20)
print(" A %d tardarías %.2f horas " % (v,tiempo))
print(" A %d km/h tardarías %.2f horas , mejor ir mas despacio y llegar bien a %s"% (v+20,tiempo2,destino))
