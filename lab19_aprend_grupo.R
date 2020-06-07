# Title     : Aprendizado em grupo
# Objective : Conhecer o que a linguagem R tem a oferecer para o processo de aprendizagem em grupo
# Created by: accol
# Created on: 05/06/2020

# Para esse laboratório vamos usar para Ensamble Learnig o pacote randonforest -> que cria o modelo a partir dos resultados mais interessantes -> será necessário instalar o pacote "randomForest"
# Usaremos os dados de Credit.csv

library(randomForest)

# Pularemos algumas etapas -> pois são repetidas dos labs anteriores, ok
credito = read.csv('D:/Users/Angelo/AULAS/Dados/Credit.csv', sep = ',', header = T)

# Vamos criar nosso modelo para o algoritmo da Máquina de Vetor de Suporte
amostra = sample(2, 1000, replace = T, prob = c(0.7, 0.3))
creditotreino = credito[amostra == 1, ]
cat('\nQual a dimensão desta base -> creditotreino: ', dim(creditotreino))
creditoteste = credito[amostra == 2, ]
cat('\n\nQual a dimensão desta base -> creditoteste: ', dim(creditoteste))
# Para o modelo vamos criar um objeto chamado floresta -> observe que os parâmetros seguem a mesma linha dos algoritmos anteriores, acrescentamos ntree (número de árvores) ||> Há uma série de outros parâmetros cabe ao analista pesquisar mais a respeito para encontrar os parâmetros mais representativos para seu projeto
floresta = randomForest(class ~ ., data=creditotreino, ntree = 100, importance = T)
# Para uma inspeção visual em nosso objeto usaremos a função varImpPlot
varImpPlot(floresta)
# O gráfico gerado nos permite visualizar a influência de cada variável em nosso modelo
cat('\nVamos agora realizar nossa previsão\n')
previsao = predict(floresta, creditoteste)
cat('\nVamos agora construir nossa matriz de confusao\n')
confusao = table(previsao, creditoteste$class)
cat('\nObservando a matriz de confusão gerada\n')
confusao
cat('\nVamos agora trabalhar a precisão do nosso modelo\n')
taxaacerto = (confusao[1] + confusao[4]) / sum(confusao)
taxaerro = (confusao[2] + confusao[3]) / sum(confusao)
cat('\nA taxa de acerto de nosso modelo é: ', round(taxaacerto * 100, 2), '%')
cat('\nA taxa de erro do nosso modelo é:   ', round(taxaerro * 100, 2), '%')
