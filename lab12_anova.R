# Title     : ANOVA
# Objective : Conhecer os recursos de R que podem nos apoiar no ANOVA => Análise de Variância
# Created by: accol
# Created on: 30/05/2020

# Para este laboratório vamos usar a base de dados anova.csv -> atençao esta base de dados possui cabeçalho e usa como separador o ';' (ponto e vígula -> não a ',' que seria o default |> acompanhe

tratamento = read.csv('D:/Users/Angelo/AULAS/Dados/anova.csv', sep = ';', header = T)
cat('\nInspeção rápida na base de dados anova\n')
print.table(tratamento)
print.table(head(tratamento))
# Vamos conhecer a dimensão de nossa tabela
cat('\nA dimensão da nossa base de dados -> tratamento é: ', dim(tratamento))
# Vamos também fazer uma rápida inspeção visual na nossa base -> usaremos boxplot => por hora queremos observar duas variáveis apenas -> HORAS e REMEDIO (há três)
boxplot(tratamento$Horas ~ tratamento$Remedio)
# Primeiramente vamos fazer o teste de Variância de um fator (Remédios e Horas) e depois de dois fatores (Remédios Horas e Sexo)
an = aov(Horas ~ Remedio, data = tratamento)
summary(an)
# Observe o P value = 0.592
# Agora vamos adicionar uma variável -> Remedio e Sexo são variáveis Independentes -> Horas nossa variável dependente
andois = aov(Horas ~ Remedio * Sexo, data = tratamento)
summary(andois)
# Importante que você analise os valores P para as três variáveis ||> Remedio -> 0.596; Sexo -> 0.311 e Remedio:Sexo -> 0.440
# Vamos agora a partir dos objetos criados realizar o teste de Tukey visto que nossa análise constata que há uma variância

tukey = TukeyHSD(an)
cat('\nResultado do teste de Tukey\n')
print(tukey)
# Podemos observar graficamente como se comporta nossa Variação sob o teste de Tukey -> nos mostra a variação média dos efeitos dos medicamentos A, B e C em termos de horas -> nossa variável dependente
plot(tukey)
