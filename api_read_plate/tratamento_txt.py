import re

class ProcessadorPlacaOCR:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def corrigir_erro_ocr(self, placa):
        """
        Corrige possíveis erros de OCR em posições onde a placa deveria ter números.
        Padrão da placa: AAA#A## (posições 3, 5 e 6 devem ser números)
        """
        placa_corrigida = list(placa)
        substituicoes = {
            'Z': '2',
            'I': '1',
            'O': '0',
            'U': '0'
        }

        for pos in [3, 5, 6]:
            if pos < len(placa_corrigida):
                caractere = placa_corrigida[pos]
                if caractere in substituicoes:
                    placa_corrigida[pos] = substituicoes[caractere]

        return ''.join(placa_corrigida)

    def processar_texto(self, texto):
        """
        Processa o texto extraído e busca placas no formato 'BRA3R52',
        aplicando correções em possíveis erros de OCR.
        """
        texto_limpo = re.sub(r'[^A-Z0-9\s]', '', texto.upper()).replace(" ", "")
        print(f"[INFO] Texto após limpeza:\n{texto_limpo}")

        padrao_placa = r'\b[A-Z]{3}[0-9A-Z][A-Z][0-9A-Z]{2}\b'
        placas_encontradas = re.findall(padrao_placa, texto_limpo)
        placas_corrigidas = []

        for placa in placas_encontradas:
            if len(placa) == 8:
                placa = placa[:-1]
            placa_corrigida = self.corrigir_erro_ocr(placa)
            placas_corrigidas.append(placa_corrigida)

        return placas_corrigidas

    def ler_arquivo(self):
        """
        Lê o conteúdo do arquivo de texto onde estão os resultados do OCR.
        """
        try:
            with open(self.caminho_arquivo, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            print(f"[ERROR] Erro ao ler o arquivo: {e}")
            return ""

    def salvar_placa(self, placa):
        """
        Salva a placa detectada no arquivo de texto.
        """
        try:
            with open(self.caminho_arquivo, 'w', encoding='utf-8') as file:
                file.write(f"Placa detectada: {placa}")
            print(f"[INFO] Placa salva no mesmo arquivo: {self.caminho_arquivo}")
        except Exception as e:
            print(f"[ERROR] Erro ao salvar o arquivo: {e}")

    def executar(self):
        """
        Executa o processamento completo do arquivo: leitura, extração e salvamento.
        """
        texto = self.ler_arquivo()

        if texto:
            placas = self.processar_texto(texto)

            if placas:
                placa_final = placas[0]
                print(f"[INFO] Placa detectada: {placa_final}")
                self.salvar_placa(placa_final)
            else:
                print("[INFO] Nenhuma placa válida detectada.")
        else:
            print("[ERROR] Não foi possível ler o arquivo de texto.")

# Exemplo de uso
if __name__ == '__main__':
    caminho = 'api_read_plate/placa_detectada.txt'  # Pode ser parametrizado no futuro
    processador = ProcessadorPlacaOCR(caminho)
    processador.executar()
