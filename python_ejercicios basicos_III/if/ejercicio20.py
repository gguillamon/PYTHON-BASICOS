# Una compañía de transporte internacional tiene servicio en algunos países de América del Norte,
#  América Central, América del Sur, Europa y Asia. 
# El costo por el servicio de transporte se basa en el peso del paquete y
#  la zona a la que va dirigido. Lo anterior se muestra en la tabla:
# Zona
# Ubicación
# Costo/gramo
# 1
# América del Norte
# 24.00 euros
# 2
# América Central
# 20.00 euros
# 3
# América del Sur
# 21.00 euros
# 4
# Europa
# 10.00 euros
# 5
# Asia
# 18.00 euros
# Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, 
# esto por cuestiones de logística y de seguridad.
# Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso,
#  el rechazo de la entrega.

lugarEnvio=float(input("Introduzca el lugar donde quiere enviar: "))
peso=float(input("Introduzca el peso en kg: "))

if peso <= 5:
        if lugarEnvio == 1:
                print("El precio del envio es de 24.00€")
        elif lugarEnvio == 2:
                print("El precio del envio es de 20.00€")
        elif lugarEnvio == 3:
                print("El precio del envio es de 21.00€")
        elif lugarEnvio == 4:
                print("El precio de envio es de 10.00€")
        elif lugarEnvio == 5:
                print("El precio de su envio es de 18.00€")
else:
        print("Peso superior al permitido")    

        #comprobar if anidados



