from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List

# 👉 Agora o router não tem prefixo nem tags, isso será controlado pelo main.py
router = APIRouter()

# --------------------------
# Modelos e Mocks
# --------------------------
class Enxadrista(BaseModel):
    id: int
    nome: str
    categoria: str
    rating: int

enxadristas_mock = [
    Enxadrista(id=1, nome="Mauricio Fernandes", categoria="Adulto", rating=2850),
    Enxadrista(id=2, nome="Daniel Malta", categoria="Adulto", rating=2840),
]

# Mock histórico e estatísticas
historico_mock = {
    1: ["Vitória contra Daniel Malta", "Derrota contra João Silva"],
    2: ["Vitória contra João Silva", "Derrota contra Mauricio Fernandes"]
}

estatisticas_mock = {
    1: {"vitorias": 1, "derrotas": 1, "empates": 0},
    2: {"vitorias": 1, "derrotas": 1, "empates": 0}
}

# --------------------------
# Endpoints existentes
# --------------------------
@router.get("/", summary="Mensagem de boas-vindas")
def home():
    return {"mensagem": "Bem-vindo à API do Torneio de Xadrez!"}

@router.post("/jogador/", status_code=status.HTTP_201_CREATED, summary="Cadastrar um enxadrista")
def cadastrar_enxadrista_route(enxadrista: Enxadrista):
    enxadristas_mock.append(enxadrista)
    return {
        "mensagem": "Enxadrista cadastrado com sucesso (simulado)!",
        "dados": enxadrista
    }

@router.get("/jogador/", response_model=List[Enxadrista], summary="Listar enxadristas")
def listar_enxadristas_route():
    return enxadristas_mock

# --------------------------
# Novos Endpoints
# --------------------------
@router.get("/jogador/{id}", response_model=Enxadrista, summary="Buscar jogador específico")
def buscar_jogador(id: int):
    for jogador in enxadristas_mock:
        if jogador.id == id:
            return jogador
    raise HTTPException(status_code=404, detail="Jogador não encontrado")

@router.put("/jogador/{id}", response_model=Enxadrista, summary="Atualizar dados do jogador")
def atualizar_jogador(id: int, dados: Enxadrista):
    for i, jogador in enumerate(enxadristas_mock):
        if jogador.id == id:
            enxadristas_mock[i] = dados
            return dados
    raise HTTPException(status_code=404, detail="Jogador não encontrado")

@router.delete("/jogador/{id}", status_code=status.HTTP_204_NO_CONTENT, summary="Excluir jogador")
def excluir_jogador(id: int):
    for i, jogador in enumerate(enxadristas_mock):
        if jogador.id == id:
            enxadristas_mock.pop(i)
            return
    raise HTTPException(status_code=404, detail="Jogador não encontrado")

@router.get("/jogador/{id}/historico", summary="Histórico de partidas do jogador")
def historico_jogador(id: int):
    if id in historico_mock:
        return {"historico": historico_mock[id]}
    raise HTTPException(status_code=404, detail="Histórico não encontrado")

@router.get("/jogador/{id}/estatisticas", summary="Estatísticas do jogador")
def estatisticas_jogador(id: int):
    if id in estatisticas_mock:
        return {"estatisticas": estatisticas_mock[id]}
    raise HTTPException(status_code=404, detail="Estatísticas não encontradas")

@router.get("/ranking", summary="Ranking geral de jogadores")
def ranking_geral():
    ranking = sorted(enxadristas_mock, key=lambda x: x.rating, reverse=True)
    return ranking
