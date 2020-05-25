# Title     : Distribuição T de Student
# Objective : Uso de Python para manipular dados que atendam à distribuição T de Student
# Created by: accol
# Created on: 25/05/2020

# Ferramentas que estão disponíveis no Python


from scipy.stats import t 


# Problema 1: Media de salário dos cientistas de dados = R$ 75,00 por hora. A amostra é de 9 funcionários e o desvio padrão da amostra é 10
# Qual a probabilidade de selecionar um cientista de dados com salário com salário inferior a R$ 80,00 a hora?


# Estamos trabalhando com problemas do tipo menor que, logo usaremos a função cdf() >- usaremo t = 1,5 extraído da tabela e os demais parâmetros conforme enunciado tø = (9 -1) = 8

prob1 = t.cdf(1.5, 8)
print('\nA probabilidade de selecionar um cientista de dados com salário inferior a 80,00 é: ', prob1)

# Problema 2: Media de salário dos cientistas de dados = R$ 75,00 por hora. A amostra é de 9 funcionários e o desvio padrão da amostra é 10
# Qual a probabilidade de selecionar um cientista de dados com salário com salário maior de R$ 80,00 a hora?

# Estamos trabalhando com problemas do tipo maior que, logo usaremos a função sf() >- usaremo t = 1,5 extraído da tabela e os demais parâmetros conforme enunciado tø = (9 -1) = 8

prob2 = t.sf(1.5, 8)
print('\nA probabilidade de selecionar um cientista de dados com salário superior a 80,00 é: ', prob2)

# Podemos obter o mesmo resultado em % multiplicando por 100
print('\nA probabilidade de selecionar um cientista de dados com salário superior a 80,00 é: ', prob2 * 100, '%')

# Verificando os resultados com base no conceito de que a probabilidade é cumulativa a partir da esquerda >- deve ser igual a unidade
print('\nA probabilidade total dos slarios cientista de dados é: ', prob1 + prob2)
# Podemos encontra o valor de prob2 realizar subtraindo prob1 da unidade, observe
print('\nA probabilidade de selecionar um cientista de dados com salário superior a 80,00 é: ', (1 - prob1) * 100, '%')
