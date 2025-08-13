from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter()

class Enxadrista(BaseModel):
    nome: str
    categoria: str
    rating: int

enxadristas_mock = [
    Enxadrista(nome="Mauricio Fernandes", categoria="Adulto", rating=2850),
    Enxadrista(nome="Daniel Malta", categoria="Adulto", rating=2840),
]

@router.get("/", summary="Mensagem de boas-vindas")
def home():
    return {"mensagem": "Bem-vindo à API do Torneio de Xadrez!"}

@router.post("/jogador/", status_code=status.HTTP_201_CREATED, summary="Cadastrar um enxadrista")
def cadastrar_enxadrista_route(enxadrista: Enxadrista):
    # Aqui você pode futuramente salvar no banco
    return {
        "mensagem": "Enxadrista cadastrado com sucesso (simulado)!",
        "dados": enxadrista
    }

@router.get("/jogador/", response_model=list[Enxadrista], summary="Listar enxadristas")
def listar_enxadristas_route():
    return enxadristas_mock
