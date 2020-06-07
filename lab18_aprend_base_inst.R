# Title     : Aprendizado baseado em instância
# Objective : Conhecer ferramentas da linguagem R para o aprendizado de máquina baseado em instâncias
# Created by: accol
# Created on: 05/06/2020

# Lembrando que no aprendizado baseado em instância não há a geração do modelo -> o processo é feito em tempo real -> a classificação é feita em função da proximidade dos dados em tempo real

# Vamos trabalhar com o algoritmo do Vizinho mais Próximo. Vamos precisar do pacote "class"
# Vamos usar o banco de dadis iris.csv -> que é nativo do R

library(class)

# Uma rápida inspeçao na base de dados
cat('\nVisualizando os primeiros registros da base\n\n')
head(iris)
cat('\nVisualizando um sumário da base\n\n')
summary(iris)

# Vamos criar nossas amostras de treino e o vetor que queremos classificar com nosso modelo => classificar
amostra = sample(2, 150, replace = T, prob = c(0.7, 0.3))
iristreino = iris[amostra == 1, ]
classificar = iris[amostra == 2, ]
cat('\nA dimensão dos nossos modelos treino e classificar são:\n\n')
cat('Iristreino:', dim(iristreino))
cat('\nClassificar:', dim(classificar))
# Agora estamos prontos para realizar a previsão -> usaremos o Algoritmo do vizinho mais próximo knn. O parâmetro k é o número de vizinhos próximos a ser considerado no processo de classificação -> iristreino o vetor usado para a busca no processo de classificação, classificar -> vetor a ser classificado e iristreino[, 5] a referência da classificação (lista de classificação) ||> note que não passamos para o previsor a coluna 5 => coluna de classificação
previsao = knn(iristreino[, 1:4], classificar[, 1:4], iristreino[, 5], k = 3)
# Uma vez feita a previsão -> você poderá alterar o valor de k e realizar outros testes a fim de encontrar o melhor valor para seu modelo
cat('\nAgora vamos avaliar a precisão do nosso modelo, criando a matriz de confusao\n')
confusao = table(classificar[,5], previsao)
confusao
cat('\nCalculando a taxa de acerto\n')
taxaacerto = (confusao[1] + confusao[5] + confusao[9]) / sum(confusao)
cat('\nA taxa de acerto -> do nosso modelo é: ', round(taxaacerto, 2) * 100, '%')
taxaerro = (confusao[2] + confusao[3] + confusao[4] + confusao[6] + confusao[7] + confusao[8]) / sum(confusao)
cat('\nA taxa de erro -> do nosso modelo_novo é: ', round(taxaerro, 2) * 100, '%')
