#CONDICIONALES
'''
Escribe un programa que solicite al usuario un número entero y calcule
si es divisible por 3 y por 5.
'''
n= int(input("Por favor, ingresa el número: "))
if n%3==0 and n%5==0:
    print("El número es divisible por 3 y no 5")
else:
    print("El número no es divisible")