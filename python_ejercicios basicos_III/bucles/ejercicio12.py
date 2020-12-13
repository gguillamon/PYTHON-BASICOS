# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, 
# si al final de cada mes deposita cantidades variables de dinero; además, 
# se quiere saber cuánto lleva ahorrado cada mes. 

ahorroMes=0


for mes in range(1,13):
    cantidad=float(input("Introduzca la cantidad del mes %d : " % mes))
    porcentaje=cantidad*0.10
    ahorroMes+=porcentaje
    print("Va a ahorrar este mes ",mes," %.2f €" % porcentaje)
    print("Ha conseguido ahorrar  hasta hoy %.2f "% ahorroMes)

   