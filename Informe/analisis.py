# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

path = 'FIFA.csv'
lista_fifa = pd.read_csv(path)


"""
Seleccionar los 10 deportistas mejores pagados según el juego de FIFA19
"""

columnas_usar = ['ID','Name', 'Age', 'Nationality', 'Overall', 'Position','Potential', 'Club', 'Value', 'Position', 'Height', 'Weight']
lista_jugadores = pd.read_csv(path, usecols=columnas_usar)

# Los paises que tienen más jugadores dentro del top 100

jugadores = lista_jugadores.head(100)
nacionalidades = jugadores['Nationality'].unique()
cantidad_nacionalidades = np.zeros(nacionalidades.size)

for idNacionalidad, pais in enumerate(nacionalidades):
    cantidad_nacionalidades[idNacionalidad] = jugadores[jugadores['Nationality'] == pais].Name.count()
   
plt.figure(2)
plt.title('Pais que tiene más jugadores en el top 100 en FIFA 19')
plt.xlabel('Paises')
plt.ylabel('Cantidad jugadores')
plt.xticks(rotation=90)
plt.bar(nacionalidades, cantidad_nacionalidades)

# Los arqueros mejores puntuados de la lista de 100

lista_arqueros = pd.DataFrame(jugadores, columns=['Name', 'Overall', 'Position'])
mejores_arqueros = lista_arqueros.sort_values(ascending = [False, False], by = ['Position', 'Overall']).query('Position == "GK"')

print(mejores_arqueros)

# Los 10 mejores jugadores ecuatorianos en el juego de FIFA19

lista_ecuatorianos = pd.DataFrame(lista_jugadores, columns=['Name', 'Overall', 'Club', 'Nationality'])
ecuatorianos_mejor_puntuados = lista_ecuatorianos.sort_values(ascending = [False], by = ['Overall']).query('Nationality == "Ecuador"')
print(ecuatorianos_mejor_puntuados.head(10))
