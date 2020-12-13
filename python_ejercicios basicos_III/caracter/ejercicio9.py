# Realizar un programa que compruebe si una cadena contiene una subcadena. 
# Las dos cadenas se introducen por teclado.
cadena=input("Introduce un texto: ")
subcadena=input("Introduce palabra: ")
acumulador=0

if subcadena in cadena:
    
    print("Ha introducido la palabra",subcadena,"y se encuentra en el texto")
else:
    print("No se ha encontrado la palabra en el texto")