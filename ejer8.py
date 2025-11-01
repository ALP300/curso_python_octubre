import pandas as pd
import numpy as np

datos= pd.read_csv('Data.csv')
print(datos.iloc[7:10])
print(datos.iloc[[0,3,4,5,19,129],])
print(datos.iloc[:,0:2])
print(datos.iloc[[0,3,4,3], [0,3,45]])
print(datos.iloc[3:9,0:2])