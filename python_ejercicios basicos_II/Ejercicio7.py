# 7.- Escribir un programa que dada una fecha en el formato DIA/MES/AÑO, diga si la fecha es
# correcta o incorrecta. Si la fecha es correcta el programa debe escribirla con el formato DIA de
# MES de AÑO. Ejemplo:
# Introduzca una fecha: 24/12/2004
# La fecha es 24 de diciembre de 2004
# Ejemplo:
# Introduzca una fecha: 31/02/2003
# La fecha es incorrecta

dias_mes = [31, 28, 31, 30,31, 30, 31, 31, 30, 31, 30, 31]
meses=["Enero" ,"Febrero" ,"Marzo" ,"Abril" ,"Mayo" , "Junio", "julio", "Agosto","Septiembre", "Octubre","Noviembre","Diciembre"]
d=int(input("Introduzca dia:"))
m=int(input("Introduzca mes:"))
a=int(input("Introduzca año:"))

m -= 1 
if((a%4 == 0 and a%100 != 0) or a%400 == 0):
    dias_mes[1] += 1
elif(m < 1 or m > 12):
    print("La fecha es incorrecta")
    #Comprobar que el dia sea valido
   
elif(d <= 0 or d > dias_mes[m]):
    print("La fecha es incorrecta")
else:
    print("la fecha es valida")
    print("La fecha es %d de %s de %d" %(d,meses[m],a))

 
 
