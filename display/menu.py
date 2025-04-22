

from api_read_plate.plate_read import PlacaOCR
from api_read_plate.tratamento_txt import ProcessadorPlacaOCR
from manager.caminhao import cadastrar_caminhao, salvar_dados_json
from manager.entrada_de_grao import registrar_carga_soja_no_banco
from oracle_db.conection import conectar
from oracle_db.crud import conferir_tabela, create, read, read_plate, update
from simulador_carga.simulador_carga import carregar_dados_json, gerar_carga_soja, salvar_em_json


def menu():
    conn = None  # Inicializa a variável de conexão
    while True:
        print("\nMenu de Opções:")
        print("1. Conectar ao banco de dados")
        print("2. Cadastro de Caminhões")
        print("3. Entrada de Camimhão")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ")

        if opcao == "1":
            conn = conectar()
            if conn:
                print("Conexão bem-sucedida.")
                conferir_tabela()
            else:
                print("Falha ao conectar ao banco de dados.")

        elif opcao == "2":
            caminhao = cadastrar_caminhao()
            salvar_dados_json(caminhao, 'dados_caminhao.json')
            caminho_arquivo = "dados_caminhao.json"
            db_dados = carregar_dados_json(caminho_arquivo)
            create(table = "CAMINHAO", data = db_dados)

        elif opcao == "3":
            ocr = PlacaOCR()
            ocr.executar()
            caminho = 'api_read_plate/placa_detectada.txt'  # Pode ser parametrizado no futuro
            processador = ProcessadorPlacaOCR(caminho)
            processador.executar()
            placa = processador.ler_arquivo()
            placa = placa[17:]
            carga = gerar_carga_soja()
            print(read_plate("CAMINHAO", placa))
            salvar_em_json({'placa': placa, **carga}, 'carga_soja.json')
            registrar_carga_soja_no_banco(placa, carga)
            
            

        elif opcao == "4":
            print("Saindo...")
            break  # Sai do loop e termina o programa

        else:
            print("Opção inválida. Tente novamente.")
