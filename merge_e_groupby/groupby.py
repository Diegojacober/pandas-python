import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': ['verdadeiro', 'falso','verdadeiro', 'falso','verdadeiro', 'falso','verdadeiro', 'falso'],
    'B': ['um', 'um', 'dois','tres', 'dois', 'dois','um', 'tres'],
    'C': np.random.randn(8),
    'D': np.random.randn(8)})

#soma de todos valores contendo falso
print(df)

#agrupar pela coluna A e somar as categorias em relação a coluna A
soma_de_todos_valores = df.groupby(['A']).sum()
print(soma_de_todos_valores)

# media = df.groupby(['A']).mean()

soma_de_todos_valores_b = df.groupby(['B']).sum()
print(soma_de_todos_valores_b)

soma_de_todos_valores_ab = df.groupby(['A','B']).sum()
print(soma_de_todos_valores_ab)