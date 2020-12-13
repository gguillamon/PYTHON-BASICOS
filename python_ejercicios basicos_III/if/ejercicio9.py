#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

num1=int(input("Introduzca el primer numero:"))
num2=int(input("Introduzca el segundo numero:"))
num3=int(input("Introduzca el tercer numero:"))

if num1 > num2 and num2 > num3:
    print(num1)
    print(num2)
    print(num3)
elif num2 > num3 and num3 > num1:
    print(num2)
    print(num3)
    print(num1)
else:
    print(num3)
    print(num2)
    print(num1)           
