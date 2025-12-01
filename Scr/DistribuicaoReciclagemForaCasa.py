#Importação das Bibliotecas Necessárias
import pandas as pd
import matplotlib.pyplot as plt

#Definição da paleta de cores (Verde, Azul)
CORES = ["#4CAF50", "#2196F3"]

df = pd.read_csv('Dados\DadosLimpos.csv')

#GRÁFICO CIRCULAR - Distribuição de Reciclagem Fora de Casa
plt.figure(figsize = (7, 7))
Contagem_participantes = df['Outside_Recycling'].value_counts() #Conta quantos sim e quantos não
plt.pie(
    Contagem_participantes, #Valores que determinam o tamanho de cada fatia
    labels = Contagem_participantes.index, #Coloca as etiquetas em cada fatia (sim e não) - variáveis usadas na coluna 'Outisde_Recycling'
    autopct = '%1.1f%%', #Escreve dentro de cada fatia a percentagem que ela representa, com uma casa decima
    startangle = 90, #Roda o gráfico para começar a desenhar a primeira fatia a partir do ângulo de 90 graus (normalmente o topo)
    colors = CORES,  #Define as cores a usar (Verde e Azul)
    wedgeprops = {'edgecolor': 'black'}) #Adiciona uma borda preta em volta de cada fatia para melhor definição visual

plt.title('Distribuição de Reciclagem Fora de Casa', fontsize = 14)
plt.tight_layout()
plt.savefig('Graficos/Distribuicao_Reciclagem_Fora_Casa.png')
plt.close()