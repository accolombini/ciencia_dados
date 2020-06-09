# Title     : AGRUPAMENTO K-MEDOIDS
# Objective : Conhecer como a linguagem R emprega o algoritmo de agrupamento K-Medoids => este algoritmo trabalha com agrupamentos por Menoids (ponto real mais representativo)
# Created by: accol
# Created on: 08/06/2020

# Exige a instalação do pacote cluster e suas dependências "cluster", dependencias = T

library(cluster)

# Vamos pratica -> observe que os passos são praticamente os mesmos => nosso conjunto de dados será o iris e o número de agrupamentos sugeridos k será 3
cluster = pam(iris[, 1:4], k=3)
cat('\nO tipo de dado da nossa variável gerada é: ', typeof(cluster))
cat('\nVamos observar nossa variável cluster gerada\n')
cluster
# Observe que os Medoids utilizados são pontos reais (pertencentes a base iris) -> observe
cat('\nOlhando para os medoids escolhidos\n\n')
cluster$medoids
# Observe também que foi criado um vetor onde foi atribuído os valores 1 2 e 3 para os três grupos encontrados
cat('\nOlhando para os clusters gerados\n\n')
cluster$clustering
# Analisando os resultados -> matriz de confusão
confusao = table(iris$Species, cluster$clustering)
print(confusao)
# Observe que temos uma taxa de acerto interessante -> muito próxima para não dizer igual aos algoritmos usados anteriormente
cat('\nFaremos algora uma inspeção gráfica deste modelo\n')
plot(iris[,1:4], col=cluster$clustering)
