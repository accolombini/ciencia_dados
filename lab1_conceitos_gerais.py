# Estatistica --> Ciencia que usa de teorias em experimentos e observacoes para o estudo destes,divide-se em:
# 1- Descritiva => organizar, demonstrar e resumir dados
# 2- Probabilidade => analisar situações sujeitas ao acaso
# 3- Inferência => obter respostas sobre um fenômeno com dados representativos
# Observacao e experimento:
# 1- Observacao => estudo em que os elementos analisados nao sao afetados (pesquisa de intencao de votos, por exemplo) <> nao ha como controlar uma relacao de causa e efeito, por exemplo
# 2- Experimentos => condicoes ou tratamentos sao impostas a grupos, para avaliar o resultado (nete caso o pesquisador interfere no processo, por exmplo definindo algumas condicoes) <> neste caso e possivel controlar uma relacao entre causa e feito
# Quando o assunto e Estatitistica podemos definir Variaveis estabelecendo a seguinte divisao:
# 1- Quantitativa => numericas, podendo ser: continuas >>= valores reais, podem assumir qualquer intervalo e => discretas >>= numeros fixos, inteiro num intervalo
# 2- Qualitativas => tambem chamadas de categoricas, podendo ser: nominais >>= categorias sem hieraquia => ordinais >>= categorias com hierarquia
# Importante <=> estatistica dependera muito da interpretacao dos resultados (o analista tem papel muito importante na analise dos dados); => escolhas >>= cabe tambem ao analista com base nos resultados realizar escolhas que tambem exercerao impacto no resultado final; avaliacao >>= por fim, a interpretacao dos resultados que sera um fator de suas escolhas como analistas devem ser interpretados, avaliados e criticados
# Amostra => parte de uma populacao, selecionada usano alguma tecnica que de chances iguais a todos os elementos da populacao de serem selecionados (atencao => e fundamental que a tecnica usada para coletar sua amostra garanta que todos os elementos da populacao tenham chances iguais)
# Populacao => e o alvo do estudo (por exemplo, todos os eleitores em condicoes de voto)
# Amostra => e um subconjunto da populacao
# Censo => quando a pesquisa e realizada com toda a populacao (melhor condicao, mas proibitiva dado ao tempo e custo)
# E possivel inferir sobre uma amostra => se uma amostra for feita corretamente ela devera representar as mesmas caracterisitcas da populacao de onde ela foi retirada
# Se ela nao representa a populacao, dizemos que ela e 'enviesada' => enviesada e o nome que se da quando voce superestima o parametro da populacao: algumas causas -> pesquisa de pessoas que sao proximas ou de mais facil acesso -> pesquisa pela internet => respondera quem se sentir mais apto para faze-lo compormentendo o resultado -> sem o uso de mecanismo de selecao aleatorio => e imperativo que a amostra seja oresultado de uma selecao onde todos os membros da populacao tenham a mesma chance de serem selecionados
# "Custo" da Amostra => uma amostra possui uma margem de erro e um nivel de confianca -> variacao => amostras diferentes extraidas da mesma populacao em dias diferentes podem apresentar resultados diferentes -> podemos => medir a variacao esperada
# Quando se fala em amostras e preciso fazer uma analise custo/beneficio -> e preciso tambem separar a pupulacao para teste/treino/validacao => ainda para este evento (separacao) e preciso o uso de tecnicas que confiram a mesma oportunidade a todos os participantes de serem selcionados => experimentos diferentes -> neste caso tambem ha que se tomar cuidados e estabelecer criterios para o processo de separacao das amostras
# Os principais tipos de amostras sao: aleatoria simples (com ou sem reposicao); estratificada e sistematica
# Amostras aleatorias simples >>= um determinado numero de elementos e retirado da populacao de forma aleatoria; => todos os elementos da populacao alvo do processo de amostragem, devem ter as mesmas chances de serem selecionadas para fazer parte da amostra.
# Na amostra estratificada => as populacoes estao divididas nos chamados estratos (caracterisitcas comuns dos individuos, por exemplo, raca, religiao, tipo sanguineo, regiao, etc)
# Na amostragem sistematica e escolhido um elemento aleatorio, e a partir dai, a cada N elementos um novo membor e escolhido (por exemplo: 0 escolha +100 escolha +100 escolha +100 escolha ...). Neste caso suponha que o elemento aleatorio escolhido seja o numero 80 (faz o papel do numero 0 no exemplo acima)
# </> Funçoes no R que podem nos apoiar no tratamento de amostras:
# 1- sample() => usada para gerar uma amostra simples com ou sem reposicao
# 2- strata() => usada para gerar uma amostra estratificada
# 3- S.SY() => usada para gerar uma amostra sistemática
# Vamos agora estudar outros conecitos importantes para a estatistica <$> MEDIDAS DE CENTRALIDADE => sua funcao nos fornecer insumos para visualizarmos a centralidade dos dados <$>
# Medidas de Centralidade => Media; Moda e Mediana
# Na notacao para medidas de Centralidade usamos simbolos diferentes para representar Centralidade da Amostra e Centralidade da Populacao >>= μ -> Para media da Populacao e X (barrado) -> media da Amostra
# A Moda e o conjunto de dados mais frequente >>= a moda e sempre o mais frequente que pode ou nao existir
# A Mediana e remente ao valor central >>= e necessario antes ordenar os valores em ordem crescente. Note que, se o numero de elementos for par teremos que tirar a media dos valores intermediarios para encontrar a Mediana
# <$> Mediana vesus Media <$>
# Imagine o seguinte conjunto de dados: [10, 20, 30, 40, 10000]. A media e: 2020 e a Mediana: 30 <=> note que, embora ambas as medidas sejam de centralidade ha uma discrepacia enorme neste caso entre media e mediana. O interessante e que quando se tem um grande volume de dados o calculo da media e mediana nos fornecerao uma boa nocao da centralidade de sua amostra/populacao
# <$> Medidas de Variabilidade => sua funcao nos mostrar a distancia entre os dados quanto mais distantes os dados, maior sera sua variabilidade <$>
# Variancia => nos mostra a regularidade de um conjunto de dados em relacao a media, sendo representa por σ² (para o Calculo da Variancia da Populacao) e S² (para o Calculo da Variancia da Amostra)
# Desvio Padrao => o desvio padrao nos diz a que distancia os dados estao da media sendo calculado pela raiz quadrada da Variancia ~~> quanto maior o desvio padrao, mais afastados os dados estao da media
# Amplitude => pouco utilizado representa apenas a diferenca entre o maior e o menor elemento de um conjunto de dados (max - min)
# Nao centrais => Quartis >=> nos ajudam a entender como os dados estao distribuidos >- sendo Q1: 25% dos menores valores do conjunto de dados; Q2: 50% do conjunto de dados (corresponde a mediana); Q3: 75% dos maiores valores do conjunto de dados
# Amostra <> Populacao possuem notacao especifica em estatistica para media e desvio padrao: Media da Amostra X >- Media da Populacao μ; Desvio Padrao da Amostra S >- Desvio Padrao da Populacao σ
# Medidas de Centralidade em R >>= Funcoes no R:
# quantile() => para o calculo dos quartis
# sd() => para o calculo do desvio padrao
# var() => para o calculo da variancia
# mean() => para o calculo da media
# median() => para o calculo da mediana
# summary() => visualizacao rapida da base de dados
# <$> PROBABILIDADE <$>
# Probabilidade (P) >=> 0 <= p <= 1
# P = 1 >=> chamado de evento certo
# P = 0 >=> chamado de evento impossivel
# Probabilidade de 50% >=> 0,5 ou 1/2
# Impossivel >=> -0,5 - 20% 2/1 >- enfim valores que fogem do intervalo 0 <= p <= 1
# Conceitos chaves de Probabilidade
# Experimento >=> o que está sendo estudado
# Espaco Amostral >=> sao todas as possibilidades de ocorrencia de um evento
# Evento >=> resultados ocorridos
# Exemplo >- Experimento -> jogar moeda; Espaco Amostral >- cara ou coroa; Evento >- coroa (resultado de lancar uma moeda)
# Eventos Excludentes >=> sao eventos que nao podem ocorrer ao mesmo tempo. Exemplo >- jogar um dado e obter como resultado o numero 1 e par
# Eventos Nao Excludentes >=> sao eventos que podem ocorrer ao mesmo tempo. Exemplo >- jogar um dado e obter como resultado o numero 2 e par
# Eventos Dependentes >=> a ocorrencia de um evento afeta o outro. Um tem que ocorrer para depois ocorrer o outro
# Eventos Independentes >=> a ocorrencia de um evento nao afeta o outro
# <$> Um unico evento <$>
# P = (Ocorrencia Espeada)/ (Numero de Eventos Possiveis)
# Exemplo >- Jogar uma moeda e dar cara: Experimento -> jogar uma moeda; Evento -> dar cara; Espaco Amostral [Cara, Coroa] <=> P = (1)/(2) = 50%
# <$> EVENTOS EXCLUDENTES <$>
# Soma-se as probabilidades: Jogar um dado e ser um ou par. Experimento >- jogar um dado; Evento >- ser um ou par. A probabilidade sera calculada por: P = (1/6 + 3/6) = 4/6 ou 66%
# <$> EVENTOS NAO EXCLUDENTES <$>
# Soma-se as probabilidaes, diminui-se as sobreposicoes: Jogar um dado e ser 2 ou par. Experimento >- jogar um dado; Evento >- ser 2 ou par. A probabilidade sera calculada por: P = 1/6 + 3/6 - 1/6 = 1/2 ou 50%
# <$> EVENTOS INDEPENDENTES >>- produto <$>
# Temos sempre mais de um evento, entao, como eles se relacionam?
# A relacao entre os eventos sera de multiplicacao. Exemplo: quala probabilidade de jogar dois dados, e dar 1 e 6: Experimento >- jogar dois dados; Evento >- sair um e seis >>= note que os eventos sao independentes, os resultados de um dado nao afetam o outro dado: P = 1/6 * 1/6 = 0.027
# <$> EVENTOS DEPENDENTES (nao ha reposicao) >>- produto so que e necessario apos realizar o primeiro experimento retira-lo do espaco amostral <$> 
# Com 6 cartas na mao (A, 2, 3, 4, 5, 6), qual a probabilidade de tirar A no primeiro evento e no segundo tirar 4? P = 1/6 * 1/5 = 0.033 
# <$> PROBABILIDADE A LONGO PRAZO >>- NO LONGO PRAZO a probabilidade tende a convergir para a media esperada <$>
# Jogando um dado justo 6 vezes, qual a media esperada? PM = (1 + 2 + 3 + 4 + 5 + 6) / 6 = 3,5 >>- 3,5 e a media esperada, para se chegar a esse valor voce podera ter que realizar o experimento um numero significativamente grande de vezes -> dai o conceito de longo prazo
# </> TRABALHANDO COM DISTRIBUICOES </>
# Distribuicoes sao usadas principalmente na teoria da probabilidade mostrando o comportamento de dados aleatorios
# <$> DISTRIBUICAO BINOMIAL <$>
# O que é >=> trata-se de uma distribuicao de probabilidade discreta onde certos pre-requisitos precisam ser atendidos:
# Pre-requisitos >>- Numero fixo de experimentos; Cada experimento pode ter 2 resultados apenas >- sucesso ou fracasso; A probabiidade de suceso deve ser a mesma em cada experimento; Os experimentos sao independentes
# Exemplo: Se eu jogar uma moeda 5 vezes. Qual a probabilidade de dar cara 3 vezes?
# O que temos: Numero fixo de experimentos? Sim (5); Cada experimento pode ter 2 resultados apenas: sucesso ou fracasso? Sim cara ou coroa; A probabilidade de sucesso deve ser a mesma em cada experimento? Sim 50% para cada; Os experimentos sao independentes? Sim >>= Note que todas os pre-requisitos de uma distribuicao normal foram atendidos
# Exemplo: Um cesto tem 10 frutas que pesam entre 3 e 5 quilos. Qual a probabilidade de eu retirar duas frutas, uma de 4 quilos e outra de 3 quilos?
# O que temos: Numero fixo de experimentos? Sim (2); Cada experimento pode ter 2 resultados apenas: sucesso ou fracasso? Nao; A probabilidade de sucesso deve ser a mesma em cada experimento? Nao da para saber; Os experimentos sao independentes? Sim supondo que as frutas sao devolvidas a cada experimento ou nao se nao houver reposicao >>= logo nao se trata de uma distribuicao Binomial
# </> ALGUMAS CONVENSOES QUE SERAO UTILIZADAS </>
# X = total de sucesso esperado do experimento
# p = probabilidade de sucesso
# n = numero de experimentos
# 1 - p = probabilidade de fracasso 
# Voce podera calcular a distribuicao Binomial utilizando ferramentas computacionais ou usando tabelas de distribuicao Binomial
# <$> DISTRIBUICAO NORMAL <$>
# Sem duvida e a distribuicao mais importante da estatistica, nela a media dos dados se encontra ao centro. Importante 68% dos dados estao a um desvio padrao da media, cerca de 27% dos dados vao estar ate dois desvios padrao em relacao a media, 4,2% dos dados estarao a tres desvios padrao da media e mais do que tres desvios padrao voce encontrara apenas 0.2% dos dados
# TEOREMA CENTRAL DO LIMITE </> 
# Conforme o tamanho da amostra aumenta, a distribuicao das medias amostrais se aproxima cada vez mais da distribuicao NORMAL => mesmo que os dados nao estejam normalmente distribuidos
# Independente de como os dados estao distribuidos, suas medias estararao normalmente distribuidas (desde que o tamanho da amostra/populacao sejam grande o suficiente).
# O uso do teorema Central do Limite permite o uso da distribuicao Normal, por exemplo, quando a distribuicao dos dados e continua e nao e normal.
# <$> DISTRIBUICAO NORMAL PADRAO (Z) <$> >=> como e dificil calcular a probabilidade utilizando uma distribuicao Normal, usamos a distribuicao normal padrao para se calcular a probabilidade
# Mostra o numero de desvios padroes que o valor esta acima ou abaixo da media (escore Z ou valor Z)
# Media Zero
# Desvio padrao 1
# Usa-se uma formula para calcular a probabilidade de seus dados com relacao a tabela Z >=> Z = (X - μ) / σ
# Nota >>= lembre-se a maioria das distribuicoes normais nao terao media zero e desvio padrao 1 =>> isso ocorre somente para a distribuicao normal padrao e tambem, lembre-se sempre que o calculo da probabilidade e cumulativo da esquerda para a direita
# Como saber se uma distribuicao e Normal? |||> a forma mais simples de saber se os dados seguem uma distribuicao normal e gerando um HISTOGRAMA -> e avaliar se ele tem o formato de sino, se ha uma simetria e se os dados estao em torno da media
# <$> OUTRAS DISTRIBUICOES <$>
# Podemos encontrar uma distribuicao com cauda curta ||> a media e central, mas existe uma maior concentracao dos dados no entorno a media >>= outra possibilidade encontrar uma distribuicao com cauda longa ||> a media tambem e central mas os dados estao distribuidos em uma maior amplitude |||> essas distribuicoes nao sao Normal no sentido da definicao. ||| Alem dessas podemos encontrar distribuicoes com enviezamento a direita e tambem com enviezamento a esquerda
# Outra forma para se verificar se os dados estao distribuidos de forma normal e gerando um diagrama de PROBABILIDADE NORMAL ||> se ao fazer isso, envontrar os dados proximos a linha (claro pode haver uma pequena variacao nos extremos) podemos concluir que os dados estao NORMALMENTE DISTRIBUIDOS; caso contrario se houver uma grande variacao em relacao a linha normal ||> conclui-se que os dados NAO ESTAO NORMALMENTE DISTRIBUIDOS
# Uma forma um pouco mais complexa para testar os dados é usando o TESTE DE SHAPIRO-WILK
# Teste de Hipotese |||> sempre existe a hipotes nula e a hipotese Ha
# H0 = dados estao normalmente distribuidos -> hipotese Nula >- aquilo que voce define como criterio a ser avaliado
# Alfa = 0,05 >- voce escolhe o Alfa (normalnte opta-se por 0,05)
# Valor de p <= 0,05 => rejeita hipotese nula >- deve ser comparado com se valor de Alfa
# Valor de p > 0,5 => nao e possivel rejeitar a hipotese nula >- deve ser comparado com se valor de Alfa
# p-value = 0,001722 [p <= 0,05] -> nao normal ||> ha indicios de que a distribuica nao e NORMAL
# p-value = 0,05696  [p  > 0,05] -> normal ||> ha indicios de que a distribuica e NORMAL
# </> Mas QUAL O RIGOR a ser aplicado? </>
# Nem sempre os dados precisam ser rigorosamente normail. Dados aproximadamente normais sao suficientes para a maioria dos casos sob estudo. Cabe aqui uma avaliacao critica de seus dados e de seu projeto

