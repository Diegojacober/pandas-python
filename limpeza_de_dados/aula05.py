#descobrir se são dados unicos
import pandas as pd
import numpy as np

datas = pd.date_range('20230417', periods=6)

df = pd.DataFrame(np.random.randn(6,4), index=datas, columns=['Var_A', 'Var_B', 'Var_C', 'Var_D'])

df2 = pd.DataFrame({
    'A': 1,
    'B': pd.Timestamp('20230125'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype="int32"),
    'E': pd.Categorical(['test','train', 'test', 'train']),
    'F': 'Python',
    'G': [2,2,4,4],
    'H': [np.nan,2,4,np.nan]})

print(df2)

#remover as duplicatas


#se a linha inteira é duplicada
# df2_sem_duplicatas = df2.drop_duplicates(subset=None)

#analisar uma coluna especifica
#keep -> manter o ultimo duplicado ou o primeiro, ou False-> remove todas duplicatas
df2_sem_duplicatas = df2.drop_duplicates(subset='G', keep='first')


print(df2_sem_duplicatas)