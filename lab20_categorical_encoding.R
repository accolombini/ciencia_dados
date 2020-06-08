# Title     : Categorical Encoding no R
# Objective : Conhecer algumas ferramentas que a linguagem R tem a nos oferecer para trabalharmos com categorical encoding -> transformar dados categoricos em dados numéricos
# Created by: accol
# Created on: 08/06/2020


library(mltools)
library(data.table)


# Para esta prática utilizaremos os dados do Titanic nativos do R

cat('\nVamos observar nosso conjunto de dados\n', Titanic)
cat('\nPara bem tratarmos nossos dados, precisamos conhecer o tipo de dados: ', class(Titanic))
# Observe que nosso conjunto de dados está formato de tabelas -> para usarmos as ferramentas do R, precisaremos antes converter esses dados para o tipo adequado -> no caso vamos transformá-lo em um DataFrame

tit = as.data.frame(Titanic)
cat('\nVamos observar nosso conjunto de dados -> transformado\n')
print(tit)
cat('\nConferindo nossos dados, analisando a conversar de tipo: ', class(tit))

# Primeiramente vamos trabalhar com label Encoding -> vamos trabalhar com a coluna Classe, sexo e idade (categóricas)

labenc = data.matrix(tit[, 1:3])
cat('\nVamos observar nosso conjunto de dados labenc -> transformado\n')
print(labenc)

# Vamos testar agora o ONE-HOT ENCODING para as mesmas três colunas Classe, sexo e idade categóricas
# Para o ONE-HOT ENCODING teremos que transformar novamente os dados em tabela

hotenco = one_hot(as.data.table(tit[, 1:3]))
cat('\nVamos observar nosso conjunto de dados hotenco -> transformado\n')
print(hotenco)

# Para trabalhar com ONE-HOT ENCODING vamos precisar suprimir uma coluna, não se esqueça disso, ok
