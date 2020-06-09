# Title     : REGRAS DE ASSOCIAÇÃO
# Objective : Conhecer com a linguagem Python pode potencializar a mineração de dados com foco na construção de ASSOCIAÇÕES usando o algoritmo APRIORI
# Created by: accol
# Created on: 09/06/2020

# Precisaremos instalar um novo pacote => pip install apyori
# Esta prática exige a instalação do pacote "arules"
# As regras serão carregadas a partir de um arquivo .txt no formato de cesta de compras, onde cada linha representa uma transação e os produtos são separados por vírgulas


import pandas as pd 
from apyori import apriori


dados = pd.read_csv('D:/Users/Angelo/AULAS/Dados/transacoes.txt')
print('\nPodemos agora visualizar os dados\n', dados)
# Vamos agora eliminar o header
dados = pd.read_csv('D:/Users/Angelo/AULAS/Dados/transacoes.txt', header=None)
print('\nPodemos agora visualizar os dados sem header\n', dados)
# Precisamos agora fazer alterações na variável para ajustar os cálculos
transacoes = []
for i in range(0,6):
    transacoes.append([str(dados.values[i,j]) for j in range(0,3)])
print('\nVamos observar a variável transações\n', transacoes)

# Vamos agora gerar as regras -> vamos ajustar suporte e confiança para 0.5
regras = apriori(transacoes, min_support = 0.5, min_confidence = 0.5)
resultados = list(regras)
print('\nAs regras geradas são:\n', resultados)
resultados2 = [list(x) for x in resultados]
print('\nAs regras geradas melhoradas são:\n', resultados2)
resultados3 = []
for j in range(0,7):
    resultados3.append([list(x) for x in resultados2[j][2]])
print('\nAs regras geradas melhoradas são:\n', resultados3)
