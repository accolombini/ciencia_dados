# Neste laboratoria trabalharemos com recursos Python para manipulacao de amostras

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from math import ceil


base = pd.read_csv('D:\\Users\Angelo\AULAS\Dados\iris.csv')
print(base)
# Explorando os dados
print('\nInspecao inicial nos dados')
print(type(base))
print(base.head(10))
print(base.tail(10))
print('\nA dimensao do arquivo iris')
print(base.shape)
print('\nUma primeira inspecao atraves da estatistica descritiva')
print(base.describe())

print('\nVamos agora trabalhar com as Amostras vamos usar o metodo choice()')
# O metodo choice() aceita 4 parametros, o primeiro define os valores que serao sorteados (0 ou 1) o segundo o tamanho da amostra (150) o terceiro nos diz se sera com ou sem reposicao (no caso com reposicao) e o quarto a probabilidade de ocorrencia de cada elemento (0 -> 50% ou 1 -> 50%)

amostra = np.random.choice(a=[0,1], size=150, replace=True, p=[0.5, 0.5])
print(amostra)
print('\nOlhando para nossa amostra')
print(len(amostra))
print('Amostra = 0: ', len(amostra[amostra == 0]))
print('Amostra = 1: ', len(amostra[amostra == 1]))

# Para garantirmos a repetibilidade da amostra podemos usar uma semente para gerar a amostra o que e util caso voce precise repetir o experimento assegurando o mesmo resultado, veja a seguir
np.random.seed(25) # Definindo a semente para garantir a reproducao dos dados => lembre de comentar essa linha quando quiser gerar valore diferentes!
amostra1 = np.random.choice(a=[0,1], size=150, replace=True, p=[0.5, 0.5])
print(amostra1)
print('\nOlhando para nossa amostra fazendo uso de uma semente')
print(len(amostra1))
print('Amostra1 = 0: ', len(amostra1[amostra1 == 0]))
print('Amostra1 = 1: ', len(amostra1[amostra1 == 1]))

# Vamos agora fazer amostragem estratificada no Python vamos precisar importar a funcao train_test_split da biblioteca sklearn -> acompanhe

print('\nTrabalhando com amostras estratificadas')
# primeiramente vamos carregar a base:
iris = pd.read_csv('D:\\Users\Angelo\AULAS\Dados\iris.csv')
print('\nVamos agora fazer uma contagem da base pela coluna classificacao => "class"')
print(iris['class'].value_counts())

# Nosso desafio sera gerar uma amostra com 75% dos dados da base iris
print('\nPara essa tarefa faremos uso da funcao train_test_split de sklearn')
# A funcao train_test_split => dividira nossa base da forma que especificarmos, no caso, queremos selecionar 50% dos registros, mas queremos que eles contenham 50% de cada dado classificado, ou seja, setosa, versicolor e virginica >>= atento ao uso da funcao. Na variavel X teremos nossa amostra e na variavel Y teremos a classe, Nota >>= o traco logo apos o nome da variavel, por exemplo, X, _ serve para evitar que o restante da variavel nao seja carregada (em outras palavras na variavel que substituiria o _ seria carregada o complemento da base de dados)
X, _,y, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4], test_size=0.5, stratify=iris.iloc[:, 4])
print('\nOlhando para nossas variaveis <$>')
print('\nA variavel X:\n', X)
print(X.shape)
print('\nA variavel y:\n', y)
print(y.shape)
# Verificando se a estratificacao esta correta
print('\nResultado da estratificacao contando valores de y </>')
print(y.value_counts())

# Vamos agora fazer outro experimento, para isso usaremos a base de dados chamada infert
infert = pd.read_csv('D:\\Users\Angelo\AULAS\Dados\infert.csv')
print(infert)
# Explorando os dados
print('\nInspecao inicial nos dados')
print(type(infert))
print(infert.head(10))
print(infert.tail(10))
print('\nA dimensao do arquivo iris')
print(infert.shape)
print('\nUma primeira inspecao atraves da estatistica descritiva')
print(infert.describe())
# Neste exemplo nosso foco sera o atributo education (anos de escolaridade)
print('\nAvaliando o atributo Education na base infert')
print(infert['education'].value_counts())
# Queremos avaliar de forma justa, observe que o atributo education difere em quantidade para os tempos de estudo sob analise. Como sabemos a base infert contem 248 registros, queremos uma amostra de apenas 100 registros e precisamos que ela atenda a uma distribuicao honesta, todos particiapando dentro de sua proporcao na base infert. Para isso, o primeiro passo sera encontrar a proporcao: q_atributo / total_registros * q_amostra. Observe novamente o uso do <$> __. O que seignifica o 0.6? Lembre-se estamos trabalhando com proporcoes para compor nossa amostra de 100 elementos, no caso 0.6 x 248 = 148, ou seja, me sobram exatamente 100 registros para minha amostra </> Para aumentar a precisao deveriamos realizar os devidos arredondamentos, lembre-se disso >>= para este laboratorio a precisao nao e fator critico de sucesso

X1, _, y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1], test_size=0.6, stratify=infert.iloc[:, 1])
print('\nVamos agora conferir na variavel y1 se na nossa amostra temos os valores desejados por ano de escolaridade')
print(y1.value_counts())

# Vamos agora trabalhar com amostragem sistematica => nao temos ou eu nao conheco uma biblioteca especifica para este fim, logo faremos da forma tradicional >>= usaremos a biblioteca math e a funcao ceil. Importante => note que os valores definidos a seguir nao foram definidos por acaso e sim, com base no numero de registro encontrado em nossa base de dados iris

populacao = 150
amostra2 = 15
# A funcao ceil fara o arredondamento da nossa divisao para cima => veja a seguir:
k = populacao / amostra2
print('\nObserve o valor de k sem usar a funcao ceil: ', k)
k = ceil(populacao / amostra2)
print('\nObserve o valor de k usando a funcao ceil: ', k)
# Para definirmos a aleatoriedade faremos um sorteio entre 1 e o valor de k. Vamos usar o metodo randint (gera numeros randomicos inteiros) => vamos precisar de tres parametros o primeiro sera o limite inferior, o segundo o limite superior (observe que usaremos k + 1 => para que k seja incluso) e o terceiro sera o tamanho (que nos diz quantos numeros queremos gerar)>>= observe:
print('\nGerando um numero inteiro randomico entre 1 e k')
r = np.random.randint(low=1, high=k+1, size=1)
print('\nO valor de r gerado foi: ', r)
print('\nO tipo da variavel r e: ', type(r))
# Observe que r e um array numpy exatamente o que queremos para nossa atividade => agora vamos gerar uma variavel acumulador para acumular os valores gerados pelo gerador randomico

acumulador = r[0]
print('\nO valor de acumulador na posicao zero e: ', acumulador)
# Note que acumulador e um escalar => lembre-se que na amostragem sistematica apenas o primeiro valor e aleatorio, os demais serao acrescidos de um valor fixo definido, no caso deste exemplo, sera o valor de k
print('\nVamos criar uma lista vazia que depois no laco for sera preenchida com os valores randomicos')
sorteados = []  # Cria uma lista vazia de nome sorteados
for i in range(amostra2):
    sorteados.append(acumulador)
    acumulador += k
print('\nVamos ver o que temos em sorteados: ', sorteados)

# Vetor construido, vamos agora gerar nossa amostra a partir de nosso base de dados iris <=> base. O que temos que fazer e retornar os registros desta base conforme definido em sorteados

base_final = base.loc[sorteados]
print('\nPor fim, nossa amostra sistematica para a base iris e \n', base_final)
