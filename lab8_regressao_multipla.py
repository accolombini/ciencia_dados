# Title     : Regressão Linear Múltipla
# Objective : Estudar os recursos da linguagem Python que poderão contribuir no processo de Regressão Linear Múltipla
# Created by: accol
# Created on: 28/05/2020

# Neste laboratório usaremos um banco de dados chamado mt_cars.csv (revista especializada em carros -> compara 11 características (atributos) de veículos num total de 32 registros


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import statsmodels.formula.api as sm # Permite trabalhar modelos no Python como se você estivesse no R
from sklearn.linear_model import LinearRegression


# Lendo nossa base de dados
base = pd.read_csv('D:/Users/Angelo/AULAS/Dados/mt_cars.csv')
# Fazendo uma inspeção nos dados
print('\nInspecionando os dados -> original \n', base.head())
# Observe que temos um atributo (Unnamed: 0) que não nos interessa -> vamos então limpar nossa base eliminando esse atributo >- note o uso de axis=1 significando que estamos eliminando a coluna toda
base = base.drop(['Unnamed: 0'], axis=1)
print('\nInspecionando os dados sem Unnamed: 0\n', base.head())
print('\nConhecendo a base de dados com describe() \n', base.describe())
print('\nConhecendo a base de dados com shape \n', base.shape)
# Vamos fazer uma correlação entre o consumo por galões e as polegadas cúbicas mpg x disp >- vamos inicialmente fazer uma regressão simples entre esses dois atributos => Faremos disp -> nossa variável independente ou exploratória (X) e mpg -> nossa variável dependente (y) -> variável de resposta -> aquilo que se quer prever. Lembre de usar o .values para já converter para array numpy -> requisito para o cálculo da Correlação
X = base.iloc[:, 2].values # Atributo disp está na coluna de índice 2 (terceira coluna)
print('\nConhecendo X antes do reshape \n', X)
# Observe que temos array unidimensional
y = base.iloc[:, 0].values # Atributo mpg está na coluna de índice 0 (primeira coluna)
# A correlação será dada através do método corrcoef()
correlacao = np.corrcoef(X, y)
print('\nVamos avaliar a correlação \n', correlacao)
# Observe que temos uma correlação forte negativa mas forte (-0.84755). Isso nos indica que o uso de regressão se aplica para que possamos conhecendo a variável exploratória X prever o comportamento da variável dependente y
# Lembrando que para continuarmos precisamos fazer o reshape dos dados para adequá-lo aos requistos das fórmulas. )bserve o uso de (-1, 1) -> signiificando: -1 não vamos mexer nas linhas e 1 que vamos adicionar uma coluna
X = X.reshape(-1, 1)
print('\nConhecendo X após o reshape \n', X)
# Observe agora que temos array bidimensional -> que atende aos nossos propósitos >- continuemos
# Agora vamos criar nosso modelo como LinearRegression() e para efetivamente trabalhar com esse modelo usaremos para treiná-lo o método fit() -> se encarrega de fazer o aprendizado
modelo = LinearRegression()
modelo.fit(X, y)
print('\nVamos inspecionar nosso modelo -> intercept_ \n', modelo.intercept_)
print('\nVamos inspecionar nosso modelo -> coef_ \n', modelo.coef_)
# Observe que pela inclinação da reta (coef_) podemos confirmar que temos uma correlação negativa
# Agora vamos encontrar nosso coeficiente de determinação R² que indica o quanto a variável exploratória (X) é capaz de explicar a variável dependente (y) -> faremos inicialmente uso do método .score() para encontrar R² e em seguida usremos para o cálculo de R² ajustado (mais preciso) uma outra biblioteca -> este valor de R² ajustado não está presente na biblioteca sklearn de forma trivial
r_semajuste = modelo.score(X, y)
print('\nVamos inspecionar nosso R² -> antes do ajuste \n',r_semajuste)

