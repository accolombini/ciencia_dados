# Title     : Distribuição de Poisson
# Objective : Conhecer como o R poderá nos apoiar no cálcuo e análise da Distribuição de Poisson
# Created by: accol
# Created on: 30/05/2020


# Neste laboratório queremos analisar o seguinte fato. Em uma determinada localização corre uma média de 2 acidentes por dia. Queremos inicialmente saber qual a probabilidade de ocorrer extamente três acidentes em um único dia? Logo temos x = 3 e λ = 2

prob3 = dpois(3, 2)
cat('\nA probabilidade de ocorrer três acidentes é de:\n', round(prob3 * 100, 2), '%')

# Como segundo problema queremos saber qual a probabilidade de ocorrerem 3 ou menos acidentes em um único dia. x <= 3 λ = 2. Note que estamos usando o default de lower.tail que é TRUE

prob_menorigual3 = ppois(3, 2)
cat('\nA probabilidade de ocorrer três acidentes ou menos é de:\n', round(prob_menorigual3 * 100, 2), '%')

# Neste último problema queremos saber qual a probabilidade de ocorrerem mais de 3 acidentes em um único dia. x > 3 e λ = 2. Problema do tipo maior que -> observe

prob_maior3 = ppois(3,2,lower.tail = F)
cat('\nA probabilidade de ocorrer mais de três acidentes é de:\n', round(prob_maior3 * 100, 2), '%')
