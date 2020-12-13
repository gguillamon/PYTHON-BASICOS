# 6.- Una tienda que vende ropa está de rebajas. La tienda ofrece un 10% de descuento para
# compras por un importe por debajo de los 20€. Para compras de 20€ en adelante el descuento es
# del 20%. Escribe un programa que dada la cantidad total de la compra aplique el descuento
# correctamente y muestra la cantidad final.
# Ejemplo:
# Importe total: 18
# Descuento: 1.8 € (10%)
# Importe tras descuento: 16.2 €

importe=float(input("Introduzca importe de la compra:"))
if importe <20:
    descuento=importe*0.1
    total=importe-descuento
else:
    descuento=importe*0.2
    total=importe-descuento

print("Importe: %.2f\nDescuento: %.2f\nImporte tras descuento: %.2f"  % (importe,descuento,total))