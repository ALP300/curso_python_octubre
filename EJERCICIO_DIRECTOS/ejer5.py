'''
Ejercicio 1: Gestión de Estudiantes
Crea un diccionario con nombres de estudiantes 
como claves y sus calificaciones como valores.
Calcula el promedio de calificaciones.
'''
estudiantes={
    'Leonardo': 70,
    'Fabian': 80,
    'Miguel':20,
    'Nick':100,
    'Kriocy':10
}
promedio= sum(estudiantes.values())/len(estudiantes)
mejor= max(estudiantes, key=estudiantes.get)
print(f"El promedio fue de: {promedio}")
print(f"El mejor estudiante {mejor}")