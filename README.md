
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

A arquitetura do projeto foi organizada de forma modular para fácil manutenção e escalabilidade. A estrutura de diretórios é a seguinte:

```
api-torneio-de-xadrez/
├── app/
│   ├── __init__.py               # Arquivo de inicialização
│   ├── models/                   # Modelos de dados
│   ├── schemas/                  # Schemas Pydantic para validação de dados
│   ├── rotas/                    # Endpoints da API
│   │   ├── jogador.py            # Endpoints para jogadores
│   │   └── torneio.py            # Endpoints para torneios
│   ├── banco_simulado.py         # Banco de dados simulado (para testes e desenvolvimento)
│   ├── servidor.py               # Arquivo de inicialização da aplicação FastAPI
├── venv/                         # Ambiente virtual com dependências
└── requirements.txt              # Dependências do projeto
```

---

## Como Rodar a Aplicação

### Requisitos

- Python 3.7+
- Uvicorn
- FastAPI

### Passo a Passo para Instalação

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/wagnersantan/api-torneio-de-xadrez.git
   cd api-torneio-de-xadrez
   ```

2. **Crie um ambiente virtual**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows, use: venv\Scripts\activate
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie o servidor**:

   ```bash
   uvicorn app.servidor:app --reload
   ```

   O servidor estará rodando em [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Testando a API

Você pode testar os endpoints da API de forma interativa através da documentação gerada automaticamente pelo **FastAPI**:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Testes

Para rodar os testes automatizados, utilize o framework **pytest**. Execute o seguinte comando:

```bash
pytest
```

---

## Licença

Distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais informações.

---

## Contribuição

Contribuições são bem-vindas! Para sugerir melhorias ou corrigir problemas, por favor, siga as instruções abaixo:

1. Faça o **fork** do repositório.
2. Crie uma **branch** para a sua modificação.
3. Envie um **pull request** explicando as mudanças realizadas.

---

**Desenvolvido por**: Wagner Santana
