#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)
#después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).

Euros2=int(input("Ingrese cuantas monedas de 2 euros tiene:"))
Euros1=int(input("Ingrese cuantas monedas de 1 euro tiene:"))
Euros050=int(input("Ingrese cuantas monedas de 0.50 euros tiene:"))
Euros020=int(input("Ingrese cuantas monedas de 0.20 euros tiene:"))
Euros010=int(input("Ingrese cuantas monedas de 0.10 euros tiene:"))
sumaeu=(Euros2*200)+(Euros1*100)
sumacen=(Euros050*50)+(Euros020*20)+(Euros010*10)
totalsuma=sumaeu+sumacen

print("Tiene un total de %d € y %d centimos en su cartera." % (totalsuma/100,totalsuma%100))
