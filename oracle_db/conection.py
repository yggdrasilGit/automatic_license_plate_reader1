import oracledb

USER = 'c##francismar'
PASSWORD = 'senha123'
DSN = 'localhost/orclcdb'  # Modifique conforme seu ambiente Oracle

def conectar():
    try:
        # Utilizando um dicionário para passar os parâmetros de conexão
        conn = oracledb.connect(
            user=USER,
            password=PASSWORD,
            dsn=DSN
        )
        print("Conexão estabelecida com sucesso!")
        print(conn)
        return conn
    except Exception as e:
        print(f"[ERRO] Conexão com Oracle falhou: {e}")
        return None

conectar()

