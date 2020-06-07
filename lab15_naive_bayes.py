# Title     : Naive Bayes
# Objective : Conhecer os recursos que a linguagem Python tem a nos oferecer para trabalharmos com Calssificação
# Created by: accol
# Created on: 04/06/2020


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from yellowbrick.classifier import ConfusionMatrix


# Trabalharemos com a já conhecida base de dados Cred.csv e vamos explorar o Algoritmo de Classificação Naïve Bayes
credito = pd.read_csv('D:/Users/Angelo/AULAS/Dados/credit.csv')
# Fazendo uma rápida inspeção nos dados
print('\nA dimensão da nossa base é: ', credito.shape)
print('\nOs primeiros registro da nossa base são\n', credito.head())
print('\nUm resumo da nossa base é visto a seguir\n', credito.describe())
# Primeiramente vamos definir duas varíaveis -> a primeira com os atributos previsores (20) e a segunda com o atributo classificados (1 => Class "good" or "bad"). Usaremos o método .values para já converter na nossa variável para um array numpy
previsores = credito.iloc[:, 0:20]
print('\nConferindo o tipo de nossa variável previsores: ', previsores.head())
previsores = credito.iloc[:, 0:20].values
print('\nConferindo o tipo de nossa variável: ', type(previsores))
classe = credito.iloc[:,20].values
# Observe que essa biblioteca (GaussianNB) não trabalha com dados categóricos -> requisito importante para nosso classificador, sendo assim, faremos o import de uma nova biblioteca => LabelEncoder
# Criaremos uma variável do tipo LabelEncoder
labelencoder = LabelEncoder()
# Atenção será necessário trabalhar para cada atributo categórico de sua base de dados
print('\nComo exemplo, vamos transformar o primeiro atributo categórico de nossa base')
previsores[:, 0] = labelencoder.fit_transform(previsores[:, 0])
print(previsores[:, 0])
# Vamos agora trabalhar todos os atributos categóricos de nossa base
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 2])
previsores[:, 3] = labelencoder.fit_transform(previsores[:, 3])
previsores[:, 5] = labelencoder.fit_transform(previsores[:, 5])
previsores[:, 6] = labelencoder.fit_transform(previsores[:, 6])
previsores[:, 8] = labelencoder.fit_transform(previsores[:, 8])
previsores[:, 9] = labelencoder.fit_transform(previsores[:, 9])
previsores[:, 11] = labelencoder.fit_transform(previsores[:, 11])
previsores[:, 13] = labelencoder.fit_transform(previsores[:, 13])
previsores[:, 14] = labelencoder.fit_transform(previsores[:, 14])
previsores[:, 16] = labelencoder.fit_transform(previsores[:, 16])
previsores[:, 18] = labelencoder.fit_transform(previsores[:, 18])
previsores[:, 19] = labelencoder.fit_transform(previsores[:, 19])
print('\nVamos observar o primeiro registro apenas para inspecionar a transformação:\n', previsores[0])
# Nosso próximo passo será criarmos as varíaveis de treino e teste -> para na sequência trabalharmos com o Algoritmo Naïve Bayes => usaremos random_state=0 para fixar e tornar repetível os resultados desse laboratório. Obsrve que craiamos a variável X_treinamento e a variável de resposta y_treinamento e assim por diante
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size=0.3, random_state=0)
print('\nVamos observar nossas variáveis criadas\n')
print('\nX_treinamento\n', X_treinamento)
print('\nX_teste\n', X_teste)
# <$> Até fizemos o tratamento necessário dos dados <$>
# Vamos agora criar um objeto do tipo Naïve Bayes
naive_bayes = GaussianNB()
# Vamos agora fazer o treinamento de nosso objeto
naive_bayes.fit(X_treinamento, y_treinamento)
# A partir daqui estamos prontos para fazer as previsões -> usaremos a variável X_teste
previsoes = naive_bayes.predict(X_teste)
print('\nVamos conferir nosso previsor\n', previsoes)
print('\nA dimensão de nosso previsor é: ', previsoes.shape)
# Observe que nosso previsor usará o nosso modelo treinado para encontrar a classe "good" or "bad"
# Para avaliar a qualidade de nosso previsor devemos comparar com nossa variável y_teste que contém os dados históicos para estes 300 registros. Para visualizarmos a qualidade de nossos resultados vamo precisar de um novoimport => confusion_matrix e accuracy_score
print('\nVamos iniciar criando a matriz de confusão \n')
confusao = confusion_matrix(y_teste, previsoes)
print(confusao)
taxa_acerto = accuracy_score(y_teste, previsoes)
print('\nVamos agora calular a taxa de acerto de nosso previsor: ', round(taxa_acerto * 100, 2), '%')
taxa_erro = 1 - taxa_acerto
print('\nVamos agora calular a taxa de erro de nosso previsor:   ', round(taxa_erro * 100, 2), '%')
# Para melhorar a visão de nossa matriz de confusão precisaremos de uma nova biblioteca -> yellowbrick
# Observe que teremos que reconstruir o que foi feito anteriormente -> na prática você poderá optar por um ou outro método
v = ConfusionMatrix(GaussianNB())
v.fit(X_treinamento, y_treinamento)
v.score(X_teste, y_teste)
print('\nVamos agora fazer uma inspeção visual em nossa nova Matriz de Confusão \n')
v.poof()
# <$> Vamos agora levar nosso modelo para o ambiente de produção Simulando com registros novos => usaremos nossa base NovoCredit.csv que contém apenas um registro <$>
# Vamos precisar ler nosso arquivo e formatá-lo usando o .values
novo_credito = pd.read_csv('D:/Users/Angelo/AULAS/Dados/NovoCredit.csv')
novo_credito = novo_credito.iloc[:, 0: 20].values
# Lembre-se que deverá tratar seus dados e deixá-los todos no mesmo formato do modelo. Precisamos agora trabalhar todos os atributos categóricos de nossa base
novo_credito[:, 0] = labelencoder.fit_transform(novo_credito[:, 0])
novo_credito[:, 2] = labelencoder.fit_transform(novo_credito[:, 2])
novo_credito[:, 3] = labelencoder.fit_transform(novo_credito[:, 3])
novo_credito[:, 5] = labelencoder.fit_transform(novo_credito[:, 5])
novo_credito[:, 6] = labelencoder.fit_transform(novo_credito[:, 6])
novo_credito[:, 8] = labelencoder.fit_transform(novo_credito[:, 8])
novo_credito[:, 9] = labelencoder.fit_transform(novo_credito[:, 9])
novo_credito[:, 11] = labelencoder.fit_transform(novo_credito[:, 11])
novo_credito[:, 13] = labelencoder.fit_transform(novo_credito[:, 13])
novo_credito[:, 14] = labelencoder.fit_transform(novo_credito[:, 14])
novo_credito[:, 16] = labelencoder.fit_transform(novo_credito[:, 16])
novo_credito[:, 18] = labelencoder.fit_transform(novo_credito[:, 18])
novo_credito[:, 19] = labelencoder.fit_transform(novo_credito[:, 19])
print('\nVamos a uma rápida inspeção se tudo está ok\n', novo_credito)
# Agora vamos avaliar se esse novo cliente será um bom ou mal pagador
novo = naive_bayes.predict(novo_credito)
print('\nO novo cliente foi classificado como: ', novo)
# Assim, o algoritmo recomenda que se conceda o crédito!
