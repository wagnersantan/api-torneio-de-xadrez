
# API de Enxadristas

Esta é uma **API RESTful** para organizar e gerenciar torneios de xadrez. A API foi construída com **FastAPI** e permite o registro de jogadores, exibição dos dados e gestão das entidades no torneio.

## Funcionalidades
- **POST /jogador/**: Registra novos jogadores no sistema.
- **GET /jogadores/**: Lista todos os jogadores cadastrados.
- **POST /jogador/{id}/atualizar/**: Atualiza informações de um jogador.
- **GET /jogador/{id}**: Recupera informações de um jogador específico.

## Como rodar a aplicação
### Requisitos
- Python 3.7+
- Uvicorn
- FastAPI

### Instalação
Clone o repositório:

```bash
git clone https://github.com/wagnersantan/api-enxadristas.git
cd api-enxadristas

