# Title     : AGRUPAMENTOS -> USANDO K-MEANS
# Objective : Conhecer como a linguagem Python pode nos apoiar nos processos de classificação -> explorando nesta prática o algoritmoK-MEANS
# Created by: accol
# Created on: 08/06/2020


from sklearn import datasets
import pandas as pd 
import numpy as np 
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans


iris = datasets.load_iris()
print('\nA base a ser trabalhada é a base iris')
print('\nO tipo de dado da nossa base é: ', type(iris))
# Vamos fazer uma contagem de quantos elementos temos de cada classe
unicos, quantidade = np.unique(iris.target, return_counts=True)
print('\nOs valores de contagem são "unicos e quantidade" respectivamente \n', unicos, quantidade)

# Ambiente preparado vamos agora trabalhar o algoritmo de agrupamento kMeans. Este algoritmo exige um único argumento que é o número de cluster que você deverá informar

cluster = KMeans(n_clusters=3)
cluster.fit(iris.data)
# Para visualizarmos algum resultado precisamos criar uma variável centróide
centroide = cluster.cluster_centers_
print('\nVamos observar os centroides gerador de cada grupo de nosso cluster: \n', centroide)
# Agora vamos criar uma variável previsoes
previsoes = cluster.labels_
unicos2, quantidade2 = np.unique(previsoes, return_counts=True)

# O próximo passo será avaliar a qualidade do nosso previsor utilizando a Matriz de Confusão
resultados = confusion_matrix(iris.target, previsoes)
print(resultados)

# Agora faremos uma inspeção visual -> usaremos um gráfico de dispersão -> que requer dois atributos x e y -> por isso vamos trabalhar apenas com as colunas 0 e 1
plt.scatter(iris.data[previsoes == 0, 0], iris.data[previsoes == 0, 1], c='green', label='Setosa')
plt.scatter(iris.data[previsoes == 1, 0], iris.data[previsoes == 1, 1], c='red', label='Versicolor')
plt.scatter(iris.data[previsoes == 2, 0], iris.data[previsoes == 2, 1], c='blue', label='Virginica')
plt.legend()
plt.show()
