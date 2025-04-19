from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from enum import Enum

# Inicializa a aplicação FastAPI
app = FastAPI()

# Enum para papéis possíveis
class PapelEnum(str, Enum):
    organizador = "organizador"
    enxadrista = "enxadrista"
    arbitragem = "arbitragem"

# Modelo de enxadrista
class Enxadrista(BaseModel):
    nome: str
    idade: int
    cidade: str
    rating: int
    papeis: List[PapelEnum]

banco_enxadristas: List[Enxadrista] = []

# Rota principal (home)
@app.get("/")
async def home():
    return {"mensagem": "Bem-vindo à API de Enxadristas!"}

# Rota para cadastrar enxadrista
@app.post("/jogador/")
async def cadastrar_enxadrista(enxadrista: Enxadrista):
    return {
        "mensagem": "Enxadrista cadastrado com sucesso!",
        "dados": enxadrista
    }
@app.get("/jogadores")
def listar_enxadristas():
    return banco_enxadristas