# <$> ESTATISTICA PARAMÉTRICA -> corresponde a Estatística que Estamos estudando <$>
# Estatística Paramétrica => requer que os dados estejam em conformidade com alguma distribuição, por exemplo, Distribuiçao Normal
# <$> ESTATISTICA NÃO PARAMÉTRICA -> não será tratada neste momento, ficará fora do escopo inicial proposto pelo curso <$> 
# Quando os dados não estão em conformidade com alguma distribuição, em outras palavras, quando não se conhece a distribuição dos dados

# </> INTERVALOS DE CONFIANÇA </>
# É possível inferir características de uma população a partir de uma amostra -> porque? Custo; Viabilidade; Etc.
# Preço => erro padrão / nível de confiança
# Riscos => dados ruins, enviesamento
# Porém ... =>> Como estamos utilizando amostras ... devemos esperar variações no resultado; A primeira amostra pode variar com relação à segunda e assim por diante ...; Mas, o grande detalhe é que podemos "medir" o quanto pode ser esta variação e avaliar se atende ou não as expectativas do projeto em questão
# Intervalos de Confiança =>> deverá parametrizar mais ou menos a margem de erro estimada.
# Parâmetro é o valor a ser estimado >- um exemplo de parâmetro aqui é a média, outro parâmetro pode ser a proporção e assim por diante
# A margem de erro =>> é a variabilidade, para mais ou para menos. A margem de erro é afetada pelo tamanho da amostra, pelo nível de confiança, daí a importância de estar atento aos melhores ajustes para seu objetivo/projeto
# Nível de confiança =>> de 80% a 99% >- você deverá escolher o nível de confiança, lembrando que sua escolha trará consequências para seu experimento >- Para acompanhar >=> quanto maior o nível de confinça exigido, maior será a probabilidade da amostra estar fora de seu intervalo de confiança >- para cada nível de confiança teremos um valor de Z que será utilizado nos cálculos (este valor de Z irá crescer na medida em que se aumenta o nível de confiança)
# Tamanho da Amostra (n) 
# Vamos exemplificar numericamente ...
# Entre 63 e 67% dos entrevistados pretendem votar em Maria, com um nível de confiança de 95%.
# Parâmetro (valor a ser estimado) => intenção de voto (proporção)
# Nível de confiança escolhido => 95%
# Intervalo de confiança (vem lá da margem de erro) => entre 63 e 67%
# Erro padrão => 1,96
# Entrevistados (tamanho da amostra) => 1000
# Margem de erro (+/-)2%
# Compensação >- para ajudá-lo na análise dos resultados frente suas escolhas.
# Quanto mais alto for o nível de confiança => maior será o erro padrão
# Quanto maior for o tamanho da amostra => menor será o erro padrão
# Tipos de Intervalos de Confiança:
# Intervalo de Confiança para a média
# Intervalo de Confiança para a proporção
# <$> TESTE DE HIPÓTESE <$>
# Confirmar ou negar uma premissa usando uma amostra
# Esta premissa usa um parâmetro, por exemplo, 56% dos brasileiros não gostam de estatística >>- para testar essa premissa deveremos recorrer a um teste de Hipótese
# Encontrar diferença não é tudo, é preciso saber se esta diferença é estatisticamente significante => isso é muito relevante e fortemente dependente da natureza do seu projeto
# </> ALGUMAS CONVENSÕES MUNDIALMENTE ADOTADAS PARA O TESTE DE HIPÓTESE </>
# Hø => hipótese nula => trata-se da alegação daquilo que deseja testar
# Presume-se inicialmente que Hø é verdadeira, a não ser que existam evidências para provar que não
# Exemplo => Hø: μ = 100
# Ha => hipótese alternativa
# Exemplo: Ha != 100, Ha > 100, Ha < 100
# Score padrão => erros que seus dados estão abaixo ou acima da média
# A versão padronizada de sua estatística é chamada de "estatistica de teste"
# Verificar na versão padronizada de Z. Se a sua estatística de teste estiver próxima de zero ou num intervalo onde os resultados devem estar, então não se pode rejeitar Hø. Agora se estiver próximo a cauda, então podemos rejeitar Hø
# Alfa (α) => é um valor que você deverá escolher para aplicar no seu teste de hipótese
# Níveis de Alfa (α): 0,05 ou 0,01 => normalmente sugerido >>= Enterpretar o valor-p >- Valor -P >= alfa: você não deverá rejeitar Hø; Se valor -P <= alfa: você deve rejeitar a Hø; Agora e se o valor -P estiver muito próximo de Alfa => o que fazer??? Neste caso, há autores que consideram o resultado inconclusivo, mas também cabe a sua interpretação sempre com o olhar para seu projeto
# </> ETAPAS </>
# 1- Definir o tamanho da sua amostra
# 2- Coletar os dados
# 3- Calular as medidas de centralidade => principalmente média e desvio padrão
# 4- Definir as duas hipóteses: Hø e Ha (hipótese nula e hipótese alternativa)
# 5- Definir seu valor de Alfa(α)
# 6- Padronizar seus dados gerando a estatístca de teste
# 7- Encontrar o valor -p na tabela Z
# 8- Comparar com seu valor de Alfa(α)
# 9- Emitir seu veredito => isso será muito importante!!!
# As fórmulas para Estatística de Teste são:
# Média => Z = (X - μ) / σ/sqrt(n)
# Proporção => P = (p^ - pø) / sqrt((pø * (1 - pø)) / n)
# </> ERROS </>
# Em testes de hipóteses estamos ujeitos a dois tipos de erros, são eles:
# Erro do tipo 1 => rejetiar Hø quando não deveria fazê-lo >- por exemplo, chance de ocorrer igual a Alfa(α)
# Erro do tipo 2 => não rejeitar Hø quando deveria fazê-lo >- depende do tamanho da amostra, que pode não ser adequada
# IMPORTANTE: se você reduzier o valor de Alfa(α) você reduz a chance de ERRO DO TIPO 1 >- mas também torna mais difícil rejetiar Hø >- você irá precisar de mais dados para poder rejeitar Hø e aumenta a chance de ERRO DO TIPO 2; Aumentando o tamanho de Alfa(α) aumenta a chance de ERRO DO TIPO 1 >- mas fica mais fácil rejeitar Hø e diminui a chance de ERRO DO TIPO 2
# PORTANTO: o ideal é que você tenha uma amostra grande e um Alfa(α) pequeno
# <$> DISTRIUIÇÃO T DE STUDENT => é uma distribuição extremamente importante em Estatística <$>
# Pode se dizer que se trata de um parente próximo da distribuição Normal sendo utilizada sob certas condições:
# Utilizada quando o tamanho da amostra é reduzido inferior a 30
# E não se conhece o desvio padrão da POPULAÇÃO >>= É claro que o desvio da AMOSTRA pode ser calculado
# Custo => Maior variabilidade (por exemplo, num teste de hipótese) <=> numa maior imprecisão 
# Tendência => maior de encontrar valores nas caudas (caudas maiores)
# Se n >= 30, se assemelha a uma distribuição NORMAL
# O grau de liberdade corresponde ao tamanho da amostra menos um (n - 1), exemplo, se n = 15, o grau de liberdade será 14 (tø = 14)
# Pode se usar T de Student para:
# Calcular probabilidade
# Calcular Intervalos de Confiança -> calcula-se o valor de t1 (tø -> você já tem a partir da amostra menos um) => t = (X - μø) / (S / sqrt(n))
# Executar testes de Hipótese
# Para se usar T de Student:
# Calcula-se o valor de t (grau de liberdade) >- pode ser necessário alguma interpolação no caso do uso da tabela
# Consulta-se a tabela de distribuição t ou usa-se uma ferramenta computacional como R ou Python para calcular a probabilidade
# <$> CORRELAÇÃO E REGRESSÃO LINEAR <$>
# Variáveis => existe uma correlação matemática entre as variáveis envolvidas? Se existe, como posso medir a força dessa relação? É possível usar essa relação para fazer previsões?
# Para entender o comportamento das variáveis envolvidas no processo, recomenda-se o gráfico de dispersão para uma primeira inspeção visual
# Sistematizando um pouco >>= no eixo Y do plano cartesiano, normalmente representamos a variável de Resposta ou a variável Dependente (na regressão Linear ||> trata-se do que queremos prever)||> No eixo X do plano cartesiano, normalmente representamos a variável Explanatória ou Independente ||> (na regressão é o que explica ou usamos para prever)
# Como podemos observar a regressão Linear pressupõe uma linearidade entre as variáveis observadas, essa linearidade pode ser maior ou menor

