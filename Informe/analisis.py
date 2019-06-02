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

# Los mejores jugadores ecuatorianos

lista_ecuatorianos = pd.DataFrame(lista_jugadores, columns=['Name', 'Overall', 'Club', 'Nationality'])
ecuatorianos_mejor_puntuados = lista_ecuatorianos.sort_values(ascending = [False], by = ['Overall']).query('Nationality == "Ecuador"')
print(ecuatorianos_mejor_puntuados.head(10))


# personajes_smashito_melee = pd.DataFrame(personajes['Melee']).count()


"""

pokemonDescendenteTotal = pokemons.sort_values(ascending = False, by = 'Total')

print('Pokemons màs poderosos')
print(pokemonDescendenteTotal.loc[:,['Name','Total','Type 1','Generation','Attack', 'Defense']].head(5))
print('Pokemons más debiles')
print(pokemonDescendenteTotal.loc[:,['Name','Total','Type 1','Generation','Attack', 'Defense']].tail(5))

pokemonDescendenteDefense = pokemons.sort_values(ascending = False, by = 'Defense')


plot.figure(2)
plot.bar(universos, numero_personajes_por_universo)
plot.xticks(rotation=90)
plot.xlabel('Universos')
plot.ylabel('No. de personajes por universo')
plot.title('Personajes por universo')



tiposPokemon = pokemons['Type 1'].unique()
cantidadPokemonsXTipo = np.zeros(tiposPokemon.size);
for idx, tipo in enumerate(tiposPokemon):
    cantidadPokemonsXTipo[idx] = pokemons[pokemons['Type 1'] == tipo].Name.count()




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