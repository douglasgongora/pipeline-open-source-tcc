import logging
import pandas as pd
import os
from configs import configs
from functions import functions as F

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_csv_file(file_path):
    try:
        logging.info(f"Lendo arquivo CSV: {file_path}")
        df = pd.read_csv(file_path, encoding='utf-8-sig', sep=';', on_bad_lines='skip', engine='python')
        logging.info(f"Arquivo lido com sucesso: {file_path}")
        return df
    except Exception as e:
        logging.error(f"Erro ao ler CSV {file_path}: {str(e)}")
        return None

def add_metadata(df):
    try:
        return F.add_metadata(df)  # Certifique-se de que essa função está implementada corretamente
    except Exception as e:
        logging.error(f"Erro ao adicionar metadados ao DataFrame: {str(e)}")
        return None

def save_dataframe(df, file_path):
    try:
        df.to_csv(file_path, sep=',', index=False, encoding='utf-8-sig')
        logging.info(f"DataFrame salvo em: {file_path}")
    except Exception as e:
        logging.error(f"Erro ao salvar DataFrame em {file_path}: {str(e)}")

def main():
    logging.info("Iniciando a extração de todos os arquivos CSV na pasta...")

    folder_path = "/home/douglas/docker/tcc_project/arquivos_csv"

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv"):
            file_path = os.path.join(folder_path, file_name)
            logging.info(f"Processando arquivo: {file_name}")

            df_input_data = read_csv_file(file_path)
            if df_input_data is None:
                logging.error(f"Falha ao ler dados de {file_name}. Pulando...")
                continue

            # Verificando se as colunas existem antes de tentar converter
            if 'Valor de Venda' in df_input_data.columns:
                df_input_data['Valor de Venda'] = pd.to_numeric(df_input_data['Valor de Venda'].str.replace(',', '.'), errors='coerce')
            if 'Valor de Compra' in df_input_data.columns:
                df_input_data['Valor de Compra'] = pd.to_numeric(df_input_data['Valor de Compra'].str.replace(',', '.'), errors='coerce')

            df_with_update_date = add_metadata(df_input_data)
            if df_with_update_date is None:
                continue

            destination = configs.local_path
            output_path = os.path.join(destination, file_name)
            #output_path = os.path.join(destination, file_name.replace('.csv', '_processed.csv'))
            # Verifica se o diretório de destino existe
            os.makedirs(destination, exist_ok=True)

            save_dataframe(df_with_update_date, output_path)

            logging.info(f"Arquivo {file_name} processado e salvo com sucesso em: {output_path}")

    logging.info("Extração de todos os arquivos CSV concluída.")

if __name__ == "__main__":
    main()
