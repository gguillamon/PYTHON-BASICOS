# Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. 
# El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir 
# de los datos guardados en el diccionario. Si la fruta no existe nos dará un error.
#  Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

precios={"manzana":1,"melon":2,"melocotón":3}

while True:
    fruta=input("Introduzca la fruta: ")
    if fruta.lower() in precios:
        cantidad = int(input("Dime la cantidad de frutas que has vendido:"))
        print(fruta,"cantidad= ",cantidad*precios[fruta],"euros") 
    elif fruta not in precios:
        print("No se disponen de regitros para la fruta introducida")
        mas=input("¿Desea introducir mas productos?s/n")
    elif mas == "s":
        break
    elif mas == "n":
        exit()
         
