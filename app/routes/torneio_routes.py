from fastapi import APIRouter
from app.models.torneio_model import Torneio
from app.repositories.torneio_repository import cadastrar_torneio, listar_torneios

router = APIRouter()

@router.post("/")
def criar_torneio(torneio: Torneio):
    torneio_cadastrado = cadastrar_torneio(torneio)
    return {"mensagem": "Torneio cadastrado com sucesso", "dados": torneio_cadastrado}

@router.get("/")
def obter_torneios():
    torneios = listar_torneios()
    return {"torneios": torneios}


