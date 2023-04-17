import pandas as pd
import numpy as np

datas = pd.date_range('20230417', periods=600, freq="D")

df = pd.DataFrame(np.random.randn(600,5), index=datas, columns=list('ABCDE'))

#valores de uma linha
print(df.iloc[155])
#linhas, colunas
print(df.iloc[150:155, 0:2])

#apenas posições especificas
print(df.iloc[[1,5,6], [0,2,4]])