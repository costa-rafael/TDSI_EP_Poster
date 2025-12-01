import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

CORES = ["#4CAF50", "#2196F3"] #Definição da paleta de cores: verde (recicladores), azul (não recicladores)

df = pd.read_csv('Dados\DadosLimpos.csv')

#Definir as colunas
fatores = ['Acessibility(1_4)', 'Information(1_4)', 'Incentives(1_4)', 'Hygiene(1_4)'] #Lista das colunas que representam barreiras à reciclagem (escala 1–4)
impacto = 'Make_Difference(1_10)' #Lista da coluna do impacto
colunas = fatores + [impacto] #Junção das duas variáveis (conjuto de colunas) que interessam analisar - simplifica futuras funções do pandas

#Filtrar por grupos de reciclagem
df_sim = df[df['Outside_Recycling'] == 'Sim'].dropna(subset = colunas) #Recicladores
df_nao = df[df['Outside_Recycling'] == 'Não'].dropna(subset = colunas) #Não Recicladores

novos_nomes = { #Define os novos nomes das colunas (passa de inglês para português) para poderem aparecer assim no gráfico
    'Acessibility(1_4)': 'Acessibilidade',
    'Information(1_4)': 'Informação',
    'Incentives(1_4)': 'Incentivos',
    'Hygiene(1_4)': 'Higiene'
}

corr_sim = df_sim[colunas].corr()[impacto].drop(impacto).rename(index = novos_nomes) #Correlação para Recicladores (sim)
corr_nao = df_nao[colunas].corr()[impacto].drop(impacto).rename(index = novos_nomes) #Correlação para Não-Recicladores (não)

#DataFrame para gráfico
plot_df = pd.DataFrame({
    'Fator': corr_sim.index,
    'Recicla': corr_sim.values,
    'Não Recicla': corr_nao.values}).melt(id_vars = 'Fator', var_name = 'Grupo', value_name = 'Correlação')

# Ordem pelo grupo "Sim"
ordem = corr_sim.sort_values(ascending = False).index

#GRÁFICO DE BARRAS - Correlação entre Fatores Implicativos da Reciclagem e Sentimento de Fazer a Diferença
plt.figure(figsize = (10, 6)) #Definição do tamanho da imagem
barplot = sns.barplot(
    x = 'Fator',
    y = 'Correlação',
    hue = 'Grupo',
    data = plot_df,
    order = ordem,
    palette = CORES,
    edgecolor='black'
)
for barra in barplot.containers:
    barplot.bar_label(barra, fontsize = 11, color = 'black')

plt.title('Correlação entre Fatores Implicativos da Reciclagem e Sentimento de Fazer a Diferença', fontsize = 14)
plt.xlabel('Fator', fontsize = 12)
plt.ylabel('Coeficiente de Correlação (r)', fontsize = 12)
plt.ylim(-0.3, 1.0) # Ajustar o limite Y para incluir correlações negativas fracas e fortes positivas
plt.legend(title = 'Grupo de Reciclagem')
plt.grid(axis = 'y', linestyle = '--', alpha = 0.7) #Adicionar a grelha do gráfico
plt.axhline(0, color = 'red', linestyle = '--') #Adicionar a linha horizontal para referência (correlação zero)
plt.tight_layout()
plt.savefig('Graficos\Correlacao_Fatores_Sentimo_Diferença.png')
plt.close()