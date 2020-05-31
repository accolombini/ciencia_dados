# Title     : Outliers
# Objective : Entender como a linguagem R pode nos ajudar com o tratamento de Outliers
# Created by: accol
# Created on: 30/05/2020
# Vamos precisar de um pacote que não é ativado por default no R => outiliers

library(outliers)

# Vamos iniciar os exercícios deste laboratório com o já conhecido conjunto de dados iris


# Iniciando com o já conhecido boxplot que por padrão exibe os Outliers
boxplot(iris$Sepal.Width)
# Visualmente podemos perceber a presença de três Outliers superiores e um inferior
# Podemos parametrizar nosso boxplot para não exibir Outliers => observe
boxplot(iris$Sepal.Width, outline = F)
# Queremos ir além da visão gráfica => vamos inserir dados e estatística no nosso gráfico
boxplot.stats(iris$Sepal.Width)
# Agora se quisermos observar apenas os dados que gereram os Outliers podemos escrever -> você deverá observar os três Outliers superiores 4.4, 4.1 e 4.2 e o Outlier inferior 2.0
boxplot.stats(iris$Sepal.Width)$out
# Há um outro pacote para análise de Outliers chamado Outlier -> recomendo que se estude um pouco este pacote há muito mais do que aquilo que será qui demonstradao -> não se esqueça de executá-lo no seu exercício utilizando o library 'outliers'
# Por padrão a função outlier procura por Outliers superiores -> observe que ele retornou apenas o Outlier mais alto 4.4
outlier(iris$Sepal.Width)
# Podemos querer observar os Outliers inferiores, para isso fazemos a parametrização de opposite que por default é False para True
outlier(iris$Sepal.Width, opposite = T)

