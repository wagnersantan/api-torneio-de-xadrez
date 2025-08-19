# API de Torneio de Xadrez

Esta é uma **API RESTful** construída com **FastAPI** para organizar e gerenciar torneios de xadrez. A API permite o registro de jogadores, a exibição de dados dos torneios, além da gestão de jogadores, árbitros e organizadores.


---

## Funcionalidades

- **POST /jogador/**: Registra um novo jogador no sistema.
- **GET /jogadores/**: Lista todos os jogadores cadastrados.
- **POST /jogador/{id}/atualizar/**: Atualiza as informações de um jogador.
- **GET /jogador/{id}**: Recupera as informações de um jogador específico.
- **POST /login/**: Realiza o login de um usuário (organizador, árbitro ou jogador) com autenticação JWT.
- **GET /torneios/**: Lista todos os torneios cadastrados.
- **POST /torneio/**: Cria um novo torneio de xadrez.

---

## Estrutura do Projeto

api-torneio-de-xadrez/
├── LICENSE
├── README.md
├── app/
│ ├── init.py
│ ├── core/
│ │ └── config.py
│ ├── database/
│ │ └── connection.py
│ ├── models/
│ │ ├── enxadrista_model.py
│ │ ├── torneio_model.py
│ │ └── torneio_model_sqlalchemy.py
│ ├── repositories/
│ │ ├── enxadrista_repository.py
│ │ └── torneio_repository.py
│ ├── schemas/
│ │ ├── auth_schema.py
│ │ ├── enxadrista_schema.py
│ │ └── torneio_schema.py
│ ├── services/
│ │ ├── enxadrista_service.py
│ │ └── torneio_service.py
│ ├── routes/
│ │ ├── enxadrista_routes.py
│ │ └── torneio_routes.py
│ └── utils/
│ └── helpers.py
├── chess.db
├── create_tables.py
├── main.py
├── requirements.txt
├── tests/
│ ├── init.py
│ ├── conftest.py
│ └── test_main.py
└── venv/


---

## Requisitos

- Python 3.7+
- Uvicorn
- FastAPI
- MongoDB (opcional, para testes simulados)
- SQLAlchemy (para persistência com SQLite)

---

## Como Rodar a Aplicação

### 1. Clonar o repositório
```bash
git clone https://github.com/wagnersantan/api-torneio-de-xadrez.git
cd api-torneio-de-xadrez

. Criar ambiente virtual

python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

. Instalar dependências

pip install -r requirements.txt

. Modo de execução
 Com SQLite/SQLAlchemy (produção)
Verifique se o arquivo chess.db existe ou rode o script:

python create_tables.py

Execute a API:

uvicorn main:app --reload

Modo simulado com MongoDB (para testes rápidos)
Comente ou remova as partes do código que fazem conexão real com o MongoDB (ex.: no main.py ou funções de teste).

Execute:uvicorn main:app --reload

Testando a API
Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

Testes Automatizados

pytest

1. Faça o **fork** do repositório.
2. Crie uma **branch** para a sua modificação.
3. Envie um **pull request** explicando as mudanças realizadas.

---

**Desenvolvido por**: Wagner Santana


