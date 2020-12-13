# Escribir un programa que imprima todos los números pares
# entre dos números que se le pidan al usuario.
num1=int(input("Numero uno: "))
num2=int(input("Numero dos: "))
# resto=num1%num2
for i in range(num1,num2): 
    if i % 2 == 0:
        print(i,end=" ")
        

    
  
