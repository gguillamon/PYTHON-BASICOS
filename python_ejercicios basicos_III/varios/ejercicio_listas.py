Nombresvocales = []
vocales = ['A', 'E', 'I', 'O', 'U']
Nombres = ['Tamara', 'Marcelo', 'Martin', 'Juan', 'Alberto', 'Exequiel', 'Alejandro', 'Leonel', 'Antonio', 'Omar',
'Antonia', 'Amalia', 'Daniela', 'Sofia', 'Celeste', 'Ramon', 'Jorgelina', 'Anabela']
for nombre in Nombres: #Para el elemento nombre, iteramos la lista Nombres
    if nombre[0] in vocales: #Si el índice 0 del elemento nombre está en la lista vocales
        Nombresvocales.append (nombre)#Agregamos el nombre a la lista Nombresvocales
    

print (Nombresvocales)