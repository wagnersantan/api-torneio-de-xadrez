from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Torneio(BaseModel):
    nome: str
    local: str
    data: str

# Dados mockados
torneios_mock = [
    Torneio(nome="Torneio ABC", local="São Paulo", data="2025-08-15"),
    Torneio(nome="Copa XYZ", local="Rio de Janeiro", data="2025-09-01"),
]

@router.post("/")
def criar_torneio(torneio: Torneio):
    # Só retorna o que recebeu, simulando cadastro
    return {
        "mensagem": "Torneio cadastrado com sucesso (simulado)!",
        "dados": torneio
    }

@router.get("/")
def obter_torneios():
    return {"torneios": torneios_mock}
