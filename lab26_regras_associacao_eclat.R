# Title     : Itens frequentes com Eclat
# Objective : Como a linguagem R pode contribuir para os processos de itens frequentes utilizando o algoritmo Eclat
# Created by: accol
# Created on: 09/06/2020

# O pacote é o mesmo arules


library(arules)
library(arulesViz)



transacoes = read.transactions('D:/Users/Angelo/AULAS/Dados/transacoes2.txt', format = 'basket', sep = ',')
transacoes
# Para uma melhor inspeção nas nossas transações podemos usaro o inspect
inspect(transacoes)
# Podemos criar uma imagem do arquivo para uma inspeção visual
image(transacoes)
# A partir deste momento vamos iniciar a mineração a partir da criação das regras. Observe que para restringir um pouco estou definindo que quero regras apenas com supporte minimo de 0.1 e maxlen -> número máximo de itens. Atenção este suporte é muito baixo na prática recomenda-se trabalhar com suportes a partir de 0.5
regras = eclat(transacoes, parameter = list(supp = 0.1, maxlen = 15))
# Vamos observar as regras criadas
inspect(regras)
# Vamos visualizar as regras graficamente
plot(regras)
plot(regras, method = 'graph', control = list(type = 'items'))
