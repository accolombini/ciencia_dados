# Title     : Árvore de Decisão -> Classificação
# Objective : Conhecer os recursos da linguagem Python para potencializar as aplicações de Machine Learning
# Created by: accol
# Created on: 05/06/2020


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from yellowbrick.classifier import ConfusionMatrix
import graphviz
from sklearn.tree import export_graphviz


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
# Nesta prática estaremos usando como algoritmo de classificação a Árvore de Decisão -> acompanhe
# Vamos precisar instalar um novo pacote para melhor visualizar a árvore de decisão -> graphviz (pip install graphviz)
arvore = DecisionTreeClassifier()
arvore.fit(X_treinamento, y_treinamento)
# Vamos exportar nosso arquivo para visualização com o graphviz -> observe que faremos uso da extensão .dot para nomear nossos arquivos de saída. Você deverá copiar o conteúdo o arquio tree.dot -> acessar o site Webgraphviz e colar o conteúdo do arquivo .dot para visualização do gráfico
export_graphviz(arvore, out_file='tree.dot')
# No site, deverá apagar o código exemplo e colar seu código. Após isso basta clicar em Generate Graph!
# Vamos agora para nosso estágio de previsões
previsoes = arvore.predict(X_teste)
print('\nVamos inspecionar nossa variável previsoes \n', previsoes)
# Feito isso, precisamos agora avaliar o grau de precisão de nosso algoritmo
confusao = confusion_matrix(y_teste, previsoes)
print('\nPodemos agora inspecionar nossa matriz de confusão\n', confusao)
taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1 - taxa_acerto
print('\nA taxa de acerto de nosso previsor é: ', round(taxa_acerto * 100, 2), '%')
print('\nA taxa de erro de nosso previsor   é: ', round(taxa_erro * 100, 2), '%')
# Observe que neste caso a taxa de acerto encontrada é inferior a encontrada pelo algoritmo de Naïve Bayes
# Para praticar vamos melhorar a visualização de nossa matriz de confusão usando a biblioteca yellowbrick
v = ConfusionMatrix(DecisionTreeClassifier())
v.fit(X_treinamento, y_treinamento)
v.score(X_teste, y_teste)
print('\nVamos agora fazer uma inspeção visual em nossa nova Matriz de Confusão \n')
v.poof()
