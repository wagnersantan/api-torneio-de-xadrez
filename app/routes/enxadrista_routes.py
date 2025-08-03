from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Modelo simplificado para teste (copie o que usar no seu modelo real)
class Enxadrista(BaseModel):
    nome: str
    categoria: str
    rating: int

# Dados simulados em memória
enxadristas_mock = [
    Enxadrista(nome="Magnus Carlsen", categoria="Adulto", rating=2850),
    Enxadrista(nome="Hikaru Nakamura", categoria="Adulto", rating=2750),
]

@router.get('/')
def home():
    return {"mensagem": "Bem-vindo à API do Torneio de Xadrez!"}

@router.post("/jogador/")
def cadastrar_enxadrista_route(enxadrista: Enxadrista):
    # Só retorna o que recebeu sem salvar, simulando cadastro
    return {
        "mensagem": "Enxadrista cadastrado com sucesso (simulado)!",
        "dados": enxadrista
    }

@router.get("/jogador/", response_model=list[Enxadrista])
def listar_enxadristas_route():
    # Retorna a lista mockada
    return enxadristas_mock
