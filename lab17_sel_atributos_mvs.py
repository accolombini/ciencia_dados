# Title     : Seleção de Atributos utilizando o algoritmo da Máquina de Vetor de Suporte
# Objective : Avaliar como uma boa seleção de atributos pode contribuir para melhorar a precisão do Classificador
# Created by: accol
# Created on: 05/06/2020

# Entendendo a Maldição da Dimensionalidade
# Vamos usar o mesmo conjunto de dados Credit.csv

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from yellowbrick.classifier import ConfusionMatrix
import graphviz
from sklearn.tree import export_graphviz
from sklearn.ensemble import ExtraTreesClassifier


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
# Nesta prática estaremos usando como algoritmo de classificação a Máquina de Vetor de Suporte -> acompanhe
# Para essa prática precisaremos de novo import SVC
svm = SVC()
svm.fit(X_treinamento, y_treinamento)
previsoes = svm.predict(X_teste)
# Vamos calcular a taxa de acerto e erro
taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1 - taxa_acerto
print('\nA taxa de acerto de nosso algoritmo é de: ', round(taxa_acerto * 100, 2), '%')
print('\nA taxa de erro de nosso algoritmo é   de: ', round(taxa_erro * 100, 2), '%')
# Observe que a precisão deste algoritmos está próxima da precisão do algoritmo Naïve Bayes
# <$> Agora faremos uma seleção dos melhores atributos -> para isso, vamos fazer uma nova importação => ExtraTreesClassifier <$>

forest = ExtraTreesClassifier()
forest.fit(X_treinamento, y_treinamento)
# A variável importancias nos fornecerá os atributos e sua relevância para o processo de classificação
importancias = forest.feature_importances_
print('\nObservando a variável importancias:\n', importancias)
# A partir desse resultado você deverá selecionar os atributos com a maior taxa de contribuição -> Neste lab usaremos os mesmos da aula de R (não vamos olhar para os mais relevantes, mas simpara os primeiros -> você deverá testar outras opções)
# Vamos criar uma nova variável treinamento para estes testes
X_treinamento2 = X_treinamento[:, [0, 1, 2, 3]]
X_teste2 = X_teste[:, [0, 1, 2, 3]]
# Vamos observar as novas variáveis criadas
print('\nA variável X_treinamento2 é:\n', X_treinamento2)
print('\nA variável X_teste2 é:\n', X_teste2)
# Observe que apenas 4 atributos estão presentes
# Agora vamos ao novo previsor
svm2 = SVC()
svm2.fit(X_treinamento2, y_treinamento)
previsoes2 = svm2.predict(X_teste2)
# Vamos calcular a taxa de acerto e erro
taxa_acerto2 = accuracy_score(y_teste, previsoes2)
taxa_erro2 = 1 - taxa_acerto2
print('\nA taxa de acerto2 de nosso algoritmo é de: ', round(taxa_acerto2 * 100, 2), '%')
print('\nA taxa de erro2 de nosso algoritmo é   de: ', round(taxa_erro2 * 100, 2), '%')
# Observe que neste caso a seleção de atributos não resultou em uma melhor precisão, embora a precisão tenha praticamente se mantido obteve-se uma melhor performance no uso dos recursos computacionais
