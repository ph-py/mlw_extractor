### MLW Extractor

English (EN)

## MLW Extractor
A Python utility for extracting video files from .mlw containers (used by Live Wallpaper applications). The script performs binary analysis to locate metadata, identifies the Initialization Vector (IV) and authentication tag, and employs AES-128 GCM decryption to restore the original video in .mp4 format.

Português (PT-BR)

## MLW Extractor
Ferramenta em Python para extração de arquivos de vídeo de containers .mlw (utilizados em aplicativos de Live Wallpaper). O script realiza a análise binária do arquivo para localizar metadados, identifica o vetor de inicialização (IV) e a tag de autenticação, e utiliza criptografia AES-128 no modo GCM para descriptografar e restaurar o vídeo original no formato .mp4.

---

## How to install and use / Como instalar e usar

Below are step-by-step instructions in both English and Portuguese to set up a virtual environment, install dependencies, test the script, and (optionally) use the obfuscated PyArmor build included in this repository.

Abaixo estão instruções passo a passo em inglês e português para criar um ambiente virtual, instalar dependências, testar o script e (opcionalmente) usar a versão ofuscada gerada pelo PyArmor incluída neste repositório.

---

### English — Quick start

1. Clone the repository
```bash
git clone https://github.com/your-username/mlw_extractor.git
cd mlw_extractor
```

2. Create and activate a Python virtual environment (recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```
- If `pip install cryptography` fails, install system dependencies first (Debian/Ubuntu):
```bash
sudo apt update
sudo apt install build-essential libssl-dev libffi-dev python3-dev
pip install -r requirements.txt
```

4. Run the script
```bash
python3 mlw_extractor.py path/to/file.mlw
```

5. Deactivate venv when done
```bash
deactivate
```

6. Troubleshooting
- InvalidTag / authentication error — means key/iv/tag/ciphertext mismatch; check you used the correct file and key.
- If Python complains about missing packages, ensure you activated the virtualenv and ran `pip install -r requirements.txt`.
---

### Português — Passo a passo

1. Clonar repositório
```bash
git clone https://github.com/seu-usuario/mlw_extractor.git
cd mlw_extractor
```

2. Criar e ativar um ambiente virtual (recomendado)
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instalar dependências
```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```
- Se falhar ao instalar `cryptography`, instale dependências do sistema (Debian/Ubuntu):
```bash
sudo apt update
sudo apt install build-essential libssl-dev libffi-dev python3-dev
pip install -r requirements.txt
```

4. Executar o script
```bash
python3 mlw_extractor.py caminho/para/arquivo.mlw
```

5. Desativar o venv quando terminar
```bash
deactivate
```

6. Resolução de problemas
- Erro InvalidTag — indica que a tag de autenticação não conferiu (chave/iv/ct/tag incorretos ou arquivo corrompido).
- Se faltar algum pacote Python, ative o venv e execute `pip install -r requirements.txt`.
---
