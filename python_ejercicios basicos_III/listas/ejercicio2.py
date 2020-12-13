# Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
# Copia los elementos de la lista en otra lista pero en orden inverso,
# y muestra sus elementos por la pantalla.
lista=[]
for x in range(5):
    palabras=input("Introduce una palabra: ")
    lista.append(palabras)
lista2=[] 
lista2=lista
print(lista2[::-1])