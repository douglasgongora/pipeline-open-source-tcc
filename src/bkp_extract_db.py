import logging
from configs import configs
from configs.host import host
from functions import functions as F
from plugins.postgres_data_reader import PostgresDataReader

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_data(data_reader, table_name):
    try:
        return data_reader.read_data(table_name)
    except Exception as e:
        logging.error(f"Error reading data from table {table_name}: {str(e)}")
        return None

def add_metadata(df):
    try:
        return F.add_metadata(df)
    except Exception as e:
        logging.error(f"Error adding metadata to DataFrame: {str(e)}")
        return None

def add_month_key(df, column_name):
    try:
        return F.add_month_key_column(df, column_name)
    except Exception as e:
        logging.error(f"Error adding month key to DataFrame: {str(e)}")
        return None

def save_dataframe(df, file_path):
    try:
        df.to_csv(file_path, sep=',', index=False)
        logging.info(f"DataFrame saved to: {file_path}")
    except Exception as e:
        logging.error(f"Error saving DataFrame to {file_path}: {str(e)}")

def main():
    logging.info("Starting ingestions from AdventureWorks to Landing Zone...")

    db_params = configs.credential_postgres_adventureworks
    data_reader = PostgresDataReader(db_params)

    if not data_reader.connect():
        logging.error("Failed to connect to the database. Exiting...")
        exit(1)

    try:
        for table_input_name in configs.tables_postgres_adventureworks.values():
            try:
                table_input_path = F.convert_table_name(table_input_name)

                df_input_data = read_data(data_reader, table_input_name)
                if df_input_data is None:
                    continue

                logging.info(f"Processing table: {table_input_path}")

                df_with_update_date = add_metadata(df_input_data)
                if df_with_update_date is None:
                    continue

                destination = configs.local_path
                local_path_csv = f"{destination}{table_input_path}.csv"
                save_dataframe(df_with_update_date, local_path_csv)

                logging.info(f"Table {table_input_path} successfully processed and saved to CSV: {local_path_csv}")

            except Exception as e:
                logging.error(f"Error processing table {table_input_name}: {str(e)}")

    finally:
        data_reader.disconnect()
        logging.info("Extraction Completed!")

if __name__ == "__main__":
    main()
