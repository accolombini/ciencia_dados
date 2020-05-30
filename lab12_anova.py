# Title     : ANOVA
# Objective : Conhecer os recursos de Python que podem nos apoiar no ANOVA => Análise de Variância
# Created by: accol
# Created on: 30/05/2020

# Para este laboratório vamos usar a base de dados anova.csv -> atençao esta base de dados possui cabeçalho e usa como separador o ';' (ponto e vígula -> não a ',' que seria o default |> acompanhe


import pandas as pd 
import matplotlib.pyplot as plt
import statsmodels.api as sm 
from statsmodels.formula.api import ols
from scipy import stats
from statsmodels.stats.multicomp import MultiComparison     # Requisito para teste de Tukey -> comparação


# Vamos carregar a base de dados anova.csv => Lembrando que nossa variável de resposta será as HORAS ||> quanto tempo que o medicamento levou para fazer efeito
tratamento = pd.read_csv('D:/Users/Angelo/AULAS/Dados/anova.csv', sep=';')
# Façamos uma rápida inspeção em nossa base de dados
print('\nDimensão da base: ', tratamento.shape)
print('\nPrimeiros registros da base: \n', tratamento.head())
print('\nSumário da base: \n', tratamento.describe())
# Vamos fazer uma rápida inspeção gráfica -> usando boxplot e agrupando por Remédio => temos Remédio A, Remédio B e Remédio C
tratamento.boxplot(by='Remedio', grid = False)
plt.show()
# Antes de usarmos o método ANOVA no Python precisaremos usar o método OLS -> Ordinary Lest Square (realizamos uma Regressão para só depois efetivamente trabalharmos com o ANOVA)
# Vamos criar um modelo usando Horas como variável de Resposta e Remedio como variável independente e vamos usar o fit() para fazer efetivamente o treinamento do nosso modelo
modelo1 = ols('Horas ~ Remedio', data=tratamento).fit()
resultado1 = sm.stats.anova_lm(modelo1)
print('\nO resultado da ANOVA\n', resultado1)
# Observe que nosso valor de P foi de 0.591966 -> este é o valor que deve ser comparado com seu valor de α para que possa validar ou não sua Hipótese 0 => no caso sim
# Como nosso segundo problema vamos criar um teste com dois atributos -> para isso, vamos criar o modelo2 no qual trabalharemos com a variável Horas como variável de resposta e as variáveis Remedio e Sexo como variáveis independentes
modelo2 = ols('Horas ~ Remedio * Sexo', data=tratamento).fit()
resultado2 = sm.stats.anova_lm(modelo2)
print('\nO resultado da ANOVA para duas variáveis independentes\n', resultado2)
# Novamente observe os valores de P para cada variável -> Temos P para Remedio; P para Sexo e P para a combinação do Remedio com o Sexo. Você deve comparar esses valores de P com seu valor de α -> achando que há uma variação significativa precisaremos recorrer ao teste de Tukey
mc = MultiComparison(tratamento['Horas'], tratamento['Remedio'])
resultado_teste = mc.tukeyhsd()
print('\nResultado do Teste de Tukey para a variável Remedio\n', resultado_teste)
# Fazendo uma inseção gráfica temos o plot_simultaneous() específico para este tipo de análise
resultado_teste.plot_simultaneous()
plt.show()
# Olhando agora só para execrcitar para a variável Sexo
mc1 = MultiComparison(tratamento['Horas'], tratamento['Sexo'])
resultado_teste1 = mc1.tukeyhsd()
print('\nResultado do Teste de Tukey para a variável Sexo\n', resultado_teste1)
