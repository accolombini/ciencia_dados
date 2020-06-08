# Title     : Features Scalling => DIMENSIONAMENTO DE CARACTERÍSTICAS
# Objective : Como a linguagem R pode nos apoiar nos trabalhos de tratamento de dados usando Feature Scalling
# Created by: accol
# Created on: 08/06/2020


import pandas as pd 
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.compose import make_column_transformer


# Para esse laboratório trabalharemos com o conjunto de dados Credit.csv
# Inicalmente vamos visualizar os dados sem qualquer transformação
dataset = pd.read_csv('D:/Users/Angelo/AULAS/Dados/Credit.csv')
print('\nObservando nosso conjunto de Dados sem qualquer transformação')
print('\n', dataset.head())
print('\nA dimensão da nossa base é: ', dataset.shape)


# Como vamos trabalhar com Feature Scalling => queremos trabalhar com variáeveis numéricas -> vamos neste laboratório trabalhar com 3 colunas => duration [1], credit_amount [4] e allment_commit [7]
# Nosso primeiro passo é separar os atributos (variáveis) de nosso interesse
dt = dataset.iloc[:, [1, 4, 7]].values
print('\nVamos observar nossa variável criada\n', dt)
print('\nA dimensão de dt -> criada é: ', dt.shape)

# Primeiramente vamos fazer a padronização
sc = StandardScaler()
x = sc.fit_transform(dt)
print('\nVamos observar nossa variável x após aplicação da transformação\n', x)
print('\nA dimensão de x -> transformada é: ', x.shape)
print('\nObserve que x apresenta como resultado as variáveis padronizadas, com média igual a zero e desvio padrão igual a 1\n')

# Agora faremos a normalização entre 0 e 1 usando  NORMALIZAÇÃO (MIN-MAX)
sc = MinMaxScaler()
y = sc.fit_transform(dt)
print('\nVamos observar nossa variável y após aplicação da normalização\n', y)
print('\nA dimensão de y -> transformada é: ', y.shape)
print('\nObserve que y apresenta como resultado as variáveis normalizadas, com valores variando entre 0 e 1\n')
