#descobrir se são dados unicos
import pandas as pd
import numpy as np

datas = pd.date_range('20230417', periods=6)

df = pd.DataFrame(np.random.randn(6,4), index=datas, columns=['Var_A', 'Var_B', 'Var_C', 'Var_D'])

df2 = pd.DataFrame({
    'A': 1,
    'B': pd.Timestamp('20230125'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'E': pd.Categorical(['test','train', 'test', 'train']),
    'F': 'Python',
    'G': [2,2,4,4],
    'H': [np.nan,2,4,np.nan]})

print(df2)
#axis=0 -> linha, axis = 1 -> coluna, dropna -> se nan conta como um valor unico ou não
print(df2.nunique(axis=0, dropna=False))