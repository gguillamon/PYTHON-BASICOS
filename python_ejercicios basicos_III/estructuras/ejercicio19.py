#Escribir un algoritmo para calcular la nota final de un estudiante, 
# considerando que: por cada respuesta correcta 5 puntos,
#  por una incorrecta -1 y por respuestas en blanco 0. 
# Imprime el resultado obtenido por el estudiante.

RespCorrect=int(input("Introduzca el numero de respuestas correctas:"))
RespIncorrect=int(input("Introduzca el numero de respuestas incorrectas:"))
RespBlanc=int(input("Introduzca las respuestas en blanco:"))
nota=RespCorrect*5
notaFinal=nota-RespIncorrect
print("la nota final obtenida es de:",notaFinal,"puntos")