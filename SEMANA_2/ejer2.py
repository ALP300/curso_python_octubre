'''
Búsqueda avanzada de elementos:
Crea un array de objetos con productos 
(nombre, categoría, precio). Solicita una
categoría y muestra todos los productos
de esa categoría ordenados por precio.
'''
import math
num= 49
pi=3.1416
print(math.pi)
print(math.sqrt(num))
print(math.pow(5,8))

def busquedad():
    productos=[
        {"nombre":"Laptop","categoria":"Electrónicos","precio":1500},
        {"nombre":"Mouse","categoria":"Electrónicos","precio":500},
        {"nombre":"Celular","categoria":"Electrónicos","precio":1200},
        {"nombre":"Polo","categoria":"Ropa","precio":200},
        {"nombre":"Short","categoria":"Ropa","precio":100},
        {"nombre":"zapatillas","categoria":"Calzado","precio":100},
    ]
    
    categoria= input("Por favor, ingresa la categoria: ")
    filtrados= [p for p in productos if p["categoria"].lower()==categoria.lower()]
    filtrado_ordenado= sorted(filtrados, key=lambda x:x["precio"]) 
    print(filtrado_ordenado)
    for p in filtrado_ordenado:
        print(f"{p["nombre"]} - {p["precio"]}")

busquedad()
    