'''
9. Búsqueda avanzada de elementos:
Crea un array de objetos con productos 
(nombre, categoría, precio). Solicita una
categoría y muestra todos los productos
de esa categoría ordenados por precio.
'''
def busquedad():
    productos=[
        {"nombre":"Laptop","categoria":"Electrónica","precio":1200},
        {"nombre":"Mouse","categoria":"Electrónica","precio":200},
        {"nombre":"Teclado","categoria":"Electrónica","precio":300},
        {"nombre":"Polo","categoria":"Ropa","precio":300},
        {"nombre":"Pantalón","categoria":"Ropa","precio":400},
    ]
    categoria= input("Ingresa la categoria: ")
    filtrado= [p for p in productos if p["categoria"].lower()==categoria.lower()]
    
    filtrado_ordenado=sorted(filtrado, key=lambda x: x["precio"]) 
    print(filtrado_ordenado)
    for p in filtrado_ordenado:
        print(f"{p["nombre"] - {p["precio"]}}")
busquedad()