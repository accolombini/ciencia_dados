# Title     : Amostras
# Objective : Como o R pode nos auxiliar para trabalhar com amostras
# Created by: accol
# Created on: 19/05/2020
# Lab1_amostras => neste laboratório vamos explorar algumas ferramentas do R que poderao ser uteis para trabalhar
# com estatistica. Importante ha muitas outras ferramentas em R, vamos explorar algumas aqui, sugiro que se
# aprofundem na literatura. Divirtam-se!

library(sampling)
library(TeachingSampling)

dim(iris) # visualizar a dimensao da base de dados

# Imagine agora que precisamos separar estes dados em dois conjuntos (amostras) com 50% cada
# Para isso vamos gerar um conjunto com 150 numeros aleatorios e depois usa-los para compor as duas amostras com 50% cada
# A funcao sample() recebe 4 parametros o primeiro refere-se ao conjunto de dados, de onde serao extaridas as amostras
# (no caso nossa amostra será de 0s e 1s), depois a quantidade de numeros aleatorios que serao gerados, no caso 150,
# o terceiro parametro e utilizado para dizer se e com reposicao ou nao e o quarto parametro e um vetor de distribuicao
# de probabilidades (nem sempre este tera os mesmos valores, embora neste exemplo a probabilidade seja 50%, 50%)

amostra = sample(c(0,1), 150, replace = TRUE, prob = c(0.5, 0.5))

amostra

# Para avaliar adimensao de cada vetor gerador de amostra (lembre-se que os eventos sao independentes, assim nao necessariamente teremos 75 uns ou 75 zeros, usamos o comando length para avaliar o tamanho da amostra

length(amostra[amostra == 1])
length(amostra[amostra == 0])

# Para fixar a amostra, digo repetir sempre os mesmos resultados, voce podera usar o comando set.seed(semente)

set.seed(250) # Estecomando define uma semente que assegura que possamos reproduzir o experimento sempre com
# os mesmos valores
sample((100), 1)

# A seguir vamos gerar amostras estratificadas, para isso, vamos usar o conjunto de dados iris

summary(iris)

# Imagine a situação na qual se queira selecionar 1 amostra com 25 elementos de cada especie, mas que tenham
# sido selecionados ao acaso. Para isso, usaremos o pacote "sampling"
# Trabalhando com amostras estratificadas => lembre de carregar o pacote, nao basta instala-lo
# O metodo que sera usado para gerar os dados aleatorios sera uma constante, para isso, bsta digitar 'srswor' => metodo
# padrao da funcao strata que gera uma amostra aleatoria sem reposicao

amostra2 = strata(iris, ('Species'), size=c(25, 25, 25), method = 'srswor')
amostra2
summary(amostra2)

# Ate aqui tudo muito bem comportado, vamos agora usar uma outra base de dados do R chamada infert onde os dados
# nao sao tao bem comportados como no caso das floresde iris

summary(infert)

# Queremos gerar uma amostra estratificada que tenha proporcao da coluna education => por exemplo, imagina uma
# amostra estratificada de 100 elementos. Neste caso, precisaremos calcular a proporcao, dado que nosso conjunto
# de dados possui caracteristicas dispares. Usaremos a formula numero de individuos/education dividido pelo total
# de individuos multiplicado pelo tamanho desejado da amostra, vamos ao R

zero_cinco = round(12 / 248 * 100)
seis_onze = round(120 / 248 * 100)
mais_doze = round(116 / 248 * 100)

# Gerando a amostra estratificada assegurando a proporcao

amostra3 = strata(infert, ('education'), size=c(5, 48, 47), method = 'srswor')
amostra3
summary(amostra3)
dim(amostra3)

# Vamos agora trabalhar com amostragem sistematica utilizando R. Precisamos instalar a biblioteca 'TeachingSampling'
# Esta biblioteca ira gerar numeros aleatorios ue depois poderao ser utilizados para gerar as amostras. No exemplo,
# iremos trabalhar com o Banco de Dados Iris e queremos que a amostra pegue um elemento a cada 10, lembrando que
# na amostra sistematica o primeiro e gerado aleatoriamente. A funcao S.SY() requer dois parametros, o primeiro diz
# o numero de elementos da populacao e o segundo o intervalo de coleta, observe:

amostra4 = S.SY(150, 10)
amostra4

# Para gerar nossa amostra a partir desta aleatoriedade, basta fazermos o que segue, observe que estamos pegando
# as linhas do banco de dados Iris que coincidam com nossa amostra

amostrairis = iris[amostra4,]
amostrairis
