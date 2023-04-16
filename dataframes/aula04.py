import pandas as pd
import numpy as np

#Visualizando dataframes

datas = pd.date_range('20230416', periods=60, freq='D') 

df = pd.DataFrame(np.random.randn(60,5), index=datas, columns= list("ABCDE"))
#obter apenas as 2 primeiras linhas
df.head(2)

#obter apenas as 2 ultimas
df.tail(2)

#indexes
# print(df.index)

#colunas
colunas = df.columns

# print(colunas)

#transformar os dados em um array
array_dados = df.to_numpy()
# print(array_dados)

#tranforma coluna em linha e linha em coluna
# print(df.T)

