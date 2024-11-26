# Pipeline ETL

Este pipeline ETL foi projetado para extrair, transformar e carregar dados, integrando várias ferramentas modernas.

## **Fluxo do Pipeline**
1. **Extração**:
   - Dados extraídos do banco de dados PostgreSQL.
2. **Transformação**:
   - Validação de qualidade utilizando **Soda Core**.
   - Conversão para o formato **CSV**.
3. **Carregamento**:
   - Dados salvos no **MinIO**.

## **Tecnologias Utilizadas**
- **PostgreSQL**: Banco de dados relacional.
- **Pandas**: Manipulação de dados.
- **MinIO**: Armazenamento de objetos compatível com S3.

*(Adicione prints ou diagramas do pipeline aqui.)*
