# Title     : Séries Temporais
# Objective : Conhecer um pouco daquilo que a linguagem Python tem a nos oferecer para o tratamento de Séries Temporais
# Created by: accol
# Created on: 31/05/2020

# Para essa prática usaremos o conjunto de dados chamado AirPassangers.csv -> passageiros transportados pelas companhias aéreas americanas no período de 1949 -> 1960


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from datetime import datetime
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from pmdarima.arima import auto_arima


# Leitura da base de dados AirPassangers.csv
base = pd.read_csv('D:/Users/Angelo/AULAS/Dados/AirPassengers.csv')
# Inspeção inicial da base AirPassangers.csv
# <$> INICIANDO COM A EXPLORAÇÃO DOS DADOS <$>
print('\nDimensões da base de dados AirPassangers: ', base.shape)
print('\nInspecionando os primeiros registros da base AirPassangers: \n', base.head())
print('\nAnálise dos últimos registros dos dados da base: \n', base.tail())
print('\nAnálise dos dados da base: \n', base.describe())
# Para trabalharmos com Séries Temporaris em Python, antes precisamos preparar os dados transformado o atributo Month num tipo data -> requisito para Séries Temporais, observe. Você sabe que base é um DataFrame pandas, mas queremos saber mais que isso
print('\nOs tipos/tipo de dados da nossa base é:\n', type(base))
print('\nOs tipos/tipo de dados envolvidos em nossa base é/são:\n', base.dtypes)
# Note que Month é do tipo object => precisamos transformá-lo em um tipo data para que tenhamos os recursos de Séries temporais à nossa disposição. Criaremos uma variável utilizando uma função λ -> importante acompanhe
#dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m') # Funciona tudo certo, mas a opção a seguir é mais interessante, por isso, deixei essa opção comentada
dateparse = lambda dates: datetime.strptime(dates, '%Y-%m')
print('\nO valor de dates é: ', dateparse)
# Agora faremos a leitura da nossa base de dados novamente fazendo as devidas transformações. Quando trabalhamos com Séries Temporais queremos que nosso índice seja a data, observe ~~>
base = pd.read_csv('D:/Users/Angelo/AULAS/Dados/AirPassengers.csv', parse_dates=['Month'], index_col='Month', date_parser=dateparse)
# Para verificar se temos nosso índice no formato de data escrevemos:
print('\nFormato do índice: ', base.index)
# Outra recomendação para se trabalhar com Séries Temporaris no Python é transformar nossa variável do tipo DataFrame no tipo Séries ~~> acompanhe
ts = base['#Passengers']
print('\nO tipo atribuído a ts (time series) é: ', type(ts))
print(ts.head())
# Veja algumas formas de indexar uma Série Temporal
print('\nPodemos indexar a série ts -> diretamente: ', ts[1])
print('\nPodemos indexar a série ts -> passando uma data específica: ',ts['1949-02-01'])
print('\nPodemos indexar a série ts -> passando uma data resumida: ',ts['1949-02'])
print('\nPodemos indexar a série ts -> usando datetime (requer import datetime): ',ts[datetime(1949, 2, 1)])
print('\nPodemos indexar a série ts -> por intervalos: ',ts['1950-01-01' : '1950-07-31'])
print('\nPodemos indexar a série ts -> todas as datas anteriores a uma específica: ',ts[:'1950-07-31'])
print('\nPodemos indexar a série ts -> somente pelo ano (todos os meses do ano): ',ts['1955'])
print('\nPodemos pegar o valor máximo da série ts: ',ts.index.max())
print('\nPodemos pegar o valor mínimo da série ts: ',ts.index.min())
# Vamos agora fazer uma inspeção visual na série ts
plt.plot(ts)
plt.show()
# Da inspeção visual percebemos uma clara tendência de crescimento anual => vamos agora fazer um agrupamento por ano. Posteriormente potaremos esse gráfico -> suavizando a curva
ts_ano = ts.resample('A').sum()
print('\nO somatório total de passageiros por ano é: ', ts_ano)
plt.plot(ts_ano)
plt.show()
# Vamos agora fazer um agrupamento por mês -> estamos em busca de entender o comportamente mês a mês da série
ts_mes = ts.groupby([lambda x: x.month]).sum()
plt.plot(ts_mes)
plt.show()
# Podemos observar que o maior fluxo de passageiros ocorre nos meses de junho, julho e agosto (sazonalidade -> período de férias)
# Vamos agora gerar um gráfico filtrando por datas -> um intervalo a sua escolha
ts_datas = ts['1960-01-01':'1960-12-01']
plt.plot(ts_datas)
plt.show()

# <$> <$> AGORA VAMOS TRABALAR COM A DECOMPOSIÇÃO DOS DADOS => Tendência, Sazonalidade e Aleatoriedade <$>
# Precisamos de uma nova importação -> seasonal_decompose
# Feito a importação e reaproveitando o código anterior podemos iniciar nossos estudos sobe DECOMPOSIÇÃO
print('\nVamos iniciar com uma inspeção visual aproveitando que já trabalhamos na nossa base AirPassengers anteriormente\n')
plt.plot(ts)
plt.show()
# Vamos agora criar uma variável chamada decomposição e a partir dela separar os elementos ||> Tencência, Sazonalidade e Aleatoriedade
decomposicao = seasonal_decompose(ts)
tendencia = decomposicao.trend
sazonal = decomposicao.seasonal
aleatorio = decomposicao.resid
# Vamos agora realizar uma inspeção visual na decomposição ||> Tencência, Sazonalidade e Aleatoriedade
print('\nObservando a Sazonalidade da base AirPassangers\n')
plt.plot(sazonal)
plt.show()
print('\nObservando a Tendência da base AirPassangers\n')
plt.plot(tendencia)
plt.show()
print('\nObservando a Aleatoriedade da base AirPassangers\n')
plt.plot(aleatorio)
plt.show()
# Vamos agora unir todos esses gráficos em um único subgráfico => acompanhe
plt.subplot(4,1,1)
plt.plot(ts, label = 'Original')
plt.legend(loc = 'best')
plt.subplot(4,1,2)
plt.plot(tendencia, label = 'Tendência')
plt.legend(loc = 'best')
plt.subplot(4,1,3)
plt.plot(sazonal, label = 'Sazonalidade')
plt.legend(loc = 'best')
plt.subplot(4,1,4)
plt.plot(aleatorio, label = 'Aleatoriedade')
plt.legend(loc = 'best')
plt.tight_layout()
plt.show()

