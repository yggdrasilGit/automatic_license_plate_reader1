

from oracle_db.conection import conectar
from oracle_db.criar_tabela import executar_arquivo_sql


def create(table, data: dict):
    conn = conectar()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        colunas = ', '.join(data.keys())
        valores = ', '.join([f':{i+1}' for i in range(len(data))])
        sql = f"INSERT INTO {table} ({colunas}) VALUES ({valores})"
        cursor.execute(sql, list(data.values()))
        conn.commit()
        print("[INFO] Registro criado com sucesso.")
    except Exception as e:
        print(f"[ERRO] CREATE: {e}")
    finally:
        conn.close()

def read_plate(table: str, filtro: str = None):
    conn = conectar()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = f"SELECT * FROM {table}"
        if filtro:
            sql += f" WHERE {filtro}"
        cursor.execute(sql)
        colunas = [desc[0] for desc in cursor.description]
        resultados = cursor.fetchall()
        
        if resultados:
            for row in resultados:
                print(dict(zip(colunas, row)))
        else:
            print(f"[INFO] Nenhum registro encontrado na tabela '{table}'.")

    except Exception as e:
        print(f"[ERRO] READ: {e}")
    finally:
        conn.close()


def read(table, filtro=None):
    conn = conectar()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = f"SELECT * FROM {table}"
        if filtro:
            sql += f" WHERE {filtro}"
        cursor.execute(sql)
        colunas = [desc[0] for desc in cursor.description]
        resultados = cursor.fetchall()
        for row in resultados:
            print(dict(zip(colunas, row)))
    except Exception as e:
        print(f"[ERRO] READ: {e}")
    finally:
        conn.close()

def update(table, data: dict, filtro):
    conn = conectar()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        set_clause = ', '.join([f"{col} = :{i+1}" for i, col in enumerate(data.keys())])
        sql = f"UPDATE {table} SET {set_clause} WHERE {filtro}"
        cursor.execute(sql, list(data.values()))
        conn.commit()
        print("[INFO] Registro atualizado com sucesso.")
    except Exception as e:
        print(f"[ERRO] UPDATE: {e}")
    finally:
        conn.close()

def delete(table, filtro):
    conn = conectar()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        sql = f"DELETE FROM {table} WHERE {filtro}"
        cursor.execute(sql)
        conn.commit()
        print("[INFO] Registro excluído com sucesso.")
    except Exception as e:
        print(f"[ERRO] DELETE: {e}")
    finally:
        conn.close()

def verificar_tabela_existente(conn, nome_tabela):
    cursor = conn.cursor()
    try:
        # Verifica se a tabela já existe no banco de dados
        query = f"SELECT COUNT(*) FROM user_tables WHERE table_name = UPPER('{nome_tabela}')"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0] > 0  # Se 0, não existe; se > 0, a tabela existe
    except Exception as e:
        print(f"[ERRO] Ao verificar a tabela: {e}")
        return False
    finally:
        cursor.close()
        
def conferir_tabela():
    conn = conectar()
    if conn:
        nome_tabela = "CAMINHAO"  # Nome da tabela que você quer verificar
        nome_tabela_2 = "GRAO_SOJA"
        if verificar_tabela_existente(conn, nome_tabela_2):
            print(f"A tabela '{nome_tabela_2}' já existe. Não será criada novamente.")
        else:
            print(f"A tabela '{nome_tabela}' não existe. Criando...")
            executar_arquivo_sql("sql_table/tabela_cadastra_motorista.sql")

        conn.close()

