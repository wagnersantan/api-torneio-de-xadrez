from pydantic import BaseModel 
from enum import Enum 
from typing import List

class PapelEnum(str, Enum):
    organizador = "organizador"
    arbitro = "arbitro"
    competidor = "competidor"

class Enxadrista(BaseModel):
    nome: str
    idade: int
    cidade: int
    papeis: List[PapelEnum]
