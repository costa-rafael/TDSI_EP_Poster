import pandas as pd


df = pd.read_csv('Dados\DadosLimpos.csv')

colunas_numericas = [
    'Age', 'Frequency(1_4)', 'Acessibility(1_4)', 'Information(1_4)',
    'Incentives(1_4)', 'Hygiene(1_4)', 'Make_Difference(1_10)'] #Identifica e agrupa as colunas que são numéricas

def verificacao_outliers(series): #Definição da função que verifica a existência de outliers
    data = series.dropna() #Remove os valores NaN (vazio) para conseguir realizar os cálculos
    if data.empty:
        return [] #Se não existirem dados suficientes para calcular os outliers

    Q1 = data.quantile(0.25) #Cálculo do Quartil 1
    Q3 = data.quantile(0.75) #Cálculo do Quartil 3
    AIQ = Q3 - Q1 #Cálculo da Amplitute Interquartil

    #Definição dos limites dos Outliers Moderados:
    limite_inferior = Q1 - 1.5 * AIQ #Limite inferior
    limite_superior = Q3 + 1.5 * AIQ #Limite Superior

    #Cálculo dos Outliers (fora dos limites)
    outliers = data[(data < limite_inferior) | (data > limite_superior)] #O operador | é um "ou" lógico
    return sorted(outliers.unique().tolist()) #(Unique) obtém valores únicos - sem duplicados, (tolist) transforma esses valores numa lista, (sorted) ordena esses valores por ordem crescente

resultado_outliers = {} #Cria-se um dicionário vazio que servirá para guardar cada coluna numérica juntamente com os seus outliers
for col in colunas_numericas: #Itera sobre todas as colunas numéricas
    outliers = verificacao_outliers(df[col]) #Verifica em todas as colunas numéricas a existência de outliers
    resultado_outliers[col] = outliers #Adiciona ao dicionário os outliers da respetiva coluna

print(resultado_outliers) #Imprime o resultado obtido, para a realização da tabela de outliers