# Title     : Séries Temporais
# Objective : Conhecer um pouco daquilo que a linguagem R tem a nos oferecer para o tratamento de Séries Temporais
# Created by: accol
# Created on: 31/05/2020

library(forecast) # Pacote necessário para fazermos previsões

# Para essa prática usaremos o conjunto de dados nativo do R chamado AirPassangers -> passageiros transportados pelas companhias aéreas americanas no período de 1949 -> 1960

# <$> INICIANDO COM A EXPLORAÇÃO DOS DADOS <$>
# Fazendo uma inspeção visual em nossa base de dados
cat('\nA serie a ser trabalhada é a AirPassangers sua dimensão é de: ', length(AirPassengers), '\n')
cat('\nUma rápida inspeção sob os primeiros registros da Serie:\n ', head(AirPassengers), '\n')

print(AirPassengers)

# Visualizando as datas de início e fim da série
cat('\nA data de início da Série AirPassangers é: ', start(AirPassengers))
cat('\nA data final da Série AirPassangers é: ', end(AirPassengers))

# Agora faremos uma rápida inspeção Visual
plot(AirPassengers)
# Refinando ainda mais nossa Análise Exploratória EDA
plot(aggregate(AirPassengers))
# Refinando mais ainda vamos na nossa EDA avaliar o comportamento mensal da Série
monthplot(AirPassengers)
# Imagine agora que queremos visualizar uma janela -> uma parte da nossa Série Temporal => neste caso vamos extrair uma janela de Janeiro de 1960 à Dezembro de 1960 (um ano) ->> observe
subst = window(AirPassengers, start = c(1960, 1), end = c(1960, 12))
cat('\nA nossa janela atribuída a variável subst -> número de passageiros por mês é: \n', subst)
# Visualizando nossa janela graficamente temos:
plot(subst)

# <$> AGORA VAMOS TRABALAR COM A DECOMPOSIÇÃO DOS DADOS => Tendência, Sazonalidade e Aleatoriedade<$>

# É bem simples, podemos usar a função decompose() observe:
dec = decompose(AirPassengers)
# Observando nossa variável dec
cat('\n\nA variável dec armazena todos os dados referentes à decomposição de nossa base de dados\n')
print(dec)
cat('\nVamos agora plotar o gráfico da decomposição da base AirPassangers -> observe:\n\n')
plot(dec)
# Podemos acessar os dados por decomposição, por exemplo, imagine que desejo visualizar apenas a sazonalidade
dec_saz = dec$seasonal
cat('\nA sazonalidade apresenta os seguintes dados, observe:\n\n')
print(dec_saz)
# Podemos acessar os dados por decomposição, por exemplo, imagine que desejo visualizar apenas a linha de tendência
dec_tend = dec$trend
cat('\nA tendência da nossa base de dados apresenta os seguintes valores, observe:\n\n')
print(dec_tend)
# Podemos acessar os dados por decomposição, por exemplo, imagine que desejo visualizar apenas a aleatoriedade
dec_al = dec$random
cat('\nA aleatoridade da nossa base de dados apresenta os seguintes valores, observe:\n\n')
print(dec_al)
# Podemos da mesma forma visulaizar graficamente cada um dos elementos separadamente, observe
cat('\n\nVamos plotar o gráfico da Sazonalidade\n')
plot(dec_saz)
cat('\n\nVamos plotar o gráfico da Tendência\n')
plot(dec_tend)
cat('\n\nVamos plotar o gráfico da Aleatoriedade\n')
plot(dec_al)

# <$> FEITO TUDO ISSO PODEMOS ENTRAR NO PREOCESSO DE PREVISÃO -> O QUE PODEMOS ESPERAR PARA O FUTURO <$>
# Fazendo previsões da forma Simples -> não tão precisa
cat('\nA méida de todos os dados coletados é calulada por: \n', mean(AirPassengers))
# Observe que o uso da média para realizar previsões não levará a bons resultados, principlamente que sabemos que esta é uma Série com Sazonalidade, Aleatoriedade e Tendência de crescimento muito acentuada, logo há uma grande variabilidade nos dados
# Veja a seguir o cálculo da média considerando apenas o último ano da Série observe a discrepância
cat('\nA méida dos dados coletados no último ano da Série é calulada por: \n', mean(window(AirPassengers, start = c(1960,1), end = c(1960,12))))
# Uma forma mais refinada para aumentar a precisão é trabalhar com o conceito de Médias Móveis => a Média se ajusta na medida em que o tempo passa. Antes de tudo iremos precisar instalar o pacote 'forecast'
# No caso deste exemplo estaremos considerando 12 meses para o cálculo da média móvel (order = 12) -> você deverá experimentar outros valores até encontrar o que melhor se ajusta a seu projeto. No caso, vamos prever um ano após 1960
mediamovel = ma(AirPassengers, order = 12)
cat('\n\nExibindo o resultado da média móvel calculada considerando 12 meses\n')
print(mediamovel)
# Inspecionando seus dados mediamovel -> observerá alguns dados faltando NA -> isto ocorre porque ao escolher um parâmetro para o cálculo você fica dependente de ter periodiciadade acumulada para os cálculos da média
# Vamos experimentar agora alterar para 2 meses o período para o cálculo da media móvel
mediamovel_2 = ma(AirPassengers, order = 2)
cat('\n\nExibindo o resultado da média móvel calculada considerando 12 meses\n')
print(mediamovel_2)
plot(mediamovel)
plot(mediamovel_2)
# Através da inspeção visual poderá observar que os resultados encontrados com a mediamovel_2 se aproximam bem mais da realidade do comportamento dos dados -> e se usar meses igual 1 você poderá observar que retornará à série original, então usaremos a variação igual a 12
# Definida a média móvel podemos agora realizar a previsão => usaremos forecast note que usaremos h = 12 (quanto tempo que queremos prever) -> acompanhe ||> Provavelmente você terá uma mensagem de Warning ela é esperada em função dos NA de nossa base utilizada. Na prática você pode pensar em realizar uma limpeza na base (se for necessário)
previsao = forecast(mediamovel, h=12)
cat('\n\nExibindo o resultado da previsão considerando h = 12\n')
print(previsao)
# Vamos fazer uma inspeção visual de nossa previsão. Observe os níveis o efeito dos níveis de confiança -> acompanhe:
plot(previsao)
# Podemos sofisticar ainda mais nossa previsão usando a Técnica ARIMA. Vale a pena um estudo mais profundo em cima desta técnica, para esse laboratório vamos explorar apenas a auto.arima()
# Inicialmente vamos criar um objeto chamado arima
arima = auto.arima(AirPassengers)
cat('\n\nExibindo o objeto arima\n')
print(arima)
# Agora usaremos esse objeto para previsões
previsao_2 = forecast(arima, h=12)
cat('\n\nExibindo o nosso previsor\n')
print(previsao_2)
# Fazendo uma inspeção visual no nosso previsor2
plot(previsao_2)
