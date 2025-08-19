from fastapi import FastAPI
from app.api.v1.routes.enxadistas import router as enxadrista_routes
from app.api.v1.routes.torneios.torneios import router as torneio_routes
from app.api.v1.routes.partidas import router as partidas_routes
from app.api.v1.routes.rankings import router as rankings_routes
from app.api.v1.routes.pontuacao import router as pontuacao_routes
from app.api.v1.routes.arbitros import router as arbitros_routes
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.get("/")
def read_root():
    return {"message": f"{settings.PROJECT_NAME} funcionando sem banco (modo simulado)"}

# 👉 Aqui é onde controlamos os prefixos e tags
app.include_router(enxadrista_routes, prefix=f"{settings.API_PREFIX}/enxadrista", tags=["Enxadristas"])
app.include_router(torneio_routes, prefix=f"{settings.API_PREFIX}/torneios", tags=["Torneios"])
app.include_router(partidas_routes, prefix=f"{settings.API_PREFIX}/partidas", tags=["Partidas"])
app.include_router(rankings_routes, prefix=f"{settings.API_PREFIX}/rankings", tags=["Rankings"])
app.include_router(pontuacao_routes, prefix=f"{settings.API_PREFIX}/pontuacao", tags=["Pontuação"])
app.include_router(arbitros_routes, prefix=f"{settings.API_PREFIX}/arbitros", tags=["Árbitros"])


