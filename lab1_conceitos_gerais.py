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
