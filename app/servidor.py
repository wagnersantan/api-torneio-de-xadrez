from fastapi import FastAPI
from app.rotas.rotas_enxadrista import router as enxadrista_router

app = FastAPI(
    title="API Torneio de Xadrez",
    description="Gerencia enxadrista e seus papéis no torneio",
    version="1.0.0"
)

app.include_router(enxadrista_router, prefix="/api")
