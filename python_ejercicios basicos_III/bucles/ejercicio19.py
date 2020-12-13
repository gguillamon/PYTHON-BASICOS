# Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta
#  que seleccionamos la opción de “Salir”.

while True:
    print("---------MENU PARA ESCOGER UNA OPCION---------")
    print("1.Contacto")
    print("2.Quienes somos")
    print("3.Fotografias")
    print("4.Agenda")
    print("5.salir")
    opcion=int(input("Introduzca una opcion: "))
    if opcion == 1:
        print("ha elegido contacto")
    elif opcion == 2:
        print("ha elegido Quienes somos")
    elif opcion == 3:
        print("ha elegido Fotografias")
    elif opcion == 4:
        print("ha elegido Agenda")
    elif opcion == 5:
        print("PROGRAMA TERMINADO")
        break
    else:
        print("opcion no valida")
            
