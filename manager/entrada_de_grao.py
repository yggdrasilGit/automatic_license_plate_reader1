from oracle_db.conection import conectar

def registrar_carga_soja_no_banco(placa, carga):
    conn = conectar()
    if not conn:
        print("[ERRO] Não foi possível conectar ao banco de dados.")
        return
    try:
        cursor = conn.cursor()

        # Busca o ID do caminhão pela placa
        cursor.execute("SELECT id FROM CAMINHAO WHERE placa = :1", [placa])
        resultado = cursor.fetchone()
        if not resultado:
            print(f"[ERRO] Caminhão com placa '{placa}' não encontrado.")
            return

        caminhao_id = resultado[0]

        sql = """
            INSERT INTO GRAO_SOJA (tipo_cultura, peso_toneladas, caminhao_id)
            VALUES (:1, :2, :3)
        """
        cursor.execute(sql, [carga['tipo_cultura'], carga['peso_toneladas'], caminhao_id])
        conn.commit()
        print("[INFO] Carga registrada com sucesso no banco de dados.")
    except Exception as e:
        print(f"[ERRO] Falha ao registrar a carga: {e}")
    finally:
        conn.close()
