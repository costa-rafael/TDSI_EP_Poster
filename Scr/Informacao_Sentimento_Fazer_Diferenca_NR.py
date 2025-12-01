import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

CORES = ["#4CAF50", "#2196F3"]


df = pd.read_csv("Dados/DadosLimpos.csv")

df = df[df["Outside_Recycling"] == "Não"].dropna(subset = ["Information(1_4)", "Make_Difference(1_10)"]) #Filtro: do gráfico correlação, aparece apenas a linha informação para os não recicladores (segunda coluna a contar da esq)

x = df["Information(1_4)"]
y = df["Make_Difference(1_10)"]

a, b, r_value, _, _ = linregress(x, y) #a = declive (inclinação); b = ordenada na origem; r_value = coeficiente de correlação pearson

#REGRESSÃO LINEAR - Informação vs. Sentimento de Fazer a Diferença (Não Recicla)
plt.figure(figsize = (8,5)) #Define o tamanho da imagem
sns.scatterplot(x = x, y = y, color = CORES[1], s = 60) #Desenha os pontos do gráfico de dispersão (tamanho dos pontos = 60)
plt.plot(x, a*x + b, "-", color = CORES[0], label = f"y={a:.2f}x+{b:.2f},  r = {r_value:.2f}") #Desenha a linha de refressão linear; usa os valores de x e prevê os valores de y (pela equação da reta); a:.2f -> Arredondamento com duas casas decimais
plt.title("Informação vs. Sentimento de Fazer a Diferença (Não Recicla)")
plt.xlabel("Informação (1–4)")
plt.ylabel("Sentimento de Fazer a Diferença (1–10)")
plt.legend()
plt.tight_layout()
plt.savefig("Graficos\Informacao_Sentimento_Fazer_Diferenca_NR.png")
plt.close()