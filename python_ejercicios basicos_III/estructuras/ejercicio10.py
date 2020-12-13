#Ejercicio que calcula mediante la suma de porcentajes el total de una nota

nota1=float(input("Introduce la 1ª nota:")) 
nota2=float(input("Introduce la 2ª nota:")) 
nota3=float(input("Introduce la 3ª nota:"))
trabajoFinal=float(input("Nota trabajo final:"))
promedio=(nota1+nota2+nota3)/3
criterio1=promedio*0.55
criterio2=nota3*0.30
criterio3=trabajoFinal*0.15
NotaFinal=criterio1+criterio2+criterio3
print("La nota final del curso es: %.2f" % NotaFinal)