# </> CORRELAÇÃO e COEFICINETE DE DETERMINAÇÃO [R²]
# CORRELAÇÃO [R] |||> Mostra a força e a direção da relação entre as variáveis |||> quanto mais próximo de ZERO menor a força da correlação
# CORRELAÇÃO [R] |||> pode ser um fator entre -1 e 1
# CORRELAÇÃO [R] |||> de A ~ B é a mesma de B ~ A 
# Importante ||> é preciso estar atento à direção da correlação!!! Não perca de vista!!! A correlação pode ser direta => mas, também podemos ter uma correlação inversa |||> Correlação positva => significa que as variáveis estão na mesma direção |||> correlação negativa => significa que as variáveis estão em direções opostas
# Entendendo a força da CORRELAÇÃO =>> pense em intervalos, por exemplo entre 0.7 e 1 -> CORRELAÇÃO forte, e assim por diante, ok:
# = 1 -> CORRELAÇÃO Perfeita
# = 0.7 -> CORRELAÇÃO Forte
# = 0.5 -> CORRELAÇÃO Moderada
# = 0.25 -> CORRELAÇÃO Fraca
# = 0 -> Não EXISTE CORRELAÇÃO
# = -0.25 -> CORRELAÇÃO Fraca
# = -0.5 -> CORRELAÇÃO Moderada
# = -0.7 -> CORRELAÇÃO Forte
# = -1 -> CORRELAÇÃO Perfeita
# </> COEFICIENTE DE DETERMINAÇÃO R² </>
# Nos mostra o quanto o modelo consegue explicar os valores
# Quanto maior R², mais explicativo é seu modelo
# O Restante da variabilidade está em variáveis que por algum motivo não foram incluídas no modelo
# VAria entre Zero até 1 (sempre positivo)
# É calculado a partir do quadrado do coeficiennte de correlaçao (R)
# Exemplificando => imagine um modelo onde o coeficiente de CORRELAÇÃO R = 0.93 o coeficiente de DETERMINAÇÃO r² = 0.93² = 0.86 |||> isso significa que 86% da variável dependente consigue ser explicada pelas variáveis exploratórias presentes no modelo
# <$> REGRESSÃO LINEAR => PREVISÃO <$> 
# Fundamental para se fazer previsões a partir dos dados históricos e da CORRELAÇÃO do seu modelo
# Para construir a reta de regressão => a intersecção nos mostra o ponto onde a reta corta o eixo Y e a inclinação nos da da o coeficiente de inclinação da reta (regressão linear SIMPLES)
# </> COMO PREVER? </>
# Previsão => intersecção (ponto onde corta o eixo Y) + (inclinação (inclinação da reta) * valor a prever)
# Qualquer software executa esse cálculo automaticamente, neste laboratório usaremo R e Python
# </> REGRESSÃO LINEAR -> Residuais </>
# Ocorre com frequência quando a linha de regressão não passa por praticamente nenhum ponto do modelo (há resíduos) -> RESIDUOS são calculados a partir da diferença entre os valores do modelo e a linha de melhor ajuste (linha de regressão -> REGRESSÃO SIMPLES) =>> podem ser calculados medindo a diferença entre o ponto do modelo e a linha de regressão >- Se o ponto estiver acima da linha de regressão seu RESÍDUO será POSITIVO, se estiver abaixo será NEGATIVO, se coincidir com a linha de regressão será NULO. O valor ajustado corresponde ao valor do ponto refletido na linha de melhor ajuste (REGRESSÃO)
# A diferença de todos os residuais do modelo podem ser usados para se calcular o  ERRO
# </> OUTLIERS, EXPLORAÇÃO, CORRELAÇÃO NÃO É CAUSA </>
# OUTLIERS => são valores que fogem do padrão >- podem reduzir drasticamente o coeficiente de CORRELAÇÃO =>> você deverá avaliar seu modelo e entender qual a melhor ação a tomar
# EXTRAPOLAÇÃO => quando estamos olhando para além dos limites de nossa regressão (inferior ou superior) =>> nestes casos não podemos afirmar que o nosso modelo se comportará exatamente como dentro da análise estudada >>= pode comprometar drasticamente a previsão. ATENÇÃO essa ação nao é proibida, mas fique atento aos resultados
# CORRELAÇÃO NÃO É CAUSA => por exemplo, pessoas com mais treinamento tem melhor performance >- OU SERÁ >- Elas receberam treinamento porque performaram melhor? ou ainda >- Candidatos vistos como carismáticos obtém mais votos >- ou será >- Candidatos mais votados são vistos como mais carismáticos?
# CUIDADO -> pode ser que a causa seja uma outra variável, talvez até que não tenha entrado nos estudos >- Tenha sempre muita cautela
# <$> CONDIÇÕES E REGRESSÃO LINEAR MÚLTIPLA <$>
# Uma importante condição é a FORÇA da correlação => não importa se é positiva ou negativa, o importante é a força da CORRELAÇÃO =>> Para bons resultados busque por CORRELAÇÕES MODERADA OU FORTE

