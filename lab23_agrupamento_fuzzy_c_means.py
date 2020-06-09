# Title     : Agrupamento usando Fuzzy c-means
# Objective : Conhecer o algoritmo de agrupamento Fussy c-means e como aplicá-lo utilizando a Linguagem Python. O princípio deste algoritmos é que uma instância pode pertencer a mais de um grupo -> dada uma certa probabilidade de pertença
# Created by: accol
# Created on: 08/06/2020
# Esta prática requer a instalação do pacote => pip install scikit-fuzzy


from sklearn import datasets
import numpy as np 
import skfuzzy
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt


iris = datasets.load_iris()
# Vamos criar uma variável r que receberá o resultado de nosso algoritmo -> observe que teremos que transpor a Matriz daí o uso do T. Vamos usar c = 3 (número de cluster) e para m usaremos o default da documentação m=2, error = 0.005 (recomendado) maxiter = 1000 (número de repetições) e init = None (default)
r = skfuzzy.cmeans(data=iris.data.T, c=3, m=2, error=0.005, maxiter=1000, init=None)
# Agroa criaremos uma variável para as previsões
previsoes_porcentagem = r[1]
# Para visualizar nosso previsor -> lembre-se que mantemos a coluna a variamos as linhas => temos
print(previsoes_porcentagem[0][0])
print(previsoes_porcentagem[1][0])
print(previsoes_porcentagem[2][0])
# Podemos conferir se a distribuição de probabilidade está ok e somando as probabiidade e verificando se somam 100%
print('\nTeste da distribuição de probabilidade: ', (previsoes_porcentagem[0][0] + previsoes_porcentagem[1][0] + previsoes_porcentagem[2][0]) == 1.0)
# Podemos agora verificar a precisão do nosso modelo com a Matriz de Confusão -> Antes usaremos o método .argmax com axis = 0 indicando que estamos trabalhando por colunas
previsoes = previsoes_porcentagem.argmax(axis = 0)
resultados = confusion_matrix(iris.target, previsoes)
print('\nPodemos agora observar a matriz de confusão\n', resultados)
