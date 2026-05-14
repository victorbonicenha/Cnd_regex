# 🤖 Robô de Emissão de Certidões (CND)

Este projeto automatiza a emissão e salvamento de **Certidões Negativas de Débito** em diversos portais, incluindo:

- 💼 **FGTS**
- ⚖️ **Trabalhista**
- 🏛️ **Municipal**
- 📜 **Dívida Ativa**

O robô utiliza **Selenium**, **Anti-Captcha** e integração com **Telegram** para envio de status, prints e logs.  
Além disso, os resultados são registrados em um banco de dados via **config_banco.py**.

---

## 📂 Estrutura do Projeto
```bash
CND_Robo/
│
├── 📜 main.py                # Código principal (executa todas as certidões)
├── 📜 config_banco.py        # Controle de logs no banco de dados
├── 📜 config_telegram.py     # Envio de mensagens e imagens ao Telegram
├── 🔑 .env                   # Variáveis de ambiente (NÃO subir no GitHub)
├── 📦 requirements.txt       # Dependências do projeto
└── 📘 README.md              # Documentação
```

---

⚙️ Pré-requisitos
```bash
🔹 Python 3.9+  
🔹 Google Chrome instalado  
🔹 ChromeDriver (gerenciado automaticamente pelo webdriver-manager)  
🔹 Conta no Anti-Captcha  
🔹 Bot no Telegram  
```

---

📥 Instalação e Uso

1️⃣ Clone este repositório
```bash
git clone https://github.com/seuusuario/CND_Robo.git
cd CND_Robo
```

---

2️⃣ Crie e ative o ambiente virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python3 -m venv venv
source venv/bin/activate
```

---

3️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```

---

4️⃣ Configure o arquivo .env

Crie um arquivo .env na raiz do projeto e adicione suas credenciais:
```bash
# Telegram
ITOKEN=
CHAT_ID=

# Banco de dados
DB_HOST=
DB_NAME=
DB_USER=
DB_PASS=

# CNPJ / CPF
CNPJ_BASE=
CNPJ_BASICO=
CNPJ_SC=
CPF=

# Anti-Captcha
CHAVE_API=

# Paths
BASE_PATH=
```

---

5️⃣ Execução

Para rodar o robô principal:
```bash
python main.py
