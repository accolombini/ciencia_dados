# Title     : AGRUPAMENTOS -> USANDO K-MEANS
# Objective : Conhecer como a linguagem R pode nos apoiar nos processos de classificação -> explorando nesta prática o algoritmoK-MEANS
# Created by: accol
# Created on: 08/06/2020

# Nesta prática faremos uso do conjunto de dados iris -> nativo no R
# Esta base -> já possui uma classe (Species) bem definida o que a torna ideal para nossos estudos

cat('\nConhecendo nossa base de dados\n', dim(iris))
cat('\nConhecendo nossa base de dados -> olhando para os atributos\n')
head(iris)
cat('\nConhecendo como as classes estão divididas\n')
summary(iris)
# Podemos observar que nossa base possui exatamente 50 regisgtros para cada classe +=> setosa = 50; versicolor = 50 e virginica = 50
# Praticando => uso do K-MEANS -> observe que não passamos a classe para o agrupador -> no caso aqui sabemos que se trata de 3 grupos - depois discutiremos como escolher o melhor conjunto de grupos
cluster = kmeans(iris[1:4], centers = 3)
cat('\nVamos observar nosso cluster\n')
cluster
cat('\nVamos olhar apenas para os Clusters gerados\n')
cluster$cluster
cluster$betweenss
# Você irá observar que o algoritmo não atribui nomes aos clusters e sim números, neste caso números 1, 2 e 3
# Comparando com o real
table(iris$Species, cluster$cluster)
# Desta tabela podemos observar que nosso algoritmo classificou todas as setosa corretamente, foi muito bem na classificação de versicolor e errou mais em virginica
# Vamos agora visualizar graficamente nossa classificação -> usaremos o plot padrão do R. Neste gráfico estaremos plotando as colunas de um a quatro da nossa base iris e usando como cores -> col = cluster que ele gerou => acompanhe
plot(iris[,1:4], col=cluster$cluster)
