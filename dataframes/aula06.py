import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    'A': ['A1','A2','A3','A4'],
    'B': ['B1','B2','B3','B4'],
    'C': ['C1','C2','C3','C4'],
    'D': ['D1','D2','D3','D4']
}, index=range(4))

df2 = pd.DataFrame({
    'A': ['A5','A6','A7','A8'],
    'B': ['B5','B6','B7','B8'],
    'C': ['C5','C6','C7','C8'],
    'D': ['D5','D6','D7','D8']
}, index=[4,5,6,7])

df3 = pd.DataFrame({
    'E': ['E1','E2','E3','E4'],
    'F': ['F1','F2','F3','F4'],
    'G': ['G1','G2','G3','G4'],
    'H': ['H1','H2','H3','H4']
}, index=range(4))


grupo = pd.concat([df1,df2], keys=['dataframe1','dataframe2'])

# print(grupo['A'])

# print(grupo.loc['dataframe2']['B'])

g2 = df1.append(df2)