# A outra importante condição é o COEFICIENTE DE DETERMINAÇÃO [R²], sendo os parâtros a seguir desejáveis:
# > 0.7 -> ÓTIMO
# Entre eles -> ? >- Cabe ao analista decidir se vai usar o modelo para fazer previsão
# 0 < R² < 0.3 -> Ruins
# Outro item importante são so RESIDUAIS PADRONIZADS
# Verifique se eles se encontram próximos de uma Distribuição NORMAL -> Nota estamos falando dos Residuos Padronizados, ok

# </> REGRESSÃO LINEAR SIMPLES E MÚLTIPLA </.
# SIMPLES => uma variável exploratória X (independente) para prever uma variável dependente Y (aquela que se deseja explicar) -> Y ~ X
# MÚLTIPLA => duas ou mais variáveis exploratórias X1, X2, ..., XN (independentes) para prever uma variável dependente Y (aquela que se deseja explicar) -> Y ~ X1 + X2 + XN
# ANALISAR CADA X COM Y
# Analisar cada variável independente com Y individulamente
# Gerar gráficos de dispersão individuais
# Buscar redundâncias [mesmos efeitos de X sobre Y]: veremos isso mais à frente -> basicamente se existem variáveis exploratórias que explicam a variável dependente da mesma forma, eles devem ser eliminadas, pois poderão prejudicar o modelo
# Outro ponto importante é o COEFICIENTE DE DETERMINAÇÃO [R²]
# Lembrando que R² é o percentual de variação da variável de resposta que é explicada pelo modelo
# Quando se colocam mais variáveis no modelo a tendência é que R² aumente, mesmo que a adição na variável não aumenta a precisão do modelo -> daí a necessidade de avaliar com cautela se uma variável deve ou não fazer parte do modelo
# Para isso, utiliza-se R² ajustado, que ajusta a variação do modelo de acordo com o número de variáveis independentes que é incluída no modelo
# R² ajustado vai ser sempre menor que R²
# Outro conceito importante é a COLINEARIDADE E PARCIMÔNIA
# COLINEARIDADE => duas variáveis independentes que são correlacionadas
# Incluir variáveis independentes colineares pode prejudicar o modelo, criando previsões não confiáveis
# PARCIMÔNIA => não colocar variáveis que não melhorem o modelo em nada >- criar MODELOS PARCIMONIOSOS
# Requisitos básicos
# 1- Linearidade entre a variável dependente e as variáveis independentes
# 2- Que as variáveis sejam normalmente distribuídas >- a variável dependente não necessita ser normalmente distribuída
# 3- Pouca ou nenhuma colinearidade 
# E quanto aos RESIDUAIS
# Próximos a distribuição NORMAL
# Variância constante em relação a linha de melhor ajuste
# independentes (sem padrão)
# Nota >- a variável dependente não necessita ser normalmente distribuída
# <$> REGRESSÃO LINEAR => FÓRMULAS <$>
# O processo de cálculo segue os seguintes passos:
# 1- Correlação
# 2- Inclinação
# 3- Interceptação
# 4- Previsão
# CORRELAÇÃO DE PEARSON => r = cov(X, Y) / SQRT(var(x) * var(y))
# INCLINAÇÃO => m = r (Sy / Sx)
# INTERCEPTAÇÃO -> ponto em que a reta intercepta o eixo Y => b = y - mx
# PREVISÃO => P = b + (m * v) -> onde v é o valor que você está buscando prever o resultado
# <$> REGRESSÃO LOGÍSTICA <$>
# Semelhante a regressão Linear, porém a variável de resposta é binária: sucesso ou fracasso
# 1- Sucesso
# 0- Fracasso
# O sucesso ou o fracasso é representado através de probabilidade (em outras palavras você terá a probabilidade de Sucesso ou a probabilidade de Fracasso)
# A Regressão Logística também pode ser Simples ou Múltipla

