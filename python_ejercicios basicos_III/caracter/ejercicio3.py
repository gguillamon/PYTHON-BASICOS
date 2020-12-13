# Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces
#  aparece el carácter en la cadena.
cadena=input("Introduzca un texto: ")
caracter=input("Introduzca un caracter: ")

if caracter.isalpha() != True:
    print("Error.Introduzca un caracter")
else:    
    print("Es un caracter y está contenido en el texto ",cadena.count(caracter),"veces")