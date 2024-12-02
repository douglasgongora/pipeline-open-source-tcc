CREATE TABLE hive.landing.department_parquet (
   departmentid varchar,
   name varchar,
   groupname varchar,
   modifieddate varchar,
   last_update varchar
)
WITH (
   external_location = 's3a://landing/humanresources_department_parquet',
   format = 'PARQUET'
);



CREATE TABLE hive.landing.humanresources_department (
   departmentid varchar,
   name varchar,
   groupname varchar,
   modifieddate varchar,
   last_update varchar
)
WITH (
   external_location = 's3a://landing/humanresources_department',
   format = 'csv'
);



CREATE TABLE hive.landing.titles (
  id VARCHAR,
  title VARCHAR,
  type VARCHAR,
  description VARCHAR,
  release_year VARCHAR,
  age_certification VARCHAR,
  runtime VARCHAR,
  genres VARCHAR,
  production_countries VARCHAR,
  seasons VARCHAR,
  imdb_id VARCHAR,
  imdb_score VARCHAR,
  imdb_votes VARCHAR,
  tmdb_popularity VARCHAR,
  tmdb_score VARCHAR
) WITH (
  format='CSV',
  external_location='s3a://landing/titles/',
  skip_header_line_count=1
)


CREATE SCHEMA hive.landing WITH (location='s3a://landing/')



CREATE TABLE hive.landing.humanresources_employee (
   businessentityid varchar,
   nationalidnumber varchar,
   loginid varchar,
   jobtitle varchar,
   birthdate varchar,
   maritalstatus varchar,
   gender varchar,
   hiredate varchar,
   salariedflag varchar,
   vacationhours varchar,
   sickleavehours varchar,
   currentflag varchar,
   rowguid varchar,
   modifieddate varchar,
   organizationnode varchar,
   last_update varchar
)
WITH (
   external_location = 's3a://landing/humanresources_employee',
   format = 'csv'
);

CREATE TABLE hive.landing.sales_countryregioncurrency (
   countryregioncode varchar,
   currencycode varchar,
   modifieddate varchar,
   last_update varchar
)
WITH (
   external_location = 's3a://landing/sales_countryregioncurrency',
   format = 'csv'
);

CREATE TABLE hive.landing.sales_creditcard (
   creditcardid varchar,
   cardtype varchar,
   cardnumber varchar,
   expmonth varchar,
   expyear varchar,
   modifieddate varchar,
   last_update varchar
)
WITH (
   external_location = 's3a://landing/sales_creditcard',
   format = 'csv'
);


CREATE TABLE hive.landing.sales_salesorderheader (
   salesorderid varchar,
   revisionnumber varchar,
   orderdate varchar,
   duedate varchar,
   shipdate varchar,
   status varchar,
   onlineorderflag varchar,
   purchaseordernumber varchar,
   accountnumber varchar,
   customerid varchar,
   salespersonid varchar,
   territoryid varchar,
   billtoaddressid varchar,
   shiptoaddressid varchar,
   shipmethodid varchar,
   creditcardid varchar,
   creditcardapprovalcode varchar,
   currencyrateid varchar,
   subtotal varchar,
   taxamt varchar,
   freight varchar,
   totaldue varchar,
   comment varchar,
   modifieddate varchar,
   last_update varchar
)
WITH (
   external_location = 's3a://landing/sales_salesorderheader',
   format = 'csv'
);


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



CREATE TABLE hive.landing.department_parquet (
   departmentid varchar,
   name varchar,
   groupname varchar,
   modifieddate varchar,
   last_update varchar
)
WITH (
   external_location = 's3a://landing/humanresources_department_parquet',
   format = 'PARQUET'
);



CREATE TABLE hive.landing.department_tcc_csv (
   departmentid varchar,
   name varchar,
   groupname varchar,
   modifieddate varchar,
   last_update varchar
)
WITH (
   external_location = 's3a://landing/humanresources_department_tcc_csv',
   format = 'csv'
);



CREATE TABLE hive.landing.titles (
  id VARCHAR,
  title VARCHAR,
  type VARCHAR,
  description VARCHAR,
  release_year VARCHAR,
  age_certification VARCHAR,
  runtime VARCHAR,
  genres VARCHAR,
  production_countries VARCHAR,
  seasons VARCHAR,
  imdb_id VARCHAR,
  imdb_score VARCHAR,
  imdb_votes VARCHAR,
  tmdb_popularity VARCHAR,
  tmdb_score VARCHAR
) WITH (
  format='CSV',
  external_location='s3a://landing/titles/',
  skip_header_line_count=1
)


CREATE SCHEMA hive.landing WITH (location='s3a://landing/')