# <$> ANÁLISE EXPLORATÓRIA DE DADOS <$>
# EDA => Análise Exploratória de Dados -> (AED)
# John Wilder Tukey 1977 -> Exploratory Data Analysis (EDA - AED)
# Conceitos de EDA
# 1- Busca obter informações ocultas sobre os dados
# 1a- Variação
# 1b- Anomalias
# 1c- Distribuição
# 1d- Tendências
# 1e- Padrões
# 1f- Relações
# Importante => deve-se iniciar uma análise de dados pela EDA, só então decidir como buscar a solução para o problema iso garante uma maior assertividade na criação de seu MODELO >- EM OUTRAS PALAVRAS ->> ENTENDA ANTES SEUS DADOS
# </> EDA versus GRÁFICOS </>
# Não são a mesma coisa, porém EDA é altamente baseado na produção de gráficos
# Gráficos de dispersão, boxplots, histogramas, etc.
# <$> DISTRIBUIÇÃO DE POISSON <$>
# Mede a probabilidade da ocorrência de eventos em intervalo de tempo, em vez de um certo número de experimentos
# Importante => os eventos a cada intervalo devem ser independentes
# Existem tabelas de Poisson para apoiá-lo nos cálculos
# Como podemos olhar para uma Distribuição de Poisson:
# 1- P(X = x)
# 2- P(X < x) - P(X <= x)
# 3- P(X > x) - P(X >= x)
# A fómula para a Distribuição de Poisson é: P(X = x) = (e sqr(-λ)) * λ(sqr(x)) / x!
# Onde -> x é o número de eventos que estão sendo calculados
# λ -> número médio de eventos que ocorrem no período
# e = constante = 2.71828
# Como R pode nos apoiar na solução de problemas que envolvam a distribuição de Poisson
# Probabilidade exata, por exemplo "ocorrência de dois no segundo dia" -> dpois(x, λ)
# Probabilidade menos que, ou mais que (lower.tail = F) -> ppois(x, λ, lower.tail=F)
# Fique atento quando estiver trabalhando em eventos do tipo menor que ou maior que você deverá computar o valor a menos em depois -> isto é necessário porque aquele valor não está incluído no cálcuo da probabilidade
#