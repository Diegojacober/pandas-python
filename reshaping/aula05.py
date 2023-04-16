import pandas as pd

df = pd.DataFrame({
    'A': {0: 'a', 1:'b', 2:'c',},
    'B': {0:1, 1:3, 2:5},
    'C': {0:2, 1:4, 2:6}})

print(df)
#dataframe, id de referencia, funcao com os valores de tal coluna
df_melt = pd.melt(df, id_vars=['A'], value_vars=['B'])

#tudo que estiver em A vai estar combinado com B
# print(df_melt)

df_melt = pd.melt(df, id_vars=['A'], value_vars=['B','C'], var_name='Varteste', value_name='Nome do valor')
print(df_melt)