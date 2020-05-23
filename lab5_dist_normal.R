# Title     : Distribuicao Normal
# Objective : Apresentar as ferramentas em R para suporte a aplicacoes com Distribuicao Normal
# Created by: accol
# Created on: 23/05/2020

# Calculo da distribuicao normal no R
# P[X < x]
# prnorm()
# P[X > x] => lower.tail = FALSE
# qnorm() => faz o processo inverso
# rnorm[] => gera numeros aleatorios normalmente distribuidos
# qqnorm[] => gera o teste de normalidade
# qqline[] => gera a linha de melhor ajuste (completando o qnorm) para comparacao
# shapiro.test[] => realiza o teste de SHAPIRO-WILK

# Neste exemplo temos uma caixa com objetos. Sabe-se que a media do peso e de  8 quilos, o desvio padrao e 2,
# e estao distribuidos de forma Normal => pede-se a chance de um objeto retirado da caixa pesar menos
# de 6 quilos ||> para esse exemplo simples, devemos lembrar que a probabilidade e cumulativa e que estamos
# trabalhando na regiao a esquerda da media (neste caso, nao precisamos subtrair de um)

# Vamos usar a funcao pnorm() que exige tres paraetros => o primeiro o que estou buscando >- no caso 6 quilos
# abaixo, o segundo parametro e a media e o terceiro o desvio padrao ||> problema do tipo menor que

menor_seis = pnorm(6, 8, 2)
print('A probabilidade de retirar um objeto com menos de 6 quilos e')
print(menor_seis)

# Neste segundo problema queremos saber qual a chance de retiramos um objeto com mais de 6 quilos ||> fique atento
# e acompanhe => trata-se de um problema do tipo maior que => lembra do parametro Lower Tail que normalmente vem
# setado como True

maior_seis = pnorm(6, 8, 2, lower.tail = F)
print('A probabilidade de retirar um objeto com mais de 6 quilos e')
print(maior_seis)

# Neste terceiro problema queremos saber qual a chance de retiramos um objeto com menos de 6 quilos ou mais
# de 10 quilos||> fique atento a clausula 'ou' e acompanhe => temos que encontrar a probabilidade de ser menor
# de 6 quilos e depois maior de 10 quilos, por fim somar as duas, ou entao, neste caso, basta encontrar uma e
# multiplicar por 2

menor_seis_maior_dez = pnorm(6, 8, 2) + pnorm(10, 8, 2, lower.tail = F)
print('A probabilidade de retirar um objeto com menos de 6 quilos ou mais de 10 quilos e:')
print(menor_seis_maior_dez)

# Nosso quarto problema nos pede para encontrarmos a probabilidade de retirarmos um objeto com menos de 10 quilos
# e com mais de 8 quilos ||> Note que estamos trabalhando com duas probabilidades na cauda a esquerda => neste
# caso, encontramos cada uma e subtraimos uma da outra, observe

menor_10_maior_8 = pnorm(10, 8, 2) - pnorm(8, 8, 2)
print('A probabilidade de retirar um objeto com menos de 10 quilos e mais de 8 quilos e:')
print(menor_10_maior_8)

# <$> AGORA VAMOS AOS TESTES >=> Queremos saber se uma distribuicao e ou nao normal <$>
# Primeiramente atraves do Histograma
# Para este exemplo, primeiramente vamos gerar dados uniformente distribuidos utilizando a funcao >- rnorm()

x = rnorm(100) # devera retornar 100 numeros seguindo uma distribuicao normal
print('Variavel gerada atraves de rnorm():')
print(x)

# Gerando o grafico de normalidade => primeiro usando qqnorm()
print('Gerando o grafico de normalidade, para inspecao visual')
print(qqnorm(x))
# Gerando o grafico de normalidade => primeiro usando qqline()
print('Gerando o grafico de linha, para melhorar a inspecao visual')
print(qqline(x))
# Gerando um histograma => primeiro usando hist()
print('Gerando historgrama, para melhorar a inspecao visual')
print(hist(x, main = 'Histograma da Distribuicao de X', xlab = 'Dados', ylab = 'Frequencia'))
# Usando agora o teste de Shapiro-Wilk |||> shapiro.test()
print('Usando o teste de Shapiro-Wilk => com os parametros normais')
print(shapiro.test(x))
# Note que pelos resultados estamos claramente com uma distribuicao NORMAL -> basta comparar o valor de p
# com seu valor de Alfa