# <$> FEITO TUDO ISSO PODEMOS ENTRAR NO PREOCESSO DE PREVISÃO -> O QUE PODEMOS ESPERAR PARA O FUTURO <$>
# Vamos aproveitar todo código anterior para ostrabalhos nesta prática
# </> PREVISÕES MÉDIAS ||> Extrapolando a partir da média </>
# Média simples -> pouco precisa para este conjunto de dados
media_periodo = ts.mean()
print('\nA média simples desse conjunto de dados é: ', media_periodo)
# Para melhorar a precisão dessa que é uma série não estacionária usaremos a média do último ano para prever o próximo
media_ult_ano = ts['1960-01-01':'1960-12-01'].mean()
print('\nA média simples desse conjunto de dados é: ', media_ult_ano)
# Observe a diferença entre as duas médias e tire suas conclusões
# Para elevar ainda mais nossa previsão usaremos agora o conceito da média móvel
# Como estamos trabalhando com uma previsão de um ano -> usaremos como referência de cálculo 12 (window = 12) meses anteriores
media_movel = ts.rolling(window=12).mean()
print('\nInspecionando a média_movel calculada: ', media_movel)
# Podemos visualizar os cálculos que foram feitos através da análise dos seguintes resultados
print('\nAnalisando os resultados de media movel para os 12 meses iniciais: ', ts[0:12].mean())
print('\nAnalisando os resultados de media movel para o 13 mes ', ts[1:13].mean())
# Fazendo uma inspeção gráfica
plt.plot(ts)
plt.plot(media_movel, color='red')
plt.show()
# Note que a média móvel apresenta um deslocamento inicial em relação ao início dos dados, isso é decorrente dos registros NAN iniciais
# Nosso objetivo agora é usar o conceito da média móvel para prever. Neste laboratório faremos previsão para os próximos 12 meses, no caso o ano de 1961. Para isso, estaremos utilizando a média dos últimos 12 meses calculados ||>acompanhe
# Como estaremos construindo nosso previsor no Python sem o uso de uma biblioteca específica, os passos estarão comentados para que você possa realizar os testes e perceber como o processo foi construído -> acompanhe
previsoes = []
for i in range(1,13):
#    print(i)
    superior = len(media_movel) - i
    inferior = superior - 11
#    print(inferior)
#    print(superior)
#    print('---')
    previsoes.append(media_movel[inferior:superior].mean())
# Note que vamos precisar fazer a inversão em nosso previsor, pois ele esta na sequência direta
previsoes = previsoes[::-1]
# Vamos agora fazer uma inspeção visual para os próximos 12 meses
plt.plot(previsoes)
plt.show()

# </> PARA FINALIZAR VAMOS FAZER AGORA A IMPLEMENTAÇÃO DO ARIMA => Vamos precisar de um novo import ||> ARIMA </>
# Vamos criar E treinar nosso modelo ||> Observe que vamos precisar de três parâmetros p (númerode termos autoregressivos), q (número da média móvel) e d (número de diferenças não sazonais) requistos para order -> acompanhe ||> em termos práticos você precisará testar esses parâmetros para encontrar ao que melhor se adapta ao seu modelo
modelo = ARIMA(ts, order=(2,1,2))
modelo_treinado = modelo.fit()
# A seguir vamos observar o nosso modelo treinado -> Não se preocupe com os Warning
print('\nNosso modelo treinado é: \n')
print(modelo_treinado.summary())
# Criado e treinado o modelo ||> Chegou a hora das previsões -> faremos 12 previsões a frente (parâmetro steps = 12)
previsões = modelo_treinado.forecast(steps=12)[0]
# para uma inspeção visual vamos compor nosso gráfico
eixo = ts.plot()
modelo_treinado.plot_predict('1960-01-01', '1962-01-01', ax=eixo, plot_insample = True)
plt.show()
# Experimente extrapolar para anos posteriores -> analise conclua -> estude

# </> VAMOS AGORA TRABALHAR COM O AUTO ARIMA precisaremos instalar o pyramid-arrima </>
# Primeiramente vamos usar o autoarima para escolher os melhores parâmteros para nosso projeto p, q e d
modelo_auto = auto_arima(ts, m = 12, seasonal = True, trace = True)
# Ps alguns Warnings serão normais -> não se preocupe com eles
# Finalizado vamos observar qual foi o melhor conjunto de parâmetros que ele encontrou para nosso projeto
print(modelo_auto.summary())
# Observe que a sugestão foram os valores (2, 1, 2) usados anteriormente -> na verdade primeiro fiz este teste para depois usar o método anteriormente descrito
# Agora faremos uma previsão com o auto-arrima
proximos_12 = modelo_auto.predict(n_periods=12)
print(proximos_12)
