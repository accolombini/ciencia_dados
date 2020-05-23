# Neste laboratorio estaremos trabalhando com as ferramentas disponiveis de Python para medidas de centralidade

import numpy as np
from scipy import stats


jogadores = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]
# Vamos calcular a media
media_salarios = np.mean(jogadores)
print('O valor da media salarial dos jogadores e: ', media_salarios)
# Calculo da mediana
mediana_salarios = np.median(jogadores)
print('\nO valor da mediana salarial dos jogadores e: ', mediana_salarios)
# Calculo dos quartis => note que temos que definir quais os quartis que queremos calcular
quartis_salarios = np.quantile(jogadores, [0, 0.25, 0.5, 0.75, 1])
print('\nVisao geral dos quartis: ', quartis_salarios)
# Calculo do desvio padrao do salario dos jogadores => observe que o resultado e diferente do obtido em R
dpadrao_salarios = np.std(jogadores)
print('\nO desvio padrao do salario dos jogadores e: ', dpadrao_salarios)
# Calculo do desvio padrao do salario dos jogadores => observe os parametros necessarios para obter o mesmo resultado de R (em R o parametro ddof utiliza no denominador (n-1) e no Python apenas (n) =>> para tornar os resultados equivalentes voce devera corrigir isso)
dpadrao_ddof_salarios = np.std(jogadores, ddof=1)
print('\nO desvio padrao corrigido para R do salario dos jogadores e: ', dpadrao_ddof_salarios)
# Uma forma rapida de visualizar todos os parametros de centralidade de uma base de dados e com o uso do metodo describe()
resumo_salarios = stats.describe(jogadores)
print('\nO resumo das medidas de centralidade do salario dos jogadores e: \n\n', resumo_salarios)
