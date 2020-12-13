
importe = float(input("Importe total: "))
if importe < 20:
    descuento = importe * 0.1
    print(f'Descuento: {descuento} (10%)')
else:
    descuento = importe * 0.2
    print(f'Descuento: {descuento} (20%)')

importeTotal = importe - descuento
print(f'Importe tras descuento: {importeTotal} euros')