# 4.- Escribir un programa que calcule ecuaciones de segundo grado del tipo ax2+bx+c=0. El
# programa solicitará los coeficientes a, b y c. A continuación mostrará las soluciones.
from math import sqrt
 
a = float(input('Introduzca Valor de a: '))
b = float(input('Introduzca Valor de b: '))
c = float(input('Introduzca Valor de c: '))
if a != 0:
    x1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
    x2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)
    print ('Soluciones de la ecuacion: x1=%4.3f y x2=%4.3f ' % (x1, x2))
else:
    if b != 0:
       x = -c / b
       print ('Solucion de la ecuacion: x=%4.3f ' % (x))
 
    else:
       if c != 0:
          print ('La ecuacion no tiene solucion. ')
 
       else:
          print ('La ecuacion tiene infinitas soluciones. ')
