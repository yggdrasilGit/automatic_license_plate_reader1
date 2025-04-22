import random
import json

def gerar_carga_soja():
    """
    Gera uma carga de caminhão com cultura 'soja' e peso aleatório.
    """
    tipo_cultura = 'soja'
    peso_carga = round(random.uniform(20.0, 40.0), 1)
    numero_caminhao = random.randint(1, 100)

    return {
        'caminhao': f'Caminhão #{numero_caminhao}',
        'tipo_cultura': tipo_cultura,
        'peso_toneladas': peso_carga
    }

def salvar_em_json(dados, caminho_arquivo):
    """
    Salva os dados em formato JSON, sobrescrevendo o conteúdo anterior.
    """
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
        print(f"[INFO] Carga salva em {caminho_arquivo}")


def carregar_dados_json(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            print("\n--- Dados Carregados do JSON ---")
            for item in dados:
                print(item)
            return dados
    except FileNotFoundError:
        print(f"[ERRO] Arquivo '{caminho_arquivo}' não encontrado.")
    except json.JSONDecodeError as e:
        print(f"[ERRO] JSON inválido: {e}")
    except Exception as e:
        print(f"[ERRO] Erro ao carregar JSON: {e}")
    return []

#if __name__ == '__main__':
    #carga = gerar_carga_soja()
    #salvar_em_json(carga, 'carga_soja.json')
