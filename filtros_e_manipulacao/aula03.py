import pandas as pd
import numpy as np

datas = pd.date_range('20230417', periods=600, freq="D")

df = pd.DataFrame(np.random.randn(600,5), index=datas, columns=list('ABCDE'))

#toda coluna A, apenas valores maiores que 0
# print(df[df.A > 0])

#de todas as colunas
print(df[df > 0])