# Orquestração com Apache Airflow

O **Apache Airflow** foi utilizado para gerenciar e automatizar o pipeline ETL.

## **DAG do Projeto**
A DAG `dag_etl_pipeline_tcc` contém as seguintes etapas:
1. **Validação de Dados**: Verifica a conformidade dos dados com **Soda Core**.
2. **Extração e Transformação**: Extrai dados do PostgreSQL e converte para CSV.
3. **Carregamento**: Salva os arquivos processados no **MinIO**.

## **Código da DAG**
```python
# Insira o código da DAG do Airflow
