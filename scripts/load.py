import os
from minio import Minio
from configs import configs

# Initialize MinIO client
client = configs.credential_minio

# Local folder containing CSV files
local_folder_path = configs.local_path

# List all files in the local folder
files = os.listdir(local_folder_path)

for file in files:
    if file.endswith('.csv'):
        file_path = os.path.join(local_folder_path, file)
        
        # Define the folder inside the bucket based on file name (without extension)
        folder_name = os.path.splitext(file)[0]  # Remove the '.csv' extension
        bucket_path = f"{folder_name}/{file}"    # Each file goes into a folder with its own name

        # Upload CSV file to MinIO within the specified folder
        with open(file_path, 'rb') as file_data:
            file_stat = os.stat(file_path)
            client.put_object('landing', bucket_path, file_data, file_stat.st_size)

            print(f"Uploaded {file} to MinIO bucket 'landing' in folder '{folder_name}'")
