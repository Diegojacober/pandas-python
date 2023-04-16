import pandas as pd

df = pd.read_csv("reshaping/nba.csv")

# print(df.tail(5))
# print(df.shape)

#Stack -> empilhar a tabela de dados
stack_df = df.stack()

print(stack_df)
#no indice 0 há linhas que antes era colunas, mas agora em apenas uma coluna
#útil para visualizações

unstack_df = stack_df.unstack()
print(unstack_df)