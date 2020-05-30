# Title     : Distribuição de Poisson
# Objective : Conhecer como o Python poderá nos apoiar no cálcuo e análise da Distribuição de Poisson
# Created by: accol
# Created on: 30/05/2020


from scipy.stats import poisson


# Neste laboratório queremos analisar o seguinte fato. Em uma determinada localização corre uma média de 2 acidentes por dia. Queremos inicialmente saber qual a probabilidade de ocorrer extamente três acidentes em um único dia? Logo temos x = 3 e λ = 2. Quando temos a palavra EXATAMENTE => usamos o método .pmf()
prob3 = poisson.pmf(3, 2)
print('\nA probabilidade de termos 3 acidentes em um dia é de: ', round(prob3 * 100, 2), '%')

# Neste segundo problema queremos saber qual a probabilidade de encontrarmos três ou menos acidentes em um único dia. Quando temos a palavra MENOS => usamos o método .cdf()
prob_menorigual3 = poisson.cdf(3, 2)
print('\nA probabilidade de termos 3 ou menos acidentes em um dia é de: ', round(prob_menorigual3 * 100, 2), '%')

# Neste segundo problema queremos saber qual a probabilidade de encontrarmos mais de 3 acidentes em um único dia. Quando temos a palavra MAIS/MAIOR => usamos o método .sf()
prob_maior3 = poisson.sf(3, 2)
print('\nA probabilidade de termos mais de 3 acidentes em um dia é de: ', round(prob_maior3 * 100, 2), '%')
