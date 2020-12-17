# 1.- Programa que lee un número y muestra la tabla de multiplicar de dicho número. Hacer el
# ejercicio de dos formas, con bucle while y con bucle for.
# Número: 8
# 8 x 0 = 0
# 8 x 1 = 8
# 8 x 2 = 16
# 8 x 3 = 24
# 8 x 4 = 32
# 8 x 5 = 40
# 8 x 6 = 48
# 8 x 7 = 56
# 8 x 8 = 64
# 8 x 9 = 72
# 8 x 10 = 80
# numero=int(input("Numero: "))
# suma=0

# while suma < 11:
#     print(" %d x %d = %d" % (numero,suma,numero*suma) )
#     suma+=1
    
#Version con for
numero=int(input("Numero: "))
suma=0

for i in range(10):
    print(" %d x %d = %d" % (numero,suma,numero*suma) )
    suma+=1
    