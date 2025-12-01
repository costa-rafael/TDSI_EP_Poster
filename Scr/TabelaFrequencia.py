import pandas as pd #Importa a biblioteca necessária

df = pd.read_csv('Dados/DadosLimpos.csv') #Lê o nosso ficheiro csv

#Lista de variáveis qualitativas
variaveis_qualitativas = [
    'Gender', 'Education', 'Outside_Recycling', 'Locals',
    'Reasons_Why_Not', 'Willingness_Change'
]

#Função para criar tabela de frequência de variáveis qualitativas
def criar_tabelafreq_qualitativas(df, coluna):
    freq_abs = df[coluna].value_counts(dropna = True)  #Tem de ignorar os valores nulos (NaN)
    freq_rel = (df[coluna].value_counts(normalize = True, dropna = True) * 100).round(3) #Cálculo da freq rel (%)
    
    tabela = pd.DataFrame({
        'Categoria': freq_abs.index.astype(str),
        'Frequência Absoluta': freq_abs.values,
        'Frequência Relativa (%)': freq_rel.values
    })
    
    tabela.loc[''] = ['TOTAL', freq_abs.sum(), freq_rel.sum().round(0)] #Adiciona a linha do total no final da tabela
    return tabela

#Gerar tabelas de frequência variáveis QUALITATIVAS
for col in variaveis_qualitativas:
    tabela = criar_tabelafreq_qualitativas(df, col)
    tabela.to_csv(f"TabelasFreq\TabelaFreq_Qualitativa_{col}.csv", index = False)



#Listas de variáveis quantitativas
variaveis_quantitativas = [
    'Age', 'Frequency(1_4)', 'Acessibility(1_4)', 'Information(1_4)',
    'Incentives(1_4)', 'Hygiene(1_4)', 'Make_Difference(1_10)'
]

#Função para criar tabela de frequência de variáveis quantitativas
def criar_tabelafreq_quantitativas(df, coluna):
    freq_abs = df[coluna].value_counts(dropna = True).sort_index() #Ordena as categorias (para as freqs. acumuladas)
    freq_rel = (freq_abs / len(df[coluna].dropna()) * 100).round(3) #Remove os valores nulos (NaN)
    freq_abs_acumulada = freq_abs.cumsum()
    freq_rel_acumulada = freq_rel.cumsum().round(3)
    
    tabela = pd.DataFrame({
        'Categoria': freq_abs.index.astype(str),
        'Frequência Absoluta': freq_abs.values,
        'Frequência Relativa (%)': freq_rel.values,
        'Frequência Absoluta Acumulada': freq_abs_acumulada.values,
        'Frequência Relativa Acumulada (%)': freq_rel_acumulada.values
    })
    
    tabela.loc[''] = ['TOTAL', freq_abs.sum(), freq_rel.sum().round(0), '---------', '---------'] #'---' porque as freq. acumuladas não têm total
    return tabela
   

#Gerar tabelas de frequência VARIÁVEIS QUANTITATIVAS
for col in variaveis_quantitativas:
    tabela = criar_tabelafreq_quantitativas(df, col)
    tabela.to_csv(f"TabelasFreq\TabelaFreq_Quantitativa_{col}.csv", index = False)