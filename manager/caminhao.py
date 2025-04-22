import json
import re

def validar_placa(placa):
    """
    Valida se a placa está no formato Mercosul: LLLNLNN
    Ex: BRA3R52 ou BRA3R525 (se tiver número extra, será ignorado)
    """
    placa = placa.strip().upper().replace(" ", "")
    padrao = r'^[A-Z]{3}[0-9][A-Z][0-9]{2}$'
    
    if len(placa) == 8:
        placa = placa[:-1]  # Remove o número extra, se houver

    if re.fullmatch(padrao, placa):
        return placa
    else:
        return None

def cadastrar_caminhao():
    """
    Coleta dados simples de um caminhão via input, com validação da placa.
    """
    print("=== Cadastro de Caminhão ===")

    while True:
        placa_input = input("Placa (formato Mercosul): ")
        placa_valida = validar_placa(placa_input)
        if placa_valida:
            break
        else:
            print("[ERRO] Placa inválida. Exemplo válido: BRA3R52")

    modelo = input("Modelo: ").strip().title()
    ano = input("Ano: ").strip()
    motorista = input("Nome do motorista: ").strip().title()

    caminhao = {
        'placa': placa_valida,
        'modelo': modelo,
        'ano': ano,
        'motorista': motorista
    }

    return caminhao

def salvar_dados_json(dados, caminho_arquivo):
    """
    Salva os dados no JSON sobrescrevendo o conteúdo anterior.
    """
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
        print(f"[INFO] Dados salvos com sucesso em '{caminho_arquivo}'.")

if __name__ == '__main__':
    dados_caminhao = cadastrar_caminhao()
    salvar_dados_json(dados_caminhao, 'dados_caminhao.json')
