# Title     : REGRAS DE ASSOCIAÇÃO
# Objective : Conhecer com a linguagem R pode potencializar a mineração de dados com foco na construção de ASSOCIAÇÕES usando o algoritmo APRIORI
# Created by: accol
# Created on: 09/06/2020

# Esta prática exige a instalação do pacote "arules"
# As regras serão carregadas a partir de um arquivo .txt no formato de cesta de compras, onde cada linha representa uma transação e os produtos são separados por vírgulas


library(arules)
library(arulesViz)

transacoes = read.transactions('D:/Users/Angelo/AULAS/Dados/transacoes.txt', format = 'basket', sep = ',')
transacoes
# Para uma melhor inspeção nas nossas transações podemos usaro o inspect
inspect(transacoes)
# Podemos criar uma imagem do arquivo para uma inspeção visual
image(transacoes)
# A partir deste momento vamos iniciar a mineração a partir da criação das regras. Observe que para restringir um pouco estou definindo que quero regras apenas com supporte e confiança mínimos de 50%. Sem essa condição muitas regras serão geradas => fique atento
regras = apriori(transacoes, parameter = list(supp=0.5, conf=0.5))
# Como podemos observar as regras geradas com mais detalhes => podemos usar o inspect
inspect(regras)
# Note que as primeiras regras não são relevantes => as regras interessantes surgem a partir da Regra de número 4
# Regras geradas o próximo passo é aplicá-las ao seu sistema de e-commerce, por exemplo
# Para melhorar nossa visualização vamos instalar o pacote "arulesViz"
plot(regras)
# Melhorando a visualização
plot(regras, method = 'graph', control = list(type = 'items'))
