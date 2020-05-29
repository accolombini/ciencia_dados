# Title     : Regressão Linear Múltipla
# Objective : Estudar os recursos da linguagem R que poderão contribuir no processo de Regressão Linear Múltipla
# Created by: accol
# Created on: 28/05/2020

# Neste laboratório usaremos um banco de dados Nativo do R mt_cars.csv -> compara 11 características (atributos) de veículos num total de 32 registros

# Fazendo uma inspeção nos dados

print(head(mtcars))
print(tail(mtcars))
print(summary(mtcars))
cat('As colunas ou atributos da base de dados são: \n', colnames(mtcars))
cat('\nA dimensão da base de dados é \n', dim(mtcars))

# Inicialmente vamos trabalhar com REGRESSÃO LINEAR SIMPLES </>
# Neste exemplo queremos avaliar o consumo mpg por polegadas cúbicas -> variáves mpg e disp
# Inicialmente -> vamos olhar para as 4 colunas iniciais (supondo que estou descobrindo onde as variáveis estão) e avaliar a correlação entre estes atributos
cat('\nFazendo a correlação entre os quatro atributos iniciais \n')
cor(mtcars[1: 4])

# Da resultante da correlação, podemos perceber que há uma correlação negativa forte
# Vamos criar um modelo de regressão Simples, com uma variável exploratória X (independente) e uma variável dependente Y (aquilo que se deseja prever)
# Para este exercício usaremos o atributo/variável mpg  -> como variável de resposta Y (queremos prever -> variável dependente) e como variável exploratória usaremos o atributo/variável disp nosso X
modelo = lm(mpg ~ disp, data = mtcars)
cat('\nCaracterísticas do modelo linear \n')
print(modelo)
# Vamos agora calcular o COEFICIENTE DE DETERMINAÇÃO R² => nos fornece o quanto de nossas variáveis independetes explicam a variável dependente
summary(modelo)$r.squared
# Obtivemos um bom coeficiente de determinação aproximadamente 72% das nossas variáveis independetes (exploratórias) explicam nossa variável dependente. Lembre-se que, quando temos mais de uma variável exploratória, corremos o risco de inflacionar o valor de R² de forma imprópria
# Para minimizar esse impacto, vamos agora determinar o coeficiente de determinação R² ajustado >- observe a seguir:
summary(modelo)$adj.r.squared
# Note que nosso coeficiente de determinação ajustado R² caiu para 70% -> ainda assim, podemos concluir que temos um bom modelo
# Vamos agora fazer uma inspeção visual entre as variáveis sob estudo (mpg -> Y) e (disp -> X)
plot(mpg ~ disp, data = mtcars)
# Para melhor visualizarmos a correlação entre as variáveis vamos gerar a linha de melhor ajuste
abline(modelo)
# A partir daqui -> atendemos as condições para o uso de Regressão, vamos usar nosso modelo para fazermos previsões >- No caso, usaremos um veículo com disp = 200 (polegadas cúbicas) e queremos saber qual o consumo em galões por milhas
predict(modelo, data.frame(disp=200))
# Vamos agora trabalhar com Regressão Multivariável >- para isso, vamos acrescentar mais duas variáveis Hp (cavalos e número de cilindros (cyl) -> como variáveis exploratórias (conhecidas -> X1, X2, X3) para explicar o consumo (variável dependente -> Y)
# O rpimeiro passo será criar um modelo de Regressão Linear Múltipla
modelo_mult = lm(mpg ~ disp + hp + cyl, data = mtcars)
# Vamos observar nosso coeficiente de variação R² -> devemos esperar que seja maior que o anterior, uma vez que, temos mais variáveis para explicar nossa variável dependente
summary(modelo_mult)$r.squared
# Vamos também observar nosso R² ajustado
summary(modelo_mult)$adj.r.squared
# Vamos agora fazer uma previsão multivariável
predict(modelo_mult, data.frame(disp = 200, hp = 100, cyl = 4))
