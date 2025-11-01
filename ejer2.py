import pandas as pd
import numpy as np

datos= pd.read_csv('Data.csv')
print(datos.info())
print(datos.describe())
nuevo= datos.replace('N/A',"0")
nuevo= datos.replace('NR',"0")
nuevo['Wsets']= nuevo.Wsets.astype(int)
print(nuevo.info())
print(nuevo)