'''
EJERCICIO 2: ADIVINA EL NÚMERO 🎲
'''
import random
def adivina_el_numero():
    numero_secreto= random.randint(1,100)
    intentos=0
    max_intentos=10
    print(f"Tienes {max_intentos} intentos")
    while intentos<max_intentos:
        try:
            intento= int(input(f"Intento {intentos+1}: "))
            intentos+=1
            if intento == numero_secreto:
                print("Eres un grande, felicitaciones, crack, maestro, fiera, mastodonte")
                break
            elif intento<numero_secreto:
                print("El número es más alto")
            else:
                print("El número secreto es más bajo")            
        except ValueError:
            print("Por favor, ingresa un número válido")
            intentos-=1

adivina_el_numero()