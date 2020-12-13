# Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) 
# y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. 
# Para simplificarlo vamos a suponer que febrero tiene 28 días.

mes=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
usuario=int(input("Introduzca el numero de mes: "))

if mes[usuario-1] == "Enero" or mes[usuario-1] == "Marzo" or mes[usuario-1] == "Mayo" or mes[usuario-1] == "Julio" or mes[usuario-1] == "Agosto" or mes[usuario-1] == "Octubre" or mes[usuario-1] == "Diciembre":
    print( mes[usuario -1],"tiene 31 dias")
elif mes[usuario-1] == "Abril" or "Junio" or "Septiembre" or "Noviembre":
    print(mes[usuario-1],"tiene 30 dias")
elif mes[usuario-1] == "Febrero":
    print(mes[usuario-1],"tiene 28 dias")


