#Ejercicio que obtiene el valor de una compra final dado un descuento

compra=float(input("Introduzca el valor de la compra:"))
descuento=(compra*15/100)
pagoFinal=compra-descuento
print("El precio con descuento es %.2f €" % pagoFinal)