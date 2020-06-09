# Title     : Agrupamento usando Fuzzy c-means
# Objective : Conhecer o algoritmo de agrupamento Fussy c-means e como aplicá-lo utilizando a Linguagem R. O princípio deste algoritmos é que uma instância pode pertencer a mais de um grupo -> dada uma certa probabilidade de pertença
# Created by: accol
# Created on: 08/06/2020


library(e1071)

# Agrupamento parcial Difuso
cluster = cmeans(iris[, 1:4], center = 3)
cat('\nVamos observar nossa variável cluster\n')
cluster
cat('\nVamos observar apenas os Cluster gerados\n')
cluster$cluster
# Você poderá observar no Closet hard clustering que o algoritmo já apresnta uma proposta de soluçao de agrupaento para nosso conjunto de dados iris
# Vamos avaliar o resultado desse processo de agrupamento utilizando uma Matriz de Confusão
confusao = table(iris$Species, cluster$cluster)
print(confusao)
