# Title     : CORRELACAO -> REGRESSÃO LINEAR SIMPLES
# Objective : Conhecer o que R tem a nos oferecer para trabalhar com CORRELAÇÃO
# E REGRESSÃO LINEAR SIMPLES
# Created by: accol
# Created on: 27/05/2020

# Vamos usar o Banco de Dados Cars (nativo do R) -> queremos saber a distância percorrida pelo carro, a partir do momento da frenagem

print(dim(cars))
# Vamos observer os registros da base de dados cars
print(head(cars))
print(tail(cars))
# Vamos agora verificar se existe uma correlação entre as duas variáveis (velocidade x distância)
print(cor(cars))
correlacao = cor((cars))
print(correlacao)

# Descoberta a correlação e neste caso temos uma correlação forte e positva (0.8068)
# O próximo passo é a criação do modelo para as análises. O R facilita nossa vida neste quesito, vamos usar a função lm que tem como parâmetros as variáeis e a base de dados, acompanhe
modelo = lm(speed ~ dist, data = cars)
# Vamos visualizar o modelo
print(modelo)
# Fazendo uma inspeção gráfica no modelo
plot(modelo)
# Agora faremos um gráfico do modelo definindo os parâdero desejados
plot(speed ~ dist, data = cars)
# Vamos agora criar a linha de melhor ajuste usando a função abline() que recebe como parâmetro o modelo gerado => observe
abline(modelo)
# Como exercício vamos tentar prever através de regressão liner qual a velocidade do veículo se a distância percorrida for de 22 pés
# Lembrabdo, precisamos encontrar o ponto de inteceptação
modelo$coefficients
# Para calcular, vamos precisar do primeiro ponto de intercptação + o segundo ponto multiplicado pela distância
velocidade_22pes = modelo$coefficients[1] + modelo$coefficients[2] * 22
print(velocidade_22pes)
# Outra forma de resolver o problema é usando a função predic() -> nesta função passa-se um DataFrame com os valores conhecidos, neste caso, seria algo como:
velocidade_22pes_predict = predict(modelo, data.frame(dist = 22))
print(velocidade_22pes_predict)
velocidade_50pes_predict = predict(modelo, data.frame(dist = 50))
print(velocidade_50pes_predict)
# Vamos visualizar um sumário do nosso modelo
summary(modelo)
# Além dos coeficientes podemos obter outras informações do modelo =>> observe
modelo$coefficients
print(modelo$model)
# Valores ajustados =>> são os valores usados para gerar a linha de melhor ajuste
print(modelo$fitted.values)
# Vamos comparar esse resultado com car dist num gráfico, observe >-
plot(modelo$fitted.values, cars$dist)
