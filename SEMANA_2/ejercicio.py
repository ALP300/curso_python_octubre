'''
Inversión y manipulación de arrays:
Crea un array de palabras. Muestra el array original, 
luego uno con los elementos invertidos, 
y otro con cada palabra en mayúsculas si tiene más de 5 letras.

'''



def invertir():
    palabras= ["Agentina","Brazil","Chile","Mexico","Peru"]
    invertido= palabras [::-1]
    print(palabras)
    print(invertido)
    
    mayusculas= [palabra.upper() if len(palabra)>5 else palabra for palabra in palabras]
    print(mayusculas)
    
invertir()