# Para fazermos a previsões -> visto que nosso R² é alto podemos usar Regressão Linear para encontrar o valor da variável dependente y
previsoes = modelo.predict(X)
print('\nVamos inspecionar o que previsoes consegue nos trazer -> compare com o valor de y \n', previsoes)
print('\nVamos inspecionar a variavel y original -> compare com o valor de y \n', y)
print('\nObservando a divergência entre o real e o previsto \n', previsoes - y)
# Para os ajustes precisaremos importar a biblioteca stasmodels que mos permite trabalhar no Python como se estivessemos no R -> observe o uso do método .ols() de ordinary least squares (mínimos quadrados orinários)
modelo_ajustado = sm.ols(formula='mpg ~ disp', data=base)
modelo_ajustado = modelo_ajustado.fit()
print('\nVamos inspecionar nosso R² ajustado -> antes do ajuste \n',modelo_ajustado.summary())
# Observe que o valor de R² ajustado é de 70.1% -> este deve ser o valor de R² utilizado para explicar oquanto a variável explicativa (independente) está explicando a variável dependente
# Vamos agora fazer uma inspeção gráfica
plt.scatter(X, y)
plt.plot(X, previsoes, color='red')
plt.show()
# Vamos agora realizar uma previsão a partir do modelo criado. Neste caso queremos saber o mpg para um disp = 200 >- não se esqueça de ajustar os valores para o exigido pelo método predict()
var_prev = np.array(200)
print('\nO tipo da variável usada para realizar as previsões é: ', type(var_prev))
var_prev = var_prev.reshape(-1, 1)
previsor = modelo.predict(var_prev)
print('\nO valor esperado para mpg a partir de disp = 200 é:\n', previsor)

# Agora vamos trabalhar com regressão LINEAR MÚLTIPLA -> vamos utilizar mais de uma variável exploratória para prever nossa variável dependente, teremos algo como >- y = (Xa + Xb + ... + Xn) = X1 >- observe que faremos isso no Python -> não se esqueça que o último índice não entra na composição de X1 -> [cyl, disp, hp]
X1 = base.iloc[:, 1:4].values
print('\nConhecendo X1 \n', X1)
print('\nDimensão de X1 -> queremos confirmar se temos uma matriz 32x3\n', X1.shape)
# Vamo criar nossa variável y1 que será usada para fazermos a previsão
y1 = base.iloc[:, 0].values
print('\nConhecendo y1 \n', y1)
print('\nDimensão de y1 -> queremos confirmar se temos uma vetor 32x0\n', y1.shape)
# Agora vamos criar o modelo 2 e treiná-lo
modelo2 = LinearRegression()
modelo2.fit(X1, y1)
# Vamos visualizar qual o nosso R² -> para validarmos o uso do regressor
print('\nVisualizando o R² do modelo2\n', modelo2.score(X1, y1))
# Como era de esperar -> maior número de variáveis maior valor de R² -> no caso 0.7678877440928638 ou seja, 76% que é um valor bem interessante para nosso previsor
# Para encontrarmos nosso R² ajustado devemos fazer:
modelo2_ajustado = sm.ols(formula='mpg ~ cyl + disp + hp', data=base)
modelo2_ajustado = modelo2_ajustado.fit()
print('\nVamos inspecionar nosso R² ajustado\n',modelo2_ajustado.summary())
# Observe que ainda assim R² ajustado 74% é alto o bastante para assegurar o uso do previsor
# Vamos agora fazer uma previsão considerando cyl = 4, disp = 200 e hp = 100 >- observe
novo = np.array([4, 200, 100])
# Assim como antes faremos uma alteração na variável novo usando o reshape >- neste caso usaremos reshape(1, -1) que significa que vamos adicionar uma linha e não vamos mexer nas colunas
novo = novo.reshape(1, -1)
# Agora sim podemos fazer nossa previsão
print('\nVamos avaliar nosso valor de mpg a partir do previsor\n', modelo2.predict(novo))
