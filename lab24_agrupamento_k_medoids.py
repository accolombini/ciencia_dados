# Title     : AGRUPAMENTO K-MEDOIDS -> escolhe pontos reais para os centróides
# Objective : Conhecer como a linguagem Python emprega o algoritmo de agrupamento K-Medoids => este algoritmo trabalha com agrupamentos por Menoids (ponto real mais representativo). Note que neste caso não precisaremos fazer a previsão do número de Cluster, o próprio algoritmo se encarrega de encontrar o melhor número de cluster para nós
# Created by: accol
# Created on: 08/06/2020
# Requer a instalaçãodo pacote => pip install pyclustering

import numpy as np 
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster import cluster_visualizer


# Vamos criar nossa variável de trabalho iris que deverá receber os dados da base iris
# Atenção faremos análise de apenas dois atributos -> o atributo 0 e o atributo 1 -> requisitos impostos pelo método cluster_visualizer
iris = datasets.load_iris()
# Vamos iniciar criano nossa variável -> vamos testar com os valores [3, 12, 20] => experimente outros ok
cluster = kmedoids(iris.data[:,0:2], [3, 12, 20])
cluster.get_medoids()
# Faremos o treinamento com processes()
cluster.process()
# Vamos agora para as nossas previsões
previsoes = cluster.get_clusters()
print('\nOs indices para os registros de cada grupo podem ser visto em previsoes\n', previsoes)
# Observe que em previsões nós temos na verdade um índice para os registros pertecnetes a cada grupo
# A variável medoides trará o índice para o medoide utilizado noprocesso de clusterização
medoides = cluster.get_medoids()
print('\nOs indices para os registros dos medoides utilizados são:\n', medoides)
# Vamos criar uma variável para visualizar este Cluster -> cuidado com o uso de clusters e cluster
v = cluster_visualizer()
v.append_clusters(previsoes, iris.data[:, 0:2])
v.append_cluster(medoides, data=iris.data[:, 0:2], marker='*', markersize=15)
v.show()

# O próximo passo será avaliar a qualidade do nosso previsor -> Precisaremos ajustar nossa variável para que fique no padrão de target => acompanhe
lista_previsoes = []
lista_real =[]
for i in range(len(previsoes)):
    print('---')
    print(i)
    print('---')
    for j in range(len(previsoes[i])):
#        print(j)
        print(previsoes[i][j])
        lista_previsoes.append(i)
        lista_real.append(iris.target[previsoes[i][j]])
# Precisamos converter nossa variável para o formato numpy array -> requisito para construção da Matriz de Confusão
lista_previsoes = np.array(lista_previsoes)
lista_real = np.array(lista_real)
# Feito as transformação podemos construir nossa Matriz de Confusão
resultados = confusion_matrix(lista_real, lista_previsoes)
print('\nVamos observar nossa matriz de confusão:\n', resultados)
