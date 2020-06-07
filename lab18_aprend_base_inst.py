# Title     : Aprendizado baseado em instância
# Objective : Conhecer ferramentas da linguagem Python para o aprendizado de máquina baseado em instâncias
# Created by: accol
# Created on: 05/06/2020

# Lembrando que no aprendizado baseado em instância não há a geração do modelo -> o processo é feito em tempo real -> a classificação é feita em função da proximidade dos dados em tempo real

# Vamos trabalhar com o algoritmo do Vizinho mais Próximo
# Usaremos os dados de iris.csv


from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from scipy import stats


# Observe que desta vez não importaremos a base de dados iris.csv => vamos usar a biblioteca datasets -> acompanhe
iris = datasets.load_iris()
# Vamos conferir se nossa base está ok
sumario = stats.describe(iris.data)
print('\nUm sumário da nossa base de dados é\n', sumario)
# Vamos criar as variáveis para nosso previsor
previsores = iris.data
classe = iris.target

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size=0.3, random_state=0) 

# Vamos criar a variável que conterá nosso algoritmo classificador, no caso o KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_treinamento, y_treinamento)
previsoes = knn.predict(X_teste)
# Observe que neste caso será realizado o cálculo da distância entre os vizinhos em tempo real
print('\nNossa variável previsoes é \n', previsoes)
# Precisamos agora avaliar a precisão de nosso algoritmo
confusao = confusion_matrix(y_teste, previsoes)
print('\nA matriz de confusão pode ser vista a seguir:\n', confusao)
taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1 - taxa_acerto
print('\nA taxa de acerto de nosso algoritmo é de: ', round(taxa_acerto * 100, 2), '%')
print('\nA taxa de erro de nosso algoritmo é   de: ', round(taxa_erro * 100, 2), '%')
# Observe que nosso algoritmo apresenta uma taxa extramente alta de acerto -> acima de 97%
