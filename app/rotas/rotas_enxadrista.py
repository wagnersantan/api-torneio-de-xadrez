from fastapi import APIRouter
from typing import List
from app.models.modelo_enxadrista import Enxadrista
from app.dados.banco_simulado import banco_enxadristas

router = APIRouter()

@router.get('/')
def home():
    return {"mensagem": "Bem-vindo à API do Torneio de Xadrez!"}

@router.post("/jogador/")
def cadastrar_enxadrista(enxadrista: Enxadrista):
    banco_enxadristas.append(enxadrista)
    return {
        "mensagem": "Enxadrista cadastrado com sucesso!",
        "dados": enxadrista  # Aqui deve ser enxadrista, o parâmetro da função
    }

@router.get("/jogador/", response_model=List[Enxadrista])
def listar_enxadristas():
    return banco_enxadristas
