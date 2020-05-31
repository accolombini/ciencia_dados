# Title     : Outliers
# Objective : Entender como a linguagem Python pode nos ajudar com o tratamento de Outliers
# Created by: accol
# Created on: 30/05/2020


import matplotlib.pyplot as plt 
import pandas as pd 
from pyod.models.knn import KNN


# Para este laboratório vamos usar a já conhecida base de dados iris => vamos iniciar carregando nossa base
iris = pd.read_csv('D:/Users/Angelo/AULAS/Dados/iris.csv')
# Faremos a decteção dos Outliers utilizando boxplot => só estamos interessados para essa prática na coluna SepalWidth
plt.boxplot(iris.iloc[:, 1])
plt.show()
# De uma rápida inspeção visual podemos dizer que há três Outliers superiores e um inferior
# Caso não queira exibir os Outiliers no boxplot basta parametrizá-lo para isso, observe
plt.boxplot(iris.iloc[:, 1], showfliers=False)
plt.show()
# Imagine que você queira extrair do gráfico quais os valores que estão sinalizando a presença de Outliers em seu sistema (base de dados) ||> observe que vamos criar uma função a partir de nossa inspeção visual no gráfico
outliers = iris[(iris['sepal width'] > 4.0) | (iris['sepal width'] < 2.1 )]
print('\nOs valores dos Outliers são: ', outliers)
# No Python há uma série de pacotes para detecção de Outliers sendo um deles muito interessante chamado |||> Python Outlier Detection (PyOD)
# Para usarmos a biblioteca PyOD precisaremos fazer um reshape ajustando os dados ao requisito da biblioteca ||> acompanhe. Não se esqueça do .values para converter nossa variável para um numpy array e aí poder passar pelo processo de reshape
sepal_width = iris.iloc[:, 1].values
sepal_width = sepal_width.reshape(-1, 1)    # Não altera linhas e acrescenta uma coluna (-1, 1)
print('\nInspecionando nossa variável\n', sepal_width)
print('\nNossa variável tem o seguinte formato ', sepal_width.shape)
print('\nNossa variável é do tipo ', type(sepal_width))
# Agora vamos criar nosso detector de Outlier e treiná-lo com o método .fit()
detector = KNN()
detector.fit(sepal_width)
# Agora para visualizarmos nossos Outliers precisamos criar nosso previsor => acompanhe. Você deverá observer que existem valores 0s e valores 1s |||> os valores 1s indicam os pontos onde exitem Outliers
previsoes = detector.labels_
print('\nOs valores de previsoes são:\n', previsoes)
# Inspecionando nossos dados observamos a presença de 5 Outliers
