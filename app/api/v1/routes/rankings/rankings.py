from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/rankings", tags=["rankings"])

# --------------------------
# Modelos e Mocks
# --------------------------
class RankingItem(BaseModel):
    jogador: str
    rating: int
    categoria: str
    torneio_id: int = None  # opcional, se for ranking de torneio

ranking_mock = [
    {"jogador": "Mauricio Fernandes", "rating": 2850, "categoria": "Adulto", "torneio_id": 1},
    {"jogador": "Daniel Malta", "rating": 2840, "categoria": "Adulto", "torneio_id": 1},
    {"jogador": "João Silva", "rating": 1500, "categoria": "Infantil", "torneio_id": 2}
]

# --------------------------
# Endpoints de ranking
# --------------------------
@router.get("/geral", response_model=List[RankingItem], summary="Ranking geral")
def ranking_geral():
    ranking = sorted(ranking_mock, key=lambda x: x["rating"], reverse=True)
    return ranking

@router.get("/categoria/{categoria}", response_model=List[RankingItem], summary="Ranking por categoria")
def ranking_categoria(categoria: str):
    ranking = sorted([r for r in ranking_mock if r["categoria"] == categoria], key=lambda x: x["rating"], reverse=True)
    return ranking

@router.get("/torneio/{torneio_id}", response_model=List[RankingItem], summary="Ranking de um torneio específico")
def ranking_torneio(torneio_id: int):
    ranking = sorted([r for r in ranking_mock if r["torneio_id"] == torneio_id], key=lambda x: x["rating"], reverse=True)
    return ranking
