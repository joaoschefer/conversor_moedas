# Instruções para Rodar o Programa de Conversão de Moedas

Para rodar este programa em sua máquina, siga os passos abaixo:

## 1. Instalar e Configurar o Banco de Dados PostgreSQL e o PgAdmin

1. **Baixar e instalar o PostgreSQL**:

   - Acesse o [site oficial do PostgreSQL](https://www.postgresql.org/download/) e faça o download da versão apropriada para o seu sistema operacional.
   - Siga as instruções do instalador para concluir a instalação.

2. **Configurar o PgAdmin**:
   - Durante a instalação do PostgreSQL, você terá a opção de instalar o PgAdmin, uma ferramenta de gerenciamento de bancos de dados. Certifique-se de que esta opção esteja selecionada.
   - Após a instalação, abra o PgAdmin e configure um novo banco de dados.

## 2. Configurar as Informações do Banco de Dados no Código

Abra o código Python e substitua as informações de conexão com o banco de dados pelos seus próprios dados:

```python
conn = psycopg2.connect(
    dbname="python_cotacoes",  # Nome do banco de dados
    user="postgres",           # Nome de usuário do PostgreSQL
    password="root",           # Senha do usuário do PostgreSQL
    host="localhost",          # Host (geralmente localhost)
    port="5432"                # Porta do PostgreSQL (geralmente 5432)
)
```
