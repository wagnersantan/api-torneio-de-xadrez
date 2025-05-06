# app/routes/enxadrista_routes.py

from fastapi import APIRouter
from app.models.enxadrista_model import Enxadrista
from app.repositories.enxadrista_repository import cadastrar_enxadrista, listar_enxadristas

router = APIRouter()

@router.get('/')
def home():
    return {"mensagem": "Bem-vindo à API do Torneio de Xadrez!"}

@router.post("/jogador/")
def cadastrar_enxadrista_route(enxadrista: Enxadrista):
    # Chamando o repositório para cadastrar o enxadrista
    enxadrista_cadastrado = cadastrar_enxadrista(enxadrista)
    return {
        "mensagem": "Enxadrista cadastrado com sucesso!",
        "dados": enxadrista_cadastrado
    }

@router.get("/jogador/", response_model=list[Enxadrista])
def listar_enxadristas_route():
    # Chamando o repositório para listar os enxadristas
    return listar_enxadristas()

