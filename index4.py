'''
EJERCICIO 1: PIEDRA, PAPEL 
O TIJERA (YAN KEN PO) 
'''
import random

def yan_ken_po():
    opciones= ["piedra","tijera","papel"]
    victorias_jugador=0
    victorias_compu= 0
    print("Welcome a los juegos")
    while True:
        jugador= input("Ingresa PIEDRA/PAPEL/TIJERA/SALIR: ")
        if jugador == 'salir':
            print("Gracias por jugar")  
            break          
        if jugador not in opciones:
            print("Opción inválida")
            continue
        
        computadora= random.choice(opciones)
        print(f"La computadore eligió {computadora}")
        if jugador == computadora:
            print("Empate!!!!!!!!!!!")
        elif (jugador=="piedra" and computadora=="tijera") or \
            (jugador=="papel" and computadora=="piedra") or \
            (jugador=="tijera" and computadora=="papel"):
            print("Ganasteeeeee!!")
            victorias_jugador+=1
        else:
            print("Perdisteeee :(")
            victorias_compu+=1


yan_ken_po()