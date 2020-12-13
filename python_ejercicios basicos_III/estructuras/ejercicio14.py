#ejercicio que obtiene numero invertido 

numero=int(input("introduzca un numero:"))
primeraCifra=numero//10
Segundacifra=numero%10
print("El numero invertido es: %d%d" % (Segundacifra,primeraCifra))