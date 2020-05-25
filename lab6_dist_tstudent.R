# Title     : Distribuição T de Student
# Objective : Uso de R para manipular dados que atendam à distribuição T de Student
# Created by: accol
# Created on: 25/05/2020

# Ferramentas que estão disponíveis no R
# P[X < x]
# pt() >- se for uma probabilidade do tipo menor que
# P[X > x] = lower.tail = FALSE >- se for uma probabilidade do tipo maior que

# Prática 1: cientistas de dados ganham em média 75,00 a hora, tamanho da amostra igual 9 com desvio
# padrão da amostra igual 10. Pergunta-se qual a probabilidade de selecionar um cientista de dados e
# o salário for menor que 80,00 a hora? Sabemos da tabela T que t = 1,5, assim temos:
# pt() >- exige dois parâmetros no caso em que temos um problema do tipo menor que >- o valor de t
# (extraído da tabela) e tø (n -1) = 8
probabilidade1 = pt(1.5, 8)
print(probabilidade1)

# Prática 2: qual a probabilidade de selecionar um cientista de dados com salário superior a 80,00?
# Note que se trata de um problema maior que >- devemos usar o parâmetro lower.tail
probabilidade2 = pt(1.5, 8, lower.tail=FALSE)
print(probabilidade2)

# Lembrando que a probabilidade é cumulativa a partir da esquerda, poderíamos encontrar o mesmo
# resultado fazendo:
probextra = 1 - probabilidade1
print(probextra)
# Caso queira confirmar o resultado, poderá verificar se a soma das duas probabilidades, no caso,
# dos problemas acima ser igual a 1 (100%)
probcem = probabilidade1 + probabilidade2
print(probcem)
