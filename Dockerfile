# Use a imagem base oficial do Python
FROM python:3.10-slim

# Define o diretório de trabalho na imagem
WORKDIR /src


# Copia o arquivo de requisitos para a imagem
COPY requirements.txt .
COPY ./arquivos_csv arquivos_csv/

# Instala as dependências listadas no arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo do diretório local para o diretório de trabalho na imagem
COPY src/ .

# Expõe a porta que sua aplicação vai usar (se aplicável)
# EXPOSE 8080

# Define a variável de ambiente para garantir que os logs do Python sejam exibidos corretamente
ENV PYTHONUNBUFFERED=1

# Comando para executar a aplicação
CMD ["python", "orchestrator.py"]
