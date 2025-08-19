from fastapi import APIRouter

router = APIRouter(prefix="/pontuacao", tags=["pontuacao"])

# --------------------------
# Endpoints de pontuação
# --------------------------
@router.post("/calcular/{torneio_id}", summary="Recalcular pontuação de um torneio")
def recalcular_pontuacao(torneio_id: int):
    # Aqui você pode adicionar a lógica real de cálculo futuramente
    return {"mensagem": f"Pontuação do torneio {torneio_id} recalculada com sucesso (simulado)!"}

