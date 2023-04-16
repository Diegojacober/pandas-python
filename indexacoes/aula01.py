import pandas as pd

arrays = [[1,1,2,2], ['red', 'blue', 'red','blue']]
v = pd.MultiIndex.from_arrays(arrays, names=('numero','cor'))
print(v)