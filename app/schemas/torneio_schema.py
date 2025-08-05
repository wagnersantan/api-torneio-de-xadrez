from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID
from datetime import date


class TorneioBase(BaseModel):
    nome: str = Field(..., example="Torneio Aberto de Verão")
    local: str = Field(..., example="Salvador")
    data: date = Field(..., example="2025-09-10")
    descricao: Optional[str] = Field(default=None, example="Evento oficial da Federação")


class TorneioCreate(TorneioBase):
    pass


class TorneioUpdate(TorneioBase):
    pass


class TorneioResponse(TorneioBase):
    id: UUID
    participantes: Optional[List[UUID]] = []

    class Config:
        orm_mode = True
