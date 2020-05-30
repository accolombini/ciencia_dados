# Title     : Teste de Qui quadrado
# Objective : Conhecer como a linguagem Python pode contribuir para a análise de hipóteses com o teste do Qui quadrado
# Created by: accol
# Created on: 30/05/2020

# Para esse laboratório que avaliar se assistir ou não novelas entre homens e mulheres >>- se há uma relação entre as variáveis. Como hipótese nula ||> Admitimos que não há uma relação a menos do mero acaso!
# Criaremos uma matriz de duas linhas e duas colunas passando os dados referente a assistir ou não novelas (colunas) e sexo serão as linhas (masculino e feminino)


import numpy as np
from scipy.stats import chi2_contingency


# Vamos agora criar a nossa base de dados para os trabalhos
novela = np.array([[19, 6], [43, 32]])
print('\nInspecionando nossa matriz de trabalho\n', novela)
# Para realizarmos o teste de Qui quadrado >- é bem simples observe
quiquadrado = chi2_contingency(novela)
print('\nResultado do teste de Qui quadrado para a nossa matriz novela:\n', quiquadrado)
# Observe que nosso valor de p = 15.35% -> portanto, maior que α = 5% logo não podemos descartar a hipótese H0