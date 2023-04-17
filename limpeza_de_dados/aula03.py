import pandas as pd
import numpy as np

datas = pd.date_range('20230417', periods=6)

df = pd.DataFrame(np.random.randn(6,5), index=datas, columns=list('ABCDE'))

#Missing values, NaN

#gerar coluna F
df['F'] = df.A[df.A > 0]

df2 = df.copy()

df3 = df2.copy()


#remova todos os elementos que tem NaN (a linha inteira)
df2.dropna()


#substituir NA por
#medias das colunas
#df3.coluna_desejada, sem a coluna substituiria todos os NaN
print(df3.F.fillna(np.mean(df3.A)))

df4 = df.copy()

print(df4.fillna(value=0))