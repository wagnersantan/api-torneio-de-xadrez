from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional

class StatusTorneioEnum(str, Enum):
    ABERTO = "aberto"
    ENCERRADO = "encerrado"
    EM_ANDAMENTO = "em_andamento"

class TorneioBase(BaseModel):
    nome: str
    status: StatusTorneioEnum
    data_inicio: datetime
    data_fim: datetime
    local: str

class TorneioCreate(TorneioBase):
    pass

class TorneioRead(TorneioBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2 substitui orm_mode
