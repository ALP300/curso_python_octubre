'''
Escribir un programa que cree un diccionario 
simulando una cesta de la compra. El programa 
debe preguntar el artículo y su precio y añadir
el par al diccionario, hasta que el usuario 
decida terminar. Después se debe mostrar por 
pantalla la lista de la compra y el coste total,
con el siguiente formato

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste
'''


cesta={'pera':2.4,'manzana':3.1}
continuar= True
while continuar:
    item= input("Por favor , ingrese el artículo: ")
    precio= float(input("Por favor, ingresa el precio: ")) 
    cesta[item]= precio
    continuar=input("Quieres añadir más artículos (Sí/No)? ")=="Sí"

coste=0
print('Lista de la compra')
for item,precio in cesta.items():
    print(item , '\t' , precio)
    coste+=precio
print("Coste Total ", coste)
    