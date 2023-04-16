import pandas as pd
import numpy as np


datas = pd.date_range('20230416', periods=60, freq='D') 

df = pd.DataFrame(np.random.randn(60,5), index=datas, columns= list("ABCDE"))
# print(df)
print(df.shape)

#####adicionar uma nova coluna:

df['F'] = 1

print(df.head())

df['G'] = [i for i in range(60)]

print(df.tail())

df['Produto'] = df['A'] * df['B']

print(df.tail())  
