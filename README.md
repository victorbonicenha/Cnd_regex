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
# CNPJs e CPF
CNPJ_BASE=00000000
CNPJ_BASICO=000000
CNPJ_SC=00000000000000
CPF=00000000000

# AntiCaptcha
CHAVE_API=CHAVE_AQUI

# Telegram
ITOKEN=SEU_TOKEN_TELEGRAM
CHAT_ID=SEU_CHAT_ID

# Caminhos
BASE_PATH=C:\Users\seuusuario\Desktop\Certidoes
```

---

5️⃣ Execução

Para rodar o robô principal:
```bash
python main.py
