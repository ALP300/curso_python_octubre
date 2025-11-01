'''
Inventario de Tienda
Crea un sistema de inventario 
donde puedas agregar,
actualizar y eliminar productos.
'''
inventario={
    "manzana": {'precio':2, 'cantidad':50},
    "piña": {'precio':5, 'cantidad':40},
    "fresa": {'precio':2, 'cantidad':20},
    "uva": {'precio':3, 'cantidad':10},
}
inventario["papaya"]= {'precio':10, 'cantidad':3}
inventario['manzana']['cantidad']+=20
valor_total= sum(item["precio"]*item["cantidad"] for item in inventario.values())
print(f"El valor total: {valor_total}")