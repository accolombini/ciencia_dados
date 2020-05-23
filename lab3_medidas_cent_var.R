# Title     : Medidas de Centralidade e de Variabilidade
# Objective : Apresentar as principais ferramentas em R para medidas de centralidade e variabilidade
# Created by: accol
# Created on: 21/05/2020
# Medidas de Centralidade em R >>= Funcoes no R:
# quantile() => para o calculo dos quartis
# sd() => para o calculo do desvio padrao
# var() => para o calculo da variancia
# mean() => para o calculo da media
# median() => para o calculo da mediana
# summary() => visualizacao rapida da base de dados

# Para este laboratorio estaremos gerando alguns dados para analise

jogadores = c(40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000)
media_salarios = mean(jogadores) # Calculo da media
mediana_salarios = median(jogadores) # Calculo da mediana
quartis_salarios = quantile(jogadores) # Calculo dos quartis
print(media_salarios)
print(mediana_salarios)
print(quartis_salarios)
# Para visualizar um quartil especifico, basta o seguinte <$> Atencao => indices em R iniciam em 1
print(quartis_salarios[1])
desviop_salarios = sd(jogadores) # Calcula o desvio padrao
print(desviop_salarios)
# Caso deseje visualizar rapidamente um resumo de sua base de dados, podera utilizar a funcao summary()
print('Resumo da base de dados:')
resumo_salarios = summary(jogadores)
print(resumo_salarios)
