#.txt -> linha por linha, dados não estruturados, não organizados
#.csv -> mais comum, Comma Separated Values, valores separados por virgulas
#.xslx -> Excel
# https://archive.ics.uci.edu/ml/index.php -> repositório de dados gratuitos

#abrir arquivo de dados externos
import pandas as pd

data = pd.read_csv('importing_exporting/iris.data',sep=',')

print(data.head(5))
print(data.describe())

d1 = pd.read_excel('dados_3.xlsx')

csv_data = d1.to_csv('local_para_ser_salvo/nome.csv')