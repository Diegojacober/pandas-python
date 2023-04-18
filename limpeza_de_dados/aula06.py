#Ordenar os dados
import pandas as pd
import numpy as np

datas = pd.date_range('20230417', periods=6)

df = pd.DataFrame({
    'Col1': ['A','A','B', np.nan,'D', 'C'],
    'Col2': [2, 1, 9, 8, 7, 4],
    'Col3': [0, 1, 9, 4, 2 ,3]
})

#by -> qual coluna ordenar, axis -> por linha ou por coluna, asc -> crescente
dados_ordenados = df.sort_values(by='Col2', axis=0, ascending=True)

print(dados_ordenados)
