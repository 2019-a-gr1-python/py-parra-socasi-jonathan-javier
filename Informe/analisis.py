# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

path = '/home/dev-05/Desktop/py-parra-socasi-jonathan-javier/Informe/FIFA.csv'
lista_fifa = pd.read_csv(path)


"""
Seleccionar los 10 deportistas mejores pagados según el juego de FIFA19
"""

columnas_usar = ['Name', 'Age', 'Nationality', 'Potential', 'Club', 'Value', 'Position', 'Height', 'Weight']
lista_campos_seleccionados = pd.read_csv(path, usecols=columnas_usar)

jugadores  =lista_campos_seleccionados.head(1000)

nacionalidadJugadores = jugadores['Nationality'].unique()
cantidadPokemonsXTipo = np.zeros(nacionalidadJugadores.size);

print(nacionalidadJugadores, cantidadPokemonsXTipo)

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

columnas_a_usar = ['name','ID','ALIGN','SEX','GSM','ALIVE','APPEARANCES','FIRST APPEARANCE','YEAR']
contenido_archivo = pd.read_csv(
    'dc-data.csv',
    usecols=columnas_a_usar
    )

df_gropu_good = contenido_archivo.groupby("ALIGN")
print(df_gropu_good)
print(type(df_gropu_good))
valores = []
valore = []
for name , df_agrupado in df_gropu_good:    
    valores.append(name)
    valore.append(len(df_agrupado.index))
    

plt.xlabel('En x')
plt.xlabel('En y')
plt.plot(valores,valore)
"""