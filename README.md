#  Test Automation — Petstore API + SauceDemo Web

Este projeto foi desenvolvido para a disciplina de **Teste e Qualidade de Software** no **5º período de Engenharia de Software**. O objetivo central é demonstrar uma solução de automação robusta que integra testes de contrato (API) e interface (Web) em um pipeline de CI/CD via GitHub Actions.

A arquitetura do projeto reflete os princípios da **Pirâmide de Testes**, onde a separação das camadas garante que cada nível detecte falhas específicas de forma complementar e eficiente, simulando os desafios reais de garantia de qualidade em aplicações modernas.

| Camada | Ferramenta | Alvo |
|--------|-----------|------|
| API    | Python + Requests + Pytest | Petstore Swagger |
| Web    | Python + Selenium + Pytest | SauceDemo |
| CI/CD  | GitHub Actions | Fluxo Automatizado |

## Decisões Técnicas
**Pytest + Requests (API):** A biblioteca requests permite validar contratos HTTP de forma leve e sem overhead. O uso de fixtures do Pytest com ciclo de vida claro (yield) garante o setup e teardown dos dados, evitando o acoplamento entre os cenários de teste.

**Selenium + Page Object Model (Web):** O Selenium foi escolhido por ser o padrão da indústria, contando com gerenciamento automático de drivers. Aplicamos o padrão Page Object Model (POM) para desacoplar a localização de elementos da lógica de teste, facilitando a manutenção caso a interface mude.

**Pipeline com Jobs Separados:** Os testes de API e Web possuem perfis de execução distintos. A separação em jobs independentes no GitHub Actions permite identificar rapidamente qual camada falhou e facilita a implementação de paralelismo, tornando o feedback do CI mais ágil.

---

##  Estrutura do Projeto

```
test-automation/
├── .github/
│   └── workflows/
│       └── ci.yml
├── api-tests/
│   ├── test_pet.py
│   ├── test_store.py
│   ├── test_user.py
│   └── requirements.txt
├── web-tests/
│   ├── pages/
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   ├── tests/
│   │   └── test_saucedemo.py
│   ├── conftest.py
│   └── requirements.txt
├── .gitignore
└── README.md
```

---

##  Pré-requisitos

- Python 3.10+
- Google Chrome 
- Git 

---

##  Instalação e Execução Local

### 1. Clone o repositório

```bash
git clone https://github.com/luizacoelh/test-automation.git
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

> O `webdriver-manager` instala o ChromeDriver automaticamente. 

---

##  Cenários Testados

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
- Login com credenciais inválidas e validação da mensagem de erro
- Adicionar produto ao carrinho com verificação do contador
- **Fluxo E2E completo:** login → seleção de 2 produtos → ir ao carrinho → preenchimento de dados → finalizar compra →  confirmação do pedido 

---

##  Padrões e Conceitos Aplicados

- **Page Object Model (POM):** cada página da aplicação tem sua própria classe, separando a lógica de localização de elementos dos testes, facilitando muito a manutenção.
- **Fixtures (pytest):** setup/teardown de dados de teste isolados por cenário.
- **Headless Chrome:** execução sem interface gráfica, compatível com CI.

---

##  Pipeline CI/CD (GitHub Actions)

A pipeline executa automaticamente a cada `push` ou `pull_request` na branch `main`, com dois jobs independentes:

**Jobs:**
1. `api-tests` — instala dependências e roda todos os testes de API com relatório HTML
2. `web-tests` — instala Chrome + dependências e roda os testes Selenium com relatório HTML

Os relatórios ficam disponíveis como artefatos em cada execução do workflow no GitHub Actions.

---

## Evidências de Execução


**💻 Execução Local**

#### **API** 
|**CMD**| **report.html**|
|--------|-----------|
|  (<img width="1405" height="673" alt="image" src="https://github.com/user-attachments/assets/57028204-f19d-4710-a03f-88881d5f57dc" /> |   <img width="1833" height="871" alt="image" src="https://github.com/user-attachments/assets/2012d419-80d4-475b-91d7-bed9deef0cdf" />|

### **Web** 
|**CMD** | **report.html** | 
|--------|-----------|
| <img width="1693" height="839" alt="image" src="https://github.com/user-attachments/assets/95a4a8bd-7a7d-4deb-a722-fb9a5428d678" /> |  <img width="1865" height="879" alt="image" src="https://github.com/user-attachments/assets/e22adcb0-d12e-4173-b88b-6f3590faa954" /> |

### **☁️ CI/CD - GitHub Actions (Artefatos):** 

| Api | Web |
|--------|-----------|
|<img width="1840" height="862" alt="image" src="https://github.com/user-attachments/assets/055afba6-b0cb-42d6-9a56-f952d74b9427" />|<img width="1862" height="732" alt="image" src="https://github.com/user-attachments/assets/ebbb6323-0f11-4955-bb52-d26de627e542" />|



---

##  Tecnologias

| Tecnologia | Versão | Uso |
|---|---|---|
| Python | 3.11 | Linguagem base |
| Pytest | 8.2 | Framework de testes |
| Requests | 2.31 | Requisições HTTP (API) |
| Selenium | 4.21 | Automação Web |
| webdriver-manager | 4.0.1 | Gerencia o ChromeDriver |
| GitHub Actions | — | CI/CD |
