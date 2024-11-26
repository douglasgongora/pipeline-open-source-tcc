import pandas as pd
import os

# Caminho onde estão os arquivos CSV
pasta_arquivos = "/home/douglas/teste"

# Lista para armazenar os DataFrames
dfs = []

# Loop pelos arquivos CSV na pasta
for arquivo in os.listdir(pasta_arquivos):
    if arquivo.endswith(".csv"):
        caminho_arquivo = os.path.join(pasta_arquivos, arquivo)
        print(f"Lendo o arquivo: {caminho_arquivo}")
        try:
            # Tenta ler o arquivo, ignorando linhas problemáticas
            df = pd.read_csv(caminho_arquivo, on_bad_lines='skip')  # Para pandas >= 1.3
            dfs.append(df)
        except pd.errors.ParserError as e:
            print(f"Erro ao ler o arquivo {caminho_arquivo}: {e}")
        except Exception as e:
            print(f"Erro inesperado ao ler o arquivo {caminho_arquivo}: {e}")

# Verifica se conseguiu carregar algum DataFrame
if dfs:
    # Combina todos os DataFrames em um único DataFrame
    df_combinado = pd.concat(dfs, ignore_index=True)

    # Salva o DataFrame combinado em um único arquivo CSV
    output_file = os.path.join(pasta_arquivos, "arquivo_combinado.csv")
    df_combinado.to_csv(output_file, index=False)

    print(f"Arquivos combinados com sucesso! Arquivo salvo em: {output_file}")
else:
    print("Nenhum arquivo foi processado com sucesso.")
