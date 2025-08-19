from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/torneios", tags=["torneios"])

# --------------------------
# Modelos e Mocks
# --------------------------
class Torneio(BaseModel):
    id: int
    nome: str
    categoria: str
    status: str  # "aberto", "em_andamento", "finalizado"

class Jogador(BaseModel):
    id: int
    nome: str

torneios_mock = [
    Torneio(id=1, nome="Torneio Primavera", categoria="Adulto", status="aberto"),
    Torneio(id=2, nome="Torneio Verão", categoria="Infantil", status="aberto")
]

inscricoes_mock = {
    1: [Jogador(id=1, nome="Mauricio Fernandes"), Jogador(id=2, nome="Daniel Malta")],
    2: []
}

partidas_mock = {
    1: [{"id": 1, "jogador_brancas": "Mauricio Fernandes", "jogador_negras": "Daniel Malta", "resultado": "1-0"}],
    2: []
}

class Partida(BaseModel):
    id: int
    jogador_brancas: str
    jogador_negras: str
    resultado: str

# --------------------------
# Endpoints principais
# --------------------------
@router.get("/", response_model=List[Torneio], summary="Listar todos os torneios")
def listar_torneios():
    return torneios_mock

@router.get("/{id}", response_model=Torneio, summary="Buscar torneio específico")
def buscar_torneio(id: int):
    for torneio in torneios_mock:
        if torneio.id == id:
            return torneio
    raise HTTPException(status_code=404, detail="Torneio não encontrado")

@router.post("/", response_model=Torneio, status_code=status.HTTP_201_CREATED, summary="Criar novo torneio")
def criar_torneio(torneio: Torneio):
    torneios_mock.append(torneio)
    inscricoes_mock[torneio.id] = []
    partidas_mock[torneio.id] = []
    return torneio

@router.put("/{id}", response_model=Torneio, summary="Atualizar torneio")
def atualizar_torneio(id: int, dados: Torneio):
    for i, torneio in enumerate(torneios_mock):
        if torneio.id == id:
            torneios_mock[i] = dados
            return dados
    raise HTTPException(status_code=404, detail="Torneio não encontrado")

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, summary="Excluir torneio")
def excluir_torneio(id: int):
    for i, torneio in enumerate(torneios_mock):
        if torneio.id == id:
            torneios_mock.pop(i)
            inscricoes_mock.pop(id, None)
            partidas_mock.pop(id, None)
            return
    raise HTTPException(status_code=404, detail="Torneio não encontrado")

# --------------------------
# Endpoints de inscrições
# --------------------------
@router.post("/{id}/inscrever", summary="Inscrever jogador no torneio")
def inscrever_jogador(id: int, jogador: Jogador):
    if id not in inscricoes_mock:
        raise HTTPException(status_code=404, detail="Torneio não encontrado")
    inscricoes_mock[id].append(jogador)
    return {"mensagem": f"Jogador {jogador.nome} inscrito com sucesso!"}

@router.delete("/{id}/jogadores/{jogador_id}", summary="Remover jogador do torneio")
def remover_jogador(id: int, jogador_id: int):
    if id not in inscricoes_mock:
        raise HTTPException(status_code=404, detail="Torneio não encontrado")
    inscricoes_mock[id] = [j for j in inscricoes_mock[id] if j.id != jogador_id]
    return {"mensagem": f"Jogador {jogador_id} removido do torneio"}

@router.get("/{id}/jogadores", summary="Listar jogadores inscritos")
def listar_jogadores(id: int):
    if id not in inscricoes_mock:
        raise HTTPException(status_code=404, detail="Torneio não encontrado")
    return inscricoes_mock[id]

# --------------------------
# Endpoints de status
# --------------------------
@router.post("/{id}/iniciar", summary="Iniciar torneio")
def iniciar_torneio(id: int):
    for torneio in torneios_mock:
        if torneio.id == id:
            torneio.status = "em_andamento"
            return {"mensagem": f"Torneio {torneio.nome} iniciado!"}
    raise HTTPException(status_code=404, detail="Torneio não encontrado")

@router.post("/{id}/finalizar", summary="Finalizar torneio")
def finalizar_torneio(id: int):
    for torneio in torneios_mock:
        if torneio.id == id:
            torneio.status = "finalizado"
            return {"mensagem": f"Torneio {torneio.nome} finalizado!"}
    raise HTTPException(status_code=404, detail="Torneio não encontrado")

@router.get("/{id}/classificacao", summary="Tabela de classificação (simulada)")
def classificacao_torneio(id: int):
    if id not in partidas_mock:
        raise HTTPException(status_code=404, detail="Torneio não encontrado")
    # Simulação: retorna lista de jogadores e rating
    return [{"jogador": j.nome, "rating": 2850-i*10} for i, j in enumerate(inscricoes_mock[id])]

# --------------------------
# Endpoints de partidas
# --------------------------
@router.get("/{id}/partidas", summary="Listar partidas de um torneio")
def listar_partidas_torneio(id: int):
    if id not in partidas_mock:
        raise HTTPException(status_code=404, detail="Torneio não encontrado")
    return partidas_mock[id]

@router.get("/{id}/rodadas", summary="Listar rodadas do torneio (simulado)")
def listar_rodadas(id: int):
    if id not in partidas_mock:
        raise HTTPException(status_code=404, detail="Torneio não encontrado")
    # Simulação: retorna rodadas já jogadas
    return [{"rodada": 1, "partidas": partidas_mock[id]}]

@router.post("/{id}/gerar-rodada", summary="Gerar próxima rodada (simulado)")
def gerar_rodada(id: int):
    if id not in partidas_mock:
        raise HTTPException(status_code=404, detail="Torneio não encontrado")
    # Simulação: adiciona partida fictícia
    nova_partida = {"id": len(partidas_mock[id])+1, "jogador_brancas": "Jogador A", "jogador_negras": "Jogador B", "resultado": "0-0"}
    partidas_mock[id].append(nova_partida)
    return {"mensagem": "Rodada gerada com sucesso!", "partida": nova_partida}
