import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

CORES = "#4CAF50" #Define a cor (Verde para Recicladores)

df = pd.read_csv('Dados\DadosLimpos.csv')

df_recicla = df[df['Outside_Recycling'] == 'Sim'].copy() #Filtra apenas os participantes que RECICLAM fora de casa

df_recicla['Impacto Percebido'] = df_recicla['Make_Difference(1_10)'].dropna().astype(int) #Converte a coluna do csv para uma nova do DataFrame, removendo valores nulos (NaN) e convertendo para inteiro

tabela_frequencia = df_recicla['Impacto Percebido'].value_counts().sort_index().reset_index() #Calcula a frequência (contagem) de cada pontuação (1 a 10); oderna (sort_index); constrói uma nova tabela com duas colunas:1ª contém os valores de impacto (1 a 10), 2ª contém a contagem de participantes que escolheram cada valor (permite que o gráfico saiba o que é o x e o y)
tabela_frequencia.columns = ['Pontuacao', 'Contagem'] #Define as duas colunas (x e y)

#Calcular a percentagem
total = tabela_frequencia['Contagem'].sum()
tabela_frequencia['Percentagem'] = (tabela_frequencia['Contagem'] / total * 100).round(1)

#GRÁFICO DE BARRAS - Distribuição do Sentimento de Fazer a Diferença pelos RECICLADORES
plt.figure(figsize = (9, 6)) #Definição do tamanho da imagem
barplot = sns.barplot(
    x = 'Pontuacao', #Definição da variável do eixo do x
    y = 'Percentagem', #Definição da variável do eixo do y (agora em percentagem)
    data = tabela_frequencia, #Indica qual é o conjunto de dados (DataFrame) deve ser usado para construir o gráfico
    color = CORES, #Cor verde para as barras (Recicladores)
    edgecolor = 'black'
)

#Adicionar rótulos de dados por cima das barras (apenas com percentagem)
for index, row in tabela_frequencia.iterrows(): #Percorre cada linha da tabela_frequencia, index - posição da linha, row - os valores dessa linha
    barplot.text(index, row['Percentagem'] + 0.05, #Adiciona um texto diretamente no gráfico (barplot.text); posição horizontal no gráfico (index); posição vertical um pouco acima da barra (row + 0.05)
                 f"{row['Percentagem']}%", #Define o texto que aparece, ou seja, percentagem (%) do nº de participantes
                 color ='black', ha ='center', fontsize = 11) #Cor do texto (color); alinhamento horizontal (ha - horizontal alignment)

plt.title('Distribuição do Sentimento de Fazer a Diferença (Apenas Recicladores)', fontsize = 14)
plt.xlabel('Sentimento de Fazer a Diferença (1 = Baixo, 10 = Alto)', fontsize = 12) #Define o rótulo do eixo X
plt.ylabel('Contagem de Participantes (%)', fontsize = 12) #Define o rótulo do eixo Y
plt.grid(axis = 'y', linestyle = '--', alpha = 0.7) #Adiciona uma grelha apenas no eixo Y, com linhas tracejadas e transparência de 70%
plt.tight_layout()
plt.savefig('Graficos\Distribuicao_Sentimento_Fazer_DiferencaR.png')
plt.close()