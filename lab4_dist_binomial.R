# Title     : Distribuicao Binomial
# Objective : Neste laboratorio serao exploradas as ferramentas R para o calculo da distribuicao Binomial
# Created by: accol
# Created on: 22/05/2020

# dbinom() -> Encontra a probabilidade => requer tres parametros: X -> o numero de sucesso que deseja
# sixe -> o numero de experimentos; Probabilidade -> a probabilidade de ocorrencia do evento
# pbinom() -> Cumulativa

# Neste experimento jogar uma moeda 5 vezes e obter cara 3 vezes
tres_caras = dbinom(3, 5, 0.5)
print('Tres caras')
print(tres_caras)
# Neste experimento a ideia e passar por quatro semaforos de 4 tempos cada. Qual a probabilidade de voce pegar nenhum,
# um dois três ou quatro semaforos abertos?
# Vamos resolver por partes -> encontrando a probabilidade para cada caso:
nenhum_verde = dbinom(0, 4, 0.25)
um_verde = dbinom(1, 4, 0.25)
dois_verde = dbinom(2, 4, 0.25)
tres_verde = dbinom(3, 4, 0.25)
quatro_verde = dbinom(4, 4, 0.25)
print('Semaforos de 4 tempos')
print(nenhum_verde)
print(um_verde)
print(dois_verde)
print(tres_verde)
print(quatro_verde)
# Uma forma de calcular a probabilidade cumulativa diretamente e atraves do pbinom()
acumulado = pbinom(4, 4, 0.25)
print('Valor acumulado dos 4 semaforos')
print(acumulado)
# Outro exemplo. Imagine uma prova de 12 questoes de multipla escolha (4) apenas uma certa. Qual a chance de acertar
# 7 questoes chutando todos os resultados?
acerta_7 = dbinom(7, 12, .25)
print('Acertando 7 questoes no chute')
print(acerta_7)
