# Title     : Features Scalling => DIMENSIONAMENTO DE CARACTERÍSTICAS
# Objective : Como a linguagem R pode nos apoiar nos trabalhos de tratamento de dados usando Feature Scalling
# Created by: accol
# Created on: 08/06/2020

# Para esse laboratório trabalharemos com o conjunto de dados iris
# Inicalmente vamos visualizar os dados sem qualquer transformação

print('\nObservando nosso conjunto de Dados sem qualquer transformação')
boxplot(iris[, 1:4])

# Primeiramente vamos realizar uma padronização => PADRONIZAÇÃO (Z-SCORE)
iris_padr = scale(iris[, 1:4])
print('\nObservando nosso conjunto de Dados usando PADRONIZAÇÃO (Z-SCORE)')
boxplot(iris_padr[, 1:4])

# Agora vamos realizar uma normalização => NORMALIZAÇÃO (MIN-MAX) -> para esse fim precisaremos criar uma função
normaliza = function(x){
  return((x - min(x)) / (max(x) - min(x)))
}
iris_norm = normaliza(iris[, 1:4])
print('\nObservando nosso conjunto de Dados usando NORMALIZAÇÃO (MIN-MAX)')
boxplot(iris_norm[, 1:4])
