#La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva,
#la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, ésta es
#de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque,
#considerando lo siguiente: si es de tipo A,
#se le cargan 20 céntimos al precio inicial cuando es
#de tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2.
#Realice un algoritmo para determinar la ganancia obtenida.

kilosA_Tamano1=float(input("Introduzca los kilos de tipoA1: "))
kilosA_Tamano2=float(input("Introduzca los kilos de tipoA2: "))
kilosB_Tamano1=float(input("Introduzca los kilos de tipoB1: "))
kilosB_Tamano2=float(input("Introduzca los kilos de tipoB1: "))
precio_inicial=float(input("Introduzca precio asociacion vinicultores /KG: "))
PVP=float(input("Introduzca precio venta al público: "))

TA1=precio_inicial + 0.20
TA2 = precio_inicial + 0.30
TB1= precio_inicial - 0.30
TB2= precio_inicial - 0.50


#TOTAL

totalkilos=(kilosA_Tamano1 * TA1)+(kilosA_Tamano2 * TA2)+(kilosB_Tamano1 * TB1)+(kilosB_Tamano2 * TB2)
VentaTotal=totalkilos*PVP
beneficio=VentaTotal-totalkilos

print("Se ha vendido un total de %.2f € y el beneficio obtenido es de %.2f €" % (VentaTotal,beneficio))