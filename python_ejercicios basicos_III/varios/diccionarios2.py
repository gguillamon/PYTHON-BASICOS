# 4. Suponga un diccionario que contiene como clave el nombre de una persona y como valor
# una lista con todas sus “gustos”. Desarrolle un programa que agregue “gustos” a la persona:
# Si la persona no existe la agregue al diccionario con una lista que contiene un solo elemento.
# Si la persona existe y el gusto existe en su lista, no tiene ningún efecto.
# Si la persona existe y el gusto no existe en su lista, agrega el gusto a la lista.
# Se deja de pedir personas cuando introducimos el carácter “*”.

lista_gustos=[]
nombres = []
personas = {'nombre': nombres, 'gusto': lista_gustos}

while(personas[1].values() != "*"):
    lista_gustos.append(personas[nombres])
print(nombres,lista_gustos)
    
