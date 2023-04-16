import pandas as pd
import numpy as np

datas = pd.date_range('20230416', periods=6)

df = pd.DataFrame(np.random.rand(6,4), index=datas, columns=['Var_A','Var_B','Var_C','Var_D'])
# print(df)

#transpor --> Linha vira coluna, coluna vira linha
df_transposto = df.T
# print(df_transposto)

#saber shape (linhas, colunas)
# print(df.shape)

# pegar valores
# print(df_transposto.values)

#linhas x colunas
print(np.size(df_transposto.values))

valores = df_transposto.values

#reorganizar
# tem q ser do tamanho dos dados
print(valores.reshape((8,3)))