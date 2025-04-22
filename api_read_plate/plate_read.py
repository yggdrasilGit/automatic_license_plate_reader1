import os
import cv2
import easyocr
import numpy as np

class PlacaOCR:
    def __init__(self, image_name='test_plate.png', idioma='pt', usar_gpu=False):
        self.reader = easyocr.Reader([idioma], gpu=usar_gpu)
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.image_path = os.path.join(self.current_dir, 'images', image_name)
        self.output_file = os.path.join(self.current_dir, 'placa_detectada.txt')

    def verificar_imagem(self):
        if not os.path.exists(self.image_path):
            print(f"[ERRO] Imagem não encontrada em: {self.image_path}")
            return False
        return True

    def carregar_imagem(self):
        image = cv2.imread(self.image_path)
        if image is None:
            print("[ERRO] Não foi possível carregar a imagem. Verifique o formato ou o caminho.")
            return None
        return image

    def preprocessar_imagem(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (3, 3), 0)
        _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)

    def extrair_texto(self, imagem):
        resultados = self.reader.readtext(imagem)
        return resultados

    def salvar_resultado(self, resultados):
        with open(self.output_file, 'w') as f:
            for _, text, _ in resultados:
                f.write(text.strip() + '\n')
        print(f"[INFO] Resultado salvo em: {self.output_file}")

    def executar(self):
        if not self.verificar_imagem():
            return

        imagem = self.carregar_imagem()
        if imagem is None:
            return

        imagem_processada = self.preprocessar_imagem(imagem)
        resultados = self.extrair_texto(imagem_processada)

        if not resultados:
            print("[INFO] Nenhum texto detectado na imagem.")
        else:
            print("[INFO] Resultados encontrados:")
            for _, text, conf in resultados:
                print(f"Texto: {text.strip()} | Confiança: {round(conf * 100, 2)}%")
            self.salvar_resultado(resultados)

# Exemplo de uso
# if __name__ == '__main__':
#     ocr = PlacaOCR()
#     ocr.executar()

