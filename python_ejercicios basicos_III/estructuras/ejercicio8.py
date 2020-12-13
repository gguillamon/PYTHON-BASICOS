#Ejercicio que obtiene el sueldo base mas comisiones de un vendedor

sueldoBase=float(input("Introduzca su sueldo base"))
ventas=float(input("Introduzca el total de ventas acumulado"))
sueldoMes=(ventas*10/100)+sueldoBase
print("El sueldo de este mes es %.2f" % sueldoMes)