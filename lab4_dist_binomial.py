# Title     : Distribuicao Binomial
# Objective : Neste laboratorio serao exploradas as ferramentas Python para o calculo da distribuicao Binomial
# Created by: accol
# Created on: 22/05/2020

from scipy.stats import binom


# Nesta pratica vamos lancar uma moeda 5 vezes, qual a probabilidade de dar cara 3 vezes?
# Vamos usar a funcao binom.pmf() que necessita de 3 argumentos (sucesso_desejado, numero_experimentos, probabilidade)
prob = binom.pmf(3, 5, 0.5)
print('\nProbabilidade de obter 3 caras em 5 lancamentos de uma moeda: ', prob)
# Agora queremos passar por 4 semaforos de 4 tempos, qual a probabilidade de pegar sinal verde em (nenuma, uma, duas, tres ou quatro vezes). Observe que estamos varrendo todo espaco amostral
prob_zero = binom.pmf(0, 4, 0.25)
prob_um = binom.pmf(1, 4, 0.25)
prob_dois = binom.pmf(2, 4, 0.25)
prob_tres = binom.pmf(3, 4, 0.25)
prob_quatro = binom.pmf(4, 4, 0.25)
print('\nA chance de pegar zero semaforos em verde e: ', prob_zero)
print('\nA chance de pegar um semaforos em verde e: ', prob_um)
print('\nA chance de pegar dois semaforos em verde e: ', prob_dois)
print('\nA chance de pegar tres semaforos em verde e: ', prob_tres)
print('\nA chance de pegar quatro semaforos em verde e: ', prob_quatro)
# Vamos agora considerar para efeito de ensaio que nosso semafaro seja de dois tempos, qual a chance de pegarmos 4 semafaros em verde?
prob_tempos_dois = binom.pmf(4, 4, 0.5)
print('\nA chance de pegar quatro semaforos em verde quando forem de dois tempos e: ', prob_tempos_dois)
# Vamos agora calcular a probabilidade cumulativa. Usaremos a funcao binom.cdf() que demanda os mesmos tres argumentos
prob_acumulativa = binom.cdf(4, 4, 0.25)
print('\nA probabilidade cumulativa para os semafaros de quatro tempos e: ', prob_acumulativa)
# Agora, considere um concurso com 12 questoes objetivos com 4 alternativas e apenas uma correta. Qual a probabilidade de acertar 7 questoes supondo que tera que chutar as doze?
sucesso_concurso = binom.pmf(7, 12, 0.25)
print('\nChance de sucesso em teste com 12 questoes de quatro alternativas -> requisito minimo 7 acertos >- chutando todas as questoes e:', sucesso_concurso)
# Caso queira o resultado em porcentagem, basta multiplicar por 100
sucesso_concurso_p = binom.pmf(7, 12, 0.25) * 100
print('\nChance de sucesso em teste com 12 questoes de quatro alternativas -> requisito minimo 7 acertos >- chutando todas as questoes e:', sucesso_concurso_p, '%')
# Imangine agora que deseje acertar todas as questoes nas mesmas condicoes acima
sucesso_concurso_todas = binom.pmf(12, 12, 0.25) * 100
print('\nChance de sucesso em teste com 12 questoes de quatro alternativas -> 12 acertos >- chutando todas as questoes e:', sucesso_concurso_todas, '%')
