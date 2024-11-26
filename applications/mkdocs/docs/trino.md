# Integração com Trino e MinIO

O **Trino** foi configurado para consultar dados processados e armazenados no **MinIO**, proporcionando uma camada de consulta SQL rápida e eficiente. Nesta seção, explicamos como o Trino foi configurado para acessar o bucket `landing` no MinIO e realizar consultas nos dados.

---

## **Configuração da Tabela no Trino**

Os dados do MinIO foram expostos ao Trino utilizando a tabela abaixo:

```sql
CREATE TABLE hive.landing.preco_automotivo (
   estado VARCHAR,
   municipio VARCHAR,
   revenda VARCHAR,
   cnpj_da_revenda VARCHAR,
   nome_da_rua VARCHAR,
   numero_rua VARCHAR,
   complemento VARCHAR,
   bairro VARCHAR,
   cep VARCHAR,
   produto VARCHAR,
   data_da_coleta VARCHAR,
   valor_de_venda VARCHAR,
   valor_de_compra VARCHAR,
   unidade_de_medida VARCHAR,
   bandeira VARCHAR,
   last_update VARCHAR
)
WITH (
   external_location = 's3a://landing/preco_automotivo',
   format = 'csv'
);
