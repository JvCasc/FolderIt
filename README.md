# 📂 FoldIt

O **FoldIt** é um script de automação em Python desenvolvido para acabar com a bagunça eterna da pasta de Downloads. Ele monitora a pasta em tempo real e move cada arquivo para o lugar certo.

## ✨ Funcionalidades

* **Monitoramento Ativo:** Utiliza a biblioteca `watchdog` para detectar novos arquivos instantaneamente.
* **Organização Inteligente:** Separa arquivos por categorias (Imagens, Documentos, Executáveis, etc.).
* **Automação Silenciosa:** Roda em segundo plano enquanto você trabalha ou estuda.

## 🚀 Tecnologias Utilizadas

* `pathlib` (Manipulação de caminhos)
* `watchdog` (Monitoramento de eventos do sistema)
* `shutil` (Movimentação de arquivos)

## 🛠️ Como configurar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/FoldIt.git](https://github.com/seu-usuario/FoldIt.git)
   cd FoldIt

2.   **Crie e ative seu ambiente virtual:**
    # No Windows
    python -m venv venv
    .\venv\Scripts\activate

3.  **Instale as dependências:**
    pip install watchdog

4.  **Execute o script:**
    python main.py

## 📂 Como acontece 

O script identifica o arquivo e o envia para a pasta correspondente:

| Categoria | Extensões |
| :--- | :--- |
| **Imagens** | .jpg, .jpeg, .png, .gif |
| **Documentos** | .pdf, .docx, .txt, .xlsx |
| **Compactados** | .zip, .rar, .7z |
| **Executáveis** | .exe, .msi |
| **Projetos** | .py, .asc (LTspice), .raw
