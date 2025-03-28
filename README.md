# Testes de nivelamento

Este repositório contém a resolução de um conjunto de testes de nivelamento envolvendo **Web Scraping**, **Transformação de Dados**, **Banco de Dados** e **API com Vue.js e Python**..

---

## Estrutura do Projeto

| Desafio | Tema                                      | Status              | Pasta                            |
|---------|-------------------------------------------|---------------------|----------------------------------|
| 01      | Web Scraping                              | Completo | [teste_01_web_scraping](./teste_01_web_scraping) |
| 02      | Transformação de Dados (PDF → CSV)        | Completo          | [teste_02_transformacao_dados](./teste_02_transformacao_dados) |
| 03      | Banco de Dados (SQL + Dados Públicos)     | Completo          | [teste_03_banco_de_dados](./teste_03_banco_de_dados) |
| 04      | API + Interface Web (Vue.js + Python)     | Completo          | [teste_04_api_vue_python](./teste_04_api_vue_python) |

---

## Tecnologias Utilizadas

- **Python 3.x**
- **Requests**, **BeautifulSoup** – Web scraping
- **zipfile**, **os** – Manipulação de arquivos
- **Vue.js** – Interface Web
- **PostgreSQL / MySQL** – Banco de Dados
- **SQL** – Queries e estruturação
- **Postman** – Testes de API

---

## Como Executar esse projeto?

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio

```

### 2. Criar e ativar o ambiente virtual

#### Se estiver usando windows

```bash
python -m venv .venv
venv\Scripts\activate

```


#### Se estiver usando Linux ou Mac


```bash
python3 -m venv .venv
venv\Scripts\activate

```


### 3. Para instalar as dependências

```bash
pip install -r requirements.txt

```

### 4. Como executar as soluções? ( Usando o teste 01 como exemplo )

```bash
python teste_01_web_scraping/scraping.py

```




