import pandas as pd
import os
import re # Para limpeza robusta de strings

# --- 1. Definir Caminhos e Garantir Diretório de Saída ---
input_file_path = 'Dados/dados.xlsx'
output_dir = 'Dados'
output_file_path = os.path.join(output_dir, 'dados_limpos.csv')

# Garantir que o diretório de saída existe
if not os.path.exists(output_dir):
    print(f"O diretório '{output_dir}' não existe. A criar...")
    os.makedirs(output_dir)
    print(f"Diretório '{output_dir}' criado com sucesso.")

print(f"A tentar ler o arquivo: {input_file_path}")

# Inicializa df como None para garantir que está definida se houver um erro
df = None

# --- 2. Leitura do Arquivo de Dados ---
try:
    df = pd.read_excel(input_file_path)
    print("Arquivo lido com sucesso.")

except FileNotFoundError:
    print(f"ERRO: O arquivo não foi encontrado no caminho '{input_file_path}'. Por favor, verifique o nome e o caminho.")
    exit()
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo Excel: {e}")
    exit()

# SAÍDA DE SEGURANÇA: Se o DataFrame não foi lido, o script pára aqui
if df is None:
    print("ERRO: O DataFrame não foi carregado. A sair do script.")
    exit()

print("-" * 30)
print("Informação inicial do DataFrame:")
df.info()
print("-" * 30)

# A PARTIR DA LINHA 47 DO SEU SCRIPT

# 1. Função para limpar e simplificar nomes de colunas - MAIS ROBUSTA
def clean_col_name(col):
    col = col.strip()
    # Mapeamento para remover acentos e cedilha
    accents_map = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a',
        'é': 'e', 'ê': 'e',
        'í': 'i',
        'ó': 'o', 'õ': 'o', 'ô': 'o',
        'ú': 'u',
        'ç': 'c',
        # Maiúsculas
        'Á': 'A', 'À': 'A', 'Ã': 'A', 'Â': 'A',
        'É': 'E', 'Ê': 'E',
        'Í': 'I',
        'Ó': 'O', 'Õ': 'O', 'Ô': 'O',
        'Ú': 'U',
        'Ç': 'C',
        ' ' : '_', # Substituir espaços por sublinhados
        '?' : '', ':' : '', '(' : '', ')' : '', # Remover pontuação
        '/' : '_', '.' : '',
        '\xa0' : '_' # Remover caracteres especiais de espaço (o seu problema)
    }

    # Aplica o mapeamento e remove o que sobrar de caracteres não-alfanuméricos
    for char, replacement in accents_map.items():
        col = col.replace(char, replacement)
    
    # Remove qualquer caracter que não seja letra, número ou sublinhado
    col = re.sub(r'[^a-zA-Z0-9_]+', '', col)
    col = col.lower()
    col = re.sub(r'_{2,}', '_', col) # Remove sublinhados duplicados/múltiplos
    col = col.strip('_') # Remove sublinhados no início/fim
    return col

df.columns = [clean_col_name(col) for col in df.columns]

print("Nomes das colunas normalizados para: ", list(df.columns))

## b) Eliminar Colunas Inúteis
# Agora os nomes são mais limpos e sem acentos, facilitando o acesso
df.drop(columns=['nome', 'hora_da_ultima_modificacao', 'email', 'id'], inplace=True)
print("Colunas 'nome', 'hora_da_ultima_modificacao', 'email' e 'id' removidas.")


## c) Tratamento de Valores em Falta (Missing Values - NaN)
# Usar nomes de variáveis fixos e simplificados para o resto do script:
COL_FREQUENCIA = 'com_que_frequencia_costuma_reciclar_fora_do_ambiente_domestico'
COL_TIPOS_LOCAL = 'em_que_tipos_de_locais_costuma_reciclar_fora_do_ambiente_domestico'
COL_MOTIVOS_NAO = 'quais_os_principais_motivos_que_o_levam_a_nao_praticar_reciclagem_fora_do_ambiente_domestico'
COL_DISPOSTO_ALTERAR = 'estaria_dispostoa_a_alterar_os_seus_habitos_de_reciclagem_caso_existissem_incentivos_para_tal'
COL_ESCALA = 'numa_escala_de_0_a_10_ate_que_ponto_sente_que_as_suas_acoes_individuais_de_reciclagem_fazem_diferenca_no_ambiente'


# Preencher NaNs logicamente
df[COL_FREQUENCIA] = df[COL_FREQUENCIA].fillna('Não se aplica (Não recicla)')
df[COL_TIPOS_LOCAL] = df[COL_TIPOS_LOCAL].fillna('Não se aplica (Não recicla)')
df[COL_MOTIVOS_NAO] = df[COL_MOTIVOS_NAO].fillna('Não se aplica (Recicla)')
df[COL_DISPOSTO_ALTERAR] = df[COL_DISPOSTO_ALTERAR].fillna('Não se aplica (Recicla)')


# 3. Coluna de Escala (0 a 10): preencher com a média
media_escala = df[COL_ESCALA].mean()
df[COL_ESCALA] = df[COL_ESCALA].fillna(media_escala)
print(f"Valores em falta na coluna de escala (0-10) preenchidos com a média ({media_escala:.2f}).")

# --- 5. Guardar o DataFrame Limpo ---
try:
    df.to_csv(output_file_path, index=False, encoding='utf-8')
    print(f"Sucesso: O DataFrame limpo foi guardado em: {output_file_path}") # Esta é a linha
except Exception as e:
    print(f"ERRO: Ocorreu um erro ao guardar o arquivo CSV: {e}")