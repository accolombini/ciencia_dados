# Title     : Naive Bayes
# Objective : Conhecer os recursos que a linguagem R tem a nos oferecer para trabalharmos com Calssificação
# Created by: accol
# Created on: 04/06/2020

# Importante -> vamos precisar instalar dois pacotes que juntos respondem por praticamente tudo que R oferece para trabalhar com Machine Learning -> são eles: e1071 e klaR

# Para este laboratório usaremos o pacote e1071 e a base de dados Credit.csv -> o separador default é a ',', logo desnecessário, será aqui empregado para que se lembre em caso de um separador diferente deverá ser utilizado, ok

library(e1071)

credito = read.csv('D:/Users/Angelo/AULAS/Dados/Credit.csv',',', header = T)
# Vamos iniciar fazendo uma rápida inspeção em nossa base de dados
cat('\nA base de dados Credit.csv é composta por\n')
credito
# Observe que o último atributo é a Classe que nos diz se ele/ela é um bom ou mal pagador
cat('\nObservando os primeiros registros de nossa base:\n ')
head(credito)
cat('\nQual a dimensão desta base\n', dim(credito))
cat('\nUm sumário da base para início dos trabalhos\n')
summary(credito)
# Para este laboratório queremos prever se um dado cliente solicitando crédito será um bom ou mal pagador => para isso teremos que gerar um modelo a partir dos dados históricos >>= usaremos 70% dos dados para gerar nosso modelo e 30% para realizar os testes do modelo ||> usaremos para esse propóstio a função sample() -> estudada anteriormente
# Para paramtrizar nossa função sample() usaremos -> parâmetro 1 = 2 (siginfica que estaremos gerando 1 ou 2, parâmetro 2 = 1000 (temos 1000 registros em nossa base), parâmetro 3 = replace = T (será com reposição), parâmetro 4 = prob=c(0.7, 0.3) ||> trabalharemos com 70% e 30% -> acompanhe
amostra = sample(2, 1000, replace = T, prob = c(0.7, 0.3))
cat('\nVisualizando nossa amostra que deverá ser um array composto por 1000 registros de 1 (70%) e 2 (30%)')
amostra
# Precisamos agora separar nossa amostra em dois conjuntos de dados um para treino e outro para teste -> acompanhe
creditotreino = credito[amostra == 1, ]
creditoteste = credito[amostra == 2, ]
cat('\nQual a dimensão da variável creditotreino\n', dim(creditotreino))
cat('\nInspecionando nossa variável creditotreino\n')
creditotreino
cat('\nQual a dimensão da variável teste\n', dim(creditoteste))
cat('\nInspecionando nossa variável creditoteste\n')
creditoteste
# Observe que as variáveiis creditotreino e creditoteste não apresentam resultados exatos 70% e 30% respectivamente, isso porque nossa função usa probabilidades independentes -> caso de dúvidas revise o lab onde se trabalhou com a função sample()
# O importante é que a separação dos dados em treino e teste foram realizados de forma aleatória ||> Agora vamos gerar nosso modelo -> usaremos o algoritmo naiveBayes
# Observe que estaremos usando a class (good or bad -> será nossa variável de resposta) o ~ (separa os atributos -> mostrando a separação entre as variáveis explicativas e a variável de resposta) e o . (que representa todos os argumentos -> serão nossas variáveis explicativas) ||> se quisesse uma seleção de atributos (variáveis explicativas) teria que inserir um a um concatenando-os com o sinal de '+'
modelo = naiveBayes(class ~ ., creditotreino)
cat('\nQual a dimensão do nosso modelo\n', dim(modelo))
cat('\nVamos fazer uma ispeção em nosso modelo\n')
cat('\nPodemos conferir a classe do nosso modelo: ', class(modelo))
modelo
# Atenção -> outro algoritmo poderá gerar outro resultado para seu modelo
# Precsiamos agora criar nossa variável teste para avaliar nosso modelo ||> note que a função para realizar previsões será sempre a mesma >>= predict -> que precisa de dois parâmentros um o modelo e o outro a variável de teste
predicao = predict(modelo, creditoteste)
cat('\nPodemos conferir nosso array predição\n ')
predicao
# Feito isso teremos um vetor predicao com aproximadamente 30% dos dados e podemos agora comparar esse resultado com o a amostra original que contém os dados históricos conhecidos
# Para essa análise vamos criar uma matriz de confusão -> acompanhe
confusao = table(creditoteste$class, predicao)
cat('\nPodemos conferir o resultado analisando a marriz de confusão\n ')
confusao
# Para melhor avaliar estes resultados vamos calcular o índice de acertos => acompanhe pegaremos a célula 1 e célula 4 da matriz de confusão que corresponde aos acertos e dividiremos pelo total de registros, observe
taxaacerto = (confusao[1] + confusao[4]) / sum(confusao)
cat('\nA taxa de acerto do nosso modelo é de: ', round(taxaacerto * 100, 2),'%')
# Se quisermos calcular a taxa de erro basta:
taxaerro = (confusao[2] + confusao[3]) / sum(confusao)
cat('\nA taxa de acerto do nosso modelo é de: ', round(taxaerro * 100, 2),'%')
# A partir desse momento cabe o analista avaliar se o modelo está bom o suficiente para ser colocado no ambiente de produção. Poderá o analista trabalhar o modelo com base nos fundamentos apresentados a fim de melhorar sua resposta a um ponto que considere aceitável para seu projeto
# Vamos neste momento simular o Modelo em Produção
# Para nosso teste em Produção precisamos de um/vários novo cliente/s para submetê-lo ao modelo e verificar sua resposta
novocredito = read.csv('D:/Users/Angelo/AULAS/Dados/NovoCredit.csv', sep = ',', header = T)
# Vamos iniciar fazendo uma rápida inspeção em nossa base de dados -> NovoCredit
cat('\nA base de dados NovoCredit.csv é composta por\n')
novocredito
cat('\nQual a dimensão da base NovoCredt\n', dim(novocredito))
# Observe que esta base não apresenta o classe -> temos os 20 primeiros atributos tal e qual o modelo, mas a Classe não esta presente (ela nosso modelo deverá predizer)
cat('\nObservando os primeiros registros de nossa novocredito:\n ')
head(novocredito)
# Vamos agora trabalhar a previsão dos dados
predicao_novo = predict(modelo, novocredito)
cat('\nPodemos conferir nosso array predição_novo\n ')
predicao_novo
