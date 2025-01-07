# Importação de bibliotecas utilizadas /// Importing used libraries
import requests
import pandas as pd
from sqlalchemy import create_engine

# Criação de conexão com banco de dados local (PostgreSQL) /// Creating connection to local database (PostgreSQL)
ENDBD = "postgresql+psycopg2://postgres:postgres123@localhost:5432/teste"

engine = create_engine(ENDBD)

# Definindo as datas para escopo da cotação /// Defining dates to the cotation time period
# "MM-DD-YYYY" - Formato de data /// "MM-DD-YYYY" - Date format
data_inicial = "01-01-2000"
data_final = "12-31-2024"

# Definindo URL de acesso à API do BACEN com variáveis de início e fim do período de cotação /// Defining access URL to BACEN's API with start and end time period variables.
url = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='"+data_inicial+"'&@dataFinalCotacao='"+data_final+"'&$format=json&$select=cotacaoVenda,dataHoraCotacao"

print(url)

# Utilizando o método get da biblioteca requests, acessando a url resultante da API /// Using the get method from the requests library, acessing the resulting API url
r = requests.get(url)

# Recuperando apenas o JSON resultante da API /// Recovering only the resulting JSON from the API
dados = r.json()

# Devido ao formato do JSON resultante da API, retira-se apenas a lista de valores /// Due to the format of the resulting JSON, it is retrieved only the values list
dados_2 = dados["value"]

# Os dados da lista de valores são transpostos para um DataFrame utilizando a biblioteca pandas, e depois a coluna 'dataHoraCotacao' é definida como data através do método to_datetime (anteriormente str) /// The data from the values list are transposed to a DataFrame using the pandas library, and then the column 'dataHoraCotacao' (translated to 'cotationDateHour') is defined as a date using the method to_datetime (previously str)
df_cotacoes = pd.DataFrame(dados_2)
df_cotacoes['dataHoraCotacao'] = pd.to_datetime(df_cotacoes['dataHoraCotacao'])

# Definindo o nome da tabela de destino, sendo esta cotacoes_dolar /// Setting the name of the targeted table, that being cotacoes_dolar
nomeTabela = 'cotacoes_dolar'

# Por fim o DataFrame pronto é inserido na tabela definida /// Lastly the ready DataFrame is inserted in the defined table
df_cotacoes.to_sql(name=nomeTabela, con=engine, if_exists='replace', index=False)

# Parâmetros extra:
# if_exists = define o que acontece se a tabela já possuir conteúdo, neste caso sobrepõe os dados
# index = define se o index (ordenador) será levado a tabela como uma coluna a parte, neste caso não.
# ///
# Extra parameters:
# if_exists = defines what will happen if the table already has content, in this case, it replaces the data.
# index = defines if the index will also appear ont the taple as a column, in this case, it will not.
