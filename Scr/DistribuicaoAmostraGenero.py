import pandas as pd
import matplotlib.pyplot as plt

CORES = ["#4CAF50", "#2196F3",  "#FFD700"] #Define a paleta de cores (Verde, Azul e Amarelo)

df = pd.read_csv('Dados\DadosLimpos.csv')

contagem_genero = df['Gender'].value_counts() #Calcular as frequências

#GRÁFICO CIRCULAR - Distribuição da Amostra por Género
plt.figure(figsize = (7, 7))
plt.pie(
    contagem_genero,
    labels = contagem_genero.index, #Define as legendas de cada fatia do gráfico
    autopct ='%1.1f%%', #Mostrar a percentagem com 1 casa decimal
    startangle = 90, #Define o ângulo inicial onde a primeira fatia do gráfico circular vai começar a ser desenhada
    colors = CORES,  #Cores a usar: Verde, Azul e Amarelo
    wedgeprops = {'edgecolor': 'black'}
)

plt.title('Distribuição da Amostra por Género', fontsize = 14)
plt.savefig('Graficos/Distribuicao_Amostra_Genero.png')
plt.close()