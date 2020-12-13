# 8.- Escribir un programa que pida un número comprendido entre 0 y 100. A continuación debe
# escribir el número “con letra”.
# Introduzca un número entre 0 y 100: 38
# El número introducido es el treinta y ocho.
unidades={'0':'cero','1':'uno','2':'dos','3':'tres','4':'cuatro','5':'cinco','6':'seis','7':'siete','8':'ocho','9':'nueve'}
decenas={'10':'diez','11':'once','12':'doce','13':'trece','14':'catorce','15':'quince','16':'dieciseis','17':'diecisiete','18':'dieciocho','19':'diecinueve'}
siguientes={'2':'veinti','3':'treinta','4':'cuarenta','5':'cincuenta','6':'sesenta','7':'setenta','8':'ochenta','9':'noventa'}

num=(input("Introduzca un numero entre 0 y 100: "))
if int(num) > 0 or int(num) <= 100:
    if num in unidades:
        conver=unidades[num]
        print("El numero introducido es el %s " %(conver))
    elif num in decenas:
        conver=decenas[num]
        print("El numero introducido es el %s " %(conver))
    elif num[0] in siguientes and num[1] == "0":
        conver=siguientes[num]
        print("El numero introducido es el %s " %(conver))
    elif num[0] in siguientes and num[1] in unidades:
        conver=siguientes[num[0]]
        conver2=unidades[num[1]] 
        print("El numero introducido es el %s y %s" %(conver,conver2))
    else:
        print("El numero introducido es cien")
else:
    print("Numero fuera de rango")

    

        