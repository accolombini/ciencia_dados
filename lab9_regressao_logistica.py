# Title     : Regressão Logística -> Sucesso ou Fracasso
# Objective : Conhecer as ferramentas de Python que podem nos apoiar no processo de Regressão Logística
# Created by: accol
# Created on: 29/05/2020

# Para este laboratório usaremos base de dados de campanha eleitoral -> eleicao.csv e novoscandidatos.csv
# Nesta prática queremos a partir dos dados da base eleicao.csv queremos prever se os candidados de novoscandidatos.csv serão ou não eleitos
# Na tabela eleicao.csv teremos o nome do candidato, a situação -> se ele foi eleito ou não e despesas -> quanto ele investiu na campanha


import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.linear_model import LogisticRegression


# Lendo nossa base de dados e fazendo uma primeira inspeção básica. Atenção este arquivo .csv usa ';' como separador => será necessário especificar
base = pd.read_csv('D:/Users/Angelo/AULAS/Dados/Eleicao.csv', sep=';')
print('\nA Dimensão de nossa base Eleicao.csv é \n', base.shape)
print('\nUm resumo dos dados de base Eleicao.csv é \n', base.describe())
print('\nOlhando como os dados são organizados na base Eleicao.csv\n', base.head())
# Vamos fazer uma inspeção visual em nosso DataFrame. Note que, neste caso estaremos utilizando uma formadiferente de acesso a um determinado atributo em um DataFrame
plt.scatter(base.DESPESAS, base.SITUACAO)
plt.show()
# Agora vamos calcular a Correlação entre DESPESAS e SITUACAO
correlacao = np.corrcoef(base.DESPESAS, base.SITUACAO)
print('\nA correlação entre os atributos DESPESAS e SITUACAO são \n', correlacao)
# Observe que enocntramos uma correlaçao positiva forte de 81.2% -> indicativo de uma excelente correlação => viabilizando o processo de regressão linear logistica -> continuemos
# Nosso próximo passo será a criação do nosso modelo de Regressão Logistica . Não se esqueça de criar as variáveis X (INVESTIMENTO) e y (DESPESAS) -> em seguida vamos criar e treinar o modelo com o método .fit(). Lembre de fazer o .reshape() na variável X
X = base.iloc[:,2].values
# Note que nosso rechape será um pouco diferente -> vale o aprendizado => observe como podemos criar um novo eixo na nossa variável X
X = X[:, np.newaxis]
y = base.iloc[:, 1].values
# Chegou o momento de efetivamente criar o modelo
modelo = LogisticRegression()
modelo.fit(X, y)
# Vamos fazer uma inspeção em nosso modelo -> queremos conhecer seus parâmetros chaves => coef_ e intercept_
print('\nO coeficiente de modelo é:\n', modelo.coef_)
print('\nO ponto de interceptação de modelo é:\n', modelo.intercept_)
# Fazendo uma inspeção visual
plt.scatter(X, y)
# Vamos agora preparar o ambiente para uma simulação -> usaremos 100 registros. Para essa simulação criaremos uma variável X_teste que receberá 100 registros iniciando em 10 e finalizando em 3000 (intervalo da coluna DESPESAS). Faremos uso do método linspace() acompanhe
X_teste = np.linspace(10, 3000, 100)
print('\nQuem é nossa variável X_teste? \n', X_teste)
# Usaremos X-teste para fazermos uma previsão com nosso modelo. Acompanhe -> criaremos uma função para essa ação +> observe o uso de uma sgmoide muito comum em redes Neurais
def model(x):
    return 1 / (1 + np.exp(-x))
# Vamos criar agora uma variável r de resultado para a qual passamos os valores -> observe o uso do método .ravel() que vai transformar o numpy array do formato de matriz para o formato de vetor. r nos fornece o erro do modelo
r = model(X_teste * modelo.coef_ + modelo.intercept_).ravel()
# Inspecionado visulamente
plt.plot(X_teste, r, color = 'red')
plt.show()
# Modelo preparado e testado vamos agora usar o modelo para prever o que acontecerá com os candidatos presentes na base NovosCandidatos.csv -> queremos prever se serão ou não eleitos
# Precisamos carregar a nova base de dados
base_previsoes = pd.read_csv('D:/Users/Angelo/AULAS/Dados/NovosCandidatos.csv', sep=';')
# Vamos criar uma variável despesas -> não se esqueça do reshape()
despesas = base_previsoes.iloc[:, 1].values
despesas = despesas.reshape(-1, 1)
# Podemos agora realizar nossa previsão
previsoes_teste = modelo.predict(despesas)
print('\nOs candidatos com grande chance de serem eleitos são:\n', previsoes_teste)
# Para melhor visualizar podemos usar o seguinte:
base_previsoes = np.column_stack((base_previsoes, previsoes_teste))
print('\nVisualizando os candidatos e sua classificaçao em razão de suas despesas de campanha\n', base_previsoes)
