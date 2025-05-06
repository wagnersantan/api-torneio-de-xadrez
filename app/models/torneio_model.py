from pydantic import BaseModel
from datetime import date

class Torneio(BaseModel):
    nome: str
    data_inicio: date
    data_fim: date
    local: str
    status: str  # Ex: "agendado", "em andamento", "finalizado"