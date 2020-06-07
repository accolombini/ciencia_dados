# Title     : Seleção de Atributos utilizando o algoritmo da Máquina de Vetor de Suporte
# Objective : Avaliar como uma boa seleção de atributos pode contribuir para melhorar a precisão do Classificador
# Created by: accol
# Created on: 05/06/2020

# Entendendo a Maldição da Dimensionalidade
# Vamos usar o mesmo conjunto de dados Credit.csv

library(e1071)
library(FSelector)

credito = read.csv('D:/Users/Angelo/AULAS/Dados/Credit.csv', sep = ',', header = T)

# Vamos criar nosso modelo para o algoritmo da Máquina de Vetor de Suporte
amostra = sample(2, 1000, replace = T, prob = c(0.7, 0.3))
creditotreino = credito[amostra == 1, ]
cat('\nQual a dimensão desta base -> creditotreino: ', dim(creditotreino))
creditoteste = credito[amostra == 2, ]
cat('\n\nQual a dimensão desta base -> creditoteste: ', dim(creditoteste))
# Vamos pular as etapas iniciais pois são as mesmas vistas nos laboratórios anteriores
modelo = svm(class ~ ., creditotreino)
cat('\nVisualisando nosso modelo\n')
modelo
# Vamos agora realizar nossa previsão -> avaliando nosso modelo com a variável creditoteste
predicao = predict(modelo, creditoteste)
cat('\nPodemos observar nossa variável previsao\n\n')
predicao
cat('\nPara nosso cálculo da taxa de acerto criamos antes a matriz de confusão\n\n')
confusao = table(creditoteste$class, predicao)
confusao
cat('\nCalculando a taxa de acerto\n')
taxaacerto = (confusao[1] + confusao[4]) / sum(confusao)
cat('\nA taxa de acerto -> do nosso modelo é: ', round(taxaacerto, 2) * 100, '%')
cat('\nCalculando a taxa de erros\n')
taxaerro = (confusao[2] + confusao[3]) / sum(confusao)
cat('\nA taxa de erro -> do nosso modelo é: ', round(taxaerro, 2) * 100, '%')
cat('\nA taxa de acerto utilizando todos os 20 atributos foi de:', round(taxaacerto, 2) * 100, '%')
# Vamos agora fazer uma seleção de atgributos e tentar encontrar uma melhor taxa de acerto
# Mas como saber quais são os atributos mais relevantes? Essa deve ser a grande questão a ser aqui respondida
# Sabemos que existem algoritmos que fazem essa seleção automaticamente, mas esse nem sempre será o caso. Vamos precisar de um novo pacote para nos apoiar nesta tarefa o pacote é "FSelector" -> realiza a seleção de atributos

# Vamos usar o FSelector com o método random.forest.importance() => há outros vale a pesquisa por parte dos interessados. Observe que os parâmetros são os mesmos, a menos do fato que para a seleção de atributos devemos passar todos o conjunto de dados -> credito
# Você deverá observar a lista dos 20 atributos gerada a seu grau de importância para gerar a classificação
random.forest.importance(class ~ ., credito)
# A partir deste resultado faremos uma seleção de atributos mais relevantes e vamos gerar um novo modelo -> com isso, espera-se melhor resultado no nosso previsor
cat('\nDe nossa análise inicial vamos selecionar os seguintes atribuots: checking_status, duration, credit_history e purpose\n\n')
modelo_novo = svm(class ~ checking_status + duration + credit_history + purpose, creditotreino)
cat('\nVisualisando nosso modelo_novo\n')
modelo_novo
# Vamos agora realizar nossa previsão -> avaliando nosso modelo com a variável creditoteste
predicao_nova = predict(modelo_novo, creditoteste)
cat('\nPodemos observar nossa variável previsao_nova\n\n')
predicao_nova
cat('\nPara nosso cálculo da taxa de acerto criamos antes a matriz de confusão_nova\n\n')
confusao_nova = table(creditoteste$class, predicao_nova)
confusao_nova
cat('\nCalculando a taxa de acerto\n')
taxaacerto_novo = (confusao_nova[1] + confusao_nova[4]) / sum(confusao_nova)
cat('\nA taxa de acerto -> do nosso modelo_novo é: ', round(taxaacerto_novo, 2) * 100, '%')
cat('\nCalculando a taxa de erros_novo\n')
taxaerro_novo = (confusao_nova[2] + confusao_nova[3]) / sum(confusao_nova)
cat('\nA taxa de erro -> do nosso modelo_novo é: ', round(taxaerro_novo, 2) * 100, '%')
cat('\n\nA taxa de acerto utilizando todos os 20 atributos foi de:', round(taxaacerto, 2) * 100, '%')
cat('\nA taxa de acerto utilizando todos os 4 atributos selecionados foi de:', round(taxaacerto_novo, 2) * 100, '%')
# Aparentemente não tivemos melhoria no nosso resultado, mas com apenas 4 atributos conseguimos chegar bem próximo e algumas das vezes superar o modelo com 20 atributos
