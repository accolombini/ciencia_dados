# Title     : Árvore de Decisão -> Classificação
# Objective : Conhecer os recursos da linguagem R para potencializar as aplicações de Machine Learning
# Created by: accol
# Created on: 05/06/2020

# Para este trabalho precisaremos de um novo pacote -> o pacote "rpart"

library(rpart)

# A base de dados será mesma Credit.csv
credito = read.csv('D:/Users/Angelo/AULAS/Dados/Credit.csv', sep = ',', header = T)
# Vamos pular as etapas iniciais pois são as mesmas vistas no laboratório anterior
# Vamos criar nosso modelo
amostra = sample(2, 1000, replace = T, prob = c(0.7, 0.3))
creditotreino = credito[amostra == 1, ]
cat('\nQual a dimensão desta base -> creditotreino: ', dim(creditotreino))
creditoteste = credito[amostra == 2, ]
cat('\n\nQual a dimensão desta base -> creditoteste: ', dim(creditoteste))
# Agora vamos criar nosso objeto árvore -> acompanhe -> como método temos duas opções 'anova' -> para Regressão ou 'class' -> para classificação ||> neste lab nosso foco é na classificação => acompanhe
arvore = rpart(class ~ ., data = creditotreino, method = 'class')
# Podemos visualizar essa árvore de forma textual usando print, observe
print(arvore)
# Melhorando a visualização da nossa árvore -> precisamos de dois comandos. Faça um por vez e observe os resultados para que possa refletir a respeito
plot(arvore)
text(arvore, use.n = T, all = T, cex = .8)
# Árvore criada -> nosso modelo está pronto para ser testado ||> Atenção há outras bibliotecas no R para representar árvores com melhor qualidade -> sugiro que se pesquise
teste = predict(arvore, newdata = creditoteste)
cat('\nQual a dimensão desta base -> teste: ', dim(teste))
cat('\n\nVamos inspecionar nosso objeto teste\n')
teste
# Observe que diferentemente do algoritmo de naivebayes da aula passada aqui tems uma probabilidde de ser bom ou mal pagador
# Para melhorar esse resultado devemos converter essas probabilidade de forma a definir quem é bom e quem é mal pagador ||> acompanhe!!
# A função cbind adiciona uma nova coluna em cred
cred = cbind(creditoteste, teste)
fix(cred)
# Queremos agora preencher Var25 com o resultado Good or Bad com base nos resultados do modelo ||> a nova coluna irá chamar-se Result
cred['Result'] = ifelse(cred$bad >= 0.5 , 'bad', 'good')
cat('\nVamos conferir o resultado da adição da nova coluna\n')
fix(cred)
# Podemos agora avaliar nosso classificador gerando a matriz de confusão ||> acompanhe
confusao = table(cred$class, cred$Result)
cat('\nPodemos agora visualizar nossa matriz de confusão e analisar nossa taxa de acerto/erro/n')
confusao
cat('\nCalculando a taxa de acerto\n')
taxaacerto = (confusao[1] + confusao[4]) / sum(confusao)
cat('\nA taxa de acerto -> do nosso modelo é: ', round(taxaacerto, 2) * 100, '%')
cat('\nCalculando a taxa de erros\n')
taxaerro = (confusao[2] + confusao[3]) / sum(confusao)
cat('\nA taxa de erro -> do nosso modelo é: ', round(taxaerro, 2) * 100, '%')
