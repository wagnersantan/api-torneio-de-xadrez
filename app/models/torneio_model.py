from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class StatusTorneio(str, Enum):
    ABERTO = "aberto"
    ENCERRADO = "encerrado"
    EM_ANDAMENTO = "em_andamnto"

class Torneio(BaseModel):
    nome: str
    status: StatusTorneio
    data_inicio: datetime
    data_fim: datetime
    local: str
    
