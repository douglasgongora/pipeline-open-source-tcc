# Documentação do Script - Soda Scan Schema

## Descrição

Este script Python executa o comando `soda scan` para realizar a verificação de qualidade de dados utilizando a ferramenta Soda. Ele se conecta a um banco de dados PostgreSQL e usa arquivos de configuração YAML para definir a conexão e os checks de qualidade a serem executados.

## Funcionamento

O script realiza os seguintes passos:

1. Executa o comando `soda scan` com as opções e parâmetros configurados.
2. Captura a saída padrão (STDOUT) e a saída de erro (STDERR) do comando.
3. Verifica o código de retorno do comando para determinar se a execução foi bem-sucedida.
4. Em caso de erro na execução, exibe uma mensagem de erro e encerra o script com um código de erro.

## Requisitos

- Python 3.x
- Soda CLI instalada
- Banco de dados PostgreSQL configurado e acessível
- Arquivos de configuração:
  - `./contracts/configuration.yml`
  - `./contracts/checks.yml`

## Arquivos de Configuração

- **configuration.yml**: Arquivo que contém a configuração da conexão com o banco de dados e outros parâmetros necessários para a execução do comando `soda scan`.
- **checks.yml**: Arquivo que define os checks de qualidade de dados a serem realizados pelo Soda.

## Como Executar

1. Certifique-se de que o Python e a Soda CLI estão instalados.
2. Prepare os arquivos de configuração `configuration.yml` e `checks.yml`.
3. Execute o script Python:

   ```bash
   python run_soda_scan.py
