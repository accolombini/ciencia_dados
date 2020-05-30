# Title     : Teste de Qui quadrado
# Objective : Conhecer como a linguagem R pode contribuir para a análise de hipóteses com o teste do Qui quadrado
# Created by: accol
# Created on: 30/05/2020

# Para esse laboratório que avaliar se assistir ou não novelas entre homens e mulheres >>- se há uma relação entre as variáveis. Como hipótese nula ||> Admitimos que não há uma relação a menos do mero acaso!
# Criaremos uma matriz de duas linhas e duas colunas passando os dados referente a assistir ou não novelas (colunas) e sexo serão as linhas (masculino e feminino)

novela = matrix(c(19, 6, 43, 32), nrow = 2, byrow = T)
# fix(novela) # Nos permite inspecionar a matriz criada -> se sua IDE permitir poderá visualizar diretamente sem o uso do fix

# Vamos melhorar nossa Matriz atribuindo nomes às linhas e colunas -> observe
rownames(novela) = c('Masculino', 'Feminino')
colnames(novela) = c('Assiste', 'Nao_Assiste')
# fix(novela) # Nos permite inspecionar a matriz criada -> se sua IDE permitir poderá visualizar diretamente sem o uso do fix
# Podemos agora realizar nosso teste de Qui quadrado chamando a função chisq.teste()
qui_quadrado = chisq.test(novela)
cat('\nO teste de Qui quadrado para nosso problema nos fornece:\n')
print.table(qui_quadrado)

# Do resultado podemos observar que o valor de p-value = 0.15, portanto, maior que  α = 0.05 -> padrão para validar uma hipótese, logo NÃO DEVEMOS DESCARTAR A HIPÓTESE
