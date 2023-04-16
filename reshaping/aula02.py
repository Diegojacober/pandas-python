import pandas as pd
import numpy as np

dias = pd.date_range('20230416', periods=12, freq="D")

Pessoas = ['Diego', 'Ana', 'Bianca', 'Janete']

Nomes = []
Gastos = []
for i in range(12):
    Nomes.append(np.random.choice(Pessoas))
    Gastos.append(np.round(np.random.rand() * 100, 2))
    
# print(Nomes)
# print(Gastos)

#Agrupar em um dataframe

df = pd.DataFrame({'Dia': dias, 'Nome': Nomes, 'Gastos': Gastos})

# Reshape data (produce a “pivot” table) based on column values.
# Uses unique values from specified index / columns to form axes of the resulting DataFrame.
# This function does not support data aggregation, multiple values will result in a MultiIndex in the columns.


df_pivot = df.pivot(index='Dia',columns='Nome', values='Gastos')
print(df_pivot)

#Gastos totais
somas = df.groupby(['Nome'])['Gastos'].sum()
print(somas.sort_values())