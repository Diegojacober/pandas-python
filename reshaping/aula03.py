import pandas as pd

Carros = [7, 4, 3, 2, 8]
dias = pd.date_range('20230416','20230416', periods=5)
vendedor = ['George', 'Vagner', 'Pedro', 'Vagner', 'George']

df = pd.DataFrame({'Vendas': Carros, 'Data':dias, 'Vendedor': vendedor})
print(df)


#não funciona com valores repetidos
# print(df.pivot(index='Data', columns='Vendedor',values='Vendas'))

# funciona com os valores repetidos,e faz uma média com os valores repetidos,
# por causa do parametro aggfunc que vem com padrão o valor mean
print(df.pivot_table(index='Data', columns='Vendedor',values='Vendas',aggfunc='mean'))

print(df.pivot_table(index='Data', columns='Vendedor',values='Vendas',aggfunc='sum'))

print(df.pivot_table(index='Data', columns='Vendedor',values='Vendas',aggfunc='min'))

print(df.pivot_table(index='Data', columns='Vendedor',values='Vendas',aggfunc='max'))
