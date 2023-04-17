import pandas as pd
import numpy as np

datas = pd.date_range('20230417', periods=600, freq="D")

df = pd.DataFrame(np.random.randn(600,5), index=datas, columns=list('ABCDE'))

# print(df.tail(10))

#apenas a coluna D
print(df["D"].head(2))

#linhas especificas
linhas0_4 = df[0:4]
print(linhas0_4)

#colunas especificas de linhas expecificas
colunas_B_C = df.loc[:,['B','C']]
print(colunas_B_C)

#filtro
por_data = df.loc['20230501':'20230601', ['A','E']]
print(len(por_data))