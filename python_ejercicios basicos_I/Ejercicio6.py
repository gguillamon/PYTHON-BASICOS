#Ejercicio 6- Realiza un programa que valide la entrada y muestre mensaje, con la condicion mayor que 10 menor 
# que 99 y muestra mensajes
num=input("Introduce un numero de dos cifras: ")
inversion=num[1]+num[0]

if num > 99:
     print("Numero {} no me sirve, debe ser menor o igual que 99".format(num))
    
elif num < 10:
    print("Numero {} no me sirve, debe ser igual o mayor que 10".format(num))
else:
    print("Numero correcto, entra en el rango: ",inversion )
   
