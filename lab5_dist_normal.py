# Title     : Distribuicao Normal
# Objective : Apresentar as ferramentas em Python para suporte a aplicacoes com Distribuicao Normal
# Created by: accol
# Created on: 23/05/2020

# Calculo da distribuicao normal no Python


from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt


# Conjunto de objetos em uma cesta, a media e 8 e o desvio padrao e 2 => Queremos saber qual a probabilidade
# de tiramos um objeto ao acaso e seu peso ser inferior a 6 quilos?
# Vamos usar a função norm.cdf() -> usada quando buscamos por um valor do tipo "menor que" tem como primeiro parâmetro o valor alvo (no caso 6 quilos), o segundo parâmetro é a média e o terceiro o desvio padrão

menor_seis = norm.cdf(6, 8, 2)
print('\nA probabilidade de retirar um objeto com menos de 6 quilos da cesta é: ', menor_seis)

# Neste problema, queremos saber a probabilidade de retiramos um objeto que o peso seja maior que 6 quilos? Quando usamos o conceito de maior, precisamos fazer uso de outra funcao >- norm.sf() => usamos os mesmos três artumentos

maior_seis = norm.sf(6, 8, 2)
print('\nA probabilidade de retirar um objeto com mais de 6 quilos da cesta é: ', maior_seis)

# Neste problema, queremos saber a probabilidade de retiramos um objeto que o peso é menor que 6 quilos ou maior que 10 quilos? Quando usamos o conceito de menor ou maior, precisamos fazer um somatório das probabilidades

menor_seis_maior_dez = norm.cdf(6, 8, 2) + norm.sf(10, 8, 2)
print('\nA probabilidade de retirar um objeto com mais de 6 quilos da cesta é: ', menor_seis_maior_dez)

# Neste problema, queremos saber a probabilidade de retiramos um objeto que o peso seja menor que 10 quilos e maior que 8 quilos? Note a falta da cláusula "ou", neste caso é preciso estar "entre" 8 "e" 10 ||> precisamos subtrair. Fique atento, pois embora, queremos que esteja entre 8 e 10, vamos subtrair menor de 10, por menor de 8. Para melhor entender pense no gráfico de sino

menor_dez_maior_oito = norm.cdf(10, 8, 2) - norm.cdf(8, 8,2)
print('\nA probabilidade de retirar um objeto com menos de 10 e mais de 8 quilos da cesta é: ', menor_dez_maior_oito)
# Caso prefira você poderá calcular considerando o uso do norm.sf() para os valores maior que
menor_dez_maior_oito_2 = norm.cdf(10, 8, 2) - norm.sf(8, 8,2)
print('\nA probabilidade de retirar um objeto com menos de 10 e mais de 8 quilos da cesta é: ', menor_dez_maior_oito_2)

# <$> AGORA FAREMOS TESTES PARA VERIFICAR SE A DISTRIBUICAO É OU NÃO NORMAL <$>
# Primeiro vamos criar uma variável para recener uma distribuição Normal gerada através de norm.rvs(size)
dados = norm.rvs(size=100)
print('\nOs dados gerados a partir do gerador de distribuição normal é:\n')
print(dados)
print(type(dados))
# Gerando o gráfico de distribuição Normal
g_normal = stats.probplot(dados, plot=plt)
plt.show(g_normal)
# Uma inspeção visual simples nos permite verificar que se trata de uma distribuição Normal

# Para confirmar faremos o teste de Shapiro-Wilk
shapiro_teste_hipotese = stats.shapiro(dados)
print('\nO resultado do teste de hipotese de Shapiro é: \n')
print(shapiro_teste_hipotese)
# Os resultados do teste de Shapiro confirmam a distribuição Normal dos dados
