# app/repositories/enxadrista_repository.py

from app.models.enxadrista_model import Enxadrista

# Banco de dados simulado (substitua com banco real quando necessário)
banco_enxadristas = []

def cadastrar_enxadrista(enxadrista: Enxadrista):
    banco_enxadristas.append(enxadrista)
    return enxadrista

def listar_enxadristas():
    return banco_enxadristas
