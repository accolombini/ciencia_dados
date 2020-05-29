# Title     : Regressão Logística -> Sucesso ou Fracasso
# Objective : Conhecer as ferramentas de R que podem nos apoiar no processo de Regressão Logística
# Created by: accol
# Created on: 29/05/2020

# Para este laboratório usaremos base de dados de campanha eleitoral -> eleicao.csv e novoscandidatos.csv
# Nesta prática queremos a partir dos dados da base eleicao.csv queremos prever se os candidados de novoscandidatos.csv serão ou não eleitos
# Na tabela eleicao.csv teremos o nome do candidato, a situação -> se ele foi eleito ou não e despesas -> quanto ele investiu na campanha


# Importando dados no R -> observe o uso da opção file.chose() => ela abrairá uma caixa de diálogo na qual você poderá selecionar o arquivo desejado. Note também que foi necessário definir o separador do arquivo e se há ou não um header >- acompanhe. Essa opção foi deixada como comentário para que você saiba que pode contar com ela em caso de necessidade, na prática usaremos a leitura direta do diretório

#eleicao = read.csv(file.choose(), sep = ';', header = T)
eleicao = read.csv('D:/Users/Angelo/AULAS/Dados/Eleicao.csv', sep = ';', header = T)
#fix(eleicao) # -> é uma forma de exibir a tabela caso esteja numa ide sem muitos recursos
# Vamos fazer uma inspeção gráfica na base de dados -> analisando a situação (eleito ou não) com as despesas (investimento em campanha)
plot(eleicao$DESPESAS, eleicao$SITUACAO)
# Vamos agora gerar um sumário dos nossos dados
summary(eleicao)
# Vamos agora verificar se existe uma correlação entre a Situação e as Despesas
analise1 = cor(eleicao$DESPESAS, eleicao$SITUACAO)
cat('\nA correlação entre as despesas (investimento) e a situação (eleito ou não) é:\n', analise1)
# Observe que a correlação é de 81% -> portanto, há uma boa correlação entre as variáveis Despesas e Situação
# Assim podemos agora passar para a criação do nosso modelo vamos usar a função glm() que diferente do lm() cria vários tipos de regressões lineares -> sendo que o Tipo devemos passar por parâmetro -> no caso vamos usar family='binomial' para trabalharmos com regressão logística
modelo = glm(SITUACAO ~ DESPESAS, data = eleicao, family = 'binomial')
# criado o modelo podemos visualizar seu sumário
summary(modelo)
print(modelo)
# Vamos fazer uma inspeção gráfica na base de dados -> analisando a situação (eleito ou não) com as despesas (investimento em campanha) -> formatando um pouco o gráfico anterior dando melhor visualização
plot(eleicao$DESPESAS, eleicao$SITUACAO, col = 'red', pch = 20)
# Agora neste mesmo gráfico vamos gerar alguns pontos que são ajustes feito pelo modelo (modelo$fitted)
points(eleicao$DESPESAS, modelo$fitted.values, col = 'yellow', pch = 4)
# Neste gráfico poderá observar o efeito da binomial utilizada para realizar a regressão logística
# Ajustado o modelo vamos fazer uso dele para prever a SITUAÇÃO dos novos candidatos -> vamos ler nossa segunda base de dados novoscandidatos.csv
prever_eleicao = read.csv('D:/Users/Angelo/AULAS/Dados/novoscandidatos.csv', sep = ';', header = T)
#fix(prever_eleicao) # -> é uma forma de exibir a tabela caso esteja numa ide sem muitos recursos
# Vamos agora gerar um sumário dos nossos dados
summary(prever_eleicao)
# Vamos agora fazer uma previsão (SITUAÇÃO -> ELEITO OU NÃO) a partir do quanto os candidatos desejam investir na campanha
# Vamos criar uma nova coluna RESULT e chamar a função predict >- acompanhe
prever_eleicao$RESULT = predict(modelo, newdata = prever_eleicao, type = 'response')
# fix(prever_eleicao) # Visualiza de forma tabular os dados
cat('\nOlhando para o que foi previsto \n', prever_eleicao$RESULT)
# Podemos observar que os dois últimos candidatos possuem uma grande chance de serem eleitos -> acima de 94%
