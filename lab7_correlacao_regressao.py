# Title     : CORRELACAO -> REGRESSÃO LINEAR SIMPLES
# Objective : Conhecer o que Python tem a nos oferecer para trabalhar com CORRELAÇÃO
# E REGRESSÃO LINEAR SIMPLES
# Created by: accol
# Created on: 27/05/2020

# Vamos usar o Banco de Dados cars.csv -> queremos saber a distância percorrida pelo carro, a partir do momento da frenagem


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot


# Carregando a base de dados cars.csv
base = pd.read_csv('D://Users/Angelo/AULAS/Dados/cars.csv')
print('\nVisualizando a base de trabalho')
print(base)
# Note que existe um atributo indesejado (Unnamed:0) >- vamos apagar esse atributo -> observe o uso do axis = 1 >- sinalizando que queremos apagar por coluna (toda coluna)
base = base.drop(['Unnamed: 0'], axis = 1)
print('\nVisualizando a base de trabalho sem a coluna Unnamed: 0')
print(base)
print('\nVisualizando a base de trabalho: ')
print(base.head())
print('\nVisualizando a base de trabalho: ')
print(base.describe())
print('\nVisualizando a base de trabalho: ')
print(type(base))
print('\nVisualizando a base de trabalho: ')
print(base.shape)
# Nosso objetivo é procurar prever a velocidade que o carro estava tendo por base a distância que ele levou para parar >- Note que a variável velocidade será nossa variável independente (causa) >- Distância em pés e velocidade em milhas variável dependente (efeito)
# Como primeiro passo queremos encontrar a correlação
# Para nossos trabalhos vamos criar duas variáveis x e y >- requisitos para a função que utilizaremos para o cálculo da correlação requer
# X será nossa variável independente (causa) -> distância
X = base.iloc[:, 1].values # .values para já transformar nossa variável X em um array numpy
X = X.reshape(-1, 1)
print('\nNossa variável X -> independente (causa) distância')
print(X)
print('\nNossa variável X -> independente (causa) distância')
print(X.shape)
# y será nossa variável dependente (efeito) -> distância
y = base.iloc[:, 0].values # .values para já transformar nossa variável X em um array numpy
print('\nNossa variável y -> dependente (efeito) velocidade')
print(y)
# Cáclulo do coefiente de Correlação -> observe
#correlacao = np.corrcoef(X, y)
#print('\nO coeficinete de correlação entre X e y é: \n', correlacao)
# Note que temos uma correlação forte entre X e y >- podemos aplicar o modelo de Regressão para fazermos previsão
# Precisamos criar o modelo para nossa análise
modelo = LinearRegression()
# Para fazermos o treinamento do modelo usaremos o método fit() >- note que o método fit() exige que seus argumentos estejam no formato numpy array e no formato de matriz -> daí o uso de .values e do reshape(-1, 1)
modelo.fit(X, y)
# Podemos agora visualizar algumas informações -> observe a seguir
modelo.intercept_
print('\nPonto de interceptação: ', modelo.intercept_)
# Podemos também visualizar o coeficiente de inclinação -> observe
modelo.coef_
print('\nCoeficiente: ', modelo.coef_)
# Inspeção visual
plt.scatter(X, y)
# Adicionando a linha de melhor ajuste
plt.plot(X, modelo.predict(X), color='red')
plt.show()
# Fazendo a previsão considerando deslocamento igual a 22 pés
print('\nPrevendo velocidade para 22 pés de deslocamento: ', modelo.intercept_ + modelo.coef_ * 22)
# Uma forma mais direta para fazer a previsão é:
print('\nNossa variável X é do tipo: ', type(X))

# Vamos olhar um pouco para os Residuos
print('\nOs Residuos são: \n', modelo._residues)
# Inspeção visual nos residuos
visualizador = ResidualsPlot(modelo)
visualizador.fit(X, y)
visualizador.poof()
