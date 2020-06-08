# Title     : Categorical Encoding no Python
# Objective : Conhecer algumas ferramentas que a linguagem Python tem a nos oferecer para trabalharmos com categorical encoding -> transformar dados categoricos em dados numéricos
# Created by: accol
# Created on: 08/06/2020


import pandas as pd 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import make_column_transformer


# Para esse laboratório trabalharemos com o conjunto de dados Credit.csv
# Inicalmente vamos visualizar os dados sem qualquer transformação
dataset = pd.read_csv('D:/Users/Angelo/AULAS/Dados/Credit.csv')
print('\nObservando nosso conjunto de Dados sem qualquer transformação')
print('\n', dataset.head())
print('\nA dimensão da nossa base é: ', dataset.shape)

# Faremos os nossos testes com duas variáveis categóricas => personal_status e other_parties -> índices 8 e 9 de nossa base. Criaremos uma variável X que receberá estas duas colunas -> note o uso do método .values
X = dataset.iloc[:, 8:10].values
print('\nObservando nossa variável X -> antes da transformação')
print('\n', X)
print('\nA dimensão da variável X é: ', X.shape)

# Vamos agora iniciar a transformação da nossa variável X
labelencoder = LabelEncoder()
X[:,0] = labelencoder.fit_transform(X[:, 0])

onehotencoder = make_column_transformer((OneHotEncoder(categories='auto', sparse=False), [1]), remainder='passthrough')
X = onehotencoder.fit_transform(X)
print('\nObservando nossa variável X -> usando OneHotencoder')
print('\n', X)
print('\nA dimensão da variável X é: ', X.shape)
# Só relembrando antes de utilizar esse modelo você deverá excluir uma coluna -> normalmente exclui-se a coluna 0
