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

4. Run the original (readable) script
```bash
python3 mlw_extractor.py path/to/file.mlw
```
- Output: a file named `path/to/file.mp4` (same basename as input) will be created if decryption succeeds.

5. Use the obfuscated version (if included)
- If this repository includes an obfuscated build in `obf_dist/` and you prefer to run that:
```bash
python3 obf_dist/mlw_extractor.py path/to/file.mlw
```
- Note: the obfuscated runtime (`pyarmor_runtime_000000/`) must be present next to the obfuscated script. The obfuscated build may be platform-specific (e.g., linux.x86_64).

6. Deactivate venv when done
```bash
deactivate
```

7. Troubleshooting
- InvalidTag / authentication error — means key/iv/tag/ciphertext mismatch; check you used the correct file and key.
- If Python complains about missing packages, ensure you activated the virtualenv and ran `pip install -r requirements.txt`.
- If the obfuscated script fails with runtime-related errors, confirm the `pyarmor_runtime_000000/` folder exists and matches your platform.

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

4. Executar o script original (legível)
```bash
python3 mlw_extractor.py caminho/para/arquivo.mlw
```
- Saída: será gerado `caminho/para/arquivo.mp4` (mesmo nome base) se a descriptografia for bem-sucedida.

5. Usar a versão ofuscada (se incluída)
- Se este repositório incluir `obf_dist/` com a versão ofuscada, rode:
```bash
python3 obf_dist/mlw_extractor.py caminho/para/arquivo.mlw
```
- Observação: a pasta `pyarmor_runtime_000000/` deve estar presente junto ao script ofuscado. A build ofuscada pode ser específica de plataforma (ex.: linux.x86_64).

6. Desativar o venv quando terminar
```bash
deactivate
```

7. Resolução de problemas
- Erro InvalidTag — indica que a tag de autenticação não conferiu (chave/iv/ct/tag incorretos ou arquivo corrompido).
- Se faltar algum pacote Python, ative o venv e execute `pip install -r requirements.txt`.
- Se a versão ofuscada falhar por runtime, confirme se a pasta `pyarmor_runtime_000000/` está no mesmo diretório e compatível com sua plataforma.

---

### Files and structure / Arquivos e estrutura recomendada

- mlw_extractor.py — original script (readable)
- obf_dist/ — optional: PyArmor obfuscated output (not committed by default)
- pyarmor_runtime_000000/ — required if using obf_dist/mlw_extractor.py (must be present alongside obfuscated script)
- requirements.txt — Python dependencies (e.g., cryptography)
- .gitignore — ignores venv, build artifacts, and media files

---

### Security note / Observações de segurança

- The obfuscation only increases the effort required to read the source; it does not make it impossible. Do not store long-term secrets (private keys, production secrets) directly in the source code. Use environment variables or secret managers for sensitive data.
- The obfuscated runtime is often platform-specific — if you plan to distribute cross-platform, build obfuscated artifacts for each target platform.

---

Se quiser, eu adapto o README para incluir:
- O comando exato do seu repositório (substituindo `your-username` por `ph-py`),
- O bloco de exemplo de commit/push,
- E instruções para criar o requirements.txt automaticamente a partir do venv (`pip freeze > requirements.txt`).

Quer que eu já gere o README.md pronto com esses ajustes personalizados para o seu repositório (incluindo seu nome de usuário e comando git)?
