import pandas as pd
import numpy as np

datas = pd.date_range('20230417', periods=6)

df = pd.DataFrame(np.random.randn(6,4), index=datas, columns=['Var_A', 'Var_B', 'Var_C', 'Var_D'])

df2 = pd.DataFrame({
    'A': 1,
    'B': pd.Timestamp('20230125'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'E': pd.Categorical(['test','train', 'test', 'train']),
    'F': 'Python'})

# print(df)
# print(df2)
print(df2.describe())
df1 = df.reindex(index=datas[0:4], columns=list(df.columns) + ['Var_E'])
print(df1)

df1.loc[datas[0]:datas[1],'Var_E'] = 1
print(df1)