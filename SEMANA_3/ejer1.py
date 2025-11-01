import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos= {'Nombre': ['Ana', 'N/A', 'Carlos', 'Marta', 'Lucia', 'Javier', 'Sofia', 'Diego', 'Elena', 'Miguel'],
        'Edad': ['23', '45', '12', '12','28','34', np.nan, '36', '29', '41'],
        'Sexo': ['F', 'M', 'M', 'F', 'F', 'M', 'F', 'M', 'F', 'M'],  
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Bilbao', 'Granada', 'Zaragoza', 'Malaga', 'Murcia', 'Valladolid'],
        'Calificaciones': [8.5, 7.0, 9.0, 6.5, 8.0, 7.5, 9.5, 6.0, 8.0, 7.0]}    
        
df= pd.DataFrame(datos)
print(df.head())
print(df)
print('\n'*10)
print(df.describe())
nuevo=df.replace(np.nan, '0')
nuevo['Edad']= nuevo['Edad'].astype(int)
print(nuevo)

nuevo.info()