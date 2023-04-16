#para python dataframe é um objeto
import pandas as pd
import numpy as np

datas = pd.date_range('20230415', periods=6, freq='D') 
#dados aleatórios
df = pd.DataFrame(np.random.randn(6,4), index=datas, columns= list("ABCD"))
print(df)

df2 = pd.DataFrame({"A": 7,
                    "B": pd.Timestamp('20230415'),
                    "C": pd.Series(1, index=list(range(4)), dtype='float32') ,
                    "D": np.array([3] * 4, dtype='int32'),
                    "E": pd.Categorical(["test","train","train", "test"]),
                    "F": "Python"}
                   )

print(df2)