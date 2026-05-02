# 🧪 Test Automation — Petstore API + SauceDemo Web

Projeto de automação de testes cobrindo API REST e interface Web, com pipeline de CI/CD via GitHub Actions.

| Camada | Ferramenta | Alvo |
|--------|-----------|------|
| API    | Python + Requests + Pytest | Petstore Swagger |
| Web    | Python + Selenium + Pytest | SauceDemo |
| CI/CD  | GitHub Actions | Ambos |

---

## 📁 Estrutura do Projeto

```
test-automation/
├── .github/
│   └── workflows/
│       └── ci.yml              # Pipeline CI (API + Web)
├── api-tests/
│   ├── test_pet.py             # Endpoints /pet
│   ├── test_store.py           # Endpoints /store
│   ├── test_user.py            # Endpoints /user
│   └── requirements.txt
├── web-tests/
│   ├── pages/
│   │   ├── login_page.py       # Page Object - Login
│   │   ├── inventory_page.py   # Page Object - Produtos
│   │   ├── cart_page.py        # Page Object - Carrinho
│   │   └── checkout_page.py    # Page Object - Checkout
│   ├── tests/
│   │   └── test_saucedemo.py   # Testes E2E
│   ├── conftest.py             # Fixture do WebDriver
│   └── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Pré-requisitos

- Python 3.10+
- Google Chrome instalado
- Git instalado

---

## 🚀 Instalação e Execução Local

### 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/test-automation.git
cd test-automation
```

### 2. Testes de API

```bash
cd api-tests
pip install -r requirements.txt
pytest -v
```

### 3. Testes Web (Selenium)

```bash
cd web-tests
pip install -r requirements.txt
pytest tests/ -v
```

> O `webdriver-manager` instala o ChromeDriver automaticamente. Não precisa baixar nada manualmente.

---

## 🔬 Cenários Testados

### API — Petstore (`https://petstore.swagger.io/v2`)

**Pet**
- Criar pet (`POST /pet`)
- Buscar pet por ID (`GET /pet/{id}`)
- Atualizar pet (`PUT /pet`)
- Listar pets por status (`GET /pet/findByStatus`)
- Deletar pet (`DELETE /pet/{id}`)

**Store**
- Consultar inventário (`GET /store/inventory`)
- Criar pedido (`POST /store/order`)
- Buscar pedido por ID (`GET /store/order/{id}`)
- Deletar pedido (`DELETE /store/order/{id}`)

**User**
- Criar usuário (`POST /user`)
- Buscar usuário por username (`GET /user/{username}`)
- Atualizar usuário (`PUT /user/{username}`)
- Login (`GET /user/login`)
- Logout (`GET /user/logout`)
- Deletar usuário (`DELETE /user/{username}`)

### Web — SauceDemo (`https://www.saucedemo.com`)

- Login com credenciais válidas
- Login com credenciais inválidas (validação de erro)
- Adicionar produto ao carrinho
- **Fluxo E2E completo:** login → adicionar 2 produtos → ir ao carrinho → preencher dados → finalizar compra → validar confirmação

---

## 🏗️ Design Patterns

- **Page Object Model (POM):** cada página da aplicação tem sua própria classe, separando a lógica de localização de elementos dos testes.
- **Fixtures (pytest):** setup/teardown de dados de teste isolados por cenário.
- **Headless Chrome:** execução sem interface gráfica, compatível com CI.

---

## 🔄 Pipeline CI/CD (GitHub Actions)

A pipeline executa automaticamente a cada `push` ou `pull_request` na branch `main`.

**Jobs:**
1. `api-tests` — instala dependências e roda todos os testes de API com relatório HTML
2. `web-tests` — instala Chrome + dependências e roda os testes Selenium com relatório HTML

Os relatórios ficam disponíveis em **Actions → seu workflow → Artifacts**.

---

## 🖼️ Prints

> Adicione aqui prints da pipeline passando e dos testes rodando localmente após executar o projeto.

**Sugestão de prints para incluir:**
- Terminal com `pytest -v` mostrando todos os testes passando (API)
- Terminal com `pytest tests/ -v` mostrando os testes Web passando
- Tela do GitHub Actions com os dois jobs verdes ✅

---

## 🛠️ Tecnologias

| Tecnologia | Versão | Uso |
|---|---|---|
| Python | 3.11 | Linguagem base |
| Pytest | 8.2 | Framework de testes |
| Requests | 2.31 | Requisições HTTP (API) |
| Selenium | 4.21 | Automação Web |
| webdriver-manager | 4.0.1 | Gerencia o ChromeDriver |
| GitHub Actions | — | CI/CD |
