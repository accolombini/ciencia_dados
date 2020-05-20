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
