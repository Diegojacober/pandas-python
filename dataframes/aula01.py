#para python dataframe é um objeto

import pandas as pd
import numpy as np

#dados coletados em uma escala temporal => series
series = pd.Series([7, 3, 2, 5, 10, np.nan])

# print(series)
# print(type(series))

#como obter datas
# ano mes dia
#freq se varia os dias, meses, horas ou anos
datas = pd.date_range('20230415', periods=6, freq='D') 
print(datas)

