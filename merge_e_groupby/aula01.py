import pandas as pd

#cadastro loja A
cadastro_a = {
    "ID": ['AA2930', 'BB4563', 'CC2139', 'DE2521', 'GT3462', 'HH1158'],
    "NOME": ['Angelo', 'Cadu', 'Diego', 'Nicole', 'Gabriel', 'Caio'],
    'SOBRENOME':['Carnevale', 'Barbosa','Castan', 'Siqueira', 'Bonaretti', 'Tawfiq'],
    'IDADE': [17,18,18,5,18,18],
}

cadastro_a = pd.DataFrame(cadastro_a, columns=['ID', 'NOME', 'SOBRENOME','IDADE'])

#Cadastro loja B
cadastro_b = {
    "ID": ['CC9999', 'EF4488', 'DD1234', 'GT3462', 'HH1158'],
    "NOME": ['Pedro', 'Daniel', 'Diego', 'Gabriel', 'Higor'],
    'SOBRENOME':['Ramos', 'Souza','Alencar', 'Batista', 'Gonçalves'],
    'IDADE': [19,18,18,18,18],
}

cadastro_b = pd.DataFrame(cadastro_b, columns=['ID', 'NOME', 'SOBRENOME','IDADE'])


compras = {
    'ID': ['AA2930', 'BB4563', 'CC2139', 'DE2521', 'GT3462','AA2930', 'HH1158','HH1158'],
    'DATA': ['2023-04-12', '2023-02-25', '2023-01-05', '2023-03-26', '2023-01-24', '2022-12-29', '2022-02-15', '2023-01-18'],
    'VALOR': [155,350,589,456,185,892,596,12]
}

compras = pd.DataFrame(compras, columns=['ID','DATA','VALOR'], index=range(1,len(compras['ID']) + 1))
print(compras)

# pd.merge(tabela_da_esquerda, tabela_da_direita, on="coluna_coincidente", how='left|right|inner|outer')

#inner join => duas tabelas, interseção dos dados

#full join => juntas os dados das duas tabelas

#left join => apenas informações da tebela da esquerda

#right join => apenas dados da tabela direita
