# Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. 
# El programa nos dará el siguiente menú:
# Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente,
#  permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. 
# Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
# Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
# Listar: Nos muestra todos los contactos de la agenda.
# Implementar el programa con un diccionario.

agenda={"Jose":222222,"Paco":333333,"Pepe":111111}
while True:
    print("-------------MENU------------")
    print("-------Ingresa OPCION--------")
    print()
    print("1.Añadir/Modificar ")
    print("2.Buscar nombre")
    print("3.Buscar nombre y borrar")
    print("4.listar agenda")
    print("7.Salir")
    opcion=(input())
    
    if opcion == "1":
        nombre=input("Ingrese un nombre: ")
        for nombres,telf in agenda.items():
            if nombre in agenda:
                print(telf,"--Este es el telf del nombre introducido")
                preg_modif=input("¿Desea modificarlo?s/n")
                if preg_modif == "s":
                    agenda.update((input("Introduzca nuevo telf: ",telf)))
                elif preg_modif == "n":
                    break
                else:
                    print("Telefono desconocido")    
    elif opcion == "2":
        nombre=(input("Introduzca un nombre: "))
        if nombre in agenda:
            print(agenda[nombre])
        else:
            print("No existe contacto con esa letra")
    elif opcion == "3":
        nombre=(input("Introduzca un nombre: "))
        if nombre in agenda:
            eliminar=input("Si desea conservarlo pulse 0 si desea eliminarlo 5")
            if eliminar == "5":
                nombre=agenda.update("")
            elif eliminar == "0":
                print("el registro se conserva en la agenda")
        else:
            print("El nombre introducido no se encuentra en la agenda")
    elif opcion == "4":
        print(nombres,telf)
    elif opcion == "7":
        break

    
        
    



        

