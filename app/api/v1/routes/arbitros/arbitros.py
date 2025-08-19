from fastapi import APIRouter, status
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/arbitros", tags=["arbitros"])

# --------------------------
# Modelos e Mocks
# --------------------------
class Arbitro(BaseModel):
    id: int
    nome: str
    nivel: str  # Ex: "Nacional", "Regional", "Local"

arbitros_mock = [
    Arbitro(id=1, nome="Carlos Pereira", nivel="Nacional"),
    Arbitro(id=2, nome="Ana Souza", nivel="Regional")
]

# --------------------------
# Endpoints
# --------------------------
@router.get("/", response_model=List[Arbitro], summary="Listar árbitros")
def listar_arbitros():
    return arbitros_mock

@router.post("/", response_model=Arbitro, status_code=status.HTTP_201_CREATED, summary="Cadastrar árbitro")
def cadastrar_arbitro(arbitro: Arbitro):
    arbitros_mock.append(arbitro)
    return arbitro


