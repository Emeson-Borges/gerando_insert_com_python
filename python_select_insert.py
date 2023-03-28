import psycopg2

def generate_insert_sql_file(table_name, output_file):
    # Conecta ao banco de dados
    conn = psycopg2.connect(
        host="localhost",
        database="pmssojoaodaponta",
        user="postgres",
        password="20221612"
    )
    cur = conn.cursor()

    # Obtem o nome das colunas da tabela
    cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}';")
    columns = [row[0] for row in cur.fetchall()]

    # Executa a consulta SQL para obter as linhas da tabela
    cur.execute(f"SELECT * FROM {table_name};")
    rows = cur.fetchall()

    # Escreve as linhas no arquivo de saída com os valores e as colunas
    with open(output_file, 'w') as arquivo:
        for row in rows:
            # Cria a string de valores
            values_str = ', '.join([f"'{str(value)}'" for value in row])
            # Cria a string de colunas
            columns_str = ', '.join(columns)
            # Cria a string de insert SQL com as colunas e os valores correspondentes
            insert_sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str});\n"
            # Escreve no arquivo de saída
            arquivo.write(insert_sql)

    # Fecha a conexão com o banco de dados
    conn.close()

generate_insert_sql_file('esocial.s2200', 'insert.sql')
