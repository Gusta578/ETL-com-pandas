import pandas as pd
import datetime as dt
from database import engine

# Vou fazer um ETL simples para práticar meus conhecimentos com Pandas e dados

# Extrai os dados de um Arquivo CSV, "E" da sigla ETL
df = pd.read_csv("C:\\xampp\\htdocs\\mini projeto RH itau\\funcionarios.csv")

# Filtrei só os ativos
df_ativos = df[df['ativo'] == True].copy()

# Aqui fiz uma coluna nova chamada idade, "T" de Transform da sigla ETL
hoje = pd.to_datetime('today')
df_ativos['data_nascimento'] = pd.to_datetime(df['data_nascimento'])
df_ativos['idade'] = hoje.year - df_ativos['data_nascimento'].dt.year

df_ativos = df_ativos.sort_values(by='salario', ascending=False )

# Aqui vou fechar a sigla com o LOAD "L", vou carregar os dados para meu banco de dados.

df_ativos.to_sql('funcionarios_ativos', con=engine, if_exists='replace', index=False)