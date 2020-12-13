# Escribe un programa que lea una cadena y devuelva un diccionario 
# con la cantidad de apariciones de cada carácter en la cadena. 

cadena=input("Introduzca una frase: ")
diccionario={}
for caracter in cadena:
    if caracter in diccionario:
        diccionario[caracter]+=1
    else:
        diccionario[caracter]=1
for llave,valor in diccionario.items():
    print(llave,"->",valor)