

from oracle_db.conection import conectar


def executar_arquivo_sql(caminho_arquivo_sql):
    conexao = conectar()
    if not conexao:
        return

    try:
        with open(caminho_arquivo_sql, 'r', encoding='utf-8') as arquivo:
            comandos_sql = arquivo.read()

        # Divide comandos por ponto e vírgula, remove linhas vazias
        comandos = [cmd.strip() for cmd in comandos_sql.split(';') if cmd.strip()]

        cursor = conexao.cursor()
        for comando in comandos:
            print(f"[INFO] Executando: {comando[:50]}...")
            cursor.execute(comando)
        conexao.commit()
        print("[INFO] Comandos SQL executados com sucesso.")
    except Exception as e:
        print(f"[ERRO] Falha ao executar SQL: {e}")
    finally:
        conexao.close()

#if __name__ == "__main__":
    #executar_arquivo_sql("criar_tabela.sql")
