# Sistema de Registro de Carga de Soja

## Descrição

Este sistema automatiza o processo de registro de carga de soja transportada por caminhões. Ele captura imagens de placas de caminhões, realiza a leitura da placa, converte essa leitura em texto e utiliza um simulador para calcular o peso da carga de soja. As informações geradas são então registradas em um banco de dados Oracle e também são salvas em um arquivo `.txt` para registro e controle.

### Funcionalidades Principais:

1. **Leitura de Placa de Caminhão**: O sistema usa a tecnologia OCR (Reconhecimento Óptico de Caracteres) para ler placas de veículos a partir de imagens. A biblioteca EasyOCR é utilizada para realizar a extração de texto da placa do caminhão.

2. **Simulação de Carga**: Após a leitura da placa, o sistema simula a quantidade de soja que o caminhão está carregando. A carga é simulada aleatoriamente, gerando valores entre 20 a 40 toneladas.

3. **Registro no Banco de Dados**: As informações do caminhão (placa, modelo, ano, motorista) e da carga (peso e tipo de cultura) são registradas em um banco de dados Oracle. A tabela de cargas está vinculada à tabela de caminhões por meio de uma chave estrangeira (placa).

4. **Geração de Arquivo TXT**: Após a leitura da placa e simulação do peso, o sistema cria um arquivo `.txt` contendo as informações detalhadas da carga (placa, tipo de cultura, peso da carga), facilitando o controle físico e eletrônico.

## Como Funciona o Processo:

1. **Leitura da Placa**:
   - O sistema captura a imagem da placa do caminhão.
   - A imagem é processada pela biblioteca `EasyOCR` para reconhecer a placa do veículo.
   - O texto da placa é extraído e convertido em um formato utilizável.

2. **Simulação do Peso da Carga**:
   - Com base na placa do caminhão, o sistema simula o peso da carga transportada (soja). O peso é gerado aleatoriamente entre 20 e 40 toneladas.
   
3. **Armazenamento no Banco de Dados**:
   - A informação sobre o caminhão (placa, modelo, motorista) e a carga (tipo de cultura, peso) é registrada no banco de dados.
   - A tabela `CAMINHAO` armazena dados sobre o caminhão, enquanto a tabela `GRAO_SOJA` registra as informações da carga. A chave estrangeira da tabela `GRAO_SOJA` faz referência à tabela `CAMINHAO` através da coluna `placa`.

4. **Geração do Arquivo TXT**:
   - Após o processo de leitura e simulação, o sistema gera um arquivo `.txt` contendo as informações registradas, como a placa do caminhão, tipo de carga (soja) e peso da carga.
   
## Dependências

O sistema depende de várias bibliotecas para funcionar corretamente. Abaixo está a lista de dependências necessárias:

```txt
cffi==1.17.1
cryptography==44.0.2
cx_Oracle==8.3.0
easyocr==1.7.2
filelock==3.18.0
fsspec==2025.3.2
imageio==2.37.0
Jinja2==3.1.6
lazy_loader==0.4
MarkupSafe==3.0.2
mpmath==1.3.0
networkx==3.2.1
ninja==1.11.1.4
numpy==1.26.4
openalpr==1.1.0
opencv-python==4.11.0.86
opencv-python-headless==4.11.0.86
oracledb==3.1.0
packaging==24.2
pillow==11.2.1
pyclipper==1.3.0.post6
pycparser==2.22
pytesseract==0.3.13
python-bidi==0.6.6
PyYAML==6.0.2
scikit-image==0.24.0
scipy==1.13.1
shapely==2.0.7
sympy==1.13.3
tifffile==2024.8.30
torch==2.2.2
torchvision==0.17.2
typing_extensions==4.13.2
```

### Instalação das Dependências

Para instalar as dependências necessárias, siga os passos abaixo:

1. **Crie um ambiente virtual** (opcional, mas recomendado):
   
   ```bash
   python3 -m venv env
   ```

2. **Ative o ambiente virtual**:
   - No Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - No Linux/macOS:
     ```bash
     source env/bin/activate
     ```

3. **Instale as dependências**:
   Execute o seguinte comando para instalar todas as bibliotecas necessárias:

   ```bash
   pip install -r requirements.txt
   ```

## Estrutura do Banco de Dados

O banco de dados utilizado é o Oracle, e a estrutura do banco é a seguinte:

### Tabelas:

- **Tabela CAMINHAO**:
  - `id`: Identificador único do caminhão (PK)
  - `placa`: Placa do caminhão
  - `modelo`: Modelo do caminhão
  - `ano`: Ano de fabricação
  - `motorista`: Nome do motorista

- **Tabela GRAO_SOJA**:
  - `id`: Identificador único da carga (PK)
  - `data_registro`: Data de registro da carga (com valor padrão de `SYSDATE`)
  - `tipo_cultura`: Tipo da cultura (no caso, "soja")
  - `peso_toneladas`: Peso da carga em toneladas
  - `placa`: Chave estrangeira que faz referência à tabela `CAMINHAO` (placa)

## Exemplos de Uso

### Registrar uma Carga

Após o processamento da imagem da placa e a simulação do peso da carga, o sistema registra as informações da carga no banco de dados.

```python
from datetime import datetime
from oracle_db.conection import conectar

# Exemplo de carga simulada
carga = {
    "tipo_cultura": "soja",
    "peso_toneladas": 27.6
}

placa = "ABC1234"  # Exemplo de placa de caminhão

registrar_carga_soja_no_banco(placa, carga)
```

### Gerar o Arquivo TXT

Após o registro da carga, o sistema cria um arquivo `.txt` com as informações da carga.

```python
salvar_em_json({'placa': placa, **carga}, 'carga_soja.txt')
```

## Contribuições

Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou quiser corrigir bugs, fique à vontade para abrir uma *issue* ou submeter um *pull request*.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
```

### Explicação das Melhorias:

- **Detalhamento do Processo**: Agora o processo de leitura da placa e simulação da carga de soja está explicado claramente, com ênfase em como a carga é gerada aleatoriamente e registrada no banco de dados.
  
- **Banco de Dados**: A estrutura do banco de dados foi detalhada para que o usuário saiba como as informações de caminhões e cargas são organizadas nas tabelas.

- **Exemplos de Uso**: Foram adicionados exemplos de como registrar uma carga e gerar o arquivo `.txt` com as informações da carga, proporcionando mais clareza sobre o uso do sistema.

- **Inclusão das Dependências**: As bibliotecas necessárias para rodar o sistema foram mantidas e estão detalhadas na seção de dependências, para garantir que o sistema funcione corretamente no ambiente do usuário.
