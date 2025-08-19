from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/partidas", tags=["partidas"])

# --------------------------
# Modelos e Mocks
# --------------------------
class Partida(BaseModel):
    id: int
    torneio_id: int
    jogador_brancas: str
    jogador_negras: str
    resultado: str  # "1-0", "0-1", "0.5-0.5", etc.

partidas_mock = [
    Partida(id=1, torneio_id=1, jogador_brancas="Mauricio Fernandes", jogador_negras="Daniel Malta", resultado="1-0"),
    Partida(id=2, torneio_id=1, jogador_brancas="Daniel Malta", jogador_negras="João Silva", resultado="0.5-0.5")
]

# --------------------------
# Endpoints de partidas
# --------------------------

@router.get("/", response_model=List[Partida], summary="Listar todas as partidas")
def listar_partidas():
    return partidas_mock

@router.get("/{id}", response_model=Partida, summary="Detalhes da partida")
def detalhes_partida(id: int):
    for partida in partidas_mock:
        if partida.id == id:
            return partida
    raise HTTPException(status_code=404, detail="Partida não encontrada")

@router.post("/", response_model=Partida, status_code=status.HTTP_201_CREATED, summary="Criar nova partida")
def criar_partida(partida: Partida):
    partidas_mock.append(partida)
    return partida

@router.put("/{id}", response_model=Partida, summary="Atualizar resultado da partida")
def atualizar_partida(id: int, dados: Partida):
    for i, partida in enumerate(partidas_mock):
        if partida.id == id:
            partidas_mock[i] = dados
            return dados
    raise HTTPException(status_code=404, detail="Partida não encontrada")

# --------------------------
# Endpoints vinculados a torneio
# --------------------------
@router.get("/torneio/{torneio_id}", response_model=List[Partida], summary="Listar partidas de um torneio")
def partidas_torneio(torneio_id: int):
    torneio_partidas = [p for p in partidas_mock if p.torneio_id == torneio_id]
    if not torneio_partidas:
        raise HTTPException(status_code=404, detail="Nenhuma partida encontrada para este torneio")
    return torneio_partidas
