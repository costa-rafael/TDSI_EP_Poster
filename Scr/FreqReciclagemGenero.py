#Importação das Bibliotecas Necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Definição da paleta de cores (Verde, Azul)
CORES = ["#4CAF50", "#2196F3"]

df = pd.read_csv('Dados\DadosLimpos.csv') #Lê o nosso ficheiro csv

#GRÁFICO DE BARRAS - Frequência de Reciclagem por Género
df_bar = df.dropna(subset = ['Frequency(1_4)', 'Gender']).copy() #Remove linhas com valor NaN (dropna), (subset) verifica apenas na duas colunas definidas e não no dataframe todo
df_bar['Frequency'] = df_bar['Frequency(1_4)'].astype(int).astype(str) #Adiciona no novo dataframa (copia) uma coluna com os valores da coluna original

plt.figure(figsize = (10, 6)) #Cria a figura para o gráfico com 10 polegadas de largura e 6 de altura
barplot = sns.countplot( #Função que cria o gráfico de barras
    x ='Frequency', #Usa os valores do csv para o eixo horizontal (eixo x), o eixo do y é calculado automaticamente pelo gráfico(countplot)
    hue ='Gender', #Separa as barras por género
    data = df_bar, #Diz que os dados vêm do dataframe
    palette = CORES, #Define as cores a usar (Verde e Azul)
    order = sorted(df_bar['Frequency'].unique()) #Ordena os valores da Frequência (1-4)
)

#Adiciona rótulos automaticamente em todas as barras
for barra in barplot.containers: #Cada container corresponde a um conjunto de barras - devolve uma lista desses grupos de barras
    barplot.bar_label(barra, fontsize = 11, color = 'black') #Escreve automaticamente os valores por cima de cada barra (bar_label)

plt.title('Frequência de Reciclagem por Género', fontsize = 16) #Define o título do Gráfico
plt.xlabel('Frequência de Reciclagem (1 = Raramente, 4 = Diariamente)', fontsize = 12) #Define o título do Eixo do X
plt.ylabel('Contagem de Participantes', fontsize = 12) #Define o título do Eixo do Y
plt.legend(title = 'Género') #Define o título da Legenda
plt.grid(axis = 'y', linestyle = '--', alpha = 0.7) #Adiciona uma grelha apenas no eixo Y, com linhas tracejadas e transparência de 70%
plt.tight_layout() #Ajusta automaticamente o espaçamento entre os elementos do gráfico (visualmente organizado)
plt.savefig('Graficos\Frequencia_Reciclagem_por_Genero.png') #Guarda o gráfico na pasta Graficos
plt.close() #Fecha a figura atual do Matplotlib, libertando a memória associada a este gráfico


'''
O primeiro gráfico usa números absolutos (quantidade de participantes por género).
Aí vemos diretamente quantas mulheres e quantos homens reciclam, e percebe-se que há mais mulheres a reciclar.

O segundo gráfico usa percentagens dentro de cada género.
Como existem menos homens do que mulheres, quando se calcula a percentagem: 
        percentagem = (nº de homens que reciclam / total de homens) × 100

a divisão é feita por um número mais pequeno.
Isso faz com que as barras dos homens fiquem relativamente mais altas, mesmo que o número real de homens que reciclam 
seja menor.
'''


#Importação das Bibliotecas Necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Definição da paleta de cores (Verde, Azul)
CORES = ["#4CAF50", "#2196F3"]

df = pd.read_csv('Dados\DadosLimpos.csv') #Lê o nosso ficheiro csv

#GRÁFICO DE BARRAS - Frequência de Reciclagem por Género
df_bar = df.dropna(subset = ['Frequency(1_4)', 'Gender']).copy() #Remove linhas com valor NaN (dropna), (subset) verifica apenas na duas colunas definidas e não no dataframe todo
df_bar['Frequency'] = df_bar['Frequency(1_4)'].astype(int).astype(str) #Adiciona no novo dataframa (copia) uma coluna com os valores da coluna original

#Géneros e níveis da escala
generos = df_bar['Gender'].unique()
frequencias = sorted(df_bar['Frequency'].unique()) #Ordena os valores da Frequência (1-4)

# Lista onde iremos guardar os dados finais
dados = []

# Calcula percentagens manualmente (sem groupby)
for genero in generos:
    total_gen = len(df_bar[df_bar['Gender'] == genero])  #Total desse género
    
    for freq in frequencias:
        contagem = len(df_bar[(df_bar['Gender'] == genero) &
                              (df_bar['Frequency'] == freq)])
        
        percentagem = (contagem / total_gen) * 100 if total_gen > 0 else 0 #Cálculo da %
        
        dados.append([freq, genero, percentagem])

# Converte para dataframe simples
percent_df = pd.DataFrame(dados, columns = ['Frequency', 'Gender', 'Percent'])

plt.figure(figsize = (10, 6)) #Cria a figura para o gráfico com 10 polegadas de largura e 6 de altura
barplot = sns.barplot( #Função que cria o gráfico de barras
    data = percent_df, #Diz que os dados vêm do dataframe em percentagem
    x ='Frequency', #Usa os valores do csv para o eixo horizontal (eixo x), o eixo do y é calculado automaticamente pelo gráfico(countplot)
    y = 'Percent', #O eixo y passa a ser em %
    hue ='Gender', #Separa as barras por género
    palette = CORES, #Define as cores a usar (Verde e Azul)
    order = frequencias
)

#Adiciona rótulos automaticamente em todas as barras
for barras in barplot.containers: #Cada container corresponde a um conjunto de barras - devolve uma lista desses grupos de barras
    barplot.bar_label(barras, fmt = "%.1f%%", fontsize = 11, color = 'black') #Escreve automaticamente os valores por cima de cada barra (bar_label)

plt.title('Frequência de Reciclagem por Género', fontsize = 16) #Define o título do Gráfico
plt.xlabel('Frequência de Reciclagem (1 = Raramente, 4 = Diariamente)', fontsize = 12) #Define o título do Eixo do X
plt.ylabel('Contagem de Participantes (%)', fontsize = 12) #Define o título do Eixo do Y
plt.legend(title = 'Género') #Define o título da Legenda
plt.grid(axis = 'y', linestyle = '--', alpha = 0.7) #Adiciona uma grelha apenas no eixo Y, com linhas tracejadas e transparência de 70%
plt.tight_layout() #Ajusta automaticamente o espaçamento entre os elementos do gráfico (visualmente organizado)
plt.savefig('Graficos\Frequencia_Reciclagem_por_Genero(%).png') #Guarda o gráfico na pasta Graficos
plt.close() #Fecha a figura atual do Matplotlib, libertando a memória associada a este gráfico